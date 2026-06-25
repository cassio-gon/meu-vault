"""Sumarização com Google Gemini (free tier): gera N tópicos do dia.

Usa a API REST do Gemini (generativelanguage) via stdlib (sem dependências extras).
A saída é forçada a JSON estruturado via `responseSchema`, então não há reparo
manual de JSON — o modelo devolve um array válido no formato esperado.
"""
from __future__ import annotations

import json
import os
import random
import time
import urllib.error
import urllib.request

from scraper import ScrapedDoc

GEMINI_API_BASE = "https://generativelanguage.googleapis.com/v1beta/models"

# Cadeia de modelos: tenta o primeiro; se esgotar retries com erro
# transitório ou de cota, cai para o próximo.
# `GEMINI_MODEL` (env), se setado, entra como primário.
# Ambos são elegíveis ao free tier (1.500 req/dia, 1M TPM, 15 RPM no flash).
_DEFAULT_CHAIN = ["gemini-2.5-flash", "gemini-2.5-flash-lite"]
_env_model = os.environ.get("GEMINI_MODEL")
MODELS = (
    [_env_model] + [m for m in _DEFAULT_CHAIN if m != _env_model]
    if _env_model
    else list(_DEFAULT_CHAIN)
)

MAX_CHARS_PER_SOURCE = 3000   # limita chars por fonte (~750 tokens)
MAX_TOTAL_CONTEXT_CHARS = 24_000  # teto do bloco de contexto (~6000 tokens)
NUM_TOPICS = 5

MAX_RETRIES = 5
RETRYABLE = {429, 500, 502, 503, 504}
BACKOFF_BASE = 2.0  # segundos: 2 → 4 → 8 → 16 → 32 (+jitter), com teto
BACKOFF_CAP = 60.0


def _backoff_seconds(attempt: int) -> float:
    """Espera exponencial (base 2) com teto e jitter aleatório de até 1s."""
    delay = min(BACKOFF_CAP, BACKOFF_BASE * 2 ** (attempt - 1))
    return delay + random.uniform(0, 1)


def _topics_schema(categories: list[str]) -> dict:
    """Monta o responseSchema (subset OpenAPI do Gemini) para o array de tópicos."""
    return {
        "type": "ARRAY",
        "items": {
            "type": "OBJECT",
            "properties": {
                "title": {"type": "STRING"},
                "summary": {"type": "STRING"},
                "url": {"type": "STRING"},
                "category": {"type": "STRING", "enum": categories},
                "date": {"type": "STRING"},
                "image_url": {"type": "STRING"},
            },
            "required": ["title", "summary", "url", "category", "date", "image_url"],
            "propertyOrdering": ["title", "summary", "url", "category", "date", "image_url"],
        },
    }


def _call_gemini(
    api_key: str, prompt: str, schema: dict, max_tokens: int = 8192
) -> list[dict]:
    """Chama a API do Gemini com saída JSON estruturada e devolve a lista de tópicos.

    `thinkingBudget: 0` desliga o raciocínio interno do modelo — desnecessário para
    extração estruturada e que, se ligado, consome o orçamento de saída e trunca o JSON.
    """
    last_err: Exception | None = None
    body = json.dumps(
        {
            "contents": [{"role": "user", "parts": [{"text": prompt}]}],
            "generationConfig": {
                "temperature": 0.4,
                "maxOutputTokens": max_tokens,
                "responseMimeType": "application/json",
                "responseSchema": schema,
                "thinkingConfig": {"thinkingBudget": 0},
            },
        }
    ).encode("utf-8")

    for mi, model in enumerate(MODELS):
        url = f"{GEMINI_API_BASE}/{model}:generateContent"
        print(f"   ↳ modelo: {model}")
        for attempt in range(1, MAX_RETRIES + 1):
            req = urllib.request.Request(
                url,
                data=body,
                headers={
                    "Content-Type": "application/json",
                    "x-goog-api-key": api_key,
                    "Accept": "application/json",
                },
                method="POST",
            )
            try:
                with urllib.request.urlopen(req, timeout=120) as resp:
                    data = json.load(resp)
                candidates = data.get("candidates", [])
                if not candidates:
                    # promptFeedback.blockReason indica bloqueio por safety
                    reason = data.get("promptFeedback", {}).get("blockReason", "?")
                    raise RuntimeError(f"Gemini não retornou candidates (blockReason={reason})")
                cand = candidates[0]
                finish = cand.get("finishReason", "")
                parts = cand.get("content", {}).get("parts", [])
                text = "".join(p.get("text", "") for p in parts).strip()
                if not text:
                    last_err = RuntimeError(f"Gemini retornou content vazio (finishReason={finish})")
                    wait = _backoff_seconds(attempt)
                    print(f"⚠️  {last_err}; aguardando {wait:.1f}s...")
                    if attempt < MAX_RETRIES:
                        time.sleep(wait)
                    continue
                if finish == "MAX_TOKENS":
                    raise RuntimeError(
                        "Gemini truncou a saída (MAX_TOKENS) — aumente maxOutputTokens"
                    )
                # Com responseSchema a resposta é JSON válido; sem reparo manual.
                return json.loads(text)
            except urllib.error.HTTPError as err:
                detail = err.read().decode("utf-8", "ignore")[:300]
                last_err = RuntimeError(f"Gemini HTTP {err.code}: {detail}")
                if err.code not in RETRYABLE:
                    raise last_err from err
                retry_after = 0.0
                try:
                    retry_after = float(err.headers.get("retry-after") or 0)
                except (TypeError, ValueError):
                    pass
                wait = max(_backoff_seconds(attempt), retry_after) + random.uniform(0, 2)
                print(f"⚠️  {model} HTTP {err.code} (tentativa {attempt}/{MAX_RETRIES}); aguardando {wait:.1f}s...")
            except urllib.error.URLError as err:
                last_err = RuntimeError(f"Erro de rede: {err}")
                wait = _backoff_seconds(attempt)
                print(f"⚠️  Rede falhou em {model} (tentativa {attempt}/{MAX_RETRIES}); aguardando {wait:.1f}s...")
            except json.JSONDecodeError as err:
                last_err = RuntimeError(f"JSON inválido do Gemini: {err}")
                wait = _backoff_seconds(attempt)
                print(f"⚠️  {last_err}; aguardando {wait:.1f}s...")
            if attempt < MAX_RETRIES:
                time.sleep(wait)
        if mi < len(MODELS) - 1:
            print(f"↪️  {model} indisponível; tentando próximo modelo...")
    raise RuntimeError(f"Todos os modelos Gemini falharam ({', '.join(MODELS)})") from last_err


# Perfis de prompt por área do digest. Cada área enquadra o resumo no seu domínio.
DEFAULT_PROFILE = {
    "role": "editor de tecnologia especializado em IA",
    "focus": (
        "notícias e ferramentas de IA (priorize o que realmente importa: lançamentos, "
        "rodadas de investimento, modelos novos, ferramentas relevantes)"
    ),
    "categories": ["noticia", "ferramenta"],
}
PROFILES = {
    "IA": DEFAULT_PROFILE,
    "Saude": {
        "role": "editor de jornalismo de saúde e medicina",
        "focus": (
            "atualidades em saúde e medicina (priorize o que realmente importa: estudos "
            "científicos relevantes, políticas públicas e SUS, surtos e epidemiologia, novas "
            "diretrizes clínicas, aprovações de medicamentos e tratamentos)"
        ),
        "categories": ["noticia", "estudo"],
    },
    "MercFin": {
        "role": "editor financeiro especializado em mercados de capitais e economia",
        "focus": (
            "mercado financeiro brasileiro e global (priorize: movimentos relevantes de bolsa "
            "e câmbio, decisões de bancos centrais, resultados corporativos relevantes, "
            "fusões e aquisições, commodities, cenário macro Brasil/EUA/China e tendências "
            "de investimento)"
        ),
        "categories": ["noticia", "analise", "dado"],
    },
    "Filmes": {
        "role": "editor de cinema e entretenimento especializado em filmes e séries",
        "focus": (
            "filmes e séries dos principais streamings e cinema (priorize: lançamentos e "
            "estreias da semana no cinema e streaming, críticas e análises de títulos em "
            "destaque, notícias sobre produções em andamento, renovações e cancelamentos "
            "de séries, trailers e teasers relevantes, bastidores e casting, tendências "
            "de Netflix, Disney+, Prime Video, Max, Apple TV+ e Globoplay)"
        ),
        "categories": ["lancamento", "critica", "noticia", "analise"],
    },
    "Jogos": {
        "role": "editor de jornalismo de games especializado em PS5 e PC",
        "focus": (
            "jogos e indústria de games (priorize: lançamentos e reviews relevantes, "
            "notícias da indústria como aquisições e demissões, novidades de PS5 e PC, "
            "atualizações de jogos em destaque, tendências de mercado e eventos como "
            "State of Play, Xbox Showcase e The Game Awards)"
        ),
        "categories": ["noticia", "review", "lancamento"],
    },
    "MedTrab": {
        "role": "editor especializado em medicina do trabalho e saúde ocupacional no Brasil",
        "focus": (
            "medicina do trabalho e saúde ocupacional no Brasil (priorize: atualizações de NRs "
            "e legislação trabalhista, doenças ocupacionais e nexo causal, segurança e saúde no "
            "trabalho, PCMSO/PGR/LTCAT, ergonomia, perícia médica trabalhista e jurisprudência "
            "do TST relevante para saúde do trabalhador)"
        ),
        "categories": ["noticia", "regulatorio", "estudo"],
    },
    "Puerperio": {
        "role": "especialista em saúde materna com foco no 3º trimestre de gestação",
        "focus": (
            "APENAS conteúdo prático e educativo para gestantes: exercícios físicos seguros "
            "na gravidez, alimentação e nutrição da gestante, dicas de bem-estar e autocuidado, "
            "preparação para o parto, saúde mental na gestação, curiosidades sobre o "
            "desenvolvimento fetal, cuidados com o corpo e sono. "
            "DESCARTE OBRIGATORIAMENTE qualquer tópico sobre: Fiocruz, Ministério da Saúde, "
            "SUS, políticas públicas, seminários, cooperações institucionais, legislação, "
            "programas governamentais ou notícias de eventos — esses NÃO devem aparecer"
        ),
        "categories": ["exercicio", "nutricao", "dica", "curiosidade"],
    },
    "RN": {
        "role": "especialista em cuidados com recém-nascidos e bebês",
        "focus": (
            "APENAS conteúdo prático e educativo sobre recém-nascidos e bebês: cuidados "
            "essenciais com o RN, amamentação e aleitamento materno, desenvolvimento "
            "neuromotor e cognitivo, sono do bebê, choro e cólicas, curiosidades sobre "
            "o desenvolvimento, orientações para pais de primeira viagem. "
            "DESCARTE OBRIGATORIAMENTE qualquer tópico sobre: Fiocruz, Ministério da Saúde, "
            "SUS, políticas públicas, seminários, cooperações institucionais, legislação, "
            "programas governamentais ou notícias de eventos — esses NÃO devem aparecer"
        ),
        "categories": ["dica", "curiosidade", "estudo"],
    },
}


def summarize_digest(
    api_key: str,
    docs: list[ScrapedDoc],
    num_topics: int = NUM_TOPICS,
    area: str = "IA",
) -> list[dict]:
    """Recebe os docs raspados e devolve uma lista de tópicos do dia.

    O enquadramento do resumo depende da área (ver PROFILES).
    """
    profile = PROFILES.get(area, DEFAULT_PROFILE)
    cats = profile["categories"]
    cats_json = "|".join(f"'{c}'" for c in cats)

    blocks = []
    total_chars = 0
    for d in docs:
        trecho = d.markdown[:MAX_CHARS_PER_SOURCE].strip()
        if not trecho:
            continue
        bloco = f"## Fonte: {d.title}\nURL: {d.url}\n\n{trecho}"
        if total_chars + len(bloco) > MAX_TOTAL_CONTEXT_CHARS:
            break
        blocks.append(bloco)
        total_chars += len(bloco)
    context = "\n\n---\n\n".join(blocks)
    print(f"   ↳ contexto: {len(blocks)} fontes, {total_chars} chars")

    prompt = (
        f"Você é um {profile['role']}. A seguir estão conteúdos raspados HOJE de várias "
        "fontes.\n\n"
        f"Selecione os {num_topics} tópicos MAIS IMPORTANTES do dia no total, cobrindo "
        f"{profile['focus']}. Para cada tópico escreva um resumo objetivo em português do "
        "Brasil de aproximadamente 800 caracteres. "
        "Use a URL ESPECÍFICA do artigo (a linha 'URL:' que aparece logo após cada manchete "
        "no conteúdo abaixo) — NUNCA use a URL do feed ou da fonte em si. "
        f"Classifique cada tópico em uma das categorias: {cats_json}.\n\n"
        'O campo "date": data de publicação entre colchetes na manchete, ex: [24/06/2026]. '
        'Se não houver, use "N/D".\n'
        'O campo "image_url": URL da linha "IMAGEM:" correspondente ao artigo. '
        'Se não houver imagem disponível, use "".\n\n'
        f"Conteúdo das fontes:\n\n{context}"
    )

    schema = _topics_schema(cats)
    print(f"🧠 Resumindo (área: {area}) — cadeia: {' → '.join(MODELS)}")
    topics = _call_gemini(api_key, prompt, schema, max_tokens=8192)
    print(f"   → {len(topics)} tópicos gerados")
    return topics

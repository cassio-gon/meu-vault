"""Sumarização com Gemini Flash (free tier): gera N tópicos do dia.

Usa a API REST do Google Generative Language via stdlib (sem dependências extras).
"""
from __future__ import annotations

import json
import os
import random
import re
import time
import urllib.error
import urllib.request

from scraper import ScrapedDoc

# Cadeia de modelos: tenta o primeiro; se ele esgotar os retries com erro
# transitório (503 sobrecarga) ou de cota (429), cai para o próximo.
# `GEMINI_MODEL` (env), se setado, entra como primário e o resto vira fallback.
_DEFAULT_CHAIN = ["gemini-2.5-flash", "gemini-2.5-flash-lite"]
_env_model = os.environ.get("GEMINI_MODEL")
MODELS = (
    [_env_model] + [m for m in _DEFAULT_CHAIN if m != _env_model]
    if _env_model
    else list(_DEFAULT_CHAIN)
)

MAX_CHARS_PER_SOURCE = 6000  # limita tokens de entrada por fonte
NUM_TOPICS = 6

# Retry por modelo para 429/5xx (sobrecarga/cota transitória do Gemini).
# Picos de demanda do Gemini ("high demand", 503) costumam durar minutos, então
# o backoff é exponencial com teto e jitter — atravessa o pico sem derrubar a run.
MAX_RETRIES = 5
RETRYABLE = {429, 500, 502, 503, 504}
BACKOFF_BASE = 2.0  # segundos: 2 → 4 → 8 → 16 → 32 (+jitter), com teto
BACKOFF_CAP = 60.0  # teto por espera, em segundos


def _backoff_seconds(attempt: int) -> float:
    """Espera exponencial (base 2) com teto e jitter aleatório de até 1s."""
    delay = min(BACKOFF_CAP, BACKOFF_BASE * 2 ** (attempt - 1))
    return delay + random.uniform(0, 1)


def _endpoint(model: str) -> str:
    return f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"


def _repair_truncated_json(text: str) -> str:
    """Tenta fechar um JSON truncado adicionando delimitadores faltantes."""
    s = text.rstrip()
    # Conta chaves e colchetes abertos para fechar na ordem certa
    stack = []
    in_string = False
    escaped = False
    for ch in s:
        if escaped:
            escaped = False
            continue
        if ch == "\\" and in_string:
            escaped = True
            continue
        if ch == '"':
            in_string = not in_string
            continue
        if in_string:
            continue
        if ch in "{[":
            stack.append("}" if ch == "{" else "]")
        elif ch in "}]" and stack:
            stack.pop()
    # Fecha string aberta e estruturas pendentes
    suffix = '"' if in_string else ""
    suffix += "".join(reversed(stack))
    return s + suffix


def _parse_topics(text: str) -> list[dict]:
    """Extrai o array de tópicos do texto da resposta (tolerante a cercas e JSON truncado)."""
    cleaned = text.strip()
    fence = re.search(r"```(?:json)?\s*(.*?)```", cleaned, re.DOTALL)
    if fence:
        cleaned = fence.group(1).strip()
    try:
        data = json.loads(cleaned)
    except json.JSONDecodeError:
        repaired = _repair_truncated_json(cleaned)
        try:
            data = json.loads(repaired)
            print(f"⚠️  JSON truncado reparado ({len(cleaned)}→{len(repaired)} chars)")
        except json.JSONDecodeError as err:
            raise RuntimeError(f"JSON inválido mesmo após reparo: {err}") from err
    if isinstance(data, dict):
        return data.get("topics", [])
    return data


def _call_gemini(api_key: str, prompt: str, max_tokens: int = 32768) -> str:
    """Chama o Gemini e devolve o texto da resposta (JSON forçado)."""
    body = json.dumps(
        {
            "contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": {
                "maxOutputTokens": max_tokens,
                "responseMimeType": "application/json",
                "temperature": 0.4,
                # thinkingBudget=0 desativa thinking interno do 2.5 Flash,
                # evitando que tokens de raciocínio consumam o limite de saída
                "thinkingConfig": {"thinkingBudget": 0},
            },
        }
    ).encode("utf-8")

    last_err: Exception | None = None
    for mi, model in enumerate(MODELS):
        endpoint = _endpoint(model)
        print(f"   ↳ modelo: {model}")
        for attempt in range(1, MAX_RETRIES + 1):
            req = urllib.request.Request(
                f"{endpoint}?key={api_key}",
                data=body,
                headers={"Content-Type": "application/json"},
                method="POST",
            )
            try:
                with urllib.request.urlopen(req, timeout=120) as resp:
                    data = json.load(resp)
                candidates = data.get("candidates", [])
                if not candidates:
                    raise RuntimeError(f"Gemini não retornou candidates: {str(data)[:300]}")
                return candidates[0]["content"]["parts"][0]["text"]
            except urllib.error.HTTPError as err:
                detail = err.read().decode("utf-8", "ignore")[:200]
                last_err = RuntimeError(f"Gemini HTTP {err.code}: {detail}")
                if err.code not in RETRYABLE:
                    raise last_err from err
                wait = _backoff_seconds(attempt)
                print(f"⚠️  {model} HTTP {err.code} (tentativa {attempt}/{MAX_RETRIES}); aguardando {wait:.1f}s...")
            except urllib.error.URLError as err:
                last_err = RuntimeError(f"Gemini erro de rede: {err}")
                wait = _backoff_seconds(attempt)
                print(f"⚠️  Rede falhou em {model} (tentativa {attempt}/{MAX_RETRIES}); aguardando {wait:.1f}s...")
            if attempt < MAX_RETRIES:
                time.sleep(wait)
        # Esgotou os retries deste modelo: cai para o próximo da cadeia, se houver.
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
    for d in docs:
        trecho = d.markdown[:MAX_CHARS_PER_SOURCE].strip()
        if trecho:
            blocks.append(f"## Fonte: {d.title}\nURL: {d.url}\n\n{trecho}")
    context = "\n\n---\n\n".join(blocks)

    prompt = (
        f"Você é um {profile['role']}. A seguir estão conteúdos raspados HOJE de várias "
        "fontes.\n\n"
        f"Selecione os {num_topics} tópicos MAIS IMPORTANTES do dia no total, cobrindo "
        f"{profile['focus']}. Para cada tópico escreva um resumo objetivo em português do "
        "Brasil de aproximadamente 500 caracteres. Use a URL mais relevante da fonte "
        f"correspondente e classifique cada tópico como {cats_json}.\n\n"
        "Responda APENAS com um objeto JSON válido no formato:\n"
        '{"topics": [{"title": "...", "summary": "...", "url": "...", '
        f'"category": {cats_json}}}]}}\n\n'
        f"Conteúdo das fontes:\n\n{context}"
    )

    print(f"🧠 Resumindo (área: {area}) — cadeia: {' → '.join(MODELS)}")
    text = _call_gemini(api_key, prompt)
    topics = _parse_topics(text)
    print(f"   → {len(topics)} tópicos gerados")
    return topics

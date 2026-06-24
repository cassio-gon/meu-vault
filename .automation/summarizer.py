"""Sumarização com Groq (free tier): gera N tópicos do dia.

Usa a API REST do Groq (compatível com OpenAI) via stdlib (sem dependências extras).
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

GROQ_API = "https://api.groq.com/openai/v1/chat/completions"

# Cadeia de modelos: tenta o primeiro; se esgotar retries com erro
# transitório ou de cota, cai para o próximo.
# `GROQ_MODEL` (env), se setado, entra como primário.
_DEFAULT_CHAIN = ["llama-3.3-70b-versatile", "llama-3.1-8b-instant"]
_env_model = os.environ.get("GROQ_MODEL")
MODELS = (
    [_env_model] + [m for m in _DEFAULT_CHAIN if m != _env_model]
    if _env_model
    else list(_DEFAULT_CHAIN)
)

MAX_CHARS_PER_SOURCE = 1500   # limita chars por fonte (~375 tokens)
MAX_TOTAL_CONTEXT_CHARS = 18_000  # teto do bloco de contexto (~4500 tokens)
NUM_TOPICS = 6

MAX_RETRIES = 5
RETRYABLE = {429, 500, 502, 503, 504, 529}  # 529 = Claude overloaded
BACKOFF_BASE = 2.0  # segundos: 2 → 4 → 8 → 16 → 32 (+jitter), com teto
BACKOFF_CAP = 60.0


def _backoff_seconds(attempt: int) -> float:
    """Espera exponencial (base 2) com teto e jitter aleatório de até 1s."""
    delay = min(BACKOFF_CAP, BACKOFF_BASE * 2 ** (attempt - 1))
    return delay + random.uniform(0, 1)


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


def _call_groq(api_key: str, prompt: str, max_tokens: int = 8192) -> str:
    """Chama a API do Groq e devolve o texto da resposta."""
    last_err: Exception | None = None
    for mi, model in enumerate(MODELS):
        body = json.dumps(
            {
                "model": model,
                "max_tokens": max_tokens,
                "temperature": 0.4,
                "messages": [{"role": "user", "content": prompt}],
            }
        ).encode("utf-8")
        print(f"   ↳ modelo: {model}")
        for attempt in range(1, MAX_RETRIES + 1):
            req = urllib.request.Request(
                GROQ_API,
                data=body,
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {api_key}",
                    "User-Agent": "groq-python/0.9.0",
                    "Accept": "application/json",
                },
                method="POST",
            )
            try:
                with urllib.request.urlopen(req, timeout=120) as resp:
                    data = json.load(resp)
                choices = data.get("choices", [])
                if not choices:
                    raise RuntimeError(f"Groq não retornou choices: {str(data)[:300]}")
                return choices[0]["message"]["content"]
            except urllib.error.HTTPError as err:
                detail = err.read().decode("utf-8", "ignore")[:200]
                last_err = RuntimeError(f"Groq HTTP {err.code}: {detail}")
                if err.code not in RETRYABLE:
                    raise last_err from err
                wait = _backoff_seconds(attempt)
                print(f"⚠️  {model} HTTP {err.code} (tentativa {attempt}/{MAX_RETRIES}); aguardando {wait:.1f}s...")
            except urllib.error.URLError as err:
                last_err = RuntimeError(f"Erro de rede: {err}")
                wait = _backoff_seconds(attempt)
                print(f"⚠️  Rede falhou em {model} (tentativa {attempt}/{MAX_RETRIES}); aguardando {wait:.1f}s...")
            if attempt < MAX_RETRIES:
                time.sleep(wait)
        if mi < len(MODELS) - 1:
            print(f"↪️  {model} indisponível; tentando próximo modelo...")
    raise RuntimeError(f"Todos os modelos Groq falharam ({', '.join(MODELS)})") from last_err


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
        "Brasil de aproximadamente 500 caracteres. Use a URL mais relevante da fonte "
        f"correspondente e classifique cada tópico como {cats_json}.\n\n"
        "Responda APENAS com um objeto JSON válido no formato:\n"
        '{"topics": [{"title": "...", "summary": "...", "url": "...", '
        f'"category": {cats_json}}}]}}\n\n'
        f"Conteúdo das fontes:\n\n{context}"
    )

    print(f"🧠 Resumindo (área: {area}) — cadeia: {' → '.join(MODELS)}")
    text = _call_groq(api_key, prompt)
    topics = _parse_topics(text)
    print(f"   → {len(topics)} tópicos gerados")
    return topics

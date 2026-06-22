"""Sumarização com Gemini Flash (free tier): gera N tópicos do dia.

Usa a API REST do Google Generative Language via stdlib (sem dependências extras).
"""
from __future__ import annotations

import json
import re
import urllib.error
import urllib.request

from scraper import ScrapedDoc

MODEL = "gemini-2.5-flash"
ENDPOINT = (
    f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"
)
MAX_CHARS_PER_SOURCE = 6000  # limita tokens de entrada por fonte
NUM_TOPICS = 6


def _parse_topics(text: str) -> list[dict]:
    """Extrai o array de tópicos do texto da resposta (tolerante a cercas ```)."""
    cleaned = text.strip()
    fence = re.search(r"```(?:json)?\s*(.*?)```", cleaned, re.DOTALL)
    if fence:
        cleaned = fence.group(1).strip()
    data = json.loads(cleaned)
    if isinstance(data, dict):
        return data.get("topics", [])
    return data


def _call_gemini(api_key: str, prompt: str, max_tokens: int = 8000) -> str:
    """Chama o Gemini e devolve o texto da resposta (JSON forçado)."""
    body = json.dumps(
        {
            "contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": {
                "maxOutputTokens": max_tokens,
                "responseMimeType": "application/json",
                "temperature": 0.4,
            },
        }
    ).encode("utf-8")

    req = urllib.request.Request(
        f"{ENDPOINT}?key={api_key}",
        data=body,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = json.load(resp)
    except urllib.error.HTTPError as err:
        detail = err.read().decode("utf-8", "ignore")[:300]
        raise RuntimeError(f"Gemini HTTP {err.code}: {detail}") from err

    candidates = data.get("candidates", [])
    if not candidates:
        raise RuntimeError(f"Gemini não retornou candidates: {str(data)[:300]}")
    return candidates[0]["content"]["parts"][0]["text"]


def summarize_digest(
    api_key: str,
    docs: list[ScrapedDoc],
    num_topics: int = NUM_TOPICS,
) -> list[dict]:
    """Recebe os docs raspados e devolve uma lista de tópicos do dia."""
    blocks = []
    for d in docs:
        trecho = d.markdown[:MAX_CHARS_PER_SOURCE].strip()
        if trecho:
            blocks.append(f"## Fonte: {d.title}\nURL: {d.url}\n\n{trecho}")
    context = "\n\n---\n\n".join(blocks)

    prompt = (
        "Você é um editor de tecnologia especializado em IA. A seguir estão conteúdos "
        "raspados HOJE de várias fontes (notícias e ferramentas de IA).\n\n"
        f"Selecione os {num_topics} tópicos MAIS IMPORTANTES do dia no total, misturando "
        "notícias e ferramentas (priorize o que realmente importa: lançamentos, rodadas de "
        "investimento, modelos novos, ferramentas relevantes). Para cada tópico escreva um "
        "resumo objetivo em português do Brasil de aproximadamente 500 caracteres. Use a URL "
        "mais relevante da fonte correspondente e classifique cada tópico como 'noticia' ou "
        "'ferramenta'.\n\n"
        "Responda APENAS com um objeto JSON válido no formato:\n"
        '{"topics": [{"title": "...", "summary": "...", "url": "...", '
        '"category": "noticia"|"ferramenta"}]}\n\n'
        f"Conteúdo das fontes:\n\n{context}"
    )

    print(f"🧠 Resumindo com {MODEL}...")
    text = _call_gemini(api_key, prompt)
    topics = _parse_topics(text)
    print(f"   → {len(topics)} tópicos gerados")
    return topics

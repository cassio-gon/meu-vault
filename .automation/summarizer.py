"""Sumarização com Claude: lê o conteúdo raspado e gera N tópicos do dia."""
from __future__ import annotations

import json
import re

from anthropic import Anthropic

from scraper import ScrapedDoc

MODEL = "claude-opus-4-8"
MAX_CHARS_PER_SOURCE = 6000  # limita tokens de entrada por fonte
NUM_TOPICS = 6


def _parse_topics(text: str) -> list[dict]:
    """Extrai o array de tópicos do texto da resposta (tolerante a cercas ```)."""
    cleaned = text.strip()
    # Remove cercas de código tipo ```json ... ```
    fence = re.search(r"```(?:json)?\s*(.*?)```", cleaned, re.DOTALL)
    if fence:
        cleaned = fence.group(1).strip()
    data = json.loads(cleaned)
    if isinstance(data, dict):
        return data.get("topics", [])
    return data  # caso o modelo devolva o array direto


def summarize_digest(
    api_key: str,
    docs: list[ScrapedDoc],
    num_topics: int = NUM_TOPICS,
) -> list[dict]:
    """Recebe os docs raspados e devolve uma lista de tópicos do dia."""
    client = Anthropic(api_key=api_key)

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
        "Responda APENAS com um objeto JSON válido, sem texto antes ou depois, no formato:\n"
        '{"topics": [{"title": "...", "summary": "...", "url": "...", '
        '"category": "noticia"|"ferramenta"}]}\n\n'
        f"Conteúdo das fontes:\n\n{context}"
    )

    print(f"🧠 Resumindo com {MODEL}...")
    response = client.messages.create(
        model=MODEL,
        max_tokens=8000,
        messages=[{"role": "user", "content": prompt}],
    )

    if response.stop_reason == "refusal":
        raise RuntimeError("Claude recusou a requisição (stop_reason=refusal).")

    text = next(b.text for b in response.content if b.type == "text")
    topics = _parse_topics(text)
    print(f"   → {len(topics)} tópicos gerados")
    return topics

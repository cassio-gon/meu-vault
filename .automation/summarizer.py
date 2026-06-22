"""Sumarização com Claude: lê o conteúdo raspado e gera N tópicos do dia."""
from __future__ import annotations

import json

from anthropic import Anthropic

from scraper import ScrapedDoc

MODEL = "claude-opus-4-8"
MAX_CHARS_PER_SOURCE = 6000  # limita tokens de entrada por fonte
NUM_TOPICS = 6

# Estrutura garantida da resposta (structured outputs)
SCHEMA = {
    "type": "object",
    "properties": {
        "topics": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "title": {"type": "string"},
                    "summary": {"type": "string"},
                    "url": {"type": "string"},
                    "category": {"type": "string", "enum": ["noticia", "ferramenta"]},
                },
                "required": ["title", "summary", "url", "category"],
                "additionalProperties": False,
            },
        }
    },
    "required": ["topics"],
    "additionalProperties": False,
}


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
        f"Conteúdo das fontes:\n\n{context}"
    )

    print(f"🧠 Resumindo com {MODEL}...")
    response = client.messages.create(
        model=MODEL,
        max_tokens=8000,
        thinking={"type": "adaptive"},
        output_config={"format": {"type": "json_schema", "schema": SCHEMA}},
        messages=[{"role": "user", "content": prompt}],
    )

    if response.stop_reason == "refusal":
        raise RuntimeError("Claude recusou a requisição (stop_reason=refusal).")

    text = next(b.text for b in response.content if b.type == "text")
    topics = json.loads(text)["topics"]
    print(f"   → {len(topics)} tópicos gerados")
    return topics

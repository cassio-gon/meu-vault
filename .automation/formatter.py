"""Converte ScrapedDoc em arquivo .md com frontmatter YAML."""
from __future__ import annotations

import re
import unicodedata
from pathlib import Path

import yaml

from scraper import ScrapedDoc

MAX_SLUG_LEN = 80


def slugify(text: str) -> str:
    """Transforma um título em slug seguro para nome de arquivo."""
    # Remove acentos
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = text.lower().strip()
    # Troca tudo que não é alfanumérico por hífen
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = text.strip("-")
    return (text or "sem-titulo")[:MAX_SLUG_LEN]


def build_filename(doc: ScrapedDoc) -> str:
    """Monta o nome do arquivo: `YYYY-MM-DD — titulo-slugificado.md`."""
    return f"{doc.scraped_at} — {slugify(doc.title)}.md"


def render_markdown(doc: ScrapedDoc, tag: str, source: str = "firecrawl") -> str:
    """Gera o conteúdo final do .md (frontmatter YAML + corpo)."""
    frontmatter = {
        "title": doc.title,
        "date": doc.scraped_at,
        "url": doc.url,
        "tags": [tag],
        "source": source,
    }
    yaml_block = yaml.safe_dump(
        frontmatter, allow_unicode=True, sort_keys=False
    ).strip()
    return f"---\n{yaml_block}\n---\n\n{doc.markdown.strip()}\n"


def save_note(doc: ScrapedDoc, notes_dir: Path, tag: str) -> Path:
    """Escreve a nota em disco e retorna o caminho do arquivo criado."""
    notes_dir.mkdir(parents=True, exist_ok=True)
    path = notes_dir / build_filename(doc)
    path.write_text(render_markdown(doc, tag), encoding="utf-8")
    print(f"✅ Nota salva: {path.name}")
    return path

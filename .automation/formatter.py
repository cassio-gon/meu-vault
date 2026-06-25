"""Converte resultados em arquivos .md com frontmatter YAML."""
from __future__ import annotations

import re
import unicodedata
from datetime import datetime, timedelta, timezone

_BRT = timezone(timedelta(hours=-3))
from pathlib import Path

import yaml

from scraper import ScrapedDoc

MAX_SLUG_LEN = 80


def slugify(text: str) -> str:
    """Transforma um título em slug seguro para nome de arquivo."""
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = text.strip("-")
    return (text or "sem-titulo")[:MAX_SLUG_LEN]


def build_filename(doc: ScrapedDoc) -> str:
    """Monta o nome do arquivo: `YYYY-MM-DD — titulo-slugificado.md`."""
    return f"{doc.scraped_at} — {slugify(doc.title)}.md"


def render_markdown(doc: ScrapedDoc, tag: str, source: str = "trafilatura") -> str:
    """Gera o conteúdo de uma nota crua (scrape/crawl)."""
    frontmatter = {
        "title": doc.title,
        "date": doc.scraped_at,
        "url": doc.url,
        "tags": [tag],
        "source": source,
    }
    yaml_block = yaml.safe_dump(frontmatter, allow_unicode=True, sort_keys=False).strip()
    return f"---\n{yaml_block}\n---\n\n{doc.markdown.strip()}\n"


def save_note(doc: ScrapedDoc, notes_dir: Path, tag: str) -> Path:
    """Escreve uma nota crua em disco e retorna o caminho."""
    notes_dir.mkdir(parents=True, exist_ok=True)
    path = notes_dir / build_filename(doc)
    path.write_text(render_markdown(doc, tag), encoding="utf-8")
    print(f"✅ Nota salva: {path.name}")
    return path


# --- Digest (resumo do dia gerado por IA) -------------------------------------


# Ícone por categoria de tópico (cobre as categorias de todas as áreas).
CATEGORY_EMOJI = {
    "noticia": "📰",
    "ferramenta": "🛠️",
    "estudo": "🔬",
}
DEFAULT_CATEGORY_EMOJI = "📌"


def render_digest(topics: list[dict], day: str, tag: str, area: str) -> str:
    """Gera o conteúdo do digest: frontmatter + tópicos resumidos."""
    frontmatter = {
        "title": f"{area} — Digest {day}",
        "date": day,
        "tags": [tag, "digest"],
        "area": area,
        "source": "trafilatura+gemini",
    }
    yaml_block = yaml.safe_dump(frontmatter, allow_unicode=True, sort_keys=False).strip()

    valid = [t for t in topics if t.get("title") and t.get("summary") and t.get("url")]
    if len(valid) < len(topics):
        print(f"⚠️  {len(topics) - len(valid)} tópico(s) incompletos descartados")
    parts = [f"---\n{yaml_block}\n---\n", f"# 🗞️ {area} — Principais do dia ({day})\n"]
    for i, t in enumerate(valid, 1):
        emoji = CATEGORY_EMOJI.get(t.get("category"), DEFAULT_CATEGORY_EMOJI)
        news_date = t.get("date", "N/D")
        image_url = t.get("image_url", "").strip()
        image_block = f"![]({image_url})\n\n" if image_url else ""
        parts.append(
            f"## {i}. {emoji} {t['title']}\n\n"
            f"{image_block}"
            f"{t['summary'].strip()}\n\n"
            f"📅 Data da notícia: {news_date} · [Fonte]({t['url']})\n"
        )
    return "\n".join(parts)


def save_digest(topics: list[dict], notes_dir: Path, tag: str, area: str) -> Path:
    """Escreve o digest do dia e retorna o caminho do arquivo."""
    notes_dir.mkdir(parents=True, exist_ok=True)
    day = datetime.now(tz=_BRT).strftime("%Y-%m-%d %Hh%M")
    path = notes_dir / f"{day} — {area} Digest.md"
    path.write_text(render_digest(topics, day, tag, area), encoding="utf-8")
    print(f"✅ Digest salvo: {path.name}")
    return path

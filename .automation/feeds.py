"""Leitura de feeds RSS/Atom via stdlib (sem Firecrawl → 0 créditos).

Devolve um ScrapedDoc compatível com o resto do pipeline (summarizer/formatter):
o markdown vira uma lista das manchetes mais recentes + resumo de cada item.
"""
from __future__ import annotations

import re
import time
import urllib.error
import urllib.request
from datetime import date
from xml.etree import ElementTree as ET

from scraper import ScrapedDoc

MAX_ITEMS = 15        # nº de manchetes por feed que entram no contexto do LLM
MAX_DESC_CHARS = 500  # corta a descrição de cada item
MAX_RETRIES = 3
BACKOFF_SECONDS = 2

_TAG_RE = re.compile(r"<[^>]+>")
_ENTITIES = {
    "&amp;": "&", "&lt;": "<", "&gt;": ">", "&quot;": '"',
    "&#39;": "'", "&apos;": "'", "&nbsp;": " ",
}


def _localname(tag: str) -> str:
    """Nome da tag sem namespace, em minúsculas (ex.: '{ns}item' → 'item')."""
    return tag.split("}")[-1].lower()


def _text(el) -> str:
    return (el.text or "").strip() if el is not None else ""


def _strip_html(s: str) -> str:
    s = _TAG_RE.sub("", s)
    for ent, char in _ENTITIES.items():
        s = s.replace(ent, char)
    return re.sub(r"\s+", " ", s).strip()


def _fetch(url: str) -> bytes:
    """GET com retry/backoff; devolve os bytes do XML."""
    last_err: Exception | None = None
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            req = urllib.request.Request(
                url, headers={"User-Agent": "Mozilla/5.0 (vault-automator)"}
            )
            with urllib.request.urlopen(req, timeout=30) as resp:
                return resp.read()
        except (urllib.error.URLError, urllib.error.HTTPError) as err:
            last_err = err
            wait = BACKOFF_SECONDS * attempt
            print(f"⚠️  RSS {url} falhou (tentativa {attempt}/{MAX_RETRIES}): {err}")
            if attempt < MAX_RETRIES:
                time.sleep(wait)
    raise RuntimeError(f"RSS {url} falhou após {MAX_RETRIES} tentativas") from last_err


def _item_link(entry) -> str:
    """Extrai o link de um item (RSS: texto de <link>; Atom: href, evita rel=self)."""
    fallback = ""
    for c in entry:
        if _localname(c.tag) != "link":
            continue
        if c.text and c.text.strip():
            return c.text.strip()  # RSS/RDF: link no texto
        href = c.get("href", "")
        if href and c.get("rel") != "self":
            return href  # Atom: alternate
        fallback = fallback or href
    return fallback


def fetch_feed(url: str, max_items: int = MAX_ITEMS) -> ScrapedDoc:
    """Baixa e parseia um feed RSS/Atom/RDF, retornando um ScrapedDoc."""
    print(f"📡 RSS: {url}")
    root = ET.fromstring(_fetch(url))

    # Título do feed: primeiro <title> em ordem de documento (channel/feed).
    feed_title = url
    for el in root.iter():
        if _localname(el.tag) == "title" and _text(el):
            feed_title = _text(el)
            break

    entries = [el for el in root.iter() if _localname(el.tag) in ("item", "entry")]

    lines = []
    for entry in entries[:max_items]:
        title = desc = ""
        for c in entry:
            ln = _localname(c.tag)
            if ln == "title" and not title:
                title = _text(c)
            elif ln in ("description", "summary", "encoded", "content") and not desc:
                desc = _text(c)
        title = _strip_html(title)
        desc = _strip_html(desc)[:MAX_DESC_CHARS]
        link = _item_link(entry)
        if not title:
            continue
        block = f"- **{title}**"
        if desc:
            block += f": {desc}"
        if link:
            block += f"\n  {link}"
        lines.append(block)

    markdown = f"# {feed_title}\n\n" + "\n".join(lines)
    print(f"   → {len(lines)} itens")
    return ScrapedDoc(
        title=feed_title,
        markdown=markdown,
        url=url,
        scraped_at=date.today().isoformat(),
    )

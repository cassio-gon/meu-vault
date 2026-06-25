"""Leitura de feeds RSS/Atom via stdlib (sem Firecrawl → 0 créditos).

Devolve um ScrapedDoc compatível com o resto do pipeline (summarizer/formatter):
o markdown vira uma lista das manchetes recentes + resumo de cada item.
Itens mais antigos que MAX_AGE_DAYS são descartados automaticamente.
"""
from __future__ import annotations

import email.utils
import re
import time
import urllib.error
import urllib.request
from datetime import date, datetime, timedelta, timezone
from xml.etree import ElementTree as ET

from scraper import ScrapedDoc

MAX_ITEMS = 15
MAX_DESC_CHARS = 500
MAX_RETRIES = 3
BACKOFF_SECONDS = 2
MAX_AGE_DAYS = 7  # descarta artigos mais antigos que isso

_TAG_RE = re.compile(r"<[^>]+>")
_ENTITIES = {
    "&amp;": "&", "&lt;": "<", "&gt;": ">", "&quot;": '"',
    "&#39;": "'", "&apos;": "'", "&nbsp;": " ",
}


def _localname(tag: str) -> str:
    return tag.split("}")[-1].lower()


def _text(el) -> str:
    return (el.text or "").strip() if el is not None else ""


def _strip_html(s: str) -> str:
    s = _TAG_RE.sub("", s)
    for ent, char in _ENTITIES.items():
        s = s.replace(ent, char)
    return re.sub(r"\s+", " ", s).strip()


def _parse_date(s: str) -> datetime | None:
    """Parseia data RSS (RFC 2822) ou Atom (ISO 8601). Retorna None se falhar."""
    if not s:
        return None
    s = s.strip()
    # RFC 2822: "Tue, 24 Jun 2026 15:30:00 +0000"
    try:
        return email.utils.parsedate_to_datetime(s)
    except Exception:
        pass
    # ISO 8601: "2026-06-24T15:30:00Z" ou "2026-06-24T15:30:00+00:00"
    try:
        return datetime.fromisoformat(s.replace("Z", "+00:00"))
    except ValueError:
        pass
    # Só data: "2026-06-24"
    try:
        return datetime.strptime(s[:10], "%Y-%m-%d").replace(tzinfo=timezone.utc)
    except ValueError:
        pass
    return None


def _is_recent(raw_date: str) -> bool:
    """Retorna True se o artigo for de até MAX_AGE_DAYS atrás. Sem data = inclui."""
    dt = _parse_date(raw_date)
    if dt is None:
        return True
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    cutoff = datetime.now(tz=timezone.utc) - timedelta(days=MAX_AGE_DAYS)
    return dt >= cutoff


def _fmt_date(raw_date: str) -> str:
    """Formata a data como DD/MM/AAAA para exibição."""
    dt = _parse_date(raw_date)
    if dt is None:
        return ""
    return dt.strftime("%d/%m/%Y")


def _fetch(url: str) -> bytes:
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
    fallback = ""
    for c in entry:
        if _localname(c.tag) != "link":
            continue
        if c.text and c.text.strip():
            return c.text.strip()
        href = c.get("href", "")
        if href and c.get("rel") != "self":
            return href
        fallback = fallback or href
    return fallback


def _item_date(entry) -> str:
    for c in entry:
        if _localname(c.tag) in ("pubdate", "published", "updated", "date"):
            return _text(c)
    return ""


def _item_image(entry) -> str:
    """Extrai URL da imagem do item RSS (media:content, media:thumbnail, enclosure, img no HTML)."""
    _IMG_EXT = (".jpg", ".jpeg", ".png", ".webp", ".gif")
    for c in entry:
        ln = _localname(c.tag)
        if ln in ("content", "thumbnail"):
            url = c.get("url", "")
            if url and (c.get("medium") == "image" or url.split("?")[0].lower().endswith(_IMG_EXT)):
                return url
        if ln == "enclosure":
            url = c.get("url", "")
            if url and c.get("type", "").startswith("image/"):
                return url
    # fallback: primeiro <img src> encontrado no HTML da description
    for c in entry:
        if _localname(c.tag) in ("description", "summary", "content"):
            html = c.text or ""
            m = re.search(r'<img[^>]+src=["\']([^"\']+)["\']', html)
            if m:
                return m.group(1)
    return ""


def fetch_feed(url: str, max_items: int = MAX_ITEMS) -> ScrapedDoc:
    """Baixa e parseia um feed RSS/Atom/RDF, retornando um ScrapedDoc."""
    print(f"📡 RSS: {url}")
    root = ET.fromstring(_fetch(url))

    feed_title = url
    for el in root.iter():
        if _localname(el.tag) == "title" and _text(el):
            feed_title = _text(el)
            break

    entries = [el for el in root.iter() if _localname(el.tag) in ("item", "entry")]

    lines = []
    skipped_old = 0
    for entry in entries[:max_items]:
        title = desc = raw_date = ""
        for c in entry:
            ln = _localname(c.tag)
            if ln == "title" and not title:
                title = _text(c)
            elif ln in ("description", "summary", "encoded", "content") and not desc:
                desc = _text(c)
            elif ln in ("pubdate", "published", "updated", "date") and not raw_date:
                raw_date = _text(c)

        if not _is_recent(raw_date):
            skipped_old += 1
            continue

        title = _strip_html(title)
        desc = _strip_html(desc)[:MAX_DESC_CHARS]
        link = _item_link(entry)
        date_str = _fmt_date(raw_date)
        image_url = _item_image(entry)

        if not title:
            continue

        block = f"- **{title}**"
        if date_str:
            block += f" [{date_str}]"
        if desc:
            block += f": {desc}"
        if link:
            block += f"\n  URL: {link}"
        if image_url:
            block += f"\n  IMAGEM: {image_url}"
        lines.append(block)

    markdown = f"# {feed_title}\n\n" + "\n".join(lines)
    suffix = f" ({skipped_old} antigos ignorados)" if skipped_old else ""
    print(f"   → {len(lines)} itens recentes{suffix}")
    return ScrapedDoc(
        title=feed_title,
        markdown=markdown,
        url=url,
        scraped_at=date.today().isoformat(),
    )

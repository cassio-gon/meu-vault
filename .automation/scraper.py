"""Scraping via trafilatura (sem API externa, sem limites de crédito)."""
from __future__ import annotations

import json
import time
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import datetime
from html.parser import HTMLParser

import trafilatura

MAX_RETRIES = 3
BACKOFF_SECONDS = 2

_HF_API = "https://huggingface.co/api/models?sort=trending&limit=20"
_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (compatible; vault-bot/1.0; +https://github.com/cassio-gon/meu-vault)"
    )
}


@dataclass
class ScrapedDoc:
    title: str
    markdown: str
    url: str
    scraped_at: str  # YYYY-MM-DD HH:MM


def _with_retry(fn, label: str):
    last_err: Exception | None = None
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            return fn()
        except Exception as err:  # noqa: BLE001
            last_err = err
            wait = BACKOFF_SECONDS * attempt
            print(f"⚠️  {label} falhou (tentativa {attempt}/{MAX_RETRIES}): {err}")
            if attempt < MAX_RETRIES:
                print(f"   ⏳ aguardando {wait}s antes de tentar de novo...")
                time.sleep(wait)
    raise RuntimeError(f"{label} falhou após {MAX_RETRIES} tentativas") from last_err


def _hf_trending() -> ScrapedDoc:
    """Busca modelos trending via API pública do HuggingFace (sem JS)."""
    req = urllib.request.Request(_HF_API, headers=_HEADERS)
    with urllib.request.urlopen(req, timeout=30) as resp:
        models = json.load(resp)

    lines = ["# HuggingFace — Modelos Trending\n"]
    for m in models[:20]:
        name = m.get("id", "")
        likes = m.get("likes", 0)
        downloads = m.get("downloads", 0)
        pipeline = m.get("pipeline_tag", "")
        line = f"- [{name}](https://huggingface.co/{name})"
        if pipeline:
            line += f" ({pipeline})"
        line += f" — {likes} likes, {downloads} downloads"
        lines.append(line)

    return ScrapedDoc(
        title="HuggingFace Trending Models",
        markdown="\n".join(lines),
        url="https://huggingface.co/models?sort=trending",
        scraped_at=datetime.now().strftime("%Y-%m-%d %H:%M"),
    )


def _extract_text(url: str) -> ScrapedDoc:
    """Extrai texto limpo de uma URL via trafilatura."""
    downloaded = trafilatura.fetch_url(url)
    if not downloaded:
        raise RuntimeError("trafilatura não conseguiu baixar a página")

    result = trafilatura.bare_extraction(
        downloaded,
        include_links=False,
        include_images=False,
        favor_recall=True,
    )
    if not result or not result.get("text"):
        raise RuntimeError("trafilatura não extraiu conteúdo")

    return ScrapedDoc(
        title=str(result.get("title") or url).strip(),
        markdown=str(result["text"]).strip(),
        url=str(result.get("url") or url),
        scraped_at=datetime.now().strftime("%Y-%m-%d %H:%M"),
    )


def scrape_url(url: str) -> ScrapedDoc:
    """Faz scrape de uma única URL e retorna um ScrapedDoc."""
    if "huggingface.co/models" in url:
        print(f"🤗 HuggingFace API: {url}")
        return _with_retry(_hf_trending, "huggingface-api")

    print(f"📄 Scrape: {url}")
    return _with_retry(lambda: _extract_text(url), f"scrape({url})")


class _LinkParser(HTMLParser):
    """Extrai links internos de uma página HTML."""

    def __init__(self, base: str) -> None:
        super().__init__()
        self.base = base
        self.links: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list) -> None:
        if tag != "a":
            return
        for attr, val in attrs:
            if attr == "href" and val:
                full = urllib.parse.urljoin(self.base, val).split("#")[0]
                if full.startswith(self.base) and full != self.base:
                    self.links.add(full)


def crawl_domain(url: str, limit: int = 10) -> list[ScrapedDoc]:
    """Faz crawl de um domínio (até `limit` páginas) sem API externa."""
    print(f"🕸️  Crawl: {url} (limite {limit} páginas)")

    try:
        req = urllib.request.Request(url, headers=_HEADERS)
        with urllib.request.urlopen(req, timeout=30) as resp:
            html = resp.read().decode("utf-8", "ignore")
    except Exception as err:
        raise RuntimeError(f"Não foi possível acessar {url}: {err}") from err

    parser = _LinkParser(url)
    parser.feed(html)
    urls_to_crawl = list(parser.links)[:limit]

    docs: list[ScrapedDoc] = []
    for page_url in urls_to_crawl:
        try:
            doc = scrape_url(page_url)
            if doc.markdown.strip():
                docs.append(doc)
        except Exception as err:  # noqa: BLE001
            print(f"⚠️  Pulei {page_url}: {err}")

    print(f"   → {len(docs)} páginas com conteúdo")
    return docs

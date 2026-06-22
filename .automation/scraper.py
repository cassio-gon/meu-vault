"""Lógica de scraping/crawling via Firecrawl Python SDK."""
from __future__ import annotations

import time
from dataclasses import dataclass
from datetime import date

from firecrawl import FirecrawlApp

# Política de retry para rate limit / erros transitórios
MAX_RETRIES = 3
BACKOFF_SECONDS = 2


@dataclass
class ScrapedDoc:
    title: str
    markdown: str
    url: str
    scraped_at: str  # YYYY-MM-DD


def _extract_doc(result: dict, fallback_url: str) -> ScrapedDoc:
    """Normaliza a resposta do Firecrawl (dict) num ScrapedDoc."""
    # O SDK pode devolver o conteúdo na raiz ou dentro de "data"
    data = result.get("data", result) if isinstance(result, dict) else {}
    metadata = data.get("metadata", {}) or {}

    title = (
        metadata.get("title")
        or metadata.get("ogTitle")
        or fallback_url
    )
    url = metadata.get("sourceURL") or metadata.get("url") or fallback_url
    markdown = data.get("markdown") or ""

    return ScrapedDoc(
        title=str(title).strip(),
        markdown=markdown,
        url=url,
        scraped_at=date.today().isoformat(),
    )


def _with_retry(fn, label: str):
    """Executa fn() com retry e backoff linear (2s, 4s, 6s)."""
    last_err: Exception | None = None
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            return fn()
        except Exception as err:  # noqa: BLE001 — Firecrawl agrega vários tipos
            last_err = err
            wait = BACKOFF_SECONDS * attempt
            print(f"⚠️  {label} falhou (tentativa {attempt}/{MAX_RETRIES}): {err}")
            if attempt < MAX_RETRIES:
                print(f"   ⏳ aguardando {wait}s antes de tentar de novo...")
                time.sleep(wait)
    raise RuntimeError(f"{label} falhou após {MAX_RETRIES} tentativas") from last_err


def scrape_url(api_key: str, url: str) -> ScrapedDoc:
    """Faz scrape de uma única URL e retorna um ScrapedDoc."""
    app = FirecrawlApp(api_key=api_key)
    print(f"📄 Scrape: {url}")

    def _run():
        return app.scrape_url(url, params={"formats": ["markdown"]})

    result = _with_retry(_run, "scrape_url")
    return _extract_doc(result, url)


def crawl_domain(api_key: str, url: str, limit: int = 10) -> list[ScrapedDoc]:
    """Faz crawl de um domínio inteiro (até `limit` páginas)."""
    app = FirecrawlApp(api_key=api_key)
    print(f"🕸️  Crawl: {url} (limite {limit} páginas)")

    def _run():
        return app.crawl_url(
            url,
            params={"limit": limit, "scrapeOptions": {"formats": ["markdown"]}},
        )

    result = _with_retry(_run, "crawl_url")

    # crawl_url devolve algo como {"status": ..., "data": [ {..}, {..} ]}
    pages = result.get("data", []) if isinstance(result, dict) else []
    docs: list[ScrapedDoc] = []
    for page in pages:
        doc = _extract_doc(page, url)
        if doc.markdown.strip():
            docs.append(doc)

    print(f"   → {len(docs)} páginas com conteúdo")
    return docs

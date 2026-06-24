"""vault-automator — entry point CLI.

Pipeline: Firecrawl scrape → Markdown formatado → Git commit → Push GitHub.
Modo digest: várias fontes → resumo do dia (Claude) → 1 nota.

Uso:
    python main.py scrape --url https://exemplo.com --tag medicina
    python main.py crawl  --url https://exemplo.com --limit 10 --tag concorrentes
    python main.py digest --area IA --tag ia --folder "Pesquisas/IA"
    python main.py sync
"""
from __future__ import annotations

import argparse
import sys

import feeds
import formatter
import git_sync
import scraper
import summarizer
from config import load_config

# Fontes que alimentam cada digest, indexadas por área (--area).
# Cada fonte é uma URL (str → scrape via Firecrawl) ou um dict
# {"url", "kind": "rss"|"scrape"}. RSS é lido por stdlib e NÃO gasta crédito.
# r/LocalLLaMA e X ficaram de fora do digest de IA por bloquearem scraping.
DIGEST_SOURCES = {
    "IA": [
        "https://techcrunch.com/category/artificial-intelligence/",
        "https://www.theverge.com/ai-artificial-intelligence",
        "https://tldr.tech/ai",
        "https://huggingface.co/models?sort=trending",
        "https://www.theresanaiforthat.com/",
    ],
    # Mercado Financeiro — fontes brasileiras e globais via RSS e scrape.
    "MercFin": [
        {"url": "https://www.infomoney.com.br/feed/", "kind": "rss"},
        {"url": "https://feeds.reuters.com/reuters/businessNews", "kind": "rss"},
        {"url": "https://www.cnbc.com/id/10000664/device/rss/rss.html", "kind": "rss"},
        {"url": "https://exame.com/mercados/", "kind": "scrape"},
        {"url": "https://br.investing.com/news/stock-market-news", "kind": "scrape"},
        {"url": "https://www.moneytimes.com.br/", "kind": "scrape"},
    ],
    # Medicina do Trabalho e Saúde Ocupacional — viés regulatório brasileiro.
    "MedTrab": [
        {"url": "https://www.anamt.org.br/portal/", "kind": "scrape"},
        {"url": "https://rbmt.org.br/", "kind": "scrape"},
        {"url": "https://www.segurancanotrabalho.com.br/", "kind": "scrape"},
        {"url": "https://portal.cfm.org.br/noticias/feed/", "kind": "rss"},
        {"url": "https://news.google.com/rss/search?q=medicina+do+trabalho+brasil&hl=pt-BR&gl=BR&ceid=BR:pt-419", "kind": "rss"},
        {"url": "https://news.google.com/rss/search?q=NR+segurança+saúde+trabalho+brasil&hl=pt-BR&gl=BR&ceid=BR:pt-419", "kind": "rss"},
    ],
    # Recém-Nascidos — saúde, desenvolvimento e orientação para pais.
    # Mix de fontes brasileiras (SBP, Fiocruz, Medscape PT) e internacionais (AAP, WHO, ScienceDaily).
    "RN": [
        {"url": "https://news.google.com/rss/search?q=rec%C3%A9m+nascido+neonatal+sa%C3%BAde+brasil&hl=pt-BR&gl=BR&ceid=BR:pt-419", "kind": "rss"},
        {"url": "https://news.google.com/rss/search?q=neonatologia+pediatria+beb%C3%AA+rec%C3%A9m+nascido&hl=pt-BR&gl=BR&ceid=BR:pt-419", "kind": "rss"},
        {"url": "https://www.sbp.com.br/noticias/", "kind": "scrape"},
        {"url": "https://www.jped.com.br/", "kind": "scrape"},
        {"url": "https://www.sciencedaily.com/rss/health_medicine/infant_and_toddler_health.xml", "kind": "rss"},
        {"url": "https://www.healthychildren.org/English/ages-stages/baby/Pages/default.aspx", "kind": "scrape"},
        {"url": "https://portugues.medscape.com/pediatria", "kind": "scrape"},
        {"url": "https://www.who.int/news/item/", "kind": "scrape"},
        {"url": "https://www.pais-e-filhos.com.br/bebe/", "kind": "scrape"},
        {"url": "https://agencia.fiocruz.br/rss.xml", "kind": "rss"},
    ],
    # Saúde (viés Brasil) + medicina com base científica.
    # RSS onde há feed noticioso bom; scrape onde não há.
    # gov.br: /RSS lista pastas por ano (inútil) → scrape. Medscape PT: sem feed → scrape.
    "Saude": [
        # Saúde geral
        {"url": "https://agencia.fiocruz.br/rss.xml", "kind": "rss"},
        {"url": "https://www.gov.br/saude/pt-br/assuntos/noticias", "kind": "scrape"},
        {"url": "https://saude.abril.com.br/feed/", "kind": "rss"},
        # Medicina / base científica
        {"url": "https://portal.cfm.org.br/noticias/feed/", "kind": "rss"},
        {"url": "https://portugues.medscape.com/", "kind": "scrape"},
        {"url": "https://www.sciencedaily.com/rss/health_medicine.xml", "kind": "rss"},
    ],
}


def _cmd_scrape(args, cfg) -> int:
    tag = args.tag or cfg.default_tag
    doc = scraper.scrape_url(args.url)
    if not doc.markdown.strip():
        print("❌ Scrape não retornou conteúdo.")
        return 1
    formatter.save_note(doc, cfg.notes_dir, tag)
    git_sync.sync(cfg.vault_path, cfg.git_branch, note_count=1)
    return 0


def _cmd_crawl(args, cfg) -> int:
    tag = args.tag or cfg.default_tag
    docs = scraper.crawl_domain(args.url, limit=args.limit)
    if not docs:
        print("❌ Crawl não retornou páginas com conteúdo.")
        return 1
    for doc in docs:
        formatter.save_note(doc, cfg.notes_dir, tag)
    git_sync.sync(cfg.vault_path, cfg.git_branch, note_count=len(docs))
    return 0


def _cmd_digest(args, cfg) -> int:
    tag = args.tag or cfg.default_tag
    notes_dir = cfg.vault_path / args.folder

    sources = DIGEST_SOURCES.get(args.area)
    if not sources:
        disponiveis = ", ".join(DIGEST_SOURCES)
        print(f"❌ Área sem fontes definidas: {args.area}. Disponíveis: {disponiveis}")
        return 2

    # 1. Coleta cada fonte: RSS (stdlib) ou scrape (Firecrawl).
    #    Falhas individuais não derrubam o digest.
    docs = []
    for src in sources:
        if isinstance(src, str):
            src = {"url": src, "kind": "scrape"}
        url, kind = src["url"], src.get("kind", "scrape")
        try:
            if kind == "rss":
                doc = feeds.fetch_feed(url)
            else:
                doc = scraper.scrape_url(url)
            if doc.markdown.strip():
                docs.append(doc)
        except Exception as err:  # noqa: BLE001
            print(f"⚠️  Pulei {url}: {err}")

    if not docs:
        print("❌ Nenhuma fonte retornou conteúdo.")
        return 1

    # 2. Claude sintetiza os tópicos do dia
    topics = summarizer.summarize_digest(
        cfg.gemini_api_key, docs, num_topics=args.topics, area=args.area
    )
    if not topics:
        print("❌ O resumo não gerou tópicos.")
        return 1

    # 3. Salva o digest e sincroniza
    formatter.save_digest(topics, notes_dir, tag, area=args.area)
    git_sync.sync(cfg.vault_path, cfg.git_branch, note_count=1)
    return 0


def _cmd_sync(args, cfg) -> int:
    git_sync.sync(cfg.vault_path, cfg.git_branch, note_count=0)
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="vault-automator",
        description="Firecrawl → Markdown → Git, automatizado.",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_scrape = sub.add_parser("scrape", help="Scrape de uma única URL")
    p_scrape.add_argument("--url", required=True)
    p_scrape.add_argument("--tag")
    p_scrape.set_defaults(func=_cmd_scrape)

    p_crawl = sub.add_parser("crawl", help="Crawl de um domínio inteiro")
    p_crawl.add_argument("--url", required=True)
    p_crawl.add_argument("--limit", type=int, default=10)
    p_crawl.add_argument("--tag")
    p_crawl.set_defaults(func=_cmd_crawl)

    p_digest = sub.add_parser("digest", help="Resumo do dia (várias fontes → Claude → 1 nota)")
    p_digest.add_argument("--area", default="IA", help="Nome da área (ex: IA)")
    p_digest.add_argument("--tag", help="Tag das notas (default: DEFAULT_TAG)")
    p_digest.add_argument("--folder", default="Pesquisas/IA", help="Subpasta de destino no vault")
    p_digest.add_argument("--topics", type=int, default=6, help="Quantidade de tópicos")
    p_digest.set_defaults(func=_cmd_digest)

    p_sync = sub.add_parser("sync", help="Só commita e dá push (sem scrape)")
    p_sync.set_defaults(func=_cmd_sync)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        cfg = load_config()
    except RuntimeError as err:
        print(f"❌ Configuração inválida: {err}")
        return 2

    return args.func(args, cfg)


if __name__ == "__main__":
    sys.exit(main())

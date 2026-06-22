"""vault-automator — entry point CLI.

Pipeline: Firecrawl scrape → Markdown formatado → Git commit → Push GitHub.

Uso:
    python main.py scrape --url https://exemplo.com --tag medicina
    python main.py crawl  --url https://exemplo.com --limit 10 --tag concorrentes
    python main.py sync   # só faz o git push, sem scrape
"""
from __future__ import annotations

import argparse
import sys

import formatter
import git_sync
import scraper
from config import load_config


def _cmd_scrape(args, cfg) -> int:
    tag = args.tag or cfg.default_tag
    doc = scraper.scrape_url(cfg.firecrawl_api_key, args.url)
    if not doc.markdown.strip():
        print("❌ Scrape não retornou conteúdo.")
        return 1
    formatter.save_note(doc, cfg.notes_dir, tag)
    git_sync.sync(cfg.vault_path, cfg.git_branch, note_count=1)
    return 0


def _cmd_crawl(args, cfg) -> int:
    tag = args.tag or cfg.default_tag
    docs = scraper.crawl_domain(cfg.firecrawl_api_key, args.url, limit=args.limit)
    if not docs:
        print("❌ Crawl não retornou páginas com conteúdo.")
        return 1
    for doc in docs:
        formatter.save_note(doc, cfg.notes_dir, tag)
    git_sync.sync(cfg.vault_path, cfg.git_branch, note_count=len(docs))
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
    p_scrape.add_argument("--url", required=True, help="URL a ser raspada")
    p_scrape.add_argument("--tag", help="Tag aplicada na nota (default: DEFAULT_TAG)")
    p_scrape.set_defaults(func=_cmd_scrape)

    p_crawl = sub.add_parser("crawl", help="Crawl de um domínio inteiro")
    p_crawl.add_argument("--url", required=True, help="URL base do domínio")
    p_crawl.add_argument("--limit", type=int, default=10, help="Máx. de páginas (default: 10)")
    p_crawl.add_argument("--tag", help="Tag aplicada nas notas (default: DEFAULT_TAG)")
    p_crawl.set_defaults(func=_cmd_crawl)

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

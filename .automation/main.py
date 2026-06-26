"""vault-automator — entry point CLI.

Pipeline: Firecrawl scrape → Markdown formatado → Git commit → Push GitHub.
Modo digest: várias fontes → resumo do dia (Gemini) → 1 nota.

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
    # IA — RSS confiáveis (sem dependência de scrape com JS pesado).
    "IA": [
        {"url": "https://techcrunch.com/category/artificial-intelligence/feed/", "kind": "rss"},
        {"url": "https://www.wired.com/feed/tag/ai/latest/rss", "kind": "rss"},
        {"url": "https://www.technologyreview.com/feed/", "kind": "rss"},
        {"url": "https://tecnoblog.net/feed/", "kind": "rss"},
        {"url": "https://news.google.com/rss/search?q=inteligencia+artificial+ia&hl=pt-BR&gl=BR&ceid=BR:pt-419", "kind": "rss"},
    ],
    # Saúde — RSS confiáveis (sem dependência de scrape com JS pesado).
    "Saude": [
        {"url": "https://g1.globo.com/dynamo/saude/rss2.xml", "kind": "rss"},
        {"url": "https://saude.abril.com.br/feed/", "kind": "rss"},
        {"url": "https://www.sciencedaily.com/rss/health_medicine.xml", "kind": "rss"},
        {"url": "https://news.google.com/rss/search?q=saude+medicina+brasil&hl=pt-BR&gl=BR&ceid=BR:pt-419", "kind": "rss"},
        {"url": "https://feeds.folha.uol.com.br/equilibrioesaude/rss091.xml", "kind": "rss"},
    ],
    # Medicina do Trabalho — fontes especializadas definidas pelo usuário.
    "MedTrab": [
        {"url": "https://abmt.org.br/noticias/", "kind": "scrape"},
        {"url": "https://www.anamt.org.br/portal/", "kind": "scrape"},
        {"url": "https://www.soc.com.br/", "kind": "scrape"},
        {"url": "https://revistaproteger.com.br/", "kind": "scrape"},
        {"url": "https://www.sesi.org.br/", "kind": "scrape"},
        {"url": "https://www.fundacentro.gov.br/", "kind": "scrape"},
        {"url": "https://sbmt.org.br/", "kind": "scrape"},
    ],
    # Mercado Financeiro — Brasil e global, RSS com artigos datados.
    "MercFin": [
        {"url": "https://news.google.com/rss/search?q=mercado+financeiro+bolsa+ibovespa+economia+brasil&hl=pt-BR&gl=BR&ceid=BR:pt-419", "kind": "rss"},
        {"url": "https://www.infomoney.com.br/feed/", "kind": "rss"},
        {"url": "https://rss.uol.com.br/feed/economia.xml", "kind": "rss"},
        {"url": "https://www.moneytimes.com.br/feed/", "kind": "rss"},
        {"url": "https://www.cnbc.com/id/10000664/device/rss/rss.html", "kind": "rss"},
    ],
    # Puerpério — 3º trimestre: exercícios, alimentação, dicas práticas, bem-estar.
    # Apenas RSS com pubDate para garantir conteúdo da semana.
    "Puerperio": [
        {"url": "https://news.google.com/rss/search?q=%22exercicios+para+gestantes%22+OR+%22yoga+gestante%22+OR+%22pilates+gravidez%22&hl=pt-BR&gl=BR&ceid=BR:pt-419", "kind": "rss"},
        {"url": "https://news.google.com/rss/search?q=%22alimentacao+na+gravidez%22+OR+%22o+que+comer+gravidez%22+OR+%22nutricao+gestante%22&hl=pt-BR&gl=BR&ceid=BR:pt-419", "kind": "rss"},
        {"url": "https://news.google.com/rss/search?q=%22dicas+para+gestantes%22+OR+%22cuidados+na+gravidez%22+OR+%22bem-estar+gestante%22&hl=pt-BR&gl=BR&ceid=BR:pt-419", "kind": "rss"},
        {"url": "https://news.google.com/rss/search?q=%22preparacao+para+o+parto%22+OR+%22saude+mental+gestante%22+OR+%22ansiedade+gravidez%22&hl=pt-BR&gl=BR&ceid=BR:pt-419", "kind": "rss"},
        {"url": "https://www.sciencedaily.com/rss/health_medicine/pregnancy_and_childbirth.xml", "kind": "rss"},
    ],
    # Filmes e Séries — lançamentos, críticas, notícias de streamings e cinema.
    "Filmes": [
        {"url": "https://omelete.com.br/feed/", "kind": "rss"},
        {"url": "https://cinepop.com.br/feed", "kind": "rss"},
        {"url": "https://variety.com/feed/", "kind": "rss"},
        {"url": "https://collider.com/feed/", "kind": "rss"},
        {"url": "https://news.google.com/rss/search?q=filmes+series+lancamento+streaming+cinema+netflix+disney&hl=pt-BR&gl=BR&ceid=BR:pt-419", "kind": "rss"},
    ],
    # Jogos — foco em PS5 e PC, feeds diários com artigos individuais.
    "Jogos": [
        {"url": "https://br.ign.com/feed.xml", "kind": "rss"},
        {"url": "https://www.eurogamer.net/?format=rss", "kind": "rss"},
        {"url": "https://www.pcgamer.com/rss/", "kind": "rss"},
        {"url": "https://www.destructoid.com/feed/", "kind": "rss"},
        {"url": "https://www.rockpapershotgun.com/feed/", "kind": "rss"},
    ],
    # Recém-Nascidos — cuidados práticos com RN, amamentação, desenvolvimento, sono.
    # Apenas RSS com pubDate para garantir conteúdo da semana.
    "RN": [
        {"url": "https://news.google.com/rss/search?q=%22cuidados+recem-nascido%22+OR+%22como+cuidar+do+bebe%22+OR+%22dicas+bebe%22&hl=pt-BR&gl=BR&ceid=BR:pt-419", "kind": "rss"},
        {"url": "https://news.google.com/rss/search?q=%22amamentacao%22+OR+%22aleitamento+materno%22+OR+%22leite+materno%22&hl=pt-BR&gl=BR&ceid=BR:pt-419", "kind": "rss"},
        {"url": "https://news.google.com/rss/search?q=%22desenvolvimento+bebe%22+OR+%22sono+bebe%22+OR+%22choro+bebe%22&hl=pt-BR&gl=BR&ceid=BR:pt-419", "kind": "rss"},
        {"url": "https://news.google.com/rss/search?q=%22vacina+bebe%22+OR+%22triagem+neonatal%22+OR+%22teste+pezinho%22&hl=pt-BR&gl=BR&ceid=BR:pt-419", "kind": "rss"},
        {"url": "https://www.sciencedaily.com/rss/health_medicine/infant_and_toddler_health.xml", "kind": "rss"},
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

    p_digest = sub.add_parser("digest", help="Resumo do dia (várias fontes → Gemini → 1 nota)")
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

# meu-vault

Vault do Obsidian versionado no Git. Sincroniza entre máquinas via `git pull`/`git push`
e recebe notícias raspadas automaticamente pelo Firecrawl via GitHub Actions.

## Estrutura

- `Research/` — notas raspadas automaticamente caem aqui
- `.automation/` — pipeline Python (Firecrawl → Markdown → Git)
- `.github/workflows/scrape.yml` — agendador na nuvem (cron diário às 8h BRT)

## Como sincronizar em outra máquina

```bash
git clone <url-do-repo> ~/vault
```

Depois abra essa pasta como vault no Obsidian e instale o plugin **Obsidian Git**
(ative "Pull on startup").

## Rodar a automação manualmente

GitHub → aba **Actions** → "Scrape para o vault" → **Run workflow**.

Detalhes do pipeline em [.automation/README](.automation/) (veja o projeto original).

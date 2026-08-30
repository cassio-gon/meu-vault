---
title: Health Check do Sync — 2026-08-30
date: 2026-08-30
area: Infra
tags: [infra, sync]
source: routine
---

# Health Check do Sync — 2026-08-30 (domingo, 20h BRT)

## TL;DR

**Semáforo geral: 🟡 AMARELO.** Mac saudável (commit real há ~4h48). Windows: reconciliado manualmente em 24/08 depois de ficar 25 dias travado (relatado em 08-23), sincronizou por ~20h e **voltou a ficar mudo** — 0 commits reais há **5 dias e 1h40** (ainda dentro do limite duro de 7 dias, mas é a 2ª vez que emperra em 5 semanas). Zero segredo novo na árvore, zero conflito real — mas os 6 segredos do relatório de 08-16 seguem só removidos da árvore (não do histórico, ~1,28 GiB), rotação ainda não confirmada: continuo reportando como **pendente**, não resolvido. Mismatch de doc do intervalo (15 min vs 60 min) chega à **7ª semana seguida** sem correção. Ação recomendada: `Get-ScheduledTaskInfo -TaskName ClaudeAutoSync` + `sync.log` no Windows.

Repo analisado: `claude-config`, só leitura. Clone chegou raso de novo (`git rev-parse --is-shallow-repository` = `true`); rodei `git fetch --unshallow` antes de qualquer check — sem isso o commit de fronteira do shallow apareceria como uma sincronização gigante fantasma e mascararia o gap real do Windows (já aconteceu em relatórios anteriores). Também desrasei `meu-vault` antes de escrever aqui, pelo mesmo motivo.

## Comparando com os checks anteriores (08-16, 08-23, hoje)

| | 08-16 | 08-23 | 08-30 (hoje) |
|---|---|---|---|
| Gap do Windows | ~434h (18d1h40) | ~602h (25d1h35) | **~121,7h (5d1h40) — melhorou muito, mas relapso** |
| Último commit real do Windows | `43e42f5` (29/07) | o mesmo `43e42f5` | **`e0f7e56` (25/08 18:37) — quebrou a sequência de 43e42f5, mas parou de novo 5 dias depois** |
| Commits reais do Windows (7 dias) | 0 | 0 | **6 — todos numa janela de ~20h em 24-25/08, zero depois** |
| Commits reais do Mac (7 dias) | — | 64 | **40 — cadência normal, sem buraco suspeito** |
| Segredos reais na árvore atual | 7 achados | 0 (limpeza de `.jsonl` em 22/08) | **0 — confirmado de novo, mesmos 6 seguem só no histórico** |
| Doc do intervalo (15 min vs 60 min) | mesmo mismatch (5ª semana) | mesmo mismatch (6ª semana) | **mesmo mismatch, 7ª semana seguida sem correção** |
| `.git` (histórico completo) | ~1,2 GB | ~1,4 GB | **~1,28 GiB (pack) — estável/leve queda, sem repack visível de encolhimento real** |
| Working tree | ~742 MB | ~113 MB | **~128 MB — voltou a crescer (+~15 MB), puxado por tool-results novos** |

## 1) Último commit por máquina + gap — 🟢 Mac / 🟡 Windows

- **Mac**: `6024b9b`, 2026-08-30 15:34:19 -03:00 (toca `projects/-Users-cassiogoncalves.../memory/...`) — **~4h48 atrás**. 🟢 Bem dentro do limite de 72h.
- **Windows**: `e0f7e56`, 2026-08-25 18:37:32 -03:00 — **~121,7h (5 dias e 1h40) atrás**. 🟡 Ainda **abaixo** do limite duro de 7 dias (168h), então não é alerta VERMELHO pela regra — mas é a 2ª vez em 5 semanas que o Windows para de commitar depois de ter sido "consertado", o que pesa mais que um número isolado sugere.

Contexto que encontrei no próprio histórico (não é conclusão minha, é o que o commit `b070169` diz): o Windows ficou travado em conflito de rebase **desde 10/08** porque os commits locais tocavam `.jsonl` que o Mac removeu do git em 21/08. Em **24/08 22:23** houve uma reconciliação manual (`chore: reconciliar Windows com o repo apos a faxina do Mac`, com backup preservado na branch `backup-windows-2026-08-24`) que realinhou o Windows com `origin/main`. Depois disso o auto-sync rodou normalmente por ~20h (6 commits reais entre 24/08 22:39 e 25/08 18:37) e então **parou de novo**, sem nenhum commit real desde então.

## 2) Frequência (7 dias) — 🟢 Mac / 🟡 Windows

- **Mac**: 40 commits reais (`A`/`M`) nos últimos 7 dias, distribuídos em todos os dias da semana (23/08 a 30/08), sem buraco suspeito — cadência compatível com o script só commitando quando há mudança de verdade.
- **Windows**: 6 commits reais, todos concentrados numa janela de ~20h logo após a reconciliação manual de 24/08 (22:39 → 25/08 18:37). Zero commits reais nos 5 dias seguintes. Não dá para saber daqui se é a task falhando de novo ou a máquina simplesmente desligada — ver seção "o que eu não consigo ver daqui".

## 3) Conflitos — 🟢

Busquei `<<<<<<<`, `=======`, `>>>>>>>` em início de linha nos arquivos rastreados (`git ls-files`, não o disco): nenhum marcador de merge real. As linhas `====`/`===========` que aparecem (em `commands/`, `skills/ecc/`, `scripts/hooks/insaits-security-monitor.py`, `workstations/B2B-Secretaria-IA/`, tool-results de sessão) são todas separadores decorativos de texto — conferi que nenhuma tem `<<<<<<<`/`>>>>>>>` como par. Zero `.orig`/`.rej` versionado.

## 4) Peso — 🟡 (achados repetidos, nenhum novo grave)

- `.git` completo: pack de **~1,28 GiB** (`git count-objects -v`), praticamente estável frente à semana passada (~1,4 GB) — a limpeza de `.jsonl` de 22/08 continua sem encolher o histórico (blobs antigos permanecem; o mesmo `.../e44b2ca3-....jsonl`, hoje pesando 70 MB no blob mais recente daquele caminho, segue lá).
- Working tree voltou a crescer: **~128 MB** (era ~113 MB em 08-23, +~15 MB). Maior parte é orgânica — dois arquivos novos >1 MB entraram nos últimos 7 dias, ambos sob `projects/.../tool-results/`: um `.txt` de 9,3 MB e um `.html` de artifact de 2,3 MB. Não violam o `.gitignore` (não são `.jsonl`), mas mostram que o peso pode voltar a subir aos poucos por esse canal.
- Zero mídia (`.pdf/.png/.jpg/.mp4/.mov`) escapada para dentro de `workstations/` — `.gitignore` cobrindo certo.
- Achados repetidos, ainda sem tratamento (mesmos de 08-23, tamanhos idênticos): os 3 `.zip` de sempre (`Kirvano/Secretaria-IA.zip` 7,3 MB, `Secretaria_IA/Secretaria_IA.zip` 64 KB, `Secretaria_IA_Design/WhatsApp message bubbles design.zip` 5,2 MB) fora das regras do `.gitignore`; `skills/playwright-skill/node_modules/` (171 arquivos) e `.profiles/` (296 arquivos, incluindo cache/perfil de navegador Chromium tipo `GraphiteDawnCache`, `BrowserMetrics-spare.pma`) continuam rastreados no repo de config.

## 5) Segredos — 🟡 (mesma pendência da semana passada, sem mudança)

Varri **apenas os arquivos rastreados** (`git ls-files`, nunca o disco) pelos padrões pedidos: `sk-`, `sk-ant-`, `gsk_` (Groq), `AIza` (Google), `ghp_`/`github_pat_`, `$aact_` (Asaas), `RESEND_`, `X-N8N-API-KEY`, `eyJ` (JWT de 3 segmentos), `password=`/`senha=`. **Zero achado real** — todo hit foi confirmado como falso positivo pelo contexto: nome de header/variável de ambiente mencionado em texto (`X-N8N-API-KEY`, `RESEND_API_KEY`), código de exemplo/fixture de teste em `skills/ecc/*` e `commands/kotlin-test.md`/`rust-test.md` (`password = "SecureP@ss1"` etc.), campo de formulário em capturas de tela de sessão (`const senha = ...`), redator de log (`post-bash-command-log.js` já mascara `password=` antes de logar). Confirmei também que nenhum `.jsonl` voltou a ser rastreado (`git ls-files | grep -c '\.jsonl$'` = 0) e nenhum arquivo com nome de segredo (`.env`, `credentials.json`, `.key`, `.pem`, `settings.local.json`) está versionado.

**Isso não muda o status dos 6 segredos que o relatório de 08-16 encontrou** (2× OpenAI `sk-proj-`, 2× Anthropic `sk-ant-api03-`, Groq `gsk_`, OpenRouter `sk-or-v1-`) e que a limpeza de `.jsonl` de 22/08 tirou da árvore como efeito colateral: eles seguem **recuperáveis no histórico** (mesmos blobs, não houve `filter-repo`/BFG — nem deveria ser feito aqui sem decisão explícita do Cássio, é destrutivo e conflitaria com o auto-sync das duas máquinas). Nada nos commits desta semana indica rotação. **Continuo reportando como pendente, não resolvido**, até haver algum sinal de rotação nos provedores.

## 6) Integridade — 🟡

- `settings.json`: JSON válido. 🟢
- `CLAUDE.md` e `workstations/CLAUDE.md`: existem, ambos. 🟢
- **Mesmo mismatch de documentação, agora 7ª semana seguida sem correção**: `CLAUDE.md` (raiz) diz "a cada 1h" para as duas máquinas; `WINDOWS-SETUP.md` configura de fato `-RepetitionInterval (New-TimeSpan -Minutes 60)` com o comentário "intervalo atual: 60 min" (linha 94-97) — mas o título da própria seção 4 ainda diz "Agendar a cada 15 min" (linha 86), e o cabeçalho de `scripts/sync/windows-auto-sync.ps1` (linha 2) ainda diz "Agendado pelo Task Scheduler a cada 15 min". Cosmético (o comando real usa 60 min), mas seria um bom momento para corrigir já que o Windows vai precisar de atenção manual de qualquer forma.

## O que eu não consigo ver daqui

Rodo na nuvem e só enxergo o repositório git `claude-config` (e, para entregar este relatório, `meu-vault`). **Não tenho acesso** ao LaunchAgent do Mac (`com.cassio.claude-autosync`), à task `ClaudeAutoSync` do Windows, nem a `~/.claude/.autosync/sync.log` — esse log é local-only, fora do git, e é o único lugar que mostraria se a task do Windows está: (a) desabilitada, (b) habilitada mas falhando de novo (rede/git/auth — o mesmo tipo de trava de rebase que já aconteceu em 10/08), ou (c) a máquina simplesmente não liga há 5 dias. Também não enxergo o que sincroniza por Syncthing (mídia e transcritos `.jsonl` desde 22/08) — não afirmo nada sobre esse canal, só sobre o git. Não sei se as 6 chaves do achado de 08-16 foram rotacionadas — só que os blobs continuam recuperáveis.

```powershell
# Windows — confirmar se a task ainda existe, está habilitada e sem erro
Get-ScheduledTaskInfo -TaskName ClaudeAutoSync
Get-ScheduledTask -TaskName ClaudeAutoSync | Select State
Get-Content "$env:USERPROFILE\.claude\.autosync\sync.log" -Tail 30
```

```bash
# Mac — só para confirmar que o lado dele segue saudável (os commits recentes já indicam que sim)
launchctl print gui/$(id -u)/com.cassio.claude-autosync
tail -30 ~/.claude/.autosync/sync.log
```

Se `Get-ScheduledTaskInfo` mostrar `LastTaskResult` diferente de 0, ou `State` diferente de `Ready`, é isso que explica o silêncio recorrente. Se a task estiver `Ready` e `LastTaskResult 0` mas sem commits novos há 5 dias, o problema é outro (rede/git auth de novo, ou a máquina não liga) — e o `sync.log` deve mostrar o erro, ou nem existir se a task não rodou nesse período.

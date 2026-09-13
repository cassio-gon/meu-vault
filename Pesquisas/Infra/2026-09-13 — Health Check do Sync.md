---
title: Health Check do Sync — 2026-09-13
date: 2026-09-13
area: Infra
tags: [infra, sync]
source: routine
---

# Health Check do Sync — 2026-09-13 (domingo, 20h BRT)

## TL;DR

**Semáforo geral: 🔴 VERMELHO — não pelo sync, pelo segredo Chatwoot que segue exposto.** Mac (commit real há ~5h36) e Windows (~29h30) estão saudáveis, dentro dos limites. O achado: o token Chatwoot real `THp1QBPDo26byUHmTfqVzC9q` saiu do texto de `Secretaria_IA/MEMORY.md` (onde o check de 09-06 o flagrou) mas **continua em texto puro em 3 arquivos JSON de workflow** (`onboarding_workflow.json` e duas cópias), como `defaultValue` do campo "API Token Chatwoot" — presente desde o commit inicial do repo (30/06), nunca rotacionado. Some da doc não é o mesmo que resolver. Os 6 segredos de 08-16 (OpenAI/Anthropic/Groq/OpenRouter) seguem só recuperáveis no histórico, sem sinal de rotação — 9ª semana como pendente. Zero conflito real. Mismatch do intervalo (15 min vs 60 min) chega à **9ª semana sem correção**. Ação recomendada: remover/rotacionar o token Chatwoot nos 3 JSONs e confirmar rotação das 6 chaves antigas.

Repo analisado: `claude-config`, só leitura. Clone chegou raso de novo — rodei `git fetch --unshallow` antes de qualquer check.

## Comparando com o check anterior (09-06)

| | 09-06 | 09-13 (hoje) |
|---|---|---|
| Gap do Mac | ~22h | **~5h36 — 🟢** |
| Gap do Windows | ~26h | **~29h30 — 🟢** |
| Último commit real do Mac | `df18ed5` (05/09 22:10) | **`c257550` (13/09 14:36:57)** |
| Último commit real do Windows | `b155807` (05/09 17:39) | **`dd35a96` (12/09 14:39:47)** |
| Commits reais do Mac (7 dias) | 34 | **7 — cadência bem mais baixa, com buraco 09-09/09-11** |
| Commits reais do Windows (7 dias) | 27 | **15 — cadência normal, sem buraco preocupante** |
| Segredos reais na árvore | 1 achado novo (Chatwoot, em MEMORY.md) + 6 antigos pendentes | **o mesmo token Chatwoot, agora localizado em 3 JSONs (não mais em MEMORY.md) + os mesmos 6 antigos — nenhum rotacionado** |
| Pasta-mistério `projects/-/*` (origem não identificada) | 26 arquivos, sem explicação | **0 arquivos — sumiu, sem explicação de causa daqui** |
| Doc do intervalo (15 min vs 60 min) | 8ª semana sem correção | **9ª semana sem correção** |
| `.git` (pack) | ~978 MiB | **~977,75 MiB — estável** |
| Working tree (sem `.git`) | ~190 MB | **~81 MB — caiu bastante, sem conseguir atribuir a causa daqui** |

## 1) Último commit por máquina + gap — 🟢 Mac / 🟢 Windows

- **Mac**: `c257550`, 2026-09-13 14:36:57 -03:00 (toca `projects/-Users-cassiogoncalves-Developer-remoto/memory/MEMORY.md` e `remoto-windows-sem-imagem.md`) — **~5h36 atrás**. Bem dentro do limite de 72h.
- **Windows**: `dd35a96`, 2026-09-12 14:39:47 -03:00 (toca `projects/c--Users-C-ssio--claude/memory/MEMORY.md` e adiciona `sem-alerta-token-exposto.md`) — **~29h30 atrás**. Bem dentro do limite de 7 dias.

Nota: esse mesmo commit `dd35a96` também toca arquivos sob o prefixo do Mac (`projects/-Users-cassiogoncalves.../memory/*.md`, removendo linhas) — um único commit com edições atribuíveis aos dois prefixos ao mesmo tempo. Não consigo explicar esse padrão daqui (os dois processos de auto-sync deveriam, a princípio, commitar só o que é local à própria máquina); vale o Cássio confirmar se isso é esperado (ex.: reconciliação manual) ou se aponta pra alguma configuração cruzando as duas árvores.

## 2) Frequência (7 dias) — 🟡 Mac (buraco no meio da semana) / 🟢 Windows

Commits reais (`A`/`M` sob o prefixo de cada máquina) nos últimos 7 dias, em ordem:

| Data/hora | Máquina |
|---|---|
| 09-07 07:39 até 09-08 23:39 (9 commits) | Windows |
| 09-07 15:32, 09-08 07:32/09:33/17:33 (4 commits) | Mac |
| 09-09 22:39 | Windows |
| 09-10 01:39 | Windows |
| 09-11 21:39 | Windows |
| **09-09, 09-10, 09-11 — zero commits reais do Mac** | — |
| 09-12 14:39 | Mac + Windows (mesmo commit, ver nota acima) |
| 09-13 13:36, 14:36 | Mac (2 commits) |

Mac: 7 commits reais na semana, com um **buraco de ~93h (09-08 17:33 → 09-12 14:39, quase 4 dias) sem nenhum commit real**. Isso não violou o limite de alerta (72h é medido a partir de agora, não do meio da semana) e é consistente com o Mac simplesmente não ter sido usado nesse intervalo (fim de semana) — não dá pra saber daqui se o LaunchAgent continuou rodando silenciosamente (sem mudança = sem commit) ou parou. Vale conferir localmente se achar estranho.

Windows: 15 commits reais, razoavelmente espalhados, sem buraco que se aproxime do limite de 7 dias.

## 3) Conflitos — 🟢

Busquei `<{7}`/`={7}`/`>{7}` em início de linha nos arquivos rastreados (`git ls-files`, não o disco). Isolando os marcadores inequívocos `<<<<<<<` e `>>>>>>>` (os `=======`/`===...===` soltos são separador decorativo em `commands/`, `skills/ecc/*`, `scripts/hooks/insaits-security-monitor.py` etc.): **zero ocorrência real**. Zero `.orig`/`.rej` versionado.

## 4) Peso — 🟢

- `.git`: pack de **~977,75 MiB** (`git count-objects -vH`, 15380 objetos em 3 packs) — estável frente aos ~978 MiB de 09-06. Os blobs grandes (`.jsonl` antigos de antes de 22/08, um deles com blobs de até ~70 MB) seguem só no histórico; nenhum sinal de crescimento novo relevante.
- Working tree ~81 MB (excluindo `.git`) — caiu de ~190 MB na semana passada; não consigo atribuir a causa exata daqui (arquivos temporários de sessão que saíram do índice, por exemplo). Nenhum arquivo novo >600 KB introduzido nos commits dos últimos 7 dias, exceto `workstations/_arquivo/cha-de-bebe/cha-bebe-chat.html` (~607 KB, HTML de chat arquivado, sem novidade preocupante).
- Zero mídia (`.pdf/.png/.jpg/.mp4/.mov`) escapada para dentro de `workstations/` — os mesmos 4 `.zip` de sempre (`Gravador-Tela`, `Kirvano/Secretaria-IA.zip`, `Secretaria_IA.zip`, `WhatsApp message bubbles design.zip`), sem novidade. Os 7 arquivos de mídia rastreados no repo inteiro estão todos sob `skills/` (assets de exemplo de skills, ex. `skills/last30days/assets/*`), fora da regra que cobre só `workstations/`.
- A pasta-mistério `projects/-/*` (26 arquivos sem prefixo de Mac nem de Windows, relatada em 09-06) **sumiu — 0 arquivos hoje**. Não sei explicar a causa daqui (limpeza manual, ou os arquivos nunca tinham ficado na árvore atual); reporto como resolvida por ora, sem certeza da causa.

## 5) Segredos — 🔴 (o mesmo achado de 09-06 não foi resolvido, só mudou de lugar)

Varri **apenas os arquivos rastreados** (`git ls-files`/`git grep`, nunca o disco) pelos padrões pedidos: `sk-`, `sk-ant-`, `gsk_`, `AIza`, `ghp_`/`github_pat_`, `$aact_`, `RESEND_`, `X-N8N-API-KEY`, `eyJ` (JWT), tokens de Chatwoot, `password=`/`senha=`.

**Achado confirmado, real, ainda na árvore atual:**

- O token real `THp1QBPDo26byUHmTfqVzC9q` (o mesmo achado em `Secretaria_IA/MEMORY.md:99` no check de 09-06) **não está mais nesse arquivo** — mas está, em texto puro, como `defaultValue` do campo `"fieldLabel": "API Token Chatwoot"` (placeholder "Token de acesso da conta Chatwoot") em **3 arquivos JSON de workflow n8n**:
  - `workstations/Secretaria_IA/onboarding_workflow.json:69`
  - `workstations/Secretaria_IA/templates/workflows_v2/onboarding_workflow.json:69`
  - `workstations/Secretaria_IA/workflows-backup/2026-06-19/Onboarding — Secretaria IA__oLN9pPZPLIUhitW3.json:69` (e de novo na linha 962)
  - `git log --follow` mostra que esses arquivos estão na árvore desde o **commit inicial do sync** (`c3ab5a8`, 30/06/2026) — ou seja, o valor real nunca saiu do repo, só a menção dele em texto no MEMORY.md. Isso é **pior**, não melhor, que o achado de 09-06: é um valor pré-preenchido (`defaultValue`) de um formulário de onboarding, ou seja, pronto para uso caso alguém rode o workflow.
  - Confirmei não ser exemplo/fixture: o campo é claramente rotulado como token real de uma conta Chatwoot específica, e o valor bate exatamente com o já documentado como "potencialmente comprometido" desde 24/06.

**Não é achado novo, mas segue confirmado como falso positivo:** a tabela "Credenciais importantes (n8n)" em `Secretaria_IA/MEMORY.md` (por ex. `apikey` → `oA4QEb7NzJ1D5dhE`, `Chatwoot Agente` → `xCYMUWtx3cEYzwKA`) — esses valores têm formato de **ID de credencial do n8n** (identificador interno do objeto salvo no cofre de credenciais do n8n), não o token/segredo em si; o padrão de nomenclatura (`Nome na UI | ID | Tipo`) e o uso no texto ("credencial `apikey` (`oA4QEb7NzJ1D5dhE`)") confirmam que é um ponteiro, não a chave. Resto do restante seguiu limpo pelo mesmo critério de sempre (nome de header/env var, código de exemplo em `skills/ecc/*`, fixtures em `django-tdd`, etc.). Confirmei de novo que nenhum `.jsonl` está rastreado (`git ls-files | grep -c '\.jsonl$'` = 0) e o `.gitignore` ainda cobre `projects/**/*.jsonl`.

**Isso não muda o status dos 6 segredos do achado de 08-16** (2× OpenAI `sk-proj-`, 2× Anthropic `sk-ant-api03-`, Groq `gsk_`, OpenRouter `sk-or-v1-`): seguem **recuperáveis no histórico**, sem sinal de rotação nos commits desta semana. Continuo reportando como **pendente** — 9ª semana desde o achado original (08-16).

## 6) Integridade — 🟡

- `settings.json`: JSON válido. 🟢
- `CLAUDE.md` (raiz) e `workstations/CLAUDE.md`: existem, ambos. 🟢
- **Mesmo mismatch de documentação do intervalo, agora 9ª semana seguida sem correção**: `CLAUDE.md` diz "a cada 1h" para as duas máquinas; `WINDOWS-SETUP.md` configura de fato 60 min (linha ~97, comentário "intervalo atual: 60 min") — mas o título da seção 4 (linha 86) ainda diz "Agendar a cada 15 min", e o cabeçalho de `scripts/sync/windows-auto-sync.ps1` (linha 2) também ainda diz "a cada 15 min". Cosmético (o comando real usa 60 min), mas nove semanas é tempo mais que suficiente pra um ajuste de duas linhas.

## O que eu não consigo ver daqui

Rodo na nuvem e só enxergo o repositório git `claude-config` (e, para entregar este relatório, `meu-vault`). **Não tenho acesso** ao LaunchAgent do Mac (`com.cassio.claude-autosync`), à task `ClaudeAutoSync` do Windows, nem a `~/.claude/.autosync/sync.log` — local-only, fora do git. Também não enxergo o que sincroniza por Syncthing (mídia e transcritos `.jsonl`). Não sei se o token Chatwoot `THp1...` ou as 6 chaves de 08-16 foram rotacionados — só que os valores continuam recuperáveis/presentes. Não sei explicar por que o commit `dd35a96` mistura prefixos de Mac e Windows, nem por que a pasta-mistério `projects/-/*` sumiu, nem por que o working tree caiu de ~190 MB para ~81 MB nesta semana.

```bash
# Ação prioritária desta semana: remover/rotacionar o token Chatwoot
# THp1QBPDo26byUHmTfqVzC9q dos 3 JSONs (onboarding_workflow.json e cópias)
# e confirmar rotação das 6 chaves de 08-16.
```

```powershell
# Windows — confirmação de rotina
Get-ScheduledTaskInfo -TaskName ClaudeAutoSync
Get-Content "$env:USERPROFILE\.claude\.autosync\sync.log" -Tail 30
```

```bash
# Mac — confirmação de rotina
launchctl print gui/$(id -u)/com.cassio.claude-autosync
tail -30 ~/.claude/.autosync/sync.log
```

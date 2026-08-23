---
title: Health Check do Sync — 2026-08-23
date: 2026-08-23
area: Infra
tags: [infra, sync]
source: routine
---

# Health Check do Sync — 2026-08-23 (domingo, 20h BRT)

**Semáforo geral: 🔴 VERMELHO** — o Windows segue sem nenhum commit real desde **29/07** (mesmo commit `43e42f5` de sempre): o gap passou de **18 dias** (relatado em 08-16) para **25 dias e 1h35** — 3ª semana seguida em zero. É o único critério de prioridade alta batido esta semana (mais de 7 dias parado); não achei segredo novo nem conflito real. Do lado bom: a limpeza de `.jsonl` do dia 22/08 (documentada no `CLAUDE.md`) tirou da árvore rastreada **todos os 6 segredos** que o relatório passado tinha listado — mas eles continuam recuperáveis no histórico do git, e não tenho como confirmar se foram rotacionados de verdade.

Repo analisado: `claude-config`, só leitura. **Importante sobre metodologia:** o clone chegou raso de novo (`git rev-parse --is-shallow-repository` = `true`, boundary em `e5e755cd`, 08-18) — se eu não tivesse rodado `git fetch --unshallow` antes de fechar os checks 1/2/4, o commit de fronteira do shallow clone (2991 arquivos, todos aparecendo como "Added" por falta de pai pra comparar) teria sido lido como uma megassincronização real do Windows em 18/08, mascarando os 25 dias de silêncio real. Depois do unshallow (543 commits, volta a 30/06), apliquei a mesma regra do relatório anterior: só conta como "commit real de uma máquina" o que **adiciona ou modifica** (`A`/`M`) arquivo sob o prefixo de pasta daquela máquina — nunca `D` isolado, que é reconciliação/limpeza, não sincronização.

## Comparando com os checks anteriores (08-02, 08-09, 08-16)

| | 08-02 | 08-09 | 08-16 | 08-23 (hoje) |
|---|---|---|---|---|
| Gap do Windows | ~97h (4d1h30) | ~266h (11d2h) | ~434h (18d1h40) | **~602h (25d1h35) — piorou de novo** |
| Último commit real do Windows | `43e42f5` (29/07) | o mesmo | o mesmo | **o mesmo `43e42f5` — 4ª semana seguida sem nenhum commit novo** |
| Commits reais do Windows (7 dias) | 10 (2 rajadas) | 0 | 0 | **0 — 3ª semana seguida em zero** |
| Segredos reais na árvore atual | +1 (OpenRouter) | 5+ achados | 7 achados (2 novos coladas em 13/08) | **0 na árvore — os 6 do relatório passado saíram junto da limpeza de `.jsonl` (22/08); seguem no histórico** |
| Doc do intervalo (15 min vs 60 min) | mesmo mismatch | mesmo mismatch (4ª semana) | mesmo mismatch (5ª semana) | **mesmo mismatch, 6ª semana seguida sem correção** |
| `.git` (histórico completo) | ~506 MB | ~927 MB | ~1,2 GB | **~1,4 GB — continua crescendo (o histórico antigo não encolheu com a limpeza)** |
| Working tree | — | — | ~742 MB | **~113 MB — despencou por causa da limpeza de `.jsonl`** |

Resumo da semana: o problema crônico (Windows mudo) não foi tocado e piorou; o problema mais grave do relatório anterior (segredos reais na árvore) foi mitigado por um efeito colateral de uma limpeza que não tinha esse objetivo — não posso chamar isso de "resolvido" porque não sei se as chaves foram rotacionadas nem se alguém que já clonou o repo completo ainda tem os blobs antigos.

## 1) Último commit por máquina + gap — 🟢 Mac / 🔴 Windows

- **Mac**: `bf3c742`, 2026-08-23 18:59:29 -03:00 (modifica `projects/.../memory/rotinas-nuvem-agendadas.md`) — **~1h20 atrás**. 🟢
- **Windows**: `43e42f5`, 2026-07-29 18:39:49 -03:00 — **~602h (25 dias e 1h35) atrás**. Mais de **3,5×** o limite duro de 7 dias.

(Confirmei manualmente que `bf3c742` tem conteúdo real — 1 `M` sob o prefixo do Mac — e não é só reconciliação: o resto do commit é 38 `D` + 6 `R100`, limpeza/renomeação contínua.)

## 2) Frequência (7 dias) — 🟢 Mac / 🔴 Windows

- **Mac**: 64 commits reais (`A`/`M`) nos últimos 7 dias, cadência horária normal, sem buracos suspeitos (maior intervalo entre commits com mudança real foi de poucas horas, esperado já que o script só commita quando há algo pra sincronizar).
- **Windows**: **zero** commits reais nos últimos 7 dias — 3ª semana seguida em zero, contando desde 08-09.

## 3) Conflitos — 🟢

Busquei `<<<<<<<`, `=======`, `>>>>>>>` em início de linha nos arquivos rastreados (`git ls-files`, não o disco): nenhuma ocorrência real de marcador de merge — as únicas linhas `====` que aparecem em `commands/`/`skills/ecc/` são separadores de documentação, contexto conferido um a um. Zero `.orig`/`.rej` versionados.

## 4) Peso — 🟡

- `.git` com histórico completo: **~1,4 GB** (era ~1,2 GB há uma semana — mais ~17%). A limpeza de `.jsonl` de 22/08 **não** encolheu isso: ela tira arquivo do commit mais recente, mas os blobs antigos (inclusive os que acabaram de ser removidos) continuam para sempre no histórico sem reescrita (`git filter-repo`/BFG) — o mesmo blob de 66,8 MB do arquivo `.../e44b2ca3-....jsonl` que o relatório de 08-16 já tinha achado continua lá.
- Working tree: **~113 MB**, caiu de ~742 MB — efeito direto e esperado da limpeza (0 `.jsonl` rastreado no HEAD atual; confirmei que nenhum `.jsonl` novo voltou a ser commitado depois da limpeza).
- Mídia binária (`.pdf/.png/.jpg/.mp4/.mov`) dentro de `workstations/`: nenhuma fora do esperado — `.gitignore` cobrindo certo.
- Mesmos 3 `.zip` de sempre, tamanhos idênticos aos de 08-16: `Kirvano/Secretaria-IA.zip` (7,3 MB), `Secretaria_IA/Secretaria_IA.zip` (64 KB), `Secretaria_IA_Design/WhatsApp message bubbles design.zip` (5,2 MB) — achado repetido, `.zip` ainda fora das regras do `.gitignore`.
- `skills/playwright-skill/node_modules/` (171 arquivos) e `.profiles/` (296 arquivos) continuam rastreados — achado repetido, sem confirmação se é intencional.

## 5) Segredos — 🟡 (achado principal da semana: sumiram da árvore, mas não do histórico)

Varri todos os arquivos rastreados (`git ls-files`, nunca o disco) pelos padrões pedidos: `sk-`, `sk-ant-`, `gsk_`, `AIza`, `ghp_`/`github_pat_`, `$aact_`, `RESEND_`, `X-N8N-API-KEY`, `eyJ` (JWT de verdade, com os 3 segmentos), `password=`, `senha=`. Zero achado real — todo hit foi falso positivo confirmado pelo contexto (placeholder de doc como `sk-proj-xxxxx`, nome de variável de ambiente como `RESEND_API_KEY`/`X-N8N-API-KEY`, coluna de banco `env_senha`, ou texto de um bundle JS minificado de terceiro em `jspdf.umd.min.js`).

Isso é uma mudança real: os **6 segredos** que o relatório de 08-16 tinha listado por arquivo:linha (2× OpenAI `sk-proj-`, 2× Anthropic `sk-ant-api03-` — uma antiga de 24/07 e uma nova de 13/08 —, Groq `gsk_`, OpenRouter `sk-or-v1-`, Asaas homologação `$aact_hmlg_`) estavam **todos** em arquivos `.jsonl` sob `projects/`. A limpeza de `.jsonl` do commit `d626532` (22/08, 428 remoções) tirou a árvore rastreada inteira de `.jsonl` — confirmei `git ls-files | grep -c '\.jsonl$'` = 0 no HEAD atual, e nenhum `.jsonl` novo foi commitado depois disso.

**Por que isso é 🟡 e não 🟢:** a limpeza foi feita por peso (o `.gitignore` documenta isso explicitamente: "870 MB de 881 MB... travou o sync"), não por segurança — é um efeito colateral, não uma resposta ao alerta de segredo. Duas coisas continuam em aberto que eu não consigo confirmar daqui:
1. **Rotação**: nada nos commits indica se as 6 chaves foram revogadas/rotacionadas nos provedores. Se não foram, elas continuam válidas onde quer que estejam, independente de estarem na árvore do git ou não.
2. **Histórico**: remover da árvore e commitar não apaga o blob do histórico. Quem tiver (ou já tirou) um clone completo do repo antes de 22/08 — ou até depois, já que o histórico não foi reescrito — ainda consegue recuperar os valores originais via `git show <commit-antigo>:<caminho>`. Não fiz `filter-repo`/BFG aqui (destrutivo, conflitaria com o auto-sync das duas máquinas) — só confirmo que ninguém mais fez isso também.

**Ação recomendada, ainda válida independente da limpeza de árvore:** se as 6 chaves (2× OpenAI, 2× Anthropic, Groq, OpenRouter — a Asaas é de homologação, risco menor) do relatório de 08-16 ainda não foram rotacionadas, rotacionar agora. A limpeza de peso não substitui isso.

## 6) Integridade — 🟡

- `settings.json`: JSON válido. 🟢
- `CLAUDE.md` e `workstations/CLAUDE.md`: existem, ambos. 🟢
- **Mesmo mismatch de documentação, 6ª semana seguida sem correção**: `CLAUDE.md` diz "a cada 1h" e o próprio `WINDOWS-SETUP.md` (passo 4, bloco de código) configura `-RepetitionInterval (New-TimeSpan -Minutes 60)` com o comentário "intervalo atual: 60 min" — mas o título da seção 4 ainda diz "Agendar a cada 15 min" e o cabeçalho de `scripts/sync/windows-auto-sync.ps1` (linha 2) ainda diz "Agendado pelo Task Scheduler a cada 15 min". Cosmético, não é a causa do gap de 25 dias, mas seria um bom momento pra corrigir já que a task do Windows vai precisar de atenção manual mesmo.

## O que eu não consigo ver daqui

Rodo na nuvem e só enxergo o repositório git `claude-config`. **Não tenho acesso** ao LaunchAgent do Mac (`com.cassio.claude-autosync`), à task `ClaudeAutoSync` do Windows, nem a `~/.claude/.autosync/sync.log` — esse log é local-only, fora do git, e é o único lugar que mostraria se a task do Windows está: (a) desabilitada, (b) habilitada mas falhando (rede/git/auth), ou (c) a máquina simplesmente não liga há 25 dias. Também não enxergo o que sincroniza por Syncthing (mídia e transcritos `.jsonl` desde 22/08) — não posso afirmar nada sobre esse canal, só sobre o git. Não posso afirmar qual dos três casos acima é o do Windows — só afirmo o que os commits provam: 25 dias corridos sem nenhum commit real, pior número desde que este health check começou.

```powershell
# Windows — confirmar se a task scheduled ainda existe e está habilitada
Get-ScheduledTaskInfo -TaskName ClaudeAutoSync
Get-ScheduledTask -TaskName ClaudeAutoSync | Select State
Get-Content "$env:USERPROFILE\.claude\.autosync\sync.log" -Tail 30
```

```bash
# Mac — só pra confirmar que o lado dele está saudável (os commits recentes já indicam que sim)
launchctl print gui/$(id -u)/com.cassio.claude-autosync
tail -30 ~/.claude/.autosync/sync.log
```

Se `Get-ScheduledTaskInfo` mostrar `LastTaskResult` diferente de 0, ou `State` diferente de `Ready`, é isso que explica o silêncio. Se a task estiver `Ready` e `LastTaskResult 0` mas sem commits novos há 25 dias, o problema é outro (rede/git auth, ou a máquina não liga há semanas) e o `sync.log` deve mostrar o erro — ou nem existir, se a task nunca rodou nesse período.

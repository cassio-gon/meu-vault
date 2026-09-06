---
title: Health Check do Sync — 2026-09-06
date: 2026-09-06
area: Infra
tags: [infra, sync]
source: routine
---

# Health Check do Sync — 2026-09-06 (domingo, 20h BRT)

## TL;DR

**Semáforo geral: 🔴 VERMELHO — não pelo sync, pelo achado de segredo.** Mac e Windows estão saudáveis (commit real há ~22h e ~26h, ambos dentro do limite; Windows se recuperou bem do problema das últimas semanas). O motivo do vermelho: `workstations/Secretaria_IA/MEMORY.md:99` tem, em texto puro, um token Chatwoot real (`THp1...`) — não é falso positivo, é o próprio arquivo dizendo "token exposto em chat... potencialmente comprometido" e pedindo pra regenerar, só que isso nunca foi feito e o token continua na árvore há ~7 semanas. Além disso, os 6 segredos do achado de 08-16 (OpenAI/Anthropic/Groq/OpenRouter) seguem só removidos da árvore, não do histórico — sem sinal de rotação, continuo reportando como **pendente**. Zero conflito real. Mismatch de doc do intervalo (15 min vs 60 min) chega à 8ª semana sem correção. Ação recomendada pro Cássio: regenerar o token Chatwoot no `Secretaria_IA/MEMORY.md:99` e confirmar rotação das 6 chaves antigas.

Repo analisado: `claude-config`, só leitura. Clone chegou raso de novo — rodei `git fetch --unshallow` antes de qualquer check.

## Comparando com o check anterior (08-30)

| | 08-30 | 09-06 (hoje) |
|---|---|---|
| Gap do Mac | ~4h48 | **~22h — segue 🟢** |
| Gap do Windows | ~121,7h (5d1h40), parado | **~26h — recuperou, 🟢** |
| Último commit real do Windows | `e0f7e56` (25/08) | **`b155807` (05/09 17:39)** |
| Commits reais do Mac (7 dias) | 40 | **34 — cadência normal** |
| Commits reais do Windows (7 dias) | 6 (só numa janela de 20h) | **27 — espalhados pela semana, sem buraco** |
| Segredos reais na árvore | 0 achado novo (6 antigos pendentes) | **1 achado NOVO real (Chatwoot) + os mesmos 6 antigos pendentes** |
| Doc do intervalo (15 min vs 60 min) | 7ª semana sem correção | **8ª semana sem correção** |
| `.git` (pack) | ~1,28 GiB | **~978 MiB** (não sei precisar a causa daqui — pode ser repack do lado do GitHub; nenhum sinal de reescrita de histórico local) |

## 1) Último commit por máquina + gap — 🟢 Mac / 🟢 Windows

- **Mac**: `df18ed5`, 2026-09-05 22:10:14 -03:00 (`projects/-Users-cassiogoncalves.../tool-results/...additionalContext.txt`) — **~22h atrás**. Bem dentro do limite de 72h.
- **Windows**: `b155807`, 2026-09-05 17:39:48 -03:00 (toca `tool-results/`, `.temp-execution-*.js` e `Medicina Ocupacional/DORTPREV/MEMORY.md`) — **~26h atrás**. Bem dentro do limite de 7 dias, e uma boa recuperação frente ao gap de 5 dias relatado em 08-30.

## 2) Frequência (7 dias) — 🟢 Mac / 🟢 Windows

Distribuição diária de commits reais (`A`/`M` sob o prefixo de cada máquina), últimos 7 dias:

| Data | Mac | Windows |
|---|---|---|
| 08-31 | 14 | 3 |
| 09-01 | 4 | 4 |
| 09-02 | 2 | 6 |
| 09-03 | 6 | 6 |
| 09-04 | 1 | 1 |
| 09-05 | 3 | 3 |
| 09-06 (parcial, até 20h) | 0 | 0 |

Sem buraco suspeito no meio da semana em nenhuma das duas — o Windows, que vinha emperrando repetidamente nas últimas semanas, voltou a commitar todos os dias. Zero commits reais hoje (09-06) até o horário do check é esperado (dia ainda em andamento, e o gap de cada máquina já está coberto acima).

## 3) Conflitos — 🟢

Busquei `<{7}`/`={7}`/`>{7}` em início de linha nos arquivos rastreados (`git ls-files`, não o disco). Isolando especificamente `<<<<<<<` e `>>>>>>>` (os marcadores inequívocos, já que `=======`/`===...===` aparecem soltos como separador decorativo em `commands/`, `skills/ecc/*`, `scripts/hooks/insaits-security-monitor.py` e vários `tool-results/*.txt`): **zero ocorrência real**. Zero `.orig`/`.rej` versionado.

## 4) Peso — 🟡 (achados repetidos + uma pista nova de terceira origem)

- `.git`: pack de **~978 MiB** (`git count-objects -vH`, 14688 objetos em 3 packs), abaixo do ~1,28 GiB de 08-30. Não sei atribuir a causa daqui (pode ser repack do lado do GitHub); não há sinal de reescrita de histórico local, e os blobs dos segredos antigos (seção 5) continuam recuperáveis por hash, então não tratem isso como limpeza de segredo.
- Working tree ~190 MB (excluindo `.git`), crescimento orgânico na semana: 2 `tool-results/*.txt` novos de ~4,9 MB cada (`projects/-Users-cassiogoncalves--buzz/...`) e 1 PDF de tool-result de ~1,16 MB — padrão parecido com semanas anteriores.
- Zero mídia (`.pdf/.png/.jpg/.mp4/.mov`) escapada para dentro de `workstations/` fora do que já é esperado — os 4 `.zip` de sempre (`Gravador-Tela` 108 KB — intencional, viaja pelo git por decisão do Cássio —, `Kirvano/Secretaria-IA.zip` 7,3 MB, `Secretaria_IA.zip` 64 KB, `WhatsApp message bubbles design.zip` 5,2 MB) seguem os mesmos de sempre, sem novidade.
- **Pista nova**: 26 arquivos pequenos (`hook-*-additionalContext.txt`) sob `projects/-/*` — um prefixo que **não bate nem com o padrão do Mac** (`projects/-Users-cassiogoncalves*`) **nem com o do Windows** (`projects/C--Users-C-ssio*`/`projects/c--Users-C-ssio*`). Primeira aparição em 24/08, mesmo autor/mensagem `auto-sync <timestamp>` que as duas máquinas usam. Não consigo identificar daqui se é uma terceira máquina/ambiente rodando o mesmo auto-sync com um slug de pasta diferente (ex.: cwd resolvendo pra `/`), ou artefato de alguma sessão na nuvem. Não é segredo (já cobri esses arquivos na varredura da seção 5), só um crescimento silencioso fora do que as regras deste check sabem classificar — vale o Cássio confirmar se reconhece essa origem.

## 5) Segredos — 🔴 (achado novo real, não é falso positivo)

Varri **apenas os arquivos rastreados** (`git ls-files`/`git grep`, nunca o disco) pelos padrões pedidos: `sk-`, `sk-ant-`, `gsk_`, `AIza`, `ghp_`/`github_pat_`, `$aact_`, `RESEND_`, `X-N8N-API-KEY`, `eyJ` (JWT 3 partes), tokens de Chatwoot, `password=`/`senha=`.

**Achado novo, real, não é exemplo/fixture:**

- `workstations/Secretaria_IA/MEMORY.md:99` — token Chatwoot em texto puro, começando em `THp1`. O próprio arquivo documenta: *"Regenerar token Chatwoot exposto em chat ... foi colado em conversa em 2026-06-24; potencialmente comprometido"* — um item de pendência aberto (`[ ]`) que nunca foi fechado. `git log -S` mostra que essa linha está na árvore desde o commit inicial de configuração do sync (por volta de meados de julho/2026), ou seja, um token potencialmente comprometido ficou em texto claro no repo por ~7 semanas sem rotação. Nenhum health check anterior tinha esse padrão explícito na lista de busca, por isso é a primeira vez que aparece aqui — não é uma regressão desta semana, é uma lacuna anterior do próprio check.

Todo o resto foi confirmado como falso positivo pelo contexto (nome de header/variável de ambiente — `X-N8N-API-KEY`, `RESEND_API_KEY`, `api_access_token` —, código de exemplo/fixture em `skills/ecc/*` e `commands/kotlin-test.md`, variável de formulário em capturas de sessão tipo `const senha = ...`, e as ocorrências de `sk-` são nomes de variável/exemplo tipo `sk-review`, `sk-master`, `sk-vazou-aqui`/`sk-secreta` — esses dois últimos em português e claramente texto de exemplo, não uma chave real). Confirmei de novo que nenhum `.jsonl` está rastreado (`git ls-files | grep -c '\.jsonl$'` = 0) e o `.gitignore` ainda cobre `projects/**/*.jsonl`.

**Isso não muda o status dos 6 segredos do achado de 08-16** (2× OpenAI `sk-proj-`, 2× Anthropic `sk-ant-api03-`, Groq `gsk_`, OpenRouter `sk-or-v1-`): seguem **recuperáveis no histórico**, sem qualquer sinal de rotação nos commits desta semana. Continuo reportando como **pendente**, não resolvido.

## 6) Integridade — 🟡

- `settings.json`: JSON válido. 🟢
- `CLAUDE.md` (raiz) e `workstations/CLAUDE.md`: existem, ambos. 🟢
- **Mesmo mismatch de documentação do intervalo, agora 8ª semana seguida sem correção**: `CLAUDE.md` diz "a cada 1h" para as duas máquinas; `WINDOWS-SETUP.md` configura de fato 60 min (linha ~94-97, comentário confirma "intervalo atual: 60 min") — mas o título da seção 4 (linha 86) ainda diz "Agendar a cada 15 min", e o cabeçalho de `scripts/sync/windows-auto-sync.ps1` (linha 2) também ainda diz "a cada 15 min". Cosmético (o comando real usa 60 min), mas seria fácil de corrigir.

## O que eu não consigo ver daqui

Rodo na nuvem e só enxergo o repositório git `claude-config` (e, para entregar este relatório, `meu-vault`). **Não tenho acesso** ao LaunchAgent do Mac (`com.cassio.claude-autosync`), à task `ClaudeAutoSync` do Windows, nem a `~/.claude/.autosync/sync.log` — local-only, fora do git. Também não enxergo o que sincroniza por Syncthing (mídia e transcritos `.jsonl`). Não sei se o token Chatwoot ou as 6 chaves de 08-16 foram rotacionados — só que os valores/blobs continuam recuperáveis. Não sei identificar a origem da terceira pasta `projects/-/*` (seção 4).

```bash
# Ação prioritária desta semana: regenerar o token Chatwoot
# (workstations/Secretaria_IA/MEMORY.md:99) e confirmar rotação das 6 chaves de 08-16.
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

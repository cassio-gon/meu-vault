---
title: Health Check do Sync — 2026-08-02
date: 2026-08-02
area: Infra
tags: [infra, sync]
source: routine
---

# Health Check do Sync — 2026-08-02 (domingo, 20h BRT)

**Semáforo geral: 🔴 VERMELHO** — os mesmos segredos reais (incluindo a chave de produção do Asaas) seguem versionados em `projects/`, agora há pelo menos 3 semanas seguidas sem rotação. Achei uma chave nova que os relatórios anteriores não tinham pego (OpenRouter, `sk-or-v1-`). O Windows voltou a ficar mais de 4 dias em silêncio, mas dentro do limite duro de 7 dias.

Repo analisado: `claude-config`, só leitura, clone completo local (não raso).

## Comparando com o check de 2026-07-26

| | 07-26 | 08-02 (hoje) |
|---|---|---|
| Gap do Windows | ~116h (4d20h) | **~97h (4d1h30)** — melhorou um pouco, mas o padrão de rajada-e-silêncio continua |
| Commits do Windows (7 dias) | 2 | 10, mas todos concentrados em 2 dias (07-27 e 07-29) — depois, silêncio |
| Segredos reais encontrados | 7 achados | os mesmos ~7, **+1 novo** (OpenRouter `sk-or-v1-`), e 2 dos arquivos antigos (GitHub PAT do Windows, um `sk-` da opensquad) foram **removidos da árvore atual — mas continuam no histórico do git**, então a exposição não foi de fato eliminada |
| GitHub PAT (Windows) | exposto | arquivo deletado em 31/07, **segredo ainda recuperável via `git show a94da39:...`** |
| .docx de paciente versionados | 5 arquivos | os mesmos 5, ainda presentes |
| Doc do intervalo (15 min vs 60 min) | mismatch | mesmo mismatch, não corrigido — 3ª semana seguida |
| Tamanho do repo | ~1,2 GB / .git ~409 MB | ~1,3 GB / .git ~506 MB — continua crescendo |

Nada foi remediado de verdade na última semana: dois arquivos com segredos sumiram da árvore de trabalho, mas isso **não** removeu o conteúdo do histórico do git — quem tiver o clone ainda consegue extrair a chave de um commit antigo. Ação nenhuma foi tomada sobre as chaves em si (nenhuma rotação confirmada).

## 1) Último commit por máquina — 🟡 (Mac verde, Windows amarelo)

- **Mac**: último commit `d9e9b2b`, 2026-08-02 17:13:38 -03:00 — ~3h atrás. 🟢
- **Windows**: último commit `43e42f5`, 2026-07-29 18:39:49 -03:00 — gap de **~97h (4 dias e ~1h30)** até agora. Não passou do limite duro de 7 dias, e está um pouco melhor que os ~116h do relatório passado, mas o Windows ficou silencioso justo nos últimos 4 dias corridos (desde a última rajada de commits). 🟡

## 2) Frequência (7 dias) — 🟢 Mac / 🔴 Windows

- **Mac**: 38 commits `auto-sync` nos últimos 7 dias, cadência horária normal. 🟢
- **Windows**: 10 commits nos últimos 7 dias, mas **todos concentrados em duas rajadas** — 07-27 (6 commits, 18:39–23:39, de hora em hora) e 07-28→07-29 (4 commits, 21:08–18:39 do dia seguinte) — e depois **zero commits nos últimos ~4 dias**. Mesmo diagnóstico dos dois relatórios anteriores: não parece "sync horário com buracos", parece "só roda quando alguém liga a máquina". 🔴
- 2 commits do período tocaram caminhos de Mac e Windows ao mesmo tempo (`bd44d83`, `a94da39`) — são merges de `pull --rebase` reconciliando o backlog das duas máquinas, comportamento esperado, não é problema.

## 3) Conflitos — 🟢

Busquei `<<<<<<<` e `>>>>>>>` explicitamente. As ocorrências fora de `projects/` são falsos positivos confirmados no contexto: fontes `.ttf` binárias e uma string literal dentro de `skills/playwright-skill/node_modules/playwright/lib/runner/index.js` (o próprio Playwright gera esse texto como parte de uma feature de diff, não é um conflito real). As ocorrências dentro de `projects/` são transcrições de conversa mencionando marcadores de conflito de *outro* projeto (prontuario-ia), não conflitos deste repo. As linhas de `====` em `commands/*.md` e `skills/ecc/**/SKILL.md` são separadores decorativos. Nenhum `.orig`/`.rej` versionado. 🟢

## 4) Peso — 🟡

- Repo total ~1,3 GB, `.git` ~506 MB — cresceu de novo (~962 mil linhas inseridas nos últimos 7 dias, é o design esperado de versionar `.jsonl` de transcrição crescendo a cada commit).
- **Achado repetido, não corrigido**: `.docx` com nome completo de paciente continuam versionados em `workstations/Medicina Ocupacional/DORTPREV/.../Encaminhamento Medico/` (4 arquivos com nome de paciente + 1 template) — dado de saúde identificável indo pelo git em vez do canal de mídia (Syncthing).
- **Achado repetido, não corrigido**: 3 `.zip` (até ~7 MB) em `workstations/Infoprodutos/Kirvano/`, `workstations/Secretaria_IA/` e `workstations/Secretaria_IA_Design/` — o `.gitignore` só bloqueia mídia binária de imagem/vídeo/pdf em `workstations/`, não `.zip`/`.docx`.
- **Achado novo (não coberto pelos relatórios anteriores)**: `skills/playwright-skill/node_modules/` está **versionado no git** — 171 arquivos, ~18 MB. `node_modules` normalmente não deveria ser versionado (deveria estar no `.gitignore` do repo, reinstalável via `npm install`); não sei se isso é intencional (skill empacotada para funcionar offline) ou um vazamento de `git add -A` do auto-sync — vale confirmar com o Cássio.

Sugestão (repetida): adicionar `workstations/**/*.docx` e `workstations/**/*.zip` na seção de mídia do `.gitignore`.

## 5) Segredos — 🔴 (o achado mais importante)

Reportando só arquivo:linha e os 4 primeiros caracteres de cada segredo.

| Provedor | Máquina | Arquivo:linha | Prefixo | Status vs. 07-26 |
|---|---|---|---|---|
| **Asaas (produção!)** | Mac | `projects/-Users-cassiogoncalves--claude/6c3c0b24-.../*.jsonl:698,703,718,722,723,749,764,767,859` e `projects/-Users-cassiogoncalves/826fa7ee-.../*.jsonl:8,13,19,29` | `$aac` | mesmo achado, ainda presente |
| Anthropic (`sk-ant-api03-`) | Mac | `projects/-Users-cassiogoncalves--claude/d9ccb190-.../*.jsonl:227,231,232,237` | `sk-a` | mesmo achado, ainda presente |
| **OpenRouter (`sk-or-v1-`) — NOVO** | Mac | `projects/-Users-cassiogoncalves--claude/294a5a33-.../*.jsonl:530,534,535,545,559,572,590,603,620,625,640` | `sk-o` | não estava nos relatórios de 07-19/07-26 |
| Groq (`gsk_`) — 2 chaves distintas | Mac | `projects/-Users-cassiogoncalves--claude/37e6ee96-.../*.jsonl:69,430,434,446,464` e `.../f3a1568a-.../*.jsonl:300,304,306,313,331` | `gsk_` | mesmo achado, ainda presente |
| Google (`AIza...`) — pelo menos 2 chaves distintas | Mac | `projects/-Users-cassiogoncalves-Documents-Claude/f3b5da17-.../*.jsonl:252` e `projects/-Users-cassiogoncalves--claude-opensquad/{7c80c3b7,d051de80}-.../*.jsonl` (chave presente, não bateu no meu regex exato desta vez, confirmei por substring) | `AIza` | mesmo achado, ainda presente |
| GitHub PAT (`github_pat_` e `ghp_`) | Windows | **arquivo `projects/c--Users-C-ssio--claude/09a5936d-....jsonl` foi deletado em `bd44d83` (31/07)** — sumiu da árvore atual, mas o blob continua acessível via commit `a94da39` (27/07) | `gith`/`ghp_` | removido da árvore, **NÃO removido do histórico** — ainda extraível |
| OpenAI-style (`sk-s...`) | Mac | arquivo `projects/-Users-cassiogoncalves--claude-opensquad/bb4d7bda-....jsonl` foi deletado em `9c35b52` (30/07) — mesma situação: some da árvore, continua no histórico via `08a2cf3`/`a94da39` | `sk-s` | removido da árvore, **NÃO removido do histórico** |

Também apareceram ~129 arquivos com tokens no formato JWT (`eyJ...`) e ~138 ocorrências de `password=`/`senha=` — não tive orçamento pra revisar linha a linha; numa amostra rápida a maioria de `password=`/`senha=` parece placeholder de exemplo/dev (`your_secure_password_here`, `localdev_fhir_pw`), mas não posso garantir que não haja senha real de produção misturada. Sinalizando como pendência de revisão manual.

**Sobre os dois arquivos "removidos"**: apagar o arquivo da árvore de trabalho (e commitar a remoção) não apaga o blob do histórico do git — qualquer clone completo do repo ainda consegue rodar `git show <commit-antigo>:<caminho>` e recuperar o PAT do GitHub e a chave OpenAI-style inteiras. Se a intenção foi remediar esses dois vazamentos, a remediação está **incompleta**: falta reescrever o histórico (`git filter-repo` ou BFG) ou, mais simples e mais seguro, **rotacionar as chaves** (o que resolve o problema independente do que ficou no histórico).

**Ação recomendada (repetida): rotacionar todas as chaves acima — Asaas de produção e GitHub PAT primeiro (dinheiro e acesso a repositório).** Reescrever o histórico é destrutivo e vai gerar conflito com o auto-sync das duas máquinas (rebase sobre histórico reescrito) — não fiz isso aqui, é decisão sua.

## 6) Integridade — 🟡

- `settings.json`: JSON válido. 🟢
- `CLAUDE.md` e `workstations/CLAUDE.md`: existem, ambos. 🟢
- **Mesmo mismatch de documentação da 3ª semana seguida, não corrigido**: `CLAUDE.md` diz "a cada 1h", e o `WINDOWS-SETUP.md` (bloco de código com `-Minutes 60`) concorda — mas o **cabeçalho** de `scripts/sync/windows-auto-sync.ps1` ("Agendado... a cada 15 min") e o **título da seção 4** do `WINDOWS-SETUP.md` ("Agendar a cada 15 min") continuam desatualizados. Não afeta o comportamento real (que segue os 60 min), mas confunde numa reinstalação do zero. 🟡

## O que eu não consigo ver daqui

Rodo na nuvem e só enxergo o repositório git `claude-config`. **Não tenho acesso** ao LaunchAgent do Mac (`com.cassio.claude-autosync`), à task `ClaudeAutoSync` do Windows, nem a `~/.claude/.autosync/sync.log` — esse log é local-only, fora do git, e é o único lugar que mostraria falha real de rede/autenticação (diferente de "a task simplesmente não rodou"). Não posso afirmar "o sync está rodando" nem "está quebrado" — só afirmo o que os commits provam: Mac consistente, Windows em rajadas seguidas de silêncio, pelo terceiro relatório seguido.

Comandos pra rodar na máquina afetada e fechar o diagnóstico:

```powershell
# Windows
Get-ScheduledTaskInfo -TaskName ClaudeAutoSync
Get-ScheduledTask -TaskName ClaudeAutoSync | Select State
Get-Content "$env:USERPROFILE\.claude\.autosync\sync.log" -Tail 30
```

```bash
# Mac, se quiser confirmar que o lado dele está saudável
launchctl print gui/$(id -u)/com.cassio.claude-autosync
tail -30 ~/.claude/.autosync/sync.log
```

O `sync.log` (Mac ou Windows), se existir, é o que vai dizer se a task está rodando e falhando (rede, git, auth) ou simplesmente não está sendo disparada.

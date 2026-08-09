---
title: Health Check do Sync — 2026-08-09
date: 2026-08-09
area: Infra
tags: [infra, sync]
source: routine
---

# Health Check do Sync — 2026-08-09 (domingo, 20h BRT)

**Semáforo geral: 🔴 VERMELHO** — dois problemas graves simultâneos: (1) os mesmos segredos reais de produção seguem versionados em `projects/`, agora há 4 semanas seguidas sem rotação confirmada, e (2) o Windows não gera **nenhum** commit de auto-sync há **11 dias** (desde 29/07) — não é mais "rajada e silêncio", é silêncio total, passou de longe o limite duro de 7 dias.

Repo analisado: `claude-config`, só leitura. **Nota metodológica importante**: meu clone inicial veio raso (`shallow`, só 50 commits, começando em 30/07) — se eu tivesse rodado os checks 1 e 2 em cima disso, teria erroneamente concluído "o Windows nunca sincronizou de verdade". Rodei `git fetch --unshallow` antes de fechar o diagnóstico e recuperei os 396 commits completos (desde 30/06). Registro isso porque é o tipo de erro silencioso que um relatório automatizado pode cometer sem avisar.

## Comparando com os checks anteriores (07-26, 08-02)

| | 07-26 | 08-02 | 08-09 (hoje) |
|---|---|---|---|
| Gap do Windows | ~116h (4d20h) | ~97h (4d1h30) | **~266h (11d2h)** — piorou muito, saiu do padrão "rajada e silêncio" para silêncio contínuo |
| Último commit real do Windows | — | `43e42f5` (29/07 18:39) | **o mesmo `43e42f5`** — nenhum commit novo do Windows em 11 dias |
| Commits do Windows (7 dias) | 2 | 10 (em 2 rajadas) | **0** |
| Segredos reais na árvore atual | 7 achados | mesmos 7 + 1 novo (OpenRouter) | Anthropic, 2× Groq, OpenRouter — **ainda presentes**; Asaas, Google AIza, GitHub PAT — **saíram da árvore atual** (prováveis remoções pontuais), mas os commits antigos que os continham seguem existindo no histórico |
| Doc do intervalo (15 min vs 60 min) | mismatch | mesmo mismatch | **mesmo mismatch, 4ª semana seguida sem correção** |
| Tamanho do repo (`.git`) | ~409 MB | ~506 MB | **~927 MB** — quase dobrou numa semana |

Nada foi remediado de fato: as chaves continuam sem rotação confirmada, e agora o problema do Windows escalou de "atraso" para "parado".

## 1) Último commit por máquina + gap — 🟢 Mac / 🔴 Windows

- **Mac**: `9111fc3`, 2026-08-09 15:30:28 -03:00 — **~4,9h atrás**. 🟢
- **Windows**: `43e42f5`, 2026-07-29 18:39:49 -03:00 — **~266h (11 dias e 2h) atrás**. Passou o limite duro de 7 dias por um fator de mais de 1,5×. 🔴

(Metodologia: por causa dos commits de limpeza que tocam os dois conjuntos de pastas ao mesmo tempo — ver seção 3 — considerei "commit real de uma máquina" apenas aquele que **adiciona ou modifica** (não só deleta) arquivo sob o prefixo de pasta daquela máquina.)

## 2) Frequência (7 dias) — 🟢 Mac / 🔴 Windows

- **Mac**: 28 commits `auto-sync` nos últimos 7 dias, cadência horária normal, sem buracos suspeitos. 🟢
- **Windows**: **zero** commits nos últimos 7 dias. Não é mais o padrão de "rajada seguida de silêncio" dos dois relatórios anteriores — é silêncio desde 29/07, ponto final. 🔴

## 3) Conflitos — 🟢

Busquei `<<<<<<<`, `=======`, `>>>>>>>` em início de linha nos arquivos rastreados: zero ocorrências (nem falsos positivos desta vez). Zero `.orig`/`.rej` versionados.

Achado à parte (não é conflito, é anomalia de commit): pelo menos 4 commits (`b015e23`, `0d0ffdf`, `bd44d83`, `8510a88`) tocam simultaneamente arquivos sob os prefixos de pasta do Mac **e** do Windows num único commit — todos com status `D` (deleção em massa, provavelmente limpeza de sessões antigas de ambas as máquinas de uma vez). Comportamento plausível de reconciliação via `pull --rebase`, não indica corrupção, mas é bom saber que a heurística "caminho tocado = máquina que commitou" falha nesses commits específicos — por isso os checks 1/2 acima usam só `A`/`M`, não `D`.

## 4) Peso — 🟡

- `.git` **~927 MB** (era ~506 MB há uma semana — quase dobrou), working tree completo maior ainda. Crescimento é majoritariamente esperado (transcrições `.jsonl` de sessão, por design), mas no ritmo atual o repo passa de 1 GB de `.git` em poucas semanas e não há rotina de poda/compactação.
- Sem mídia (`.pdf/.png/.jpg/.mp4/.mov`) fora do esperado dentro de `workstations/` — só os mesmos 3 `.zip` já sinalizados em relatórios anteriores (`Kirvano/Secretaria-IA.zip`, `Secretaria_IA/Secretaria_IA.zip`, `Secretaria_IA_Design/WhatsApp message bubbles design.zip`), que o `.gitignore` atual não bloqueia (só bloqueia mídia binária de imagem/vídeo/pdf, não `.zip`).
- `skills/playwright-skill/node_modules/` e `skills/playwright-skill/.profiles/` continuam versionados (dezenas de MB de cache de browser e bundle JS) — achado repetido de relatórios anteriores, ainda sem confirmação se é intencional.

## 5) Segredos — 🔴 (o achado mais importante)

Reportando só arquivo:linha e os 4 primeiros caracteres de cada segredo, nunca o valor completo.

| Provedor | Arquivo:linha | Prefixo | Status |
|---|---|---|---|
| **Anthropic** (`sk-ant-api03-`) | `projects/-Users-cassiogoncalves--claude/d9ccb190-9aca-4d82-a3a6-2e65647c5dbc.jsonl:227,231,232,237` | `sk-ant-api03-CeGl` | ainda na árvore atual, achado repetido |
| **Groq** (`gsk_`) — chave 1 | `projects/-Users-cassiogoncalves--claude/16b14d6e-16d8-4f82-8c63-314fc13bc5b4.jsonl:22` e `.../37e6ee96-2583-4daf-8437-0a41b2938b24.jsonl:430,434,446,464` | `gsk_KqB8` | ainda na árvore atual, achado repetido |
| **Groq** (`gsk_`) — chave 2 | `projects/-Users-cassiogoncalves--claude/37e6ee96-2583-4daf-8437-0a41b2938b24.jsonl:69` | `gsk_7Ten` | ainda na árvore atual, achado repetido |
| **OpenRouter** (`sk-or-v1-`) | `projects/-Users-cassiogoncalves--claude/294a5a33-4d84-4403-94a1-08f635894e5d.jsonl:530,534,535,545,559,572,590,603,620,625,640` | `sk-or-v1-a3ed` | ainda na árvore atual, achado repetido |
| **n8n** (JWT `X-N8N-API-KEY` / API key), pelo menos 3 tokens distintos | `projects/-Users-cassiogoncalves--claude/ed7dc4b4-0a36-4e7a-a286-10781a628775.jsonl:1057,1254,1308,1333,1385,1411,1444`; `projects/-Users-cassiogoncalves--claude/b6e515db-05fe-4f92-ad13-da2fc98a2efa.jsonl:35`; `projects/-Users-cassiogoncalves-Documents-Claude/2e2e8313-d754-4657-ab5f-249848527f79.jsonl:56` | `eyJh` | **achado novo, não coberto pelos relatórios anteriores** — 3 tokens n8n distintos (mesmo usuário `sub`, `jti`/`aud` diferentes) |
| **Asaas** (produção, `$aact_`) | não apareceu na árvore atual desta vez (arquivo `6c3c0b24-...jsonl`, tocado pela última vez no commit `cbe7293` de 08/08, parece ter sido limpo) | — | **sumiu da árvore, mas os commits anteriores a `cbe7293` continuam existindo no histórico** — não confirmei extração do valor no tempo que tinha, mas a lógica é a mesma dos outros dois casos abaixo: deletar da árvore não remove do histórico |
| **Google** (`AIza...`) | não bati com o padrão restrito desta vez | — | mesma ressalva do Asaas: histórico anterior ainda existe (não confirmei se o conteúdo específico é recuperável) |
| **GitHub PAT** (`ghp_`/`github_pat_`) | não está na árvore atual | — | achado de 07-26, arquivo deletado em `bd44d83` (31/07) — **esse commit e seu pai (`a94da39`) continuam existindo no histórico completo**, ou seja a remediação continua incompleta se a intenção era eliminar o segredo (só sumiu da árvore, não do histórico) |

Também apareceram ~207 ocorrências do padrão `password=`/`senha=` espalhadas por dezenas de arquivos. Não tive orçamento para revisar linha a linha de novo; numa amostra aleatória de 8, todas eram claramente fixture/placeholder de código de teste (`senha-forte-1`, `senha-secreta-...`, nome de variável `envSenha`) — mas, como nos relatórios anteriores, não posso garantir que não haja uma senha real de produção misturada nesse volume. Seguindo sinalizado como pendência de revisão manual (ou de uma ferramenta dedicada tipo gitleaks/trufflehog, que eu não tenho aqui).

**Sobre os três "sumiram da árvore" (Asaas, Google, GitHub PAT)**: mesmo diagnóstico do relatório de 08-02 — apagar da árvore de trabalho e commitar a remoção **não** apaga o blob do histórico do git. Quem tiver o clone completo (que agora eu confirmei ter 396 commits, não só os 50 do clone raso) ainda consegue rodar `git show <commit-antigo>:<caminho>` e recuperar o segredo original, a não ser que o histórico tenha sido reescrito (`git filter-repo`/BFG) — não há evidência disso aqui; os commits antigos (`a94da39`, `bd44d83`, `9c35b52`, `08a2cf3`) todos continuam acessíveis.

**Ação recomendada, repetida pela 4ª semana**: rotacionar as chaves — Anthropic e Groq primeiro (estão ativas na árvore atual agora), depois n8n (achado novo), depois confirmar se Asaas/Google/GitHub PAT já foram rotacionadas (se não, são as de maior risco financeiro/acesso). Reescrever o histórico do git é destrutivo e vai conflitar com o auto-sync das duas máquinas — decisão sua, não fiz isso aqui.

## 6) Integridade — 🟡

- `settings.json`: JSON válido. 🟢
- `CLAUDE.md` e `workstations/CLAUDE.md`: existem, ambos. 🟢
- **Mesmo mismatch de documentação, 4ª semana seguida sem correção**: `CLAUDE.md` e `WINDOWS-SETUP.md` (bloco `-RepetitionInterval (New-TimeSpan -Minutes 60)`) dizem 1h — mas o **cabeçalho** de `scripts/sync/windows-auto-sync.ps1` ("Agendado pelo Task Scheduler a cada 15 min", linha 2) continua desatualizado. Cosmético (não afeta o comportamento real), mas some com o único hard-block do gap de 11 dias.

## O que eu não consigo ver daqui

Rodo na nuvem e só enxergo o repositório git `claude-config`. **Não tenho acesso** ao LaunchAgent do Mac (`com.cassio.claude-autosync`), à task `ClaudeAutoSync` do Windows, nem a `~/.claude/.autosync/sync.log` — esse log é local-only, fora do git, e é o único lugar que mostraria se a task Windows está: (a) desabilitada, (b) habilitada mas falhando (rede/git/auth), ou (c) a máquina simplesmente não liga há 11 dias. Não posso afirmar qual desses três é o caso — só afirmo o que os commits provam: 11 dias corridos sem nenhum commit real do Windows, o pior número das últimas 3 semanas.

Dado que o gap passou de "atraso" pra "parado" desde a semana passada, valeria a pena confirmar isso na própria máquina o quanto antes:

```powershell
# Windows — confirmar se a task scheduled ainda existe e está habilitada
Get-ScheduledTaskInfo -TaskName ClaudeAutoSync
Get-ScheduledTask -TaskName ClaudeAutoSync | Select State
Get-Content "$env:USERPROFILE\.claude\.autosync\sync.log" -Tail 30
```

```bash
# Mac — só pra confirmar que o lado dele está saudável (já indicam commits recentes que sim)
launchctl print gui/$(id -u)/com.cassio.claude-autosync
tail -30 ~/.claude/.autosync/sync.log
```

Se `Get-ScheduledTaskInfo` mostrar `LastTaskResult` diferente de 0, ou `State` diferente de `Ready`, é isso que explica o silêncio. Se a task estiver `Ready` e `LastTaskResult 0` mas sem commits novos, o problema é outro (rede/git auth) e o `sync.log` deve mostrar o erro.

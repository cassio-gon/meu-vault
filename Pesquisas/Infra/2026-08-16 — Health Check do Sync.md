---
title: Health Check do Sync — 2026-08-16
date: 2026-08-16
area: Infra
tags: [infra, sync]
source: routine
---

# Health Check do Sync — 2026-08-16 (domingo, 20h BRT)

**Semáforo geral: 🔴 VERMELHO** — dois problemas graves e nenhum foi corrigido desde a semana passada: (1) o Windows passou de **11 dias** de silêncio (relatado em 08-09) para **18 dias** — a última vez que a task `ClaudeAutoSync` de fato gravou algo foi em 29/07; (2) apareceram **segredos reais novos** no repo — duas chaves OpenAI (`sk-proj-`) e uma chave Anthropic (`sk-ant-api03-`) diferente da já conhecida, todas coladas em conversa em **13/08, quatro dias depois** do relatório anterior já ter pedido rotação. O aviso de 4 semanas seguidas não mudou o comportamento.

Repo analisado: `claude-config`, só leitura. Clone inicial veio raso (50 commits); fiz `git fetch --deepen` e depois `git fetch --unshallow` antes de fechar o diagnóstico — histórico completo confirmado (477 commits, desde 30/06). Sem isso, os checks 1 e 2 teriam classificado errado pelo menos 6 commits de reconciliação (deleção em massa que toca pastas do Mac e do Windows no mesmo commit) como "atividade real do Windows" — mesma armadilha descrita no relatório de 08-09; usei a mesma regra (só conta `A`/`M` sob o prefixo da máquina, nunca `D`) para não cair nela de novo.

## Comparando com os checks anteriores (07-26, 08-02, 08-09)

| | 07-26 | 08-02 | 08-09 | 08-16 (hoje) |
|---|---|---|---|---|
| Gap do Windows | ~116h (4d20h) | ~97h (4d1h30) | ~266h (11d2h) | **~434h (18d1h40) — piorou de novo** |
| Último commit real do Windows | — | `43e42f5` (29/07 18:39) | o mesmo `43e42f5` | **o mesmo `43e42f5` — 18 dias sem nenhum commit novo** |
| Commits do Windows (7 dias) | 2 | 10 (2 rajadas) | 0 | **0 — 2ª semana seguida em zero** |
| Segredos reais na árvore atual | 7 achados | +1 (OpenRouter) | Anthropic, 2×Groq, OpenRouter, +n8n (novo) | **+2 OpenAI novas, +1 Anthropic nova (chave diferente) — coladas em 13/08** |
| Doc do intervalo (15 min vs 60 min) | mismatch | mesmo mismatch | mesmo mismatch (4ª semana) | **mesmo mismatch, 5ª semana seguida sem correção** |
| Tamanho do repo (`.git`, histórico completo) | ~409 MB | ~506 MB | ~927 MB | **~1,2 GB — mais uma vez em forte crescimento** |

Nada foi remediado: a task do Windows segue muda, as chaves antigas seguem sem rotação confirmada, e agora há chaves **novas** coladas depois do último aviso — o problema está piorando, não estabilizando.

## 1) Último commit por máquina + gap — 🟢 Mac / 🔴 Windows

- **Mac**: `e8df2b2`, 2026-08-16 16:36:59 -03:00 — **~3,7h atrás**. 🟢
- **Windows**: `43e42f5`, 2026-07-29 18:39:49 -03:00 — **~434h (18 dias e 1h40) atrás**. Mais de **2,5×** o limite duro de 7 dias, e pior que o gap já alarmante da semana passada.

(Metodologia: contei como "commit real de uma máquina" apenas o que **adiciona ou modifica** — não só deleta — arquivo sob o prefixo de pasta daquela máquina, para não confundir reconciliação/limpeza com atividade genuína. Reclassifiquei manualmente 6 commits entre 06/08 e 11/08 que meu primeiro grep automático tinha marcado como "Windows" e que na verdade eram só deleções em massa tocando as duas pastas — nenhum é commit real do Windows.)

## 2) Frequência (7 dias) — 🟢 Mac / 🔴 Windows

- **Mac**: 68 commits `auto-sync` (A/M) nos últimos 7 dias, cadência horária normal, sem buracos suspeitos.
- **Windows**: **zero** commits reais nos últimos 7 dias — 2ª semana seguida em zero. O silêncio começou em 29/07 e não teve nenhuma rajada de recuperação desde então.

## 3) Conflitos — 🟢

Busquei `<<<<<<<`, `=======`, `>>>>>>>` em início de linha nos arquivos rastreados: as únicas ocorrências são linhas `====...====` de separador em documentação (`commands/`, `skills/ecc/`, etc.) — confirmei o contexto de cada uma, nenhuma é marcador real de merge. Zero `.orig`/`.rej` versionados.

## 4) Peso — 🟡

- `.git` com histórico completo: **~1,2 GB** (era ~927 MB há uma semana — mais ~30%). Working tree: 742 MB. Maior causa continua sendo `.jsonl` de transcrição reescrito por inteiro a cada commit (encontrei blobs de até **70 MB** para um único arquivo de sessão, `.../e44b2ca3-....jsonl`, versionado repetidas vezes no histórico recente).
- Mídia binária (`.pdf/.png/.jpg/.mp4/.mov`) dentro de `workstations/`: nenhuma fora do esperado — o `.gitignore` está funcionando para essas extensões.
- Mesmos 3 `.zip` de sempre, sem crescer: `Kirvano/Secretaria-IA.zip` (7,0 MB), `Secretaria_IA/Secretaria_IA.zip` (65 KB), `Secretaria_IA_Design/WhatsApp message bubbles design.zip` (5,3 MB) — `.zip` não está coberto pelas regras atuais do `.gitignore` (só bloqueia mídia de imagem/vídeo/pdf), achado repetido, sem mudança.
- `skills/playwright-skill/node_modules/` (171 arquivos, 18 MB) e `.profiles/` (296 arquivos) continuam versionados — achado repetido de relatórios anteriores, ainda sem confirmação se é intencional.

## 5) Segredos — 🔴 (o achado mais importante, e o que mais piorou)

Reportando só arquivo:linha e os 4 primeiros caracteres de cada segredo, nunca o valor completo.

| Provedor | Arquivo:linha | Prefixo | Status |
|---|---|---|---|
| **OpenAI** (`sk-proj-`) — chave A | `projects/-Users-cassiogoncalves--claude-workstations-Calima/755259aa-89e9-4744-9fe1-44e55033211e.jsonl:459,465,487,489,527` | `sk-p` | **NOVO** — colada em 2026-08-13 15:33 (não estava em nenhum relatório anterior) |
| **OpenAI** (`sk-proj-`) — chave B | `projects/-Users-cassiogoncalves--claude-workstations-Calima/bb0077d9-4364-4035-9683-8e24944fb245.jsonl:118,122,123,180` | `sk-p` | **NOVO** — colada em 2026-08-13 11:32, mesma mensagem que a chave Anthropic nova abaixo |
| **Anthropic** (`sk-ant-api03-`) — chave nova | `projects/-Users-cassiogoncalves--claude-workstations-Calima/bb0077d9-4364-4035-9683-8e24944fb245.jsonl:118,122,123,180` | `sk-a` | **NOVA** — colada em 2026-08-13 11:32, prefixo diferente da chave já conhecida (`sk-ant-api03-CeGl`) |
| **Anthropic** (`sk-ant-api03-`) — chave já conhecida | `projects/-Users-cassiogoncalves--claude/d9ccb190-9aca-4d82-a3a6-2e65647c5dbc.jsonl:227,231,232,237` | `sk-a` | ainda na árvore, achado repetido desde 07-26 (usuário reconheceu o risco na própria mensagem: "sei do risco e escolho prosseguir assim") |
| **Groq** (`gsk_`) | `projects/-Users-cassiogoncalves--claude/16b14d6e-16d8-4f82-8c63-314fc13bc5b4.jsonl:22` | `gsk_` | ainda na árvore, achado repetido. A 2ª chave Groq relatada em 08-09 (`gsk_7Ten`, arquivo `37e6ee96-...`) **saiu da árvore atual** — mesma ressalva de sempre: sumir da árvore não apaga do histórico |
| **OpenRouter** (`sk-or-v1-`) | `projects/-Users-cassiogoncalves--claude/294a5a33-4d84-4403-94a1-08f635894e5d.jsonl:530,534,535,545,559,572,590` | `sk-o` | ainda na árvore, achado repetido, mesmo arquivo e chave de 08-09 |
| **Asaas** (homologação, `$aact_hmlg_`) | `projects/-Users-cassiogoncalves--claude-workstations-Calima/c2a4b2df-022c-4e08-83b6-5243b09ace0b.jsonl:773` (+ 11 outras linhas do mesmo arquivo) | `$aac` | achado novo nesta árvore, mas é chave de **homologação/sandbox** — risco financeiro bem menor que uma `aact_prod_` |
| n8n JWT (`X-N8N-API-KEY`, tokens de 08-09) | — | — | os 3 tokens relatados em 08-09 (`ed7dc4b4`, `b6e515db`, `2e2e8313`) **saíram da árvore atual** |

**Falso positivo verificado (não é segredo)**: `projects/-Users-cassiogoncalves--claude-workstations-Calima/f5e4e6b5-cc40-40a4-9253-7d2c8f5623d3.jsonl:79` bate com o padrão JWT (`eyJ...`), mas o campo é `idBulaPacienteProtegido` — parece um identificador correlato de bula de medicamento (contexto de API de dados de paciente/ANVISA), não um token de autenticação. Sinalizando por outro motivo: se o valor realmente amarra a um paciente identificável, é um problema de dado de saúde, não de credencial — vale uma checada manual, não entra na tabela de segredos.

**Falso positivo verificado**: string `aact_prod` encontrada em `projects/-Users-cassiogoncalves--claude/44f74752-....jsonl:87` é só **texto de discussão** ("a que mais preocupa é a do Asaas com prefixo `aact_prod`"), não uma chave real — confirmado pelo contexto ao redor.

Também apareceram dezenas de ocorrências de `password=`/`senha=`; não tive orçamento para revisar linha a linha nesta rodada (mesma ressalva das semanas anteriores — sem uma ferramenta dedicada tipo gitleaks/trufflehog aqui, não posso garantir que não haja senha real de produção misturada no volume).

**Sobre os que "sumiram da árvore"**: apagar da árvore de trabalho e commitar a remoção não apaga o blob do histórico do git — quem tiver o clone completo ainda consegue recuperar o valor original via `git show <commit-antigo>:<caminho>`, a não ser que o histórico tenha sido reescrito (`git filter-repo`/BFG). Não fiz essa reescrita aqui — é destrutiva e vai conflitar com o auto-sync das duas máquinas.

**Ação recomendada, agora mais urgente (5ª semana seguida pedindo isso)**: rotacionar **hoje**, nesta ordem — (1) as duas chaves OpenAI e a chave Anthropic novas de 13/08, coladas depois do último aviso; (2) a chave Anthropic antiga (24/07) e a Groq, que seguem ativas há semanas; (3) confirmar se a Asaas de homologação precisa mesmo ficar exposta (ambiente de teste, risco menor, mas ainda uma credencial). Reescrever o histórico do git é uma decisão separada e destrutiva — não tomei essa decisão por você.

## 6) Integridade — 🟡

- `settings.json`: JSON válido. 🟢
- `CLAUDE.md` e `workstations/CLAUDE.md`: existem, ambos. 🟢
- **Mesmo mismatch de documentação, 5ª semana seguida sem correção**: `CLAUDE.md` e `WINDOWS-SETUP.md` dizem 1h (`-RepetitionInterval (New-TimeSpan -Minutes 60)`), mas o cabeçalho de `scripts/sync/windows-auto-sync.ps1` (linha 2) ainda diz "Agendado pelo Task Scheduler a cada 15 min". Cosmético, não é a causa do gap de 18 dias, mas seria um bom momento para corrigir já que você vai mexer na task mesmo.

## O que eu não consigo ver daqui

Rodo na nuvem e só enxergo o repositório git `claude-config`. **Não tenho acesso** ao LaunchAgent do Mac (`com.cassio.claude-autosync`), à task `ClaudeAutoSync` do Windows, nem a `~/.claude/.autosync/sync.log` — esse log é local-only, fora do git, e é o único lugar que mostraria se a task do Windows está: (a) desabilitada, (b) habilitada mas falhando (rede/git/auth), ou (c) a máquina simplesmente não liga há 18 dias. Não posso afirmar qual desses três é o caso — só afirmo o que os commits provam: 18 dias corridos sem nenhum commit real do Windows, o pior número desde que este health check começou a rodar.

Vale a pena confirmar isso na própria máquina o quanto antes — é o mesmo comando de duas semanas atrás, ainda sem resposta visível daqui:

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

Se `Get-ScheduledTaskInfo` mostrar `LastTaskResult` diferente de 0, ou `State` diferente de `Ready`, é isso que explica o silêncio. Se a task estiver `Ready` e `LastTaskResult 0` mas sem commits novos, o problema é outro (rede/git auth) e o `sync.log` deve mostrar o erro.

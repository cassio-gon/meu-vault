---
title: Health Check do Sync — 2026-07-26
date: 2026-07-26
area: Infra
tags: [infra, sync]
source: routine
---

# Health Check do Sync — 2026-07-26 (domingo, 20h BRT)

**Semáforo geral: 🔴 VERMELHO** — os mesmos segredos reais (incluindo a chave de produção do Asaas) que o check de 2026-07-19 encontrou continuam versionados em `projects/` uma semana depois, sem rotação, e o sync do Windows voltou a ficar quase 5 dias em silêncio.

Repo analisado: `claude-config`, só leitura. O clone chegou raso de novo; rodei `git fetch --unshallow` (leitura) antes de qualquer conclusão — confirmei que o achado de Windows não muda com o histórico completo (293 commits desde 2026-06-30).

## Comparando com o check de 2026-07-19

| | 07-19 | 07-26 (hoje) |
|---|---|---|
| Gap do Windows | ~45h | **~116h (4d20h)** |
| Commits do Windows (7 dias) | 1 | 2 |
| Segredos reais encontrados | 7 achados | os mesmos 7, ainda presentes |
| .docx de paciente versionados | 5 arquivos | os mesmos 5, ainda presentes |
| Doc do intervalo (15 min vs 60 min) | mismatch | mesmo mismatch, não corrigido |

Nada foi remediado na última semana. Isso muda o tom do relatório: não são achados novos, são achados **abertos há 7 dias**.

## 1) Último commit por máquina — 🟡 (Mac verde, Windows amarelo)

- **Mac**: último commit `038924e`, 2026-07-26 19:53:07 -03:00 — ~7 min atrás. 🟢
- **Windows**: último commit `4e5a45b`, 2026-07-21 23:39:51 -03:00 — gap de **~116h (4 dias e 20h)** até agora. Ainda não passou do limite duro de 7 dias, mas subiu de ~45h (semana passada) para ~116h nesta — trajetória clara de piora, e ao ritmo atual cruza os 7 dias por volta de quarta-feira (2026-07-29) se ninguém mexer. 🟡

## 2) Frequência (7 dias) — 🟢 Mac / 🔴 Windows

- **Mac**: ~50 commits `auto-sync` nos últimos 7 dias, cadência horária normal (gaps maiores só de madrugada). 🟢
- **Windows**: só **2 commits** nos últimos 7 dias — ambos em 07-21 (09:21 e 23:39). Olhando o histórico completo (31 commits de Windows desde 06-30), o padrão continua de rajadas seguidas de silêncio longo:
  - 07-20: 6 commits (23:14–23:39, uma rajada só)
  - 07-21: 2 commits (09:21 bootstrap grande + 23:39)
  - **silêncio desde então — 0 commits em quase 5 dias**

  Isso é o mesmo diagnóstico do relatório anterior: não parece "sync horário com buracos à noite", parece "task que só roda quando alguém liga o PC ou mexe em algo manualmente". 🔴

## 3) Conflitos — 🟢

Nenhum marcador `<<<<<<<` / `>>>>>>>` real encontrado (busquei os dois padrões explicitamente, zero ocorrências). As linhas de `====` que aparecem em `commands/*.md`, `skills/ecc/**/SKILL.md` e em headers de tool-output tipo `=== CLAUDE.md ===` são separadores decorativos, não marcadores de merge — confirmado olhando o contexto de cada uma. Nenhum `.orig`/`.rej` versionado. 🟢

## 4) Peso — 🟡

- Repo total ~1,2 GB, `.git` ~409 MB. Cresceu de novo desde a semana passada (~516 MB → 409 MB em pack, mas +962 mil linhas inseridas nos últimos 7 dias) — esperado, é o design de versionar `.jsonl` de transcrição.
- **Achado repetido, não corrigido**: o `.gitignore` ainda só bloqueia `.pdf/.png/.jpg/.jpeg/.mp4/.mov` dentro de `workstations/` — continua sem cobrir `.zip` nem `.docx`:
  - 3 `.zip` (até ~7 MB) em `workstations/Infoprodutos/Kirvano/` e `workstations/Secretaria_IA*/` — deveriam ir por Syncthing.
  - **Os mesmos 5 `.docx` com nome completo de paciente** em `workstations/Medicina Ocupacional/DORTPREV/.../Encaminhamento Medico/` (ex.: "Encaminhamento - Fernando Marques da Silva.docx") continuam versionados, uma semana depois. É dado de saúde identificável indo pelo git em vez do canal de mídia.

  Sugestão (repetida): adicionar `workstations/**/*.docx` e `workstations/**/*.zip` na seção de mídia do `.gitignore`.

## 5) Segredos — 🔴 (o achado mais importante, e o mesmo de 7 dias atrás)

As mesmas chaves reais do check anterior continuam nos mesmos arquivos — nenhuma foi rotacionada ou removida. Reportando só arquivo:linha e os 4 primeiros caracteres:

| Provedor | Máquina | Arquivo:linha | Prefixo |
|---|---|---|---|
| **Asaas (produção!)** | Mac | `projects/-Users-cassiogoncalves--claude/6c3c0b24-.../*.jsonl:698,703,718,722,723,749,764,767` | `$aac` |
| **Asaas (produção!)** | Mac | `projects/-Users-cassiogoncalves/826fa7ee-.../*.jsonl:8,13,19,29` | `$aac` |
| Anthropic (`sk-ant-api03-`) | Mac | `projects/-Users-cassiogoncalves--claude/d9ccb190-.../*.jsonl:227,231,232,237` | `sk-a` |
| GitHub PAT (`github_pat_`) | **Windows** | `projects/c--Users-C-ssio--claude/09a5936d-.../*.jsonl:101,104,107,109,111,115` | `gith` |
| GitHub PAT clássico (`ghp_`) | **Windows** | `projects/c--Users-C-ssio--claude/09a5936d-.../*.jsonl:121,123,126,129` | `ghp_` |
| Google (`AIzaSy...`) — 2 chaves distintas | Mac | `projects/-Users-cassiogoncalves--claude-opensquad/{0e3a3221,7c80c3b7,d051de80}-.../*.jsonl` e `.../claude/ed7dc4b4-.../*.jsonl:389` | `AIza` |
| Google (`AIzaSy...`) — 1 chave | **Windows** | `projects/c--Users-C-ssio--claude/754070e7-.../tool-results/*firecrawl_search*.txt` (3 arquivos) | `AIza` |
| Groq (`gsk_`) — 2 chaves distintas | Mac | `projects/-Users-cassiogoncalves--claude/37e6ee96-.../*.jsonl:69,430...` e `f3a1568a-.../*.jsonl:300...` | `gsk_` |
| OpenAI-style (`sk-...`) | Mac | `projects/-Users-cassiogoncalves--claude-opensquad/bb4d7bda-.../*.jsonl:293` | `sk-s` |

Também apareceram ~90 tokens no formato JWT (`eyJ...`) em 7 arquivos e centenas de ocorrências do padrão `password=`/`senha=` em 167 arquivos — na amostra que revisei, a esmagadora maioria de `password=`/`senha=` é ruído (campos de JSON de transcrição, exemplos de código como `password: "SecureP@ss1"` em `commands/kotlin-test.md`/`rust-test.md`). Não tive orçamento pra revisar as ~90 linhas de JWT uma a uma; dado que os achados de API key acima já são graves o bastante pra justificar ação, sinalizo os JWTs como pendência de revisão manual em vez de gastar mais tempo de robô nisso.

O `.gitignore` do repo já documenta que essa exposição é um risco aceito conscientemente ("chave que passou por chat pode ter sido commitada... repo é privado"). Isso não muda a recomendação: a chave **Asaas de produção** e o **GitHub PAT** são as mais perigosas (pagamento e acesso a repositórios, respectivamente), e já estão expostas há pelo menos uma semana sem rotação.

**Ação recomendada (repetida, ainda não feita):** rotacionar as chaves acima (Asaas e GitHub PAT primeiro). Purgar os blobs do histórico é destrutivo e reescreveria o histórico compartilhado entre as duas máquinas — decisão sua, não fiz aqui.

## 6) Integridade — 🟡

- `settings.json`: JSON válido. 🟢
- `CLAUDE.md` e `workstations/CLAUDE.md`: existem, ambos. 🟢
- **Mesmo mismatch de documentação de 07-19, não corrigido**: `CLAUDE.md` diz "a cada 1h" para o Windows, e o `WINDOWS-SETUP.md` (bloco de código com `-Minutes 60`) concorda — mas o **cabeçalho** de `scripts/sync/windows-auto-sync.ps1` ("Agendado... a cada 15 min") e o **título da seção 4** do `WINDOWS-SETUP.md` ("Agendar a cada 15 min") continuam desatualizados. Não afeta o comportamento real (que segue os 60 min), mas confunde numa reinstalação. 🟡

## O que eu não consigo ver daqui

Rodo na nuvem e só enxergo o repositório git. **Não tenho acesso** ao LaunchAgent do Mac (`com.cassio.claude-autosync`), à task `ClaudeAutoSync` do Windows, nem a `~/.claude/.autosync/sync.log` — esse log é local-only, fora do git, e é o único lugar que mostraria falha de rede/autenticação real (diferente de "a task simplesmente não rodou"). Não posso afirmar "o sync está rodando" ou "está quebrado" — só afirmo o que os commits provam: Mac consistente, Windows não, pelo segundo relatório seguido.

Comandos pra rodar no Windows e fechar o diagnóstico:

```powershell
Get-ScheduledTaskInfo -TaskName ClaudeAutoSync
Get-ScheduledTask -TaskName ClaudeAutoSync | Select State
```

```bash
# Mac, se quiser confirmar que o lado dele está saudável
launchctl print gui/$(id -u)/com.cassio.claude-autosync
tail -30 ~/.claude/.autosync/sync.log
```

O `sync.log` do Windows (`%USERPROFILE%\.claude\.autosync\sync.log`), se existir, é o que vai dizer se a task está rodando e falhando (rede, git, auth) ou simplesmente não está sendo disparada.

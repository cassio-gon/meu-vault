---
title: Health Check do Sync — 2026-07-19
date: 2026-07-19
area: Infra
tags: [infra, sync]
source: routine
---

# Health Check do Sync — 2026-07-19 (domingo, 20h BRT)

**Semáforo geral: 🔴 VERMELHO** — segredos reais (incluindo uma chave de produção do Asaas) foram encontrados versionados em `projects/`, e o sync do Windows está funcionando de forma muito irregular.

Repo analisado: `claude-config`, só leitura. O clone local estava raso (shallow); rodei `git fetch --unshallow` (leitura, sem escrita) para poder olhar o histórico completo — sem isso o check de "commits do Windows" teria dado um falso alarme (o shallow só enxergava 2 commits de Windows em 90 dias; o histórico completo tem 25).

## 1) Último commit por máquina — 🟡 (Mac verde, Windows amarelo)

- **Mac**: último commit `ba7280f`, 2026-07-19 20:03:10 -03:00 — praticamente agora (gap ~0h). 🟢
- **Windows**: último commit `99b4619`, 2026-07-17 22:56:41 -03:00 — gap de **~45h** até agora (2026-07-19 ~20:03 -03:00). Ainda não passou do limite duro de 7 dias, mas o padrão histórico (ver check 2) mostra que já houve gap de 6 dias antes. 🟡

## 2) Frequência (7 dias) — 🟢 Mac / 🔴 Windows

- **Mac**: 51 commits `auto-sync` nos últimos 7 dias. Gaps olhados no histórico completo (desde 2026-06-30) nunca passam de ~20h, e os maiores são todos de madrugada (máquina dormindo) — comportamento esperado de um LaunchAgent de 1h. 🟢
- **Windows**: **apenas 1 commit** nos últimos 7 dias (o de 07-17 22:56). Olhando o histórico completo do repo (25 commits de Windows desde 06-30), o padrão é de rajadas seguidas de silêncio longo, não de cadência horária:
  - 06-30: 6 commits (setup inicial)
  - 07-05: 1 · 07-06: 3 · 07-07: 6 · 07-10: 4 · 07-11: 1
  - **gap de 6 dias** entre 07-11 e 07-17
  - **gap de 45h e subindo** entre 07-17 e agora
  
  Isso não é "sync horário com buracos à noite" — é "sync que só roda esporadicamente". A Task Scheduler provavelmente não está dependável (máquina desligada, task desabilitada, ou falhando silenciosamente). 🔴

## 3) Conflitos — 🟢

`git grep` por marcadores `<<<<<<<` / `=======` / `>>>>>>>` não encontrou nenhum conflito real. As únicas ocorrências de linhas de `====` são separadores decorativos em `commands/*.md`, `skills/ecc/**/SKILL.md` e em transcrições de tool-output (headers tipo `=== CLAUDE.md ===`) — nada é marcador de merge de verdade. Nenhum `.orig`/`.rej` versionado. 🟢

## 4) Peso — 🟡

- Repo total ~1.2 GB, `.git` ~516 MB. Isso é majoritariamente esperado — `projects/` versiona transcrições `.jsonl` grandes (a maior, 37 MB), decisão informada já registrada no `.gitignore`.
- **Achado real**: o `.gitignore` só bloqueia mídia dentro de `workstations/` para `.pdf/.png/.jpg/.jpeg/.gif/.webp/.mp4/.mov/.webm` — **não cobre `.zip` nem `.docx`**. Isso deixou passar pro git:
  - 3 arquivos `.zip` (até 7,3 MB) em `workstations/Infoprodutos/` e `workstations/Secretaria_IA*/` — deveriam ir pelo Syncthing, não pelo git.
  - **5 arquivos `.docx` em `workstations/Medicina Ocupacional/DORTPREV/.../Encaminhamento Medico/`, com nome completo de paciente no título do arquivo** (ex.: "Encaminhamento - Fernando Marques da Silva.docx"), adicionados em 2026-07-16. São documentos médicos reais (dado de saúde identificável) indo para um repo git em vez do canal de mídia (Syncthing) — mesmo o repo sendo privado, isso é mais sensível que só "peso".
  
  Sugestão: adicionar `workstations/**/*.docx`, `workstations/**/*.zip` (e talvez `.xlsx`) na seção de mídia do `.gitignore`, do jeito que já existe para pdf/png/mp4.

## 5) Segredos — 🔴 (o achado mais importante deste relatório)

Encontrei **chaves reais** coladas em conversas e versionadas em `projects/`, em transcrições de **ambas as máquinas**. Reportando só arquivo:linha e os 4 primeiros caracteres, como instruído:

| Provedor | Máquina | Arquivo:linha | Prefixo |
|---|---|---|---|
| **Asaas (produção!)** | Mac | `projects/-Users-cassiogoncalves--claude/6c3c0b24-.../*.jsonl:698` (+ 6 outras linhas no mesmo arquivo) | `$aac` |
| **Asaas (produção!)** | Mac | `projects/-Users-cassiogoncalves/826fa7ee-.../*.jsonl:8,13,19,29` | `$aac` |
| Anthropic (`sk-ant-api03-`) | Mac | `projects/-Users-cassiogoncalves-vscode/b48446a5-.../*.jsonl` (14 linhas, ex. :331) | `sk-a` |
| GitHub PAT clássico (`ghp_`) | Mac | `projects/-Users-cassiogoncalves-vscode/b48446a5-.../*.jsonl` (28 linhas, ex. :190) | `ghp_` |
| GitHub PAT (`ghp_` e `github_pat_`) | **Windows** | `projects/c--Users-C-ssio--claude/09a5936d-.../*.jsonl:101-129` | `ghp_` / `gith` |
| Google (`AIzaSy`) | Mac | `projects/-Users-cassiogoncalves--claude/90a1bc27-.../*.jsonl:101` | `AIza` |
| Google (`AIzaSy`) | **Windows** | `projects/c--Users-C-ssio--claude/754070e7-.../tool-results/*firecrawl*.txt` (3 arquivos) e `.../ae6472ec-.../*.jsonl` | `AIza` |
| Groq (`gsk_`) | Mac | `projects/-Users-cassiogoncalves--claude/37e6ee96-.../*.jsonl:69,430...` e `f3a1568a-.../*.jsonl:300...` (2 chaves distintas) | `gsk_` |

A que mais preocupa é a do **Asaas com prefixo `aact_prod`** — é o gateway de pagamento, chave de **produção**, colada em texto puro numa mensagem de chat ("chave api asaas $aact_prod_..."). Isso confirma, na prática, o risco que o próprio `.gitignore` do repo já reconhece como aceito ("chave que passou por chat pode ter sido commitada") — mas com uma chave de pagamento em produção o dano potencial é maior que as outras.

**Ação recomendada**: rotacionar todas as chaves acima (Asaas primeiro) e, se possível, considerar reescrever/purgar esses blobs específicos do histórico do repo — mas isso é uma operação destrutiva (reescreve histórico compartilhado entre as duas máquinas) que não fiz aqui por ser só leitura; decisão sua.

## 6) Integridade — 🟡

- `settings.json`: JSON válido. 🟢
- `CLAUDE.md` e `workstations/CLAUDE.md`: existem, ambos. 🟢
- **Mismatch de documentação**: `CLAUDE.md` diz que o Windows sincroniza "a cada 1h", e o código de setup (`New-TimeSpan -Minutes 60` em `scripts/sync/WINDOWS-SETUP.md`) concorda com isso — mas o **cabeçalho** de `scripts/sync/windows-auto-sync.ps1` ("Agendado pelo Task Scheduler a cada 15 min") e o **título da seção 4** do `WINDOWS-SETUP.md` ("Agendar a cada 15 min") ainda dizem 15 min. É doc desatualizada (não afeta o comportamento real, que segue o código de 60 min), mas vale corrigir os dois comentários para não confundir numa reinstalação futura. 🟡

## O que eu não consigo ver daqui

Rodo na nuvem e só enxergo o repositório git. **Não tenho acesso** ao LaunchAgent do Mac (`com.cassio.claude-autosync`), à task `ClaudeAutoSync` do Windows, nem a `~/.claude/.autosync/sync.log` — esse log é local-only e está fora do git, e é o único lugar que mostraria falha de rede/autenticação real (ao contrário de "a task simplesmente não rodou"). Então não posso afirmar "o sync está rodando" ou "está quebrado" com certeza — só afirmo o que os commits provam: Mac está commitando de forma consistente, Windows não.

Comandos pra rodar na máquina afetada (Windows) pra fechar o diagnóstico:

```powershell
Get-ScheduledTaskInfo -TaskName ClaudeAutoSync
Get-ScheduledTask -TaskName ClaudeAutoSync | Select State
```

```bash
# Mac, se quiser confirmar que o lado dele está saudável
launchctl print gui/$(id -u)/com.cassio.claude-autosync
tail -30 ~/.claude/.autosync/sync.log
```

O `sync.log` do Windows (se existir em `%USERPROFILE%\.claude\.autosync\sync.log`) é o que vai dizer se a task está rodando e falhando (rede, git, auth) ou simplesmente não está sendo disparada.

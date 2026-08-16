# Acervo de Conhecimento — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Transformar os digests diários e as pesquisas do `/last30days` num acervo de duas camadas que consolida conhecimento ao longo do tempo, com um grafo descartável por cima para revelar conexões.

**Architecture:** Markdown em git é a fonte da verdade. Camada 1 = diário imutável (`Pesquisas/`). Camada 2 = notas vivas por tema (`Acervo/`), editadas cirurgicamente. Três fluxos independentes: pesquisa (comando `/acervo`), consolidação diária (Routine na nuvem) e grafo (LaunchAgent no Mac, saída fora do vault).

**Tech Stack:** Markdown + git; bash (LaunchAgent, padrão do `vault-pull` já em produção); Node.js (painel agêntico existente); `graphifyy` via `uv tool`; Routine cloud `trig_018SJ1Au6eYbRA1YAJjk8dgU`.

**Spec:** `docs/superpowers/specs/2026-08-16-acervo-conhecimento-design.md`

## Global Constraints

- **Todo texto em pt-BR**, com acentuação correta. Nomes de arquivo de nota viva em linguagem natural (o wikilink do Obsidian resolve por nome).
- **Commits:** `<tipo>: <descrição>` — tipos `feat, fix, refactor, docs, test, chore, perf, ci`.
- **⚠️ Duas fontes de instrução:** regra de comportamento da camada 2 vive no `.automation/acervo-playbook.md` **e** o prompt da Routine só **aponta** para ele. Nunca duplicar regra nos dois (bug real de 02/07/2026 registrado no `CLAUDE.md` do obsidian-noticias).
- **Nota viva nunca é a única cópia:** o raw e o digest permanecem intactos. Reescrita destrutiva é proibida; só `Edit` cirúrgico.
- **Teto de 15 bullets** em `O que sabemos hoje`.
- **`atualizado: AAAA-MM-DD`** obrigatório no frontmatter, sempre com a data real da última evidência.
- **Toda alteração no vault termina em `commit` + `push`** — a Routine clona o repo; o que não foi pushado não existe para ela.
- **Não modificar `~/.claude/skills/last30days/`** — skill de terceiro, versionada (v3.8.3), com auto-update. A mudança se perde.
- **Scripts bash:** `set -uo pipefail`, `export PATH="/usr/bin:/bin:/usr/sbin:/sbin:/opt/homebrew/bin"`, lock via `mkdir`, log com rotação em 1 MB. Padrão de `~/.claude/tools/vault-pull/pull.sh`.
- **Caminhos absolutos** em plist e LaunchAgent (`/Users/cassiogoncalves/...`), nunca `~`.

---

### Task 1: Estrutura do acervo e o validador

O validador vem primeiro porque é o teste de tudo que vem depois: ele é o que
detecta a degradação silenciosa das notas vivas.

**Files:**
- Create: `/Users/cassiogoncalves/.claude/vault/Acervo/.gitkeep`
- Create: `/Users/cassiogoncalves/.claude/vault/Pesquisas/_pesquisas/.gitkeep`
- Create: `/Users/cassiogoncalves/.claude/tools/acervo/acervo-check.sh`
- Test (fixtures temporárias): `/Users/cassiogoncalves/.claude/vault/Acervo/_fixture-quebrada.md`

**Interfaces:**
- Consumes: nada (primeira task).
- Produces: `acervo-check.sh [caminho-do-vault]` → exit `0` se todas as invariantes passam, `1` se alguma falha, imprimindo uma linha `✗ <arquivo>: <problema>` por violação. Default do caminho: `$HOME/.claude/vault`. Todas as tasks seguintes usam este comando como gate.

- [ ] **Step 1: Criar as pastas**

```bash
mkdir -p /Users/cassiogoncalves/.claude/vault/Acervo
mkdir -p /Users/cassiogoncalves/.claude/vault/Pesquisas/_pesquisas
touch /Users/cassiogoncalves/.claude/vault/Acervo/.gitkeep
touch /Users/cassiogoncalves/.claude/vault/Pesquisas/_pesquisas/.gitkeep
mkdir -p /Users/cassiogoncalves/.claude/tools/acervo
```

- [ ] **Step 2: Escrever a fixture quebrada (o teste que deve falhar)**

Três violações de propósito: sem `atualizado` no frontmatter, um bullet sem
âncora, e um wikilink apontando para nota inexistente.

Criar `/Users/cassiogoncalves/.claude/vault/Acervo/_fixture-quebrada.md`:

```markdown
---
tema: Fixture Quebrada
tipo: nota-viva
criado: 2026-08-16
tags: [acervo]
---

## O que sabemos hoje
- Este fato tem âncora válida. [[👋 Comece aqui]]
- Este fato não tem âncora nenhuma.
- Este aponta para o vazio. [[Nota Que Não Existe]]

## Como isso mudou
- 2026-08-16 — fixture criada para testar o validador.

## Em aberto
- nada

## Origens
[[👋 Comece aqui]]
```

- [ ] **Step 3: Escrever o validador**

Criar `/Users/cassiogoncalves/.claude/tools/acervo/acervo-check.sh`:

```bash
#!/bin/bash
# Valida as invariantes das notas vivas do Acervo (camada 2 do acervo de conhecimento).
# Roda em segundos, sem framework. Existe para pegar a degradação silenciosa —
# o único modo de falha do acervo que não grita sozinho.
#
# Uso: acervo-check.sh [caminho-do-vault]
# Saída: 0 = todas as invariantes ok; 1 = alguma quebrada (lista os problemas).
set -uo pipefail
export PATH="/usr/bin:/bin:/usr/sbin:/sbin:/opt/homebrew/bin"

VAULT="${1:-$HOME/.claude/vault}"
ACERVO="$VAULT/Acervo"
MAX_BULLETS=15

ERRS=$(mktemp)
INDEX=$(mktemp)
trap 'rm -f "$ERRS" "$INDEX"' EXIT

# erro() escreve em arquivo, não em variável: as checagens rodam dentro de
# pipelines (subshell), e um contador em variável se perderia ao sair delas.
erro() { echo "✗ $1" >> "$ERRS"; }

[ -d "$ACERVO" ] || { echo "✗ $ACERVO não existe"; exit 1; }

shopt -s nullglob
notas=("$ACERVO"/*.md)
if [ ${#notas[@]} -eq 0 ]; then
  echo "nenhuma nota viva em $ACERVO — nada a validar"
  exit 0
fi

# Índice de nomes de nota do vault inteiro: o Obsidian resolve wikilink por nome
# de arquivo, em qualquer pasta. Montado uma vez só.
find "$VAULT" -name '*.md' -not -path '*/.git/*' -exec basename {} .md \; | sort -u > "$INDEX"

for nota in "${notas[@]}"; do
  base=$(basename "$nota")

  # Invariante 1 — frontmatter tem a data da última evidência.
  if ! grep -qE '^atualizado: [0-9]{4}-[0-9]{2}-[0-9]{2}$' "$nota"; then
    erro "$base: falta 'atualizado: AAAA-MM-DD' no frontmatter"
  fi

  # Recorta a seção "O que sabemos hoje" (até o próximo ##) uma vez só.
  secao=$(awk '/^## O que sabemos hoje/{f=1;next} /^## /{f=0} f' "$nota")

  # Invariante 2 — teto de bullets, para a nota poder esquecer.
  bullets=$(printf '%s\n' "$secao" | grep -c '^- ' || true)
  if [ "$bullets" -gt "$MAX_BULLETS" ]; then
    erro "$base: $bullets bullets em 'O que sabemos hoje' (teto: $MAX_BULLETS)"
  fi

  # Invariante 3 — todo fato termina em âncora. Fato sem âncora é fato inventado.
  printf '%s\n' "$secao" | grep '^- ' | grep -v ']]' | while IFS= read -r linha; do
    erro "$base: fato sem âncora → $(printf '%.60s' "$linha")"
  done

  # Invariante 4 — todo wikilink aponta para nota que existe.
  # Tira alias (|) e âncora de heading (#) antes de comparar.
  grep -o '\[\[[^]]*\]\]' "$nota" \
    | sed 's/^\[\[//; s/\]\]$//; s/|.*$//; s/#.*$//' \
    | sort -u | while IFS= read -r alvo; do
      [ -z "$alvo" ] && continue
      grep -qxF "$alvo" "$INDEX" || erro "$base: wikilink quebrado → [[$alvo]]"
    done
done

if [ -s "$ERRS" ]; then
  cat "$ERRS"
  echo "— $(wc -l < "$ERRS" | tr -d ' ') problema(s) em ${#notas[@]} nota(s)."
  exit 1
fi

echo "✓ ${#notas[@]} nota(s) viva(s), todas as invariantes ok."
exit 0
```

- [ ] **Step 4: Rodar contra a fixture e confirmar que FALHA**

```bash
chmod +x /Users/cassiogoncalves/.claude/tools/acervo/acervo-check.sh
/Users/cassiogoncalves/.claude/tools/acervo/acervo-check.sh
echo "exit=$?"
```

Esperado: exit `1` e exatamente estas três linhas (ordem pode variar):

```
✗ _fixture-quebrada.md: falta 'atualizado: AAAA-MM-DD' no frontmatter
✗ _fixture-quebrada.md: fato sem âncora → - Este fato não tem âncora nenhuma.
✗ _fixture-quebrada.md: wikilink quebrado → [[Nota Que Não Existe]]
```

Se aparecerem menos de três, o validador está com falso negativo — corrigir antes de seguir.

- [ ] **Step 5: Consertar a fixture e confirmar que PASSA**

Substituir o conteúdo de `/Users/cassiogoncalves/.claude/vault/Acervo/_fixture-quebrada.md` por:

```markdown
---
tema: Fixture Quebrada
tipo: nota-viva
criado: 2026-08-16
atualizado: 2026-08-16
tags: [acervo]
---

## O que sabemos hoje
- Este fato tem âncora válida. [[👋 Comece aqui]]

## Como isso mudou
- 2026-08-16 — fixture criada para testar o validador.

## Em aberto
- nada

## Origens
[[👋 Comece aqui]]
```

```bash
/Users/cassiogoncalves/.claude/tools/acervo/acervo-check.sh
echo "exit=$?"
```

Esperado: exit `0` e `✓ 1 nota(s) viva(s), todas as invariantes ok.`

- [ ] **Step 6: Apagar a fixture e commitar**

A fixture era o teste, não conteúdo. Sai antes do commit.

```bash
rm /Users/cassiogoncalves/.claude/vault/Acervo/_fixture-quebrada.md
cd /Users/cassiogoncalves/.claude/vault
git add Acervo/.gitkeep Pesquisas/_pesquisas/.gitkeep
git commit -m "feat: estrutura do acervo (Acervo/ e Pesquisas/_pesquisas/)"
git pull --rebase && git push
```

```bash
cd /Users/cassiogoncalves/.claude
git add tools/acervo/acervo-check.sh
git commit -m "feat: acervo-check.sh, validador das invariantes das notas vivas"
```

- [ ] **Step 7: Conferir o efeito colateral no painel agêntico**

O painel lista os subdiretórios de `Pesquisas/` como áreas
(`server.mjs:19-21`), então `_pesquisas` vai aparecer como uma área nova.
Isso é esperado e desejável — as pesquisas ficam visíveis ao lado dos digests.

```bash
curl -s localhost:4747/api/vault | head -c 400
```

Esperado: a resposta continua válida (JSON com `digests`). Se o painel não
estiver rodando, `curl` falha com "Connection refused" — isso não bloqueia
nada, só significa que a checagem visual fica para quando ele subir.

---

### Task 2: Playbook da consolidação

A fonte da verdade do comportamento da camada 2. Tanto o comando `/acervo`
(Task 3) quanto a Routine (Task 5) obedecem a este arquivo — é o que impede as
duas de divergirem.

**Files:**
- Create: `/Users/cassiogoncalves/.claude/vault/.automation/acervo-playbook.md`

**Interfaces:**
- Consumes: a estrutura `Acervo/` e `Pesquisas/_pesquisas/` da Task 1.
- Produces: o contrato de formato e as cinco regras anti-degradação, referenciados por caminho (`.automation/acervo-playbook.md`) pelas Tasks 3, 4 e 5.

- [ ] **Step 1: Escrever o playbook**

Criar `/Users/cassiogoncalves/.claude/vault/.automation/acervo-playbook.md`:

````markdown
# Playbook do Acervo (camada 2 — notas vivas)

Fonte da verdade do comportamento das notas vivas. Quem consome: o comando
`/acervo` (ingestão de pesquisas) e a Routine dos digests (consolidação diária).

⚠️ **Não duplicar estas regras no prompt da Routine.** O prompt deve apenas
apontar para este arquivo. Regra escrita em dois lugares diverge — foi o que
causou o bug das imagens em 02/07/2026.

## Formato da nota viva

Uma nota por tema, em `Acervo/<Tema em linguagem natural>.md`:

```markdown
---
tema: Prontuário Eletrônico com IA
tipo: nota-viva
criado: 2026-06-28
atualizado: 2026-08-13
tags: [acervo, ia, saude]
---

## O que sabemos hoje
- Médicos gastam ~2h/dia digitando prontuário. [[2026-08-10 — Pesquisa: tempo digitando]]

## Como isso mudou
- 2026-06-28 — primeira leitura do tema, mercado dominado por teclado.

## Em aberto
- Ninguém mediu adesão real depois de 90 dias.

## Origens
[[2026-08-13 — Pesquisa: ditado por voz]] · [[2026-08-10 12h00 — IA Digest]]
```

O nome do arquivo é o próprio tema, em linguagem natural, para o wikilink do
Obsidian resolver sem alias.

## As cinco regras anti-degradação

1. **`Como isso mudou` é append-only.** Só acrescentar linha no fim. Nunca
   reescrever, nunca "enxugar" o histórico. Se a síntese do topo degradar, o log
   preserva a trajetória.
2. **Todo fato carrega âncora.** Cada bullet de `O que sabemos hoje` termina num
   wikilink para a nota de origem. Fato sem âncora é fato inventado e pode ser
   removido sem perda.
3. **Reescrita é edição cirúrgica.** Usar `Edit` pontual. **Nunca** reescrever a
   nota do zero — se o texto antigo não volta a passar pelo modelo, ele não
   pode se deformar.
4. **A nota viva nunca é a única cópia.** O digest e o raw ficam intactos. Cada
   reescrita é um commit; `git log -p Acervo/` é o desfazer.
5. **Teto de 15 bullets** em `O que sabemos hoje`. Ao estourar, o mais antigo ou
   o menos ancorado desce para o log. Mente que aprende também descarta.

## Dedupe por URL

Antes de acrescentar um fato, conferir as fontes já citadas na própria nota.
URL já registrada não vira fato novo — vira, no máximo, uma linha no log
dizendo que o assunto voltou.

## Datas não se disfarçam

`atualizado` recebe a data da evidência mais recente que entrou na nota, não a
data em que o arquivo foi tocado. Nota alimentada por pesquisa de junho continua
`atualizado: 2026-06-28` até chegar coisa nova. Sem isso, afirmação velha é lida
como atual daqui a seis meses.

## Como decidir se um tema foi "tocado"

Um tema foi tocado quando alguma notícia do dia trata do mesmo assunto do campo
`tema` da nota. Na dúvida, **não tocar**: nota parada é barata, nota poluída não.
Nenhum tema tocado é o resultado normal da maioria dos dias.

## Validação

Depois de qualquer escrita em `Acervo/`, rodar:

```bash
/Users/cassiogoncalves/.claude/tools/acervo/acervo-check.sh
```

Exit `0` é obrigatório antes do commit. Se falhar, corrigir a nota — nunca
afrouxar o validador.
````

- [ ] **Step 2: Validar que o playbook não quebra o validador**

O playbook tem wikilinks dentro de blocos de exemplo, mas está em
`.automation/`, não em `Acervo/` — o validador só varre `Acervo/*.md`.

```bash
/Users/cassiogoncalves/.claude/tools/acervo/acervo-check.sh
echo "exit=$?"
```

Esperado: exit `0`, com `nenhuma nota viva em ... — nada a validar` (a fixture
foi apagada na Task 1 e nenhuma nota real existe ainda).

- [ ] **Step 3: Commitar**

```bash
cd /Users/cassiogoncalves/.claude/vault
git add .automation/acervo-playbook.md
git commit -m "docs: playbook da camada 2 do acervo"
git pull --rebase && git push
```

---

### Task 3: Comando `/acervo` — ingestão idempotente

**Files:**
- Create: `/Users/cassiogoncalves/.claude/commands/acervo.md`

**Interfaces:**
- Consumes: `acervo-check.sh` (Task 1), `.automation/acervo-playbook.md` (Task 2).
- Produces: o comando `/acervo`, que lê `~/Documents/Last30Days/*.md`, escreve notas em `Pesquisas/_pesquisas/AAAA-MM-DD — Pesquisa: <tema>.md` e notas vivas em `Acervo/<Tema>.md`. Idempotência: um raw já ingerido aparece em `raws:` no frontmatter de alguma nota datada.

- [ ] **Step 1: Escrever o comando**

Criar `/Users/cassiogoncalves/.claude/commands/acervo.md`:

````markdown
---
description: Ingere as pesquisas do /last30days no acervo do vault (idempotente)
---

Ingerir no acervo do vault todas as pesquisas do `/last30days` que ainda não
foram ingeridas. É idempotente: rodar duas vezes seguidas não cria nada na
segunda. Serve tanto para o backfill quanto para o uso contínuo.

**Antes de tudo, leia `~/.claude/vault/.automation/acervo-playbook.md`.** Ele é a
fonte da verdade do formato e das cinco regras anti-degradação. Não improvise
formato.

## Passo 1 — descobrir o que está pendente

```bash
ls -lT ~/Documents/Last30Days/*.md
grep -rh '^raws:' ~/.claude/vault/Pesquisas/_pesquisas/ 2>/dev/null | sort -u
```

Pendente = arquivo de `~/Documents/Last30Days/` cujo nome **não** aparece em
nenhuma linha `raws:` das notas já existentes. Se nada estiver pendente, diga
isso e pare — não reescreva nada.

## Passo 2 — agrupar

Agrupar os raws pendentes por **(tema, data de modificação)**. Raws diferentes do
mesmo tema e mesmo dia são a mesma pesquisa refeita ou recortada por fonte
(ex.: `...-raw-v3.md`, `-v4x`, `-v5x`; ou `plantao-medico-raw-creators.md` e
`plantao-raw-ig.md`) — viram **uma** nota datada só, listando todos em `raws:`.

Derivar o `tema` em português legível a partir do conteúdo do raw, não do nome
do arquivo (os nomes vêm com acento comido: `prontu-rio-eletr-nico`).

## Passo 3 — escrever a nota datada (camada 1)

Uma por grupo, em
`~/.claude/vault/Pesquisas/_pesquisas/AAAA-MM-DD — Pesquisa: <tema>.md`,
onde a data é a de modificação do raw:

```markdown
---
title: "Pesquisa: <tema>"
date: AAAA-MM-DD
tags: [pesquisa, last30days]
tema: <tema>
raws: [arquivo-1.md, arquivo-2.md]
source: last30days
---

## O que a pesquisa encontrou
<síntese em 5 a 12 bullets, cada um com a fonte entre parênteses e o link>

## Fontes
<lista de URLs relevantes do raw>
```

Sintetizar, não copiar: os raws somam 868 KB e o valor está na leitura, não no
despejo. O raw original continua em `~/Documents/Last30Days/` e não se move —
são dumps ruidosos, ruins para o grafo e grandes demais para o git do vault.

## Passo 4 — criar ou atualizar a nota viva (camada 2)

Para cada tema, em `~/.claude/vault/Acervo/<Tema>.md`, seguindo o playbook:

- **Não existe:** criar com `criado` e `atualizado` na data da pesquisa.
- **Já existe:** `Edit` cirúrgico. Acrescentar só o que é novo (dedupe por URL
  contra as fontes já citadas), acrescentar **uma** linha em `Como isso mudou`,
  atualizar `atualizado`. Nunca reescrever a nota inteira.

Se o teto de 15 bullets estourar, descer o mais antigo ou o menos ancorado para
o log — não apagar sem registro.

## Passo 5 — validar e publicar

```bash
/Users/cassiogoncalves/.claude/tools/acervo/acervo-check.sh
```

Exit `0` é obrigatório. Se falhar, corrigir a nota — nunca afrouxar o validador.

```bash
cd ~/.claude/vault
git add Acervo/ Pesquisas/_pesquisas/
git commit -m "acervo: ingestão de <N> pesquisa(s) — <temas>"
git pull --rebase && git push
```

O `push` não é opcional: a Routine na nuvem **clona** o repo, e nota viva que não
foi pushada não existe para ela — o tema nunca seria alimentado pelos digests.

## Ao final, reporte

Quantos raws foram ingeridos, quantos foram pulados por já existirem, quais notas
vivas nasceram e quais foram atualizadas.
````

- [ ] **Step 2: Rodar em modo seco sobre um raw só**

Escolher o raw mais recente e ingerir apenas ele, para validar o formato antes
do lote:

```
/acervo
```

Quando o comando listar os pendentes, instruir a processar **somente**
`medicina-medicos-aplicativo-plantao-medico-raw-v3.md` (13/08/2026) nesta
primeira execução.

- [ ] **Step 3: Verificar o resultado**

```bash
ls "/Users/cassiogoncalves/.claude/vault/Pesquisas/_pesquisas/"
ls "/Users/cassiogoncalves/.claude/vault/Acervo/"
/Users/cassiogoncalves/.claude/tools/acervo/acervo-check.sh
echo "exit=$?"
```

Esperado: uma nota datada, uma nota viva, exit `0` com `✓ 1 nota(s) viva(s)`.

- [ ] **Step 4: Provar a idempotência**

```
/acervo
```

Esperado: o comando reporta que o raw já foi ingerido e **não escreve nada**.
Confirmar:

```bash
cd /Users/cassiogoncalves/.claude/vault && git status --porcelain
```

Esperado: saída vazia. Se houver arquivo modificado, a idempotência quebrou —
corrigir o Passo 1 do comando antes de seguir.

- [ ] **Step 5: Commitar o comando**

```bash
cd /Users/cassiogoncalves/.claude
git add commands/acervo.md
git commit -m "feat: comando /acervo para ingestão idempotente de pesquisas"
```

---

### Task 4: Backfill dos temas já pesquisados

**Files:**
- Modify: `/Users/cassiogoncalves/.claude/vault/Acervo/` (cerca de 13 notas vivas)
- Modify: `/Users/cassiogoncalves/.claude/vault/Pesquisas/_pesquisas/` (cerca de 13 notas datadas)

**Interfaces:**
- Consumes: comando `/acervo` (Task 3).
- Produces: o acervo povoado — a base sobre a qual a Routine (Task 5) passa a trabalhar.

- [ ] **Step 1: Rodar o backfill**

```
/acervo
```

Processar todos os raws pendentes. São 16 arquivos, 15 restantes após a Task 3,
resultando em cerca de 13 temas distintos (os três `reclama-es-amplimed-iclinic`
v3/v4x/v5x agrupam em um; `plantao-medico-raw-creators` e `plantao-raw-ig`
agrupam com o de plantão médico).

- [ ] **Step 2: Conferir o agrupamento**

```bash
ls "/Users/cassiogoncalves/.claude/vault/Acervo/"
grep -h '^raws:' "/Users/cassiogoncalves/.claude/vault/Pesquisas/_pesquisas/"*.md
```

Esperado: cerca de 13 notas vivas, e uma linha `raws:` contendo os três arquivos
`reclama-es-amplimed-iclinic-*` juntos. Se saírem 16 notas vivas, o agrupamento
do Passo 2 do comando falhou — corrigir e refazer antes de commitar.

- [ ] **Step 3: Conferir as datas**

```bash
grep -h '^atualizado:' "/Users/cassiogoncalves/.claude/vault/Acervo/"*.md | sort | uniq -c
```

Esperado: datas espalhadas entre `2026-06-28` e `2026-08-13`, **não** todas com a
data de hoje. Nota nascida de pesquisa de junho descreve o mundo de junho — se
todas vierem com a data de hoje, a regra "datas não se disfarçam" foi violada e o
acervo já nasce mentindo sobre a própria idade.

- [ ] **Step 4: Validar e publicar**

```bash
/Users/cassiogoncalves/.claude/tools/acervo/acervo-check.sh
echo "exit=$?"
cd /Users/cassiogoncalves/.claude/vault && git log --oneline -3 && git status -sb
```

Esperado: exit `0`, commits feitos pelo comando, e `## main...origin/main` sem
`ahead` (o push saiu).

---

### Task 5: Consolidação diária na Routine

⚠️ Esta é a task da armadilha das duas fontes. O playbook (Task 2) já tem as
regras; o prompt da Routine deve **apontar** para ele, nunca repeti-las.

**Files:**
- Modify: prompt da Routine cloud `trig_018SJ1Au6eYbRA1YAJjk8dgU` (via skill `schedule` / `RemoteTrigger`)

**Interfaces:**
- Consumes: `Acervo/` povoado (Task 4), `.automation/acervo-playbook.md` (Task 2).
- Produces: notas vivas atualizadas diariamente às 06:00 BRT, em commit separado do commit dos digests.

- [ ] **Step 1: Ler o prompt atual e guardá-lo**

```
Skill: schedule
```

Usar `RemoteTrigger` com `action: get` e `trigger_id: trig_018SJ1Au6eYbRA1YAJjk8dgU`.
Salvar o prompt atual em
`/Users/cassiogoncalves/.claude/vault/.automation/routine-prompt-backup.md`
antes de qualquer alteração e commitar — é o rollback, e versionado ele para de
depender de scratchpad de sessão:

```bash
cd /Users/cassiogoncalves/.claude/vault
git add .automation/routine-prompt-backup.md
git commit -m "chore: backup do prompt da Routine antes da etapa de acervo"
```

- [ ] **Step 2: Acrescentar a etapa final ao prompt**

Acrescentar ao **fim** do prompt atual, sem alterar nada do que já existe:

```
ETAPA FINAL — ACERVO (só depois do commit dos digests estar feito):

1. Leia `.automation/acervo-playbook.md` e siga-o à risca. Ele é a fonte da
   verdade do formato e das regras; este prompt não as repete de propósito.
2. Rode `ls Acervo/` para ver os temas vivos. NÃO leia o conteúdo de todos.
3. Decida quais temas as notícias de hoje tocaram. Nenhum tocado é o resultado
   normal da maioria dos dias — nesse caso, encerre aqui sem escrever nada.
4. Só para os tocados: leia a nota e faça edição cirúrgica com Edit. Nunca
   reescreva a nota do zero.
5. Commit separado dos digests:
   git add Acervo/ && git commit -m "acervo: <temas tocados>"
   git pull --rebase && git push
6. No relatório final, informe quais temas foram tocados (ou "nenhum").

Se algo falhar aqui, os digests já estão salvos e commitados — não tente
desfazê-los.
```

Aplicar com `RemoteTrigger` `action: update`.

- [ ] **Step 3: Disparar um teste manual**

```
RemoteTrigger action: run, trigger_id: trig_018SJ1Au6eYbRA1YAJjk8dgU
```

- [ ] **Step 4: Verificar que só o certo mudou**

Aguardar a execução terminar, então:

```bash
cd /Users/cassiogoncalves/.claude/vault
git fetch origin && git log --oneline origin/main -5
git diff --stat HEAD..origin/main
```

Esperado: um commit de digests e, **se algum tema foi tocado**, um commit
`acervo: ...` separado mexendo só em `Acervo/`. Se o commit de acervo tocar
arquivos de `Pesquisas/`, a separação falhou — corrigir o prompt.

- [ ] **Step 5: Validar as notas após a Routine**

```bash
cd /Users/cassiogoncalves/.claude/vault && git pull --ff-only
/Users/cassiogoncalves/.claude/tools/acervo/acervo-check.sh
echo "exit=$?"
```

Esperado: exit `0`. Se a Routine produziu fato sem âncora ou estourou o teto, o
validador acusa aqui — corrigir o playbook (não o prompt) e repetir o Step 3.

- [ ] **Step 6: Registrar a mudança das duas fontes**

Confirmar por leitura que a regra de comportamento está **só** no playbook e que
o prompt apenas aponta para ele. Se alguma regra tiver sido copiada para o
prompt, remover do prompt.

---

### Task 6: Instalar o graphify e medir antes de gastar

O custo da primeira extração sobre 419 notas é desconhecido. Esta task existe
para medir num subconjunto e decidir com número na mão. Se o custo assustar,
abandonar o grafo aqui não custa nada — ele é a peça descartável.

**Files:**
- Create: `/Users/cassiogoncalves/.local/share/acervo-grafo/` (diretório de trabalho, fora do vault)

**Interfaces:**
- Consumes: o vault povoado.
- Produces: `graphify` no PATH e uma medição real de tempo/custo por nota.

- [ ] **Step 1: Instalar**

```bash
uv tool install graphifyy
which graphify && graphify --help | head -20
```

Esperado: caminho do binário e o texto de ajuda. Se `uv` não existir,
`brew install uv` primeiro.

- [ ] **Step 2: Medir numa área só**

```bash
mkdir -p /Users/cassiogoncalves/.local/share/acervo-grafo
cd /Users/cassiogoncalves/.local/share/acervo-grafo
ls /Users/cassiogoncalves/.claude/vault/Pesquisas/IA/*.md | wc -l
time graphify /Users/cassiogoncalves/.claude/vault/Pesquisas/IA --no-viz
```

Anotar: número de notas, tempo de parede, e qualquer linha de custo/tokens que a
ferramenta imprimir.

- [ ] **Step 3: Extrapolar e reportar ao Cássio**

Calcular o custo projetado para 419 notas a partir da medição e **parar para
confirmação** antes de rodar o build completo. Reportar:

- notas medidas, tempo, custo observado;
- projeção linear para 419 notas;
- o que muda se ele disser não (nada — as camadas 1 e 2 seguem funcionando).

- [ ] **Step 4: Build completo (só após o "pode ir")**

```bash
cd /Users/cassiogoncalves/.local/share/acervo-grafo
time graphify /Users/cassiogoncalves/.claude/vault
ls -la graphify-out/
```

Esperado: `graphify-out/graph.json`, `graphify-out/index.html` e
`graphify-out/GRAPH_REPORT.md`.

- [ ] **Step 5: Confirmar que nada vazou para o vault**

```bash
cd /Users/cassiogoncalves/.claude/vault && git status --porcelain
```

Esperado: saída vazia. O grafo mora fora do vault por decisão de design; se
aparecer `graphify-out/` aqui, foi rodado no diretório errado — apagar e refazer
a partir de `~/.local/share/acervo-grafo`.

---

### Task 7: Automação do grafo, painel e documentação

**Files:**
- Create: `/Users/cassiogoncalves/.claude/tools/acervo/grafo.sh`
- Create: `/Users/cassiogoncalves/Library/LaunchAgents/com.cassio.acervo-grafo.plist`
- Modify: `/Users/cassiogoncalves/.claude/painel-agentico/server.mjs`
- Modify: `/Users/cassiogoncalves/.claude/workstations/obsidian-noticias/CLAUDE.md`
- Modify: `/Users/cassiogoncalves/.claude/workstations/obsidian-noticias/MEMORY.md`

**Interfaces:**
- Consumes: `graphify` instalado (Task 6).
- Produces: `grafo.sh` rodando 1×/dia; rota `GET /grafo` no painel servindo `graphify-out/index.html`.

- [ ] **Step 1: Escrever o script do grafo**

Criar `/Users/cassiogoncalves/.claude/tools/acervo/grafo.sh`, no mesmo padrão do
`vault-pull/pull.sh` (lock por `mkdir`, log com rotação, PATH explícito):

```bash
#!/bin/bash
# Reconstrói o grafo do acervo a partir do vault, 1x/dia.
# Chamado pelo LaunchAgent com.cassio.acervo-grafo.
#
# A saída fica FORA do vault de propósito: o grafo é descartável. Se sumir,
# nenhuma nota se perde — apagar a pasta e rodar de novo reconstrói tudo.
set -uo pipefail
export PATH="$HOME/.local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/opt/homebrew/bin"

VAULT="$HOME/.claude/vault"
OUT="$HOME/.local/share/acervo-grafo"
LOG="$HOME/Library/Logs/acervo-grafo.log"
LOCK="$HOME/Library/Caches/acervo-grafo.lock"
MAX_LOG_BYTES=1048576

ts() { date '+%Y-%m-%d %H:%M:%S'; }
log() { echo "[$(ts)] $1" >> "$LOG"; }

if [ -f "$LOG" ] && [ "$(stat -f%z "$LOG" 2>/dev/null || echo 0)" -gt "$MAX_LOG_BYTES" ]; then
  : > "$LOG"
fi

# Lock: mkdir é atômico. Lock preso há mais de 2h é órfão (o build completo é lento).
if ! mkdir "$LOCK" 2>/dev/null; then
  if find "$LOCK" -maxdepth 0 -mmin +120 2>/dev/null | grep -q .; then
    rmdir "$LOCK" 2>/dev/null
    mkdir "$LOCK" 2>/dev/null || exit 0
  else
    exit 0
  fi
fi
trap 'rmdir "$LOCK" 2>/dev/null' EXIT

command -v graphify >/dev/null 2>&1 || { log "ERRO: graphify não está no PATH"; exit 1; }
[ -d "$VAULT" ] || { log "ERRO: $VAULT não encontrado"; exit 1; }

mkdir -p "$OUT"
cd "$OUT" || exit 1

# --update: re-extrai só o que mudou. O build completo é a rodada cara e já foi
# feito uma vez à mão; daqui pra frente são ~5-8 notas novas por dia.
if graphify "$VAULT" --update >> "$LOG" 2>&1; then
  log "ok: grafo atualizado ($(find "$VAULT" -name '*.md' -not -path '*/.git/*' | wc -l | tr -d ' ') notas no vault)"
else
  log "ERRO: graphify falhou — ver saída acima"
  osascript -e 'display notification "Falha ao atualizar o grafo do acervo." with title "Acervo" sound name "Basso"' 2>/dev/null || true
  exit 1
fi
```

- [ ] **Step 2: Testar o script à mão**

```bash
chmod +x /Users/cassiogoncalves/.claude/tools/acervo/grafo.sh
/Users/cassiogoncalves/.claude/tools/acervo/grafo.sh
echo "exit=$?"
tail -5 ~/Library/Logs/acervo-grafo.log
```

Esperado: exit `0` e uma linha `ok: grafo atualizado (N notas no vault)`.

- [ ] **Step 3: Testar o lock**

```bash
mkdir ~/Library/Caches/acervo-grafo.lock
/Users/cassiogoncalves/.claude/tools/acervo/grafo.sh
echo "exit=$? (esperado 0, sem nova linha no log)"
rmdir ~/Library/Caches/acervo-grafo.lock
```

Esperado: exit `0` e nenhuma linha nova no log — a segunda execução saiu cedo
em vez de disputar a primeira.

- [ ] **Step 4: Instalar o LaunchAgent**

Criar `/Users/cassiogoncalves/Library/LaunchAgents/com.cassio.acervo-grafo.plist`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.cassio.acervo-grafo</string>

    <key>ProgramArguments</key>
    <array>
        <string>/bin/bash</string>
        <string>/Users/cassiogoncalves/.claude/tools/acervo/grafo.sh</string>
    </array>

    <key>StartInterval</key>
    <integer>86400</integer>

    <key>RunAtLoad</key>
    <true/>

    <key>StandardOutPath</key>
    <string>/Users/cassiogoncalves/Library/Logs/acervo-grafo.log</string>
    <key>StandardErrorPath</key>
    <string>/Users/cassiogoncalves/Library/Logs/acervo-grafo.log</string>
</dict>
</plist>
```

```bash
launchctl bootstrap gui/$(id -u) /Users/cassiogoncalves/Library/LaunchAgents/com.cassio.acervo-grafo.plist
launchctl list | grep acervo-grafo
```

Esperado: uma linha com o label `com.cassio.acervo-grafo`.

- [ ] **Step 5: Adicionar a rota do grafo no painel**

Em `/Users/cassiogoncalves/.claude/painel-agentico/server.mjs`, acrescentar a
constante junto das outras (perto da linha 17):

```js
const GRAFO_FILE = path.join(os.homedir(), '.local', 'share', 'acervo-grafo', 'graphify-out', 'index.html');
```

E a rota, imediatamente antes do `json(res, 404, { erro: 'rota não encontrada' })`
no fim do handler:

```js
  if (route === 'GET /grafo') {
    if (!fs.existsSync(GRAFO_FILE)) {
      json(res, 404, { erro: 'grafo ainda não foi gerado — rode tools/acervo/grafo.sh' });
      return;
    }
    res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
    res.end(fs.readFileSync(GRAFO_FILE));
    return;
  }
```

- [ ] **Step 6: Testar a rota**

```bash
pkill -f "node.*painel-agentico" 2>/dev/null; sleep 1
(cd /Users/cassiogoncalves/.claude/painel-agentico && node server.mjs &) ; sleep 2
curl -s -o /dev/null -w "%{http_code} %{content_type}\n" localhost:4747/grafo
```

Esperado: `200 text/html; charset=utf-8`.

- [ ] **Step 7: Documentar na workstation**

Acrescentar ao `CLAUDE.md` da workstation, depois da seção "Arquitetura":

```markdown
## Acervo — duas camadas

O vault tem duas camadas de conhecimento, e elas não se misturam:

- **Camada 1, diário imutável:** `Pesquisas/<área>/` (digests da Routine) e
  `Pesquisas/_pesquisas/` (notas datadas das pesquisas do `/last30days`).
  Nada aqui é reescrito depois de criado.
- **Camada 2, notas vivas:** `Acervo/<Tema>.md`, uma por tema, editada
  cirurgicamente conforme chega novidade. Um tema entra na camada 2 quando o
  Cássio roda `/last30days` sobre ele — pesquisar é declarar interesse.

**Fonte da verdade do comportamento:** `.automation/acervo-playbook.md`. O
prompt da Routine apenas **aponta** para ele — não repetir regra nos dois
(mesma armadilha das imagens em 02/07/2026).

**Gate obrigatório:** `~/.claude/tools/acervo/acervo-check.sh` precisa sair com
exit 0 antes de qualquer commit em `Acervo/`. Ele valida as quatro invariantes
(frontmatter com `atualizado`, fato com âncora, teto de 15 bullets, wikilink
que resolve). Nunca afrouxar o validador para fazer uma nota passar.

**Grafo:** `~/.local/share/acervo-grafo/graphify-out/`, FORA do vault e
descartável — se sumir, nenhuma nota se perde. Atualizado 1×/dia pelo
LaunchAgent `com.cassio.acervo-grafo` (plist em `~/Library/LaunchAgents/`, fora
do repo: numa máquina nova precisa ser recriado à mão, igual ao `vault-pull`).
Visível em `localhost:4747/grafo` pelo painel agêntico.
```

Em `MEMORY.md`, registrar como fato datado: a data de entrada em produção, a
lista dos ~13 temas iniciais, e **o custo medido na Task 6** (notas, tempo, custo
do build completo). Esse número é o que ninguém vai lembrar depois e é o que
decide se vale reconstruir o grafo do zero no futuro.

- [ ] **Step 8: Commitar tudo**

```bash
cd /Users/cassiogoncalves/.claude
git add tools/acervo/grafo.sh painel-agentico/server.mjs \
        workstations/obsidian-noticias/CLAUDE.md workstations/obsidian-noticias/MEMORY.md
git commit -m "feat: automação do grafo do acervo e rota /grafo no painel"
```

O plist fica em `~/Library/LaunchAgents/`, fora do repo — como o do `vault-pull`.
Registrar no `CLAUDE.md` da workstation que ele existe e precisa ser recriado à
mão numa máquina nova.

---

## Ordem e dependências

```
Task 1 (estrutura + validador)
   └─> Task 2 (playbook)
         ├─> Task 3 (/acervo) ──> Task 4 (backfill) ──> Task 5 (Routine)
         └─────────────────────────────────────────────────┘
Task 6 (medir graphify) ──> Task 7 (automação + painel + docs)
```

Tasks 1–5 entregam o acervo funcionando sem nenhum grafo. Tasks 6–7 são a camada
de descoberta e podem ser abandonadas sem prejuízo se o custo medido não
compensar.

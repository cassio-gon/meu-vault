# Digests do Vault via Routine do Claude Cloud — Plano de Implementação

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Substituir os 8 crons do GitHub Actions por uma única Routine do Claude Cloud que, todo dia às 06:00 BRT, gera os digests das 8 áreas em sequência e dá um push só no repo `meu-vault` — mantendo o formato de nota idêntico.

**Architecture:** Um playbook versionado (`.automation/digest-playbook.md`) descreve, passo a passo, como o agente gera os digests. A Routine dispara uma sessão cloud fresca por dia, que clona `meu-vault`, lê o playbook e o executa para as 8 áreas, commitando uma vez. Os workflows antigos do GitHub Actions são desativados (schedule comentado) mas mantidos como fallback.

**Tech Stack:** Claude Cloud Routines (cron), Git, firecrawl/web search nativa, Markdown. Sem Python, sem Gemini no caminho novo.

## Global Constraints

- Repo alvo: `cassio-gon/meu-vault`, branch `main`. Push autorizado obrigatório.
- Fuso: todos os timestamps em **BRT (UTC-3)**; cron da Routine em **09:00 UTC** (= 06:00 BRT).
- Áreas (ordem do run): IA, Saúde, Medicina do Trabalho, Mercado Financeiro, Puerpério, RN, Filmes e Séries, Jogos.
- Formato de nota: idêntico ao contrato do spec; `source: claude code`.
- Dedupe: descartar tópicos já presentes nos digests dos **últimos 3 dias** da pasta da área.
- ~5 tópicos por área (mínimo 3; não inventar se faltar material).
- Resumos sempre em pt-BR. Cada tópico precisa de título, resumo e URL reais.
- Falha de uma área não derruba as outras; commit final inclui o que deu certo.
- Camada de leitura (app que lê do Obsidian/GitHub) **não muda** — mesmo repo, pastas, nomes e formato.
- Spec de referência: `docs/superpowers/specs/2026-06-30-vault-digests-claude-cloud-design.md`.

---

## File Structure

- Create: `.automation/area-sources.md` — fontes curadas por área (dica de busca), extraídas de `main.py`.
- Create: `.automation/digest-playbook.md` — playbook que o agente executa todo dia.
- Modify: `.github/workflows/{filmes,ia,jogos,medtrab,mercfin,puerperio,rn,saude}-digest.yml` — comentar `schedule:`.
- Operacional (sem arquivo): criar a Routine; disparo de validação.

Pasta `.automation/` é oculta → o Obsidian/app não exibem esses arquivos. Mantém a camada de leitura limpa.

---

### Task 1: Fontes curadas por área (referência de busca)

**Files:**
- Create: `.automation/area-sources.md`
- Reference: `.automation/main.py:28-97` (dict `DIGEST_SOURCES`)

**Interfaces:**
- Produces: arquivo `.automation/area-sources.md` com uma seção por área, cada uma listando as URLs curadas. O playbook (Task 2) referencia este arquivo como "dica".

- [ ] **Step 1: Extrair as fontes do main.py**

Ler `.automation/main.py` linhas 28–97 e copiar as URLs de cada área para o novo arquivo. Não inventar URLs — usar exatamente as que estão lá.

- [ ] **Step 2: Escrever `.automation/area-sources.md`**

Estrutura (preencher cada lista com as URLs reais de `DIGEST_SOURCES`):

```markdown
# Fontes curadas por área (dica de busca)

> Ponto de partida, NÃO restrição. A Routine faz busca aberta por tema; use estas
> fontes como referência de qualidade e como sementes de busca. Extraído de
> `.automation/main.py` (DIGEST_SOURCES).

## IA — pasta `Pesquisas/IA` — tag `ia`
- https://techcrunch.com/category/artificial-intelligence/feed/
- https://www.wired.com/feed/tag/ai/latest/rss
- https://www.technologyreview.com/feed/
- https://tecnoblog.net/feed/
- https://news.google.com/rss/search?q=inteligencia+artificial+ia&hl=pt-BR&gl=BR&ceid=BR:pt-419

## Saúde — pasta `Pesquisas/Saude` — tag `saude`
- (copiar as 5 URLs da área "Saude")

## Medicina do Trabalho — pasta `Pesquisas/Medicina do Trabalho` — tag `medtrab`
- (copiar as 7 URLs da área "MedTrab")

## Mercado Financeiro — pasta `Pesquisas/Mercado Financeiro` — tag `mercado-financeiro`
- (copiar as 5 URLs da área "MercFin")

## Puerpério — pasta `Pesquisas/Puerperio` — tag `puerperio`
- (copiar as 5 URLs da área "Puerperio")

## Recém-Nascidos — pasta `Pesquisas/RN` — tag `recem-nascidos`
- (copiar as 5 URLs da área "RN")

## Filmes e Séries — pasta `Pesquisas/Filmes e Series` — tag `filmes-series`
- (copiar as 5 URLs da área "Filmes")

## Jogos — pasta `Pesquisas/Jogos` — tag `jogos`
- (copiar as 5 URLs da área "Jogos")
```

- [ ] **Step 3: Verificar que toda área tem pasta, tag e fontes**

Run: `for a in IA Saude "Medicina do Trabalho" "Mercado Financeiro" Puerperio RN "Filmes e Series" Jogos; do test -d "Pesquisas/$a" && echo "OK pasta: $a" || echo "FALTA pasta: $a"; done`
Expected: 8 linhas "OK pasta". Conferir manualmente que o `.md` tem 8 seções, cada uma com tag e ≥1 URL.

- [ ] **Step 4: Commit**

```bash
git add .automation/area-sources.md
git commit -m "feat: fontes curadas por área como referência de busca da Routine"
```

---

### Task 2: Playbook do agente (núcleo)

**Files:**
- Create: `.automation/digest-playbook.md`
- Reference: `docs/superpowers/specs/2026-06-30-vault-digests-claude-cloud-design.md`, `.automation/area-sources.md`

**Interfaces:**
- Consumes: `.automation/area-sources.md` (Task 1) como dica de fontes.
- Produces: `.automation/digest-playbook.md` — documento único que a Routine manda o agente "ler e executar". Define ordem das áreas, formato exato da nota, dedupe, robustez e o passo de commit/push.

- [ ] **Step 1: Escrever o playbook completo**

Conteúdo de `.automation/digest-playbook.md` (verbatim, ajustando só o que estiver entre colchetes se necessário):

````markdown
# Playbook: Digests diários do Vault

Você é executado por uma Routine às 06:00 BRT. Objetivo: gerar o digest de hoje para
**cada uma das 8 áreas**, em sequência, e fazer **um único** commit+push no fim.
Trabalhe na raiz do repo `meu-vault` já clonado. NÃO altere nada fora de `Pesquisas/`.

## Ordem das áreas (faça nesta ordem)
1. IA → `Pesquisas/IA` → tag `ia`
2. Saúde → `Pesquisas/Saude` → tag `saude`
3. Medicina do Trabalho → `Pesquisas/Medicina do Trabalho` → tag `medtrab`
4. Mercado Financeiro → `Pesquisas/Mercado Financeiro` → tag `mercado-financeiro`
5. Puerpério → `Pesquisas/Puerperio` → tag `puerperio`
6. Recém-Nascidos → `Pesquisas/RN` → tag `recem-nascidos`
7. Filmes e Séries → `Pesquisas/Filmes e Series` → tag `filmes-series`
8. Jogos → `Pesquisas/Jogos` → tag `jogos`

## Para cada área, faça:

### 1. Dedupe — leia o que já saiu
Liste os 3 arquivos `*Digest.md` mais recentes da pasta da área e leia seus títulos de
tópico. Guarde-os como "já publicado".

### 2. Busca aberta do dia
Busque as notícias/conteúdos mais relevantes de HOJE (ou das últimas ~48h) para o tema da
área. Use `.automation/area-sources.md` como referência de fontes confiáveis e sementes,
mas você pode ir além delas (busca aberta). Priorize conteúdo datado e recente.

### 3. Seleção
Escolha os ~5 tópicos mais relevantes. **Descarte** qualquer um cujo assunto já apareça
nos digests dos últimos 3 dias (passo 1), salvo se houver desdobramento claramente novo.
Mínimo 3 tópicos; se não houver material suficiente, gere menos e **não invente**. Se não
houver nada novo, **pule a área sem criar arquivo**.

### 4. Escreva a nota — formato OBRIGATÓRIO
Nome do arquivo: `AAAA-MM-DD HHhMM — <Área> Digest.md` (data/hora em BRT, ex: `2026-06-30 06h05`).
Use o nome de exibição da área (IA, Saúde, Medicina do Trabalho, Mercado Financeiro,
Puerpério, Recém-Nascidos, Filmes e Séries, Jogos). Conteúdo:

```markdown
---
title: <Área> — Digest AAAA-MM-DD HHhMM
date: AAAA-MM-DD HHhMM
tags:
- <tag-da-área>
- digest
area: <Área>
source: claude code
---

# 🗞️ <Área> — Principais do dia (AAAA-MM-DD HHhMM)

## 1. <emoji> <título do tópico>

<resumo em pt-BR, 2–4 frases>

📅 Data da notícia: <DD/MM/AAAA> · [Fonte](<url-real>)

## 2. <emoji> <título>
...
```

Emoji por categoria do tópico:
`noticia 📰 · ferramenta 🛠️ · estudo 🔬 · analise 📊 · dado 📈 · review ⭐ ·
lancamento 🚀 · regulatorio ⚖️ · exercicio 🏃 · nutricao 🥗 · dica 💡 · curiosidade 🔍`.
Se não encaixar, use `📌`. Resumo SEMPRE em pt-BR (traduza fontes em inglês).
Todo tópico precisa de título, resumo e URL reais; descarte os incompletos.

### 5. Robustez
Se a busca/escrita de uma área falhar, registre o erro mentalmente e **siga para a próxima
área**. Nunca aborte o run inteiro por causa de uma área.

## Fechamento (uma vez só, depois das 8 áreas)
```bash
git add Pesquisas/
git pull --rebase origin main   # absorve edições manuais do Obsidian
git commit -m "auto: <AAAA-MM-DD HHhMM BRT> — digests do dia (<N> áreas)"
git push origin main
```
Se `git push` falhar por avanço do remoto, repita `git pull --rebase origin main` e
`git push` (até 4 tentativas).

## Relatório final (sua última mensagem)
Resuma: quantas áreas geraram nota, quais foram puladas (sem novidade) e quais falharam,
com 1 linha de motivo cada.
````

- [ ] **Step 2: Verificar o playbook contra o contrato do spec**

Conferir manualmente que o playbook contém: as 8 áreas na ordem certa, o bloco de
frontmatter com `source: claude code`, a tabela de emojis completa (12 categorias +
default), a regra de dedupe de 3 dias, o mínimo de 3 tópicos, o passo de `git pull --rebase`
antes do push, e o relatório final.

Run: `grep -c "Pesquisas/" .automation/digest-playbook.md`
Expected: ≥ 9 (8 áreas + git add).

- [ ] **Step 3: Commit**

```bash
git add .automation/digest-playbook.md
git commit -m "feat: playbook do agente para digests diários via Routine"
```

---

### Task 3: Desativar os crons do GitHub Actions (manter fallback)

**Files:**
- Modify: `.github/workflows/filmes-digest.yml`, `ia-digest.yml`, `jogos-digest.yml`, `medtrab-digest.yml`, `mercfin-digest.yml`, `puerperio-digest.yml`, `rn-digest.yml`, `saude-digest.yml`

**Interfaces:**
- Produces: 8 workflows sem agendamento automático, mas ainda disparáveis manualmente (`workflow_dispatch`) como fallback de emergência.

- [ ] **Step 1: Comentar o bloco `schedule:` em cada workflow**

Em cada um dos 8 arquivos, transformar:

```yaml
on:
  schedule:
    - cron: "7 5 * * *"  # 05:07 UTC / 02:07 BRT
  workflow_dispatch:
```

em (preservando o cron original de cada arquivo no comentário):

```yaml
on:
  # DESATIVADO 2026-06-30 — agendamento migrado para Routine do Claude Cloud.
  # Mantido como fallback manual via "Run workflow" (workflow_dispatch).
  # schedule:
  #   - cron: "7 5 * * *"  # 05:07 UTC / 02:07 BRT
  workflow_dispatch:
```

Repetir nos 8, mantendo o valor de cron específico de cada arquivo dentro do comentário.

- [ ] **Step 2: Verificar que nenhum schedule ficou ativo e que workflow_dispatch permaneceu**

Run: `grep -rL "workflow_dispatch" .github/workflows/` 
Expected: nenhuma saída (todos mantêm dispatch).

Run: `grep -rnE '^\s*schedule:' .github/workflows/`
Expected: nenhuma saída (todo `schedule:` está comentado).

- [ ] **Step 3: Commit**

```bash
git add .github/workflows/
git commit -m "chore: desativa crons do GitHub Actions (migrado p/ Routine do Claude)"
```

---

### Task 4: Push do legado desativado + provisionar a Routine

**Files:**
- Operacional (sem arquivo no repo). Usa a skill `schedule`.

**Interfaces:**
- Consumes: `.automation/digest-playbook.md` (Task 2), workflows desativados (Task 3).
- Produces: uma Routine ativa (cron `0 9 * * *` UTC) que dispara uma sessão cloud fresca por dia, vinculada ao repo `meu-vault` com push autorizado.

- [ ] **Step 1: Push das mudanças de Tasks 1–3**

```bash
git push origin main
```
Expected: push aceito. (A partir daqui o legado está desligado; a Routine assume.)

- [ ] **Step 2: Validar pré-requisitos do ambiente cloud**

Confirmar, via a skill `schedule` / Claude Code Remote: existe (ou pode ser criado) um
ambiente cloud com o repo `cassio-gon/meu-vault` clonado e **push autorizado** no `main`,
e com **firecrawl ou web search** disponível. Se firecrawl não existir, o playbook já cai
para web search nativa — sem mudança.
Expected: ambiente confirmado com repo + push + busca.

- [ ] **Step 3: Criar a Routine**

Usar a skill `schedule` para criar uma Routine que cria sessão nova a cada disparo, com:
- Cron: `0 9 * * *` (09:00 UTC = 06:00 BRT).
- Ambiente: o validado no Step 2 (repo `meu-vault`).
- Prompt (fino, aponta para o playbook versionado):

```
Você está numa sessão fresca com o repo meu-vault clonado. Leia
.automation/digest-playbook.md e execute-o integralmente para a data de hoje:
gere o digest das 8 áreas na ordem indicada e faça o commit+push único no fim.
Siga o formato de nota e as regras de dedupe exatamente como o playbook descreve.
```

Expected: Routine criada e listada como ativa, com `next_run_at` no próximo 09:00 UTC.

- [ ] **Step 4: Verificar a Routine**

Listar as Routines e confirmar nome, cron `0 9 * * *` e estado ativo.
Expected: a Routine aparece habilitada com o cron correto.

---

### Task 5: Disparo de validação e aceitação

**Files:**
- Operacional. Verifica o resultado real no repo `meu-vault`.

**Interfaces:**
- Consumes: a Routine (Task 4).

- [ ] **Step 1: Disparar a Routine manualmente uma vez**

Usar `fire_trigger` (ou "Run now" da skill `schedule`) para executar a Routine fora do
horário. Aguardar a sessão concluir.
Expected: a sessão roda as 8 áreas e termina com o relatório final.

- [ ] **Step 2: Verificar os arquivos gerados no repo**

No clone local (após `git pull origin main`):

Run: `git pull origin main && for a in IA Saude "Medicina do Trabalho" "Mercado Financeiro" Puerperio RN "Filmes e Series" Jogos; do n=$(ls -1 "Pesquisas/$a"/*Digest.md 2>/dev/null | wc -l); echo "$a: $n digests"; done`
Expected: cada área tem ao menos o digest de hoje (áreas sem novidade podem ter sido puladas — conferir no relatório final do Step 1).

- [ ] **Step 3: Verificar o formato de uma nota gerada**

Abrir o digest de hoje de `Pesquisas/IA/` e conferir contra o contrato:
- frontmatter com `source: claude code`, `area: IA`, tags `[ia, digest]`;
- título `# 🗞️ IA — Principais do dia (...)`;
- tópicos numerados com emoji, resumo em pt-BR, linha `📅 Data da notícia: ... · [Fonte](...)` com URL real.
Expected: bate com o contrato; nenhum campo placeholder.

- [ ] **Step 4: Verificar o push e a camada de leitura**

Run: `git log --oneline -1`
Expected: commit `auto: <data> — digests do dia (N áreas)` presente no `main` remoto.

Confirmar que o app de leitura (que lê do Obsidian/GitHub) mostra os novos digests
normalmente. Como repo/pastas/formato não mudaram, deve funcionar sem ajuste.

- [ ] **Step 5: Observação por alguns dias**

Deixar a Routine rodar no horário por ~7 dias. Critérios de sucesso (do spec):
1. As 8 áreas com digest novo antes das 07:00.
2. Zero falha por cron descartado e zero conflito de push.
3. Sem repetição perceptível de tópicos entre dias.
Se algo falhar, ajustar o playbook (Task 2) e/ou o horário da Routine.

---

## Self-Review (preenchido)

**Spec coverage:**
- Gatilho único 06:00 BRT → Task 4 (cron `0 9 * * *`).
- Claude faz curadoria, busca aberta → Task 2 (playbook, passo 2).
- Dedupe 3 dias → Task 2 (passo 1 e 3) + Global Constraints.
- Formato idêntico, `source: claude code` → Task 2 (passo 4) + Task 5 (passo 3).
- Sequencial + 1 push, sem concorrência → Task 2 (fechamento).
- Fontes curadas como dica → Task 1.
- Desativar Actions, manter fallback → Task 3.
- Camada de leitura preservada → Task 5 (passo 4) + Global Constraints.
- Robustez (falha de área não derruba run) → Task 2 (passo 5).

**Placeholder scan:** Os "(copiar as N URLs...)" da Task 1 são instruções de extração de
uma fonte exata e citada (`main.py:28-97`), não placeholders de design. Demais passos têm
conteúdo concreto.

**Type/nome consistency:** pastas, tags e nomes de exibição das áreas batem entre Global
Constraints, Task 1 e Task 2. Nome de arquivo `AAAA-MM-DD HHhMM — <Área> Digest.md`
consistente entre spec e playbook.

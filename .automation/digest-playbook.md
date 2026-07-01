# Playbook: Digests diários do Vault

Você é executado por uma Routine às 06:00 BRT. Objetivo: gerar o digest de hoje para
**cada área elegível hoje** (veja "Cadência por área"), em sequência, e fazer **um único**
commit+push no fim.
Trabalhe na raiz do repo `meu-vault` já clonado. NÃO altere nada fora de `Pesquisas/`.

## Ordem das áreas (faça nesta ordem)

O **Código** é o identificador curto que vai no filename, no `title:`, no `area:` do
frontmatter e no heading H1. A pasta e a tag permanecem como abaixo.

1. Código `IA` → pasta `Pesquisas/IA` → tag `ia`
2. Código `Saude` → pasta `Pesquisas/Saude` → tag `saude`
3. Código `MedTrab` → pasta `Pesquisas/Medicina do Trabalho` → tag `medtrab`
4. Código `MercFin` → pasta `Pesquisas/Mercado Financeiro` → tag `mercado-financeiro`
5. Código `Puerperio` → pasta `Pesquisas/Puerperio` → tag `puerperio`
6. Código `RN` → pasta `Pesquisas/RN` → tag `recem-nascidos`
7. Código `Filmes` → pasta `Pesquisas/Filmes e Series` → tag `filmes-series`
8. Código `Jogos` → pasta `Pesquisas/Jogos` → tag `jogos`

## Cadência por área

Por padrão todas as áreas rodam **todo dia**. Exceção (para conter custo):
- **Puerperio** e **RN** só rodam **segunda, quarta e sexta** (3×/semana). Nos demais dias
  (terça, quinta, sábado, domingo) **pule essas duas áreas** sem criar arquivo e sem contá-las
  como falha. Determine o dia da semana a partir da data de hoje em BRT antes de começar.

## Para cada área, faça:

### 1. Dedupe — leia o que já saiu
Liste os 3 arquivos `*Digest.md` mais recentes da pasta da área e leia seus títulos de
tópico. Guarde-os como "já publicado".

### 2. Busca do dia — use WebSearch como fonte principal (NUNCA firecrawl)
No ambiente da Routine, **WebSearch é a ferramenta principal e suficiente**: é ela que traz
os tópicos do dia (título, URL real e data) já nos próprios snippets. Use os sites de
`.automation/area-sources.md` como pista de temas/fontes a pesquisar (ex.:
`site:infomoney.com.br` na query). Priorize conteúdo datado e recente (HOJE ou últimas ~48h),
com URL real e verificável.

**Não use WebFetch por padrão.** A maioria dos grandes portais devolve **403 (anti-bot)**,
inclusive feeds RSS, e cada tentativa falha ainda queima tokens à toa. Extraia título, data e
resumo direto dos snippets do WebSearch. Só recorra ao WebFetch se a **data** de um tópico que
você realmente vai publicar estiver ambígua e não der pra resolver com outra busca — e, nesse
caso, **uma única tentativa**; se der 403, siga com o que o WebSearch trouxe, sem reprocessar.
**Não use firecrawl** (sem créditos).

### 3. Seleção
Escolha os ~5 tópicos mais relevantes. **Descarte** qualquer um cujo assunto já apareça
nos digests dos últimos 3 dias (passo 1), salvo se houver desdobramento claramente novo.
Mínimo 3 tópicos; se não houver material suficiente, gere menos e **não invente**. Se não
houver nada novo, **pule a área sem criar arquivo**.

### 4. Escreva a nota — formato OBRIGATÓRIO
Use o **Código** da área (IA, Saude, MedTrab, MercFin, Puerperio, RN, Filmes, Jogos) —
NÃO o nome de exibição completo — em todos os campos abaixo. O app de leitura depende
desse identificador curto para indexar e filtrar as notas.

Nome do arquivo: `AAAA-MM-DD HHhMM — <Código> Digest.md`
(data/hora em BRT, ex: `2026-06-30 06h05 — MedTrab Digest.md`).

Conteúdo:

```markdown
---
title: <Código> — Digest AAAA-MM-DD HHhMM
date: AAAA-MM-DD HHhMM
tags:
- <tag-da-área>
- digest
area: <Código>
source: claude code
---

# 🗞️ <Código> — Principais do dia (AAAA-MM-DD HHhMM)

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
git commit -m "auto: <AAAA-MM-DD HHhMM BRT> — digests do dia (<N> áreas)"
git pull --rebase origin main   # absorve edições manuais do Obsidian
git push origin main
```
O commit é feito **antes** do rebase para evitar que mudanças staged não-commitadas
abortem o rebase. Se `git push` falhar por avanço do remoto, repita apenas
`git pull --rebase origin main` e `git push` (até 4 tentativas; o commit já foi feito).

## Relatório final (sua última mensagem)
Resuma: quantas áreas geraram nota, quais foram puladas (sem novidade) e quais falharam,
com 1 linha de motivo cada.

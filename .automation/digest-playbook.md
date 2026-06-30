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

# Migração dos digests do Vault para Routine do Claude Cloud

**Data:** 2026-06-30
**Repo afetado:** `cassio-gon/meu-vault` (local em `~/.claude/vault`)
**Abordagem escolhida:** B — Claude faz a curadoria (reescrita), agendado via Routine na nuvem.

## Problema

Hoje 8 workflows do GitHub Actions (`.github/workflows/*-digest.yml`), um por área,
rodam em cron escalonado (02:07–02:42 BRT) o pipeline Python em `.automation/`
(coleta RSS/Firecrawl → resumo no Gemini → 1 nota .md → commit/push). O Obsidian puxa
o repo e o usuário lê os digests às 07:00.

Duas causas de falha, ambas registradas no histórico de commits:

1. **GitHub derruba crons agendados.** Workflow agendado no GitHub é *best-effort*:
   atrasa ou é descartado sob carga, e é desativado após 60 dias de inatividade.
   Tentativas anteriores ("crons em minutos não-redondos") não resolveram.
2. **Conflito de push entre runs concorrentes.** As 8 áreas disparam quase juntas e
   brigam pelo mesmo push; daí o `git_sync` ter ganhado `pull --rebase + retry`.

## Objetivo

Substituir o agendamento e a geração por uma **única Routine do Claude Cloud** que roda
de manhã, gera os digests das 8 áreas em sequência e dá um push só — eliminando as duas
causas de falha — mantendo o **formato de nota idêntico** ao atual.

## Decisões (confirmadas com o usuário)

| Tema | Decisão |
|---|---|
| Quem gera | Claude faz a curadoria (sem Gemini, sem código Python de coleta) |
| Agendamento | **1 Routine**, cron diário **06:00 BRT** (09:00 UTC), todas as áreas em sequência |
| Fontes | **Busca aberta por tema**; a lista curada de `DIGEST_SOURCES` entra só como dica |
| GitHub Actions atual | **Desativar** os 8 workflows, **manter os arquivos** no repo como fallback |
| Dedupe | Evitar repetir tópicos já presentes nos digests dos últimos ~3 dias da área |
| Formato da nota | **Idêntico** ao atual (ver "Contrato de saída") |

## Arquitetura alvo

```
Routine (cron 06:00 BRT, sessão cloud fresca, repo meu-vault clonado)
  └─ para cada área em ORDEM (IA, Saúde, MedTrab, MercFin, Puerpério, RN, Filmes, Jogos):
       1. Busca aberta do dia por tema (web/firecrawl), usando fontes curadas como dica
       2. Seleciona ~5 tópicos mais relevantes do dia
       3. Deduplica contra os digests dos últimos ~3 dias daquela pasta
       4. Resume cada tópico em pt-BR
       5. Escreve a nota no formato-contrato em Pesquisas/<Área>/
  └─ git add . && commit "auto: <data> — digests do dia (N áreas)" && push origin main
Obsidian no Mac puxa o repo → digests prontos antes das 07:00
```

### Áreas e pastas de destino (mantidas)

| Área | Pasta | Tag |
|---|---|---|
| IA | `Pesquisas/IA` | `ia` |
| Saúde | `Pesquisas/Saude` | `saude` |
| Medicina do Trabalho | `Pesquisas/Medicina do Trabalho` | `medtrab` |
| Mercado Financeiro | `Pesquisas/Mercado Financeiro` | `mercado-financeiro` |
| Puerpério | `Pesquisas/Puerperio` | `puerperio` |
| Recém-Nascidos | `Pesquisas/RN` | `recem-nascidos` |
| Filmes e Séries | `Pesquisas/Filmes e Series` | `filmes-series` |
| Jogos | `Pesquisas/Jogos` | `jogos` |

As fontes curadas por área (RSS + sites de Med. Trabalho) permanecem documentadas como
**dica de busca** para o agente — extraídas de `.automation/main.py` (`DIGEST_SOURCES`).

## Camada de leitura (app consumidor) — preservada

O usuário lê os digests por um **app que consome do Obsidian/GitHub**. Essa camada é
**mantida sem alteração**: a migração preserva o *contrato de saída* — mesmo repo
(`meu-vault`), mesmas pastas (`Pesquisas/<Área>/`), mesmo nome de arquivo e mesmo
formato de nota. O app continua puxando os mesmos `.md` do mesmo lugar; nada nele muda.

**Identificador de área:** o app filtra/indexa notas pelo campo `area:` e pelo filename.
Ambos devem conter o **Código histórico curto** (IA, Saude, MedTrab, MercFin, Puerperio,
RN, Filmes, Jogos), não o nome de exibição — esse contrato não pode ser quebrado.

Única diferença cosmética: o campo `source:` no frontmatter passa de
`trafilatura+groq` para `claude code` (decisão do usuário).

## Contrato de saída (formato da nota — rígido)

> **Identificador de área:** em filename, `title:`, `area:` e heading H1 usa-se o
> **Código histórico curto** — IA, Saude, MedTrab, MercFin, Puerperio, RN, Filmes, Jogos
> — NÃO o nome de exibição completo (ex: "Medicina do Trabalho", "Filmes e Séries").
> O app de leitura depende desse código para indexar e filtrar as notas.

Nome do arquivo: `AAAA-MM-DD HHhMM — <Código> Digest.md` (timestamp em BRT).
Exemplos reais do histórico: `2026-06-26 07h28 — MedTrab Digest.md`, `… — MercFin Digest.md`.
Conteúdo:

```markdown
---
title: <Código> — Digest AAAA-MM-DD HHhMM
date: AAAA-MM-DD HHhMM
tags:
- <tag>
- digest
area: <Código>
source: claude code
---

# 🗞️ <Código> — Principais do dia (AAAA-MM-DD HHhMM)

## 1. <emoji> <título do tópico>

<resumo em pt-BR, 2–4 frases>

📅 Data da notícia: <DD/MM/AAAA> · [Fonte](<url>)

## 2. ...
```

Emoji por categoria (mesma tabela do `formatter.py`): `noticia 📰 · ferramenta 🛠️ ·
estudo 🔬 · analise 📊 · dado 📈 · review ⭐ · lancamento 🚀 · regulatorio ⚖️ ·
exercicio 🏃 · nutricao 🥗 · dica 💡 · curiosidade 🔍` (default `📌`).

Regras de qualidade:
- ~5 tópicos por área (mínimo 3; se não houver material, não inventar — escrever menos).
- Cada tópico precisa de `título`, `resumo` e `url` reais; descartar incompletos.
- Resumo sempre em pt-BR, mesmo de fonte em inglês.
- `source: claude code` (substitui `trafilatura+groq`, que era impreciso).

## Robustez e modos de falha

- **Falha de uma área não derruba as outras:** erro ao coletar/resumir uma área é
  logado e o agente segue para a próxima; commit no fim inclui o que deu certo.
- **Sem novidade:** se uma área não tem tópicos novos do dia, pular sem criar nota vazia.
- **Push:** sequencial e único no fim → sem concorrência. `git pull --rebase` antes do
  push para absorver qualquer commit externo (ex.: edições manuais do Obsidian).
- **Observabilidade:** a mensagem final da Routine resume quantas áreas geraram nota e
  quais falharam, para o usuário ver no histórico da Routine.

## Pré-requisitos do ambiente cloud (validar ao montar)

1. Repo `cassio-gon/meu-vault` clonado na sessão da Routine com **push autorizado** (token/credencial de escrita no `main`).
2. **firecrawl** disponível na sessão; se não, **fallback para web search nativa**.
3. Fuso: agente calcula timestamps em **BRT (UTC-3)** independente do fuso do runner.

## Desativação do legado (sem remover)

- Em cada `.github/workflows/*-digest.yml`: **comentar o bloco `schedule:`** (manter
  `workflow_dispatch` para disparo manual de emergência). Arquivos e `.automation/`
  permanecem no repo como fallback e referência.
- Nada do Python é deletado nesta migração.

## Fora de escopo (YAGNI)

- Reescrever/limpar o código Python de `.automation/` (fica como fallback).
- Mudar a estrutura de pastas do vault ou o fluxo de leitura no Obsidian.
- Notificações externas (push/email) além do resumo no histórico da Routine.
- Migrar qualquer coisa do projeto "Secretaria IA" (n8n) — não faz parte deste fluxo.

## Critérios de sucesso

1. Por ~7 dias seguidos, todas as 8 áreas têm digest novo no vault **antes das 07:00**.
2. Zero falha por cron descartado e zero conflito de push.
3. Notas no formato-contrato, sem repetição perceptível de tópicos entre dias.

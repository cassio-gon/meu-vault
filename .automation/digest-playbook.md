# Playbook: Digests diários do Vault

Você é executado por uma Routine às 06:00 BRT. Objetivo: gerar o digest de hoje para
**cada uma das 6 áreas**, em sequência, e fazer **um único** commit+push no fim.
Trabalhe na raiz do repo `meu-vault` já clonado. NÃO altere nada fora de `Pesquisas/`.

## Ordem das áreas (faça nesta ordem)

O **Código** é o identificador curto que vai no filename, no `title:`, no `area:` do
frontmatter e no heading H1. A pasta e a tag permanecem como abaixo.

1. Código `IA` → pasta `Pesquisas/IA` → tag `ia`
2. Código `Saude` → pasta `Pesquisas/Saude` → tag `saude`
3. Código `MedTrab` → pasta `Pesquisas/Medicina do Trabalho` → tag `medtrab`
4. Código `MercFin` → pasta `Pesquisas/Mercado Financeiro` → tag `mercado-financeiro`
5. Código `Filmes` → pasta `Pesquisas/Filmes e Series` → tag `filmes-series`
6. Código `Jogos` → pasta `Pesquisas/Jogos` → tag `jogos`

## Cadência

As 6 áreas rodam **todo dia**. Não há exceção de dia da semana.

**Áreas desativadas (2026-08-29): `Puerperio` e `RN`.** NÃO gere digest para elas em
nenhum dia, NÃO crie arquivo em `Pesquisas/Puerperio` nem em `Pesquisas/RN` e NÃO as
conte como falha. As pastas `Pesquisas/Puerperio` e `Pesquisas/RN` foram **removidas**
do repo em 2026-08-29 — não as recrie.

## Para cada área, faça:

**Uma área por vez, do começo ao fim.** Para cada área: colete as páginas dela, escolha os
tópicos, colete as matérias e **grave o arquivo da área (Write) antes de começar a
próxima**. Não colete as 6 áreas de uma vez. Em 19/10/2026 isso estourou o contexto, a
compactação guardou só os domínios e 25 de 29 links saíram como `https://deadline.com`.
**Não abra subagente** (Agent/Task) e **não use `maxChars` acima do indicado** aqui.

### 1. Dedupe — leia o que já saiu
Liste os 3 arquivos `*Digest.md` mais recentes da pasta da área e leia seus títulos de
tópico. Guarde-os como "já publicado".

### 2. Busca do dia — coleta das páginas de seção pelo agente web
`.automation/area-sources.md` define **5 sites âncora por área**, cada um com a **URL da
página de seção** (ou do feed RSS) e o modo de acesso. Eles são o piso de qualidade.

**Ferramenta principal: `web_scrape` do conector `agente-web`** (Firecrawl próprio do
Cássio, custo zero). A página de seção traz a lista do dia com o link real de cada matéria,
a hora ("há 3 horas", "19/10/26") e a foto de cada card. Chame SEMPRE com
`fallback: false` (não gasta a cota paga de reserva) e `maxChars: 4000`. Âncora marcado
com `waitFor` no area-sources: passe esse valor também.

Faça, nesta ordem:
1. **Uma coleta por âncora de modo `coleta`** — `web_scrape` na URL de seção. Anote as
   matérias com data de hoje ou das últimas ~48h: título, URL da matéria e a URL da foto do
   mesmo card (regras em "Foto do tópico", seção 4). Se a coleta falhar, siga para o
   próximo âncora; não repita.
2. **Uma busca `site:` no WebSearch por âncora de modo `busca`** (sites que bloqueiam o
   coletor; hoje só os 3 de MedTrab: gov.br, conjur.com.br e tst.jus.br).
3. **Uma busca aberta no WebSearch** do tema da área, para não perder o furo que nasceu
   fora da lista.
4. **Depois de escolher os tópicos (seção 3, Seleção), uma coleta da própria matéria** de cada
   tópico: `web_scrape` com `fallback: false` e `maxChars: 2000`. É dela que saem o resumo,
   a data confirmada e, se o card não trouxe, a foto. Paywall ou falha: siga com o que a
   página de seção mostrou.

**Se o conector `agente-web` não existir na sessão ou TODAS as coletas da área falharem**
(VPS fora do ar), volte ao modo antigo só nessa área: uma busca `site:` no WebSearch por
âncora (use o domínio do âncora) + a busca aberta, sem imagens. Diga no relatório final.

**Regras das buscas no WebSearch (obrigatórias — o `site:` quebra fácil):**
- **Domínio nu, sem caminho.** `site:g1.globo.com saúde` funciona; `site:g1.globo.com/saude`
  devolve lixo. Para chegar numa seção, use as palavras do tema, não o caminho da URL.
- **NUNCA ponha data na query.** "agosto 2026", "29 de agosto", "August 29 2026" puxam
  página de retrospectiva e artigo velho. O WebSearch já prioriza o recente; a data você
  **lê no snippet**, não pede na busca.
- Se uma busca `site:` voltar resultado claramente fora do domínio pedido (Wikipédia,
  agregador), descarte-a e siga — não insista com variações da mesma query.

Prefira o que veio dos 5 âncoras. Material de outra fonte só entra se for **claramente
relevante, datado e de veículo confiável** — nunca blog agregador, nunca site que só
republica release. Priorize conteúdo de HOJE ou das últimas ~48h, com URL real e
verificável.

**Não use WebFetch.** Os grandes portais devolvem **403 (anti-bot)** e cada tentativa queima
tokens à toa; o `web_scrape` do `agente-web` faz esse papel. **Não use o conector `firecrawl`**
(o da Firecrawl cloud, sem créditos) — o `agente-web` é outro serviço, esse pode.

### 3. Seleção
Escolha os ~5 tópicos mais relevantes. **Descarte** qualquer um cujo assunto já apareça
nos digests dos últimos 3 dias (passo 1), salvo se houver desdobramento claramente novo.
Mínimo 3 tópicos; se não houver material suficiente, gere menos e **não invente**. Se não
houver nada novo, **pule a área sem criar arquivo**.

### 4. Escreva a nota — formato OBRIGATÓRIO
Use o **Código** da área (IA, Saude, MedTrab, MercFin, Filmes, Jogos) —
NÃO o nome de exibição completo — em todos os campos abaixo. O app de leitura depende
desse identificador curto para indexar e filtrar as notas.

Nome do arquivo: `AAAA-MM-DD HHhMM — <Código> Digest.md`
(data/hora em BRT, ex: `2026-06-30 06h05 — MedTrab Digest.md`).

Conteúdo (Obsidian Flavored Markdown — **cada tópico é um callout**):

```markdown
---
title: <Código> — Digest AAAA-MM-DD HHhMM
date: AAAA-MM-DD HHhMM
tags:
  - <tag-da-área>
  - digest
area: <Código>
source: routine
---

# 🗞️ <Código> — Principais do dia (AAAA-MM-DD HHhMM)

> [!tldr] Resumo do dia
> <1 frase em pt-BR resumindo o panorama do dia nesta área>

> [!<tipo>] <emoji> <título do tópico 1>
> <img src="<url-da-foto>" alt="" loading="lazy" referrerpolicy="no-referrer">
>
> <resumo em pt-BR, 2–4 frases>
>
> 📅 <DD/MM/AAAA> · [Fonte](<url-real>)

> [!<tipo>] <emoji> <título do tópico 2 (sem foto válida: sem a linha img)>
> <resumo em pt-BR, 2–4 frases>
>
> 📅 <DD/MM/AAAA> · [Fonte](<url-real>)

---

> [!note]- ℹ️ Sobre
> Área: [[<Código>]] · digest automático da Routine.
```

**Regras de formatação do callout (obrigatório):**
- O digest abre com **um** callout `> [!tldr]` de 1 frase (resumo do dia).
- **Cada tópico é um callout** `> [!<tipo>] <emoji> <título>`. TODA linha do tópico
  (foto, resumo, data, fonte) começa com `> `. Separe o resumo da linha da data com **uma linha
  `>` vazia** (senão viram um parágrafo só).
- O `<tipo>` do callout vem da categoria do tópico (a cor/ícone no leitor derivam dele):

  | Categoria | emoji | `<tipo>` |
  |---|---|---|
  | notícia | 📰 | `info` |
  | ferramenta | 🛠️ | `tip` |
  | estudo | 🔬 | `abstract` |
  | análise | 📊 | `note` |
  | dado | 📈 | `example` |
  | review | ⭐ | `quote` |
  | lançamento | 🚀 | `success` |
  | regulatório | ⚖️ | `warning` |
  | exercício | 🏃 | `todo` |
  | nutrição | 🥗 | `success` |
  | dica | 💡 | `tip` |
  | curiosidade | 🔍 | `question` |

  Se não encaixar, use `> [!note] 📌 <título>`.
- Termine com o callout de rodapé `> [!note]- ℹ️ Sobre` contendo `[[<Código>]]` — esse
  wikilink conecta os digests da área no grafo do Obsidian. Mantenha exatamente esse formato.

**Foto do tópico (opcional, nunca inventada):**
- Use a foto que veio **na coleta**: a imagem do mesmo card da matéria na página de seção
  (o `![...](url)` colado ao link dessa matéria) ou, se o card não tinha, a primeira foto do
  conteúdo da matéria coletada no passo 4 da busca.
- Descarte, e siga sem foto: `.svg`, `.gif`, pixel de rastreio (`pixel.`, `analytics`,
  `sync`), `<Base64-Image-Removed>`, logo, ícone, foto de autor (`autor`, `50x50`), URL
  que não começa com `https://`, URL igual à da própria página, e URL com aspas ou espaço.
- Nunca use foto de outra matéria, banco de imagens, Openverse ou placeholder. Tópico de
  feed RSS ou do WebSearch sem foto na coleta da matéria fica sem foto — tudo bem.
- A linha `<img>` vai logo abaixo do título, seguida de uma linha `>` vazia, exatamente
  assim: `> <img src="<url>" alt="" loading="lazy" referrerpolicy="no-referrer">`. Nunca
  `![](url)` e nunca a foto depois do resumo.

Resumo SEMPRE em pt-BR (traduza fontes em inglês). Todo tópico precisa de título, resumo e
URL reais; descarte os incompletos.

**O link `[Fonte](...)` é a URL exata da matéria**, copiada do resultado do `web_scrape`
(ou do WebSearch): nunca só o domínio (`https://deadline.com`), nunca a página de seção e
nunca um domínio deduzido. Se você não tem mais a URL exata, descarte o tópico.

### 5. Robustez
Se a busca/escrita de uma área falhar, registre o erro mentalmente e **siga para a próxima
área**. Nunca aborte o run inteiro por causa de uma área.

## Fechamento (uma vez só, depois das 6 áreas)

⚠️ **Você provavelmente está em `detached HEAD` — isso é NORMAL no ambiente da Routine e
não significa que exista trabalho por enviar.** NÃO tente consertar o branch local: nada de
`git checkout main`, `git stash`, `git reset --hard` ou `git merge`. Isso já causou conflito
e retrabalho (29/08/2026). Só faça commit e empurre com `HEAD:main`.

```bash
git add Pesquisas/
git commit -m "auto: <AAAA-MM-DD HHhMM BRT> — digests do dia (<N> áreas)"
git pull --rebase origin main   # absorve edições manuais do Obsidian
git push origin HEAD:main       # HEAD:main funciona mesmo em detached HEAD
```
O commit é feito **antes** do rebase para evitar que mudanças staged não-commitadas
abortem o rebase. Se `git push` falhar por avanço do remoto, repita apenas
`git pull --rebase origin main` e `git push` (até 4 tentativas; o commit já foi feito).

## Relatório final (sua última mensagem)
Resuma: quantas áreas geraram nota, quais foram puladas (sem novidade) e quais falharam,
com 1 linha de motivo cada.

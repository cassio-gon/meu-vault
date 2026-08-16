# Acervo de conhecimento — design

**Data:** 2026-08-16
**Repo:** `meu-vault` (local: `~/.claude/vault`)
**Workstation:** `~/.claude/workstations/obsidian-noticias/`

## Problema

Hoje existem dois fluxos de conhecimento que não se falam:

1. Os **digests diários** da Routine na nuvem — 419 notas em `Pesquisas/`
   (93 de junho, 219 de julho, 107 de agosto de 2026), uma por área por dia.
2. As **pesquisas do `/last30days`** — 16 arquivos brutos (868 KB) em
   `~/Documents/Last30Days`, fora do vault, sem frontmatter e sem tags.

Nenhum dos dois acumula. O digest de hoje não sabe o que o digest de ontem
disse; a pesquisa de agosto não sabe que houve uma sobre o mesmo tema em junho.
O objetivo é transformar isso num acervo que **aprende ao longo do tempo**, como
uma mente: consolida o que se repete, registra o que mudou, e revela conexões
que ninguém pediu.

## Objetivos

- Toda pesquisa `/last30days` fica registrada e reaproveitável.
- Os digests diários alimentam o mesmo acervo, não um silo paralelo.
- O acervo **consolida** (não só empilha) os temas que importam.
- Conexões entre áreas diferentes ficam visíveis sem alguém perguntar.
- Sobrevive às ferramentas: legível em cinco anos, no celular, sem nada instalado.

## Não-objetivos

- Não é um sistema de busca para o Claude consultar antes de agir (foi
  explicitamente descartado na fase de brainstorming).
- Não consolida retroativamente os 419 digests em notas vivas — só o grafo
  recebe o histórico completo.
- Não substitui nem altera o formato dos digests diários existentes.

## Decisões tomadas

| Decisão | Escolha | Alternativa recusada |
|---|---|---|
| Fonte da verdade | Markdown em git | SQLite (`store.py` da skill); grafo como acervo |
| Modelo de aprendizado | Híbrido em duas camadas | Append-only puro; consolidação de tudo |
| Motor da consolidação | Routine na nuvem (6h) | Mac; sob demanda |
| Motor do grafo | Mac, LaunchAgent | Routine na nuvem |
| Promoção de tema | Rodar `/last30days` promove | Lista manual; tag; recorrência automática |
| Saída do grafo | Fora do vault, no painel agêntico | `--obsidian` escrevendo no vault |

O markdown venceu o SQLite porque o banco é local e binário: a Routine na nuvem
não o alcança, e ele só conhece as pesquisas do `/last30days` — os 419 digests
ficariam de fora, criando dois acervos em vez de um. Do SQLite foi aproveitada
uma ideia só: **dedupe por URL**.

O grafo não é o acervo porque ele precisa ser **descartável**. Se o graphify
sumir, nenhuma informação se perde.

## Arquitetura

```
meu-vault/
├── Pesquisas/                  CAMADA 1 — diário imutável (existe, 419 notas)
│   ├── IA/ Saude/ ...          digests da Routine, um por dia por área
│   └── _pesquisas/             NOVO — notas datadas do /last30days
├── Acervo/                     NOVO — CAMADA 2, notas vivas (~13 no início)
│   └── Prontuário Eletrônico com IA.md, NR-1.md, Amplimed.md ...
└── .automation/
    ├── digest-playbook.md      existe
    ├── area-sources.md         existe
    └── acervo-playbook.md      NOVO — regras da consolidação

~/.local/share/acervo-grafo/    FORA do vault, descartável, não versionado
└── graphify-out/{graph.json, index.html, GRAPH_REPORT.md}
```

### Três fluxos independentes

**1. Pesquisa** — disparada por você, ao rodar `/last30days <tema>`:
salva o raw como hoje; escreve a nota datada em `Pesquisas/_pesquisas/`;
cria ou atualiza a nota viva do tema em `Acervo/`; termina em `commit` + `push`.

*Mecanismo (a fechar no plano):* a skill `last30days` é de terceiro e versionada
(v3.8.3, com auto-update) — **não editar seus arquivos**, a mudança se perde na
próxima atualização. Opção recomendada: um comando `/acervo` **idempotente** que
varre `~/Documents/Last30Days`, ignora os raws que já viraram nota e ingere os
pendentes. Assim o mesmo comando serve para o backfill dos 13 temas e para o uso
contínuo, e esquecer de rodar num dia não perde nada — a próxima execução pega o
atraso. Os raws continuam onde estão: são dumps ruidosos, ruins para o grafo e
grandes demais para engordar o git do vault.

**2. Digest diário** — Routine na nuvem, 06:00 BRT, ao final do trabalho atual:
lista os nomes dos arquivos em `Acervo/`; identifica quais temas as notícias do
dia tocaram; lê e edita **apenas** essas notas. Nenhum tema tocado, nenhuma
reescrita, nenhum custo.

**3. Grafo** — LaunchAgent no Mac, 1×/dia: `graphify --update` sobre o vault,
saída em `~/.local/share/acervo-grafo/`, servida pelo painel agêntico
(`~/.claude/painel-agentico`, `localhost:4747`).

**Independência é requisito, não consequência.** Se o graphify quebrar, nenhuma
nota se perde. Se a Routine falhar num dia, o diário fica com um buraco de um dia
e as notas vivas seguem válidas. Se `/last30days` nunca mais rodar, os outros dois
continuam. Nada é ponto único de falha.

## Formato da nota viva

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
- Amplimed e iClinic acumulam reclamação de lentidão. [[2026-08-10 — Pesquisa: Amplimed]]

## Como isso mudou
- 2026-06-28 — primeira leitura do tema, mercado dominado por teclado.
- 2026-08-13 — ditado por voz virou pauta recorrente; três produtos novos no mês.

## Em aberto
- Ninguém mediu adesão real depois de 90 dias.

## Origens
[[2026-08-13 — Pesquisa: ditado por voz]] · [[2026-08-10 12h00 — IA Digest]]
```

Nome do arquivo: o próprio tema em linguagem natural, para o wikilink do Obsidian
funcionar sem alias.

### As cinco regras anti-degradação

Sem elas a nota viva vira telefone sem fio: cada reescrita perde detalhe da
anterior até a nota afirmar coisas que ninguém disse.

1. **`Como isso mudou` é append-only.** A IA só acrescenta linha no fim. Nunca
   reescreve, nunca "enxuga" o histórico. Se a síntese do topo degradar, o log
   embaixo preserva a trajetória.

2. **Todo fato carrega âncora.** Cada bullet de `O que sabemos hoje` termina num
   wikilink para a nota de origem no diário. Afirmação sem âncora é afirmação
   inventada e pode ser removida sem perda. Mesmo princípio anti-alucinação do
   Calima: a IA preenche slots, não inventa conteúdo.

3. **Reescrita é edição cirúrgica, não regeneração.** A Routine recebe a nota
   atual mais as notícias do dia e faz `Edit` pontual. Ela **nunca** recebe
   "reescreva esta nota do zero" — o texto antigo não volta a passar pelo modelo
   a cada dia, então não tem como ir se deformando.

4. **A nota viva nunca é a única cópia.** O digest e o raw ficam intactos. O pior
   caso de uma reescrita ruim é perder uma síntese, nunca um fato. Cada reescrita
   é um commit: `git log -p Acervo/` é o botão de desfazer.

5. **Teto de 15 bullets em `O que sabemos hoje`.** Ao estourar, o mais antigo
   desce para o log. Mente que aprende também descarta — sem teto, cada nota viva
   vira em seis meses um documento tão longo quanto o problema que veio resolver.

### Dedupe por URL

A Routine lê a nota antes de editar e vê as fontes já registradas nela. Mesma URL
vista de novo não vira fato novo — vira, no máximo, uma linha no log dizendo que
o assunto voltou. Sem banco, sem índice, sem infra nova.

### Datas não se disfarçam

Nota viva nascida de pesquisa de junho descreve o mundo de junho. O frontmatter
marca `atualizado: 2026-06-28` sem maquiagem. Sem isso, daqui a seis meses uma
afirmação velha é lida como atual — a diferença entre memória e desinformação.

## Backfill do histórico

**Grafo: entra tudo.** As 419 notas de `Pesquisas/` numa extração inicial única;
depois só `--update` incremental. É aqui que "ver conexões que eu não pedi" ganha
massa: começando do zero, o grafo ficaria mudo por meses.

**Camada 2: seletivo, e o recorte já existe.** Pela regra "pesquisar promove o
tema", os 16 arquivos de `~/Documents/Last30Days` (28/06 a 13/08/2026) já são a
lista de temas declarados, com o dump de evidência salvo. Deles saem **~13 temas
distintos** — os três `reclama-es-amplimed-iclinic` (v3/v4x/v5x) são a mesma
pesquisa refeita, e `plantao-medico-raw-creators` / `plantao-raw-ig` são recortes
por fonte do mesmo assunto. Consolidação dos 419 digests em notas vivas **não é
feita**: notícia de junho tem valor histórico baixo e a varredura custa caro.

## Custo

| Fluxo | Custo | Confiança |
|---|---|---|
| Escrita na pesquisa | marginal (2 arquivos a mais) | alta |
| Consolidação diária | 0–3 notas lidas/editadas em dia típico | alta |
| Grafo, 1ª rodada | **desconhecido** | nenhuma |
| Grafo, `--update` | ~5–8 notas/dia | média |

O graphify usa LLM na extração, não está instalado e 419 notas é a maior rodada
que esse acervo terá. **Medir antes de gastar:** primeira execução restrita a
`Pesquisas/IA` (~60 notas), medindo tempo e consumo; só depois soltar nas 419. Se
o número assustar, abandonar o grafo não custa nada — ele é a peça descartável.

## Modos de falha

**Routine falha ou morre no meio.** A consolidação é a **última** etapa, depois do
commit dos digests. Se estourar antes, os digests já estão salvos e as notas vivas
ficam um dia velhas; o `atualizado` do frontmatter denuncia sozinho e o dia
seguinte recupera. Nenhuma ação manual.

**Graphify quebra.** Nada se perde. Apagar a pasta e reconstruir.

**Mac desligado.** Mesmo padrão do `vault-pull` já em produção: `RunAtLoad` mais
intervalo. O grafo fica velho, e só.

**⚠️ As duas fontes de instrução.** Registrado no `CLAUDE.md` do obsidian-noticias
como bug real (02/07/2026: as imagens voltaram porque a regra vivia em dois
lugares e só um foi limpo). As regras da camada 2 precisam entrar no
`acervo-playbook.md` **e** no prompt da Routine na nuvem. Mudança em um sem o
outro reintroduz exatamente aquele bug.

**Nota viva que não foi pushada.** A Routine roda na nuvem e **clona** o repo. Se
uma nota viva nova ficar só no disco local, a Routine não sabe que o tema existe e
nunca o alimenta. Por isso o passo da pesquisa termina obrigatoriamente em
`commit` + `push`.

## Verificação

`acervo-check.sh` — sem framework, roda em segundos, valida quatro invariantes:

1. Toda nota viva tem `atualizado` no frontmatter.
2. Todo bullet de `O que sabemos hoje` termina em wikilink.
3. Nenhuma nota passou de 15 bullets.
4. Todo wikilink aponta para arquivo existente.

É o que pega a degradação silenciosa — o único modo de falha deste sistema que não
grita sozinho.

## O que muda em cada lugar

| Arquivo / recurso | Mudança |
|---|---|
| `Pesquisas/_pesquisas/` | criar (pasta) |
| `Acervo/` | criar (pasta) + ~13 notas vivas do backfill |
| `.automation/acervo-playbook.md` | criar |
| Prompt da Routine `trig_018SJ1Au6eYbRA1YAJjk8dgU` | acrescentar etapa final de consolidação |
| Comando `/acervo` | criar — ingestão idempotente dos raws (a skill `last30days` **não** é modificada) |
| LaunchAgent do graphify | criar |
| `acervo-check.sh` | criar |
| `~/.claude/workstations/obsidian-noticias/` | documentar o acervo no `CLAUDE.md` e `MEMORY.md` |

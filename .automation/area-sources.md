# Fontes curadas por área — 5 sites fixos por área

> **Atualizado em 2026-08-29.** As áreas **Puerperio** e **RN** foram desativadas e
> as pastas `Pesquisas/Puerperio` e `Pesquisas/RN` foram **removidas** do repo. As 73
> notas antigas continuam recuperáveis pelo histórico do git (commit anterior a este).
>
> Cada área tem **5 sites âncora**, escolhidos por dois critérios verificados em
> 2026-08-29 com busca datada: (1) publicam conteúdo **recente** (últimos ~7 dias)
> e (2) são **indexáveis** — aparecem em busca com `site:`, que é como a Routine
> os alcança (os portais bloqueiam WebFetch com 403).
>
> **Como usar:** a Routine faz UMA busca `site:` por site âncora + UMA busca aberta
> do tema da área. Os 5 sites são o piso de qualidade, **não um teto**: se a busca
> aberta trouxer algo relevante de outra fonte confiável e datada, pode entrar.
>
> **Duas regras de query, aprendidas no run de teste de 29/08/2026 — o `site:` do
> WebSearch é frágil e quebra fácil:**
> 1. **Domínio nu, sem caminho.** `site:g1.globo.com saúde` funciona;
>    `site:g1.globo.com/saude` devolve lixo (Wikipédia, agregador aleatório).
> 2. **Nunca ponha data na query.** "agosto 2026" ou "August 29 2026" puxa página de
>    retrospectiva e artigo velho. O WebSearch já prioriza o recente sozinho — a data
>    você lê no snippet, não pede na busca.

## IA — pasta `Pesquisas/IA` — tag `ia`
1. `techcrunch.com` — notícia diária de IA/startups (categoria artificial-intelligence)
2. `technologyreview.com` — MIT Tech Review: análise e contexto, menos hype
3. `arstechnica.com` — apuração técnica profunda (seção /ai)
4. `olhardigital.com.br` — editoria de IA em pt-BR, publica todo dia
5. `tecnoblog.net` — pt-BR, boa cobertura de produto e do mercado brasileiro

## Saúde — pasta `Pesquisas/Saude` — tag `saude`
1. `g1.globo.com` — maior volume de saúde em pt-BR, sempre datado (seção /saude)
2. `veja.abril.com.br` — pauta clínica e de medicamentos (Anvisa, FDA); seção /saude
3. `agenciabrasil.ebc.com.br` — fonte pública, SUS e Ministério da Saúde
4. `folha.uol.com.br` — saúde e ciência com apuração própria (caderno Equilíbrio e Saúde)
5. `sciencedaily.com` (seção health_medicine) — estudos originais; traduzir para pt-BR

## Medicina do Trabalho — pasta `Pesquisas/Medicina do Trabalho` — tag `medtrab`
1. `protecao.com.br` — Revista Proteção: a fonte mais ativa de SST no Brasil
2. `gov.br` — MTE: NRs, portarias, eSocial, fiscalização (some os termos "NR", "Ministério do Trabalho" à query para cair no /trabalho-e-emprego)
3. `conjur.com.br` — seção Trabalhista: nexo, insalubridade, EPI, prova técnica
4. `tst.jus.br` — decisões e notícias do TST sobre acidente e doença ocupacional
5. `ilo.org` — OIT (tem versão pt): normas e relatórios de segurança e saúde no trabalho

> Nota: `sbmt.org.br` saiu da lista — é a Sociedade Brasileira de Medicina **Tropical**,
> não do Trabalho. `anamt.org.br` e `revistacipa.com.br` também saíram: não aparecem em
> busca datada, então não servem como pista. A ANAMT continua sendo coberta indiretamente,
> porque a Proteção noticia as ações dela.

## Mercado Financeiro — pasta `Pesquisas/Mercado Financeiro` — tag `mercado-financeiro`
1. `infomoney.com.br` — fechamento de mercado e análise, acesso aberto
2. `moneytimes.com.br` — tempo real do Ibovespa, juros futuros, câmbio
3. `valor.globo.com` — referência de economia (paywall: usar título/lide do snippet)
4. `exame.com` — seção invest/mercados, acesso aberto
5. `neofeed.com.br` — negócios, M&A e bastidores corporativos

## Filmes e Séries — pasta `Pesquisas/Filmes e Series` — tag `filmes-series`
1. `omelete.com.br` — pt-BR, notícia e crítica diária
2. `adorocinema.com` — pt-BR, agenda de estreias e lançamentos por streaming
3. `variety.com` — indústria: negócios, elenco, festivais
4. `deadline.com` — furos de escalação e produção
5. `hollywoodreporter.com` — indústria e audiência de streaming

## Jogos — pasta `Pesquisas/Jogos` — tag `jogos`
1. `br.ign.com` — IGN Brasil, pt-BR
2. `tecmundo.com.br` — Voxel: notícia diária de games em pt-BR (seção /voxel)
3. `adrenaline.com.br` — pt-BR, hardware e lançamentos
4. `gamespot.com` — notícia e review de peso
5. `polygon.com` — pauta editorial e indústria

> Nota: `eurogamer.net` e `rockpapershotgun.com` saíram — hoje a maior parte do que
> indexam é lista de "códigos de Roblox", ruim para digest.

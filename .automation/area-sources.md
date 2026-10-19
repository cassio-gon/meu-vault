# Fontes curadas por área — 5 sites fixos por área

> **Atualizado em 2026-10-19: a busca passou para o `web_scrape` do conector `agente-web`.**
> Cada âncora agora tem a **URL da página de seção** (ou do feed RSS) e um modo:
> - **coleta** — `web_scrape` nessa URL, com `fallback: false` e `maxChars: 6000`. Todas
>   foram testadas em 19/10/2026 pela instância própria: abriram com a lista do dia.
> - **busca** — o site bloqueia o coletor; use uma busca `site:<domínio>` no WebSearch.
> - **waitFor** — página que carrega por JavaScript; passe `waitFor: 4000`.
>
> Os 5 sites são o piso de qualidade, **não um teto**: a busca aberta do WebSearch ainda
> pode trazer furo de outra fonte confiável e datada.
>
> **Regras das buscas `site:` no WebSearch** (modo busca e plano B): domínio nu, sem
> caminho (`site:g1.globo.com saúde`, nunca `site:g1.globo.com/saude`), e nunca ponha data
> na query — a data você lê no snippet.
>
> As áreas **Puerperio** e **RN** seguem desativadas desde 2026-08-29.

## IA — pasta `Pesquisas/IA` — tag `ia`
1. TechCrunch — coleta — https://techcrunch.com/category/artificial-intelligence/
2. MIT Technology Review — coleta, waitFor 4000 — https://www.technologyreview.com/topic/artificial-intelligence/
3. Ars Technica — coleta (feed RSS; a página bloqueia) — https://arstechnica.com/ai/feed/
4. Olhar Digital — coleta — https://olhardigital.com.br/editorias/inteligencia-artificial/
5. Tecnoblog — coleta — https://tecnoblog.net/noticias/ (geral de tecnologia: filtre o que é IA)

## Saúde — pasta `Pesquisas/Saude` — tag `saude`
1. g1 Saúde — coleta — https://g1.globo.com/saude/
2. Veja Saúde — coleta — https://veja.abril.com.br/saude/
3. Agência Brasil — coleta — https://agenciabrasil.ebc.com.br/saude
4. Folha Equilíbrio e Saúde — coleta (feed RSS; a página só traz menu) — https://feeds.folha.uol.com.br/equilibrioesaude/rss091.xml
5. ScienceDaily Health & Medicine — coleta — https://www.sciencedaily.com/news/health_medicine/ (estudos; traduzir para pt-BR)

## Medicina do Trabalho — pasta `Pesquisas/Medicina do Trabalho` — tag `medtrab`
1. Revista Proteção — coleta (feed RSS; a página só traz menu) — https://protecao.com.br/feed/
2. gov.br (MTE) — busca — `site:gov.br` + "NR", "Ministério do Trabalho" (a página de notícias do MTE só devolve o calendário do filtro)
3. Conjur — busca — `site:conjur.com.br` + tema trabalhista (bloqueia o coletor)
4. TST — busca — `site:tst.jus.br` + acidente/doença ocupacional (bloqueia o coletor)
5. OIT — coleta — https://www.ilo.org/resource/news (geral: filtre segurança e saúde no trabalho)

> Nota: `sbmt.org.br` saiu da lista — é a Sociedade Brasileira de Medicina **Tropical**,
> não do Trabalho. `anamt.org.br` e `revistacipa.com.br` também saíram: não aparecem em
> busca datada, então não servem como pista. A ANAMT continua sendo coberta indiretamente,
> porque a Proteção noticia as ações dela.

## Mercado Financeiro — pasta `Pesquisas/Mercado Financeiro` — tag `mercado-financeiro`
1. InfoMoney — coleta — https://www.infomoney.com.br/mercados/
2. Money Times — coleta — https://www.moneytimes.com.br/mercados/ (tem o "tempo real" com hora)
3. Valor — coleta — https://valor.globo.com/financas/ (paywall: use título e linha fina; a data da URL do "ao vivo" é fixa e não vale)
4. Exame Invest — coleta — https://exame.com/invest/
5. NeoFeed — coleta — https://neofeed.com.br/negocios/

## Filmes e Séries — pasta `Pesquisas/Filmes e Series` — tag `filmes-series`
1. Omelete — coleta — https://www.omelete.com.br/noticias (mistura games e HQ: filtre filmes e séries)
2. AdoroCinema — coleta — https://www.adorocinema.com/noticias/filmes/
3. Variety — coleta — https://variety.com/v/film/
4. Deadline — coleta — https://deadline.com/v/film/
5. The Hollywood Reporter — coleta — https://www.hollywoodreporter.com/c/movies/

## Jogos — pasta `Pesquisas/Jogos` — tag `jogos`
1. IGN Brasil — coleta — https://br.ign.com/
2. Voxel (TecMundo, agora no Estadão) — coleta — https://www.estadao.com.br/tecmundo/voxel/
3. Adrenaline — coleta — https://www.adrenaline.com.br/games/
4. GameSpot — coleta (feed RSS; a página bloqueia) — https://www.gamespot.com/feeds/game-news/
5. Polygon — coleta — https://www.polygon.com/news/ (mistura cinema: filtre games)

> Nota: `eurogamer.net` e `rockpapershotgun.com` saíram — hoje a maior parte do que
> indexam é lista de "códigos de Roblox", ruim para digest.

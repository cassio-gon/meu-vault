"""Checagem rápida do parse de cards, feeds, datas e fotos. Uso: python3 .automation/test_coleta.py"""
from datetime import datetime

import coleta
from coleta import BRT

AGORA = datetime(2026, 10, 19, 6, 5, tzinfo=BRT)

SECAO = """
*   ![Logo da Anthropic](https://techcrunch.com/wp-content/uploads/2026/01/GettyImages-2252871842.jpg)
    In Brief
    ### [Anthropic says it’s committing 5% of its shares to a ‘public benefit fund’](https://techcrunch.com/2026/10/18/anthropic-says-its-committing-5-of-its-shares/)
    *   [Anthony Ha](https://techcrunch.com/author/anthony-ha/)
    17 hours ago
*   ![](https://techcrunch.com/wp-content/uploads/2024/01/character-ai-alexa.jpg)
    ### [Disney agrees to hire the majority of Character.AI’s workforce](https://techcrunch.com/2026/10/18/disney-agrees-to-hire/)
    *   [Anthony Ha](https://techcrunch.com/author/anthony-ha/)
    22 hours ago
*   ![](https://techcrunch.com/wp-content/uploads/autor-50x50.png)
    ### [An Nvidia insider-turned-VC on why robotics hasn’t hit its moment](https://techcrunch.com/video/a-nvidia-insider-turned-vc/)
    3 days ago
*   ### [India becomes the latest country to report rogue AI agent activity](https://techcrunch.com/2026/10/16/india-becomes-the-latest-country/)
    3 days ago
[Leia mais sobre o assunto aqui](https://techcrunch.com/2026/10/18/anthropic-says-its-committing-5-of-its-shares/)
"""

FEED = """<?xml version="1.0"?><rss version="2.0"><channel>
<image><url>https://cdn.arstechnica.net/cropped-ars-logo-512\\_480-60x60.png</url></image>
<item><title>Anthropic gives outside AI watchdog “employee-like” access</title>
<link>https://arstechnica.com/ai/2026/10/anthropic-gives-outside-ai-watchdog/</link>
<pubDate>Sun, 18 Oct 2026 16:25:19 +0000</pubDate>
<description><!\\[CDATA\\[The outside watchdog can publish its findings.\\]\\]></description>
<media:content url="https://cdn.arstechnica.net/wp-content/uploads/2026/09/claude-1024x648.jpg" type="image/jpeg" medium="image"></media:content>
</item>
<item><title>Old story from last week</title><link>https://arstechnica.com/ai/2026/10/old-story-here/</link>
<pubDate>Fri, 09 Oct 2026 20:59:01 +0000</pubDate></item>
"""


def test_secao():
    itens = coleta.cards(SECAO, "https://techcrunch.com/category/artificial-intelligence/", "TechCrunch", AGORA)
    urls = [i.url for i in itens]
    assert len(itens) == 3, urls  # vídeo fora, link "Leia mais" fora, sem duplicata
    a, b, c = itens
    assert a.foto.endswith("GettyImages-2252871842.jpg") and b.foto.endswith("character-ai-alexa.jpg")
    assert c.foto is None  # card sem foto não herda a do card anterior
    assert a.publicado.strftime("%d/%m %H") == "18/10 13" and b.publicado.day == 18
    assert c.publicado.day == 16


def test_feed():
    itens = coleta.cards(FEED, "https://arstechnica.com/ai/feed/", "Ars Technica", AGORA)
    assert [i.titulo[:9] for i in itens] == ["Anthropic", "Old story"]
    assert itens[0].foto.endswith("claude-1024x648.jpg") and itens[0].publicado.day == 18
    assert "watchdog" in itens[0].resumo


def test_datas():
    d = coleta.data_no_texto
    assert d("Publicado em 19/10/2026 às 05h30", AGORA).strftime("%d/%m %H:%M") == "19/10 05:30"
    assert d("18 de outubro de 2026", AGORA).day == 18
    assert d("Oct 17, 2026", AGORA).day == 17
    assert d("há 3 horas", AGORA).hour == 3
    assert d("31/12/2026", AGORA) is None  # futuro = lixo
    assert coleta.data_na_url("https://www.conjur.com.br/2026-out-15/contratar-uma-pessoa/", AGORA).day == 15
    assert coleta.data_na_url("https://valor.globo.com/financas/ao-vivo/2026/01/02/x.ghtml", AGORA) is None


def test_foto():
    ok = coleta.foto_ok
    assert ok("https://s2-g1.glbimg.com/abc/foto.jpg", "https://g1.globo.com/x")
    for ruim in ("http://a.com/f.jpg", "https://a.com/f.svg", "https://a.com/logo.png", "https://a.com/a b.jpg",
                 "https://pixel.wp.com/g.jpg", "https://a.com/autor-50x50.jpg", "<Base64-Image-Removed>"):
        assert not ok(ruim), ruim
    assert not ok("https://a.com/materia/", "https://a.com/materia")


if __name__ == "__main__":
    for nome, f in list(globals().items()):
        if nome.startswith("test_"):
            f()
            print("ok", nome)

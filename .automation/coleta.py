"""Coleta pelo agente web próprio e parse dos cards em código, sem modelo.

Usado por digests.py. Fala com a API nativa do agente-web (POST /api/scrape e /api/search,
`Authorization: Bearer $AGENTE_WEB_TOKEN`), sempre com fallback desligado.
As regras de foto seguem a seção "Foto do tópico" de digest-playbook.md.
"""
import email.utils
import html
import json
import os
import re
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import date, datetime, time, timedelta
from zoneinfo import ZoneInfo

BRT = ZoneInfo("America/Sao_Paulo")
AGENTE_URL = os.environ.get("AGENTE_WEB_URL", "https://agente.cassiogon.tech")
TIMEOUT_S = 150


class ColetaErro(Exception):
    pass


@dataclass(frozen=True)
class Item:
    titulo: str
    url: str
    fonte: str
    publicado: datetime | None  # BRT; só data conhecida = 23h59 do dia
    foto: str | None = None
    resumo: str = ""


# ---------------------------------------------------------------- agente-web

def agente(rota, corpo):
    token = os.environ.get("AGENTE_WEB_TOKEN")
    if not token:
        raise ColetaErro("AGENTE_WEB_TOKEN não definido")
    req = urllib.request.Request(
        f"{AGENTE_URL}{rota}",
        data=json.dumps(corpo).encode(),
        headers={"Authorization": f"Bearer {token}", "content-type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT_S) as r:
            dados = json.load(r)
    except urllib.error.HTTPError as e:
        raise ColetaErro(f"HTTP {e.code}: {e.read()[:200].decode('utf-8', 'replace')}") from None
    except (urllib.error.URLError, TimeoutError) as e:
        raise ColetaErro(f"rede: {e}") from None
    if not dados.get("success"):
        raise ColetaErro(str(dados.get("erro") or dados)[:200])
    return dados["data"]


def scrape(url, max_chars, wait_for=None):
    corpo = {"url": url, "fallback": False, "maxChars": max_chars}
    if wait_for:
        corpo["waitFor"] = wait_for
    return agente("/api/scrape", corpo).get("markdown") or ""


def buscar(query, limite=8, periodo="week"):
    """SearXNG do agente-web. Sem resultado, o servidor cai no web_search do Claude (raro)."""
    return agente("/api/search", {"query": query, "limit": limite, "timeRange": periodo})["resultados"]


# ---------------------------------------------------------------- datas

_MESES = {}
for _i, _nomes in enumerate([
    "jan janeiro january", "fev fevereiro feb february", "mar março marco march", "abr abril apr april",
    "mai maio may", "jun junho june", "jul julho july", "ago agosto aug august",
    "set setembro sep sept september", "out outubro oct october", "nov novembro november",
    "dez dezembro dec december",
], start=1):
    for _n in _nomes.split():
        _MESES[_n] = _i
_MES = "|".join(sorted(_MESES, key=len, reverse=True))
_HORA = r"(?:\s*(?:às|as|at|,|-|·)?\s*(\d{1,2})[:h](\d{2}))?"
_ABS = [  # (regex, ordem dos grupos: dia, mês, ano)
    (re.compile(rf"\b(\d{{1,2}})/(\d{{1,2}})/(\d{{4}}|\d{{2}})\b{_HORA}"), "dma"),
    (re.compile(rf"\b(\d{{1,2}})\.(\d{{1,2}})\.(\d{{4}})\b{_HORA}"), "dma"),
    (re.compile(rf"\b(\d{{1,2}})(?:º)? de ({_MES}) de (\d{{4}}){_HORA}", re.I), "dma"),
    (re.compile(rf"\b(\d{{1,2}}) ({_MES})\.? (\d{{4}}){_HORA}", re.I), "dma"),
    (re.compile(rf"\b({_MES})\.? (\d{{1,2}}),? (\d{{4}}){_HORA}", re.I), "mda"),
    (re.compile(rf"\b(\d{{4}})-(\d{{2}})-(\d{{2}})(?:[T ](\d{{2}}):(\d{{2}}))?"), "amd"),
]
_UNIDADE = r"(seg|segundos?|secs?|seconds?|min|mins|minutos?|minutes?|h|hrs?|horas?|hours?|d|dias?|days?)"
_REL = re.compile(rf"\b(?:há|ha)\s+(\d+)\s*{_UNIDADE}\b|\b(\d+)\s*{_UNIDADE}\s+(?:ago|atrás)", re.I)
_DIA_REL = re.compile(r"\b(ontem|yesterday|hoje|today)\b(?:,?\s*(?:às|as|at)\s*(\d{1,2})[:h](\d{2}))?", re.I)
_DM_HORA = re.compile(r"\b(\d{1,2})/(\d{1,2})\s*(?:às|as|-|,)?\s*(\d{1,2})[:h](\d{2})\b")  # "16/10 às 17:22"
_URL_DATA = [
    (re.compile(r"/(20\d\d)/(\d{1,2})/(\d{1,2})(?:/|$)"), "amd"),
    (re.compile(r"/(20\d\d)-(\d{2})-(\d{2})(?:/|-|$)"), "amd"),
    (re.compile(rf"/(20\d\d)-({_MES})-(\d{{1,2}})(?:/|$)", re.I), "amd"),
]


def _montar(grupos, ordem, agora):
    vals = dict(zip(ordem, grupos[:3]))
    try:
        dia = int(vals["d"])
        mes = int(vals["m"]) if vals["m"].isdigit() else _MESES[vals["m"].lower().rstrip(".")]
        ano = int(vals["a"])
    except (KeyError, ValueError):
        return None
    ano += 2000 if ano < 100 else 0
    if mes > 12 and dia <= 12:  # data no formato americano
        dia, mes = mes, dia
    try:
        d = date(ano, mes, dia)
    except ValueError:
        return None
    hh, mm = grupos[3:5] if len(grupos) >= 5 else (None, None)
    hora = time(int(hh), int(mm)) if hh and int(hh) < 24 and int(mm) < 60 else time(23, 59)
    quando = datetime.combine(d, hora, BRT)
    return quando if quando <= agora + timedelta(hours=12) else None  # data futura = lixo


def data_no_texto(texto, agora):
    """Primeira data (relativa ou absoluta) que aparece no texto."""
    achados = []
    for m in _REL.finditer(texto):
        n, u = (m.group(1), m.group(2)) if m.group(1) else (m.group(3), m.group(4))
        u = u.lower()
        unidade = "seconds" if u.startswith("s") else "minutes" if u.startswith("min") else "days" if u.startswith("d") else "hours"
        achados.append((m.start(), agora - timedelta(**{unidade: int(n)})))
    for m in _DIA_REL.finditer(texto):
        d = agora.date() - timedelta(days=1 if m.group(1).lower() in ("ontem", "yesterday") else 0)
        hora = time(int(m.group(2)), int(m.group(3))) if m.group(2) and int(m.group(2)) < 24 and int(m.group(3)) < 60 else time(23, 59)
        achados.append((m.start(), datetime.combine(d, hora, BRT)))
    for m in _DM_HORA.finditer(texto):
        d, mes, hh, mm = m.groups()
        q = _montar((d, mes, str(agora.year), hh, mm), "dma", agora) or _montar((d, mes, str(agora.year - 1), hh, mm), "dma", agora)
        if q:
            achados.append((m.start(), q))
    for rx, ordem in _ABS:
        for m in rx.finditer(texto):
            q = _montar(m.groups(), ordem, agora)
            if q:
                achados.append((m.start(), q))
    return min(achados, key=lambda a: a[0])[1] if achados else None


def data_na_url(url, agora):
    if "ao-vivo" in url:  # páginas "ao vivo" têm data fixa na URL (nota do Valor no area-sources)
        return None
    caminho = urllib.parse.urlsplit(url).path
    for rx, ordem in _URL_DATA:
        m = rx.search(caminho)
        if m:
            return _montar(m.groups(), ordem, agora)
    return None


# ---------------------------------------------------------------- foto (seção "Foto do tópico")

_FOTO_RUIM = re.compile(r"\.svg|\.gif|pixel\.|analytics|sync|base64|logo|icon|autor|50x50", re.I)


def foto_ok(url, pagina=None):
    if not url or not url.startswith("https://") or any(c in url for c in "\"' <>"):
        return False
    return not _FOTO_RUIM.search(url) and url.rstrip("/") != (pagina or "").rstrip("/")


# ---------------------------------------------------------------- parse dos cards

_IMG = re.compile(r"!\[([^\]]*)\]\((<Base64-Image-Removed>|\S+?)(?:\s+\"[^\"]*\")?\)")
_LINK = re.compile(r'(?<!!)\[((?:[^\[\]]|!?\[[^\[\]]*\])*)\]\((https?://[^\s)]+)(?:\s+"([^"]*)")?\)')
_SUBLINHADO = re.compile(r"^[-=]{3,}$")
_NAO_MATERIA = re.compile(r"/(autor|author|authors|tag|tags|category|categoria|editorias|topic|c|v|video|videos|podcast|podcasts|events|newsletter|print-article)/|\.(jpe?g|png|webp|gif|svg|mp4|pdf)$", re.I)
_CARA_DE_MATERIA = re.compile(r"\d{5,}|/20\d\d[/-]|[^/]*-[^/]*-[^/]*-")
_RFC822 = re.compile(r"\w{3}, \d{1,2} \w{3} \d{4} \d\d:\d\d:\d\d [+-]\d{4}")


def _desescapar(s):
    return re.sub(r"\\([\[\]_*()#!-])", r"\1", s)


def dominio(host):
    partes = host.lower().removeprefix("www.").split(".")
    n = 3 if len(partes) >= 3 and len(partes[-1]) == 2 and partes[-2] in {"com", "org", "gov", "jus", "net", "edu", "ebc"} else 2
    return ".".join(partes[-n:])


def _eh_materia(url, secao):
    p = urllib.parse.urlsplit(url)
    if dominio(p.netloc) != dominio(urllib.parse.urlsplit(secao).netloc):
        return False
    if url.split("#")[0].rstrip("/") == secao.rstrip("/") or _NAO_MATERIA.search(p.path):
        return False
    return bool(_CARA_DE_MATERIA.search(p.path))


def _titulo_ok(t):
    t = re.sub(r"[*_#`]", "", t or "").strip()
    return len(t) >= 15 and len(t.split()) >= 3 and not re.match(r"(read|leia|saiba|veja|ver|continue|comments?|coment)", t, re.I)


def _palavras(s):
    return set(re.findall(r"[a-z0-9]{4,}", norm_titulo(s.replace("-", " "))))


def _candidatos(texto, atributo):
    """Títulos possíveis de um link de card. Prioridade: atributo title > heading > linha > alt da imagem."""
    out = [(3, atributo)] if atributo else []
    out += [(0, alt) for alt, _ in _IMG.findall(texto)]
    sem_url = re.sub(r"\S*https?://\S*|\"", " ", _IMG.sub("", texto))
    linhas = [" ".join(re.sub(r"[*_`\\]", " ", linha).split()) for linha in sem_url.splitlines()]
    for i, linha in enumerate(linhas):
        if linha and not _SUBLINHADO.match(linha):
            heading = linha.startswith("#") or (i + 1 < len(linhas) and bool(_SUBLINHADO.match(linhas[i + 1])))
            out.append((2 if heading else 1, linha.lstrip("# ")))
    return out


def _melhor_titulo(cands, url):
    """O candidato que mais bate com o slug da URL; alt de imagem só entra se bater."""
    slug = _palavras(urllib.parse.urlsplit(url).path)
    validos = [(p, " ".join(t.split())) for p, t in cands if _titulo_ok(t)]
    if not validos:
        return None
    p, t = max(validos, key=lambda c: (min(len(_palavras(c[1]) & slug), 2), c[0], -len(c[1])))
    if p == 0 and len(slug) >= 3 and len(_palavras(t) & slug) < 2:
        return None
    return t


def cards(md, secao, fonte, agora, eh_feed=False):
    """Matérias de uma página de seção ou de um feed (XML, lista renderizada ou texto sem tags)."""
    if re.search(r"<(rss|feed|rdf:RDF)\b", md[:2000]):
        return feed(md, fonte, agora)
    md = _desescapar(md)
    if eh_feed:
        lista = _feed_lista(md, fonte, agora)
        return lista or _feed_texto(md, secao, fonte, agora)
    links = [m for m in _LINK.finditer(md) if _eh_materia(m.group(2).split("#")[0], secao)]
    grupos = {}
    for m in links:
        g = grupos.setdefault(m.group(2).split("#")[0], {"cands": [], "fotos": [], "textos": [], "depois": []})
        if "#" not in m.group(2):  # link com âncora (#comments, #respond) não traz o título
            g["cands"] += _candidatos(m.group(1), m.group(3))
        g["fotos"] += [u for _, u in _IMG.findall(m.group(1))]
        g["textos"].append(m.group(1))
    ordem, antes = [], {}
    for k, m in enumerate(links):  # o texto entre um link de matéria e o próximo pertence ao primeiro
        url = m.group(2).split("#")[0]
        fim = links[k + 1].start() if k + 1 < len(links) else len(md)
        grupos[url]["depois"].append(_limpo(md[m.end():fim]))
        if url not in ordem:
            ordem.append(url)
            antes[url] = md[links[k - 1].end() if k else 0:m.start()]
    itens = []
    for url in ordem:
        g = grupos[url]
        titulo = _melhor_titulo(g["cands"], url)
        if not titulo:
            continue
        foto = next((f for f in g["fotos"] if foto_ok(f, url)), None) \
            or next((f for _, f in reversed(_IMG.findall(antes[url])) if foto_ok(f, url)), None)
        quando = data_no_texto(_limpo("\n".join(g["textos"])), agora) \
            or next((d for d in (data_no_texto(t[:300], agora) for t in g["depois"]) if d), None) \
            or data_na_url(url, agora)
        itens.append(Item(titulo, url, fonte, quando, foto, max(g["depois"], key=len)[:300]))
    return itens


def _feed_lista(md, fonte, agora):
    """Feed que o Firecrawl renderizou como lista (Folha): '*   Título' + data + texto + [Leia mais](link)."""
    itens = []
    for bloco in re.split(r"^\*\s{1,4}(?=\S)", md, flags=re.M)[1:]:
        linhas = [linha.strip() for linha in bloco.splitlines()]
        urls = [u.split("/*")[-1] for u in re.findall(r"\]\((https?://[^\s)]+)\)", bloco)]
        if urls and len(linhas) > 1 and _SUBLINHADO.match(linhas[1]) and _titulo_ok(linhas[0]):
            itens.append(Item(linhas[0], urls[-1], fonte, data_no_texto(_limpo(bloco), agora), None,
                              _limpo("\n".join(linhas[2:]))[:200]))
    return itens


def _feed_texto(md, secao, fonte, agora):
    """Feed que o Firecrawl devolveu sem as tags (GameSpot): 'título URL descrição pubDate ...'."""
    achados = [m for m in re.finditer(r"(?<![(\[\w])https?://[^\s)\]]+", md) if _eh_materia(m.group(0), secao)]
    itens = []
    for i, m in enumerate(achados):
        slug, titulo = _palavras(urllib.parse.urlsplit(m.group(0)).path), []
        for palavra in reversed(md[achados[i - 1].end() if i else 0:m.start()].split()):
            if not _palavras(palavra) <= slug:
                break
            titulo.insert(0, palavra)
        fim = achados[i + 1].start() if i + 1 < len(achados) else len(md)
        data = _RFC822.search(md, m.end(), fim)
        quando = email.utils.parsedate_to_datetime(data.group(0)).astimezone(BRT) if data else None
        if _titulo_ok(" ".join(titulo)):
            itens.append(Item(" ".join(titulo), m.group(0), fonte, quando, None, _limpo(md[m.end():fim])[:200]))
    return itens


def _limpo(md):
    """Markdown sem imagens, URLs nem marcação: só o texto, numa linha."""
    s = _IMG.sub("", md)
    s = re.sub(r"(?<!!)\[([^\]]*)\]\([^)]*\)", r"\1", s)
    return " ".join(re.sub(r"[*_#>`|]", " ", s).split())


def _tag(bloco, nome):
    m = re.search(rf"<{nome}\b[^>]*>\s*(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?\s*</{nome}>", bloco, re.S)
    return html.unescape(re.sub(r"<[^>]+>", " ", m.group(1))).strip() if m else ""


def feed(md, fonte, agora):
    xml = _desescapar(md)
    itens = []
    for bloco in re.split(r"<item\b|<entry\b", xml)[1:]:
        titulo = re.sub(r"\s+", " ", _tag(bloco, "title"))
        link = _tag(bloco, "link") or (re.search(r'<link[^>]*href="([^"]+)"', bloco) or [None, ""])[1]
        if not titulo or not link.startswith("http"):
            continue
        bruto = _tag(bloco, "pubDate") or _tag(bloco, "dc:date") or _tag(bloco, "published") or _tag(bloco, "updated")
        try:
            quando = email.utils.parsedate_to_datetime(bruto).astimezone(BRT)
        except (TypeError, ValueError, IndexError):
            quando = data_no_texto(bruto, agora) if bruto else data_na_url(link, agora)
        fotos = re.findall(r'<media:content[^>]*url="([^"]+)"[^>]*(?:medium="image"|type="image/)', bloco) \
            + re.findall(r'<media:thumbnail[^>]*url="([^"]+)"', bloco) \
            + re.findall(r'<enclosure[^>]*url="([^"]+)"[^>]*type="image/', bloco) \
            + re.findall(r'<img[^>]*src="([^"]+)"', html.unescape(bloco))
        foto = next((f for f in fotos if foto_ok(f, link)), None)
        itens.append(Item(titulo, link, fonte, quando, foto, _tag(bloco, "description")[:200]))
    return itens


def materia(url, md, agora):
    """Texto limpo, data e primeira foto válida de uma matéria coletada."""
    md = _desescapar(md)
    fotos = [u for _, u in _IMG.findall(md) if foto_ok(u, url)]
    texto = "\n".join(t for t in (_limpo(linha) for linha in md.splitlines()) if t)
    return texto, data_no_texto(md[:1500], agora), (fotos[0] if fotos else None)


# ---------------------------------------------------------------- dedupe

def norm_titulo(t):
    t = unicodedata.normalize("NFKD", t.lower())
    return " ".join(re.findall(r"[a-z0-9]+", "".join(c for c in t if not unicodedata.combining(c))))


def norm_url(u):
    p = urllib.parse.urlsplit(u.strip())
    return (p.netloc.lower().removeprefix("www.") + p.path.rstrip("/")).lower()

---
title: Calima — probe do site (medido do Mac)
date: 2026-11-26
area: Calima
tags: [calima, probe, uptime]
source: mac-launchagent
---

# Probe de `calima.med.br` — 2026-11-26 07:06:24 (America/Sao_Paulo)

> Medido do Mac do Cássio, não da nuvem. O ambiente das Routines tem egress bloqueado
> para este host. Se o timestamp acima estiver velho, o Mac estava desligado — diga isso
> no relatório em vez de afirmar que o site caiu.

## Requisições

| Path | HTTP | Tempo total | TTFB | Bytes | Content-Type |
|---|---|---|---|---|---|
| `/` | 200 | 0.109108s | 0.075782s | 54707 B | text/html; charset=UTF-8 |
| `/manifest.json` | 200 | 0.176026s | 0.175740s | 884 B | application/json; charset=UTF-8 |
| `/sw.js` | 200 | 0.087676s | 0.074206s | 13942 B | application/javascript; charset=UTF-8 |
| `/js/app.js` | 200 | 0.121579s | 0.077180s | 98652 B | application/javascript; charset=UTF-8 |

## Compressão (`/css/style.css` com `Accept-Encoding: gzip, br`)

```
content-encoding: gzip
```

## Certificado TLS

```
notAfter=Feb 21 19:40:10 2027 GMT issuer= /C=US/O=Let's Encrypt/CN=YR2 
```

## Headers de resposta de `/`

```http
HTTP/2 200 
accept-ranges: bytes
alt-svc: h3=":443"; ma=2592000
cache-control: public, max-age=0
content-security-policy: default-src 'self'; img-src 'self' data:; style-src 'self'; script-src 'self'; connect-src 'self' wss://calima.med.br https://api.github.com https://raw.githubusercontent.com; object-src 'none'; base-uri 'self'; frame-ancestors 'none'; form-action 'self'
content-type: text/html; charset=UTF-8
cross-origin-opener-policy: same-origin
date: Thu, 26 Nov 2026 10:06:23 GMT
etag: W/"d5b3-1a21567f440"
last-modified: Thu, 26 Nov 2026 01:11:04 GMT
referrer-policy: no-referrer
strict-transport-security: max-age=15552000
vary: Cookie
x-content-type-options: nosniff
x-frame-options: DENY
content-length: 54707

```

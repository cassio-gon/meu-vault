---
title: Calima — probe do site (medido do Mac)
date: 2026-11-25
area: Calima
tags: [calima, probe, uptime]
source: mac-launchagent
---

# Probe de `calima.med.br` — 2026-11-25 01:06:05 (America/Sao_Paulo)

> Medido do Mac do Cássio, não da nuvem. O ambiente das Routines tem egress bloqueado
> para este host. Se o timestamp acima estiver velho, o Mac estava desligado — diga isso
> no relatório em vez de afirmar que o site caiu.

## Requisições

| Path | HTTP | Tempo total | TTFB | Bytes | Content-Type |
|---|---|---|---|---|---|
| `/` | 200 | 0.146106s | 0.096244s | 54707 B | text/html; charset=UTF-8 |
| `/manifest.json` | 200 | 0.163934s | 0.163572s | 884 B | application/json; charset=UTF-8 |
| `/sw.js` | 200 | 0.118174s | 0.100336s | 13942 B | application/javascript; charset=UTF-8 |
| `/js/app.js` | 200 | 0.153183s | 0.096640s | 98652 B | application/javascript; charset=UTF-8 |

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
date: Wed, 25 Nov 2026 04:06:05 GMT
etag: W/"d5b3-1a210b45358"
last-modified: Wed, 25 Nov 2026 03:16:23 GMT
referrer-policy: no-referrer
strict-transport-security: max-age=15552000
vary: Cookie
x-content-type-options: nosniff
x-frame-options: DENY
content-length: 54707

```

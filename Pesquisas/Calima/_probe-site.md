---
title: Calima — probe do site (medido do Mac)
date: 2026-11-07
area: Calima
tags: [calima, probe, uptime]
source: mac-launchagent
---

# Probe de `calima.med.br` — 2026-11-07 17:03:44 (America/Sao_Paulo)

> Medido do Mac do Cássio, não da nuvem. O ambiente das Routines tem egress bloqueado
> para este host. Se o timestamp acima estiver velho, o Mac estava desligado — diga isso
> no relatório em vez de afirmar que o site caiu.

## Requisições

| Path | HTTP | Tempo total | TTFB | Bytes | Content-Type |
|---|---|---|---|---|---|
| `/` | 200 | 0.474918s | 0.433103s | 50810 B | text/html; charset=UTF-8 |
| `/manifest.json` | 200 | 0.409415s | 0.408226s | 884 B | application/json; charset=UTF-8 |
| `/sw.js` | 200 | 0.336146s | 0.317399s | 11980 B | application/javascript; charset=UTF-8 |
| `/js/app.js` | 200 | 0.448658s | 0.279429s | 92757 B | application/javascript; charset=UTF-8 |

## Compressão (`/css/style.css` com `Accept-Encoding: gzip, br`)

```
content-encoding: gzip
```

## Certificado TLS

```
notAfter=Dec 22 22:32:29 2026 GMT issuer= /C=US/O=Let's Encrypt/CN=YR2 
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
date: Sat, 07 Nov 2026 20:03:42 GMT
etag: W/"c67a-1a1b73c5d48"
last-modified: Sat, 07 Nov 2026 18:19:09 GMT
referrer-policy: no-referrer
strict-transport-security: max-age=15552000
vary: Cookie
x-content-type-options: nosniff
x-frame-options: DENY
content-length: 50810

```

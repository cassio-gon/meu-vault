---
title: Calima — probe do site (medido do Mac)
date: 2026-11-20
area: Calima
tags: [calima, probe, uptime]
source: mac-launchagent
---

# Probe de `calima.med.br` — 2026-11-20 08:49:06 (America/Sao_Paulo)

> Medido do Mac do Cássio, não da nuvem. O ambiente das Routines tem egress bloqueado
> para este host. Se o timestamp acima estiver velho, o Mac estava desligado — diga isso
> no relatório em vez de afirmar que o site caiu.

## Requisições

| Path | HTTP | Tempo total | TTFB | Bytes | Content-Type |
|---|---|---|---|---|---|
| `/` | 200 | 0.158410s | 0.087156s | 54571 B | text/html; charset=UTF-8 |
| `/manifest.json` | 200 | 0.152744s | 0.152350s | 884 B | application/json; charset=UTF-8 |
| `/sw.js` | 200 | 0.127827s | 0.081683s | 13477 B | application/javascript; charset=UTF-8 |
| `/js/app.js` | 200 | 0.156324s | 0.106306s | 97288 B | application/javascript; charset=UTF-8 |

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
date: Fri, 20 Nov 2026 11:49:05 GMT
etag: W/"d52b-1a1f72259d0"
last-modified: Fri, 20 Nov 2026 04:06:26 GMT
referrer-policy: no-referrer
strict-transport-security: max-age=15552000
vary: Cookie
x-content-type-options: nosniff
x-frame-options: DENY
content-length: 54571

```

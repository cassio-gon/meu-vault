---
title: Calima — probe do site (medido do Mac)
date: 2026-08-27
area: Calima
tags: [calima, probe, uptime]
source: mac-launchagent
---

# Probe de `calima.med.br` — 2026-08-27 10:59:29 (America/Sao_Paulo)

> Medido do Mac do Cássio, não da nuvem. O ambiente das Routines tem egress bloqueado
> para este host. Se o timestamp acima estiver velho, o Mac estava desligado — diga isso
> no relatório em vez de afirmar que o site caiu.

## Requisições

| Path | HTTP | Tempo total | TTFB | Bytes | Content-Type |
|---|---|---|---|---|---|
| `/` | 200 | 0.578309s | 0.440237s | 31427 B | text/html; charset=UTF-8 |
| `/manifest.json` | 200 | 0.527500s | 0.527083s | 884 B | application/json; charset=UTF-8 |
| `/sw.js` | 200 | 0.722952s | 0.509693s | 7825 B | application/javascript; charset=UTF-8 |
| `/js/app.js` | 200 | 0.768686s | 0.497854s | 64778 B | application/javascript; charset=UTF-8 |

## Compressão (`/css/style.css` com `Accept-Encoding: gzip, br`)

```
content-encoding: gzip
```

## Certificado TLS

```
notAfter=Oct 24 01:51:45 2026 GMT issuer= /C=US/O=Let's Encrypt/CN=YR2 
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
date: Thu, 27 Aug 2026 13:59:27 GMT
etag: W/"7ac3-1a041297880"
last-modified: Thu, 27 Aug 2026 03:00:32 GMT
referrer-policy: no-referrer
strict-transport-security: max-age=15552000
x-content-type-options: nosniff
x-frame-options: DENY
content-length: 31427

```

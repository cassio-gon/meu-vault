---
title: Calima — probe do site (medido do Mac)
date: 2026-08-13
area: Calima
tags: [calima, probe, uptime]
source: mac-launchagent
---

# Probe de `calima.med.br` — 2026-08-13 01:56:15 (America/Sao_Paulo)

> Medido do Mac do Cássio, não da nuvem. O ambiente das Routines tem egress bloqueado
> para este host. Se o timestamp acima estiver velho, o Mac estava desligado — diga isso
> no relatório em vez de afirmar que o site caiu.

## Requisições

| Path | HTTP | Tempo total | TTFB | Bytes | Content-Type |
|---|---|---|---|---|---|
| `/` | 200 | 0.607679s | 0.465338s | 25911 B | text/html; charset=UTF-8 |
| `/manifest.json` | 200 | 0.498403s | 0.497959s | 884 B | application/json; charset=UTF-8 |
| `/sw.js` | 200 | 0.497321s | 0.495834s | 5993 B | application/javascript; charset=UTF-8 |
| `/js/app.js` | 200 | 0.772169s | 0.500533s | 46736 B | application/javascript; charset=UTF-8 |

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
content-security-policy: default-src 'self'; img-src 'self' data:; style-src 'self'; script-src 'self'; connect-src 'self' https://api.github.com https://raw.githubusercontent.com; object-src 'none'; base-uri 'self'; frame-ancestors 'none'; form-action 'self'
content-type: text/html; charset=UTF-8
cross-origin-opener-policy: same-origin
date: Thu, 13 Aug 2026 04:56:13 GMT
etag: W/"6537-19ff8ec7d60"
last-modified: Thu, 13 Aug 2026 02:21:16 GMT
referrer-policy: no-referrer
strict-transport-security: max-age=15552000
x-content-type-options: nosniff
x-frame-options: DENY
content-length: 25911

```

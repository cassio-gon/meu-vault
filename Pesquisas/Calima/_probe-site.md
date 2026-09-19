---
title: Calima — probe do site (medido do Mac)
date: 2026-09-19
area: Calima
tags: [calima, probe, uptime]
source: mac-launchagent
---

# Probe de `calima.med.br` — 2026-09-19 18:40:45 (America/Sao_Paulo)

> Medido do Mac do Cássio, não da nuvem. O ambiente das Routines tem egress bloqueado
> para este host. Se o timestamp acima estiver velho, o Mac estava desligado — diga isso
> no relatório em vez de afirmar que o site caiu.

## Requisições

| Path | HTTP | Tempo total | TTFB | Bytes | Content-Type |
|---|---|---|---|---|---|
| `/` | 200 | 0.742385s | 0.466600s | 45230 B | text/html; charset=UTF-8 |
| `/manifest.json` | 200 | 0.502444s | 0.501937s | 884 B | application/json; charset=UTF-8 |
| `/sw.js` | 200 | 0.624919s | 0.492681s | 9332 B | application/javascript; charset=UTF-8 |
| `/js/app.js` | 200 | 0.898801s | 0.496115s | 82808 B | application/javascript; charset=UTF-8 |

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
date: Sat, 19 Sep 2026 21:40:44 GMT
etag: W/"b0ae-1a0bb2d6ad8"
last-modified: Sat, 19 Sep 2026 19:38:31 GMT
referrer-policy: no-referrer
strict-transport-security: max-age=15552000
x-content-type-options: nosniff
x-frame-options: DENY
content-length: 45230

```

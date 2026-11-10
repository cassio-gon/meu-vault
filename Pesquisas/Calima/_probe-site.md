---
title: Calima — probe do site (medido do Mac)
date: 2026-11-10
area: Calima
tags: [calima, probe, uptime]
source: mac-launchagent
---

# Probe de `calima.med.br` — 2026-11-10 06:04:36 (America/Sao_Paulo)

> Medido do Mac do Cássio, não da nuvem. O ambiente das Routines tem egress bloqueado
> para este host. Se o timestamp acima estiver velho, o Mac estava desligado — diga isso
> no relatório em vez de afirmar que o site caiu.

## Requisições

| Path | HTTP | Tempo total | TTFB | Bytes | Content-Type |
|---|---|---|---|---|---|
| `/` | 200 | 0.169772s | 0.131226s | 50810 B | text/html; charset=UTF-8 |
| `/manifest.json` | 200 | 0.199599s | 0.199099s | 884 B | application/json; charset=UTF-8 |
| `/sw.js` | 200 | 0.165655s | 0.147719s | 11980 B | application/javascript; charset=UTF-8 |
| `/js/app.js` | 200 | 0.223987s | 0.088523s | 92757 B | application/javascript; charset=UTF-8 |

## Compressão (`/css/style.css` com `Accept-Encoding: gzip, br`)

```
(nenhum — servidor respondeu sem content-encoding mesmo com Accept-Encoding: gzip, br)
```

## Certificado TLS

```
notAfter=Dec 22 22:32:29 2026 GMT issuer= /C=US/O=Let's Encrypt/CN=YR2 
```

## Headers de resposta de `/`

```http
curl: (28) Connection timed out after 20101 milliseconds
```

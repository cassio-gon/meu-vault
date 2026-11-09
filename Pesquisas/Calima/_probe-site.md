---
title: Calima — probe do site (medido do Mac)
date: 2026-11-09
area: Calima
tags: [calima, probe, uptime]
source: mac-launchagent
---

# Probe de `calima.med.br` — 2026-11-09 18:02:15 (America/Sao_Paulo)

> Medido do Mac do Cássio, não da nuvem. O ambiente das Routines tem egress bloqueado
> para este host. Se o timestamp acima estiver velho, o Mac estava desligado — diga isso
> no relatório em vez de afirmar que o site caiu.

## Requisições

| Path | HTTP | Tempo total | TTFB | Bytes | Content-Type |
|---|---|---|---|---|---|
| `/` | ERRO | - | - | - |
| `/manifest.json` | ERRO | - | - | - |
| `/sw.js` | ERRO | - | - | - |
| `/js/app.js` | ERRO | - | - | - |

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
curl: (28) Connection timed out after 20120 milliseconds
```

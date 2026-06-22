---
title: IA — Índice
tags:
  - ia
  - moc
area: IA
---

# 🤖 Pesquisas — IA

Digests diários gerados automaticamente às 8h (Firecrawl + Claude). A tabela abaixo
se atualiza sozinha conforme novas notas chegam (requer o plugin **Dataview**).

```dataview
TABLE date AS "Data", source AS "Fonte"
FROM "Pesquisas/IA"
WHERE area = "IA" AND file.name != "_index"
SORT date DESC
```

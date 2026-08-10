---
title: Calima — Backlog de sugestões (avaliação diária)
area: Calima
tags: [calima, produto, backlog]
source: routine
---

# Calima — Backlog de sugestões

> Acumulado pela rotina diária de avaliação do Calima (`Pesquisas/Calima/AAAA-MM-DD — Avaliacao Calima.md`).
> Cada linha nasceu como "sugestão nova" num relatório; a rotina lê esta tabela antes de sugerir de novo,
> para não repetir. Ao constatar que algo já foi implementado no código, marcar "feito" aqui (e não apagar a
> linha — vira histórico). Isto é separado do `~/.claude/workstations/Prontuario-IA/PENDENCIAS.md`, que
> rastreia pendências de design/produto conhecidas por outras vias (audit, pedidos do Cássio, revisões).

| Sugestão | Data | Status |
|---|---|---|
| Ativar compressão HTTP (gzip/brotli) no Express (`server/server.js:118`) | 2026-08-10 | **improcedente** — probe do Mac em 10/08 08:20 mostrou `content-encoding: gzip` em `/css/style.css` com `Accept-Encoding: gzip, br`. O Traefik/Coolify já comprime na borda; a conclusão veio de análise só-por-código, sem medir produção |
| `Cache-Control` de longa duração para ativos imutáveis (fontes/ícones/vendor), sem tocar no caminho do SHELL do SW | 2026-08-10 | aberto |
| App Shortcuts no `manifest.json` ("Novo atendimento" direto do ícone) | 2026-08-10 | aberto |
| Assinatura eletrônica gov.br (gratuita) como reforço sobre o selo médico-legal existente | 2026-08-10 | aberto |
| CID-10 (DATASUS) como dataset estático para autocomplete determinístico no campo HD:, complementar à sugestão por IA | 2026-08-10 | aberto |

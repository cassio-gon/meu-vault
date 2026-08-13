---
title: Avaliação Calima — 2026-08-13
date: 2026-08-13
area: Calima
tags: [calima, produto, auditoria]
source: routine
---

# Calima — Avaliação diária (2026-08-13)

## TL;DR

- **21 commits em 24h** — dia de feature grande: receita médica ponta a ponta (catálogo de medicamentos, emissão, importação de modelos do dontpad, folha A4 para impressão). Suite alegada 554/554.
- **Achado de segurança/negócio (alto):** `server/routes/receitas.js` nunca aplica `requireEscrita`/`requireCota` — diferente de `records.js`, `pacientes.js`, `format`/`sugerir`. Médico bloqueado por trial vencido ou inadimplência continua importando modelos (chamada real à API da Anthropic) e emitindo receitas sem paywall.
- **2 regressões de deploy já corrigidas no próprio dia**, mas passaram despercebidas pela suíte: import de `server/lib/cota.js`/`planos.js` quebrava o boot do servidor por ~4h17 (`b4bfeb4`→`202c504`); `catalogo.json` faltava no Dockerfile e nasceu vazio em produção por ~10h (`b4bfeb4`→`a240d6c`). Nenhum teste sobe `server.js` de verdade — é por isso que passaram.
- **Tema de hoje (índice 1): Acessibilidade.** Autocomplete de medicamento não segue o padrão ARIA combobox que o autocomplete de paciente, na mesma tela, já usa; alvos de toque <44px reapareceram em 3 botões novos.
- **Site vivo:** probe de 01:56 BRT, saudável, TLS ok, gzip confirmado.

---

## O QUE MUDOU EM 24H

21 commits, todos de 12/08 — dia dominado pela feature de receita médica: `f44dbe4` (spec/plano) → `0f565d2` (registro profissional do médico) → `b4bfeb4` (catálogo de medicamentos do bulário ANVISA) → `e1a7b0a` (chassi A4 + impressão) → `ba360e9` (composição/emissão/histórico/modelos de prescrição) → `e136368` (nova aba Documentos) → `442e7fa`+`1bd8a35`+`392b678` (importar modelos do dontpad) → `2a9f712` (autocomplete de paciente e medicamento) → mais 8 commits de ajuste fino de UI e um fix de deploy (`a240d6c`).

Revisei o diff completo (não só o resumo) via um subagente dedicado. Três achados relevantes, todos já detalhados no TL;DR:

1. **`server/routes/receitas.js` sem `requireEscrita`/`requireCota`** — confirmado por grep: zero ocorrências no arquivo, contra `server.js:69,72` (que gateia `/api/format` e `/api/sugerir`) e `records.js:55`/`pacientes.js:28,39`. `POST /api/receitas/importar-dontpad` dispara `extrairModelos` (chamada real à Anthropic, até 4096 tokens de saída) sem checar `billing_status`. `tests/receitas.test.js` só semeia médico em trial ativo (linhas 12-18) — o gap não é pego pela suíte.
2. **`202c504`** ("commita libs de planos/cota que ficaram fora do push anterior") é regressão real, não só mensagem de commit cautelosa: `server/server.js:13` importa `cota.js` desde `b4bfeb4` (12:17), mas o arquivo só existe a partir de `202c504` (16:44) — qualquer boot nesse intervalo falharia com `ERR_MODULE_NOT_FOUND`. Não dá para confirmar deploy real em produção a partir do git deste clone.
3. **`a240d6c`** corrige `Dockerfile` que não copiava `data/medicamentos/catalogo.json` — sem isso `semearMedicamentos` falha em silêncio (`catch`, sem crash) e o autocomplete de medicamento nascia vazio. Janela: `b4bfeb4` (12:17) até `a240d6c` (22:20), ~10h.

Ambas as regressões de deploy já estão corrigidas hoje — ficam de exemplo de "funcionou local, faltou no deploy" e o fato de nenhum teste subir `server.js` de verdade. Fora isso (13 commits restantes), sem bug de lógica ou violação do princípio "IA nunca inventa dado clínico" — o prompt de extração do dontpad (`importar-prescricoes.js:65-77`) instrui explicitamente "NUNCA invente... copie o que está escrito", e o seed do catálogo deixa `principio_ativo` nulo em vez de vincular por adivinhação. Nenhum item do `PENDENCIAS.md` foi fechado sem baixa por este trabalho.

---

## SITE VIVO

Probe do Mac em **2026-08-13 01:56:15 America/Sao_Paulo** (~7h antes desta execução) — fresco. `/`, `/manifest.json`, `/sw.js`, `/js/app.js` todos 200; `content-encoding: gzip` confirmado em `/css/style.css`; TLS Let's Encrypt válido até 24/10/2026; headers de segurança (CSP, HSTS, X-Frame-Options DENY, COOP, nosniff) presentes. Nada a reportar.

---

## TEMA DO DIA — índice 1 — Acessibilidade

Foco nas telas novas de hoje (receita/documentos), por serem o maior volume de UI nova do dia e o fluxo mais crítico (prescrição).

1. **Autocomplete de medicamento sem padrão ARIA combobox (médio).** `public/js/receita-ui.js:118-170` monta busca de medicamento como `<input type="search">` + `<ul class="rx-sugestoes hidden">` de `<li><button>`, sem `role="combobox"`/`aria-expanded`/`aria-controls` no input nem `role="listbox"`/`role="option"` na lista, e sem navegação por seta. É inconsistência dentro do próprio diff: o autocomplete de **paciente**, na mesma tela (`receita-ui.js:251-254`, via `pacientes-ui.js:259-320`), já implementa o padrão certo — combobox, listbox, `aria-activedescendant`, setas. Quem dita/navega por teclado consegue escolher o paciente mas não o medicamento.
2. **Alvos de toque <44px reapareceram em 3 botões novos (baixo/médio).** `style.css:2699` (`.rx-remover`), `:2750` (`.doc-importar`) e `:2764` (`.rx-gestor-acoes .btn-secondary`) sobrescrevem o padding do `.btn-ghost`/`.btn-secondary` base (17px) para 4-6px, sem `min-height`. O projeto já corrigiu exatamente essa classe de problema antes (`PENDENCIAS.md`, audit `/impeccable` de 07/08) — é reintrodução, não caso novo. `.rx-remover` é usado repetidamente ao compor a receita no celular.
3. **Botão "✕ remover orientação" sem `aria-label` (baixo).** `receita-ui.js:108-109` usa só `textContent: '✕'` + `title`; o botão irmão de remover medicamento, duas linhas acima, já tem `aria-label`. O próprio código documenta a razão (`ui/modal.js:31`: "✕ sozinho é lido como multiplicação") — a correção não foi replicada aqui.
4. **Foco não é movido ao abrir o modal de revisão da importação (médio).** `importar-modelos.js`, função `revisar()` (linhas 46-107), abre overlay `role="dialog"` mas nunca chama `.focus()` — diferente do modal irmão no mesmo arquivo (`entrada.focus()` na linha 157). Usuário de teclado/leitor de tela não é levado ao diálogo novo.
5. **Folha de impressão A4 (`e1a7b0a`): sem problema encontrado.** `folha.css` tem `@media print` completo, cores da folha impressa escopadas em variáveis próprias com justificativa documentada no topo do arquivo (não é o padrão de cor solta que o projeto já teve — é exceção deliberada), e nenhuma informação depende só de cor.

---

## SUGESTÕES NOVAS

**Melhorias (3, nenhuma repete `BACKLOG.md`/`PENDENCIAS.md`):**

1. Aplicar `requireEscrita`/`anexarPlano`/`requireCota` em `server/routes/receitas.js`, no mesmo padrão de `server.js:69,72` — fecha o bypass de paywall descrito acima (prioridade alta: é custo de IA real sendo consumido fora do controle de plano).
2. Padrão ARIA combobox/listbox no autocomplete de medicamento (`receita-ui.js:118-170`), espelhando o que o autocomplete de paciente já faz em `pacientes-ui.js:259-320` — mesma tela, mesmo padrão, sem inventar solução nova.
3. Um smoke test que efetivamente sobe `server/server.js` (import + listen) na suíte — teria pego tanto o `cota.js` ausente quanto (indiretamente) o `catalogo.json` vazio; hoje nenhum teste faz isso.

**Integrações novas:** nenhuma hoje — dia foi de execução de feature já planejada (receita médica, roadmap conhecido), não de descoberta de mercado.

---

## BACKLOG (acumulado)

3 sugestões novas acrescentadas a `BACKLOG.md` nesta pasta.

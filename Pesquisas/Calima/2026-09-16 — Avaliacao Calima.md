---
title: Calima — Avaliação semanal 2026-09-16
date: 2026-09-16
area: Calima
tags: [calima, produto, auditoria]
source: routine
---

## TL;DR

- Semana recorde: **103 commits** em `main` desde o último relatório (`b3e196d`, 08/09 19:28 → `834b7fa`, 15/09) — o dobro do recorde anterior (32). Telemedicina fechou os 8 pontos abertos do `PENDENCIAS.md`, o funil de pacientes ganhou relatório até o dinheiro por médico, o plano mensal do paciente foi **DESLIGADO** (preço único R$49,90, em produção), e a agenda ganhou edição/exclusão de eventos do Google Calendar direto na tela do médico.
- **Achado novo:** o commit `d051a79` (15/09) — que abre `PUT`/`DELETE` contra a "Agenda pacientes" do Google via credencial de service account — saiu com Opus, não Fable, furando a regra do próprio `CLAUDE.md` ("qualquer mudança que toque... endpoints do proxy... variáveis de ambiente" antes de produção). É o único commit da semana tocando credencial externa que não seguiu o gate — todo o resto (inclusive commits só de doc) saiu com Fable.
- Suíte **1257/1257 verde**, rodada localmente (+336 sobre os 921 do relatório de 09/09).
- Site vivo: 200 OK, probe de hoje 00:38 BRT (fresco).
- Tema da semana (SEO/PWA): sem achado — o `SHELL_HASH` do `sw.js` foi corretamente atualizado e os 4 JS novos da agenda entraram na lista, sem repetir o bug histórico documentado no próprio arquivo.

## O que mudou na semana

103 commits, `b3e196d` (08/09 19:28) → `834b7fa` (15/09), agrupados por assunto (do mais recente):

**Agenda: folha de detalhes e edição de eventos do Google (`d051a79`/`834b7fa`, 15/09, PR #7).** Tocar num evento (do Calima ou espelhado do Google) abre uma folha com dado completo e permite editar/excluir; antes o evento não respondia ao toque. Servidor: `PUT`/`DELETE /api/eventos/gcal:<id>` (`server/routes/agenda.js:444-485`), só para o dono (`soDono`), com `If-Match`/etag contra corrida com a secretária (409 se mudou) e 503 se a integração está desligada. Código bem estruturado — ordem de recusas documentada em comentário, erro do Google separado de defeito do Calima, teste 136/136 novo (`agenda-google.test.js`). **Único problema: saiu sem o passe de risco Fable** que o `CLAUDE.md` exige para mudança em "endpoints do proxy" que tocam credencial externa (o precedente foi fixado pelo próprio relatório de 09/09: a exibição só-leitura dos eventos do Google dispensou Fable por não escrever; este commit **escreve**, e não teve o passe). A "Parte 3" segue **dormente** (env do Coolify não ligada, `PENDENCIAS.md` linha ~107) — o código de escrita já está em produção, aguardando só a env, o que não reduz a necessidade do passe.

**Plano mensal do paciente DESLIGADO, preço único R$49,90 (`941eca5`…`63eaee1`, 14/09, em produção 23:02 BRT).** Chave `PLANO_PACIENTE_ATIVO` (default off). Todos os 10 commits — inclusive os 2 só de doc/spec — saíram com Fable 5.1. Regra do `CLAUDE.md` seguida à risca; sem achado novo, já tracked `[x]` no `PENDENCIAS.md`.

**Telemedicina — 8 fixes de ponta a ponta (09/09).** Sala de espera, reconexão de socket, vínculo do link, documentos na chamada, push "está chamando você". Todos já `[x]` no `PENDENCIAS.md` com o commit correspondente; nenhum item fechado sem baixa.

**Funil de pacientes até o dinheiro, por médico (09-10).** Métrica, relatório diário e tela do médico; oito commits de correção no mesmo dia (carimbo único de desfecho, prazo único de falta). Já documentado em detalhe no `PENDENCIAS.md` ("Funil de pacientes — o que ficou aberto") com os itens que restam — não repito aqui.

**Pacientes sem ficha / adoção automática (09-10, ~25 commits).** Conta do portal criada sozinha vira paciente do médico automaticamente; ficha mostra nome/e-mail/senha do portal; escrow do paciente por admin. Documentado no `MEMORY.md` (entradas de 09-10/09-11); sem achado novo nesta revisão.

**Consistência visual + botão WhatsApp do portal (09-10/09-11).** Cosmético, tracked.

**Campanha de WhatsApp e cards de teleconsulta (09-11).** Código em produção, **dormente** (falta template aprovado na Meta + `INTERNO_SEGREDO` no Coolify). Já documentado no `MEMORY.md`.

Sem commits em `workstations/Calima/` na janela, além dos auto-syncs.

## Site vivo

Probe de **2026-09-16 00:38:27 America/Sao_Paulo** (~5h30 antes deste relatório — fresco): `/` → 200, 1,22s total, TTFB 0,96s (mais lento que os ~0,6-0,8s de semanas anteriores, mas dentro do ruído — sem série longa o suficiente para afirmar regressão); `/manifest.json`, `/sw.js`, `/js/app.js` também 200. Gzip ativo em `/css/style.css`. TLS Let's Encrypt válido até 24/10/2026. Headers seguem restritivos: CSP com `connect-src` explícito, HSTS, `X-Frame-Options: DENY`, `nosniff`, `Referrer-Policy: no-referrer`, COOP `same-origin`. Nada a apontar.

## Tema da semana — índice 3: SEO / PWA (manifest, service worker, instalabilidade)

Análise estática pelo código — sem navegador.

**Disciplina do `sw.js` correta nesta semana.** `SHELL_HASH` mudou de `d5f8022b` para `1faa179e` no mesmo commit que adicionou os 4 arquivos novos da agenda (`agenda-detalhe.js`, `agenda-detalhe-texto.js`, `agenda-form.js`, `agenda-datas.js`) à lista `SHELL` (`public/sw.js:9,38-41`) — exatamente o padrão que o próprio comentário do arquivo documenta como lição de um bug passado ("quatro commits de UI não chegaram a quem já tinha o app aberto"). Conferi os outros 22 arquivos JS novos da semana (`admin-funil.js`, `pacientes-funil.js`, `plantoes-*.js` etc.) contra a lista: **todos os que pertencem à SPA principal estão no `SHELL`**.

**Os 7 arquivos novos de `public/js/portal/*` (chamada, checkin, convite, espera, hero, push, whats) não estão em nenhum shell — por desenho, não por esquecimento.** O portal é outra SPA; seu próprio `public/portal/sw.js` não faz cache de shell de propósito (comentário explícito: "um cache aqui seria mais um lugar para o JS velho ficar preso"), só recebe push. Conferido: nenhum drift aqui.

`manifest.json` sem mudança na semana — ícones maskable presentes, `display: standalone`, `start_url: /`. Nada novo para o tema; a sugestão já aberta no `BACKLOG.md` (App Shortcuts) não é repetida.

## Sugestões novas

**Melhorias (1):**
- **Passe de risco Fable retroativo em `d051a79`** (agenda: `PUT`/`DELETE` de eventos do Google) antes de ligar `GOOGLE_SA_JSON_B64`/`GOOGLE_CALENDAR_ID` em produção — é o único commit da semana com escrita contra credencial externa que não seguiu o gate do `CLAUDE.md`. Achado detalhado na seção "O que mudou".

**Integrações (0):** nada novo esta rodada — tema da semana não foi mercado.

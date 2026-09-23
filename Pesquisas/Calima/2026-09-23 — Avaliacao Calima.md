---
title: Calima — Avaliação semanal 2026-09-23
date: 2026-09-23
area: Calima
tags: [calima, produto, auditoria]
source: routine
---

## TL;DR

- Semana dominada pela **publicação na App Store**: casca Capacitor do app iOS, exclusão de conta pelo app (exigência 5.1.1(v)), e assinatura via **RevenueCat/Apple IAP** (17 commits, 19–22/09). Todos passaram por 2–3 rodadas de "achados do passe de risco" com correções reais (sandbox liberando plano de graça, dupla cobrança Apple+Asaas, evento fora de ordem, fatura de trial nunca paga sobrevivendo à exclusão) — engenharia sólida.
- **Achado novo (governança):** nenhum dos 11 commits que tocam billing/webhook/exclusão de conta (19–22/09) tem `Co-Authored-By: Claude Fable 5.1` — todos são Opus, inclusive os que dizem "achados do passe de risco". Só o commit anterior da cadeia (`ade140c`) nomeia Fable explicitmente. É o segundo relatório seguido com esse mesmo gap (o de 16/09 já achou isso no commit `d051a79`).
- Site vivo: 200 OK, probe de hoje 00:44 BRT (fresco, dentro da janela de 24h).
- Tema da semana (Segurança/LGPD): a pendência já aberta em `PENDENCIAS.md` (22/09) sobre contas de paciente órfãs na exclusão de conta segue sem correção — não é achado novo, só confirmação de que o código ainda corresponde ao que já está rastreado.
- Sugestões novas: 1 melhoria (a de governança acima). Sem achado de mercado — tema da semana não caiu em índice 6.

## O que mudou na semana

17 commits em `calima` desde `21b32d2` (20/09), `f353464` (19/09) até `5a3a2c1` (22/09), quase todos de produção (`public/`, `server/`, `app-ios/`). Nenhum commit em `workstations/Calima/` além de auto-sync.

**Publicação na App Store — cadeia completa (19–22/09):**
- `cb36cda`/`7124e08`/`f353464` (19/09) — aba "Prontuário" unifica pacientes/atendimentos/passagens; correções de navegação.
- `21b32d2` (20/09) — card de Teleatendimento com fila em cima.
- `d938455`/`6b715a3`/`2987005` (22/09) — casca Capacitor 8 do app iOS (`app-ios/`), Team ID, versões de pacote travadas.
- `37e91c0` (22/09) — modo nativo: arquivos pela folha de compartilhar, sem SW/banner/push web.
- `98aa590`/`859f3ea`/`3b645cd` (22/09) — **exclusão de conta pelo app** (exigência App Store 5.1.1(v)): cancela assinatura do médico E do paciente no Asaas antes de apagar, conta de paciente órfã é desvinculada (não destruída), arquivos `.bin` de documentos saem do disco, trava de tentativas por conta.
- `ade140c` (22/09) — cancelamento de assinatura pelo app, mantendo o mês pago; `/privacidade` e `/termos` movidos para o domínio do app. **Este commit nomeia explicitamente "Passe de risco em Fable 5.1: 1 alto + 1 médio + baixos, todos corrigidos e reverificados."**
- `b66f975`/`97ebb09`/`16d036e`/`937de28`/`5a3a2c1` (22/09) — webhook RevenueCat + tela de venda Apple no app: fail-closed sem segredo, dedupe por evento, distinção sandbox×produção (`REVENUECAT_SANDBOX_OK`), evento fora de ordem descartado por carimbo, TRANSFER libera/corta os dois lados, cancela Asaas se o médico assinar pela Apple com o site ainda cobrando.

Contexto de negócio (não é achado de segurança): o v1 do IAP vende **um único produto** (`br.med.calima.assinatura.mensal`, R$49,90 "libera tudo") — os 4 degraus do site (Teste/Acadêmico/Recém-formado/Hipócrates) não têm equivalente no app iOS ainda. Isso é escolha deliberada documentada no código (`server/lib/apple-assinatura.js`), não um bug.

## Site vivo

Probe de **2026-09-23 00:44:11 America/Sao_Paulo** (fresco): `/` → 200, 1,27s total, TTFB 0,47s; `/manifest.json`, `/sw.js`, `/js/app.js` também 200. Gzip ativo em `/css/style.css`. TLS Let's Encrypt válido até 24/10/2026. Headers seguem restritivos: CSP com `connect-src` explícito, HSTS, `X-Frame-Options: DENY`, `nosniff`, `Referrer-Policy: no-referrer`, COOP `same-origin`. Nada a apontar.

## Tema da semana — índice 2: Segurança e LGPD

A semana já entregou, por conta própria, exatamente o que este tema cobriria — três rodadas de passe de risco sobre exclusão de conta e billing (ver "O que mudou"). Em vez de reencontrar o que já foi corrigido, o foco aqui é (1) checar se ficou algo residual e (2) o processo, não o código.

**Residual, já rastreado (não é achado novo):** `PENDENCIAS.md` linha ~3–10, aberta no mesmo dia 22/09, registra que contas de paciente órfãs (desvinculadas na exclusão do médico) não têm caminho de autoexclusão — confirmei por `grep` que não existe rota `excluir`/`apagar` para a própria conta do paciente em `server/routes/portal*.js` nem chamada correspondente em `public/js/portal/`. É exigência de verdade só se o portal do paciente virar app na App Store; hoje seria mais rigor de LGPD do que obrigação regulatória, mas cresce em urgência se a Apple perguntar sobre a conta do "usuário final" que não é o comprador.

**Webhook RevenueCat, revisado por leitura direta do código atual (`server/lib/apple-assinatura.js`, `server/routes/billing.js`):** segredo comparado com `strEqSeguro` (mesmo helper de tempo constante usado no webhook de convites), fail-closed sem `REVENUECAT_WEBHOOK_SECRET`, dedupe por `billing_events`, evento de sandbox recusado por padrão. Nada a apontar — já bem coberto pelas 3 rodadas do próprio passe de risco.

**Achado de governança:** o `CLAUDE.md` da workstation exige passe de risco em **Fable 5.1** (não Opus) antes de produção para qualquer mudança em auth, cripto, persistência de `records` ou endpoints do proxy — e billing/exclusão de conta batem em todos esses pontos. Dos 17 commits da semana, só `ade140c` credita Fable explicitamente no corpo da mensagem. Os 11 commits seguintes que tocam billing/webhook/conta (`b66f975`, `97ebb09`, `16d036e`, `937de28`, `98aa590`, `859f3ea`, `3b645cd`, entre outros) são todos `Co-Authored-By: Claude Opus 5 (1M context)`, inclusive dois cujo próprio texto diz "achados do passe de risco" sem nomear quem revisou. Isso não prova que o gate foi pulado — pode ser que Fable tenha rodado como subagente de revisão e Opus só tenha implementado as correções, o que é compatível com a regra — mas a mensagem de commit não deixa isso registrado, ao contrário de `ade140c`. É o mesmo tipo de lacuna que o relatório de 16/09 achou no commit `d051a79` (também sem Fable citado, também mexendo em credencial externa). Duas semanas seguidas com o mesmo padrão de mensagem incompleta sugere que vale ou (a) nomear Fable explicitamente no commit quando o passe rodar, ou (b) revisar se o passe está mesmo rodando em Fable consistentemente.

## Sugestões novas

**Melhorias (1):**
- **Nomear a revisão no commit.** Quando o passe de risco Fable 5.1 rodar antes do deploy (regra do `CLAUDE.md`), citar isso explicitamente no corpo do commit (como `ade140c` fez) — mesmo quando quem implementa a correção é Opus. Sem isso, do lado de fora (git log) não dá para distinguir "passe rodou e passou" de "passe não rodou". Achado de processo, não de código: nenhuma linha para mudar, só o hábito de mensagem.

**Integrações (0):** nada novo esta rodada — tema da semana não foi mercado.

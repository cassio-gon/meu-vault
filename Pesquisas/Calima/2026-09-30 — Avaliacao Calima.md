---
title: Calima — Avaliação semanal 2026-09-30
date: 2026-09-30
area: Calima
tags: [calima, produto, auditoria]
source: routine
---

## TL;DR

- **Mudança de modelo de negócio:** desde 24/09 o Calima vendeu a escada de 3 planos (Acadêmico/Recém-formado/Hipócrates) e virou **preço único, R$ 49,90 (Hipócrates), site e App Store** (`server/lib/planos.js`: `VENDAVEIS = ['staff']`). A descrição de monetização desta rotina (4 degraus) **não bate mais com o código — o código vence.** Assinantes antigos ficam no preço de legado (grandfathering confirmado).
- Também na semana: portal do paciente perdeu o "plano mensal" (agora é pagamento único por consulta + retorno grátis em 7 dias), nova grade de agenda de fim de semana em produção, EULA resolvido e app **reenviado à Apple em 28/09** (2ª rodada), e um incidente real fora do código: cliente removido do Asaas apagou a assinatura de uma médica sem avisar o app (lição registrada no `MEMORY.md`).
- Tema da semana (índice 1 — **Acessibilidade**): 1 achado novo confirmado no código atual — modal de revisão de importação de modelos abre **sem mover o foco** (`public/js/importar-modelos.js:46-107`), enquanto todo modal irmão do app move. É reincidência de um achado de 13/08 que nunca entrou no `BACKLOG.md`. Alvos de toque <44px do mesmo achado de 13/08 também continuam abertos. O `aria-label` que faltava naquele achado **já foi corrigido**.
- Site vivo: 200 OK, probe de hoje 01:16 BRT, fresco.
- Sugestões novas: 2 melhorias (achados de acessibilidade acima). Sem achado de mercado — tema da semana não caiu em índice 6.

## O que mudou na semana

10 commits em `calima`, `3487b39` (24/09) → `b7e2cd8` (27/09). Tudo em produção (`public/`, `server/`), nenhum de doc/auto-sync.

**Preço único — só o Hipócrates, R$ 49,90 (`9ffc113`, 24/09).** A escada de 3 planos (Acadêmico R$19,90/Recém-formado R$39,90/Hipócrates R$79,90) some da venda: `PAGOS = ['academico','recem','staff']` (quem já está, inclusive descontinuado) separa de `VENDAVEIS = ['staff']` (quem pode entrar hoje). Ninguém é rebaixado; assinante antigo migra para o Hipócrates e pode desfazer. O próprio commit lista 6 achados de passe de risco corrigidos no ato: retry de `/subscribe` que devolvia fatura do plano errado, e-mail de fim de trial que ainda prometia "a partir de R$19,90", `/config` anunciando preço de entrada errado, onboarding descrevendo 3 planos, rótulo cru "Plano academico" sem `plano_rotulos`, e o card único da vitrine sem destaque. **Isto substitui a descrição de monetização desta rotina — ver TL;DR.**
- `f52f405` (24/09) — isenção (cortesia) passou a entregar o produto inteiro (Hipócrates), não mais o Acadêmico — coerente com a mudança acima.
- `aeff6ff` (25/09) — o prêmio de indicação prometia "permanente"; o servidor concede 30 dias. Achado ao revisar captura para a App Store; texto da tela e do e-mail de boas-vindas corrigidos.

**Portal do paciente perde o "plano mensal" (`b6da856`, 24/09, -1666/+287 linhas).** Cada consulta passa a ser pagamento único (R$49,90); o único agendamento grátis é o retorno em até 7 dias após uma consulta realizada. Refactor limpo: aba "Meu plano" sai do HTML, CSS e JS por completo (sem botão órfão nem CSS morto — conferido por grep), rota `GET /plano` vira `GET /oferta`, `lib/plano-paciente.js` vira `lib/agenda-paciente.js`. Indicadores de assinante/pagamento pendente saem do admin. Sem achado — refactor bem executado.
- `bdab6c0`/`3487b39` (24/09) — antes do refactor acima: retorno grátis de 7 dias e correção do horizonte de agendamento (90 dias, não 14).
- `5c680a5` (24/09) — consulta do portal na agenda do médico volta a mostrar o nome do paciente (regressão corrigida no mesmo dia).
- `7245354` (24/09) — CRM com espaço/prefixo/UF colada no campo não derruba mais o cadastro.

**Nova grade de agenda de fim de semana (`b7e2cd8`, 27/09, em produção desde 29/09).** Sábado só 20h/21h/22h, domingo 9h–16h em hora cheia; segunda a sexta sem mudança. `ABRE_POR_DIA`/`HORA_FECHA` virou `HORARIOS_POR_DIA` (lista de horários de início por dia, não mais intervalo corrido). Suíte 1450/1450 (declarado no commit — não reexecutei aqui, sandbox sem `node_modules`). Publicado pelo Redeploy manual do Coolho — ver nota de processo abaixo.
- `b2691df` (24/09) — `/suporte` redireciona para a página de suporte.

**Fora do código, registrado no `MEMORY.md` da workstation (não é achado de código, mas afeta o mesmo período):** conta do GitHub liberada em 29/09 (bloqueada como spam de 25 a 29/09, sem causa informada pelo suporte); Guideline 3.1.2 da Apple (faltava link do EULA na descrição) resolvida só com metadado, app reenviado 28/09 03h49, aguardando revisão; e um incidente de produção — o cliente de uma médica foi removido do Asaas em 15/09 (provável limpeza de teste), o que apagou a assinatura sem que o app soubesse (só chega `PAYMENT_DELETED`), corrigido manualmente em 29/09 via SSH+`docker exec`. Lição já registrada pelo próprio Cássio: conferir `users.asaas_customer_id` antes de limpar clientes de teste no painel.

## Site vivo

Probe de **2026-09-30 01:16:02 America/Sao_Paulo** (~8h antes deste relatório — fresco): `/` → 200, 0,12s total, TTFB 0,09s (mais rápido que as últimas semanas); `/manifest.json`, `/sw.js`, `/js/app.js` também 200. Gzip ativo em `/css/style.css`. TLS Let's Encrypt válido até 22/12/2026. Headers seguem restritivos: CSP com `connect-src` explícito, HSTS, `X-Frame-Options: DENY`, `nosniff`, `Referrer-Policy: no-referrer`, COOP `same-origin`. Nada a apontar.

## Tema da semana — índice 1: Acessibilidade

Ciclo já tinha passado por este índice uma vez, em 13/08 (não está nos 3 relatórios mais recentes nem no `BACKLOG.md`, então os achados de lá não contam como repetição — só 1 dos 4 daquela rodada chegou a entrar na tabela). Reverifiquei o código atual dos 4 achados de 13/08 antes de procurar achado novo, para não noticiar como "novo" o que já foi corrigido nem deixar de fechar o que foi.

**Status dos 4 achados de 13/08, no código de hoje:**
1. Autocomplete de medicamento sem padrão ARIA combobox (`public/js/receita-ui.js:134-172`) — **ainda aberto**, já rastreado no `BACKLOG.md` (13/08). Sem mudança nesta rodada.
2. Alvos de toque <44px (`public/css/style.css:4455` `.rx-remover`, `:4646` `.doc-importar`, `:4660` `.rx-gestor-acoes .btn-secondary`, todos com `min-height: auto`) — **ainda aberto**, nunca entrou no `BACKLOG.md`. Reporto como sugestão nova abaixo.
3. Botão "✕ remover orientação" sem `aria-label` — **corrigido.** `receita-ui.js:118` já tem `remover.setAttribute('aria-label', 'Remover orientação')`. Não era rastreado no `BACKLOG.md` (nada para marcar "feito" lá).
4. Foco não movido ao abrir o modal de revisão da importação — **ainda aberto**, nunca entrou no `BACKLOG.md`. Detalhe abaixo (é o achado novo desta semana).

**Achado novo — foco não movido no modal de revisão de importação de modelos.** `public/js/importar-modelos.js:46-107`, função `revisar()`: abre via `abrirOverlay('importar-revisao-modal', ...)`, define `aria-label` no card (linha 47), mas nunca chama `.focus()` em nada dentro dele. Confirmei em `public/js/ui/modal.js:38-119` que `abrirOverlay` só monta o DOM, prende o Tab dentro do card e devolve o foco ao fechar (`focaveis`/`onKeydown`) — **mover o foco de entrada é responsabilidade de quem chama**, e cada chamador cuida disso: a etapa 1 do mesmo fluxo (`abrirImportarModelos`, linha 157: `entrada.focus()`), o diálogo de planos (`billing-ui.js`: `h2.setAttribute('tabindex','-1'); h2.focus()`), a confirmação genérica (`confirmarAcao`, foco no Cancelar em ação perigosa). A etapa 2 — a revisão com checkboxes, que é onde o médico decide o que salvar — é a única do fluxo que fica de fora. Quem navega por teclado ou leitor de tela permanece com o foco em `document.body` quando o modal abre, e precisa "procurar" o diálogo que já está na tela. Achado de 13/08, ainda presente 48 dias depois, sem ter entrado no `BACKLOG.md` até agora.
- **Conserto sugerido:** `h2.setAttribute('tabindex', '-1'); h2.focus({ preventScroll: true });` logo após `card.append(...)` em `revisar()` — mesmo padrão já usado em `billing-ui.js`.

## Sugestões novas

**Melhorias (2):**
- **Bug** — Mover o foco ao abrir o modal de revisão da importação de modelos (`public/js/importar-modelos.js:46-107`, função `revisar()`) — achado desta semana, detalhe acima.
- Restaurar `min-height` nos alvos de toque reduzidos a <44px: `public/css/style.css:4455` (`.rx-remover`), `:4646` (`.doc-importar`), `:4660` (`.rx-gestor-acoes .btn-secondary`) — achado de 13/08, ainda aberto, nunca tinha entrado no `BACKLOG.md`.

**Integrações (0):** nada novo esta rodada — tema da semana não foi mercado.

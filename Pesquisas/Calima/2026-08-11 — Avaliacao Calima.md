---
title: Avaliação Calima — 2026-08-11
date: 2026-08-11
area: Calima
tags: [calima, produto, auditoria]
source: routine
---

# Calima — Avaliação diária (2026-08-11)

## TL;DR

- **Sem commits em `prontuario-ia` nas últimas 24h** — nada para revisar como diff do dia.
- **Site vivo:** probe do Mac fresco (03:48 BRT, ~2h20 antes desta execução) — `/` 200 em 0,61s, TLS válido até 24/10, gzip confirmado. Sem sinal de problema.
- Tema de hoje (índice 7 do ciclo): **monetização e conversão**. Achado mais relevante: quando um pagamento vence (`PAYMENT_OVERDUE`), o app só avisa o **admin** — o **cliente nunca recebe e-mail automático** cobrando a fatura em aberto (`server/routes/billing.js:153-158`).
- Também achado: preço (R$ 19,90) e duração do trial (7 dias) **não aparecem em nenhum texto antes do cadastro** — só depois, no banner ou no paywall.
- 3 melhorias + 2 integrações novas, nenhuma repete `BACKLOG.md` nem `PENDENCIAS.md` — ver seção própria.

---

## O QUE MUDOU EM 24H

```
git -C prontuario-ia log --since="24 hours ago" ...   → vazio
git -C claude-config log --since="24 hours ago" -- workstations/Calima/  → só e1d60e1 "auto-sync" (sem conteúdo de produto)
```

Sem mudanças em 24h no código do app. Sem diff para revisar hoje.

---

## SITE VIVO

Probe do Mac em **2026-08-11 03:48:41 America/Sao_Paulo** (06:48:39 UTC), lido de `Pesquisas/Calima/_probe-site.md` — **fresco**, ~2h20 antes desta execução (09:07 UTC).

- `/` → 200, 0,610s total, TTFB 0,472s, 21.630 B.
- `/manifest.json`, `/sw.js`, `/js/app.js` → todos 200.
- Compressão: `content-encoding: gzip` confirmado em `/css/style.css` — segue válido o fechamento de 10/08 (a sugestão de compressão HTTP foi marcada "improcedente" no `BACKLOG.md`, o Traefik/Coolify já comprime na borda).
- TLS: Let's Encrypt, válido até 24/10/2026.
- Headers de segurança presentes: CSP, HSTS, X-Frame-Options DENY, COOP same-origin, X-Content-Type-Options nosniff.

Nada a reportar aqui — site saudável.

---

## TEMA DO DIA — índice 7 — Monetização e conversão

Trial de 7 dias (`server/lib/env.js:114`, `TRIAL_DIAS`) → paywall bloqueia só escrita (leitura/export livres, `server/lib/billing.js:22-23`) → assinatura R$ 19,90/mês via Asaas (`server/lib/env.js:138`, `PLAN_PRICE_CENTS`), Pix ou cartão, cobrança mensal fixa (`server/routes/billing.js:69`, `cycle: 'MONTHLY'` hardcoded). Já existem 2 e-mails de lembrete de trial (`server/lib/lembretes.js`: 2 dias antes de vencer, e no dia em que vence) e programa de indicação (1 mês grátis por indicação, já auditado em relatórios anteriores).

**1. Cobrança em atraso avisa só o admin, nunca o cliente** (`server/routes/billing.js:153-158`, `server.js:86`). O webhook `PAYMENT_OVERDUE` roda `avisar('⚠️ Calima: pagamento atrasado', ...)`, e `avisar` chama `notificarAdmin` — que é o e-mail do **Cássio**, não do assinante. Não há nenhum `enviar({ para: u.billing_email, ... })` no caminho de atraso (comparado com `lembretes.js`, que faz isso para o trial). Resultado: se um cartão expira ou um Pix não é pago, o único jeito de o médico saber é o Cássio ver o aviso e mandar mensagem manual — ou o próprio Asaas notificar via canal próprio (não verificado aqui; depende de configuração no painel Asaas, fora do que o código do repo controla).

**2. Preço e duração do trial não aparecem antes do cadastro.** Busquei `"7 dias"`, `"teste grátis"`, `"R$"` e `trial` em `public/js/onboarding.js` e `public/js/auth-ui.js` (tela "Criar conta", linha 174) — nenhuma ocorrência. O médico só descobre que é um teste de 7 dias pelo banner pós-login (`billing-ui.js:82-88`) ou, na pior hipótese, quando o paywall interrompe (`billing-ui.js:107-129`). Não é enganoso (o app é claro depois), mas é conversão deixada na mesa: quem sabe do preço antes de digitar dados costuma converter melhor do que quem é surpreendido.

**3. Cancelamento é 100% manual pelo admin** (`server/routes/billing.js:101-113`, `assinatura-ui.js:50`: "Para cancelar a assinatura, fale com o administrador."). Documentado como decisão consciente do MVP, mas vale registrar como fricção que não escala — hoje com poucos assinantes é tratável a mão; cresce, vira gargalo. **Não verifiquei** se alguma norma brasileira de cancelamento fácil (o tema circula em torno do Decreto 11.150/2022 e normas de PROCON/Senacon para assinatura recorrente online) se aplica a um SaaS médico como o Calima — não é da minha alçada afirmar enquadramento legal; deixo registrado para o Cássio avaliar com quem entende de direito do consumidor, não como achado de compliance confirmado.

**4. Ciclo de cobrança hardcoded em `MONTHLY`**, mas a lib já aceita qualquer `cycle` (`server/lib/asaas.js:40-41`, parâmetro genérico passado direto ao Asaas). Não é bug, é oportunidade barata — ver sugestão abaixo.

---

## SUGESTÕES NOVAS

**Melhorias (3):**

1. **E-mail de cobrança ao próprio cliente quando `PAYMENT_OVERDUE`** — hoje só o admin é avisado (`billing.js:153-158`). Reusar o padrão de `lembretes.js` (mensagem pt-BR, `enviar({ para: u.billing_email, ... })`) no handler do webhook. Recupera assinante que só esqueceu de atualizar o cartão, sem depender do Cássio ver o aviso a tempo.
2. **Mostrar preço e duração do trial na tela "Criar conta"** (`public/js/auth-ui.js:174`) — uma linha ("7 dias grátis, depois R$ 19,90/mês") antes do botão. Reduz surpresa, tende a melhorar conversão de quem chega decidido.
3. **Plano anual com desconto**, usando o parâmetro `cycle` que a lib do Asaas já aceita (`server/lib/asaas.js:40-41`) — hoje `billing.js:69` fixa `'MONTHLY'`. Custo de implementação baixo (é trocar o valor de um campo + UI de escolha no `formAssinar`), efeito real em churn mensal e caixa antecipado.

**Integrações novas (2):**

1. **Notificação de cobrança via WhatsApp/SMS do próprio Asaas** (recurso nativo do provedor, configurável no painel — não exige código novo) — complementa o e-mail de atraso (sugestão 1 acima) com um canal de taxa de abertura mais alta para médico em plantão, que costuma não checar e-mail com a mesma frequência que o WhatsApp.
2. **Link de pagamento recorrente por WhatsApp no fim do trial** — em vez de só o link no e-mail `TEXTOS.fim` (`lembretes.js:29-40`), oferecer opção de receber o link de assinatura pelo WhatsApp do médico (já coletado no cadastro como telefone de perfil, `nome_completo`/`telefone` em `users`, ver `MEMORY.md` de 2026-07-16) — mesmo racional de canal de maior abertura.

---

## BACKLOG (acumulado)

5 sugestões novas acrescentadas a `BACKLOG.md` nesta pasta.

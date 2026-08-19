---
title: Calima — Avaliação semanal 2026-08-19
date: 2026-08-19
area: Calima
tags: [calima, produto, auditoria]
source: routine
---

## TL;DR

- Semana de altíssima atividade (~50 commits, 14→19/08): escada de indicação virou permanente (5 colegas → Recém-formado, 15 → Hipócrates), isento sem admin virou "Acadêmico de cortesia", e foram ao ar a campanha de e-mail aos cadastrados e o e-mail de boas-vindas automático no cadastro.
- **Achado real (tema: Monetização):** a trava de "uma conta por e-mail" (`8cb8fc1`, `server/lib/cadastro.js:17-21`) só normaliza maiúsculas/minúsculas — não cobre alias Gmail (`joao+1@gmail.com`). Isso abre uma via de farming na escada de indicação, que conta qualquer cadastro pelo link sem exigir uso real do app (`server/lib/premio-indicacao.js:64-66`) — risco que o próprio commit já registra como conhecido (comentário "ponytail" na linha 59-62), mas sem trava.
- **Bug real:** `scripts/campanha-email/boasvindas-todos.mjs` (`78870c9`) não filtra por data de cadastro nem marca quem já recebeu o boas-vindas — rodá-lo depois que o e-mail automático (`9b465ff`) já está no ar duplica o disparo para quem se cadastrou no meio-tempo, e rodá-lo duas vezes reenvia a todos.
- Regressão introduzida e corrigida no mesmo dia, no redesign do login mobile: `7b7d31e`/`d81b381` deixaram "Criar conta" inacessível sem rolagem em landscape; `98bf36f`, horas depois, corrigiu. Estado atual do repo está limpo.
- Site vivo: 200 OK, probe de 18/08 22h BRT (~8h antes deste relatório, fresco), headers de segurança completos, TLS válido até 24/10.

## O que mudou na semana

Janela usada: commits de código de produção desde a última avaliação (14/08) até hoje — `git -C calima log --since="2026-08-14"`. Volume alto o suficiente para agrupar por assunto em vez de listar commit a commit.

**Monetização/indicação (foco desta semana):** `acc7c0a` (isento não-admin passa a ser Acadêmico de cortesia, com cota diária, não mais Staff irrestrito), `4b00ea5`+`9dd23f6` (escada de indicação v2: convidado ganha Acadêmico por 30 dias; indicador fecha em Recém-formado permanente com 5 colegas, Hipócrates com 15 — fonte única `ESCADA_PREMIO`), `9aeeca4` (deep link `?assinar=<plano>` abre o diálogo direto, plugado nos CTAs da campanha), `8cb8fc1` (confirmação de senha + uma conta por e-mail). Ver tema abaixo.

**Campanha de e-mail e ativação:** `82d4046`…`0a09b7c` (campanha aos cadastrados via Resend, com rótulos de marca por plano e exclusão de isentos/cobaias por padrão) e `9b465ff`/`a7d6a4c`/`963f224`/`78870c9` (e-mail de boas-vindas automático no cadastro + disparo único para a base antiga). Nenhum dos dois scripts grava estado de envio — são operações manuais sem dedupe persistido.

**Histórico do paciente na ficha** (`1f3d917` e a cadeia `c126601`…`da37733`, 16/08, em produção como v110): a ficha do paciente passa a mostrar atendimentos anteriores; corrigido também o bug de todo card de "hoje" abrir o Histórico genérico em vez do atendimento certo. Já registrado no `PENDENCIAS.md`.

**Exportação Word + auditoria a11y** (`165db4d`, `0902221`, 18/08): `.docx` nativo ao lado do PDF — fecha parte do item de Fase 2 do roadmap (ainda faltam sync celular↔notebook e template por especialidade). O próprio dia corrigiu, no `0902221`, um bug do PDF/Word introduzido horas antes: a blob URL era revogada antes do `<a>` entrar no DOM, travando o download no Safari/iOS.

**Redesign do login mobile** (`7b7d31e`, `d81b381`, `98bf36f`, 18/08) e **container sem root** (`9f3af8a`, `Dockerfile`/`docker-entrypoint.sh` — `setpriv` faz o drop root→node depois do `chown` do volume; sem achado).

Nenhum commit da semana tocou `routes/billing.js:100-123` (troca de plano sem trava), o webhook não-atômico do Asaas ou `lib/env.js:152-160` (preços sem validação) — essas pendências seguem exatamente como estavam.

## Site vivo

Probe medido em **2026-08-18 22:00:08 America/Sao_Paulo** (~8h antes deste relatório, dentro da janela — fresco): `/` → 200, 0,69s total, TTFB 0,53s, 28.760 B; gzip ativo em `/css/style.css`; TLS Let's Encrypt válido até 24/10/2026; headers de `/` com CSP restritiva, HSTS, `X-Frame-Options: DENY`, `X-Content-Type-Options: nosniff`, `Referrer-Policy: no-referrer`, `Cross-Origin-Opener-Policy: same-origin`. Nada a apontar.

## Tema da semana — índice 7: Monetização e conversão

**1. Trava de "uma conta por e-mail" não cobre alias — alimenta farming na escada de indicação**

`server/lib/cadastro.js:17-21` (`emailEmUso`) compara `lower(billing_email)`, reforçado por índice único `lower(billing_email)` em `server/lib/db.js`. Cobre maiúsc/minúsc, não cobre `joao+1@gmail.com` vs `joao@gmail.com` (Gmail ignora tudo após `+`) nem variações de ponto no Gmail. Isso interage diretamente com `server/lib/premio-indicacao.js:64-66` (`contarIndicacoesValidas`): qualquer cadastro pelo link de indicação conta, sem exigir que o convidado use o app — e desde `9dd23f6`, 5 indicações valem Recém-formado **permanente**, 15 valem Hipócrates **permanente**. Um médico com paciência para criar 5 e-mails-alias próprios sobe de plano sem indicar ninguém de verdade. O próprio código já nomeia o risco (comentário linha 59-62), mas não há mitigação além da trava de e-mail exato — que, como descrito, não fecha esse caso. Rate-limit de cadastro pode reduzir a superfície, mas não foi verificado neste ciclo.

**2. Disparo de boas-vindas em massa sem controle de dedupe**

`scripts/campanha-email/boasvindas-todos.mjs:27-40` foi criado (`78870c9`) para cobrir quem se cadastrou antes do e-mail automático (`9b465ff`) existir, mas a query de destinatários não filtra por `criado_em` nem existe coluna de "já recebeu" em `users` (`server/lib/db.js`). Rodar o script depois do deploy do automático duplica o e-mail para quem se cadastrou no intervalo; rodar `--enviar` duas vezes reenvia a todos. É um script manual, então o risco depende de disciplina operacional — mas o código não impõe a garantia que o próprio comentário do script promete.

**3. Deep link `?assinar=` e novo desconto de isento estão coerentes com o funil existente**

`9aeeca4` só abre o diálogo de assinatura após login (`app.js:1108-1120`, dentro de `entrarNoApp()`) — sem exposição a deslogado. `acc7c0a` cria fricção real (cota diária) para isentos não-admin converterem, sem tocar em admin. Nenhum dos dois introduz brecha nova.

## Layout/UX e Funções

Sem gap novo fora do já rastreado em `PENDENCIAS.md`. Fase 2 do roadmap avançou (export Word, ficha com histórico); seguem pendentes sync celular↔notebook e template por especialidade.

## Sugestões novas

**Melhorias (2):**
1. Normalizar alias de e-mail (Gmail `+tag`/pontos, no mínimo) antes de gravar `billing_email` em `cadastro.js`/`billing.js`/`perfil.js` — fecha a via de farming descrita acima na escada de indicação, sem exigir mudar a lógica de prêmio.
2. Coluna `boas_vindas_enviado_em` em `users`, checada tanto no disparo automático (`routes/auth.js`) quanto em `boasvindas-todos.mjs` — elimina o duplo envio possível hoje entre os dois caminhos.

**Integrações (0):** nada novo esta semana que já não esteja no backlog.


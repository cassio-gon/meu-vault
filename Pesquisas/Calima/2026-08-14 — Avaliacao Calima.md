---
title: Calima — Avaliação diária 2026-08-14
date: 2026-08-14
area: Calima
tags: [calima, produto, auditoria]
source: routine
---

## TL;DR

- Dia de altíssima atividade: **28 commits em 24h**, dois críticos da auditoria ruflo fechados (`d716159`: prontuário 100% vazio saía com HTTP 200 e cota debitada; `b93dca6`: importação de modelos quebrava em pad grande).
- **Achado do dia (tema: Segurança e LGPD):** a **OpenAI (gpt-5.6 "Luna") entrou hoje como 4º processador de dado clínico** — formata os 3 planos pagos (`27b5d97`) e a importação de modelos do dontpad (`b93dca6`). O texto que ela recebe já passa pelo `scrubName` (mesma anonimização de sempre), mas é um novo terceiro que processa texto clínico e não está coberto pela pendência existente "Buraco do áudio/LGPD" (que é só sobre o Groq/áudio).
- `server/lib/openai.js` — cérebro de todos os pagos, criado hoje — segue com **zero teste unitário direto** (só coberto indiretamente por `cota-rotas`/`planos`/`receitas`).
- Site vivo: 200 OK, TLS válido, todos os headers de segurança presentes (probe de 14/08 02:36 UTC — fresco). Nada a reportar.
- Nenhuma das pendências críticas já rastreadas (`8mb` antes do `requireAuth`, `prescricao_modelos.nome` em claro, exclusão de conta órfã, preços sem validação, cadeia IA vs timeout do proxy) foi tocada pelos commits de hoje — seguem abertas exatamente como estavam.

## O que mudou em 24h

28 commits, todos de 13/08 (`git log --since="24 hours ago"`). Agrupando por assunto:

**Auditoria ruflo (3 commits, os mais relevantes tecnicamente):**
- `d716159` — dois críticos: (1) `formatador.js` agora trata "todos os campos vazios" como falha do provedor (`ErroProvedor` 502, fora do `comRetry`) e desce pro reserva — antes um JSON bem-formado mas vazio (llama/OpenRouter sem schema) virava sucesso e debitava cota por um prontuário em branco; (2) `receita-estado.js` novo: reabrir a tela de receita não zera mais a prescrição em composição, com confirmação só ao trocar de paciente.
- `b93dca6` — importação de modelos do dontpad muda de Claude Sonnet para Luna (OpenAI), com reserva Claude. Fecha um alto real: sem `max_tokens`, pad de 40k chars não trunca mais em 4096 (o teto do reserva Claude subiu para 16384). Ver achado de segurança abaixo.
- `8b1ed14` — prompt de sugestão de CID restringe ao CID-10 do Brasil (não é achado de segurança, é qualidade clínica).

**Novo cérebro OpenAI para planos pagos:** `27b5d97` cria `server/lib/openai.js` e pluga "openai" na cadeia (`ia.js`); `702b2f4`, `16fa8b0`, `552e0f8`, `d772909` são os ajustes de copy/UI dos cards de planos em cima disso.

**UI/onboarding/tabbar (maioria dos commits, sem risco de segurança):** `fddef6d`, `c734769`, `93bf05e`, `a6ccac5`, `7a2168b`, `adb979c`, `27f2ad5` (revert do mesmo dia), `af63d13`, `fd73973`, `76731c8`. Ida-e-volta notável: `adb979c` tirou Agenda/Passagens da tabbar no celular e `27f2ad5`, no mesmo dia, trouxe de volta — já registrado no `PENDENCIAS.md` (Cássio pediu de volta por voz).

**Receita como documento/segunda via:** `f0617e0`, `eaa979c`, `9f71342`, `44c2c97`, `c0829d2` — receita abre como PDF nativo, com confirmação e histórico. Sem implicação de segurança nova.

**Design tokens:** `554df22` — 45 tamanhos de fonte/20 raios viram 8+8 tokens; já coberto no `PENDENCIAS.md` (concluído).

**Critique P1 (`678eeb2`):** os 4 P1 da critique de 13/08, já fechados e registrados no `PENDENCIAS.md`.

**Docs:** `2e0fd28` — guia da Play Store revisado + spec da assinatura VIDaaS (fora do escopo de segurança de hoje).

Nenhum desses commits tocou `server.js`, `routes/admin.js`, `lib/cota.js` ou `lib/env.js` (preços) — as pendências críticas de segurança já conhecidas continuam intocadas.

## Site vivo

Probe medido em **2026-08-14 02:36:17 UTC** (fresco, dentro da janela de 24h) — `_probe-site.md`:

- `/` → 200, 0.84s total, TTFB 0.65s, 27.203 B, gzip ativo em `/css/style.css`.
- TLS Let's Encrypt válido até 24/10/2026.
- Headers de `/`: CSP restritiva (`default-src 'self'`, sem `unsafe-inline`), HSTS (`max-age=15552000`), `X-Frame-Options: DENY`, `X-Content-Type-Options: nosniff`, `Referrer-Policy: no-referrer`, `Cross-Origin-Opener-Policy: same-origin`. Conjunto completo, nada a apontar.

## Tema do dia — índice 2: Segurança e LGPD

**1. Novo subprocessador de dado clínico: OpenAI ("Luna", gpt-5.6)**

Antes de hoje, texto do médico (transcrição, já sem nome — `public/js/anonymize.js:9-26`, `scrubName`) ia para Gemini, Llama (via provedor próprio) e OpenRouter, todos citados em `env.js`. Hoje, dois fluxos passaram a usar a OpenAI:

- `server/lib/openai.js:1-89` (novo) — formatador dos 3 planos pagos (Acadêmico/Recém-formado/Hipócrates), plugado em `server/lib/ia.js:5,18-31`. Recebe o `transcript` já anonimizado (mesmo pipeline de antes — o `format.js:44-48` não mudou a origem do texto).
- `server/lib/importar-prescricoes.js:143-172` (reescrito) — importação de modelos do dontpad, que **não** é dado de paciente (é texto de prescrição-modelo por comorbidade, sem nome), mas ainda é dado clínico proprietário do médico saindo para um quarto provedor.

Ambos são dormentes sem `OPENAI_API_KEY` (fail-soft confirmado no código) e o commit `b93dca6` até comenta no próprio corpo: *"trocar de provedor sem querer é mandar dado clínico do médico para outra empresa"* — ou seja, o risco já está no radar de quem escreveu o commit. O que falta é o registro formal: a pendência existente "Buraco do áudio / LGPD" (`PENDENCIAS.md`) fala especificamente do ÁUDIO indo para o Groq — não cobre texto clínico indo para a OpenAI. Vale abrir isso como item **separado** no `PENDENCIAS.md` (não faço a edição aqui — é read-only neste ambiente): a política de privacidade (repo `prontuario-ia-landing`, fora do escopo desta rotina) provavelmente também precisa listar a OpenAI como subprocessador, junto do Groq.

**2. `server/lib/openai.js` sem teste unitário direto**

Confirmado por grep: nenhum arquivo em `tests/` importa `lib/openai.js` diretamente. A cobertura vem só de rotas que passam por ele indiretamente (`cota-rotas.test.js`, `planos.test.js`, `receitas.test.js`). Esse gap já está no `PENDENCIAS.md` ("`server/lib/openai.js` com ZERO cobertura — é o formatador de todos os planos pagos") — só registro aqui que ele não foi fechado hoje, apesar de o arquivo ter sido tocado por dois commits (`27b5d97`, e indiretamente `b93dca6` que criou um segundo caminho para a mesma API). Sem teste de unidade, uma mudança de shape na resposta da OpenAI (ex.: `choices[0].message.content` vazio, ou erro 400 por `temperature` — já documentado como pegadinha no próprio código, `openai.js:10-11`) só aparece em produção.

**3. Nada regrediu nos headers/CSP/isolamento** — confirmado pelo probe (seção acima) e por não haver commit tocando `server.js` ou middlewares de segurança hoje.

## Sugestões novas

**Melhorias (2):**
1. Teste unitário dedicado para `server/lib/openai.js` (`formatar`: sucesso com schema estrito, HTTP não-200, resposta sem `choices[0].message.content`, timeout de 30s) — espelhando o padrão já usado para `gemini.js`/`llama.js`/`openrouter.js`. Motivo: é o formatador de 3 dos 4 planos e hoje só tem cobertura indireta.
2. Registrar a OpenAI como subprocessador na documentação de privacidade (fora deste repo) e, no `PENDENCIAS.md`, abrir item específico separado de "Buraco do áudio" — hoje o texto clínico anonimizado tem 4 destinos possíveis (Gemini, Llama, OpenRouter, OpenAI) e só o áudio→Groq está documentado como pendência de LGPD.

**Integrações (0):** nada novo que já não esteja coberto pelo backlog atual (assinatura gov.br, WhatsApp/SMS do Asaas já listados). Nenhuma sugestão nova hoje para não forçar item fraco.

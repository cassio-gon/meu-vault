---
title: Calima — Avaliação semanal 2026-09-09
date: 2026-09-09
area: Calima
tags: [calima, produto, auditoria]
source: routine
---

## TL;DR

- Semana mais carregada da rotina até aqui: 32 commits (02–08/09) — unificação de preços/agenda com a Secretária IA, vínculo conta↔cadastro sem token, e a nova aba **Documentos** do portal (E2E cifrado). Suíte **921/921 verde, confirmada rodando localmente** (863→921, +58 testes).
- Quase todo commit sensível (crypto, auth, credencial Google) já saiu com o passe de risco em **Fable 5.1** — a regra do `CLAUDE.md` está sendo seguida.
- **Achado novo (tema da semana — UX da aba Documentos):** `window.open()` chamado **depois de um `await` de decifração**, em 3 pontos novos desta semana. No Safari/iOS a ativação do clique costuma não sobreviver a essa espera assíncrona, e o pop-up é bloqueado — o app então mostra "Permita pop-ups", diagnóstico que não corresponde ao problema real. O próprio repo já tem essa lição registrada em outro arquivo (`receita-folha.js:5`), mas não foi aplicada aqui.
- Site vivo: 200 OK, probe de hoje 03:33 BRT, fresco.
- Nenhum item do `PENDENCIAS.md` fechado sem baixa — os 5 itens de "Unificação com a Secretária IA" batem com os commits reais desta semana.

## O que mudou na semana

32 commits em `main`, de `81818c2` (02/09) a `b3e196d` (08/09) — praticamente tudo em 08/09. Por bloco:

**Preços do portal do paciente unificados com a Secretária IA (`da865ba`→`a3dad43`, 08/09).** Consulta avulsa e "plano paciente" saíram de R$ 50,00/R$ 30,00 (primeira rodada, de manhã) para R$ 49,90/R$ 29,90 (`a3dad43`, horas depois) — arredondamento corrigido no mesmo dia, sem passar por produção com o valor errado por muito tempo. Vale a distinção: isso é o preço da **consulta do paciente** (`server/lib/env.js`, `plano-paciente.js`), não a escada de assinatura do médico (Acadêmico R$19,90/Recém-formado R$39,90/Hipócrates R$79,90, `server/lib/planos.js:22-58` — conferido, bate com a descrição desta rotina, sem divergência). Limpeza de cópias hardcoded do preço velho em Preview Deployments do Coolify já está aberta no `PENDENCIAS.md:26` — não repito.

**Vínculo conta↔cadastro sem token (`9fae4d4`…`db2820f`, 08/09).** Paciente que cria acesso pelo convite da fila casa com o cadastro do médico por e-mail+telefone (`server/lib/vinculo-portal.js`). O risco (quem souber e-mail+telefone de alguém e crie a conta antes dele fica vinculado) está documentado no próprio arquivo como decisão consciente do Cássio, mitigado por exigir os dois campos quando a fila guardou telefone e por um "Desfazer vínculo" na ficha. Não é achado novo — já vem decidido e registrado.

**Aba Documentos do portal (`889f336`…`9729ebe`, 08/09).** Envelope híbrido — RSA-OAEP para a chave pública do paciente + AES-GCM sob a DEK do médico (`public/js/documentos-cifra.js`) — cifra/decifra só no navegador; o servidor grava blob e metadados sem nunca ver o conteúdo. `auth` roda **antes** do parser de 15 MB (`server/routes/documentos-portal.js:70`, comentário explícito no código sobre a ordem), e o link enviado pelo médico só abre se for `http(s)://` (`public/js/portal/portal-documentos.js:25`) — trava correta contra `javascript:`/outros esquemas. Revisão de risco: presente (Fable, ver abaixo). Achado de UX na seção do tema.

**Agenda única com o Google Calendar (`ab95ca7`…`41bd230`, 08/09).** Cliente por service account (JWT RS256, sem lib nova) e política de espelho (`server/lib/espelho-agenda.js`) bem separados: fail-closed no freebusy (evita vender o mesmo horário duas vezes), fail-open ao listar eventos para a tela do médico (ver a própria agenda vale mais que travar). Ainda **DORMENTE** — falta ligar as envs no Coolify (`PENDENCIAS.md:22`, já aberto). Sem achado novo.

**Convite por WhatsApp Cloud API e fila só-telefone (`7088f3b` 03/09, `bda00c3` 07/09).** Código em produção e dormente, mesma situação já rastreada em `whatsapp/PENDENCIAS-MIGRACAO.md` — sem mudança de comportamento visível.

**Cobertura de Fable 5.1.** Dos commits que tocam crypto/auth/credencial esta semana (documentos, vínculo, agenda-Google — 12 commits), todos saem com `Co-Authored-By: Claude Fable 5.1`. A exceção é `41bd230` (mostrar eventos do Google na tela do médico, só leitura/exibição, Opus) — fora do gatilho por não tocar auth/crypto/env. Regra sendo seguida.

**Dívida pequena introduzida:** `abrirPayload` (decifra e abre o documento) está **duplicado quase idêntico** em `public/js/documentos-paciente-ui.js:36-45` (médico) e `public/js/portal/portal-documentos.js:22-33` (paciente), os dois novos desta semana — mesmo bug de pop-up nos dois porque a lógica foi copiada, não compartilhada.

**Suíte:** `npm ci` + `node --test` rodados aqui (sandbox sem `node_modules`, mesma situação de semanas anteriores) — **921/921 verde**, +58 testes sobre os 863 de 02/09, todos nos módulos novos.

Sem commits em `workstations/Calima/` além dos auto-syncs de rotina.

## Site vivo

Probe de **2026-09-09 03:33:29 America/Sao_Paulo** (~3h antes deste relatório — fresco): `/` → 200, 0,66s total, TTFB 0,46s; `/manifest.json`, `/sw.js`, `/js/app.js` também 200. Gzip ativo em `/css/style.css`. TLS Let's Encrypt válido até 24/10/2026. Headers seguem restritivos: CSP com `connect-src` explícito (self + `wss://calima.med.br` + `api.github.com` + `raw.githubusercontent.com`), HSTS, `X-Frame-Options: DENY`, `nosniff`, `Referrer-Policy: no-referrer`, COOP `same-origin`. Nada a apontar.

## Tema da semana — índice 4: UX de uma tela específica

Ciclo ainda não tinha passado por este índice; escolhida a tela mais nova e mais rica desta semana: a **aba Documentos do portal do paciente** (`public/js/portal/portal-documentos.js`), espelhada no painel do médico (`public/js/documentos-paciente-ui.js`). Análise estática pelo código — sem navegador, sem afirmação sobre renderização visual.

**1. `window.open()` depois de um `await` de decifração — 3 pontos, todos novos desta semana.**
- `portal-documentos.js:26` (abrir link enviado pelo médico) e `:32` (abrir PDF/imagem) — dentro de `abrirPayload`, chamada em `btn.onclick` só depois de `await abrirComoPaciente(...)`.
- `documentos-paciente-ui.js:67` — mesmo padrão do lado do médico: `onclick: async () => { abrirPayload(await abrirComoMedico(...)) }`.

Em WebKit (Safari/iOS, a plataforma que o próprio comentário do arquivo cita — "no iOS a folha de compartilhamento... salva em Arquivos ou manda no WhatsApp"), a permissão implícita de abrir pop-up que vem do clique do usuário tende a não sobreviver a uma espera assíncrona antes do `window.open`. O app já trata o caso de retorno `null` com `showToast('Permita pop-ups...')` (`portal-documentos.js:33`) — mas isso aponta o dedo para a configuração do navegador quando o motivo real é a ordem do código. Resultado provável: paciente e médico batendo em "permita pop-ups", ajustando uma configuração que não existe (ou existe e não resolve), para um documento que o app tecnicamente já decifrou com sucesso.

O próprio repositório já tinha essa lição aprendida, só que em outro arquivo: `public/js/receita-folha.js:2-5` documenta explicitamente por que a folha de receita é montada no próprio DOM e impressa com `window.print()`, "não abrir janela nova: em PWA standalone no iOS, `window.open` joga o médico para o Safari e ele perde a sessão". A aba Documentos é código novo do mesmo dia que reintroduziu o padrão que o time já sabia ser problemático em iOS, num arquivo diferente.

**Conserto sugerido:** abrir a aba (`window.open('', '_blank')`) **de forma síncrona**, dentro do próprio handler de clique, antes de qualquer `await`; guardar a referência e só setar `aba.location.href = url` depois de decifrar. Isso preserva a ativação do usuário nos navegadores que checam isso.

**2. Campo de senha sem foco automático.** `pedirSenha()` (`portal-documentos.js:74`) cria o card "Digite sua senha" sempre que a chave não está em memória (após reload), mas o `<input type="password">` não recebe `autofocus`/`.focus()` — o paciente precisa tocar no campo antes de digitar. Custo de implementação: uma linha.

## Sugestões novas

**Melhorias (3):**
- **Bug** — Corrigir a ordem `window.open` × `await` na aba Documentos (achado 1 acima) — `portal-documentos.js:26,32`, `documentos-paciente-ui.js:67`.
- Unificar `abrirPayload` (decifra-e-abre) num único helper em `documentos-cifra.js`, hoje duplicado quase idêntico entre `documentos-paciente-ui.js` e `portal-documentos.js` — corrige o bug acima uma vez só, não duas.
- Foco automático no campo de senha de `pedirSenha()` (`portal-documentos.js:74`) — achado 2 acima.

**Integrações (1):**
- **Web Share API (`navigator.share`) como alternativa ao `window.open` para abrir/compartilhar o documento decifrado no celular** — o próprio comentário do código já mira o caso de uso ("folha de compartilhamento... Arquivos ou WhatsApp"); a API nativa de share cobre isso direto, sem depender de nova aba. Vale testar se ela sofre da mesma restrição de ativação — se sim, ainda serve como o "conserto" do achado 1 (chamada síncrona dentro do clique). Não achei uma segunda integração nova que valesse a pena esta rodada.

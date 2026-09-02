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
| E-mail de cobrança ao próprio cliente quando `PAYMENT_OVERDUE` (hoje só o admin é avisado, `billing.js:153-158`) | 2026-08-11 | aberto |
| Mostrar preço (R$ 19,90/mês) e duração do trial (7 dias) na tela "Criar conta", antes do cadastro | 2026-08-11 | aberto |
| Plano anual com desconto, usando o parâmetro `cycle` que a lib do Asaas já aceita (`asaas.js:40-41`, hoje fixo `MONTHLY` em `billing.js:69`) | 2026-08-11 | aberto |
| Notificação de cobrança em atraso via WhatsApp/SMS nativo do Asaas (configuração no painel, sem código novo) | 2026-08-11 | aberto |
| Link de pagamento recorrente por WhatsApp no fim do trial, complementar ao e-mail `TEXTOS.fim` | 2026-08-11 | aberto |
| Preload da arte do login desktop (`login-painel-v5.webp`, 63 KB) — hoje só carrega via `background-image` no CSS atrás de `body:has()`, sem `<link rel="preload">` | 2026-08-12 | aberto |
| Aplicar `requireEscrita`/`anexarPlano`/`requireCota` em `server/routes/receitas.js` (hoje sem gate, ao contrário de `records.js`/`pacientes.js`/`format`/`sugerir`) — médico bloqueado por trial/inadimplência ainda consome IA (import dontpad) e emite receita sem paywall | 2026-08-13 | aberto |
| Padrão ARIA combobox/listbox no autocomplete de medicamento (`public/js/receita-ui.js:118-170`), espelhando o autocomplete de paciente na mesma tela (`public/js/pacientes-ui.js:259-320`) | 2026-08-13 | aberto |
| Smoke test que sobe `server/server.js` de verdade (import + listen) — teria pego a janela de `server/lib/cota.js` ausente (`b4bfeb4`→`202c504`, ~4h17) que quebrava o boot sem a suíte notar | 2026-08-13 | aberto |
| Teste unitário dedicado para `server/lib/openai.js` (formatador dos 3 planos pagos desde `27b5d97`) — sucesso com schema estrito, HTTP não-200, resposta sem `choices[0].message.content`, timeout de 30s — hoje só coberto indiretamente por `cota-rotas`/`planos`/`receitas` | 2026-08-14 | aberto |
| Registrar a OpenAI como subprocessador de dado clínico na política de privacidade e abrir item próprio no `PENDENCIAS.md` (separado de "Buraco do áudio/LGPD", que cobre só o Groq) — desde `27b5d97`/`b93dca6` o texto anonimizado dos planos pagos e da importação de modelos também vai para a OpenAI | 2026-08-14 | aberto |
| Normalizar alias de e-mail (Gmail `+tag`/pontos) antes de gravar `billing_email` (`cadastro.js`/`billing.js`/`perfil.js`) — a trava atual de "uma conta por e-mail" (`8cb8fc1`) só cobre maiúsc/minúsc e deixa aberta uma via de farming na escada de indicação (`premio-indicacao.js`), que conta qualquer cadastro pelo link sem exigir uso do app | 2026-08-19 | aberto |
| Coluna `boas_vindas_enviado_em` em `users`, checada no disparo automático (`routes/auth.js`) e em `scripts/campanha-email/boasvindas-todos.mjs` — hoje o script de disparo em massa não filtra por data de cadastro nem marca quem já recebeu, então rodá-lo após o e-mail automático (`9b465ff`) ou rodá-lo duas vezes duplica o boas-vindas | 2026-08-19 | aberto |
| **Bug** — Passar `pacienteId` em `abrirSalaDaConsulta` no caminho automático de `ws-tele.js:77` (`ambosPresentes`), ou religar a UI a `abrirSalaDaEspera` (`public/js/tele/tele-api.js:18`, hoje sem nenhum chamador) — sem isso, todo paciente autocadastrado pelo portal nunca tem `pacientes_contas.paciente_id` vinculado, e a fila de espera mostra e-mail em vez de nome para sempre | 2026-08-26 | aberto |
| **Bug** — Claim condicional em `POST /api/portal/plano/assinar` (`server/routes/portal-plano.js:82-118`), igual à trava já pendente para `/subscribe` do médico (`routes/billing.js:40-67`) — duplo clique cria 2 assinaturas Asaas para a mesma conta de paciente; sem teste de concorrência em `tests/portal-plano.test.js` | 2026-08-26 | aberto |
| **Bug (LGPD)** — Tirar o e-mail em claro de `avisarCadastroPaciente` (`server.js:150`, commit `a665a10`) — vai para o push (tela de bloqueio) e para o e-mail do admin, contrariando a mesma regra de privacidade escrita pelo autor na mesma semana em `billing.js` (`AVISO_PACIENTE`) e `aviso-consulta.js` | 2026-08-26 | aberto — tocado pelo commit `0584634` (02/09) sem correção |
| Atualizar o comentário do schema em `server/lib/db.js:329` ("'recem' PERMANENTE, premio_plano_ate NULL") — desde `cb0f1dd` (27/08) o prêmio de indicação passou a valer `DIAS_PREMIO` (30) dias; NULL só sobrevive em contas premiadas antes da mudança | 2026-09-02 | aberto |

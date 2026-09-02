---
title: Calima — Avaliação semanal 2026-09-02
date: 2026-09-02
area: Calima
tags: [calima, produto, auditoria]
source: routine
---

## TL;DR

- Semana de 15 commits em `main` (26–28/08): notificação administrativa por e-mail (não só push), correção de um sino que escondia avisos de paciente/cobrança, e um redesign grande ("interface-v2") que alcança o mockup do Claude Design — paleta, tipografia única, painel do dia, hero animado, botões de vidro.
- **Bug de LGPD do relatório anterior (e-mail do paciente em claro no push/e-mail do admin) foi TOCADO nesta semana e continua NÃO corrigido** — o commit que unificou os canais de aviso passou pela função exata e manteve o vazamento.
- Achado novo do tema da semana (Código/manutenibilidade): o comentário do schema em `server/lib/db.js:329` ficou desatualizado — ainda descreve o prêmio de indicação como "PERMANENTE", mas o mesmo commit que mexeu no CSS mudou a regra para 30 dias.
- Suíte **863/863 verde, confirmado rodando localmente** (não só pela palavra do commit) — o sandbox não tinha `node_modules`, corrigido com `npm ci`.
- Site vivo: 200 OK, probe de ontem (01/09) 11h21 BRT, fresco.

## O que mudou na semana

15 commits em `main`, todos de 26 a 28/08 (nada depois disso até hoje). Por assunto:

**Avisos administrativos por e-mail (`0584634`, `424e607`, 26/08).** Assinatura paga, atraso, estorno, troca de plano e cobrança recusada só saíam por push — quem estivesse longe do app descobria horas depois. Agora saem também por e-mail (padrão ligado; quem já manda e-mail próprio do mesmo fato passa `email:false` para não duplicar). Junto, um bug real de UX corrigido: o de-dup do painel do admin descartava por **destino da URL** (`/?ir=admin`), então tudo que não vinha de `users`/`billing_events` — paciente novo, cobrança recusada, atraso, estorno — sumia do painel enquanto o sino badge marcava 1. Trocado para casar por **título específico**, com o efeito colateral assumido no código: título novo no servidor volta a aparecer, no pior caso duplicado, nunca escondido.

**Redesign "interface-v2" (`cb0f1dd`, `1a30378`, `189e969`, 27/08 — maior commit da semana, 1883 linhas).** Chega o mockup do Claude Design: paleta azul única no tema claro, tipografia unificada em Inter Tight (saem Libre Franklin e Sora, −54KB de woff2 no shell do SW), painel do dia com moldura única no desktop, hero com dissolução de partículas em vez de apagar letra a letra, botões de vidro nos CTAs de ditado. Duas rodadas de correção no mesmo dia: uma varredura geométrica de contraste (achou `--on-accent` reprovando em 7 lugares, corrigido para `--accent-ink`) e dez "críticos cegos" comparando cada tela contra o mockup sem saber qual era qual — o placar (3×7 a favor do mockup, mas só em desktop) levou a rejeitar conscientemente os chips de status "Concluído/Transcrevendo" por serem dado inventado (a tabela `records` não tem campo de status). Ver achado de manutenibilidade abaixo sobre o que esse commit carregou junto.

**Ajustes de painel do dia no celular (`cf3892e`, `a8d5e9a`, `487b1c0`, `2683ee1`, 28/08).** O vídeo do hero, o painel do dia inteiro e o texto "Passagens de plantão" (que cortava palavra no meio ao dissolver) passaram a existir também no celular — o redesign de 27/08 tinha sido feito olhando desktop.

Sem commits em `workstations/Calima/` nesta janela além dos auto-syncs de rotina — nada de novo lá.

## Site vivo

Probe de **2026-09-01 11:21:26 America/Sao_Paulo** (~19h antes deste relatório — fresco): `/` → 200, 0,82s total, TTFB 0,62s; gzip ativo em `/css/style.css`; TLS Let's Encrypt válido até 24/10/2026; headers com CSP restritiva, HSTS, `X-Frame-Options: DENY`, `X-Content-Type-Options: nosniff`, `Referrer-Policy: no-referrer`, `Cross-Origin-Opener-Policy: same-origin`. Nada a apontar.

## Tema da semana — índice 5: Código / manutenibilidade

**1. Commit gigante mistura redesign de CSS com mudança de regra de negócio (`cb0f1dd`).** Além de paleta/tipografia/animações, o mesmo commit reescreveu a regra do prêmio de indicação em `server/lib/planos.js` e `server/lib/premio-indicacao.js`: o degrau ganho por indicar colegas deixou de ser **permanente** e passou a valer **30 dias** (`DIAS_PREMIO`), com o trial estendido junto para não expirar o prêmio antes do plano. A mudança em si é correta e bem testada (863 verdes), e o próprio commit explica por que não deu para separar — os arquivos JS de UI entram no `SHELL_HASH` do service worker, e um commit parcial gravaria um hash de estado que não existe em nenhum commit isolado. Mas o efeito colateral é real: quem for revisar ou reverter só a mudança de billing (ou só o CSS) não consegue sem pegar o resto junto.

**2. Doc-drift introduzido pela mesma mudança.** `server/lib/db.js:329` ainda documenta a coluna assim: *"'recem' PERMANENTE (premio_plano_ate NULL) para quem leva 5 colegas ao app"* — descrição que valia antes de `cb0f1dd` e que ninguém atualizou quando a regra virou temporária. `planos.js` (mesmo commit) já registra a mudança corretamente no comentário de `premioVigente`; só o schema em `db.js` ficou para trás. Baixo risco (é comentário, não lógica), mas é exatamente o tipo de deriva que confunde quem olha o schema primeiro antes do código de regra.

**3. Bug de LGPD do relatório de 26/08 segue aberto, e foi tocado sem correção.** `avisarCadastroPaciente` (`server/server.js:150`) continua montando `` `${email} criou conta no portal...` `` e mandando para o push (tela de bloqueio) e para o e-mail do admin em claro — o mesmo texto de antes. O commit `0584634` desta semana refatorou exatamente essa função (para usar o `notificarAdmin` unificado) mas manteve o vazamento intacto; já está no `BACKLOG.md` desde 26/08, não repetido aqui como sugestão nova, só sinalizado que a janela de correção passou por cima do código e não mexeu nisso.

**4. Suíte confirmada verde de verdade.** `node --test` falhava 61 arquivos no sandbox por falta de `node_modules` (`npm ci` resolveu em 3s); depois de instalado, **863/863 passando**, batendo com o que os commits afirmam.

## Sugestões novas

**Melhorias (1):**
- Atualizar o comentário do schema em `server/lib/db.js:329` para refletir que o prêmio de indicação hoje é de `DIAS_PREMIO` (30) dias, e que `premio_plano_ate = NULL` só sobrevive em contas premiadas antes da mudança — achado 2 acima, custo de minutos.

**Integrações (0):** nada novo esta rodada — tema da semana não foi mercado.

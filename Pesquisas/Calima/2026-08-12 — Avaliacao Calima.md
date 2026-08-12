---
title: Avaliação Calima — 2026-08-12
date: 2026-08-12
area: Calima
tags: [calima, produto, auditoria]
source: routine
---

# Calima — Avaliação diária (2026-08-12)

## TL;DR

- **4 commits em `prontuario-ia` nas últimas 24h** (todos de 11/08): refatoração da topbar do desktop (unidade + botão de Perfil) e login v5 (split-screen sem marca). Suite rodada agora: **467/467 verde**, nenhuma regressão encontrada no diff.
- **Ponto positivo medido:** a troca de arte do login já **reduziu peso** — `login-full.webp` (83.466 B) saiu, `login-painel-v5.webp` (64.652 B) entrou, **-22,5%** sem que ninguém pedisse.
- **Tema de hoje (índice 0 do ciclo): Performance.** Achado novo: a arte do login desktop entra só via `background-image` no CSS, atrás de um seletor `body:has(...)` — sem `<link rel="preload">`. Ver seção própria.
- **Site vivo:** probe do Mac em 06:56:49 UTC (~2h10 antes desta execução) — saudável, TLS até 24/10, gzip confirmado.
- 1 sugestão nova de performance; sem integração nova hoje (nada que passasse no crivo de "vale a pena e não repete backlog").

---

## O QUE MUDOU EM 24H

```
git -C prontuario-ia log --since="24 hours ago" --stat --pretty="%h %ad %s" --date=short
  ce24309 2026-08-11 feat(topbar): unidade ao lado das abas; foto+nome viram o botão de Perfil
  320d63f 2026-08-11 feat(topbar): chip da unidade abre menu para trocar de local
  e84286a 2026-08-11 feat(topbar): identidade e sino abraçam o canto direito, sino por último
  e729a2b 2026-08-11 feat: login desktop v5 — arte sem marca, fundo unificado e polish do impeccable

git -C claude-config log --since="24 hours ago" -- workstations/Calima/  → vazio
```

Os 4 commits formam uma sequência coesa (mesma tarde, 11/08): reorganizar a topbar do desktop (menu de troca de unidade, botão de Perfil) e trocar a arte do login por uma versão sem marca em split-screen. Revisei os 4 diffs completos (`git show`), não só o resumo:

- **`SHELL_HASH` do Service Worker foi bumpado nos 4 commits** (`ad835482` → `16a22dc3` → `962120be` → `ecad3247` → `64b333e0`), coerente com `tests/sw-cache.test.js` — nenhum deploy "fantasma" (o defeito que o commit `d590a35` de 04/08 já corrigiu não voltou).
- **Sem referência órfã ao webp antigo** — `grep -r "login-full"` no repo não retorna nada; só `login-painel-v5.webp` é citado, e só uma vez (`style.css:2312`).
- **`DESIGN.md` foi atualizado junto** nos 2 commits que mudam layout (login v5 e a reorganização final da topbar) — a doc de design não ficou defasada do CSS, o que costuma acontecer quando UI muda rápido.
- **Suite: rodei `npm ci && npm test` agora (ambiente desta rotina, não em produção) — 467/467 passando**, incluindo o teste de hash do SW. Nenhum item do `PENDENCIAS.md` foi fechado sem baixa (os 4 commits não tocam nenhum arquivo dos médios/baixos listados lá).
- Novo texto de UI: "Gerenciar locais…", "PERFIL", chip de unidade — não introduz o padrão "Dr(a)." já rastreado como pendência aberta; não achei ocorrência nova dele nos 4 diffs.

Nenhum bug ou regressão encontrado nos 4 commits.

---

## SITE VIVO

Probe do Mac lido de `Pesquisas/Calima/_probe-site.md`, medido em **2026-08-12 03:56:50 America/Sao_Paulo** (06:56:49 UTC) — **fresco**, ~2h10 antes desta execução (09:07 UTC).

- `/` → 200, 0,737s total, TTFB 0,508s, 24.865 B.
- `/manifest.json`, `/sw.js`, `/js/app.js` → todos 200.
- Compressão: `content-encoding: gzip` confirmado em `/css/style.css`.
- TLS: Let's Encrypt, válido até 24/10/2026.
- Headers de segurança presentes: CSP, HSTS, X-Frame-Options DENY, COOP same-origin, X-Content-Type-Options nosniff.

Nada a reportar — site saudável.

---

## TEMA DO DIA — índice 0 — Performance

Foco no que mudou nas últimas 24h (seção acima já cobriu boa parte), mais uma verificação do estado geral que não se repete de relatórios anteriores.

**1. Arte do login desktop (`login-painel-v5.webp`, 63 KB) carrega sem preload, atrás de CSS condicional.** Ela só é referenciada em `public/css/style.css:2312`:
```css
body:has(#screen-auth:not(.hidden)) #auth-aside {
  background: url('/media/login-painel-v5.webp') left center / cover no-repeat, #eef4fd;
  ...
}
```
Como é `background-image` (não `<img>`), o navegador só descobre essa URL depois de baixar e aplicar o CSSOM e casar o seletor `:has()` — não há `<link rel="preload" as="image">` no `<head>` como existe para as 2 fontes (`index.html:28-29`). No split-screen (≥1024px), essa arte cobre 46% da largura da tela — é conteúdo visual grande, não um detalhe. Em conexão lenta, quem abre a tela de login no desktop vê primeiro o fundo liso `#eef4fd` e a imagem "pipoca" depois. Não é um bug (o app funciona), é atraso evitável num elemento visualmente grande. Nota: por ser `background-image` via CSS (não `<img>`), esse asset **não conta oficialmente como candidato a LCP** pela spec — o ganho aqui é percepção de carregamento na tela de login, não a métrica LCP em si.

**2. `style.css` cresceu 234 linhas em 24h só com este trabalho** (2.237 → 2.471 linhas, arquivo total agora 120.573 B antes de gzip) — esperado para 4 commits de UI num único dia; a compressão na borda (Traefik/Coolify, confirmada pelo probe) absorve a maior parte do custo de rede. Sem achado novo aqui além do que a pendência já rastreada de convergência de escala (30 tamanhos de fonte / 12 raios) cobre — não repito.

**3. `login-full.webp` → `login-painel-v5.webp`: -22,5% de peso** (83.466 B → 64.652 B), sem SW precache de nenhum dos dois (confirmado: `grep "media/" public/sw.js` não retorna nada — a lista `SHELL` não inclui imagens, só o shell de app). Ganho limpo, sem contrapartida.

---

## SUGESTÕES NOVAS

**Melhorias (1):**

1. **Preload da arte do login desktop** — adicionar `<link rel="preload" href="/media/login-painel-v5.webp" as="image" media="(min-width: 1024px)">` no `<head>` de `public/index.html` (mesmo padrão já usado para as fontes, linhas 28-29). `media` restringe o preload ao breakpoint onde a imagem realmente é usada, para não desperdiçar banda em quem abre no celular. Custo: uma linha de HTML, zero risco — a imagem já é servida, só muda quando o navegador começa a buscá-la.

**Integrações novas:** nenhuma nova hoje que passasse no crivo de "vale a pena e não repete `BACKLOG.md`" — os itens de integração já em aberto (WhatsApp/Asaas, gov.br, CID-10) seguem sendo os candidatos relevantes; relatório curto e honesto vale mais que forçar item novo.

---

## BACKLOG (acumulado)

1 sugestão nova acrescentada a `BACKLOG.md` nesta pasta.

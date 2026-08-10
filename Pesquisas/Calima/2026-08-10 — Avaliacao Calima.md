---
title: Avaliação Calima — 2026-08-10
date: 2026-08-10
area: Calima
tags: [calima, produto, auditoria]
source: routine
---

# Calima — Avaliação diária (2026-08-10)

## TL;DR

- **SITE NÃO VERIFICADO HOJE** — `calima.med.br` está bloqueado pela política de rede (egress) *deste ambiente de execução*, não é sinal de o site estar fora do ar. Ver detalhes abaixo; isso provavelmente vai se repetir em toda execução futura até alguém ajustar a política.
- Achado mais importante do dia: **compressão HTTP (gzip/brotli) não está configurada no Express** (`server/server.js:118`) — ganho de performance real e custo zero, relevante para rede ruim de hospital.
- Código segue saudável: headers de segurança completos (CSP/HSTS/X-Frame-Options/COOP já implementados em `server/lib/security-headers.js`), SW com fallback offline correto.
- Tema aprofundado hoje: **performance** (1º do ciclo, é a 1ª execução desta rotina).
- 5 sugestões novas (3 melhorias + 2 integrações), nenhuma repete PENDENCIAS.md — ver seção própria e `BACKLOG.md`.

---

## 1. SITE VIVO — BLOQUEADO, não medido

Tentativas registradas em **2026-08-10, ~09:19 UTC**:

- `curl -D - https://calima.med.br/` → `CONNECT tunnel failed, response 403` (0.33s, sem chegar a conectar).
- Status do proxy de saída desta sessão (`$HTTPS_PROXY/__agentproxy/status`) confirma a causa:
  ```
  "recentRelayFailures": [{
    "kind": "connect_rejected",
    "detail": "gateway answered 403 to CONNECT (policy denial or upstream failure)",
    "host": "calima.med.br:443"
  }]
  ```
- `WebFetch` (caminho de rede independente do curl) → `EGRESS_BLOCKED: Access to calima.med.br is blocked by the network egress proxy.`

Duas rotas de rede diferentes bateram na mesma política — não é falha pontual de DNS/TLS, é **bloqueio deliberado do host pela política de egress desta sessão remota**. Não tentei contornar (a instrução do próprio proxy é "do not retry or route around it — report the blocked host"). Consequência prática: **a seção "SITE VIVO" desta rotina não pode ser cumprida no ambiente atual** — nem uptime, nem headers de segurança em produção, nem `manifest.json`/`service worker` ao vivo, nem tempo de resposta real. Isso é diferente de "site fora do ar": é o ambiente que roda esta rotina que não alcança o host.

**Se isso persistir amanhã, vale revisar a política de rede do ambiente desta rotina** (liberar `calima.med.br` na allowlist de egress) — do contrário essa seção fica estruturalmente vazia todo dia.

---

## 2. TEMA DO DIA — Performance (código, sem medição de rede real)

Primeira execução da rotina, então o ciclo (performance → acessibilidade → segurança → SEO/PWA → UX de tela → código/manutenibilidade → concorrência) começa aqui.

**Compressão HTTP ausente no Express** (`server/server.js:118`):
```js
app.use(express.static(PUBLIC_DIR, { dotfiles: 'allow' }));
```
Sem `compression()` (pacote `compression` do npm nem está em `package.json`) antes do `express.static`. O CSS (`public/css/style.css`, 2.237 linhas) e os 61 módulos JS de `public/js/` saem sem gzip/brotli **na camada do Express** — se o Traefik/Coolify na frente também não comprimir (não verificável hoje, rede bloqueada), o payload total do primeiro load vai maior do que precisa, o que pesa mais em rede ruim (o próprio `MEMORY.md` do projeto já cita esse cenário: "3G do subsolo do hospital"). Ativar custa uma linha e zero risco.

**Arquitetura sem bundler é deliberada, não um bug** — 61 arquivos JS carregados via `import` nativo de módulo ES (confirmado: `SHELL` do `sw.js` lista 69 entradas JS+CSS). Isso é coerente com a convenção documentada em `workstations/Prontuario-IA/CLAUDE.md` ("arquivos pequenos e focados, 200–400 linhas") e HTTP/2 mitiga bastante o custo de múltiplas requisições. Não é achado, é confirmação de que o design é intencional.

**Fontes: já bem feito.** Dois `woff2` (80 KB total) self-hosted com `<link rel="preload">` (`public/index.html:29-30`) — sem terceiro, sem FOIT longo. Nada a mudar aqui.

**Imagens de startup do iOS (4,2 MB em `public/icons/startup/`) não pesam no load real** — conferi que **não** estão na lista `SHELL` do `sw.js` (só `icon.svg` está, linha 88), então o Service Worker não as pré-cacheia; o Safari busca só a imagem que casa com a media query do aparelho, uma vez, sob demanda. Não é um problema, apesar do tamanho total no repo.

**Cache-Control do `express.static` fica no default (ETag apenas, sem `maxAge`)** — isso não é necessariamente errado aqui: o projeto usa `SHELL_HASH` no nome do `CACHE_NAME` do SW como mecanismo de invalidação por deploy (comentário em `public/sw.js:3-9`), então um `Cache-Control` de longa duração no servidor para os arquivos do SHELL poderia **brigar** com essa estratégia (o navegador serviria do HTTP cache sem nem perguntar ao SW). Para os ativos que não fazem parte dessa invalidação — fontes, ícones, `public/js/vendor/jspdf.umd.min.js` (365 KB, carregado sob demanda) — dar `Cache-Control: public, max-age=31536000, immutable` seria seguro. Detalhe na seção de sugestões.

**CSS com 30 tamanhos de fonte distintos e 12 raios de borda** (conferido hoje, `grep` em `public/css/style.css`) — confirma que o achado do `/impeccable audit` de 07/08 (registrado em `PENDENCIAS.md`) segue **sem mudança nenhuma** desde então. Não é achado novo, é confirmação de que continua aberto; efeito em performance é marginal (bytes a mais no CSS), o efeito real é manutenibilidade — já rastreado, não repito como sugestão nova.

---

## 3. FUNÇÕES — roadmap Fase 2/3 vs código

Conferido por código (não é opinião):

| Item do roadmap (Fase 2/3) | Estado no código |
|---|---|
| Sync celular↔notebook (código de sessão) | **Não implementado.** Nenhum módulo de pareamento por código encontrado. |
| Export Word (.docx) | **Não implementado.** `public/js/export.js` só tem `copyRecord` (clipboard) e `exportPdf` (jsPDF, client-side). |
| Template por especialidade | **Não implementado.** Nenhuma referência a "especialidade" no código do app. |

Os três batem exatamente com o que `PENDENCIAS.md` já lista sob "Teste em plantão real → destrava a Fase 2" — nenhum gap novo encontrado hoje além do que já está rastreado.

Bug provável percorrendo o código: nenhum encontrado hoje além dos já catalogados em `PENDENCIAS.md` (webhook Asaas não-atômico, `/subscribe` sem trava de duplo clique, etc. — não repito aqui).

---

## 4. LAYOUT/UX — nota metodológica

Análise **estática, só pelo código** (CSS/HTML/JS) — sem navegador real, então nada aqui é afirmação sobre renderização visual. O único ponto novo hoje é a confirmação do item de tipografia/raio acima (seção Tema do Dia); o resto do que já foi mapeado por auditoria visual (contraste, aria, toque) está em `PENDENCIAS.md` e não repito.

---

## 5. SUGESTÕES NOVAS (nenhuma repete PENDENCIAS.md nem BACKLOG.md — é o 1º relatório)

**Melhorias (3):**

1. **Ativar compressão HTTP no Express** — `npm i compression` + `app.use(compression())` antes de `app.use(express.static(...))` em `server/server.js:118`. Custo zero, sem risco, ganho real em rede ruim.
2. **`Cache-Control` de longa duração só para ativos verdadeiramente imutáveis** — fontes (`public/fonts/`), ícones estáticos (`public/icons/`) e `public/js/vendor/jspdf.umd.min.js`, servidos por uma rota própria (ou `express.static` separado com `maxAge`) **sem tocar** no caminho que serve os módulos do SHELL — para não colidir com a invalidação por `SHELL_HASH` do Service Worker.
3. **App Shortcuts no `manifest.json`** — hoje o arquivo (`public/manifest.json`) não tem a chave `"shortcuts"`. Adicionar um atalho "Novo atendimento" permitiria ao médico segurar o ícone do app (Android e iOS 16.4+) e cair direto na tela de ditado, sem passar pela Início — reduz fricção num fluxo repetido dezenas de vezes por plantão. Zero custo, só JSON.

**Integrações novas (2):**

1. **Assinatura eletrônica gov.br (gratuita), como reforço sobre o "selo" já existente** — hoje o prontuário fica travado por um selo local (hash + timestamp, `public/js/selo-modal.js`), que dá integridade mas não é uma assinatura eletrônica reconhecida. O gov.br oferece assinatura eletrônica básica gratuita; camada opcional sobre o selo reforçaria a validade jurídica do prontuário sem custo de operação, coerente com a preocupação médico-legal que já motivou o próprio selo.
2. **CID-10 como dataset estático (DATASUS) para autocomplete determinístico no campo `HD:`** — hoje a única fonte de código CID é a sugestão por IA (Claude Haiku, `sugestao-ui.js`). Um dataset local (~14 mil códigos, arquivo JSON estático, sem chamada de rede, sem custo de API, nenhum dado sai do aparelho) serviria de autocomplete enquanto o médico digita manualmente — complementar, não substitui a sugestão por IA, útil quando o médico já sabe o código e só quer digitar rápido.

---

## 6. BACKLOG (acumulado)

Ver `BACKLOG.md` nesta mesma pasta — criado hoje com as 5 sugestões acima, todas em aberto.

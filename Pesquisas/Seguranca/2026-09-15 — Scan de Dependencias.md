---
title: Scan de Dependências — 2026-09-15
date: 2026-09-15
area: Seguranca
tags: [seguranca, dependencias]
source: routine
---

# Scan de Dependências — 2026-09-15

Escopo: `calima` (produção, prioridade alta) e `sst-descomplica-cron` (GitHub Action, prioridade média). Ambos clonaram e rodaram sem falhas (`npm install` + `npm audit --json` + `npm outdated --json` completos em `calima`; `sst-descomplica-cron` segue sem manifesto). Nenhuma correção foi aplicada nos repos escaneados — este é só o relatório.

## TL;DR

- **P0: 1** — `multer` 2.2.0 no `calima` (rota `/api/transcribe`, produção), **3 CVEs HIGH (CVSS 7.5)**, agora indexadas pelo `npm audit` (no ciclo passado era achado por changelog, ainda sem indexação). **5º ciclo consecutivo sem correção.**
- **P1: 1** — recorrente, **5º ciclo sem correção**: Dockerfile do `calima` em `node:20-bookworm-slim`, EOL desde 30/04/2026 (~4,5 meses sem patch de segurança).
- **P2: 5** (contagem abaixo, inclui 2 CVEs moderadas novas em `qs` transitivo). Nenhum segredo commitado em nenhum dos dois repos (árvore + histórico completo).
- **Boa notícia:** um único `npm audit fix` (sem `--force`) resolve o P0 do multer **e** todo o P2 de `qs`/`body-parser`/`express` de uma vez, sem sair dos ranges já declarados no `package.json` — confirmado via `--dry-run`, zero breaking change.
- Ação: `npm audit fix` em `calima/` + configurar `limits.fieldNestingDepth`/`fieldArrayIndexLimit` em `transcribe.js` + trocar `FROM node:20-bookworm-slim` → `node:22-bookworm-slim` no Dockerfile.

## calima

`npm install` + `npm audit --json` (raiz, workspace `server`) + `npm outdated --json` rodaram limpos.

| Pacote | Versão atual | Situação | Achado |
|---|---|---|---|
| `multer` | 2.2.0 | **P0 — recorrente, agora indexado** | Ver seção dedicada abaixo. |
| `qs` (transitivo via `express`/`body-parser`) | 6.15.3 | **P2 — novo** | 2 CVEs moderadas/baixas, ver abaixo. |
| `body-parser` | 1.20.5 (transitivo) | P2 — recorrente | Mesmo achado dos 4 ciclos anteriores (GHSA-v422-hmwv-36x6, Low). Corrige junto no `npm audit fix`. |
| `express` | 4.22.2 | P2 | `npm outdated` aponta patch 4.22.3 (sem CVE direto, mas necessário para trazer `qs@6.16.0`) e major 5.2.1 (breaking, não é upgrade de segurança). |
| `better-sqlite3` | 12.11.1 | OK | Sem advisories. `npm outdated` aponta 13.0.3, mas o projeto **exige `^12`** (11.x não compila no Node 26) — não mexer nesta major. |
| `ws` | 8.21.3 | OK | Já na última versão. |
| `web-push` | 3.6.7 | OK | Já na última versão. |

### multer — P0, 5º ciclo sem correção

`npm audit` agora **indexa oficialmente** as 3 CVEs HIGH que o ciclo passado já tinha confirmado via changelog (a indexação estava atrasada em 01/09). Nada mudou no código: `server/routes/transcribe.js:7-9` continua sem `fieldNestingDepth`/`fieldArrayIndexLimit`, e a rota `/api/transcribe` segue atrás de `requireAuth(db)` + `requireEscrita` (`server/server.js:95`) — mas `SIGNUP_ABERTO` continua `true` por padrão (`server/lib/env.js:131`), então qualquer atacante se autocadastra via trial e derruba o processo com uma requisição multipart malformada.

- **CVE-2026-77078** (GHSA-wc9g-mqfw-jrwm) — HIGH, CVSS 7.5. `RangeError` não capturado derruba o processo Node.
- **CVE-2026-77037** (GHSA-qfvm-cv95-jqjf) — HIGH, CVSS 7.5. Vazamento de file descriptor em upload abortado.
- **CVE-2026-82333** (GHSA-535w-7cp7-47q4) — HIGH, CVSS 7.5. Índice de array gigante trava o event loop.
- CVE-2026-77063 (GHSA-qvfw-j98x-7q72) — Low, CVSS 3.7. Bypass de `fileSize` com `fileFilter` assíncrono.

Todas corrigidas em `>=2.3.0`. `npm outdated` mostra `2.4.0` como última — `npm audit fix` já resolve dentro do range `^2.0.0` declarado, sem editar `package.json`.

### qs — P2, novo achado

Dependência transitiva (`express` → `qs`, `body-parser` → `qs`), instalada em `6.15.3`. Duas CVEs, ambas exigem uso de API específica não presente no código do `calima` (confirmei via `grep` em `server/`: nenhum `qs.stringify(`, nenhum `comma: true`):

- **GHSA-4mjr-xmp4-gh2g** (moderate, CVSS 5.3) — DoS via `isBuffer` controlado pelo atacante. Só dispara se o app re-serializar `req.query`/body parseado de volta com `qs.stringify()` (logging, montagem de URL de redirect) — **não ocorre em produção aqui**, calima não chama `qs.stringify`.
- **GHSA-x5fp-wj9c-mxmx** (moderate, CVSS 3.7) — bypass de `arrayLimit` via chave `a[]=1,2,3,...` com `comma: true`. Express não habilita `comma: true` por padrão, e o calima não habilita explicitamente — **não ocorre em produção aqui**.

Corrigidas em `qs@6.16.0`. `express@4.22.2`/`body-parser@1.20.5` pinam `qs ~6.15.1`, então uma versão isolada de `qs` não resolveria sozinha — mas `express@4.22.3`+ e `body-parser@1.20.8`+ já declaram `qs ~6.16.0`, e `npm audit fix --dry-run` confirma que o bump automático (`express` 4.22.2→4.22.3, `body-parser` 1.20.5→1.20.8, `qs` 6.15.3→6.16.0) cai dentro do `^4.21.0` já declarado no `package.json` — sem precisar de `overrides` nem editar manifesto. Sem breaking change no changelog do `qs` 6.16.0 (só adiciona opção `depth` em `stringify`, default `Infinity`).

Classificado como **P2** (não **P0**) porque, apesar do CVSS moderado, nenhum dos dois vetores é alcançável no código atual do calima — mas como a correção vem de graça junto do `npm audit fix` do multer, entra no mesmo comando.

### Dockerfile / versão do Node — P1, 5º ciclo sem correção

`Dockerfile` continua em `node:20-bookworm-slim` nos dois estágios. Node.js 20 saiu de LTS em 30/04/2026 (confirmado: [nodejs.org/en/about/eol](https://nodejs.org/en/about/eol)) — hoje, 15/09/2026, são **~4,5 meses** sem patch de segurança oficial do Node em produção. O CI (`.github/workflows/test.yml`) já roda em Node 22 — só a imagem de produção ficou para trás, mesmo achado desde 15/07.

- **Correção:** `FROM node:20-bookworm-slim` → `FROM node:22-bookworm-slim` nas duas linhas `FROM`.
- **Risco de quebra:** baixo, inalterado desde os ciclos anteriores — `better-sqlite3@12.11.1` tem prebuilds para Node 22+, CI já valida nessa versão.

### Segredos e .gitignore

- Varredura por `gsk_`, `AIza`, `$aact_`, `RESEND_`, `sk-`, `sk-ant-` em árvore de trabalho + histórico completo (`git grep` + `git log --all -p`): **nenhuma ocorrência real**. Único hit é `server/.env.example:40`, comentado, sem valor (placeholder).
- `.gitignore` cobre `.env`, `.env.local`, `.env.*.local`, `server/.env`, `*.log`, `*.db`, `*.db-*`, `data/*` — correto, inalterado.
- Repo teve volume alto de commits desde 01/09 (portal do paciente, integração WhatsApp, campanha por e-mail/WhatsApp) — nenhum desses introduziu segredo commitado ou novo manifesto de dependências.

### GitHub Actions do calima

`.github/workflows/test.yml` inalterado: `actions/checkout@v4` e `actions/setup-node@v4` — tag mutável, não SHA. Mesmo risco baixo apontado nos ciclos anteriores (sem `secrets`, sem `permissions` elevadas). Entra na contagem P2.

### Contagem P2

1. `qs` 6.15.3 → 6.16.0 (moderate x2, não exploráveis no código atual) — detalhado acima.
2. `body-parser` 1.20.5 → 1.20.8 (Low, recorrente) — mesmo achado dos 4 ciclos anteriores.
3. `express` 4.22.2 → 4.22.3 (patch, necessário para trazer `qs` corrigido).
4. `express` major 4→5 disponível, sem CVE, breaking — sem urgência.
5. `.github/workflows/test.yml`: Actions em tag, não SHA — recorrente, baixo risco.

(`better-sqlite3` 13.0.3 disponível mas fora de escopo — projeto exige `^12`, não é achado.)

## sst-descomplica-cron

Repo sem `package.json`/manifesto npm nem `requirements.txt` — confirmado por inspeção da árvore. Nada a rodar em `npm audit`/`pip-audit`, esperado. Sem commits desde o scan de 01/09.

- **Pinagem de Actions:** workflow (`sst-publish.yml`) segue sem nenhuma linha `uses:` — só `curl`/`jq` no runner. Sem risco de supply chain via tag mutável.
- **Permissões:** `permissions: contents: read` no topo — escopo mínimo, correto.
- **Segredo:** `SST_WEBHOOK_TOKEN` via `${{ secrets.SST_WEBHOOK_TOKEN }}`, passado por env ao step, nunca hardcoded.
- **Segredos commitados:** nenhuma ocorrência nos padrões varridos (árvore + histórico completo).

Sem mudanças desde o scan de 01/09/2026.

## Plano de correção (ordem de prioridade)

1. **[P0 + P2 juntos — resolve multer, qs, body-parser e express num comando]**
   ```bash
   cd /home/user/calima && npm audit fix
   ```
   Confirmado via `--dry-run`: bump `multer` 2.2.0→2.4.0, `express` 4.22.2→4.22.3, `qs` 6.15.3→6.16.0, `body-parser` 1.20.5→1.20.8 — todos dentro dos ranges já declarados (`^2.0.0`, `^4.21.0`), sem `--force`, sem editar `package.json`, sem breaking change nos changelogs.

   Em seguida, endurecer `server/routes/transcribe.js:7-9` (achado recorrente, correção de config que o upgrade de versão sozinho não cobre):
   ```js
   const upload = multer({
     storage: multer.memoryStorage(),
     limits: { fileSize: MAX_AUDIO_BYTES, fieldNestingDepth: 2, fieldArrayIndexLimit: 10 },
     fileFilter: ...
   });
   ```
   Sem risco de quebra — a rota só espera `upload.single('audio')`.

2. **[P1 — reaberto, 5º ciclo]** Atualizar `Dockerfile`: `node:20-bookworm-slim` → `node:22-bookworm-slim` (duas ocorrências). Testar build local antes do deploy.

3. **[P2]** Pinar `actions/checkout` e `actions/setup-node` por SHA em `.github/workflows/test.yml` (opcional, risco baixo).

4. **[P2 — sem urgência]** Avaliar migração major do `express` 4→5 num ciclo dedicado, revisando breaking changes antes.

`sst-descomplica-cron` segue limpo, sem achados novos.

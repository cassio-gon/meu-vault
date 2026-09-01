---
title: Scan de Dependências — 2026-09-01
date: 2026-09-01
area: Seguranca
tags: [seguranca, dependencias]
source: routine
---

# Scan de Dependências — 2026-09-01

Escopo: `calima` (ex-`prontuario-ia`, renomeado 10/08/2026; produção, prioridade alta) e `sst-descomplica-cron` (GitHub Action, prioridade média). Ambos os repos clonaram e rodaram sem falhas (`npm install` + `npm audit` + `npm outdated` completos em `calima`; `sst-descomplica-cron` não tem manifesto). Nenhuma correção foi aplicada nos repos escaneados — este é só o relatório.

## TL;DR

- **P0: 1** — `multer` 2.2.0 no `calima` (rota `/api/transcribe`, produção) tem **3 CVEs HIGH (CVSS 7.5), DoS remoto sem autenticação e sem workaround**, corrigidas só na 2.3.0 (lançada ~3 dias atrás — `npm audit` ainda não indexou, achado confirmado via changelog oficial + 2 fontes independentes). Junto o achado recorrente (4º ciclo) de `fieldNestingDepth` ausente na config do multer.
- **P1: 1** — recorrente, 4º ciclo sem correção: Dockerfile do `calima` em `node:20-bookworm-slim`, EOL desde 30/04/2026 (~4 meses sem patch de segurança).
- **P2: 4** (contagem abaixo). Nenhum segredo commitado em nenhum dos dois repos (árvore + histórico completo).
- Ação: `npm install multer@2.3.0` em `server/` + configurar `limits.fieldNestingDepth`/`fieldArrayIndexLimit` em `transcribe.js`, e trocar `FROM node:20-bookworm-slim` → `node:22-bookworm-slim` no Dockerfile.

## calima

`npm install` + `npm audit --json` (raiz, workspace `server`) + `npm outdated` rodaram limpos.

| Pacote | Versão atual | Situação | Achado |
|---|---|---|---|
| `multer` | 2.2.0 | **P0 — novo achado + recorrente** | Ver seção dedicada abaixo. |
| `body-parser` | 1.20.5 (transitivo via `express`) | P2 | GHSA-v422-hmwv-36x6 / CVE-2026-12590, severidade Low (CVSS 3.7): limite inválido de tamanho pode silenciosamente desabilitar o enforcement. `server/server.js` usa `express.json({ limit: '256kb' })`, valor válido — vetor específico do advisory não parece disparável aqui, mas a versão instalada está no range afetado (`<1.20.6`). Mesmo achado dos 3 ciclos anteriores. Correção: `npm audit fix` (bump automático via range do `express`, sem breaking change). |
| `express` | 4.22.2 | P2 | Sem CVE conhecido nesta versão (confirmado no `History.md` oficial — só cita o fix de body-parser acima, ainda "Unreleased"). `npm outdated` aponta 5.2.1 disponível — major, breaking change de API, não é upgrade de segurança. |
| `better-sqlite3` | 12.11.1 | OK | Sem advisories. `npm outdated` aponta 13.0.3 disponível, mas o projeto **exige ficar em `^12`** (11.x não compila no Node 26) — não recomendo mexer nesta major. |
| `ws` | 8.21.3 | OK | Já na última versão (`npm outdated` não aponta nada). |
| `web-push` | 3.6.7 | OK | Já na última versão. |

### multer — P0 (novo achado real, superpõe o recorrente)

`npm audit` **não** aponta nada para `multer`, mas isso é um falso-negativo por atraso de indexação: a versão 2.3.0 foi publicada há ~3 dias no npm e o feed de advisories que o `npm audit` consulta ainda não pegou. Confirmado via `CHANGELOG.md` oficial do `expressjs/multer` (fetch direto, não resumo) e cruzado com 2 fontes independentes (SentinelOne, cyberpress.org, blog oficial `expressjs.com/2026/02/27/security-releases.html` referenciando o mesmo ciclo de releases):

- **CVE-2026-77078** (GHSA-wc9g-mqfw-jrwm) — HIGH, CVSS 7.5. Duas fields de texto malformadas em uma requisição `multipart/form-data` disparam `RangeError: Invalid array length` não capturado, derrubando o processo Node inteiro. Sem workaround — só upgrade.
- **CVE-2026-77037** (GHSA-qfvm-cv95-jqjf) — HIGH, CVSS 7.5. Vazamento de file descriptor: upload abortado/truncado deixa o stream de escrita aberto; repetir o ataque esgota os descritores do processo.
- **CVE-2026-82333** (GHSA-535w-7cp7-47q4) — HIGH, CVSS 7.5. Índice numérico gigante em nome de campo (`items[4294967294]`) força alocação de array esparso máximo; um segundo campo não-numérico dispara iteração síncrona do array inteiro, travando o event loop.
- CVE-2026-77063 (GHSA-qvfw-j98x-7q72) — Low, CVSS 3.7. Bypass de `limits.fileSize` com `fileFilter` assíncrono (menor prioridade, mesma correção).

Todas afetam qualquer versão `< 2.3.0`, sem exigir autenticação **do multer em si** — mas no `calima` a rota `/api/transcribe` fica atrás de `requireAuth(db)` + `requireEscrita` (`server/server.js:79`). Isso não elimina o risco: `SIGNUP_ABERTO` é `true` por padrão (`server/lib/env.js:128`), então qualquer atacante pode se autocadastrar via trial e depois derrubar o processo com uma única requisição multipart malformada — sem custo, sem precisar de plano pago.

**Achado recorrente (4º ciclo, ainda não corrigido):** `server/routes/transcribe.js:7-9` continua sem `limits.fieldNestingDepth`:
```js
const upload = multer({
  storage: multer.memoryStorage(),
  limits: { fileSize: MAX_AUDIO_BYTES },
  ...
```
A 2.3.0 adiciona também `limits.fieldArrayIndexLimit` (mitigação opcional específica para o CVE-2026-82333). Como não há workaround para os 3 CVEs HIGH sem fazer upgrade de versão, a correção de config sozinha (como recomendado nos ciclos anteriores) **não é mais suficiente** — o upgrade de versão passou a ser obrigatório.

### Dockerfile / versão do Node — P1, ainda aberto (4º ciclo)

`Dockerfile` continua em `node:20-bookworm-slim` nos dois estágios (`builder` e final). Node.js 20 ("Iron") saiu de LTS em 30/04/2026 — hoje, 01/09/2026, são **~4 meses** rodando em produção sem patch de segurança do próprio projeto Node. O CI (`.github/workflows/test.yml`) já roda em `node-version: 22` — só a imagem de produção ficou para trás.

- **Correção:** trocar `FROM node:20-bookworm-slim` por `FROM node:22-bookworm-slim` (Active LTS) nas duas linhas `FROM`.
- **Risco de quebra:** baixo — `better-sqlite3@12.11.1` já tem prebuilds para Node 22+, `express`/`multer` só exigem `"node": ">=18"`, e o CI já valida nessa versão. Testar o build da imagem antes do deploy.

### Segredos e .gitignore

- Varredura por `gsk_`, `AIza`, `$aact_`, `RESEND_`, `sk-`, `sk-ant-`, em arquivos versionados e em todo o histórico de commits (`git log --all -p`): **nenhuma ocorrência**.
- Único arquivo relacionado a env versionado é `server/.env.example`, só com placeholders vazios/comentados.
- `.gitignore` cobre `.env`, `.env.local`, `.env.*.local`, `server/.env`, `*.log`, `*.db`, `*.db-*`, `data/*` — correto.

### GitHub Actions do calima

`.github/workflows/test.yml` usa `actions/checkout@v4` e `actions/setup-node@v4` — **tag mutável, não SHA pinado**. Risco baixo na prática (actions oficiais do GitHub, workflow só roda testes, sem `secrets` expostos, `permissions` não elevadas), mas é o mesmo padrão de risco de supply chain que o escopo pede para checar. Entra na contagem P2.

### Contagem P2

- `body-parser` 1.20.5 → 1.20.6 (Low, DoS via limite inválido) — detalhado acima.
- `express` desatualizado (major 4→5, sem CVE) — detalhado acima.
- `better-sqlite3` 12.11.1 → 13.0.3 disponível, sem CVE, **não mexer** (requisito do projeto).
- `.github/workflows/test.yml`: `actions/checkout@v4` / `actions/setup-node@v4` em tag, não SHA — baixo risco, mas fora do padrão de supply-chain hardening.

## sst-descomplica-cron

Repo sem `package.json`/manifesto npm nem `requirements.txt` — confirmado por inspeção da árvore de arquivos. Nada a rodar em `npm audit`/`pip-audit`; isso é esperado, não é falha do scan.

Único arquivo relevante: `.github/workflows/sst-publish.yml`.

- **Pinagem de Actions:** o workflow não usa nenhuma GitHub Action de terceiros — zero linhas `uses:`. Todos os passos são `curl`/`jq` direto no runner. Sem risco de supply chain via tag mutável, porque não há Action externa pra pinar.
- **Permissões:** `permissions: contents: read` no topo — escopo mínimo, correto.
- **Segredo:** `SST_WEBHOOK_TOKEN` referenciado via `${{ secrets.SST_WEBHOOK_TOKEN }}`, passado por env var ao step, nunca hardcoded no YAML.
- **Segredos commitados:** nenhuma ocorrência nos padrões varridos (arquivos + histórico completo).

Sem mudanças desde o scan de 15/08/2026.

## Plano de correção (ordem de prioridade)

1. **[P0 — novo + recorrente]** Em `server/`, atualizar o multer para a 2.3.0:
   ```bash
   cd server && npm install multer@2.3.0
   ```
   (satisfaz o range `^2.0.0` já declarado em `package.json`, não precisa editar o manifesto). Em seguida, em `server/routes/transcribe.js:7-9`, endurecer os `limits`:
   ```js
   const upload = multer({
     storage: multer.memoryStorage(),
     limits: { fileSize: MAX_AUDIO_BYTES, fieldNestingDepth: 2, fieldArrayIndexLimit: 10 },
     fileFilter: ...
   });
   ```
   Sem risco de quebra — a rota só espera um campo de arquivo simples (`upload.single('audio')`), não usa campos aninhados nem arrays.

2. **[P1 — reaberto, 4º ciclo]** Atualizar `Dockerfile`: `node:20-bookworm-slim` → `node:22-bookworm-slim` (duas ocorrências). Testar build local antes do deploy. Node 20 não recebe patch de segurança desde 30/04/2026 e o CI já validou em Node 22.

3. **[P2]** `npm audit fix` em `calima/server` (bump automático `body-parser` → 1.20.6, sem breaking change).

4. **[P2]** Pinar `actions/checkout` e `actions/setup-node` por SHA em `.github/workflows/test.yml` (opcional, risco baixo — workflow sem secrets).

5. **[P2 — opcional, sem urgência]** Avaliar migração major do `express` 4→5 num ciclo dedicado, revisando breaking changes antes.

Nenhum outro achado neste ciclo. `sst-descomplica-cron` segue limpo.

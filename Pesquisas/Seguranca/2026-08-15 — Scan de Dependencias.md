---
title: Scan de Dependências — 2026-08-15
date: 2026-08-15
area: Seguranca
tags: [seguranca, dependencias]
source: routine
---

# Scan de Dependências — 2026-08-15

Escopo: `prontuario-ia` (produção, prioridade alta) e `sst-descomplica-cron` (GitHub Action, prioridade média). Ambos os repos clonaram e rodaram sem falhas (`npm install` + `npm audit` + `npm outdated` completos em `prontuario-ia`; `sst-descomplica-cron` não tem manifesto). Nenhuma correção foi aplicada nos repos escaneados — este é só o relatório.

## Resumo da priorização

- **P0: 1** — mesmo achado dos scans de 15/07 e 01/08, **3º ciclo seguido sem correção**: multer sem `fieldNestingDepth` no caminho de upload.
- **P1: 1** — mesmo achado dos scans anteriores, **ainda não corrigido**: Dockerfile em Node 20, EOL desde 30/04/2026 (já ~3,5 meses sem patch de segurança).
- **P2: 3** (contagem abaixo).
- **Nenhum segredo commitado encontrado** em nenhum dos dois repos (arquivos versionados + histórico completo de commits, `git log --all -p`).

## prontuario-ia

`npm install` + `npm audit --json` (raiz, workspace `server`) rodaram limpos. `npm outdated --json` também.

| Pacote | Versão atual | Situação | Achado |
|---|---|---|---|
| `multer` | 2.2.0 | **P0 — ainda aberto (3º ciclo)** | CVE-2026-5079 / GHSA-72gw-mp4g-v24j, CVSS 7.5 (High): DoS por nomes de campo com aninhamento em colchetes sem limite de profundidade (dependência `append-field`). Corrigido estruturalmente na 2.2.0 com a opção `limits.fieldNestingDepth` — mas a proteção **não é automática**, precisa ser configurada. `server/routes/transcribe.js:7-12` continua com `multer({ storage: memoryStorage(), limits: { fileSize: MAX_AUDIO_BYTES }, fileFilter })`, sem `fieldNestingDepth`. Rota fica atrás de `requireAuth(db)` + `requireEscrita` (`server/server.js:68`), mas isso não elimina o risco: qualquer usuário autenticado — inclusive trial auto-cadastrado (`SIGNUP_ABERTO=true` por padrão) — pode mandar um multipart com campos aninhados e derrubar o processo por exaustão de CPU/memória. Não aparece no `npm audit` porque o problema é de configuração, não de versão instalada; confirmado manualmente via GHSA oficial do `expressjs/multer` e GitLab Advisory DB nesta rodada. |
| `body-parser` | 1.20.5 (transitivo via `express`) | P2 | GHSA-v422-hmwv-36x6, severidade Low (CVSS 3.7): limite inválido de tamanho pode silenciosamente desabilitar o enforcement. `server/server.js` usa `express.json({ limit: '256kb' })`, um valor válido — o vetor específico do advisory não parece disparável aqui, mas a versão instalada está no range afetado (`<1.20.6`). Mesmo achado do scan de 01/08. Correção: `npm audit fix` (bump automático via range do `express`, sem breaking change). |
| `express` | 4.22.2 | P2 | Sem CVE conhecido nesta versão. `npm outdated` aponta 5.2.1 disponível — major, breaking change de API, não é upgrade de segurança. |
| `better-sqlite3` | 12.11.1 | OK | Sem advisories. `npm outdated` aponta 13.0.3 disponível, mas o projeto **exige ficar em `^12`** (11.x não compila no Node 26) — não recomendo mexer nesta major sem pedido explícito. |

### Dockerfile / versão do Node — P1, ainda aberto

`Dockerfile` continua em `node:20-bookworm-slim` nos dois estágios (`builder` e final). **Node.js 20 ("Iron") saiu de LTS em 30/04/2026** — hoje, 15/08/2026, são **~3,5 meses** rodando em produção sem patch de segurança do próprio projeto Node. A janela sem correção só cresce a cada ciclo. Nota: o workflow de CI (`.github/workflows/test.yml`) já roda em `node-version: 22` — só a imagem de produção ficou para trás.

- **Correção:** trocar `FROM node:20-bookworm-slim` por `FROM node:22-bookworm-slim` (Active LTS) nas duas linhas `FROM`.
- **Risco de quebra:** baixo — `better-sqlite3@12.11.1` já tem prebuilds para Node 22+, `express`/`multer` só exigem `"node": ">=18"`, e o CI já valida nessa versão. Testar o build da imagem antes do deploy.

### Segredos e .gitignore

- Varredura por `gsk_`, `AIza`, `$aact_`, `RESEND_`, tokens genéricos (`sk-`, `Bearer ...`), em arquivos versionados e em todo o histórico de commits (`git log --all -p`): **nenhuma ocorrência**.
- Único arquivo relacionado a env versionado é `server/.env.example`, só com placeholders vazios/comentados (ex.: `# RESEND_API_KEY=`).
- `.gitignore` cobre `.env`, `.env.local`, `.env.*.local`, `server/.env`, `*.log`, `*.db`, `*.db-*`, `data/*` — correto.

### Contagem P2

- `body-parser` 1.20.5 → 1.20.6 (Low, DoS via limite inválido) — detalhado acima.
- `express` desatualizado (major 4→5, sem CVE) — detalhado acima.
- `better-sqlite3` 12.11.1 → 13.0.3 disponível, sem CVE, **não mexer** (requisito do projeto).

## sst-descomplica-cron

Repo sem `package.json`/manifesto npm nem `requirements.txt` — confirmado por inspeção da árvore de arquivos. Nada a rodar em `npm audit`/`pip-audit`; isso é esperado, não é falha do scan.

Único arquivo relevante: `.github/workflows/sst-publish.yml`.

- **Pinagem de Actions:** o workflow não usa nenhuma GitHub Action de terceiros — zero linhas `uses:`. Todos os passos são `curl`/`jq` direto no runner. Sem risco de supply chain via tag mutável, porque não há Action externa pra pinar.
- **Permissões:** `permissions: contents: read` no topo — escopo mínimo, correto.
- **Segredo:** `SST_WEBHOOK_TOKEN` referenciado via `${{ secrets.SST_WEBHOOK_TOKEN }}`, passado por env var ao step, nunca hardcoded no YAML.
- **Segredos commitados:** nenhuma ocorrência nos padrões varridos (arquivos + histórico completo).

Sem mudanças desde o scan de 01/08/2026.

## Plano de correção (ordem de prioridade)

1. **[P0 — reaberto, 3º ciclo]** Em `server/routes/transcribe.js:7-12`, adicionar `fieldNestingDepth` ao objeto `limits` do multer:
   ```js
   const upload = multer({
     storage: multer.memoryStorage(),
     limits: { fileSize: MAX_AUDIO_BYTES, fieldNestingDepth: 2 },
     fileFilter: ...
   });
   ```
   Não requer mudança de versão (já em 2.2.0). Sem risco de quebra — a rota só espera um campo de arquivo simples.

2. **[P1 — reaberto]** Atualizar `Dockerfile`: `node:20-bookworm-slim` → `node:22-bookworm-slim` (duas ocorrências). Testar build local antes do deploy. Prioridade cada vez maior — Node 20 não recebe patch de segurança desde 30/04/2026 e o CI já validou em Node 22.

3. **[P2]** `npm audit fix` em `prontuario-ia` (bump automático `body-parser` → 1.20.6, sem breaking change).

4. **[P2 — opcional, sem urgência]** Avaliar migração major do `express` 4→5 num ciclo dedicado, revisando breaking changes antes.

Nenhum outro achado neste ciclo.

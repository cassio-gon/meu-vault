---
title: Scan de Dependências — 2026-07-15
date: 2026-07-15
area: Seguranca
tags: [seguranca, dependencias]
source: routine
---

# Scan de Dependências — 2026-07-15

Escopo: `prontuario-ia` (produção, prioridade alta) e `sst-descomplica-cron` (GitHub Action, prioridade média). Ambos os repos clonaram e rodaram sem falhas. Nenhuma correção foi aplicada nos repos escaneados — este é só o relatório.

## Resumo da priorização

- **P0: 1** — multer em produção no caminho de upload sem a mitigação de DoS configurada.
- **P1: 1** — imagem base Node 20 do Dockerfile já passou do fim de suporte.
- **P2:** ver contagem abaixo.
- **Nenhum segredo commitado encontrado** em nenhum dos dois repos.

## prontuario-ia

`npm audit` (raiz + `server/`, com `node_modules` instalado numa cópia isolada em scratch — nada foi instalado no clone real) voltou **0 vulnerabilidades** nas duas rodadas. Isso não fechou o caso sozinho: cruzei manualmente as 3 dependências diretas contra o GitHub Advisory Database.

| Pacote | Versão atual | Situação | Achado |
|---|---|---|---|
| `multer` | 2.2.0 | **P0** | Versão é a "corrigida" para GHSA-72gw-mp4g-v24j (CVE-2026-5079, DoS por aninhamento profundo de campos multipart, CVSS 7.5 High) e GHSA-3p4h-7m6x-2hcm (CVE-2026-5038, Moderate). Mas a correção **não é automática**: o multer só passou a aceitar a opção `limits.fieldNestingDepth`, com default `Infinity` — ou seja, sem configurar essa opção explicitamente, o app continua exposto mesmo na versão corrigida. `server/routes/transcribe.js:7-12` usa `multer({ storage: memoryStorage(), limits: { fileSize: MAX_AUDIO_BYTES }, fileFilter })` — **sem `fieldNestingDepth`**. É o único uso de multer no repo. A rota fica atrás de `requireAuth` + `requireEscrita`, mas isso não elimina o risco: qualquer usuário autenticado (inclusive trial) pode mandar um multipart com campos profundamente aninhados e derrubar o processo por exaustão de memória/CPU. |
| `express` | 4.22.2 | P2 | Sem CVE conhecido nesta versão (CVE-2024-43796 e a suspeita CVE-2024-51999 já corrigidas/rejeitadas antes de 4.22.2). `npm outdated` aponta 5.2.1 disponível, mas é major — não é upgrade de segurança, é breaking change de API; não recomendo neste ciclo. |
| `better-sqlite3` | 12.11.1 | OK | Sem advisories publicados no repositório do projeto. Já está na major `^12` exigida — **não mexer**, confirmado que `engines` do pacote no npm aceita Node 20.x/22.x/23.x/24.x/25.x/26.x, então não há amarração a Node 20. |

Nenhuma outra dependência transitiva relevante apareceu no `npm ls --all` fora do que já é coberto pelo audit.

### Dockerfile / versão do Node — P1

`Dockerfile` usa `node:20-bookworm-slim` nos dois estágios. Node.js 20 ("Iron") **saiu de LTS/EOL em 30/04/2026** — hoje (15/07/2026) já são ~2,5 meses sem patch de segurança do próprio projeto Node. Como `better-sqlite3@12.11.1` já declara suporte a Node 22 a 26 (prebuilds inclusos), a troca não deveria exigir tocar em `better-sqlite3`.

- **Correção:** trocar `FROM node:20-bookworm-slim` por `FROM node:22-bookworm-slim` (Active LTS) nas duas linhas `FROM` do Dockerfile.
- **Risco de quebra:** baixo — `better-sqlite3` já suporta a versão via prebuild (não deve precisar compilar do zero), `express`/`multer` não têm restrição de engine além de `"node": ">=18"` em `server/package.json`. Recomendo testar o build da imagem localmente antes de fazer deploy, mas não espero incompatibilidade de API.

### Segredos e .gitignore

- Varredura por padrões `gsk_`, `AIza`, `$aact_`, `RESEND_`, tokens genéricos (`api_key=`, `secret=`, `token=` etc.) em todo o conteúdo versionado: **nenhuma ocorrência**.
- Único arquivo relacionado a env versionado é `server/.env.example` (sem valores reais) e `server/lib/env.js` (código de leitura, sem segredo hardcoded).
- `.gitignore` já cobre `server/.env`, `*.log`, `*.db`, `data/` — correto.

### Contagem P2 (sem detalhe individual)

- `express` desatualizado (major, sem CVE) — 1 item, já detalhado acima por ser o único caso.
- Nenhuma outra dependência com achado de médio/baixo risco ou apenas desatualizada sem CVE.

## sst-descomplica-cron

Repo **não tem `package.json`/manifesto npm** nem `requirements.txt` — confirmado por inspeção direta da árvore de arquivos. Não há o que rodar `npm audit`/`pip-audit` nele; isso é esperado e não é uma falha do scan.

Único arquivo relevante: `.github/workflows/sst-publish.yml`.

- **Pinagem de Actions:** o workflow **não usa nenhuma GitHub Action de terceiros** — não há uma única linha `uses:` no arquivo. Todos os passos são `curl`/`jq` diretos no runner `ubuntu-latest`. Ou seja, não existe risco de supply chain via tag mutável aqui, porque não há Action externa para pinar. Nada a corrigir neste ponto.
- **Permissões:** `permissions: contents: read` no topo do workflow — escopo mínimo, correto.
- **Segredo:** `SST_WEBHOOK_TOKEN` é referenciado corretamente via `${{ secrets.SST_WEBHOOK_TOKEN }}` e passado por env var para o step, nunca aparece hardcoded no YAML.
- **Segredos commitados:** nenhuma ocorrência nos padrões varridos.

## Plano de correção (ordem de prioridade)

1. **[P0]** Em `server/routes/transcribe.js:7-12`, adicionar `fieldNestingDepth` ao objeto `limits` do multer, por exemplo:
   ```js
   const upload = multer({
     storage: multer.memoryStorage(),
     limits: { fileSize: MAX_AUDIO_BYTES, fieldNestingDepth: 2 },
     fileFilter: ...
   });
   ```
   Não requer mudança de versão (já está em 2.2.0). Sem risco de quebra — a rota só espera um campo de arquivo simples, não formulários aninhados.

2. **[P1]** Atualizar `Dockerfile`: `node:20-bookworm-slim` → `node:22-bookworm-slim` (duas ocorrências, estágio `builder` e estágio final). Testar build local antes do deploy.

3. **[P2 — opcional, sem urgência]** Avaliar migração major do `express` 4→5 num ciclo futuro dedicado, revisando o changelog de breaking changes antes (mudanças em `req.query`, remoção de métodos depreciados, etc.) — não é item de segurança, é modernização.

Nenhum outro achado neste ciclo.

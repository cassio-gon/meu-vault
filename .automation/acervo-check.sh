#!/bin/bash
# Valida as invariantes das notas vivas do Acervo (camada 2 do acervo de conhecimento).
# Roda em segundos, sem framework. Existe para pegar a degradação silenciosa —
# o único modo de falha do acervo que não grita sozinho.
#
# Uso: acervo-check.sh [caminho-do-vault]   (padrão: a raiz do repo onde o script está)
# Saída: 0 = todas as invariantes ok; 1 = alguma quebrada (lista os problemas).
set -uo pipefail
export PATH="/usr/bin:/bin:/usr/sbin:/sbin:/opt/homebrew/bin"

VAULT="${1:-$(cd "$(dirname "$0")/.." && pwd)}"
ACERVO="$VAULT/Acervo"
MAX_BULLETS=15

ERRS=$(mktemp)
INDEX=$(mktemp)
trap 'rm -f "$ERRS" "$INDEX"' EXIT

# erro() escreve em arquivo, não em variável: as checagens rodam dentro de
# pipelines (subshell), e um contador em variável se perderia ao sair delas.
erro() { echo "✗ $1" >> "$ERRS"; }

[ -d "$ACERVO" ] || { echo "✗ $ACERVO não existe"; exit 1; }

shopt -s nullglob
notas=("$ACERVO"/*.md)
if [ ${#notas[@]} -eq 0 ]; then
  echo "nenhuma nota viva em $ACERVO — nada a validar"
  exit 0
fi

# Índice de nomes de nota do vault inteiro: o Obsidian resolve wikilink por nome
# de arquivo, em qualquer pasta. Montado uma vez só.
find "$VAULT" -name '*.md' -not -path '*/.git/*' -exec basename {} .md \; | sort -u > "$INDEX"

for nota in "${notas[@]}"; do
  base=$(basename "$nota")

  # Invariante 1 — frontmatter tem a data da última evidência.
  if ! grep -qE '^atualizado: [0-9]{4}-[0-9]{2}-[0-9]{2}$' "$nota"; then
    erro "$base: falta 'atualizado: AAAA-MM-DD' no frontmatter"
  fi

  # Recorta a seção "O que sabemos hoje" (até o próximo ##) uma vez só.
  secao=$(awk '/^## O que sabemos hoje/{f=1;next} /^## /{f=0} f' "$nota")

  # Invariante 2 — teto de bullets, para a nota poder esquecer.
  bullets=$(printf '%s\n' "$secao" | grep -c '^- ' || true)
  if [ "$bullets" -gt "$MAX_BULLETS" ]; then
    erro "$base: $bullets bullets em 'O que sabemos hoje' (teto: $MAX_BULLETS)"
  fi

  # Invariante 3 — todo fato termina em âncora. Fato sem âncora é fato inventado.
  printf '%s\n' "$secao" | grep '^- ' | grep -v ']]' | while IFS= read -r linha; do
    erro "$base: fato sem âncora → $(printf '%.60s' "$linha")"
  done

  # Invariante 4 — todo wikilink aponta para nota que existe.
  # Tira alias (|) e âncora de heading (#) antes de comparar.
  grep -o '\[\[[^]]*\]\]' "$nota" \
    | sed 's/^\[\[//; s/\]\]$//; s/|.*$//; s/#.*$//' \
    | sort -u | while IFS= read -r alvo; do
      [ -z "$alvo" ] && continue
      grep -qxF "$alvo" "$INDEX" || erro "$base: wikilink quebrado → [[$alvo]]"
    done
done

if [ -s "$ERRS" ]; then
  cat "$ERRS"
  echo "— $(wc -l < "$ERRS" | tr -d ' ') problema(s) em ${#notas[@]} nota(s)."
  exit 1
fi

echo "✓ ${#notas[@]} nota(s) viva(s), todas as invariantes ok."
exit 0

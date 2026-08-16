# Playbook do Acervo (camada 2 — notas vivas)

Fonte da verdade do comportamento das notas vivas. Quem consome: o comando
`/acervo` (ingestão de pesquisas) e a Routine dos digests (consolidação diária).

⚠️ **Não duplicar estas regras no prompt da Routine.** O prompt deve apenas
apontar para este arquivo. Regra escrita em dois lugares diverge — foi o que
causou o bug das imagens em 02/07/2026.

## Formato da nota viva

Uma nota por tema, em `Acervo/<Tema em linguagem natural>.md`:

```markdown
---
tema: Prontuário Eletrônico com IA
tipo: nota-viva
criado: 2026-06-28
atualizado: 2026-08-13
tags: [acervo, ia, saude]
---

## O que sabemos hoje
- Médicos gastam ~2h/dia digitando prontuário. [[2026-08-10 — Pesquisa: tempo digitando]]

## Como isso mudou
- 2026-06-28 — primeira leitura do tema, mercado dominado por teclado.

## Em aberto
- Ninguém mediu adesão real depois de 90 dias.

## Origens
[[2026-08-13 — Pesquisa: ditado por voz]] · [[2026-08-10 12h00 — IA Digest]]
```

O nome do arquivo é o próprio tema, em linguagem natural, para o wikilink do
Obsidian resolver sem alias.

## As cinco regras anti-degradação

1. **`Como isso mudou` é append-only.** Só acrescentar linha no fim. Nunca
   reescrever, nunca "enxugar" o histórico. Se a síntese do topo degradar, o log
   preserva a trajetória.
2. **Todo fato carrega âncora.** Cada bullet de `O que sabemos hoje` termina num
   wikilink para a nota de origem. Fato sem âncora é fato inventado e pode ser
   removido sem perda.
3. **Reescrita é edição cirúrgica.** Usar `Edit` pontual. **Nunca** reescrever a
   nota do zero — se o texto antigo não volta a passar pelo modelo, ele não
   pode se deformar.
4. **A nota viva nunca é a única cópia.** O digest e o raw ficam intactos. Cada
   reescrita é um commit; `git log -p Acervo/` é o desfazer.
5. **Teto de 15 bullets** em `O que sabemos hoje`. Ao estourar, o mais antigo ou
   o menos ancorado desce para o log. Mente que aprende também descarta.

## Dedupe por URL

Antes de acrescentar um fato, conferir as fontes já citadas na própria nota.
URL já registrada não vira fato novo — vira, no máximo, uma linha no log
dizendo que o assunto voltou.

## Datas não se disfarçam

`atualizado` recebe a data da evidência mais recente que entrou na nota, não a
data em que o arquivo foi tocado. Nota alimentada por pesquisa de junho continua
`atualizado: 2026-06-28` até chegar coisa nova. Sem isso, afirmação velha é lida
como atual daqui a seis meses.

## Como decidir se um tema foi "tocado"

Um tema foi tocado quando alguma notícia do dia trata do mesmo assunto do campo
`tema` da nota. Na dúvida, **não tocar**: nota parada é barata, nota poluída não.
Nenhum tema tocado é o resultado normal da maioria dos dias.

## Validação

Depois de qualquer escrita em `Acervo/`, rodar:

```bash
/Users/cassiogoncalves/.claude/tools/acervo/acervo-check.sh
```

Exit `0` é obrigatório antes do commit. Se falhar, corrigir a nota — nunca
afrouxar o validador.

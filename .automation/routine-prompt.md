# Prompt ATUAL da Routine "Digests do Vault — diário"

> Versão 2026-08-29. Mudanças desta versão: áreas **Puerperio** e **RN** desativadas
> (6 áreas restantes) e busca ancorada nos **5 sites fixos por área** de
> `.automation/area-sources.md`.
> Rollback da versão anterior: `.automation/routine-prompt-backup.md`.

```
Você está numa sessão fresca de nuvem com o repositório meu-vault já clonado no diretório de trabalho. Sua tarefa de hoje:

1. Leia .automation/digest-playbook.md e .automation/area-sources.md e execute-os INTEGRALMENTE para a data de hoje. O playbook é a fonte da verdade do formato e do fluxo; o area-sources é a fonte da verdade das FONTES.

2. São 6 áreas, todas rodam todo dia, nesta ordem exata: IA, Saude, MedTrab, MercFin, Filmes, Jogos. As áreas Puerperio e RN foram DESATIVADAS — não gere digest para elas, não crie arquivo em Pesquisas/Puerperio nem em Pesquisas/RN, e não as conte como falha nem como área pulada.

3. Busca — cada área tem 5 SITES ÂNCORA em .automation/area-sources.md. Para cada área, faça 5 buscas `site:` (uma por site âncora, somando o tema do dia) + 1 busca aberta do tema da área, e monte o digest priorizando o que veio desses 5 sites. Fonte fora da lista só entra se for claramente relevante, datada e de veículo confiável — nunca blog agregador nem site que só republica release. Os 5 âncoras de cada área são:
   - IA: techcrunch.com, technologyreview.com, arstechnica.com, olhardigital.com.br, tecnoblog.net
   - Saude: g1.globo.com/saude, veja.abril.com.br/saude, agenciabrasil.ebc.com.br, folha.uol.com.br/equilibrioesaude, sciencedaily.com
   - MedTrab: protecao.com.br, gov.br/trabalho-e-emprego, conjur.com.br, tst.jus.br, ilo.org
   - MercFin: infomoney.com.br, moneytimes.com.br, valor.globo.com, exame.com, neofeed.com.br
   - Filmes: omelete.com.br, adorocinema.com, variety.com, deadline.com, hollywoodreporter.com
   - Jogos: br.ign.com, tecmundo.com.br/voxel, adrenaline.com.br, gamespot.com, polygon.com

4. Use SOMENTE WebSearch e WebFetch — NUNCA firecrawl (sem créditos). WebSearch é a ferramenta principal e traz título, URL real e data nos próprios snippets. Os grandes portais bloqueiam o WebFetch com 403, então NÃO dependa dele; não use WebFetch por padrão.

5. Siga o formato de nota, os CÓDIGOS curtos de área (IA, Saude, MedTrab, MercFin, Filmes, Jogos) em filename/title/area/heading, e o dedupe de 3 dias EXATAMENTE como o playbook descreve. NÃO inclua imagens nos digests.

6. Fechamento git único do playbook: git add Pesquisas/ → commit → git pull --rebase origin main → git push origin main. Se o git push falhar com 403 do proxy, use a integração do GitHub (push_files) para gravar os arquivos de Pesquisas/ na branch main.

7. Relatório final: quantas áreas geraram nota, quais áreas foram puladas e quais falharam, com 1 linha de motivo cada.

ETAPA FINAL — ACERVO (só depois do commit dos digests estar feito):

8. Leia .automation/acervo-playbook.md e siga-o à risca. Ele é a fonte da verdade do formato e das regras da camada 2; este prompt não as repete de propósito.
9. Rode ls Acervo/ para ver os temas vivos. NÃO leia o conteúdo de todos.
10. Decida quais temas as notícias de hoje tocaram. Nenhum tocado é o resultado normal da maioria dos dias — nesse caso, encerre aqui sem escrever nada.
11. Só para os tocados: leia a nota e faça edição cirúrgica com Edit. Nunca reescreva a nota do zero.
12. Commit SEPARADO do commit dos digests: git add Acervo/ && git commit -m "acervo: <temas tocados>" → git pull --rebase origin main → git push origin main.
13. No relatório final, informe quais temas foram tocados (ou "nenhum").

Se algo falhar na etapa de acervo, os digests já estão salvos e commitados — não tente desfazê-los.

Não altere nada fora de Pesquisas/ e Acervo/.
```

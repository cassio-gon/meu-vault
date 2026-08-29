# Prompt ATUAL da Routine "Digests do Vault — diário"

> Versão 2026-08-29 (rev. 2, após run de teste). Mudanças: áreas **Puerperio** e **RN** desativadas
> (6 áreas restantes) e busca ancorada nos **5 sites fixos por área** de
> `.automation/area-sources.md`.
> Rollback da versão anterior: `.automation/routine-prompt-backup.md`.

```
Você está numa sessão fresca de nuvem com o repositório meu-vault já clonado no diretório de trabalho. Sua tarefa de hoje:

1. Leia .automation/digest-playbook.md e .automation/area-sources.md e execute-os INTEGRALMENTE para a data de hoje. O playbook é a fonte da verdade do formato e do fluxo; o area-sources é a fonte da verdade das FONTES.

2. São 6 áreas, todas rodam todo dia, nesta ordem exata: IA, Saude, MedTrab, MercFin, Filmes, Jogos. As áreas Puerperio e RN foram DESATIVADAS — não gere digest para elas, não crie arquivo em Pesquisas/Puerperio nem em Pesquisas/RN (essas pastas foram removidas do repo), e não as conte como falha nem como área pulada.

3. Busca — cada área tem 5 SITES ÂNCORA em .automation/area-sources.md. Para cada área, faça 5 buscas `site:` (uma por site âncora, somando o tema do dia) + 1 busca aberta do tema da área, e monte o digest priorizando o que veio desses 5 sites. Fonte fora da lista só entra se for claramente relevante, datada e de veículo confiável — nunca blog agregador nem site que só republica release. Os 5 âncoras de cada área são:
   - IA: techcrunch.com, technologyreview.com, arstechnica.com, olhardigital.com.br, tecnoblog.net
   - Saude: g1.globo.com, veja.abril.com.br, agenciabrasil.ebc.com.br, folha.uol.com.br, sciencedaily.com
   - MedTrab: protecao.com.br, gov.br, conjur.com.br, tst.jus.br, ilo.org
   - MercFin: infomoney.com.br, moneytimes.com.br, valor.globo.com, exame.com, neofeed.com.br
   - Filmes: omelete.com.br, adorocinema.com, variety.com, deadline.com, hollywoodreporter.com
   - Jogos: br.ign.com, tecmundo.com.br, adrenaline.com.br, gamespot.com, polygon.com

4. DUAS REGRAS DE QUERY, obrigatórias: (a) `site:` sempre com DOMÍNIO NU, sem caminho — `site:g1.globo.com saúde` funciona, `site:g1.globo.com/saude` devolve lixo; (b) NUNCA ponha data na query ("agosto 2026", "August 29 2026") — isso puxa retrospectiva e artigo velho; a data você lê no snippet. Se uma busca `site:` voltar resultado fora do domínio pedido, descarte e siga sem insistir.

5. Use SOMENTE WebSearch e WebFetch — NUNCA firecrawl (sem créditos). WebSearch é a ferramenta principal e traz título, URL real e data nos próprios snippets. Os grandes portais bloqueiam o WebFetch com 403, então NÃO dependa dele; não use WebFetch por padrão.

6. Siga o formato de nota, os CÓDIGOS curtos de área (IA, Saude, MedTrab, MercFin, Filmes, Jogos) em filename/title/area/heading, e o dedupe de 3 dias EXATAMENTE como o playbook descreve. NÃO inclua imagens nos digests.

7. Fechamento git único do playbook: git add Pesquisas/ → commit → git pull --rebase origin main → git push origin HEAD:main. ATENÇÃO: você provavelmente está em detached HEAD — isso é NORMAL neste ambiente e não significa que há trabalho por enviar. NÃO rode git checkout main, git stash, git reset --hard nem git merge; só commite e empurre com HEAD:main. Se o git push falhar com 403 do proxy, use a integração do GitHub (push_files) para gravar os arquivos de Pesquisas/ na branch main.

8. Relatório final: quantas áreas geraram nota, quais áreas foram puladas e quais falharam, com 1 linha de motivo cada.

ETAPA FINAL — ACERVO (só depois do commit dos digests estar feito):

9. Leia .automation/acervo-playbook.md e siga-o à risca. Ele é a fonte da verdade do formato e das regras da camada 2; este prompt não as repete de propósito.
10. Rode ls Acervo/ para ver os temas vivos. NÃO leia o conteúdo de todos.
11. Decida quais temas as notícias de hoje tocaram. Nenhum tocado é o resultado normal da maioria dos dias — nesse caso, encerre aqui sem escrever nada.
12. Só para os tocados: leia a nota e faça edição cirúrgica com Edit. Nunca reescreva a nota do zero.
13. Commit SEPARADO do commit dos digests: git add Acervo/ && git commit -m "acervo: <temas tocados>" → git pull --rebase origin main → git push origin HEAD:main.
14. No relatório final, informe quais temas foram tocados (ou "nenhum").

Se algo falhar na etapa de acervo, os digests já estão salvos e commitados — não tente desfazê-los.

Não altere nada fora de Pesquisas/ e Acervo/.
```

# Prompt ATUAL da Routine "Digests do Vault — diário"

> Versão 2026-10-19. Mudança: a busca passou para o `web_scrape` do conector `agente-web`
> nas páginas de seção dos âncoras (URLs em `.automation/area-sources.md`), e as fotos
> voltaram, só quando vêm na própria coleta. WebSearch ficou para os 3 âncoras de MedTrab
> que bloqueiam o coletor, para a busca aberta e para o plano B. O conector `agente-web`
> foi anexado à Routine em `mcp_connections`.
> Rollback da versão anterior: `.automation/routine-prompt-backup.md`.

```
Você está numa sessão fresca de nuvem com o repositório meu-vault já clonado no diretório de trabalho. Sua tarefa de hoje:

1. Leia .automation/digest-playbook.md e .automation/area-sources.md e execute-os INTEGRALMENTE para a data de hoje. O playbook é a fonte da verdade do formato e do fluxo; o area-sources é a fonte da verdade das FONTES.

2. São 6 áreas, todas rodam todo dia, nesta ordem exata: IA, Saude, MedTrab, MercFin, Filmes, Jogos. As áreas Puerperio e RN foram DESATIVADAS — não gere digest para elas, não crie arquivo em Pesquisas/Puerperio nem em Pesquisas/RN (essas pastas foram removidas do repo), e não as conte como falha nem como área pulada.

3. Busca — cada área tem 5 SITES ÂNCORA em .automation/area-sources.md, cada um com a URL da página de seção (ou do feed RSS) e o modo: coleta ou busca. Para cada área: (a) um web_scrape do conector agente-web por âncora de modo coleta, SEMPRE com fallback: false e maxChars: 6000 (e waitFor quando o area-sources indicar); (b) uma busca `site:` no WebSearch por âncora de modo busca; (c) uma busca aberta no WebSearch do tema da área. Depois de escolher os tópicos, faça um web_scrape da própria matéria de cada tópico (fallback: false, maxChars: 3000): é dele que saem o resumo, a data confirmada e a foto. Fonte fora da lista só entra se for claramente relevante, datada e de veículo confiável — nunca blog agregador nem site que só republica release.

4. DUAS REGRAS DE QUERY no WebSearch, obrigatórias: (a) `site:` sempre com DOMÍNIO NU, sem caminho — `site:g1.globo.com saúde` funciona, `site:g1.globo.com/saude` devolve lixo; (b) NUNCA ponha data na query ("agosto 2026", "August 29 2026") — isso puxa retrospectiva e artigo velho; a data você lê no snippet. Se uma busca `site:` voltar resultado fora do domínio pedido, descarte e siga sem insistir.

5. Ferramentas: web_scrape do conector agente-web é a principal (ela chega como ferramenta adiada: carregue antes com ToolSearch, consulta "select:mcp__agente-web__web_scrape"); WebSearch só nos três usos do item 3. NUNCA use WebFetch (os portais dão 403) nem o conector firecrawl (sem créditos) — o agente-web é outro serviço e pode. Se o conector agente-web não existir na sessão, ou se TODAS as coletas de uma área falharem, faça essa área no modo antigo: uma busca `site:` no WebSearch por âncora (domínio do âncora) + a busca aberta, sem fotos.

6. Siga o formato de nota, os CÓDIGOS curtos de área (IA, Saude, MedTrab, MercFin, Filmes, Jogos) em filename/title/area/heading, e o dedupe de 3 dias EXATAMENTE como o playbook descreve. Foto: inclua a linha <img> de um tópico SÓ com a URL de imagem que veio na coleta (card da página de seção ou matéria coletada), seguindo a seção "Foto do tópico" do playbook. Nunca invente nem busque foto em outro lugar; sem foto válida, o tópico sai sem foto.

7. Fechamento git único do playbook: git add Pesquisas/ → commit → git pull --rebase origin main → git push origin HEAD:main. ATENÇÃO: você provavelmente está em detached HEAD — isso é NORMAL neste ambiente e não significa que há trabalho por enviar. NÃO rode git checkout main, git stash, git reset --hard nem git merge; só commite e empurre com HEAD:main. Se o git push falhar com 403 do proxy, use a integração do GitHub (push_files) para gravar os arquivos de Pesquisas/ na branch main.

8. Relatório final: quantas áreas geraram nota, quais áreas foram puladas e quais falharam, com 1 linha de motivo cada; e, por área, quantas coletas do agente-web funcionaram, quantos tópicos saíram com foto e se alguma área caiu no modo antigo.

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

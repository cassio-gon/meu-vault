# Backup do prompt da Routine — antes da etapa de acervo

> Capturado em 2026-08-16 via `RemoteTrigger action: get`.
> Routine `Digests do Vault — diário`, `trigger_id: trig_018SJ1Au6eYbRA1YAJjk8dgU`,
> cron `0 9 * * *` UTC (06:00 BRT), modelo `claude-sonnet-4-6`.
>
> Este é o rollback. Se a etapa de acervo causar problema, restaurar o texto
> abaixo com `RemoteTrigger action: update`.

```
Você está numa sessão fresca de nuvem com o repositório meu-vault já clonado no diretório de trabalho. Sua tarefa de hoje:

1. Leia .automation/digest-playbook.md e execute-o INTEGRALMENTE para a data de hoje. O playbook é a fonte da verdade — siga-o à risca, inclusive a cadência por área (algumas áreas não rodam todo dia).
2. Gere o digest de cada área elegível hoje, na ordem exata do playbook. Use SOMENTE WebSearch e WebFetch — NUNCA firecrawl (sem créditos). WebSearch é a ferramenta principal para achar os tópicos do dia (título, URL real, data); os grandes portais bloqueiam o WebFetch com 403, então NÃO dependa dele — use os sites de .automation/area-sources.md como pista de busca (ex.: site:infomoney.com.br). Não use WebFetch por padrão.
3. Siga o formato de nota, os CÓDIGOS curtos de área (IA, Saude, MedTrab, MercFin, Puerperio, RN, Filmes, Jogos) em filename/title/area/heading, e o dedupe de 3 dias EXATAMENTE como o playbook descreve. NÃO inclua imagens nos digests.
4. Fechamento git único do playbook: git add Pesquisas/ → commit → git pull --rebase origin main → git push origin main. Se o git push falhar com 403 do proxy, use a integração do GitHub (push_files) para gravar os arquivos de Pesquisas/ na branch main.
5. Relatório final: quantas áreas geraram nota, quais áreas foram puladas e quais falharam, com 1 linha de motivo cada.

Não altere nada fora de Pesquisas/.
```

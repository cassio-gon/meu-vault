---
title: Vigia de Concorrência — 2026-08-14
date: 2026-08-14
area: Concorrencia
tags: [concorrencia, mercado]
source: routine
---

# Vigia de Concorrência — semana de 2026-08-14

> Comparado contra o relatório de **2026-08-07** (uma semana de intervalo). Reporta só o que é
> genuinamente novo ou que os relatórios anteriores não tinham capturado.

## Achados

1. **Meta Business Agent confirmado na fonte oficial — e exclui a vertical Saúde.** A
   documentação oficial (`developers.facebook.com/documentation/meta-business-agent/overview`,
   atualizada 10/08/2026) confirma o que só vinha de fonte secundária até semana passada: o
   agente **orquestra de verdade** — "toma ações através dos seus próprios sistemas (como
   consultar um pedido ou **agendar uma consulta**)" e usa webhooks para "agendar uma consulta ou
   **confirmar um pagamento**". Preço confirmado: US$2,00/milhão de tokens desde 01/08/2026
   (~US$0,04–0,05/mensagem), faturado em BRL para contas brasileiras. **Mas a mesma página lista
   os requisitos de elegibilidade e exclui explicitamente "Finanças, Governo, Saúde, Álcool,
   Jogos de azar..."** — clínicas categorizadas como Saúde no perfil WhatsApp Business **não são
   elegíveis** para o Business Agent. Fontes:
   [developers.facebook.com](https://developers.facebook.com/documentation/meta-business-agent/overview)
   e [about.fb.com/news/2026/06/meta-business-agent](https://about.fb.com/news/2026/06/meta-business-agent)
   (anúncio original 03/06/2026), lidas 14/08/2026. **E daí pro Cássio:** é o oposto do que a
   leitura preliminar da semana passada temia — a Meta orquestra sim (confirma que a ameaça é
   qualitativamente real), mas se autoexclui do nosso segmento. Ponto a verificar antes de
   descartar de vez: confirmar que as clínicas-cliente de fato estão/ficam categorizadas como
   "Saúde" no cadastro WhatsApp Business (e não em alguma categoria genérica tipo "Serviços
   profissionais" que escaparia da exclusão).

2. **Telepatia AI mapeada — não é concorrente direto do Calima.** Startup incubada em Stanford,
   captou US$9M seed (10/2025) + US$33M Series A (a16z, 07/2026) = US$42M. Produto é copiloto
   clínico completo (transcrição + sugestão de conduta + integração com +50 sistemas
   hospitalares tipo Epic/TASY/MV + BI), não um scribe simples. **Preço: grátis para médico de
   consulta privada** — o modelo é B2B2C, monetiza hospital/operadora, não o médico individual.
   Meta declarada: 20 mil médicos no Brasil até fim de 2026. Fontes:
   [telepatia.ai/en](https://www.telepatia.ai/en),
   [ColombiaOne](https://colombiaone.com/2026/07/09/telepatia-ai-42-million-funding/) (09/07/2026),
   checadas 14/08/2026. **E daí pro Cássio:** não compete pelo mesmo bolso do Calima hoje (foco
   institucional/hospital, grátis pro médico solo), mas é o tipo de player que pode virar
   pressão de preço se algum dia pivotar pra PF/pequena clínica — grátis pro médico é hoje uma
   ameaça de posicionamento, não de receita direta.

3. **Voa Health — concorrente brasileiro de scribe médico não mapeado antes.** Startup nacional
   (fundada 2023), aporte de US$3M da Prosus Ventures (02/2025), já reivindica +60 mil médicos
   impactados e +1M consultas; lançou V3 do produto no início de 2026 mirando virar "hub de
   agentes de IA para saúde". Sem preço público encontrado. Fontes:
   [startups.com.br](https://startups.com.br/negocios/um-ano-apos-aporte-da-prosus-voa-health-da-novos-passos/),
   [Bloomberg Línea](https://www.bloomberglinea.com.br/startups/prosus-investe-em-startup-brasileira-que-mira-ser-um-hub-de-agentes-de-ia-para-saude/),
   checadas 14/08/2026. **E daí pro Cássio:** entra no radar como concorrente nacional direto de
   porte real (capital + escala de usuários já visível); preço "não público" — investigar mystery
   shop na próxima rodada.

4. **Nenhuma mudança de preço nos ERPs/concorrentes já mapeados esta semana** — Feegow (Starter
   R$129/Plus R$199/VIP R$249), Simples Dental (R$149,90–R$349,90, IA de voz ainda add-on à
   parte), Dr. Agenda (R$70 promo + R$40/agenda exame), Clinicorp IA (R$299/mês de R$499),
   Doctoralia (Starter R$429/Plus R$529/VIP R$679 + Noa Notes R$199) — todos relidos ao vivo
   (`maxAge:0`) em 14/08/2026, valores idênticos à semana passada. **E daí pro Cássio:** semana
   de consolidação, sem sinal de guerra de preço nos ERPs tradicionais.

5. **"Clínica nas Nuvens" esclarecida — é ERP de gestão, não um bot de WhatsApp dedicado.**
   A integração citada pela usesecretariaia.com na semana passada é um sistema de gestão de
   clínica (concorrente de Amplimed/iClinic), não um agente conversacional concorrente direto.
   Preço de R$499/mês com fidelidade de 12 meses aparece só em fonte secundária
   ([bydoctor.com.br](https://bydoctor.com.br)) — **não confirmado diretamente** na página oficial
   (scrape ao vivo não concluído desta vez). usesecretariaia.com manteve o ritmo: 3 posts de blog
   novos (11, 12, 13/08), preço segue "sob consulta". Fonte: usesecretariaia.com, 14/08/2026.
   **E daí pro Cássio:** reduz o alarme de "ERP novo virando bot de WhatsApp"; segue sendo só um
   sistema de gestão tradicional na lista de integrações de um concorrente já monitorado.

6. **Possíveis concorrentes novos descobertos, ainda não confirmados como lançamento recente —
   destaque para o Secretar.AI.** Nas buscas desta semana apareceram Secretar.AI, Pixedoc,
   WorkAI, ia-secretaria.com.br e secretariavirtual.net.br. O mais relevante é o **Secretar.AI**,
   que anuncia um "Agente Financeiro" que emite cobrança Pix — feature quase idêntica ao
   diferencial central da Secretária IA (cobrar Pix antes de confirmar o horário). Nenhum teve
   preço nem data de lançamento confirmados nesta rodada — mapeamento superficial, via busca.
   **E daí pro Cássio:** prioridade #1 da próxima rodada é fazer mystery-shop no Secretar.AI —
   se a cobrança de Pix deixou de ser diferencial exclusivo, isso muda a tese de venda.

7. **CFM 2.454/2026 — sem prorrogação; prazo de adequação vence em ~12 dias (26/08/2026).**
   Nenhuma norma complementar ou prorrogação encontrada até 14/08/2026. Fonte:
   [Conjur](https://www.conjur.com.br/2026-mar-14/resolucao-do-cfm-trata-do-uso-de-inteligencia-artificial-na-medicina/),
   checada 14/08/2026. **E daí pro Cássio:** nada muda hoje, mas o prazo cai dentro da janela do
   próximo vigia — se algo mudar (prorrogação, norma complementar), é nesses ~12 dias.

8. **ANPD — correção de contexto: a consulta de 13/08 era sobre o Sandbox de IA, não sobre
   fiscalização geral de dados de saúde (como o vigia anterior supunha).** A consulta pública de
   13/08/2026 tratava especificamente do **Sandbox Regulatório de IA** — piloto com 3 empresas
   (Metatext, Synapse AI, Prevvine Tecnologia), nenhuma delas concorrente do Calima/Secretária
   IA. Fonte:
   [ConvergenciaDigital](https://convergenciadigital.com.br/governo/anpd-faz-consulta-a-sociedade-sobre-sandbox-regulatorio-de-ia-e-protecao-de-dados/)
   (01/06/2026), checada 14/08/2026. **Não foi possível confirmar se a reunião ocorreu nem o
   resultado** — as páginas de resultado no gov.br retornaram erro de acesso (401); um título
   indexado sugere possível prorrogação da consulta até 01/12/2026, mas sem confirmação de
   conteúdo. **E daí pro Cássio:** menos urgente do que parecia semana passada (não é uma
   fiscalização iminente sobre dados de saúde), mas o resultado real ainda precisa ser checado
   manualmente — Claude for Chrome resolveria o bloqueio de 401 se quiser confirmar.

## Pressão de preço

- **Calima (antes "Prontuário IA"):** ⚠️ **mudança interna a registrar** — o produto deixou de
  ter preço único de R$19,90/mês e passou a uma escada de 4 planos (Teste grátis · Acadêmico
  R$19,90 · Recém-formado R$39,90 · Hipócrates R$79,90/mês ilimitado), em produção desde
  11–13/08/2026. As comparações deste vigia contra "R$19,90" precisam passar a mirar a **escada
  inteira**, não só a entrada. Nenhum concorrente mapeado até hoje (Doctoralia Noa Notes R$199,
  Telepatia grátis-mas-institucional, Voa Health sem preço público) invalida qualquer degrau da
  escada — segue folgado em todos os níveis.
- **Secretária IA:** nenhum piso novo abaixo de R$247/mês confirmado esta semana. O único sinal
  de atenção é o Secretar.AI (achado 6) — preço ainda não verificado; se vier baixo e replicar a
  cobrança de Pix, é o primeiro concorrente a copiar o diferencial central do produto.
- Ninguém identificado dando o serviço de graça no nosso segmento — a única oferta gratuita
  encontrada (Telepatia AI) é institucional/B2B2C, não compete pelo bolso do médico solo ou da
  clínica pequena.

## Comoditização

- **Meta Business Agent (achado 1) é o caso mais importante da semana, e a leitura virou
  ambivalente:** confirma que a Meta orquestra de verdade (achado técnico validado), mas ao
  mesmo tempo **se autoexclui da vertical Saúde** — o que é uma boa notícia direta para a
  Secretária IA, contanto que as clínicas-cliente realmente estejam categorizadas como Saúde no
  WhatsApp Business (ponto a confirmar, não a supor).
- **n8n/Evolution API:** sem checagem nova desta rodada — sem indício de mudança, mas não foi
  revisitado ativamente; retomar checagem ativa na próxima rodada.
- **Secretar.AI (achado 6)** é o primeiro sinal — ainda não confirmado — de um concorrente
  replicando a feature de cobrança Pix, que até aqui era exclusiva da Secretária IA.

## Posicionamento — recomendações

1. **Meta Business Agent: não é mais ameaça de substituição direta, mas verificar a categoria
   WhatsApp Business das clínicas-cliente antes de fechar o assunto.** Se todas estiverem
   corretamente categorizadas como "Saúde", a exclusão de elegibilidade (achado 1) neutraliza o
   risco mapeado nas últimas duas semanas. Prioridade #2 da próxima rodada (atrás do mystery-shop
   do Secretar.AI).

2. **Atualizar a baseline de comparação do Calima para a escada de planos, não mais R$19,90
   isolado.** O piloto grátis de 7 dias (agora "plano Teste") e o degrau de entrada R$19,90
   (Acadêmico) continuam defensáveis — nenhum concorrente mapeado até hoje aperta esse preço.
   Mas os vigias futuros devem comparar contra os 4 degraus (R$19,90/R$39,90/R$79,90), não só
   contra o antigo preço único — é um câmbio de produto real, não só de posicionamento.

3. **Sugestão de mensalidade B2B para a Secretária IA: manter a faixa R$147–197/mês sugerida em
   07/08 (revisão do R$100 fixado em 15/07), sem mudança esta semana** — nenhum piso novo abaixo
   de R$247 apareceu, e o único risco de comoditização de feature (Secretar.AI copiando a
   cobrança de Pix) ainda não tem preço confirmado para recalibrar a faixa. Recomenda-se travar
   essa faixa como decisão formal no script comercial assim que o Secretar.AI for verificado —
   se ele vier abaixo de R$147, a resposta padrão de objeção de preço precisa ser revisada de
   novo antes que o vendedor bata de frente com um concorrente mais barato copiando a mesma
   feature.

## Nota metodológica

Pesquisa feita com 2 agentes em paralelo (concorrentes diretos da Secretária IA + Meta Business
Agent; scribes internacionais + Telepatia AI + regulação). Firecrawl com fetch ao vivo
(`maxAge:0`) funcionou bem para a maioria das páginas de preço relidas esta semana (Feegow,
Simples Dental, Dr. Agenda, Clinicorp, Doctoralia, usesecretariaia.com, Meta developers). A
página oficial de preço da "Clínica nas Nuvens" e as páginas de preço de Ninsáude/Amplimed não
foram relidas ao vivo nesta rodada (orçamento de tempo priorizou a confirmação do Meta Business
Agent, que era a prioridade #1 herdada da semana passada) — retomar na próxima rodada. As páginas
de resultado da consulta pública da ANPD no gov.br deram erro 401 (bloqueio de acesso) — não foi
possível confirmar se a consulta ocorreu ou seu resultado; título indexado sugere possível
prorrogação até 01/12/2026, sem confirmação de conteúdo.

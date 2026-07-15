---
title: Vigia de Concorrência — 2026-07-15
date: 2026-07-15
area: Concorrencia
tags: [concorrencia, mercado]
source: routine
---

# Vigia de Concorrência — semana de 2026-07-15

> **Baseline.** Não há relatório anterior em `Pesquisas/Concorrencia/` — esta é a primeira
> rodada. A partir da próxima semana, os relatórios comparam contra este.

## Achados

1. **Meta vai cobrar por toda resposta de bot no WhatsApp a partir de 01/10/2026** — qualquer
   resposta de atendente humano ou IA de terceiros dentro da janela de 24h passa a custar o
   mesmo de uma mensagem de utilidade (hoje R$ 0,035/mensagem no Brasil). Fonte:
   [mobiletime.com.br, 01/07/2026](https://www.mobiletime.com.br/noticias/01/07/2026/whatsapp-cobra-respostas/).
   **E daí pro Cássio:** o custo de ~R$ 0,30/agendamento da Secretária IA precisa ser
   recalculado incluindo essa taxa por mensagem antes de outubro — pode comer margem, ou pior,
   virar argumento de venda ruim se o cliente notar a cobrança da Meta duplicando a sua.

2. **Meta lançou o "Meta Business Agent" — agente nativo com agendamento via Google Calendar
   embutido no WhatsApp** — plataforma para parceiros desde 01/07/2026 (consumer desde
   03/06/2026), já integra Google Calendar, Shopify, Salesforce e Zendesk para agendar
   compromissos dentro do próprio app. Respostas desse agente nativo ficam **isentas** da
   cobrança por mensagem do achado 1 — só pagam por token (1M tokens = US$ 2, cobrança a
   partir de 01/08/2026). Fontes: [about.fb.com, 06/2026](https://about.fb.com/news/2026/06/meta-business-agent/),
   [surgiu.com.br, 08/07/2026](https://surgiu.com.br/2026/07/08/cobranca-no-whatsapp-api-meta-vai-cobrar-empresas-por-respostas-a-partir-de-outubro/).
   **E daí pro Cássio:** este é o risco de comoditização mais direto que existe hoje — a Meta
   está simultaneamente encarecendo bots de terceiros e oferecendo de graça (via token barato)
   uma alternativa nativa que já agenda compromisso. Vale avaliar se dá pra rodar a Secretária
   IA sobre o Business Agent da própria Meta para escapar da taxa por mensagem.

3. **O stack exato da Secretária IA (n8n + Chatwoot + Evolution API) já está sendo revendido
   como template pronto por terceiros** — o produto "Secretária v2 — N8N + Chatwoot + Evolution
   API" da fazer.ai está à venda no Gumroad, com múltiplas agendas Google Calendar, respostas em
   áudio (TTS) e escalonamento automático. Fonte:
   [fazeraiconsultoria.gumroad.com](https://fazeraiconsultoria.gumroad.com/l/secretaria-n8n-v2).
   **E daí pro Cássio:** o infoproduto de R$ 15 na Kirvano já tem concorrência direta no mesmo
   modelo (DIY, mesma stack) — o diferencial não pode mais ser só "a receita pronta", precisa
   ser suporte/onboarding/prompt afinado (que é justamente o que o B2B consultivo vende).

4. **ANPD abriu processo sancionador contra organização social por vazamento de 500 mil
   prontuários** (ransomware expôs nome, data de nascimento, prontuário, exames e diagnósticos
   de pacientes de unidades públicas de saúde em GO/RS/BA/AL/PI/TO) — multa pode chegar a
   R$ 50 milhões. Fonte:
   [gov.br/anpd, divulgado 08/07/2026](https://www.gov.br/anpd/pt-br/assuntos/noticias/anpd-instaura-processo-de-sancao-contra-organizacao-social-por-falha-na-protecao-de-dados-de-500-mil-pacientes-de-unidades-publicas-de-saude).
   **E daí pro Cássio:** reforça que o argumento "nome do paciente cifrado no cliente" do
   Prontuário IA não é feature de marketing, é blindagem regulatória real — a ANPD está
   fiscalizando dado de saúde ativamente. Vale usar esse caso (sem citar nomes) como gancho de
   copy: "veja o que acontece com prontuário sem cifra".

5. **Amplimed vende um add-on de IA por voz que faz exatamente o que o Prontuário IA faz** —
   "Ampli IA" transcreve a consulta por voz direto no prontuário, vendido à parte por
   ~R$ 120/mês sobre uma base de R$ 89–99/mês (pacote completo fica bem acima de R$ 19,90).
   Fonte: [amplimed.com.br/planos-e-recursos](https://www.amplimed.com.br/planos-e-recursos/)
   (preço não confirmado por leitura direta — WebFetch bloqueado; ver nota metodológica no fim).
   **E daí pro Cássio:** é o concorrente de feature mais próximo encontrado, e ele custa ~6x
   mais que o Prontuário IA quando empacotado — o R$ 19,90 standalone segue com posicionamento
   agressivo frente a esse comparável.

6. **Dragon Copilot (Microsoft/Nuance) cortou preço em 57%** — de US$ 3.528 para
   US$ 1.512/usuário/mês, efetivo em 01/05/2026, com unificação de marca (DAX Copilot + Dragon
   Medical One) e mais de 200 mil médicos usuários. Fonte:
   [schneider.im, 2026](https://www.schneider.im/microsoft-dragon-copilot-price-decrease-licensing-changes/).
   **E daí pro Cássio:** não é concorrente direto no Brasil (preço ainda em outro patamar), mas
   confirma que o mercado global de scribe está sob pressão de preço — sinal de que a categoria
   inteira está comoditizando, o que valida posicionar o Prontuário IA pelo preço baixo agora,
   antes que isso vire padrão esperado.

7. **Telepatia AI (origem Stanford/Colômbia) captou US$ 33 milhões em Series A liderada pela
   a16z**, mirando atender metade dos médicos da América Latina até 2027, já ativa no Brasil.
   Fonte: [Bloomberg, 17/06/2026](https://www.bloomberg.com/news/articles/2026-06-17/ai-health-startup-wants-to-assist-half-of-latin-american-doctors).
   **E daí pro Cássio:** é o player internacional mais bem capitalizado mirando documentação
   médica por IA na América Latina — vale monitorar se lança produto de ditado/prontuário em
   português nos próximos meses.

8. **Voa Health (scribe 100% em português, foco Brasil) passou de 1 milhão de consultas
   transcritas, com 60 mil profissionais usando** o produto. Fonte:
   [blog.voa.health](https://blog.voa.health/blog/novidades-voa-3/voa-health-1-milhao-consultas-ia-medica-45).
   **E daí pro Cássio:** é hoje o concorrente brasileiro de scribe por voz com tração mais visível
   — vale conferir o preço deles (não coletado nesta rodada) na próxima semana.

9. **CFM Resolução 2.454/2026 sofreu retificação em 05/03/2026** (artigos 16 e 17, sobre
   tratamento de dados no desenvolvimento/uso de IA em medicina) — não é resolução nova, mas as
   regras entram em vigor em **26/08/2026**. Fonte:
   [abmes.org.br](https://abmes.org.br/legislacoes/detalhe/5429/resolucao-cfm-n-2.454).
   **E daí pro Cássio:** prazo real se aproximando — vale conferir se o Prontuário IA já cumpre
   a redação retificada dos artigos 16/17 antes de 26/08.

10. **Levantamento de preços dos concorrentes de agenda de clínica** (iClinic R$ 99–169/mês,
    Ninsáude R$ 199/mês, Shosp R$ 149–229/mês, Amplimed R$ 89–99/mês base) — nenhum abaixo de
    R$ 19,90 como sistema completo, nenhum de graça. Doctoralia e Dr. Agenda: preço **não
    público**. Feegow e Simples Dental: valores encontrados só em fontes secundárias, não
    confirmados na página oficial (ver nota metodológica). **E daí pro Cássio:** nenhuma pressão
    de preço vindo desses sistemas de agenda tradicionais — a pressão real está em cima (achados
    1–3, Meta) e não embaixo.

## Pressão de preço

- **Ninguém está abaixo de R$ 19,90/mês** entre os sistemas de gestão de clínica pesquisados
  (todos cobram por profissional, R$ 89 a R$ 229/mês).
- **O mais próximo de "de graça" é o Meta Business Agent** (achado 2) — não é um concorrente de
  prontuário/agenda tradicional, mas se a Meta oferece agendamento nativo cobrado a centavos por
  token, isso pressiona o valor percebido de qualquer camada paga por cima do WhatsApp,
  incluindo a Secretária IA.
- **O infoproduto de R$ 15 (Kirvano) já tem equivalente direto à venda** (achado 3) — pressão de
  preço lateral, não de cima para baixo.

## Comoditização

- **Meta é o risco real, não n8n/Chatwoot/Evolution API.** A stack de automação em si (n8n,
  Chatwoot, Evolution API) não ganhou nenhuma feature nativa de agendamento nesta janela — quem
  se moveu foi a própria Meta, com o Business Agent (achado 2) oferecendo scheduling nativo via
  Google Calendar dentro do WhatsApp, e com a nova cobrança por resposta (achado 1) que torna
  bots de terceiros proporcionalmente mais caros que a alternativa nativa dela.
- Evolution API seguiu em manutenção incremental (v2.3.4, rebranding "Evolution Foundation
  2026"), sem feature nova de agendamento. Chatwoot: nada encontrado de agendamento nativo.

## Posicionamento — recomendações

1. **R$ 19,90/mês + piloto grátis 7 dias do Prontuário IA continuam defensáveis.** Nenhum
   concorrente direto (Amplimed, scribes internacionais) chega perto desse preço — o
   comparável mais próximo (Amplimed Ampli IA) custa ~6x mais quando empacotado. Manter.

2. **Mensalidade B2B da Secretária IA — sugestão de âncora: R$ 197–297/mês por clínica** (ou por
   número de WhatsApp). Base do cálculo: (a) sistemas de agenda tradicionais cobram R$ 89–229
   por *profissional* só pela agenda, sem IA de atendimento; (b) add-ons de IA por voz
   comparáveis (Amplimed Ampli IA ~R$ 120, scribes internacionais US$ 119–150) mostram que
   mercado paga prêmio por automação de IA em cima do sistema base; (c) a partir de 01/10/2026
   a Meta cobra por resposta de bot — o preço da Secretária IA precisa de margem para absorver
   esse custo extra sem virar prejuízo por cliente. R$ 197–297/mês fica abaixo do custo de meio
   turno de recepcionista e ainda dá fôlego para a nova taxa da Meta.

3. **Prioridade imediata: modelar o custo pós-01/10/2026 antes de fechar qualquer mensalidade
   B2B.** A cobrança por resposta da Meta (achado 1) muda a estrutura de custo por agendamento
   (hoje ~R$ 0,30) e o Business Agent nativo (achado 2) é uma ameaça direta ao "agendar pelo
   WhatsApp com IA" — vale avaliar nas próximas semanas se compensa migrar/integrar a Secretária
   IA sobre a API do Meta Business Agent (isento da taxa por mensagem) em vez de manter tudo em
   cima da Evolution API não-oficial.

## Nota metodológica

Firecrawl ficou sem créditos (erro 402) em todas as chamadas desta rodada — toda a pesquisa foi
feita via WebSearch nativo. WebFetch direto nas páginas de preço (iClinic, Ninsáude, Feegow,
Amplimed, Doctoralia, Shosp, Simples Dental, Dr. Agenda) retornou 403 em todos os casos; os
preços acima vêm de resultados de busca e páginas de terceiros, não de leitura primária da
página oficial — confiança menor que o padrão, revalidar manualmente os valores de Feegow, Shosp,
Simples Dental e Ninsáude antes de usar em material comercial.

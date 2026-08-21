---
title: Vigia de Concorrência — 2026-08-21
date: 2026-08-21
area: Concorrencia
tags: [concorrencia, mercado]
source: routine
---

# Vigia de Concorrência — semana de 2026-08-21

> Comparado contra o relatório de **2026-08-14** (uma semana de intervalo). Reporta só o que é
> genuinamente novo ou que os relatórios anteriores não tinham capturado.

## Achados

1. **Voa Health revelou preço público pela primeira vez — e tem um plano grátis.** Concorrente
   brasileiro de scribe médico mapeado semana passada sem preço público agora mostra: plano
   **Pro a partir de R$249/mês** (cobrado mensalmente dentro de contrato anual, uso ilimitado,
   7 dias grátis) e um **plano gratuito permanente** (10 consultas/mês, 10 pacientes ativos, 10
   mensagens/mês ao assistente clínico "Charcot"). Fonte: página de preços indexada via busca
   (não foi possível abrir voa.health/pricing diretamente — WebFetch bloqueado), checada
   21/08/2026. **E daí pro Cássio:** R$249 fica acima do teto do Calima (R$79,90 Hipócrates),
   então não aperta a escada por cima. O risco é o **plano grátis** — um médico que só dita 10
   consultas/mês (plantonista, consultório iniciante) pode preferir "grátis com limite" a pagar
   R$19,90 sem limite. Vale reler a página oficial para confirmar os números antes de usar em
   material de venda.

2. **Meta vai cobrar mensagens de serviço a partir de 01/10/2026 — hoje são grátis.** Achado novo
   sobre a WhatsApp Business API oficial: além da cobrança por token do Business Agent (US$2,00/
   milhão, vigente desde 01/08), a partir de outubro **toda resposta dentro da janela de 24h**
   (hoje gratuita) passa a ser cobrada. Fontes: [Meta Business Agent
   overview](https://developers.facebook.com/documentation/meta-business-agent/overview),
   [Maxbot](https://www.maxbot.com.br/blog/meta-business-agent), [Alexandre
   Guimarães](https://www.aleguimas.com.br/blog/whatsapp-business-api-o-que-muda/), checadas
   21/08/2026. **E daí pro Cássio:** isso eleva o custo de operar via **API oficial (Cloud API)**
   da Meta em geral — mas a Secretária IA roda em **Evolution API (WhatsApp Web não-oficial)**,
   fora desse faturamento. Ponto a **confirmar, não supor**: se algum concorrente que usa a API
   oficial (ex.: integrações nativas tipo WorkAI+Feegow, achado 3) tiver seu custo elevado em
   outubro, isso pode ser um argumento comercial ("nosso custo não sobe com a Meta").

3. **Dois concorrentes novos no radar — Pixedoc e WorkAI (esta com integração nativa ao ERP
   Feegow).** Pixedoc (pixedoc.com.br) é "secretária de IA" para odonto/estética/psicologia:
   agenda, confirma, cobra, CRM operacional, dados hospedados no Brasil (Supabase SP), 7 dias
   grátis, preço não público. WorkAI (workai.com.br/feegow) anuncia integração direta com o
   **Feegow** — transforma o ERP em "secretária virtual 24/7" (agenda, confirma, remarca, lê
   pedido de exame, faz triagem), preço não público. Fontes: [Pixedoc](https://www.pixedoc.com.br/),
   [WorkAI + Feegow](https://workai.com.br/feegow/), checadas 21/08/2026. **E daí pro Cássio:** o
   vetor da WorkAI é o mais preocupante estruturalmente — não é concorrente autônomo, é
   **parceria de canal que embute IA de agendamento dentro de um ERP já instalado** (Feegow tem
   base de clientes própria). Se esse modelo pegar, ERPs concorrentes (Amplimed, iClinic, Ninsáude)
   podem replicar e reduzir o motivo pra clínica contratar um produto à parte.

4. **Correção de mapeamento: secretariavirtual.net.br NÃO é concorrente de IA.** Checagem desta
   semana mostra que é uma **franquia de secretariado humano remoto** (taxa de franquia a partir
   de R$1.500–2.500), não um agente de IA. Havia sido listado como possível concorrente na semana
   passada sem essa verificação. **E daí pro Cássio:** remover da lista de vigilância; não voltar
   a contar como sinal de mercado.

5. **Secretar.AI — mystery shop parcial, ainda sem confirmar o diferencial de Pix.** O site
   confirma "agentes que recebem pacientes, agendam, cobram e fazem follow-up" e planos
   segmentados por porte (autônomo/pequena clínica/equipe), mas **nenhum snippet cita
   explicitamente "Pix"** e o preço segue **não público**. Fonte: [secretar.ai](https://secretar.ai/),
   checada 21/08/2026. **E daí pro Cássio:** a ameaça ao diferencial central (cobrar Pix antes de
   confirmar) segue **hipotética, não verificada** — dois vigias seguidos sem conseguir fechar
   esse mystery-shop por busca. Se for prioritário, só resolve com WebFetch/navegador direto no
   chat do site ou simulação manual de contratação.

6. **Meta Business Agent segue excluindo Saúde — estável, sem mudança de texto ou preço.**
   Documentação oficial relida ao vivo confirma a mesma frase de exclusão de "Finance, Government,
   **Health**, Alcohol, Gambling..." e o mesmo preço (US$2,00/milhão de tokens desde 01/08).
   Fonte: [developers.facebook.com](https://developers.facebook.com/documentation/meta-business-agent/overview),
   checada 21/08/2026. **E daí pro Cássio:** ponto de verificação pendente desde a semana passada
   (confirmar categoria WhatsApp Business das clínicas-cliente) segue pendente — sem mudança que
   force ação agora.

7. **Indícios (não confirmados em fonte primária) de reestruturação de preço em Simples Dental e
   Clinicorp.** Simples Dental: piso citado em agregador como "a partir de R$128,94/mês" (era
   R$149,90 na referência anterior). Clinicorp: um agregador cita planos "Standard R$159,90 /
   Premium R$369,90" (divergente da faixa "Starter R$299 de R$499" mapeada antes) e promoção
   CIOSP 2026 (50% off nas 6 primeiras mensalidades). **Não confirmado diretamente nas páginas
   oficiais** (simplesdental.com/planos-e-precos, clinicorp.com/planos) nesta rodada — fontes
   foram agregadores terceiros. **E daí pro Cássio:** possível sinal de pressão de preço nos ERPs
   tradicionais, mas precisa de confirmação direta antes de virar fato no radar; retomar na
   próxima rodada com scrape ao vivo dessas duas páginas.

8. **Heidi Health (scribe internacional) SUBIU preço — de referência indireta para o Calima.**
   Reestruturação de início de 2026: plano Clinician foi de ~US$90 para **US$150/usuário/mês**
   (anual); Free permanece (10 "Pro Actions"/mês). Fonte: [pricingsaas.com/companies/heidihealth](https://pricingsaas.com/companies/heidihealth),
   checada 21/08/2026 (data exata da mudança de preço não confirmada, "início de 2026"). **E daí
   pro Cássio:** não é concorrente direto no Brasil, mas reforça que scribes internacionais
   operam numa faixa de preço muito acima da escada do Calima (R$19,90–79,90) — nenhuma pressão
   de cima para baixo.

9. **CFM 2.454/2026 — sem prorrogação; prazo vence em 5 dias (26/08/2026).** Nenhuma norma
   complementar encontrada. Achado novo: o próprio CFM reconhece publicamente que "grande parte
   das instituições ainda não está preparada" e prevê ações de letramento com hospitais/empresas —
   sinal de que a pressão por prorrogação pode crescer, mas nada formalizado. Fontes:
   [Conjur, 01/08/2026](https://conjur.com.br/2026-ago-01/inteligencia-artificial-na-medicina-a-resolucao-cfm-2-454-2026-e-os-novos-contornos-da-responsabilidade-civil/),
   [portal.cfm.org.br](https://portal.cfm.org.br/noticias/cfm-normatiza-uso-da-ia-na-medicina/),
   checadas 21/08/2026. **E daí pro Cássio:** o prazo cai **dentro da janela até o próximo
   vigia** — se sair prorrogação ou norma complementar, é nos próximos 7 dias. Vale considerar
   destacar essa data no material de venda do Calima (urgência real de adequação).

10. **ANPD Sandbox — consulta pública ocorreu em 13/08, resultado ainda não publicado; nenhuma
    das 3 empresas participantes concorre com o Calima.** Confirmado: consulta remota via Teams
    em 13/08/2026, empresas em teste até dezembro/2026 são **Metatext, Synapse AI e Prevvine
    Tecnologia** (não a "possível prorrogação até 01/12" citada especulativamente semana
    passada — isso era o cronograma original do sandbox, não uma prorrogação nova). Relatório
    consolidado da consulta ainda não publicado. Fontes:
    [ConvergenciaDigital](https://convergenciadigital.com.br/governo/anpd-faz-consulta-a-sociedade-sobre-sandbox-regulatorio-de-ia-e-protecao-de-dados/),
    [gov.br/anpd](https://www.gov.br/anpd/pt-br/assuntos/noticias/apos-recursos-anpd-divulga-resultado-definitivo-do-projeto-sandbox-regulatorio),
    checadas 21/08/2026. **E daí pro Cássio:** item resolvido — pode sair do radar de urgência;
    manter só vigilância passiva.

## Pressão de preço

- **Calima:** nenhum concorrente aperta a escada de R$19,90/R$39,90/R$79,90 por baixo com preço
  confirmado. O único sinal de atenção é o **plano grátis do Voa Health** (achado 1) — grátis com
  limite de 10 consultas/mês, não uso ilimitado, então não é substituto direto do plano de
  entrada, mas compete pela atenção do médico que testaria "grátis" antes de pagar R$19,90.
- **Secretária IA:** nenhum piso novo abaixo de R$247/mês confirmado (referência = a divergência
  de preço real vs. tabela achada no Reclame Aqui da Doctoralia, R$247 vs. R$429 de tabela — não
  é um concorrente batendo esse preço, é sinal de que o "preço de tabela" nem sempre é o preço
  real cobrado). Secretar.AI (achado 5) segue sem preço público — dois vigias seguidos sem
  conseguir fechar esse ponto.
- Ninguém dando o serviço de graça no segmento Secretária IA. No segmento scribe, Voa Health tem
  free tier limitado (achado 1) — é o primeiro "grátis" real mapeado nesse nicho brasileiro.

## Comoditização

- **WorkAI + Feegow (achado 3) é o caso mais importante da semana**: é o primeiro sinal concreto
  de um **ERP embutindo IA de agendamento via parceria de canal**, em vez de a clínica precisar
  contratar um produto à parte. Se outros ERPs (Amplimed, iClinic, Ninsáude) replicarem, isso
  reduz a razão de a clínica contratar a Secretária IA como produto autônomo — vale monitorar se
  aparecem parcerias similares.
- **Meta segue não regalando nada de graça** — pelo contrário, está cobrando mais (Business
  Agent por token desde agosto, mensagens de serviço a partir de outubro, achado 2). Tendência da
  semana é de monetização, não comoditização, na API oficial. Mas a Secretária IA está fora desse
  faturamento por rodar em Evolution API — ponto a usar como diferencial de custo se algum
  concorrente que usa API oficial ficar mais caro em outubro.
- **Voa Health free tier** é o sinal de comoditização mais concreto da semana, mas no segmento
  scribe/prontuário, não no segmento secretária/agendamento.

## Posicionamento — recomendações

1. **Calima: manter a escada atual (R$19,90/R$39,90/R$79,90 + teste grátis 7 dias) — mas
   monitorar o free tier do Voa Health como o primeiro concorrente brasileiro direto com plano
   grátis permanente.** Nenhum concorrente aperta por preço pago; o risco é posicionamento
   ("por que pagar se dá pra testar grátis com limite"). Se o Voa Health começar a crescer nesse
   segmento, considerar destacar que o Calima tem **uso ilimitado desde o primeiro plano pago**
   (R$19,90), diferente do cap de 10 consultas do concorrente.

2. **Sugestão de mensalidade B2B para a Secretária IA: manter a faixa R$147–197/mês (revisão de
   07/08), sem mudança esta semana** — nenhum piso novo confirmado, e os dois concorrentes novos
   (Pixedoc, WorkAI) ainda não têm preço público para recalibrar. Mas incluir no script comercial
   um argumento novo: **a integração WorkAI+Feegow (achado 3) é o tipo de objeção que pode
   aparecer** ("meu ERP já vai ter isso") — vale preparar resposta padrão diferenciando produto
   autônomo (menos lock-in, funciona com qualquer ERP) de add-on de ERP específico.

3. **Fechar o mystery-shop do Secretar.AI de vez** — é a segunda semana seguida em que a busca
   não confirma preço nem a mecânica de Pix. Prioridade #1 da próxima rodada: usar Claude for
   Chrome ou contato direto no site/WhatsApp do Secretar.AI para simular contratação e confirmar
   se a cobrança Pix é de fato replicada. Prioridade #2: reler ao vivo simplesdental.com/planos-e-
   precos e clinicorp.com/planos para confirmar ou descartar a reestruturação de preço sugerida
   por agregadores (achado 7).

## Nota metodológica

Pesquisa feita com 2 agentes em paralelo (concorrentes diretos da Secretária IA + Meta Business
Agent + ERPs; scribes internacionais + Voa Health + Telepatia AI + regulação CFM/ANPD). WebSearch
foi a ferramenta principal em ambos — WebFetch seguiu bloqueado (403) nos portais grandes
(secretar.ai, voa.health, gov.br/anpd), então os preços de Voa Health e as possíveis mudanças em
Simples Dental/Clinicorp vêm de snippets de busca ou agregadores terceiros, não de scrape direto
da página oficial — sinalizado explicitamente em cada achado onde isso se aplica. Nenhum número
foi inventado; onde não havia preço público, ficou registrado "não público".

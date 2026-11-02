---
title: Vigia de Concorrência — 2026-11-02
date: 2026-11-02
area: Concorrencia
tags: [concorrencia, mercado]
source: routine
---

## TL;DR

- A SmartDoctor publicou o preço: R$ 99,90/mês com escriba IA, WhatsApp oficial e telemedicina. É o tudo-em-um com escriba mais perto do Calima, pelo dobro do preço.
- A Anvisa adiou o SNCR para 03/03/2027. A partir de 04/03/2027, toda receita de controle especial terá numeração digital. Hoje o Calima recusa controlado.
- O Simples Dental pôs um "Assistente IA por voz" à parte na tabela, e a odontologia entrou em Black November.
- Na teleconsulta avulsa, o Einstein cobra R$ 389,90 (agora confirmado na página ao vivo) e o Dr. Consulta R$ 125. A THM segue empatada com o Calima, a R$ 49,90.
- Nenhum preço caiu abaixo de R$ 49,90. As 3 recomendações continuam, com um ajuste no add-on.

> Comparado com o relatório de **2026-11-01**. **Varredura completa:** sim, por ser segunda-feira. A anterior foi em 26/10. Os ~40 alvos foram relidos em 02/11/2026 pelo Firecrawl, com `maxAge: 0`.
> Preço do Calima conferido no repo (`origin/main` `0708dd9`): o `site/index.html` mostra R$ 49,90 (7 ocorrências); `VENDAVEIS = ['staff']`; `PLANO_STAFF_CENTS` e `CONSULTA_AVULSA_CENTS` têm default 4990. Nada mudou.

## Achados

1. **SmartDoctor: preço público, com o escriba incluso.** O plano DOCTOR custa R$ 99,90/mês para 1 profissional e inclui:
   - Escriba IA: grava pelo navegador ou por upload, capta os dois lados na teleconsulta, monta um resumo em formato de anamnese com revisão obrigatória e apaga o áudio em até 30 dias.
   - WhatsApp Oficial: as mensagens são cobradas pela Meta direto no cartão do cliente.
   - "Assistant Doctor IA".
   - Telemedicina.

   O plano CLINIC custa R$ 350/mês para 5 profissionais (+R$ 50 por profissional extra), e o anual tem 20% de desconto.
   - Fonte: [smartdoctor.com.br/home/planos](https://www.smartdoctor.com.br/home/planos), lido em 02/11/2026. Até 26/10, o preço não era público.
   - **E daí pro Calima:** é o concorrente mais parecido no pacote (escriba, teleconsulta e WhatsApp num preço só), e cobra o dobro. É a melhor âncora para dizer "tudo-em-um com escriba pela metade do preço".

2. **Anvisa adia a transição do SNCR para 03/03/2027.** A partir de 04/03/2027, a Receita de Controle Especial e a Receita Sujeita à Retenção só valem com a numeração do SNCR. Até lá, papel e receita eletrônica continuam valendo juntos. O prazo anterior era 30/10.
   - Fonte: [futurodasaude.com.br](https://futurodasaude.com.br/anvisa-prorroga-prazo-transicao-sistema-nacional-de-controle-de-receituarios/), de 01/11/2026.
   - **E daí pro Calima:** hoje o Calima barra todo item da Portaria 344 e manda o médico para o talonário (`public/js/receita-ui.js:211`). Com o SNCR, a receita de controlado passa a poder ser digital. Isso vale para psicotrópico no plantão, e a Memed e os ERPs vão oferecer. Existem 4 meses para decidir se o Calima integra a numeração ou continua recusando.

3. **O Simples Dental pôs um "Assistente IA por voz", vendido à parte, na tabela de planos.** A Secretária IA continua em pré-lançamento, a "menos de R$ 6/dia". A Black November dá a clientes novos 25% no anual Basic/Plus (R$ 112,42 / R$ 187,42) e 20% no mensal por 10 meses. A Clinicorp também anuncia Black November, e o Combo IA dela (com "Voice Control") continua sob consulta.
   - Fontes: [simplesdental.com/planos-e-precos](https://www.simplesdental.com/planos-e-precos) e [clinicorp.com/planos](https://www.clinicorp.com/planos), lidos em 02/11/2026.
   - **E daí pro Calima:** os dois líderes da odontologia já têm voz e secretária IA. Isso confirma que a odontologia não deve ser a próxima frente.

4. **Teleconsulta avulsa: três preços que antes não estavam confirmados.**
   - **Einstein Conecta:** avulsa a R$ 389,90, com 24 h para usar, agora confirmada na página ao vivo. Os planos anuais custam R$ 129,90/mês (individual) e R$ 99,90 por membro (familiar). Fonte: [telemedicina.einstein.br](https://telemedicina.einstein.br/).
   - **Dr. Consulta:** clínica geral online agendada a R$ 125 (3x R$ 41,67). Fonte: [drconsulta.com/servicos/consultas](https://drconsulta.com/servicos/consultas).
   - **Conexa:** os planos particulares viraram públicos, a 12x R$ 26,90 / R$ 32,90 / R$ 89,90. A avulsa não tem preço na página. Fonte: [conexasaude.com.br/produtos/planos-particulares](https://www.conexasaude.com.br/produtos/planos-particulares).
   - Todos lidos em 02/11/2026.
   - **E daí pro Calima:** a faixa da avulsa vai de R$ 49,90 (THM e Calima) a R$ 389,90. Os R$ 49,90 do Calima ficam no piso, e o argumento continua sendo "com o seu médico".

5. **clina.ai: o plano Clínica subiu de R$ 397 para "a partir de R$ 497".** O Completo Médico segue a R$ 249. Entraram seis módulos novos, de R$ 39 a R$ 99 (Convênios & TISS, Fechamento & Contador, Rotinas, Ultrassom etc.), além do Certificado ICP a R$ 229. A Sofia Triagem e a Sofia Acompanhamento (agora "Clina Care") seguem a R$ 49 cada.
   - Fonte: [clina.ai/planos](https://clina.ai/planos), lido em 02/11/2026.
   - **E daí pro Calima:** o clina.ai sobe preço e soma módulos, enquanto o Calima fica parado em R$ 49,90. A diferença a favor do Calima aumenta.

6. **Heidi Health: o plano Free agora diz "Unlimited ambient AI documentation", e saiu o "Heidi II".** O Clinician segue a US$ 110 no anual. A página não diz que há pt-BR.
   - Fonte: [heidihealth.com/en-us/pricing](https://www.heidihealth.com/en-us/pricing), lido em 02/11/2026.
   - **E daí pro Calima:** é o primeiro escriba grátis e sem limite declarado. Por enquanto vale só para quem dita em inglês. Se a Heidi lançar pt-BR, é a maior ameaça ao preço do Calima.

7. **O WhatsApp baniu contas de usuários do Instinct, um agente pessoal de IA dos EUA**, citando os termos contra automação e wrappers não autorizados.
   - Fonte: [indianexpress.com](https://indianexpress.com/article/technology/artificial-intelligence/instinct-whatsapp-disruption-ai-agents-what-happened-10947160/), de 02/11/2026.
   - **E daí pro Calima:** mostra a Meta aplicando de fato a regra de 15/01. A secretária do Calima está do lado certo, na Cloud API oficial, e isso vale como argumento de venda contra secretárias de WhatsApp não oficiais.

8. **Dr. Assistente: preços confirmados na página oficial.** Básico R$ 150, Avançado R$ 250 e Pro R$ 450 por mês (anual R$ 1.500 / 2.500 / 4.500). Fonte: [drassistente.com.br](https://drassistente.com.br/), lido em 02/11/2026.
   - **E daí pro Calima:** confirma o que o comparativo de ontem indicava. Nenhuma decisão muda.

**Outros (sem efeito no Calima):**
- A Amplimed marcou a live "AmpliBlack", com ofertas, para 04/11 às 19h. A "Amélia Transcrição" segue sem preço público. Vale reabrir a página na quinta.
- O Vokkari passou a assinar com VIDaaS.
- O iClinic tem um add-on de assinatura eletrônica do paciente a R$ 14,90.
- A NoHarm (IA que confere prescrição no SUS) é finalista de um prêmio. É do setor público e não concorre.

## Regulação

- **CFM 2.454/2026:** a 1ª instância negou a suspensão e extinguiu a ação sem resolver o mérito. Houve apelação, e o pedido segue no TRF1, sem decisão. A resolução continua em vigor. A fonte é só um post de Instagram de ~28/10, sem confirmação num site jurídico.
- **Anvisa:** adiou o SNCR (achado 2). Nada novo sobre a RDC 657 (software como dispositivo médico).
- **WhatsApp Cloud API:** a página da Meta foi atualizada em 30/09/2026 e não anuncia mudança depois de 01/10. Utility e authentication custam US$ 0,0068 por mensagem no Brasil. A tarifa de marketing não foi lida na fonte oficial (o CSV da Meta deu 403). A próxima janela possível de reajuste é 01/01/2027. Contas que já faturam no Brasil têm até 30/06/2027 para migrar para BRL.
- **CFP, CFN, CFO, COFFITO, COFEN, ANPD, Apple:** nada novo.

## Pressão de preço

- **Escriba abaixo de R$ 49,90:** os grátis com limite continuam os mesmos (Voa Free com 10 atendimentos, Dora com 10 consultas, Vokkari com 5 h, Telepatia a US$ 0). A Heidi Free passou a se dizer "unlimited", mas só em inglês. Em pt-BR, nenhum pago fica abaixo de R$ 49,90. O mais barato é a Dora, a R$ 79.
- **Tudo-em-um:** o SmartDoctor, a R$ 99,90 com escriba, WhatsApp e tele, é o mais próximo e custa o dobro. O clina.ai ficou mais caro. Os R$ 49,90 do Calima continuam baratos.
- **Teleconsulta avulsa:** ninguém cobra menos que R$ 49,90. A THM empata; Dr. Consulta (R$ 125) e Einstein (R$ 389,90) cobram mais.
- **Secretária no WhatsApp por profissional abaixo de R$ 99,90:** os mesmos de antes.
  - Embutida em outro produto: Sofia grátis (+R$ 49 por função), Dr. Agenda a R$ 70 e, agora, o SmartDoctor, que embute o WhatsApp oficial nos R$ 99,90.
  - Avulsa: o piso continua em R$ 147 (AgendaCare), seguido de Singulare R$ 197, Desler R$ 198 e Secretar.AI R$ 360.

## Comoditização

- **Escriba embutido:** entraram o SmartDoctor (escriba incluso no plano, sem custo extra) e o Simples Dental (voz como add-on pago). Já estavam Feegow (Noa Notes no VIP), Amplimed, PsicoManager, Clinicorp e Doctoralia.
- **Meta, WhatsApp e n8n:** nada de graça. A Meta aperta o cerco a agentes não oficiais (achado 7).
- **Big tech:** nenhum ditado clínico em pt-BR. Nabla, Abridge, Suki e Dragon Copilot seguem sem preço público e sem lançamento no Brasil.

## Posicionamento — recomendações

1. **O plano único de R$ 49,90 com 7 dias grátis sem cartão continua defensável.** O concorrente com o pacote mais parecido (SmartDoctor) cobra R$ 99,90, e todo escriba pago em pt-BR cobra pelo menos R$ 79. Dois riscos a acompanhar:
   - a Heidi Free "unlimited", se chegar ao pt-BR;
   - as promoções de Black November, que vão baixar o preço dos ERPs por alguns meses.

   Não há motivo para baixar o preço. Uma alternativa é uma oferta de Black November no anual, para travar quem chegar agora.
2. **Add-on Secretária por médico: manter os R$ 99,90 e vender como "na API oficial da Meta".** O mercado avulso começa em R$ 147 e vai até R$ 360, então os R$ 99,90 ficam abaixo de todo avulso. Somados à assinatura, dão R$ 149,80, que ainda fica abaixo de Desler + ERP ou do clina.ai Completo. Ajuste em relação a 26/10: o SmartDoctor embute WhatsApp em R$ 99,90. Por isso, a secretária do Calima precisa entregar agendar, remarcar e cobrar de ponta a ponta, não só disparar mensagem. Funções extras, como triagem e retorno, a R$ 39–49, como faz o clina.ai.
3. **Profissão menos servida por escriba em pt-BR: segue a nutrição.** Dietbox e WebDiet (o Black tem a "Clara IA") não têm ditado por voz da consulta. A situação das outras:
   - Psicologia: o PsicoManager já transcreve sessões.
   - Odontologia: tem voz no Simples Dental e na Clinicorp.
   - Fisioterapia (ZenFisio) e enfermagem (Vitalia): nenhuma voz visível nas páginas de preço, o que faz delas a segunda opção.

## Varredura completa — preços lidos em 02/11/2026

| Alvo | Preço lido | Mudou desde 26/10? |
|---|---|---|
| iClinic | R$ 99/129/169/299; WhatsApp a partir de R$ 29,90; 10 teleconsultas por R$ 35; assinatura eletrônica R$ 14,90 | Não (a assinatura é dado novo) |
| Ninsaúde Apolo | R$ 199 por profissional (dos termos de uso; /precos dá 404) | Não |
| Feegow | R$ 129/199/249 (site agora em feegowclinic.com.br) | Não |
| Amplimed | R$ 89 / R$ 139; Amélia Transcrição sem preço público | Não |
| Doctoralia Pro | R$ 429/529/679 + Noa Notes R$ 199 + site R$ 99 (pro.doctoralia.com.br/preco) | Não |
| Shosp | R$ 0 + ativação R$ 299 / R$ 149 / R$ 229 | Não |
| Dr. Agenda | R$ 70 promo (de R$ 90), com secretária IA; agenda de exames R$ 40 | Não |
| clina.ai | Grátis / Completo Médico R$ 249 / **Clínica a partir de R$ 497** / módulos de R$ 39 a R$ 99 | **Sim** |
| SmartDoctor | **DOCTOR R$ 99,90 / CLINIC R$ 350** (+R$ 50 por profissional) | **Sim (agora público)** |
| Simples Dental | R$ 149,90/249,90/349,90; Black November −25% no anual; Assistente IA por voz à parte | **Sim (promo + voz)** |
| Clinicorp | R$ 159,90 / R$ 369,90; Combo IA sob consulta | Não |
| Dietbox | R$ 49,90 por 3 meses, depois R$ 91,90 · R$ 133,90 | Não |
| WebDiet | R$ 49,90 por 3 meses, depois R$ 94,90 · R$ 139,90 | Não |
| PsicoManager | R$ 89 / R$ 119 | Não |
| ZenFisio | R$ 79/179/439 | Não |
| Vitalia Pro | R$ 63/119/223 no anual | Não |
| Voa Health | Free / Pro R$ 289–349 / Ultra R$ 2.490–2.900 | Não |
| Heidi Health | Free ("unlimited") / US$ 110 / sob consulta | Texto do Free |
| Freed | US$ 39–59 / 59–79 / 104–119 | Não |
| Telepatia AI | US$ 0 de lançamento (US$ 99 riscado) | Não |
| Dora Health | Grátis 10/mês · Premium R$ 79 | Não |
| Vokkari | Grátis 5 h · R$ 179,99 · R$ 449,99 | Não |
| Escriba Médico | R$ 97 / R$ 997 no ano | Não |
| Dr. Assistente | R$ 150 / 250 / 450 | Confirmado na página oficial |
| Assist4Doc | R$ 197/397/997 | Não |
| Nabla, Abridge, Suki, Dragon Copilot | Não público | — |
| Secretar.AI | R$ 360/720/1.080 | Não |
| Singulare (singulare.org) | R$ 197/397 + humano a partir de R$ 297 | Não |
| AgendaCare | R$ 0 / 79,90 / 147 / 297 / 497 / 797 / 1.297; conversa extra R$ 2,20 | Não |
| Desler AI | R$ 159 / 198 / 298 | Não |
| THM Saúde | Avulsa R$ 49,90 · plano R$ 79,90 | Não |
| Einstein Conecta | Avulsa R$ 389,90 · R$ 129,90 / R$ 99,90 | Confirmado ao vivo |
| Dr. Consulta | Clínica geral online R$ 125 | **Novo (antes não público)** |
| Conexa | Planos 12x R$ 26,90 / 32,90 / 89,90; avulsa não pública | **Novo (planos públicos)** |
| Doctoralia (teleconsulta) | Não público (cada profissional define o seu) | — |

**Lacunas:**
- O agente web (MCP `agente-web`) não estava disponível nesta sessão de nuvem, então a rotina usou a reserva: Firecrawl e WebSearch.
- A tarifa de marketing do WhatsApp no Brasil não foi lida na fonte oficial (CSV da Meta com 403).
- A avulsa da Conexa e a do Dr. Consulta sem agendamento não têm preço público.
- O Firecrawl avisou que os créditos da conta estão acabando.
- Nenhum número foi estimado.

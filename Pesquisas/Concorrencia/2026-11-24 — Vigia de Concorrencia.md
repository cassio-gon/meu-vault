---
title: Vigia de Concorrência — 2026-11-24
date: 2026-11-24
area: Concorrencia
tags: [concorrencia, mercado]
source: routine
aviso: enviado
---

## TL;DR

- **XuzIA vende secretária IA no WhatsApp para o autônomo por R$ 99/mês**, com 50% off nos 2 primeiros meses (R$ 49,50) até 31/12. É o novo piso do add-on: R$ 0,90 abaixo dos R$ 99,90 em estudo. Antes, o piso era a AgendaCare, a R$ 147.
- **Maia Health** (novo, 1.800 médicos): escriba por voz a partir de R$ 249 por médico, com cota de 50 h no plano Basic. **Hub Médica**: secretária no WhatsApp a partir de R$ 597.
- Calima sem mudança (R$ 49,90). Recomendação (b) ajustada: lançar o add-on a R$ 99,90 **com o prontuário junto** como argumento, não pelo preço.

> Comparado com o relatório de **2026-11-23**. **Varredura completa:** não (terça; a última foi ontem, 23/11). Reabertas só as páginas de quem apareceu no noticiário.
> Calima conferido no repo (`origin/main` `65e344b`): R$ 49,90 no site (7 ocorrências), `VENDAVEIS = ['staff']`, `PLANO_STAFF_CENTS` e `CONSULTA_AVULSA_CENTS` com default 4990.

## Achados

1. **XuzIA: secretária IA no WhatsApp a R$ 99/mês para o autônomo.**
   - Atende 24h, agenda, confirma, lembra e remarca. Não faz triagem clínica e, se o paciente relatar urgência, sinaliza a equipe. Fica pronta em até 48h.
   - **Preço:** Autônomo R$ 99 (1 número). Equipe Básico R$ 197 (2 profissionais), Equipe R$ 347 (até 5), PME R$ 597. Só mensal, sem fidelidade, Pix ou cartão.
   - **Promoção:** 50% off nos 2 primeiros meses com cupom pessoal, válido até 31/12. Não há plano grátis, só uma conversa de teste sem cadastro.
   - Não tem prontuário, ditado nem teleconsulta.

   Fonte: [xuzia.com.br/precos](https://xuzia.com.br/precos/), lida em 24/11/2026. Primeira vez neste vigia.
   ![XuzIA, preços no celular](https://agente.cassiogon.tech/prints/a7b4d1902ab48a6cc2270a3764953882.jpg)
   - **E daí pro Calima:** os R$ 99,90 do add-on empatam com a XuzIA, que entrega só a secretária. O add-on se defende pelo que vem junto: a secretária agenda direto na agenda do Calima, cobra a teleconsulta e o médico dita o prontuário no mesmo app. Pela secretária sozinha, o preço não se diferencia.

2. **Maia Health: prontuário com escriba a partir de R$ 249 por médico.**
   - Transcreve o atendimento em tempo real e estrutura a nota. Tem agenda, confirmação e lembrete pelo WhatsApp (automação, não assistente de IA), receituário e questionários de acompanhamento. Diz ter mais de 1.800 médicos. Não encontrei teleconsulta.
   - **Preço:** Basic R$ 249 (50 h de transcrição por mês), Essentials R$ 309 (ilimitado, com documentos assinados), Visionary R$ 527. Tudo por médico, mensal, sem fidelidade. "Comece grátis, sem cartão", sem dizer por quanto tempo.

   Fonte: [marketing.healthmaia.com/precos.html](https://marketing.healthmaia.com/precos.html), lida em 24/11/2026. Primeira vez neste vigia.
   ![Maia, preços no celular](https://agente.cassiogon.tech/prints/b57721d3962d18153e3d9e8478457b70.jpg)
   - **E daí pro Calima:** é mais um escriba de consultório na faixa de R$ 250 a R$ 530. O Calima custa cerca de 1/5 do plano de entrada da Maia, sem cota de horas.

3. **Hub Médica: secretária no WhatsApp para clínica a partir de R$ 597.**
   - A HubIA agenda, confirma, cobra e reativa pacientes. Integra com iClinic, Feegow, MedX, Clinicorp e outros prontuários. Tem teleconsulta (Virtual Care) e um "resumo de consulta por IA" em beta a partir do segundo plano.
   - **Preço:** Flex R$ 597 (de R$ 970; 1 profissional, 2 mil atendimentos). Essencial R$ 990 (de R$ 1.290). Prontuário +R$ 79. A Meta cobra à parte (R$ 0,035 por lembrete, R$ 0,3217 por campanha), e a IA é cobrada pelo consumo. 7 dias grátis. Na Black, a fidelidade cai para 3 meses.

   Fonte: [web.hubmedica.com.br/planos.html](https://web.hubmedica.com.br/planos.html), lida em 24/11/2026. Primeira vez neste vigia.
   - **E daí pro Calima:** confirma que secretária "de clínica" custa cerca de 6x o add-on, mais o uso da Meta. Não pressiona os R$ 99,90.

4. **Medics publicou comparativo com preço: R$ 249/mês para 1 profissional, mais R$ 100 por profissional adicional,** com transcrição por IA em rascunho que o médico revisa. O mesmo texto cita o HiDoctor Online a R$ 98 e o iClinic de R$ 99 a R$ 299 (iguais à varredura de ontem). Fonte: [medics.com.br, blog de 24/11](https://www.medics.com.br/blog/melhores-prontuarios-eletronicos-para-clinicas), lida em 24/11/2026.
   - **E daí pro Calima:** um escriba de R$ 249 entra na mesma faixa da Maia. Nada abaixo dos R$ 49,90.

5. **MedScribe (medscribe.com.br): escriba que gera anamnese, resumo e evolução, com conta grátis sem cartão.** Preço não público, e a página não diz os limites do gratuito. Fonte: [medscribe.com.br](https://medscribe.com.br/), lida em 24/11/2026. Primeira vez neste vigia.
   - **E daí pro Calima:** é mais um escriba avulso com porta de entrada grátis. Vale reabrir na próxima varredura para ver se publicou os planos.

## Regulação

- **Nada novo.**
- **CFM 2.454/2026 e telemedicina:** só colunas jurídicas (Migalhas) e guias repetindo a CFM 2.314/2022.
- **Meta/WhatsApp:** guias de 20 a 24/11 repetem a tabela em reais de novembro (marketing R$ 0,3217 por mensagem entregue) e a cobrança da mensagem de serviço desde 01/10. A Wati lembra que a Meta AI do WhatsApp é para o consumidor, não para empresas.
- **Anvisa, ANPD, CFP, CFN, CFO, COFFITO, COFEN e Apple:** nada nas últimas 24 h.

## Pressão de preço

- **Escriba abaixo de R$ 49,90:** sem nome novo. Os de ontem continuam (NurseUp R$ 39,95 por 3 meses, Recinto grátis no beta, Ordexa R$ 39,90 com cota, Desler grátis dentro de R$ 159). MedScribe tem conta grátis, com limite não público.
- **Tudo-em-um:** a Maia (R$ 249 a R$ 527) e a Medics (R$ 249) reforçam a faixa de R$ 159 a R$ 590. Os R$ 49,90 seguem baratos.
- **Teleconsulta avulsa:** sem mudança.
- **Secretária por profissional: há uma agora no limite.** XuzIA Autônomo, R$ 99/mês, e R$ 49,50 nos 2 primeiros meses com cupom até 31/12.

## Comoditização

- **Secretária no WhatsApp virou produto de prateleira:** XuzIA, Hub Médica, Santé (Fer), MEDX Care, Super Márcia e Versatilis (vídeo de 23/11) anunciam a mesma coisa (agenda, confirma, remarca 24h). O que diferencia é estar ligada ao prontuário e à cobrança.
- **Meta, n8n e big techs:** nada novo em pt-BR.

## Posicionamento

- **(a) e (c):** sem mudança de recomendação.
- **(b) Add-on Secretária por médico: manter R$ 99,90, mas vender pelo pacote.**
  - Com a XuzIA a R$ 99, os R$ 99,90 deixam de ser "o mais barato do mercado".
  - Na página do add-on, o argumento passa a ser **"a secretária que agenda no seu prontuário e cobra a teleconsulta antes de confirmar"**, coisa que a XuzIA não faz.
  - Se for usar promoção de lançamento, a XuzIA já pratica 50% off por 2 meses. Um teste de 7 dias grátis, como o do plano, é a contra-oferta mais simples.
  - Teto de R$ 129,90 mantido.

---
Checado hoje: 8 buscas (prontuário com IA, secretária no WhatsApp, rodadas, regulação, outras profissões, WhatsApp/Meta, teleconsulta, MedScribe), 2 extrações (9 páginas) e 2 prints. Calima conferido no repo.

Já registrados e não repetidos: Avie, Super Márcia, MEDX Care, Santé, DoctorAssistant.ai, Corpora, Tivita, Pronova, Darwin, Medora, Recinto, Musas (Black já relatada em 22/11), Vem Consulta, Cloudia, Secretária IA (usesecretariaia).

Reserva: nenhuma página precisou de reserva. Nenhum número foi estimado. "Cerca de 1/5" e "cerca de 6x" são contas sobre os preços publicados.

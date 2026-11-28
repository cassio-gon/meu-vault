---
title: Vigia de Concorrência — 2026-11-28
date: 2026-11-28
area: Concorrencia
tags: [concorrencia, mercado]
source: routine
aviso: brief
---

## TL;DR

- **A Oi Clinic faz evolução por voz (SOAP/DAP/BIRP) com IA inclusa e teleconsulta por R$ 19,90 a R$ 39,90/mês**, conforme a profissão, e tem plano grátis com 5 pacientes. É o preço mais baixo já visto para voz + teleconsulta.
- **A Hill Odonto lançou o "Atendente IA no WhatsApp" e a evolução por voz** num ERP de odontologia. A secretária vem a partir de R$ 199,90/mês.
- **A Aionis (psicologia) anuncia R$ 49,90/mês com 7 dias grátis sem cartão**: o mesmo preço e o mesmo teste do Calima, mas a IA parte das anotações, não da voz.
- Calima sem mudança (R$ 49,90). Muda a recomendação (c): fisioterapia e TO já têm voz a R$ 19,90.

> Comparado com o relatório de **2026-11-27**. **Varredura completa:** não (sábado; a última foi em 23/11). Reabertas só as páginas de quem apareceu na busca.
> Calima conferido no repo (`origin/main` `1279fc7`): R$ 49,90 no site (7 ocorrências), `VENDAVEIS = ['staff']`, `PLANO_STAFF_CENTS` e `CONSULTA_AVULSA_CENTS` com default 4990.

## Achados

1. **Oi Clinic: evolução por voz com IA e teleconsulta por R$ 19,90 a R$ 39,90/mês.**
   - É uma plataforma para psicologia, fonoaudiologia, terapia ocupacional e fisioterapia. Tem "Evoluções SOAP / DAP / BIRP por voz", e a evolução fica "pronta para revisar": o profissional revisa e assina, e nada vai sozinho ao prontuário. A IA tira CPF, telefone e e-mail antes da análise. Tem teleconsulta por vídeo sem instalar nada, lembretes no WhatsApp sem IA, TISS e app do paciente.
   - **Preço por mês, com a IA inclusa:**
     - Gratuito: até 5 pacientes.
     - Profissional: R$ 39,90 (psicologia), R$ 29,90 (fono) e R$ 19,90 (TO e fisioterapia).
     - Duo: R$ 49,90 (2 profissionais).
     - Clínica: R$ 99,90 (até 5 profissionais).
   - O teste dura 15 dias, sem cartão, e depois a conta cai no Gratuito.

   Fonte: [oiclinic.com.br](https://oiclinic.com.br/), lida em 28/11/2026. Primeira vez neste vigia.
   ![Oi Clinic, capa no celular](https://agente.cassiogon.tech/prints/2a5eac07926370de0995813b1788c13c.jpg)
   - **E daí pro Calima:** voz + teleconsulta + anonimização abaixo de R$ 49,90 em quatro profissões. Para fisioterapia e TO, o Calima custa 2,5 vezes mais. O que só o Calima tem: o texto montado por código, o plantão e o uso por médico.

2. **Hill Odonto: "Atendente IA no WhatsApp" e evolução por voz, as duas marcadas como novas.**
   - É um ERP de odontologia. A atendente responde no WhatsApp 24 h, agenda, informa o valor exato e passa para humano, com log auditável. A evolução do tratamento é ditada por voz. Há também leitura de radiografia e rascunho de receita por IA (Premium IA).
   - **Preço por mês:** Básico R$ 89,90 (1 profissional), Essencial R$ 129,90 (voz), Profissional R$ 199,90 (a atendente de IA) e Premium IA R$ 249,90. O teste dura 14 dias, sem cartão.

   Fonte: [hillodonto.com.br](https://hillodonto.com.br/), lida em 28/11/2026. Primeira vez neste vigia.
   ![Hill Odonto, capa no celular](https://agente.cassiogon.tech/prints/e3b01728085cd295e2747f801e209918.jpg)
   - **E daí pro Calima:** a odontologia ganha a quarta secretária de IA de série (Simples Dental, Clinicorp, Guia Odonto e agora Hill). Aqui a secretária custa R$ 110 a mais que o plano de entrada, o que reforça os R$ 99,90 do add-on como preço de mercado.

3. **Aionis: sistema para psicologia com IA por R$ 49,90/mês e 7 dias grátis sem cartão.**
   - A página foi atualizada em 28/11. Ela traz prontuário, agenda, financeiro, escalas psicológicas e um assistente que gera evolução, resumo e plano terapêutico **a partir das anotações**, sem voz. Diz ter "mais de 2.400 psicólogos" e dá 6 meses grátis a quem indicar 10 colegas.
   - O preço de R$ 49,90/mês e os 7 dias sem cartão estão na descrição da página; a tabela de planos não carregou.

   Fonte: [aionis.com.br, 28/11/2026](https://aionis.com.br/sistema-para-psicologos). Primeira vez neste vigia.
   ![Aionis, página para psicólogos](https://agente.cassiogon.tech/prints/af6b5e8ae9e0b29719642271c98404cf.jpg)
   - **E daí pro Calima:** a mesma âncora (R$ 49,90 + 7 dias sem cartão) já é usada por um sistema de psicologia sem voz. O que separa o Calima é o ditado. A indicação com prêmio (6 meses por 10 colegas) é uma tática a observar.

4. **ApexPlus (odontologia): ditado da evolução com IA no plano Advanced, a R$ 89,99/mês no anual.**
   - "Dite a evolução clínica e a IA escreve no prontuário", só no Advanced. Os planos anuais: Basic R$ 43,20/mês, Pro R$ 71,91/mês e Advanced R$ 89,99/mês. A chamada é "a partir de R$ 48/mês". WhatsApp pela API oficial só para confirmação, sem IA. O teste dura 7 dias, sem cartão.

   Fonte: [apexplus.com.br](https://apexplus.com.br/), lida em 28/11/2026. Primeira vez neste vigia.
   - **E daí pro Calima:** na odontologia o ditado já é item de plano de topo. O dentista paga R$ 90 ou mais por mês por ele.

5. **Salutes (nutrição): plano alimentar ditado por voz.**
   - O nutricionista descreve as refeições por áudio e a Salutes organiza alimentos e medidas. O WhatsApp serve a lembretes, sem IA. Preço não público na parte lida. O teste dura 7 dias.

   Fonte: [salutes.com.br](https://salutes.com.br/), lida em 28/11/2026. Primeira vez neste vigia.
   - **E daí pro Calima:** a nutrição já tem voz, mas para o plano alimentar, não para a evolução da consulta. Essa brecha ainda está aberta.

6. **Lia (Lima IA tech): secretária no WhatsApp para dentista que não marca horário sozinha.**
   - Ela responde 24 h no número do consultório, entende áudio, anota o pedido ou manda o link de agendamento e avisa o dentista em caso de urgência. Não marca, confirma nem cancela, e não dá orientação clínica. Preço não público.

   Fonte: [limaiatech.ia.br, 25/11/2026](https://limaiatech.ia.br/secretaria-virtual-dentista-whatsapp/). Primeira vez neste vigia.
   - **E daí pro Calima:** a secretária do Calima marca e cobra antes de confirmar. Isso continua a diferenciá-la das secretárias simples, que só respondem.

7. **DocHelp: teleconsulta avulsa a R$ 49,90 e plano familiar de R$ 100/mês para até 4 pessoas.**
   - Clínico geral 24 h e 12 ou mais especialidades por agendamento, com psicologia no plano. Sem carência e sem coparticipação.

   Fonte: [dochelp.com.br](https://www.dochelp.com.br/), lida em 28/11/2026. Primeira vez neste vigia.
   - **E daí pro Calima:** empata com a teleconsulta avulsa do Calima. O plano de R$ 25 por pessoa é a referência caso o plano mensal do paciente volte.

## Regulação

- **Nada novo.**
- **CFM 2.454/2026:** só textos que repetem a regra (Saúde Digital News e Economia SP, 25 e 26/11, sobre registrar no prontuário o uso de IA; JOTA, Portal Telemedicina, AI Brasil).
- **Cofen:** a Resolução 818, de 25/11/2026, aprova um guia de normas da enfermagem na APS. Não trata de IA nem de prontuário eletrônico.
- **Meta/WhatsApp:** os guias repetem a cobrança por mensagem, a mensagem de serviço paga desde 01/10 e a restrição a assistentes genéricos desde 15/01.
- **Anvisa, ANPD, CFP, CFN, CFO, COFFITO e Apple:** nada nas últimas 24 h.

## Pressão de preço

- **Escriba abaixo de R$ 49,90:** **sim, de novo.** A Oi Clinic dá voz + teleconsulta por R$ 19,90 (fisioterapia e TO), R$ 29,90 (fono) e R$ 39,90 (psicologia), com plano grátis de 5 pacientes. Continuam valendo Brainn Care, Sinthoma, PsicoProntuários, Lina e os grátis com limite.
- **Tudo-em-um:** a Aionis cobra os mesmos R$ 49,90, sem voz. Na odontologia, a voz só vem em planos de R$ 90 a R$ 130 (ApexPlus, Hill). O Calima segue barato para o médico.
- **Teleconsulta avulsa:** a DocHelp cobra R$ 49,90, o mesmo preço. Nada abaixo, além dos casos já registrados (LoopMed com cupom).
- **Secretária por profissional:** nada abaixo de R$ 99,90 além da Luna da Villo (R$ 89,90, já registrada). A Hill põe a secretária a R$ 199,90 no plano.

## Comoditização

- **Escriba nativo em ERP:** entram na lista a Oi Clinic (incluso desde R$ 19,90), a Hill Odonto e a ApexPlus (odontologia) e a Salutes (plano alimentar). A voz virou item de série nos sistemas das outras profissões.
- **Secretária no WhatsApp:** a Hill Odonto põe a dela de série no plano Profissional. Meta, n8n e big techs: nada novo.

## Posicionamento

- **(c) muda:** fisioterapia e TO já têm voz a R$ 19,90 (Oi Clinic) e R$ 79,90 (Vedius). A odontologia tem voz em pelo menos quatro sistemas, e a psicologia segue saturada. Restam a **enfermagem** (nenhum escriba dedicado achado) e a **nutrição** na evolução da consulta (a Salutes só dita o plano alimentar). Recomendação: se o Calima for abrir outra profissão, testar enfermagem primeiro.
- **(a) sem mudança, com ressalva:** os R$ 49,90 ilimitados e com teleconsulta seguem defensáveis para o médico. Fora da medicina, a Oi Clinic deixa o preço alto. Não vale baixar o preço geral, mas a página para as outras profissões não deve competir só no preço.
- **(b) sem mudança:** a Hill (R$ 110 acima do plano de entrada) e a Villo (R$ 89,90) cercam os R$ 99,90 do add-on.

---
Checado hoje: 11 buscas (prontuário com IA, secretária no WhatsApp, rodadas, CFM, escribas globais, Black Friday, Meta/WhatsApp, teleconsulta avulsa, Anvisa/ANPD/conselhos, outras profissões) e 10 páginas lidas (Oi Clinic, Hill Odonto, Aionis, ApexPlus, Salutes, Lima IA tech, DocHelp, Clinvo, Aiude e a página de Aionis por scrape), com 3 prints. Calima conferido no repo.

Já registrados e não repetidos: Klinity, Aura, AxônioMed, Secretária IA (usesecretariaia), Clinia, MEDX Care, Ordexa, THM, Teledoc, LoopMed, Olá Doutor, Telepatia, Conclínica, Certu, Guia Odonto, HiDoctor LIVE, Medcloud Laraa Max e São Camilo.

Vistos sem novidade ou fora do foco: Clinvo (fisioterapia, R$ 39 a R$ 149, sem IA), Aiude (página sem conteúdo legível), Ouro Verde (teleconsulta a R$ 89,90), healthtech de glosas (rodada, fora do foco), Healthtech Rounds #07 (rodadas globais, nenhuma de escriba no Brasil).

Reserva: nenhuma página precisou de reserva. Nenhum número foi estimado.

---
title: Vigia de Concorrência — 2026-11-18
date: 2026-11-18
area: Concorrencia
tags: [concorrencia, mercado]
source: routine
aviso: enviado
---

## TL;DR

- A teleconsulta avulsa ganhou piso novo: **Linkadoc** e **Consultar Médico** cobram **R$ 39,90** por consulta em vídeo, R$ 10 abaixo do Calima. As duas são pronto-atendimento com médico de plantão, não com o médico do paciente.
- **LoopMed** cobra R$ 39,90 na 1ª consulta por chat com cupom e R$ 59,90 depois. **Olá Doutor** cobra a partir de R$ 69.
- Microsoft (Ignite): o **Dragon Copilot Transcribe** passou a rodar no motor próprio MAI-Transcribe-2. Ainda sem produto clínico em pt-BR.
- Calima sem mudança (R$ 49,90). Recomendações mantidas.

> Comparado com o relatório de **2026-11-17**. Varredura completa: não (é quarta, e a última foi em 16/11). Só reabri as páginas que apareceram no noticiário.
> Calima conferido no repo (`origin/main` `6e0ef3a`, o mesmo de ontem): R$ 49,90 no site, `VENDAVEIS = ['staff']`, defaults 4990/4990.

## Achados

1. **Linkadoc: consulta por vídeo a partir de R$ 39,90, sem mensalidade.**
   - **Como funciona:** médico com CRM, por vídeo no navegador, sem instalar nada. Atende das 7h30 às 23h todos os dias, com espera média de 3 a 5 minutos.
   - **Documentos:** receita no padrão CFM com QR Code, atestado e encaminhamento.
   - **Pagamento:** Pix ou cartão, antes da consulta. Reembolso integral se a consulta não acontecer.
   Fonte: [linkadoc.com.br](https://linkadoc.com.br/), lida em 18/11/2026. É a primeira vez neste vigia.
   ![Linkadoc, R$ 39,90 avulso](https://agente.cassiogon.tech/prints/74a1039b54496fb9d9d790c7a651b787.jpg)
   - **E daí pro Calima:** passa a Telemedico (R$ 40) e vira o piso do avulso em vídeo. O Calima vende outra coisa: a consulta com o médico que o paciente já escolheu, com agenda. É isso que precisa aparecer no portal, e não preço.

2. **Consultar Médico: R$ 39,90 por vídeo, 24 h, com espera de 45 segundos.**
   - **Pagamento:** Pix ou cartão em até 3x. Não cobra se faltar médico.
   - **Documentos:** com ICP-Brasil, inclusive atestado de aptidão física, declaração de comparecimento e laudo.
   - **Âncora:** a página diz que "consulta avulsa costuma custar R$ 69–90".
   Fonte: [consultarmedico.com.br](https://consultarmedico.com.br/), lida em 18/11/2026. É a primeira vez neste vigia.
   ![Consultar Médico, R$ 39,90](https://agente.cassiogon.tech/prints/0a4485d01ca065e74afed00743840018.jpg)
   - **E daí pro Calima:** são dois players a R$ 39,90 no mesmo dia, o que indica que o preço de pronto-atendimento online está convergindo para esse valor.

3. **LoopMed e Olá Doutor: avulso por chat de R$ 39,90 a R$ 69.**
   - **LoopMed** ([loopmed.com.br](https://loopmed.com.br/)):
     - Clínica geral por chat: R$ 39,90 na 1ª consulta (cupom LOOP39) e R$ 59,90 depois.
     - Psiquiatria: R$ 99,90.
     - Anuncia um plano "em breve" a partir de R$ 89,90/mês.
   - **Olá Doutor** ([oladoutor.app/precos](https://oladoutor.app/precos/)):
     - Consulta Imediata: generalista a R$ 69 e especialista a R$ 119.
     - Planos de R$ 19,90, R$ 199,90 e R$ 399,90 por mês.
     - A Consulta Agendada tem preço definido por cada médico.
   - As duas lidas em 18/11/2026, primeira vez neste vigia.
   - **E daí pro Calima:** a Consulta Agendada do Olá Doutor é a única que se parece com o modelo do Calima (o médico define o preço). Fica como referência caso um dia o Calima deixe o profissional fixar o valor do avulso.

4. **Microsoft: o Dragon Copilot Transcribe passou para o motor próprio MAI-Transcribe-2 (Ignite 2026).**
   - **Números divulgados:** cerca de 10 milhões de consultas por mês e metade dos erros em conversa com troca de idioma. A WER média no FLEURS, em 60 idiomas, foi de 5,2%.
   - **Preço:** a fonte secundária fala em US$ 0,10 por hora de áudio.
   Fontes:
   - [lupai.ai](https://www.lupai.ai/pt/novo-modelo-adotado-pelo-dragon-copilot-transcribe-da-microsoft-alcancando-ganhos-significativos-na-precisao-da-transcricao-medica), de 18/11/2026, que cita a AIBase.
   - Post de Dominic King (Microsoft AI) no LinkedIn, cerca de 17/11.
   - O preço não foi conferido na página oficial.
   - **E daí pro Calima:** não é lançamento em pt-BR. Mas um STT multilíngue barato pode virar alternativa ou reserva ao Groq Whisper. Vale medir quando sair na Azure.

## Regulação

- **Meta/WhatsApp:** só repercussão (Correio Braziliense, 17/11) da cobrança da mensagem de serviço desde 01/10, já registrada.
- **CFM 2.454/2026:** só blog (Ordexa). Nada oficial novo.
- **Anvisa, ANPD, CFP, CFN, CFO, COFFITO, COFEN e Apple:** nada novo.

## Pressão de preço

- **Escriba:** sem mudança. O Ordexa segue a R$ 39,90, com plano grátis até 50 pacientes.
- **Tudo-em-um:** sem mudança.
- **Teleconsulta avulsa:** **sim, abaixo de R$ 49,90.** Linkadoc e Consultar Médico cobram R$ 39,90 por vídeo, e a LoopMed cobra R$ 39,90 na 1ª consulta por chat. São pronto-atendimento com médico de plantão, não o médico do paciente.
- **Secretária por profissional:** sem mudança, nada abaixo de R$ 99,90.

## Comoditização

- **Microsoft:** reforçou o Dragon Copilot com o STT próprio, mas sem pt-BR clínico.
- **ERPs:** nenhum passou a embutir o escriba de graça.

## Posicionamento

Sem mudança de recomendação. Uma nota para o avulso: com o piso em R$ 39,90 no pronto-atendimento, o portal do paciente deve vender "consulta com o seu médico" e não "consulta online". Se o preço do avulso for revisto, ele não deve ser comparado ao desses serviços.

---
Checado hoje:
- 8 buscas: escriba, secretária, rodadas, regulação, players globais, teleconsulta, WhatsApp e escriba por profissão.
- 6 páginas: Linkadoc, Consultar Médico, LoopMed, Olá Doutor, lupai.ai (Dragon), e os prints de duas delas.

Já registrados e não repetidos: Darwin Saúde, Alyvia, Clara, Carecode, Cloudia, Telepatia e Voa (15 mil/dia). Fora do escopo: Skedia (financeiro de clínica) e Clínica Experts (estética).

Reserva: nenhuma página precisou de reserva, tudo veio pelo agente web. Nenhum número foi estimado.

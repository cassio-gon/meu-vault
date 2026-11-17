---
title: Vigia de Concorrência — 2026-11-17
date: 2026-11-17
area: Concorrencia
tags: [concorrencia, mercado]
source: routine
aviso: enviado
---

## TL;DR

- **Klinity**, escriba novo para médico, nutricionista e psicólogo: grátis até 5 consultas, ilimitado por **R$ 199/mês**. É 4x o Calima.
- Três secretárias no WhatsApp entram no radar, todas para clínica e bem acima de R$ 99,90: **MEDX** (R$ 250/mês + R$ 1.000), **GeraCare** (R$ 610 + R$ 800, Meta e OpenAI à parte) e **Clinia** (a partir de R$ 890).
- Teleconsulta avulsa por chat da **Consulta+** custa R$ 79,90, acima dos R$ 49,90 do Calima.
- Sem mudança de preço no Calima nem de recomendação.

> Comparado com o relatório de **2026-11-16**. Varredura completa: não (é terça, e a última foi ontem). Só foram reabertas as páginas que apareceram no noticiário.
> Calima conferido no repo (`origin/main` `6e0ef3a`, o mesmo de ontem): R$ 49,90 no site, `VENDAVEIS = ['staff']`, defaults 4990/4990 e teste de 7 dias.

## Achados

1. **Klinity: escriba com grátis limitado e plano pago de R$ 199/mês.**
   - **O que faz:** grava a consulta, presencial ou teleconsulta, transcreve e monta o prontuário. Traz CID-10 para médico, TMB para nutricionista e DSM-5 para psicólogo. Exporta em PDF ou por cópia.
   - **Grátis:** R$ 0, com 5 consultas, 5 documentos e 45 min por consulta, sem envio por e-mail ou WhatsApp.
   - **Profissionais:** R$ 199/mês, com consultas ilimitadas e 2 h por consulta.

   Diz ter "+500" profissionais. Fonte: [klinity.com/pricing](https://www.klinity.com/pricing), lida em 17/11/2026, primeira vez neste vigia.
   - **E daí pro Calima:** é mais um escriba ilimitado que cobra 4x o Calima. Ele já cobre nutrição e psicologia, então não conta como lacuna dessas profissões.

2. **MEDX Care: secretária IA no WhatsApp por R$ 250/mês, no plano anual.**
   - **O que faz:** usa a API oficial da Meta e fica integrada ao sistema da MEDX. Atende até 2.000 pacientes por mês, recebe exames e fotos direto no prontuário e envia receita e pedido de exame.
   - **Custo:** R$ 1.000 de implantação mais R$ 3.000 por ano.
   - **Marketing ("em breve"):** cerca de R$ 0,35 por mensagem, repassados da Meta sem markup.

   Fonte: [care.medx.med.br/medbot](https://care.medx.med.br/medbot), lida em 17/11/2026.
   - **E daí pro Calima:** um ERP médico vende a secretária integrada ao prontuário a R$ 250. É a mesma proposta do add-on, e R$ 99,90 fica em 40% disso, sem taxa de implantação.

3. **GeraCare e Clinia: secretárias com CRM, para clínica e não para o profissional sozinho.**
   - **GeraCare** ([geracare.com.br](https://geracare.com.br/), tabela de novembro):
     - Professional: R$ 610/mês (R$ 549 no anual) mais R$ 800 de implantação, para 1 profissional e 2.000 atendimentos de IA por mês.
     - Atendimento extra de IA: R$ 0,27.
     - O WhatsApp Cloud API e a OpenAI são cobrados à parte.
   - **Clinia** ([clinia.io](https://clinia.io/)): R$ 890 / R$ 1.990 / R$ 4.900 por mês.
   - **Chiko** ([chiko.ai](https://www.chiko.ai/)): cobra "pelo que o agente resolve", com preço não público.
   - **E daí pro Calima:** a GeraCare põe um preço público no atendimento de IA, de R$ 0,22 a R$ 0,27. Serve de régua para o custo medido do piloto. Nenhum dos três mexe no piso de R$ 147 da AgendaCare para o profissional sozinho.

4. **Consulta+: teleconsulta avulsa só por chat, sem vídeo, por R$ 79,90.**
   - **Como funciona:** o paciente é atendido por chat, sem vídeo e sem hora marcada, ao longo de até dois dias. Recebe atestado, receita e pedido de exame com assinatura ICP-Brasil.
   - **Preço:** R$ 79,90 no Pix ou em até 12x.

   Publica uma página de transparência sobre IA, conforme a CFM 2.454. Fonte: [consultamais.app](https://consultamais.app/), lida em 17/11/2026.
   - **E daí pro Calima:** mais um avulso acima dos R$ 49,90. O piso segue na Telemedico, a R$ 40.

5. **Avie agora vende plano com prontuário com IA.** O Avie Cuida custa R$ 1.530/mês por clínica, mais R$ 2.550 de implantação. Inclui a secretária, as notas de consulta com IA (Avie Notes) e receita pela Memed. O Avie Atende segue a R$ 1.350 mais R$ 2.700, igual a 27/10. Fonte: [avie.me](https://avie.me/), lida em 17/11/2026.
   - **E daí pro Calima:** é mais um pacote de secretária com escriba, só que na faixa de clínica. Não muda nada para o profissional autônomo.

6. **Ninsaúde Safe, a gravação e transcrição de consulta da Ninsaúde, custaria "a partir de R$ 99".** A fonte é secundária ([rvsolutions10.com](https://rvsolutions10.com/blog/melhores-sistemas-para-clinicas.html), cerca de 4 dias atrás), sem dizer a periodicidade. A página oficial de planos dá 404. Fica como **não confirmado**.
   - **E daí pro Calima:** se o valor se confirmar, a Ninsaúde entra no grupo de ERPs que cobram o escriba à parte, por R$ 99 ou mais.

## Regulação

- **CFM 2.454/2026:** só conteúdo de blog (MedGuias, Chiko). Nada oficial novo.
- **Meta/WhatsApp:** os artigos da semana repetem a cobrança da mensagem de serviço acima da franquia e a categoria Business Agent, as duas já registradas.
- **Anvisa, ANPD, CFP, CFN, CFO, COFFITO, COFEN e Apple:** nada novo.

## Pressão de preço

- **Escriba:** quem entrou hoje (Klinity, a R$ 199) fica acima. O mais barato sem cota segue o Escriba Médico, a R$ 97, e a Klinity grátis (5 consultas) entra na lista dos grátis com limite.
- **Tudo-em-um:** sem mudança.
- **Teleconsulta avulsa:** a Consulta+ cobra R$ 79,90, e o piso segue na Telemedico, a R$ 40.
- **Secretária por profissional:** a MEDX cobra R$ 250 mais implantação, e nada abaixo de R$ 99,90.

## Comoditização

Nada novo. O escriba continua vendido à parte (Klinity a R$ 199, Ninsaúde Safe a partir de R$ 99, ainda sem confirmação).

## Posicionamento

Sem mudança de recomendação. As três de 16/11 continuam valendo: manter os R$ 49,90, lançar a secretária a R$ 99,90 (até R$ 129,90 se o custo pedir) e focar na enfermagem.

---
Checado hoje: 6 buscas (escriba, secretária, rodadas, regulação, WhatsApp e players globais) e 11 páginas: Klinity (duas), Avie, Consulta+, Clinia, GeraCare, MEDX, Chiko, Ninsaúde e o blog da RV Solutions. Reserva: nenhuma chamada fora do agente web. Dentro dele, uma página (MEDX) veio pelo Firecrawl cloud. Nenhum número foi estimado.

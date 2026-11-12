---
title: Vigia de Concorrência — 2026-11-12
date: 2026-11-12
area: Concorrencia
tags: [concorrencia, mercado]
source: routine
aviso: enviado
---

## TL;DR

- A **Aura (auraclinic.ai)** oferece de graça e para sempre prontuário com escriba por IA, receita e atestado assinados em ICP-Brasil e teleconsulta, sem limite de pacientes. Quem paga são farmacêuticas, que compram estudos feitos com dados anonimizados. Um Pro de R$ 99/mês vem "em breve".
- A Aura tem parceria com a Telepatia, que segundo o banner da Aura captou US$ 42 mi.
- A Aria, secretária no WhatsApp para consultório particular, cobra de R$ 449 a R$ 649/mês. O add-on de R$ 99,90 continua muito abaixo do mercado.
- O Gemini for Healthcare, do Google, é só para hospitais nos EUA. A regulação não mudou.

> Comparado com o relatório de **2026-11-11**. **Varredura completa:** não. Hoje é quinta, e a última completa foi em 09/11. Só foram abertas as páginas que apareceram no noticiário.
> Calima conferido no repo (`origin/main` `a7c0c60`): `site/index.html` segue com R$ 49,90 (7 ocorrências). O único commit novo é um e-mail da campanha. Nada mudou em `planos.js` nem em `env.js`.

## Achados

1. **Aura: prontuário com escriba de graça, pago por farmacêutica.** O Plano Padrão custa R$ 0 "para sempre", sem cartão, sem limite de pacientes e para até 20 profissionais por clínica. Ele inclui:
   - prontuário e agenda;
   - "consulta com IA": grava a conversa e escreve a evolução;
   - receita e atestado assinados em ICP-Brasil (VIDaaS e BirdID), enviados ao paciente pelo WhatsApp;
   - teleconsulta e o chat "Dr. Aurélio".

   A página anuncia "em breve" um **Pro a R$ 99/mês (R$ 79 no anual)**, com revisão clínica de cada documento. Ela também tem uma calculadora que compara a Aura com iClinic, Doctoralia, Voa, Noa Notes e outros.

   A conta fecha assim: "Farmacêuticas e outras empresas de saúde pagam por estudos com dados anonimizados". A Aura diz que não vende dados pessoais e que as consultas não treinam IA. O banner fala em "parceria com Telepatia · US$ 42 mi captados"; este vigia tinha registrado US$ 33 mi.

   Fontes: [auraclinic.ai/precos](https://auraclinic.ai/precos) e [/seguranca](https://auraclinic.ai/seguranca) (atualizada em 10/11/2026), lidas em 12/11/2026. O guia de "prontuário gratuito" da Aura é de 14/10, mas é a primeira vez que ela aparece neste vigia.
   ![Aura, prontuário grátis para sempre](https://agente.cassiogon.tech/prints/188301f56da517f1eeb5d6ccc6dca9ce.jpg)
   - **E daí pro Calima:** é o primeiro concorrente com escriba, ICP e teleconsulta a custo zero sem cota aparente. O preço deixa de ser argumento. A resposta é privacidade: no Calima, o nome do paciente é cifrado no aparelho e nenhum dado vira estudo para farmacêutica. Isso deve aparecer explícito no site e na campanha.

2. **Aria: secretária de IA no WhatsApp a R$ 449–649/mês.** É feita só para consultório particular. Atende 24 horas, "qualifica" o paciente com método consultivo e quebra de objeção, agenda no Google Agenda, faz follow-up dentro da janela de 24 horas e tem pipeline de 10 estágios. Os planos:
   - **Mensal:** R$ 649
   - **Trimestral:** R$ 549/mês
   - **Anual:** R$ 449/mês

   Não cobra setup, mas o primeiro passo é uma demonstração. Fonte: [ariasaude.ia.br](https://ariasaude.ia.br/), lida em 12/11/2026. É a primeira vez que a Aria aparece neste vigia.
   ![Aria, secretária médica de IA](https://agente.cassiogon.tech/prints/b0aa4f08d0bfda3aba317e0e38b455a0.jpg)
   - **E daí pro Calima:** é mais uma âncora alta, entre a Clara (R$ 690) e a Analu (R$ 197). O add-on de R$ 99,90 fica muito barato. A Aria se vende como "vendedora da consulta particular", e a Secretária do Calima pode se posicionar como agenda e cobrança transparentes.

3. **Google lança o Gemini for Healthcare.** É uma plataforma de agentes para hospitais e operadoras, com integração a Epic, Oracle e Suki. Por enquanto está em prévia só nos EUA. Fontes: [blog.google](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/gemini-for-healthcare/) e [Unite.AI](https://www.unite.ai/pt/google-cloud-opens-gemini-for-healthcare-preview-in-the-u-s/), 10/11/2026.
   - **E daí pro Calima:** nenhum efeito agora. Não há ditado clínico em pt-BR nem oferta para o profissional autônomo. Vale acompanhar se chega ao Brasil.

**Sem efeito no Calima:**
- A GestãoDS publicou um guia de preços para 2027 que cita a cobrança do WhatsApp pela API e a CFM 2.454 (11/11). Não há preço novo dela.
- A AD PRO vende um agente de IA sob medida para clínicas por R$ 4.000, pagos uma vez. Está fora do escopo do add-on.

## Regulação

- **CFM 2.454/2026:** só conteúdo de blog (Cliniq+, Laudos.AI), sem fato novo.
- **Marco legal de IA:** nada além do que já estava registrado em 11/11.
- **Anvisa, ANPD, CFP, CFN, CFO, COFFITO, COFEN, Apple e WhatsApp/Meta:** nada novo desde ontem.

## Pressão de preço

- **Escriba abaixo de R$ 49,90:** **sim, e agora sem cota aparente.** A Aura dá escriba, ICP e teleconsulta por R$ 0. Os grátis com limite seguem iguais (Voa Free, PoliHealth, Vokkari com 5 h). O empate em R$ 49,90 com o DataPronto continua.
- **Teleconsulta avulsa:** nada mudou.
- **Secretária por profissional:** a Aria fica em R$ 449–649/mês. O piso avulso segue em R$ 147 (AgendaCare).

## Comoditização

A Aura é o caso mais forte até agora de escriba como recurso grátis, bancado por dados agregados para a indústria e não pelo médico. Uma big tech lançou um produto de saúde (Google), mas para hospitais nos EUA e sem ditado em pt-BR. A Meta e o n8n não mudaram nada.

## Posicionamento

A recomendação (a) muda. As recomendações (b) e (c) seguem iguais.

- **(a)** Os R$ 49,90 continuam defensáveis, mas só com um "porquê pagar" explícito diante de um concorrente grátis. A sugestão é pôr no site e nos e-mails da Black Friday a frase "seus dados não viram produto: nome do paciente cifrado no aparelho, nada vendido a farmacêutica, ilimitado e sem cota". Não baixar o preço para competir com o grátis.
- **(b)** O add-on Secretária a R$ 99,90 segue abaixo de todo o mercado (R$ 147 a R$ 690, com a Aria a R$ 449–649). A recomendação não muda.
- **(c)** A nutrição continua a profissão menos servida. A Aura também é só para médico.

---
Ferramentas: o agente web atendeu tudo (8 buscas, 6 páginas e 2 prints). Nenhuma página precisou de reserva. Nenhum número foi estimado.

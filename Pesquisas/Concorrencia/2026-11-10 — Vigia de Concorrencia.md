---
title: Vigia de Concorrência — 2026-11-10
date: 2026-11-10
area: Concorrencia
tags: [concorrencia, mercado]
source: routine
aviso: enviado
---

## TL;DR

- A PoliHealth anuncia "prontuário, IA e gestão por R$ 49/mês" até 30/11, mas só nos 2 primeiros meses. Depois cobra R$ 399,90. É a primeira manchete de concorrente no preço do Calima.
- A Twofold entrou em pt-BR com escriba a R$ 99 no 1º mês e R$ 259 depois.
- A Analu (beta) cobra R$ 197/mês por profissional pela secretária no WhatsApp, com 250 conversas e R$ 0,80 por conversa extra. Fica acima dos R$ 99,90 do add-on.
- A Black Friday do Calima (preço de fundador travado em R$ 49,90 até 30/11) é a resposta certa: o desconto deles some e o preço do Calima fica.

> Comparado com o relatório de **2026-11-09**. **Varredura completa:** não. É terça, e a completa foi ontem. Só foram abertas as páginas que apareceram no noticiário.
> Preço do Calima conferido no repo (`origin/main` `3b507c0`): `site/index.html` mostra R$ 49,90 (7 ocorrências); `VENDAVEIS = ['staff']`; `PLANO_STAFF_CENTS` e `CONSULTA_AVULSA_CENTS` com default 4990; `TRIAL_DIAS` default 7.
> **Mudança do lado do Calima (09/11, `92c3dec`…`3b507c0`):** está pronta a campanha de Black Friday, com a página `site/black-friday.html`:
> - "preço de fundador" de R$ 49,90/mês enquanto a pessoa for assinante, para quem assinar até 30/11;
> - aviso de que "em 2027, o preço do Hipócrates sobe";
> - Hipócrates liberado até 30/11 para quem já tem conta e ainda não assina, com teto de 100 prontuários por dia;
> - 4 e-mails da campanha.
>
> A partir de hoje, este vigia compara os concorrentes com essa oferta.

## Achados

1. **PoliHealth: "Prontuário, IA e gestão da clínica por R$ 49/mês", na Black Friday até 30/11.** O preço vale só nos 2 primeiros meses de qualquer plano. Depois:
   - **Mensal:** R$ 399,90/mês.
   - **Semestral:** R$ 202/mês no 1º semestre e renovação a R$ 279,93.
   - **Anual:** R$ 174/mês no 1º ano, renovação a R$ 199,95 e um microfone de mesa de brinde.
   - **Grátis:** R$ 0, com 5 escutas por mês.

   A IA "escuta, organiza a nota e **sugere hipóteses**", e o áudio é apagado depois da transcrição. A página não mostra secretária no WhatsApp nem teleconsulta. Fonte: [polihealth.ai](https://polihealth.ai/), lido em 10/11/2026.
   ![PoliHealth, Black Friday R$ 49/mês](https://agente.cassiogon.tech/prints/282f24f93690393ff096d56de522db07.jpg)
   - **E daí pro Calima:** é o primeiro concorrente com manchete de preço igual à do Calima. O contra-argumento já está pronto na campanha: R$ 49 por 2 meses e depois R$ 399,90, contra R$ 49,90 travado enquanto a pessoa assinar e com teleconsulta incluída. Vale pôr essa comparação, sem citar a marca, num dos 4 e-mails.

2. **Twofold: escriba em pt-BR, com preço em reais.**
   - **Teste:** 7 dias grátis sem cartão, com registros ilimitados.
   - **Individual mensal:** R$ 99 no 1º mês e R$ 259/mês depois.
   - **Individual anual:** R$ 1.908, o que dá R$ 159/mês.
   - **Equipe:** sob medida.

   A Twofold publicou em novembro um ranking das "6 IAs no Brasil" (ela mesma, Voa, Anamne, Dr. Assistente, SmartDoctor e Dora). O Calima não aparece. Fontes: [trytwofold.com/pt-br/precos](https://www.trytwofold.com/pt-br/precos) e [o ranking no blog](https://www.trytwofold.com/pt-br/blog/melhores-ias-para-transcrever-consultas-medicas), lidos em 10/11/2026.
   ![Twofold, preços pt-BR](https://agente.cassiogon.tech/prints/9e6fbb61854a0439dd18dcc21bdbb8fd.jpg)
   - **E daí pro Calima:** é mais um player global no Brasil, com o teste igual ao do Calima (7 dias sem cartão) e preço 5x maior. Os rankings de "melhor IA para transcrever consulta" estão virando a vitrine de SEO do nicho, e o Calima não está em nenhum.

3. **Analu (beta): secretária de IA no WhatsApp com prontuário, a R$ 197/mês por profissional.**
   - **Plano Clínica:** R$ 197/mês por profissional, com 250 conversas por mês, R$ 0,80 por conversa extra e mensagens da Meta incluídas.
   - **Grátis:** prontuário, receita com ICP e até 10 teleconsultas por mês, sem a secretária.
   - **Teste:** 30 dias do plano Clínica.

   O agente do WhatsApp não lê o prontuário. Fonte: [analu.app](https://www.analu.app/), lido em 10/11/2026.
   ![Analu, secretária IA](https://agente.cassiogon.tech/prints/043b25ebfabb9fd9430a0731d9ef6dbe.jpg)
   - **E daí pro Calima:** é a primeira referência pública de preço por conversa (R$ 0,80) e de franquia por profissional (250). Isso ajuda a desenhar o teto do add-on de R$ 99,90.

4. **Outros escribas e secretárias encontrados hoje, nenhum abaixo de R$ 49,90:**
   - **Pronova Tech:** prontuário com escriba; Solo Plus a R$ 132,30/mês no anual com −30%, e 7 dias grátis ([pronovatech.com.br](https://pronovatech.com.br/)).
   - **RMED:** prontuário com escriba, copiloto e secretária no WhatsApp; preço não público, 30 dias grátis ([rmed.life](https://rmed.life/)).
   - **Alyvia:** assistente no WhatsApp do médico com um "Alyvia Scribe" novo; preço não público ([alyvia.com.br](https://alyvia.com.br/)).
   - **FluKAI:** CRM e secretária para clínica; R$ 297 nos 2 primeiros meses e R$ 594 depois, em pré-lançamento ([flukai.com.br](https://flukai.com.br/)).

   Todos foram lidos em 10/11/2026.
   - **E daí pro Calima:** a oferta de escriba e secretária em pt-BR se multiplicou, mas o piso pago segue a Dora, a R$ 79.

**Sem efeito no Calima:** a Rivio fechou uma Série A de R$ 180 mi, mas faz faturamento hospitalar ([Startups](https://startups.com.br/negocios/rodada-de-investimento/rivio-fecha-serie-a-de-r-180m-e-passa-de-r-1-bi-em-valuation/), há ~6 dias). Belle Software e Clínica nas Nuvens dão até 50% de desconto na Black Friday.

## Regulação

- **CFM 2.454/2026:** só matérias explicativas (Tua Saúde, 07/11), sem fato novo.
- **WhatsApp:** a CNDL (09/11) repete a cobrança por tokens do Business Agent (US$ 2 por 1 milhão de tokens) e a mensagem de serviço a US$ 0,0068, que já estavam no relatório de ontem.
- **Anvisa, ANPD, CFP, CFN, CFO, COFFITO, COFEN e Apple:** nada novo.

## Pressão de preço

- **Escriba abaixo de R$ 49,90:** a PoliHealth chega a R$ 49, mas só por 2 meses, e depois cobra de R$ 199,95 a R$ 399,90. O grátis dela tem 5 escutas por mês. Nenhum pago fica abaixo do Calima de forma permanente.
- **Teleconsulta avulsa:** nada mudou.
- **Secretária por profissional:** a Analu fica em R$ 197, acima do add-on. O piso avulso segue em R$ 147 (AgendaCare).

## Comoditização

Nada mudou. A Analu e o plano grátis da PoliHealth embutem prontuário de graça, mas isso já acontecia (Shosp, clina.ai). Nenhuma big tech lançou ditado clínico em pt-BR.

## Posicionamento

Há um ajuste na recomendação (a), e as recomendações (b) e (c) não mudam.

- **(a)** A oferta curta que a recomendação 1 de ontem pedia já existe: é o preço de fundador. Recomendação nova: na campanha, mostrar o custo dos concorrentes depois do 2º ou do 3º mês (PoliHealth R$ 399,90 e Twofold R$ 259, contra o Calima a R$ 49,90 para sempre).
- **(b)** A Analu reforça que o add-on de R$ 99,90 tem espaço. Para o desenho, considerar uma franquia de conversas, por exemplo 250 por mês, com excedente cobrado.
- **(c)** A nutrição continua a profissão menos servida.

---
Ferramentas: o agente web atendeu tudo (4 buscas, 2 extrações de 8 páginas e 3 prints). Nenhuma página precisou de reserva. Nenhum número foi estimado.

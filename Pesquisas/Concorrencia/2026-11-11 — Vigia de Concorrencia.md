---
title: Vigia de Concorrência — 2026-11-11
date: 2026-11-11
area: Concorrencia
tags: [concorrencia, mercado]
source: routine
aviso: enviado
---

## TL;DR

- O DataPronto vende prontuário com transcrição por IA, receita assinada (ICP) e agenda por **R$ 49,90/mês**, o mesmo preço do Calima, com 30 dias grátis. A IA tem uma cota mensal de tokens.
- A Clara, secretária no WhatsApp feita por um psiquiatra, cobra R$ 690/mês. Isso confirma que os R$ 99,90 do add-on ficam muito abaixo do mercado.
- A Voa diz que já faz 15 mil atendimentos por dia e prevê que o mercado vai passar a cobrar IA por crédito.
- A regulação não mudou.

> Comparado com o relatório de **2026-11-10**. **Varredura completa:** não. Hoje é quarta, e a última completa foi em 09/11. Só foram abertas as páginas que apareceram no noticiário.
> Calima conferido no repo (`origin/main` `22b0666`): `site/index.html` segue com R$ 49,90 (7 ocorrências). Desde `3b507c0` só entraram 2 ajustes de texto do e-mail E3 da campanha. Nada mudou em `planos.js` nem em `env.js`.

## Achados

1. **DataPronto: prontuário com escriba por R$ 49,90/mês.** Os três planos têm prontuário, agenda, página pública de agendamento, receita, atestado e exame assinados em ICP-Brasil, confirmação de consulta por WhatsApp e transcrição por IA:
   - **Starter:** R$ 49,90/mês, com 1 usuário e 200.000 tokens de IA por mês. Profissional a mais custa R$ 39,90 e secretária a mais, R$ 14,90.
   - **Pro:** R$ 69,90/mês, com 700.000 tokens.
   - **Clinic:** R$ 89,90/mês, com 2.000.000 tokens.

   Os planos têm 30 dias grátis e são pagos só com cartão (Stripe). Quando a cota acaba, a transcrição pausa até o mês seguinte ou até a compra de crédito avulso. O áudio é transcrito no Brasil e apagado em seguida, mas o texto transcrito vai para a OpenAI, nos EUA. A página não diz quantas consultas cabem em 200 mil tokens. Fontes: [datapronto.com.br/precos](https://datapronto.com.br/precos) e [/ia-transcricao-de-consultas](https://datapronto.com.br/ia-transcricao-de-consultas), lidas em 11/11/2026. É a primeira vez que o DataPronto aparece neste vigia.
   ![DataPronto, planos a partir de R$ 49,90](https://agente.cassiogon.tech/prints/e22c263f8654eb8b5d1743c21047d7e3.jpg)
   - **E daí pro Calima:** é o primeiro concorrente com escriba que cobra os mesmos R$ 49,90 de forma permanente, e não só como promoção. Ele leva vantagem em ICP, agenda pública e 30 dias de teste. O Calima ganha em quatro pontos: prontuários ilimitados (contra a cota de tokens), nome cifrado antes da IA (contra o texto que vai para a OpenAI), teleconsulta incluída e app na App Store.

2. **Clara: secretária de IA no WhatsApp a R$ 690/mês.** Foi criada por um psiquiatra (Dr. Luigi Fernando), para médico, psicólogo, dentista e nutricionista. Tem duas formas de começar:
   - **Pague o que usar:** R$ 150 de crédito grátis, que a página diz durar "cerca de 7 dias de uso", sem mensalidade e sem cartão.
   - **Starter:** R$ 690/mês, com 7 dias grátis, cartão no cadastro e −17% no anual.

   A secretária usa a API oficial da Meta, integra com o Google Calendar e o médico pode comandá-la pelo próprio WhatsApp. A página promete que "seus pacientes não percebem que é uma IA". Fonte: [clara.app.br](https://clara.app.br/#pricing), lida em 11/11/2026.
   ![Clara, planos](https://agente.cassiogon.tech/prints/7667a4b8efc25229dee075b75c60f977.jpg)
   - **E daí pro Calima:** é outra secretária "de médico para médico" e confirma que o add-on de R$ 99,90 está muito abaixo do mercado (Analu R$ 197, AgendaCare R$ 147, Clara R$ 690). A promessa de esconder que é IA é o oposto da transparência que a CFM 2.454 cobra. A Secretária do Calima pode usar isso como diferencial: ela se apresenta como assistente virtual.

3. **Voa Health passou de 15 mil atendimentos por dia.** A empresa bateu em setembro a meta de receita de 2026, mas não divulga o faturamento. Segundo o cofundador, o mercado de IA começa a cobrar por crédito, porque cada tarefa gasta tokens. A Voa acompanha esse modelo, mas hoje vende plano com uso ilimitado e usa modelos próprios. Fonte: [Saúde Insider](https://saudeinsider.com.br/voa-health-ultrapassa-15-mil-atendimentos-por-dia-e-atinge-em-nove-meses-a-receita-prevista-para-2026/), 11/11/2026.
   - **E daí pro Calima:** a Voa (Pro de R$ 289 a R$ 349) e o DataPronto (cota em tokens) mostram que "prontuários ilimitados por R$ 49,90" está ficando raro. Vale manter isso visível na campanha e ficar de olho no custo de IA por assinante.

**Sem efeito no Calima:**
- O dr.consulta disse em evento que limita a autonomia da IA em decisões clínicas ([TI Inside](https://tiinside.com.br/10/11/2026/dr-consulta-limita-autonomia-da-ia-em-decisoes-clinicas-para-preservar-seguranca-dos-pacientes/), 10/11). Não há mudança de preço nem de oferta.
- A Revena captou R$ 45 mi em seed, mas faz faturamento hospitalar.
- A "Tia Bete" é uma IA para diabetes, voltada ao paciente.
- O iClinic segue com o "iClinic IA" (transcrição, resumo e hipóteses) e cita a CFM 2.454 na página, o que não é novo.

## Regulação

- **CFM 2.454/2026:** só artigos de opinião (Executivos da Saúde, 10/11, e revista DCS), sem fato novo.
- **Marco legal de IA:** o Futuro da Saúde (~05/11) diz que pode avançar ainda em 2026. Não há votação marcada.
- **Anvisa, ANPD, CFP, CFN, CFO, COFFITO, COFEN, Apple e WhatsApp/Meta:** nada novo desde ontem.

## Pressão de preço

- **Escriba abaixo de R$ 49,90:** nenhum, mas **agora há um empate permanente**: o DataPronto Starter custa R$ 49,90, com cota de IA, 30 dias grátis, ICP e agenda. Os grátis com limite seguem iguais (Voa Free, PoliHealth Grátis).
- **Teleconsulta avulsa:** nada mudou.
- **Secretária por profissional:** a Clara fica em R$ 690/mês. O piso avulso segue em R$ 147 (AgendaCare).

## Comoditização

O DataPronto junta escriba, ICP e confirmação por WhatsApp num plano de entrada de R$ 49,90. É mais um caso de escriba embutido no ERP (iClinic e Amplimed já fazem isso), agora no preço mais baixo. Nenhuma big tech lançou ditado clínico em pt-BR. A Meta e o n8n não mudaram nada.

## Posicionamento

A recomendação (a) ganha um ajuste. As recomendações (b) e (c) não mudam.

- **(a)** Os R$ 49,90 continuam defensáveis, mas o argumento de preço já não basta contra o DataPronto. Para a campanha e o site, a diferença que vale destacar é **"ilimitado, sem cota de IA, e o nome do paciente cifrado antes de qualquer IA"**. O teste de 7 dias perde para os 30 dias do DataPronto e da Analu, mas a Black Friday já cobre isso até 30/11. Depois da campanha, avaliar se o teste deve passar para 14 dias.
- **(b)** O add-on Secretária a R$ 99,90 segue bem abaixo do mercado (R$ 147 a R$ 690). Recomendação inalterada.
- **(c)** A nutrição continua a profissão menos servida.

---
Ferramentas: o agente web atendeu tudo (6 buscas, 8 páginas e 2 prints). Nenhuma página precisou de reserva. Nenhum número foi estimado.

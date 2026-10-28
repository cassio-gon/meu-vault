---
title: Vigia de Concorrência — 2026-10-28
date: 2026-10-28
area: Concorrencia
tags: [concorrencia, mercado]
source: routine
---

## TL;DR

Sem mudança relevante desde 2026-10-27.

> Comparado com o relatório de **2026-10-27**. **Varredura completa:** não. Hoje é quarta, e a última completa foi em 26/10, há 2 dias. Ninguém novo apareceu no noticiário, então nenhuma página de preço foi reaberta.
> Preço do Calima conferido no repo (commit de 27/10): o `site/index.html` mostra R$ 49,90; `VENDAVEIS = ['staff']`; `PLANO_STAFF_CENTS` e `CONSULTA_AVULSA_CENTS` têm default 4990.

## Achados

Nenhum achado novo. Dois nomes surgiram nas buscas e foram descartados:

- **Memed, rodada de R$ 80 mi para IA na clínica:** a notícia é de 21/05/2026 ([startups.com.br](https://startups.com.br/negocios/healthtechs/memed-levanta-r-80m-para-levar-ia-a-clinica-medica/)). É antiga, mas não estava nos relatórios. Fica como contexto: a Memed, de prescrição, tem caixa para entrar em documentação clínica com IA. Vale observar se ela lança um scribe.
- **Voxmed, scribe em pt-BR com 10 consultas grátis:** só há um post antigo no TabNews e a página do Facebook, sem data nem preço público. Fica no radar; não é lançamento novo.
- **Tolki:** é a mesma matéria patrocinada de 26/10, agora também no Valor/Dino, e já estava no relatório de 27/10.

## Regulação

- **CFM 2.454/2026 e TRF1:** nenhuma decisão nova.
- **Anvisa, conselhos (CFP, CFN, CFO, COFFITO, COFEN) e ANPD:** nenhuma norma nova. A revisão da RDC 657 segue só na agenda regulatória.
- **WhatsApp Cloud API:** sem mudança. Os valores do Brasil desde 01/10 continuam: marketing R$ 0,3217, utilidade e serviço R$ 0,035, com 1.000 mensagens de serviço grátis por número a cada mês.
- **Apple:** sem mudança.

## Pressão de preço

Sem mudança. Ninguém vende scribe ilimitado abaixo de R$ 49,90. Os free tiers com limite (Voa, Dora, Telepatia) já estavam nos relatórios.

## Comoditização

Sem mudança. Nenhum ERP embutiu scribe, a Meta e o n8n não lançaram nada de graça, e nenhuma big tech lançou ditado clínico em pt-BR.

## Posicionamento

Sem mudança de recomendação.

## O que foi checado em 28/10/2026

- **Notícias:** Firecrawl (notícias de 24 h e de 7 dias) e WebSearch.
  - Prontuário e scribe com IA, rodadas e lançamentos de healthtechs.
  - Secretária IA no WhatsApp.
  - Menções a Doctoralia, iClinic, Feegow, Simples Dental e Voa.
  - CFM 2.454 e TRF1, Anvisa (SaMD) e preço e regras da WhatsApp API.
- **Lacunas:**
  - O agente web (MCP `agente-web`) não estava disponível nesta sessão de nuvem, então a rotina usou a reserva: Firecrawl e WebSearch.
  - A busca de notícias de 24 h do Firecrawl veio vazia.
  - Nenhum número foi estimado.

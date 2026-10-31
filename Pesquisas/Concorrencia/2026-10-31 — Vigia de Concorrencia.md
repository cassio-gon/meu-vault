---
title: Vigia de Concorrência — 2026-10-31
date: 2026-10-31
area: Concorrencia
tags: [concorrencia, mercado]
source: routine
---

## TL;DR

Sem mudança relevante desde 2026-10-30.

> Comparado com o relatório de **2026-10-30**. **Varredura completa:** não. Hoje é sábado, e a última completa foi em 26/10, há 5 dias. Nenhum alvo da lista apareceu com novidade, então nenhuma página de preço foi reaberta.
> Preço do Calima conferido no repo (`origin/main` `97695a0`): o `site/index.html` mostra R$ 49,90; `VENDAVEIS = ['staff']`; `PLANO_STAFF_CENTS` e `CONSULTA_AVULSA_CENTS` têm default 4990.

## Achados

1. **A Doutor.AI diz ter 98% de acurácia em mais de 700 mil atendimentos.** Funciona em pronto-socorro, preenche o prontuário e roda em 35 hospitais, com meta de 100 contratos até o fim do ano. Não há rodada nova.
   - Fonte: [Saúde Digital News](https://saudedigitalnews.com.br/27/10/2026/healthtech-atinge-98-de-acerto-em-700-mil-casos-e-supera-teste-de-validacao-medica/), publicada em 27/10/2026 e lida em 31/10.
   - **E daí pro Calima:** pouco. A Doutor.AI vende para hospitais, não para o plantonista que paga do próprio bolso. Mas é a mesma dor (o plantão), e o número de 98% vai aparecer em comparação com o Calima.
2. **Meu Prontuário no WhatsApp é um app novo nos relatórios.** O paciente registra consultas, exames e remédios por texto, áudio ou foto, e o app exporta em HL7 FHIR. Tem plano grátis e plano pago.
   - Fonte: [meuprontuario.ai](https://www.meuprontuario.ai/), lido em 31/10/2026.
   - O preço do plano pago não é público, e a data de lançamento não aparece no site.
   - **E daí pro Calima:** é um registro de saúde pessoal do paciente, não prontuário do profissional, então não concorre. Mas mostra que o paciente já aceita guardar dado de saúde num WhatsApp com IA, o que favorece a secretária do portal.

**Descartados nas buscas:**
- **Doctoralia:** a Nova é só do México, e o Noa Notes e o Noa Evidence já estão registrados.
- **Voa, NAIA e Pixeon:** só notícias antigas. A NAIA cita uma captação planejada, mas nenhuma rodada.
- **Teleconsulta (Dr. Consulta, Conexa, Einstein Conecta):** nada novo.
- **Secretária IA no WhatsApp:** só vagas de freelancer e produtos genéricos (Clínica Work, AiSensy, Maria IA na Hotmart). Nenhum lançamento.

## Regulação

- **CFM 2.454/2026:** a ação que pede a suspensão segue sem decisão noticiada.
- **Conselhos e órgãos:** nenhuma norma nova do CFP, CFN, CFO, COFFITO, COFEN, ANPD ou Anvisa, nem da Apple.
- **WhatsApp:** nada além da cobrança de 01/10, já registrada. O Meta Business Agent cobra por token desde agosto, e a IA que só faz atendimento continua permitida.

## Pressão de preço

Sem mudança desde 30/10.

## Comoditização

Sem mudança desde 30/10.

## Posicionamento

Sem mudança de recomendação.

## O que foi checado em 31/10/2026

- **Notícias:** WebSearch (standard e extended).
  - Prontuário com IA e rodadas de healthtechs com transcrição.
  - Doctoralia, iClinic, Feegow e Voa.
  - Secretária IA no WhatsApp.
  - Teleconsulta avulsa.
  - CFM 2.454, conselhos e ANPD.
  - Preço e regras da WhatsApp API.
- **Páginas lidas com Firecrawl:** Saúde Digital News (Doutor.AI) e meuprontuario.ai.
- **Lacunas:**
  - O agente web (MCP `agente-web`) não estava disponível nesta sessão de nuvem, então a rotina usou a reserva: WebSearch e Firecrawl.
  - Nenhum número foi estimado.
- **Próxima varredura completa:** segunda, 02/11.

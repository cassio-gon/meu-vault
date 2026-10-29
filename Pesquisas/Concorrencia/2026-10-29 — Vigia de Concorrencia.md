---
title: Vigia de Concorrência — 2026-10-29
date: 2026-10-29
area: Concorrencia
tags: [concorrencia, mercado]
source: routine
---

## TL;DR

- Achamos mais um scribe em pt-BR, o Vokkari Med: grátis com 5 h de gravação sem prazo; o pago começa em R$ 179,99/mês. Tem app iOS e hipótese diagnóstica por IA.
- Fora isso, nada mudou desde 2026-10-28. O TRF1 ainda não decidiu sobre a CFM 2.454.

> Comparado com o relatório de **2026-10-28**. **Varredura completa:** não. Hoje é quinta, e a última completa foi em 26/10, há 3 dias. Só reabri a página de quem apareceu no noticiário (Vokkari).
> Preço do Calima conferido no repo (`origin/main` `0972d2e`, 29/10): o `site/index.html` mostra R$ 49,90; `VENDAVEIS = ['staff']`; `PLANO_STAFF_CENTS` e `CONSULTA_AVULSA_CENTS` têm default 4990.

## Achados

1. **Vokkari Med: scribe em pt-BR que ainda não estava nos relatórios.** Grava a consulta, inclusive offline e na teleconsulta pelo navegador. Gera 9 documentos (receita, atestado, pedido de exame etc.) com o CRM do médico e assina com VIDaaS. Tem apps para iOS e Android e versão no navegador. Os planos:
   - **Grátis:** R$ 0, com 5 h de gravação que não expiram, 10 pacientes, marca d'água e sem cartão.
   - **Essencial:** R$ 179,99/mês, ou R$ 164,99 no anual, com 80 h/mês.
   - **Profissional:** R$ 449,99/mês, com 200 h/mês.

   Inclui uma **"Opinião da IA" (hipótese diagnóstica com até dois diferenciais)** em todos os planos, inclusive no app iOS. A home cita "Psicologia e dezenas de outras especialidades", mas o texto é todo voltado a médico.
   - Fonte: [vokkari.com](https://vokkari.com/), lido em 29/10/2026 (maxAge 0). Comparativo do próprio Vokkari, com preços reconferidos em 15/09/2026: [vokkari.com/blog/alternativa-voa-health](https://vokkari.com/blog/alternativa-voa-health/).
   - **E daí pro Calima:**
     - O Vokkari custa 3,6 vezes o Calima e mede o uso em horas. O "ilimitado por R$ 49,90" segue sem par.
     - A hipótese diagnóstica no iOS é justamente o recurso que a Apple barrou no Calima em 30/09. Vale ver se a Apple o tolera por lá (talvez pelo aviso de revisão obrigatória) antes de cogitar devolver a Sugestão IA. Não reintroduzir sem checar com a Apple e com a Anvisa.

2. **Escriba Médico: scribe por R$ 97/mês com consultas ilimitadas.** O preço cheio é R$ 149,90, ou R$ 997/ano, com 15 dias de teste. Gera prontuário, receita, evolução, atestado e encaminhamento.
   - Fonte: só o comparativo do Vokkari, de 15/09/2026, no link acima. **Não conferi na página oficial**, que a busca não achou. Trate como "segundo concorrente".
   - **E daí pro Calima:** se o número se confirmar, é o scribe ilimitado pago mais barato depois do Calima. Mesmo assim fica quase o dobro dos R$ 49,90.

**Descartados nas buscas:**
- **Conexa compra iMedicina:** a notícia é de 2020.
- **iClinic Assist em Beta e Noa Notes no VIP da Feegow por R$ 249:** já estavam no radar, ou são comparativos antigos sem data nova.
- **Blog da Voa (23 e 27/10):** são posts sobre TISS, não lançamento.

## Regulação

- **CFM 2.454/2026 e TRF1:** nenhuma decisão nova.
- **Anvisa, conselhos (CFP, CFN, CFO, COFFITO, COFEN) e ANPD:** nenhuma norma nova. A revisão da RDC 657 segue só na agenda 2026–2027.
- **WhatsApp Cloud API:** sem mudança. Desde 01/10, marketing custa R$ 0,3217 e utilidade R$ 0,035. A cobrança de US$ 0,0625 por mensagem de chatbot de IA de terceiros, de março, já era conhecida.
- **Apple:** sem mudança de regra.

## Pressão de preço

- **Scribe:** entram mais dois free tiers com limite: o Vokkari (5 h) e, se confirmado, o teste de 15 dias do Escriba Médico. Já havia o do Voa, o da Dora e o da Telepatia. O pago ilimitado mais barato além do Calima seria o Escriba Médico, a R$ 97, ainda não confirmado. Ninguém vende scribe ilimitado abaixo de R$ 49,90.
- **Tudo-em-um, teleconsulta avulsa e secretária por profissional:** sem mudança.

## Comoditização

Sem mudança. Nenhum ERP novo embutiu scribe, a Meta e o n8n não lançaram nada de graça, e nenhuma big tech lançou ditado clínico em pt-BR.

## Posicionamento

Sem mudança de recomendação. Uma nota para o próximo ciclo: os concorrentes já empilham assinatura VIDaaS e documentos com o CRM do médico. Se o Calima não assina digitalmente, isso pode virar objeção na venda.

## O que foi checado em 29/10/2026

- **Notícias:** WebSearch (standard e extended) e Firecrawl (notícias de 7 dias, que veio vazia).
  - Prontuário e scribe com IA, lançamentos de healthtechs.
  - Secretária IA no WhatsApp.
  - Voa, Noa Notes, iClinic e Feegow.
  - Teleconsulta avulsa (Conexa, Dr. Consulta, Einstein Conecta).
  - CFM 2.454 e TRF1, Anvisa (SaMD) e preço e regras da WhatsApp API.
- **Páginas reabertas:** vokkari.com (home e blog), com Firecrawl.
- **Lacunas:**
  - O agente web (MCP `agente-web`) não estava disponível nesta sessão de nuvem, então a rotina usou a reserva: WebSearch e Firecrawl.
  - A página oficial do Escriba Médico não foi achada.
  - Nenhum número foi estimado.

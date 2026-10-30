---
title: Vigia de Concorrência — 2026-10-30
date: 2026-10-30
area: Concorrencia
tags: [concorrencia, mercado]
source: routine
---

## TL;DR

Sem mudança relevante desde 2026-10-29.

> Comparado com o relatório de **2026-10-29**. **Varredura completa:** não. Hoje é sexta, e a última completa foi em 26/10, há 4 dias. Ninguém da lista de alvos apareceu no noticiário, então nenhuma página de preço foi reaberta.
> Preço do Calima conferido no repo (`origin/main` `97695a0`, 29/10): o `site/index.html` mostra R$ 49,90; `VENDAVEIS = ['staff']`; `PLANO_STAFF_CENTS` e `CONSULTA_AVULSA_CENTS` têm default 4990.

## Achados

1. **Alice (operadora) capta US$ 40 milhões em Série D liderada pelo IFC.** Tem um copiloto que transforma a conversa em rascunho de consulta para o médico da própria rede revisar. A notícia é de cerca de 20/10 e ainda não estava nos relatórios.
   - Fonte: [startups.com.br](https://startups.com.br/negocios/rodada-de-investimento/alice-capta-us-40m-para-ser-healthtech-ai-first/), achada em 30/10/2026. A data exata não foi conferida na página.
   - **E daí pro Calima:** nenhum. É uma ferramenta interna de um plano de saúde, não vendida ao profissional autônomo. Só confirma que "scribe" virou recurso padrão.

**Descartados nas buscas:**
- **CADE e a liberação de IA de terceiros no WhatsApp:** a notícia é de 06/03/2026 e a cobrança já está nos relatórios.
- **Cobrança das mensagens de serviço:** R$ 0,035, com franquia de 1.000 por mês e por número. É a regra de 01/10, também já registrada.
- **Memed (R$ 80 mi), Telepatia (US$ 33 mi) e Voa (1 milhão de consultas):** notícias antigas, já registradas.
- **Transcrição para psicólogo, nutricionista e fisioterapeuta:** só blogs de fornecedores estrangeiros (Sonix, Upheal, Freed). Nenhum lançamento novo em pt-BR.

## Regulação

- **CFM 2.454/2026 e TRF1:** nenhuma decisão nova. A ação que pede a suspensão segue sem liminar noticiada.
- **Anvisa, conselhos (CFP, CFN, CFO, COFFITO, COFEN), ANPD e Apple:** nenhuma norma nova.
- **WhatsApp Cloud API:** sem mudança desde 01/10.

## Pressão de preço

Sem mudança. Ninguém vende scribe ilimitado abaixo de R$ 49,90. Seguem os free tiers com limite já listados: Voa, Dora, Telepatia e Vokkari. O Escriba Médico, a R$ 97, segue sem confirmação na página oficial.

## Comoditização

Sem mudança. Nenhum ERP novo embutiu scribe, a Meta e o n8n não lançaram nada de graça, e nenhuma big tech lançou ditado clínico em pt-BR.

## Posicionamento

Sem mudança de recomendação.

## O que foi checado em 30/10/2026

- **Notícias:** WebSearch (standard e extended).
  - Prontuário e scribe com IA, e rodadas de healthtechs.
  - Voa, iClinic, Doctoralia e Feegow.
  - Secretária IA no WhatsApp.
  - Teleconsulta avulsa (Conexa, Dr. Consulta, Einstein Conecta).
  - Transcrição para psicologia, nutrição e fisioterapia.
  - CFM 2.454 e TRF1, e preço e regras da WhatsApp API.
- **Páginas lidas com Firecrawl:** Canaltech (CADE, 06/03) e Forbes (cobrança de 01/10), só para datar as notícias.
- **Lacunas:**
  - O agente web (MCP `agente-web`) não estava disponível nesta sessão de nuvem, então a rotina usou a reserva: WebSearch e Firecrawl.
  - Nenhum número foi estimado.
- **Próxima varredura completa:** segunda, 02/11.

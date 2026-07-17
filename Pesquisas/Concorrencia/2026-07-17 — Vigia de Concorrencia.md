---
title: Vigia de Concorrência — 2026-07-17
date: 2026-07-17
area: Concorrencia
tags: [concorrencia, mercado]
source: routine
---

# Vigia de Concorrência — semana de 2026-07-17

> Comparado contra o relatório de **2026-07-15** (só 2 dias de intervalo — a maior parte do
> cenário não mudou nesse período curto). Este relatório reporta só o que é genuinamente novo
> ou que o relatório anterior não tinha capturado.

## Achados

1. **Evolution API (v2.4.0, lançada 06/05/2026) passou a exigir ativação de licença — e isso
   pode derrubar a Secretária IA em produção sem aviso.** A partir dessa versão, toda instância
   precisa ser ativada contra o servidor de licenciamento da Evolution Foundation; até a
   ativação, **todo endpoint de negócio (inclusive os chamados pelo n8n) devolve
   `503 LICENSE_REQUIRED`**. A licença community é grátis, mas a ativação exige login manual e
   interativo no painel `/manager` num navegador — não existe variável de ambiente ou modo
   headless documentado. Há uma issue aberta (#2534, maio/2026, sem resposta oficial) de
   desenvolvedores relatando exatamente esse problema em deploys automatizados (Docker,
   Kubernetes, CI/CD). Fontes:
   [github.com/evolution-foundation/evolution-api/releases](https://github.com/evolution-foundation/evolution-api/releases)
   (nota da v2.4.0, 06/05/2026),
   [issue #2534](https://github.com/evolution-foundation/evolution-api/issues/2534).
   **E daí pro Cássio:** o relatório da semana passada já registrava a instância em v2.3.4
   (anterior a essa mudança) — mas a Secretária IA roda em Coolify com auto-deploy, exatamente o
   cenário que a issue #2534 descreve como quebrado. Se a imagem do Evolution API for atualizada
   (manual ou automaticamente) para ≥2.4.0, **todas as mensagens da secretária param de sair**
   até alguém logar manualmente no `/manager` e ativar a licença — silencioso até o primeiro
   cliente reclamar. **Prioridade imediata, antes de qualquer decisão de preço:** checar a versão
   em produção agora e decidir conscientemente entre travar em <2.4.0 ou ativar a licença
   community de propósito (documentando o processo, já que não é automatizável).

2. **ANPD avalia abrir processos sancionadores contra 21 entidades brasileiras** — sinal de
   escalada geral na fiscalização da LGPD, publicado há ~18h (16/07/2026). Não é notícia
   específica de saúde, mas especialista consultado (Lucas Paglia) descreve como "nova fase" da
   atuação da autoridade, saindo do modo orientativo para o sancionador. Fonte:
   [segs.com.br, 17/07/2026](https://www.segs.com.br/seguros/451499-anpd-avalia-processos-contra-21-entidades-e-reforca-fiscalizacao-da-lgpd).
   **E daí pro Cássio:** reforça o achado da semana passada (vazamento de 500 mil prontuários) —
   não foi um caso isolado, a ANPD está ampliando fiscalização de forma geral. Continua validando
   usar a cifra local de nome de paciente do Prontuário IA como argumento de blindagem
   regulatória, não só feature técnica.

3. **Heidi Health confirma tier 100% grátis e ilimitado de documentação por IA** — verificado por
   leitura direta da página oficial (não em relatório anterior): plano Free = US$ 0, transcrição
   e "Evidence" (citações clínicas) ilimitados; planos pagos Clinician US$ 110/mês e Practice
   US$ 180/mês (cobrança anual). Fonte:
   [heidihealth.com/pricing](https://www.heidihealth.com/en-us/pricing) (lido diretamente,
   17/07/2026). **E daí pro Cássio:** é o primeiro "de graça" confirmado por fonte primária entre
   os scribes internacionais — ainda não é ameaça direta no Brasil (produto em inglês, GTM
   global, sem menção a mercado brasileiro), mas se a Heidi localizar para pt-BR mantendo o tier
   grátis, isso pressiona o R$ 19,90 do Prontuário IA de um jeito que nenhum concorrente nacional
   pressiona hoje. Vale um alerta recorrente (não é urgente agora).

4. **Doctoralia lançou "Noa Evidence"**, um assistente de IA para suporte à decisão clínica
   baseado em literatura médica (não é scribe nem prontuário por voz) — lançado há
   aproximadamente 1 mês, não capturado no relatório-baseline de 07-15. Fonte:
   [medicinasa.com.br, ~jun/2026](https://medicinasa.com.br/doctoralia-noa-evidence/).
   **E daí pro Cássio:** a Doctoralia (que controla a Feegow) está investindo em camadas de IA
   clínica além de agendamento — ainda não compete com o Prontuário IA, mas é o tipo de produto
   que pode evoluir para sugestão de CID-10/conduta (item #1 do roadmap competitivo definido
   contra a Amplimed em 16/07). Vale monitorar se a Noa Evidence ganha essa função.

## Pressão de preço

- **Ninguém identificado abaixo de R$ 19,90/mês** entre concorrentes diretos brasileiros nesta
  rodada (sem mudança em relação à semana passada).
- **Heidi Health tem tier grátis ilimitado confirmado por fonte primária** (achado 3) — é hoje o
  "de graça" mais concreto de toda a categoria de scribe, mas ainda fora do radar de mercado
  brasileiro.
- A licença community da Evolution API (achado 1) também é grátis — mas isso não é pressão de
  preço, é fricção operacional nova numa peça de infraestrutura que a Secretária IA usa de graça
  hoje.

## Comoditização

- Nada novo de Meta/n8n oferecendo agendamento nativo grátis nesta janela curta — o risco já
  registrado semana passada (Meta Business Agent) segue de pé, sem atualização.
- **Movimento oposto identificado na Evolution API** (achado 1): em vez de ficar mais
  "commoditizada" (grátis e sem fricção), ela ganhou uma trava de licenciamento que quebra
  justamente o uso automatizado/self-hosted que sustenta a Secretária IA. Não é uma ameaça
  competitiva — é um risco de disponibilidade da própria operação.

## Posicionamento — recomendações

1. **R$ 19,90/mês + piloto grátis 7 dias do Prontuário IA continuam defensáveis.** Nenhum
   concorrente brasileiro chega perto; o único "de graça" real (Heidi Health, achado 3) ainda não
   opera no Brasil. Manter, mas registrar Heidi Health como o item a re-checar se ela anunciar
   localização pt-BR.
2. **Mensalidade B2B da Secretária IA — mantém a âncora sugerida semana passada: R$ 197–297/mês
   por clínica.** Nada nesta rodada muda esse cálculo (segue pendente modelar o custo pós-Meta de
   01/10/2026, como já recomendado).
3. **Nova prioridade, à frente de qualquer decisão de preço: auditar a versão do Evolution API em
   produção hoje** (achado 1). É o único achado desta rodada com risco de derrubar receita
   **atual**, não só futura — um auto-deploy do Coolify pode saltar para v2.4.0+ e travar o envio
   de mensagens até ativação manual no `/manager`. Decidir conscientemente: travar a versão ou
   ativar a licença community de propósito, documentando o passo (não é automatizável hoje).

## Nota metodológica

Firecrawl operou normalmente nesta rodada (sem o erro 402 da semana passada), permitindo leitura
direta de várias páginas oficiais (Heidi Health, Amplimed, GitHub). iClinic e Ninsáude devolveram
404 nas URLs de plano testadas — preços desses dois seguem não confirmados por fonte primária
nesta rodada (sem mudança em relação à semana passada). Janela de comparação é de apenas 2 dias
(07-15 → 07-17); a maior parte do cenário de mercado não teve tempo de mudar nesse intervalo — os
achados acima são os que genuinamente não estavam no relatório anterior.

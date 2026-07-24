---
title: Vigia de Concorrência — 2026-07-24
date: 2026-07-24
area: Concorrencia
tags: [concorrencia, mercado]
source: routine
---

# Vigia de Concorrência — semana de 2026-07-24

> Comparado contra o relatório de **2026-07-17** (uma semana de intervalo). Reporta só o que é
> genuinamente novo ou que os relatórios anteriores não tinham capturado.

## Achados

1. **A Amplimed (maior EMR/agenda tradicional do Brasil) passou a vender um módulo separado de
   "assistente virtual que conversa com pacientes e organiza agendamentos" — distinto do módulo
   de confirmações automáticas por WhatsApp que já existia.** Na página de planos atual, os
   add-ons contratáveis à parte agora são quatro: confirmações por WhatsApp (não-IA), SMS,
   "Amélia Transcrição" (voz→prontuário) e este novo assistente conversacional. Preço não
   divulgado ("Vamos conversar"); a página tem `modified_time` de 21/07/2026, dentro da janela
   desta semana. Fontes:
   [amplimed.com.br/planos-e-recursos](https://www.amplimed.com.br/planos-e-recursos/) e
   [amplimed.com.br/consultorio-planos](https://www.amplimed.com.br/consultorio-planos/) (lidas
   diretamente, 24/07/2026). **E daí pro Cássio:** é a primeira vez que a maior concorrente de
   EMR tradicional expõe publicamente um produto que faz exatamente o que a Secretária IA faz
   (agente conversacional que agenda pelo WhatsApp) — antes só existia a Amélia por voz. Clínicas
   que já usam Amplimed agora têm a opção "já estou aqui, só ligo o módulo" como objeção
   comercial. Prioridade: mystery-shop o preço desse módulo (contato comercial da própria
   Amplimed) antes de fechar a mensalidade B2B.

2. **O nicho de "secretária IA por WhatsApp para clínicas" (o produto exato da Secretária IA)
   ficou mais lotado — e pela primeira vez apareceram dois concorrentes diretos brasileiros com
   preço público real.** Mapeamento desta rodada encontrou pelo menos 6 players dedicados que não
   constavam nos relatórios anteriores: **Secretar.AI**, **Syntia**, **IA Secretária**
   (ia-secretaria.com.br), **usesecretariaia.com**, Cloudia e WorkAI. Dois têm preço público:
   - **Secretar.AI**: planos Solo R$ 300/mês, Consultório R$ 600/mês, Clínica R$ 900/mês (todos
     com desconto anual de 50%), posicionado como plataforma completa (WhatsApp + agenda +
     prontuário + financeiro + marketing/TV de recepção), mais focado em clínicas estéticas.
   - **Syntia**: mensalidade padrão R$ 247/mês, mas com **promoção que trava o assinante em
     R$ 97/mês indefinidamente** enquanto a assinatura ficar ativa sem interrupção (conforme os
     próprios termos de uso).
   Fontes: [secretar.ai](https://secretar.ai/) e
   [syntiamed.com/termos-de-uso](https://syntiamed.com/termos-de-uso) (lidas diretamente,
   24/07/2026). **E daí pro Cássio:** é a primeira âncora de preço real do concorrente que vende
   a mesma coisa que a Secretária IA (não sistemas de agenda genéricos) — a Syntia entra **abaixo**
   até da faixa R$ 197–297/mês sugerida nos relatórios anteriores, e o Secretar.AI mostra que o
   teto de mercado para uma plataforma completa passa de R$ 900/mês. Isso dá range real pra
   ancorar a mensalidade B2B pela primeira vez (ver recomendação 2 abaixo).

3. **O bug de licenciamento da Evolution API (issue #2534, flagrado como prioridade máxima no
   relatório de 17/07) segue sem solução oficial** — última resposta de um mantenedor foi em
   14/05/2026 ("se vão continuar exigindo ativação manual, precisa ter forma de ativar
   automaticamente"), sem PR, sem variável de ambiente documentada, sem modo headless confirmado.
   Uma busca secundária mencionou "ativação automática opcional" nas versões 2.4.x, mas isso
   **não aparece na thread da issue nem foi confirmado por leitura primária** — tratar com
   ceticismo até verificar diretamente no changelog oficial. Fonte:
   [github.com/evolution-foundation/evolution-api/issues/2534](https://github.com/evolution-foundation/evolution-api/issues/2534)
   (lida diretamente, 24/07/2026). **E daí pro Cássio:** a ação pendente da semana passada
   ("auditar a versão em produção agora, decidir travar ou ativar de propósito") continua sem
   solução alternativa vinda do projeto — segue sendo responsabilidade 100% do lado de cá.

4. **iClinic — primeira leitura direta confirmada da página oficial de preços** (bloqueada por
   403 nas duas rodadas anteriores): 4 planos por profissional de saúde — Starter R$ 99, Plus
   R$ 129, Pro R$ 169, Premium R$ 299/mês. Fonte:
   [iclinic.com.br/precos](https://iclinic.com.br/precos/) (lida diretamente, 24/07/2026).
   **E daí pro Cássio:** confirma e estende o range já estimado (R$ 99–169) com um teto agora
   conhecido de R$ 299 — mais um dado primário mostrando que nenhum concorrente tradicional de
   agenda/EMR chega perto do R$ 19,90 do Prontuário IA.

5. **Doctoralia "Noa Evidence" (citado no relatório de 17/07 como já lançado) foi lançado
   especificamente no Chile em julho/2026, não no Brasil** — cobertura de imprensa chilena
   (g5noticias.cl, pauta.cl, entre outros) confirma lançamento local, gratuito, sem menção a
   operação brasileira. Fonte:
   [pauta.cl, 14/07/2026](https://www.pauta.cl/actualidad/2026/07/14/doctoralia-presento-noa-evidence-en-chile-la-ia-que-ayuda-a-medicos-a-consultar-evidencia-cientifica-en-segundos.html).
   **E daí pro Cássio:** corrige a leitura anterior — ainda não é uma ameaça no mercado brasileiro
   do Prontuário IA. Vale monitorar se replica para o Brasil, mas sem urgência.

6. **Freed (scribe internacional) redesenhou a página de preços com planos promocionais mais
   baixos**: Starter US$ 39/mês (de US$ 59), Premier US$ 104/mês anual (de US$ 119) — primeira
   leitura direta deste concorrente (não constava em relatórios anteriores). Fonte:
   [getfreed.ai/pricing](https://www.getfreed.ai/pricing) (lida diretamente, 24/07/2026).
   **E daí pro Cássio:** reforça (não muda) a tese já registrada com a Heidi Health — a categoria
   internacional de scribe está com pressão de preço de entrada. Ainda em dólar/GTM americano, sem
   sinal de localização pt-BR.

## Pressão de preço

- **Prontuário IA (R$ 19,90):** ninguém identificado abaixo disso entre concorrentes diretos
  brasileiros nesta rodada — sem mudança em relação às semanas anteriores.
- **Secretária IA (mensalidade B2B ainda indefinida):** pela primeira vez há pressão real e
  mensurável — a **Syntia entra em R$ 97/mês (promoção travada)**, abaixo da faixa R$ 197–297
  sugerida antes. É o "abaixo de X" mais concreto encontrado até hoje para o produto exato que a
  Secretária IA vende (não um sistema de agenda genérico).

## Comoditização

- **Amplimed (achado 1) é o movimento mais relevante da rodada**: o maior player de EMR
  tradicional do Brasil começou a empacotar um assistente conversacional de WhatsApp como add-on
  — o mesmo território que a Secretária IA ocupa. Ainda sem preço público, mas é o primeiro sinal
  de que o "atendimento por IA no WhatsApp" está deixando de ser exclusividade de players
  dedicados e virando checkbox de EMR estabelecido.
- **O próprio nicho de "secretária IA por WhatsApp" comoditizou horizontalmente** (achado 2): de
  2 concorrentes conhecidos (fazer.ai no Gumroad, semana baseline) para pelo menos 6 players
  dedicados mapeados agora — o produto virou categoria, não mais diferencial único.
  Diferenciação por feature (cobrança Pix antes de confirmar, handoff humano) importa mais do que
  nunca.
- **Meta/n8n/Evolution API**: sem novidade de comoditização nativa nesta janela (achado 3 é
  fricção operacional, não ameaça competitiva — repete o quadro de 17/07).

## Posicionamento — recomendações

1. **R$ 19,90/mês + piloto grátis 7 dias do Prontuário IA continuam defensáveis.** Nenhum achado
   desta rodada muda esse cálculo — manter.

2. **Mensalidade B2B da Secretária IA — primeira vez com âncoras reais de concorrentes que vendem
   a mesma coisa.** Sugestão refinada: **R$ 247–297/mês por clínica**, entre o piso promocional da
   Syntia (R$ 97, que lê como isca de entrada de um player menor, não uma referência de mercado
   madura) e o teto do Secretar.AI (R$ 300–900, mas para uma plataforma completa de
   marketing/CRM que a Secretária IA não é). Justificar o preço pela feature que nenhum dos dois
   anuncia explicitamente: **cobrança de Pix antes de confirmar o horário**. Não entrar em guerra
   de preço com a Syntia — a diferenciação é por escopo, não por ser mais barato.

3. **Nova prioridade: mystery-shop o preço do módulo de assistente virtual da Amplimed** (achado
   1) antes de fechar a mensalidade B2B — se o preço desse add-on for baixo, ele vira a objeção
   nº 1 nas conversas comerciais com clínicas que já usam EMR tradicional. Em paralelo, o item
   pendente de 17/07 continua aberto: **auditar a versão do Evolution API em produção** — a issue
   #2534 (achado 3) segue sem solução do lado do projeto, então a decisão de travar/ativar
   licença continua 100% por conta do Cássio.

## Nota metodológica

Firecrawl operou bem nesta rodada para a maioria das páginas — mas **Ninsáude, Feegow, Shosp,
Simples Dental e Dr. Agenda devolveram 404 nas URLs de preço testadas** (páginas provavelmente
mudaram de endereço); preços desses cinco seguem **não confirmados por leitura primária** nesta
rodada (Feegow e Shosp têm páginas `/precos-e-planos` e `/precos` que apareceram em busca mas não
foram raspadas a tempo — revisitar na próxima rodada). Doctoralia devolveu 404 na URL testada.
CFM 2.454/2026 (prazo 26/08/2026) e a cobrança do WhatsApp Business API (token a partir de
01/08, por resposta a partir de 01/10) foram reconfirmados mas **sem mudança** em relação aos
relatórios anteriores — por isso não entraram como achados novos.

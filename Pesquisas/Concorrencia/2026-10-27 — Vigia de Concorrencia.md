---
title: Vigia de Concorrência — 2026-10-27
date: 2026-10-27
area: Concorrencia
tags: [concorrencia, mercado]
source: routine
---

## TL;DR

- Achamos um scribe novo em pt-BR, a Dora Health: tem plano grátis de 10 consultas/mês sem cartão e Premium a R$ 79/mês. Ela atende de saída nutrição, psicologia, odontologia e fisioterapia.
- A Tolki (MG) vende agentes de IA no WhatsApp para reativar pacientes. Diz que corta o custo do disparo de R$ 0,34 para R$ 0,035 ao enquadrar a mensagem como utilidade.
- Fora isso, nada mudou desde 2026-10-26. O TRF1 ainda não decidiu sobre a CFM 2.454.

> Comparado com o relatório de **2026-10-26**. **Varredura completa:** não. Hoje é terça, e a última completa foi em 26/10, há 1 dia. Só reabri a página de quem apareceu no noticiário.
> Preço do Calima conferido no repo: o `site/index.html` mostra R$ 49,90; `VENDAVEIS = ['staff']`; `PLANO_STAFF_CENTS` e `CONSULTA_AVULSA_CENTS` têm default 4990. O `CONSULTA_SEXTA_CENTS` segue dormente, como já estava.

## Achados

1. **Dora Health: scribe em pt-BR que ainda não estava nos relatórios.** A IA ouve a consulta e entrega o prontuário estruturado. A página lista mais de 30 áreas, entre elas psicologia, nutrição, odontologia e fisioterapia. Plano gratuito de **R$ 0 com 10 consultas/mês, sem cartão**, e **Dora Premium a R$ 79/mês** com 2.000 minutos de consulta. O blog dela foi indexado nesta semana, com o post "Gravar consulta médica é permitido?".
   - Fonte: [dorahealth.com.br](https://dorahealth.com.br/), lido em 27/10/2026 (maxAge 0).
   - **E daí pro Calima:** mais um free tier igual ao do Voa (10 consultas/mês). A Dora é só scribe, e o pago dela custa 58% acima dos R$ 49,90 do Calima, que têm prontuários ilimitados. O dado que mais pesa é outro: a Dora já se vende para nutrição e fisioterapia, então essas profissões deixam de estar "sem scribe".

2. **Tolki, healthtech mineira, vende agentes de IA no WhatsApp para reativar pacientes antigos de clínicas médicas e odontológicas.** Ela diz que estrutura as mensagens na API oficial como **utilidade, não marketing**, e que assim cada disparo cai de **R$ 0,34 para R$ 0,035**. A empresa declara 52 mil pacientes captados e R$ 8 mi de economia em 12 meses. Não divulga preço; diz só que é "menor do que o salário de um funcionário".
   - Fonte: [Jornal de Barueri, 26/10/2026](https://jornaldebarueri.com.br/tecnologia/tolki-capta-52-mil-pacientes-e-poupa-r-8-milhoes-a-clinicas). É conteúdo patrocinado, com números da própria empresa.
   - **E daí pro Calima:** a função "Retorno/reativação" do add-on da secretária depende de os templates serem aprovados como utilidade, senão o custo por mensagem fica 10 vezes maior. Vale conferir a categoria dos templates na hora de medir o custo do piloto.

3. **Avie: secretária IA no WhatsApp a R$ 1.350/mês, para até 1.000 pacientes/mês e com mensagens ilimitadas, mais R$ 2.700 de implantação.** É produto para clínica, não por profissional.
   - Fonte: [avie.me](https://avie.me/), lido em 27/10/2026.
   - **E daí pro Calima:** fica no topo da faixa e não pressiona os R$ 99,90. Mostra que o mercado cobra implantação à parte.

4. **Recepta IA: secretária no WhatsApp oficial para consultório**, com agenda no Google Calendar, lembretes 24h e 2h antes e transbordo para humano. A política de privacidade é de 24/10/2026. O preço não é público e o "Acessar plataforma" aponta para um IP solto, o que indica produto bem no começo.
   - Fonte: [recepta-ia.github.io](https://recepta-ia.github.io/), lido em 27/10/2026.
   - **E daí pro Calima:** a mesma proposta do add-on, feita por gente pequena. Não ameaça agora; só mostra que entrar nesse mercado é barato.

5. **O Voa Health divulga com influenciador um cupom de R$ 400 de desconto mais 7 dias grátis sem cartão para assinante novo** (YouTube, 27/10). A tabela não mudou.
   - **E daí pro Calima:** o Voa repete o "7 dias sem cartão" do Calima. Só os 7 dias grátis deixaram de diferenciar o Calima; o "ilimitado por R$ 49,90" ainda diferencia.

**Regulação sem mudança:**
- **CFM 2.454/2026:** o TRF1 ainda não decidiu o pedido da CNSaúde, da FENAESS e do SBH. Nas buscas, nenhuma notícia é posterior à de 19/10. Um artigo novo na Migalhas defende avaliar a "competência clínica" da IA generativa, além da RDC 657 da Anvisa. É só opinião.
- **CFP, CFN, CFO, COFFITO, COFEN, ANPD e Anvisa:** nenhuma norma nova. O COFFITO recebe o Simpósio FCFAS sobre saúde digital e IA em 18 e 19/11; vale acompanhar.
- **WhatsApp Cloud API:** a cobrança das mensagens de serviço, com 1.000 grátis por número por mês, vale desde 01/10. Já estava nos relatórios de setembro e outubro, e não houve mudança nova.
- **Apple:** sem mudança.

## Pressão de preço

- **Scribe abaixo de R$ 49,90:** entra a Dora Health com 10 consultas grátis/mês. Já estavam o Voa Free (10/mês) e a Telepatia (US$ 0). O pago mais barato em pt-BR continua sendo o Dora Premium, a R$ 79. Ninguém vende scribe ilimitado abaixo de R$ 49,90.
- **Tudo-em-um:** sem mudança.
- **Teleconsulta avulsa:** sem mudança. A THM Saúde segue empatada em R$ 49,90.
- **Secretária por profissional abaixo de R$ 99,90:** sem mudança. A Avie (R$ 1.350) e a Recepta (preço não público) não mexem no piso.

## Comoditização

- **Nenhum ERP novo embutiu scribe hoje.**
- **Meta, WhatsApp e n8n:** nada novo de graça. O jeito da Tolki de classificar a mensagem como utilidade é técnica de uso, não recurso da Meta.
- **Big tech:** nenhum ditado clínico em pt-BR.

## Posicionamento

- **(a) Plano único de R$ 49,90:** a recomendação não muda.
- **(b) Add-on da secretária:** a recomendação não muda. Uma observação: o custo medido no piloto deve separar a mensagem de utilidade da de marketing (achado 2).
- **(c) Profissão menos servida: ajuste.** A Dora Health já anuncia nutrição, fisioterapia e psicologia num scribe genérico. Mesmo assim, nenhum scribe é feito para a rotina dessas profissões, e os ERPs delas (Dietbox, WebDiet, ZenFisio) seguem sem voz. Então a nutrição continua sendo a melhor frente, mas a janela ficou menor.

## O que foi checado em 27/10/2026

- **Notícias:** Firecrawl (busca de 24 h e de 7 dias) e WebSearch.
  - Scribe e prontuário com IA.
  - Secretária IA no WhatsApp.
  - CFM 2.454 e TRF1.
  - Conselhos (CFP, CFN, CFO, COFFITO, COFEN), ANPD e Anvisa.
  - Preço da WhatsApp API.
  - Menções a Voa, Telepatia, Doctoralia, iClinic, Feegow, Simples Dental e clina.ai.
- **Páginas relidas:** dorahealth.com.br, avie.me, recepta-ia.github.io e a matéria da Tolki.
- **Lacunas:**
  - O agente web (MCP `agente-web`) não estava disponível nesta sessão de nuvem, então a rotina usou a reserva: Firecrawl e WebSearch.
  - A busca de notícias de 24 h do Firecrawl veio vazia.
  - O Instagram não pode ser lido pelo Firecrawl; o post sobre o Cliniclic não foi lido.
  - Nenhum número foi estimado.

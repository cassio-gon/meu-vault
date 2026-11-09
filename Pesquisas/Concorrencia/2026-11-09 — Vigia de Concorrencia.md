---
title: Vigia de Concorrência — 2026-11-09
date: 2026-11-09
area: Concorrencia
tags: [concorrencia, mercado]
source: routine
---

## TL;DR

- A Black Friday dos concorrentes começou: Doctoralia (Noa Notes 60% off), Amplimed (até 50% off com a Amélia), PsicoManager (−25%), Dietbox (−55%) e Simples Dental.
- Ninguém vende escriba por voz em pt-BR abaixo de R$ 49,90: o pago mais barato continua a Dora, a R$ 79.
- A Doctoralia trocou a tabela para R$ 420,42/518,42/665,42 "+2% de imposto", que dá na prática o preço antigo.
- A Meta tem uma categoria "Business Agent" (IA dela no WhatsApp) a US$ 0,04–0,05 por mensagem. Isso serve de referência de custo para o add-on.
- As 3 recomendações continuam. O ajuste é uma oferta curta de Black Friday no Calima, e a nutrição continua a profissão menos servida.

> Comparado com o relatório de **2026-11-08**. **Varredura completa:** sim, por ser segunda. A anterior foi em 02/11. Os ~40 alvos foram relidos em 09/11/2026 pelo Firecrawl, com `maxAge: 0`.
> Preço do Calima conferido no repo (`origin/main` `ea957f7`): `site/index.html` mostra R$ 49,90 (7 ocorrências) e "7 dias grátis sem cartão"; `VENDAVEIS = ['staff']`; `PLANO_STAFF_CENTS` e `CONSULTA_AVULSA_CENTS` com default 4990; `TRIAL_DIAS` default 7. O teste é de 10 prontuários por dia desde `0dec14e` (07/11). O Calima não tem plano anual.

## Achados

1. **Começou a Black Friday dos ERPs e das verticais.**
   - **Doctoralia Pro:** "Oferta Especial 2026" no anual em 12x: Starter com Noa R$ 615,44; Plus R$ 591,92 (de R$ 728); VIP R$ 738,92 (de R$ 878); Noa Notes com 60% off. Fonte: [pro.doctoralia.com.br/preco](https://pro.doctoralia.com.br/preco).
   - **Amplimed:** a AmpliBlack dá "até 50% OFF nos planos + Amélia", só em novembro, sem preço final público. A tabela segue em R$ 89 / R$ 139. Fonte: [amplimed.com.br/ampliblack](https://www.amplimed.com.br/ampliblack/).
   - **PsicoManager:** Plus anual a R$ 1.070,90 no Pix (de R$ 1.428, −25%) ou 12x R$ 94, com o cupom BLACKNOVEMBER, de 3 a 30/11, só para clientes novos. Fonte: [psicomanager.com.br/planos](https://psicomanager.com.br/planos).
   - **Dietbox:** a "DB Friday" põe o Premium semestral a 6x R$ 53,90 (de 6x R$ 129,02, −55%). Fonte: [dietbox.me/pt-BR/planos](https://dietbox.me/pt-BR/planos).
   - **Simples Dental:** o −20% por 10 meses passou a valer também no mensal, e o Pro tem −8% no anual com uma caneta de brinde. Fonte: [simplesdental.com/planos-e-precos](https://www.simplesdental.com/planos-e-precos).
   - **Clinicorp:** tem banner da Black November, sem preço. Fonte: [clinicorp.com/planos](https://www.clinicorp.com/planos).
   - Todos lidos em 09/11/2026.
   - **E daí pro Calima:** até 30/11, o médico vai ver "60% off no escriba" da Doctoralia, que ainda assim custa mais de R$ 590/mês. O Calima, a R$ 49,90 sem promoção, continua o mais barato, mas fica sem um gatilho de urgência enquanto todos os outros têm.

2. **Doctoralia: a tabela de base passou a mostrar o imposto à parte.** Os planos aparecem a R$ 420,42 / 518,42 / 665,42 "+2% de imposto"; em 02/11 eram R$ 429 / 529 / 679. Com os 2%, o valor é praticamente o mesmo. O Noa Notes avulso segue a R$ 199. Fonte: [pro.doctoralia.com.br/preco](https://pro.doctoralia.com.br/preco), lido em 09/11/2026.
   - **E daí pro Calima:** não houve corte real de preço. O escriba da Doctoralia continua a ~4x o Calima.

3. **Meta: a categoria "Meta Business Agent" (a IA da própria Meta respondendo no WhatsApp) existe desde 01/07/2026.** É cobrada por complexidade, e a Meta estima US$ 0,04–0,05 por mensagem com IA, contra US$ 0,09–0,10 de uma IA de terceiros somada à tarifa de serviço. O mesmo documento traz outras regras:
   - A mensagem de serviço é cobrada desde 01/10, com franquia de 1.000 grátis por mês por número.
   - A Meta não anunciou mudança de preço para 2027.
   - Quem fatura no Brasil precisa migrar para BRL até 30/06/2027; a partir de 01/07/2027, a Meta para de entregar as mensagens de quem não migrou.
   - Fonte: [developers.facebook.com/docs/whatsapp/pricing](https://developers.facebook.com/docs/whatsapp/pricing), "Updated: Sep 30, 2026", lida em 09/11/2026. A tarifa de marketing do Brasil de novo não foi lida, porque o CSV deu 403.
   - **E daí pro Calima:** é a primeira vez que este vigia registra a tabela da Business Agent. A Meta vende a própria IA no WhatsApp pela metade do custo de terceiros. A secretária do Calima (n8n + Claude Haiku) deve medir o custo por conversa contra esses US$ 0,04–0,05, e a migração da conta para BRL entra na lista com prazo de 30/06/2027.

4. **Voa Health: a página de preços diz que o Free inclui ditado por voz em português** (10 atendimentos por mês, até 30 min por consulta). O Pro (R$ 289–349) traz telemedicina, assinatura VIDaaS e LME do SUS. Os preços não mudaram. Fonte: [voa.health/precos](https://voa.health/precos), lida em 09/11/2026.
   - **E daí pro Calima:** os 10 atendimentos grátis por mês da Voa ficam bem abaixo do teste do Calima (10 por dia durante 7 dias). O argumento "teste mais generoso" segue válido.

5. **Vokkari: assinatura VIDaaS em todos os planos, marcada como "Novidade", e conferência do nome do medicamento no registro da Anvisa até no grátis.** O preço não mudou (R$ 0 com 5 h / R$ 179,99 / R$ 449,99). Fonte: [vokkari.com](https://vokkari.com), lido em 09/11/2026.
   - **E daí pro Calima:** assinatura digital com ICP passou a ser item básico até no escriba grátis (Voa, Vokkari, AgendaCare). Se o Calima ainda não assina receita e atestado com certificado em nuvem, a diferença aparece na comparação.

6. **A Heidi segue sem pt-BR e a Microsoft não lista o Brasil para o Dragon Copilot.** A Heidi Free ("unlimited") não menciona português nem Brasil. O Dragon Copilot lista EUA, CA, UK, IE, FR, DE, AT, BE, NL e CH. Fontes: [heidihealth.com/en-us/pricing](https://www.heidihealth.com/en-us/pricing) e [página do Dragon Copilot](https://www.microsoft.com/en-us/health-solutions/clinical-workflow/dragon-copilot), lidas em 09/11/2026.
   - **E daí pro Calima:** a maior ameaça de preço (escriba grátis e ilimitado de big tech) continua fora do pt-BR.

**Outros (sem efeito no Calima):**
- O iClinic mudou a página de preços para `/precos/`, com 8% off no anual e o mesmo preço.
- A Feegow mudou a página para `/precos-e-planos`, com o mesmo preço.
- O Shosp dá −15% no anual.
- A ZenFisio dá 25% em 3 meses do anual.
- O Escriba Médico tem programa de indicação (R$ 97 de crédito para quem indica e R$ 30 de desconto para o colega indicado) e teste de 7 dias sem cartão.
- A Singulare tem check-in PHQ-9/GAD-7 pelo WhatsApp entre as consultas.
- A Desler mostra um limite de 400 conversas por mês por acesso.
- As notícias de 09/11 não trouxeram lançamento, rodada nem player global novo no Brasil.

## Regulação

- **CFM 2.454/2026:** sem notícia nova. O manifesto das 10 entidades é de 16/09 ([Futuro da Saúde](https://futurodasaude.com.br/norma-do-cfm-sobre-ia-enfrenta-nova-contestacao-de-entidades-de-saude/)), e o recurso no TRF1 segue sem decisão pública. O PL 2.338 (marco da IA) não tem votação marcada na Câmara.
- **Anvisa:** a revisão da RDC 657 (software como dispositivo médico) segue na agenda de 2026–2027, sem texto novo. O SNCR continua com a transição até 03/03/2027.
- **WhatsApp / Meta:** ver o achado 3.
- **CFP, CFN, CFO, COFFITO, COFEN, ANPD, Apple:** nada novo.

## Pressão de preço

- **Escriba abaixo de R$ 49,90:** ninguém pago. Os grátis com limite seguem os mesmos:
  - Voa Free: 10 por mês;
  - Dora: 10 por mês;
  - Vokkari: 5 h;
  - Telepatia: US$ 0;
  - Heidi Free "unlimited", só em inglês.

  O pago mais barato em pt-BR continua a Dora, a R$ 79.
- **Tudo-em-um:** nenhuma promoção da Black Friday põe escriba abaixo de R$ 49,90.
  - Doctoralia com Noa: mais de R$ 590/mês.
  - Amplimed, com até 50% off: o Pro de R$ 139 pode cair para perto de R$ 70, mas a Amélia Transcrição continua sem preço público.
  - SmartDoctor: R$ 99,90, sem mudança.
- **Mais perto dos R$ 49,90:** a Dietbox a R$ 53,90/mês no semestral, mas ela não tem ditado da consulta.
- **Teleconsulta avulsa:** ninguém abaixo de R$ 49,90. A THM empata em R$ 49,90; Dr. Consulta cobra R$ 125 e Einstein R$ 389,90.
- **Secretária por profissional abaixo de R$ 99,90:** a mesma lista de antes.
  - Embutida em outro produto: Sofia grátis (+R$ 49 por função), Dr. Agenda R$ 70, SmartDoctor no plano de R$ 99,90.
  - Avulsa: o piso segue em R$ 147 (AgendaCare).

## Comoditização

- **Escriba embutido no ERP:** nenhum ERP novo. A mudança é de preço: a Doctoralia dá 60% off no Noa Notes e a Amplimed põe a Amélia no pacote da Black.
- **A Meta vende a própria IA no WhatsApp** (Business Agent, achado 3). Não é de graça, mas sai mais barato que um agente de terceiros, e é o primeiro passo para comoditizar a secretária.
- **Big tech:** nenhum ditado clínico em pt-BR. O Dragon Copilot não lista o Brasil, e a Heidi não tem português.

## Posicionamento — recomendações

1. **O plano único de R$ 49,90 com 7 dias grátis sem cartão continua defensável, e o teste de 10 prontuários por dia o deixou mais forte.** Nenhum concorrente, nem com a Black Friday, vende escriba em pt-BR abaixo de R$ 49,90. A ação para as próximas 3 semanas é uma oferta própria até 30/11, para ter um gatilho de urgência no mês em que todos os outros têm. Não baixar a mensalidade. Duas opções:
   - (a) um anual inédito com 2 meses grátis (~R$ 499/ano);
   - (b) o primeiro mês a R$ 29,90.

   Peça para comparar: "escriba + tudo-em-um por R$ 49,90, sem promoção, contra R$ 590 da Doctoralia com 60% off".
2. **Add-on Secretária por médico: manter os R$ 99,90.** O piso avulso continua em R$ 147, e quem fica abaixo só entrega a secretária embutida num ERP. O custo de referência mudou: a IA da própria Meta sai a US$ 0,04–0,05 por mensagem (achado 3). Antes de abrir a venda, medir o custo real por conversa do n8n + Haiku. Se passar disso numa conversa típica de agendamento, rever a margem dos R$ 99,90 ou pôr um teto de conversas por mês (como a Desler, com 400).
3. **A profissão menos servida por escriba em pt-BR continua a nutrição.** Dietbox e WebDiet seguem sem ditado da consulta, e a Dietbox está a R$ 53,90/mês na DB Friday, o que mostra que o nutricionista paga em torno de R$ 50. A situação das outras profissões:
   - Psicologia: tem o PsicoManager e a Singulare.
   - Odontologia: está saturada (voz e secretária no Simples Dental e na Clinicorp).
   - Fisioterapia (ZenFisio) e enfermagem (Vitalia): seguem sem voz e continuam a segunda opção.

## Varredura completa — preços lidos em 09/11/2026

| Alvo | Preço lido | Mudou desde 02/11? |
|---|---|---|
| iClinic (iclinic.com.br/precos/) | R$ 99/129/169/299; anual −8%; WhatsApp a partir de R$ 29,90; 10 teleconsultas R$ 35 | Não (URL nova) |
| Ninsaúde | R$ 199 por profissional | Não |
| Feegow (/precos-e-planos) | R$ 129/199/249 | Não (URL nova) |
| Amplimed | R$ 89 / R$ 139; AmpliBlack até 50% off; Amélia Transcrição não pública | **Promo** |
| Doctoralia Pro | R$ 420,42/518,42/665,42 +2% imposto; Oferta Especial anual 12x R$ 591,92–738,92; Noa Notes R$ 199 (60% off na oferta) | **Sim** |
| Shosp | R$ 0 + ativação R$ 299 / R$ 149 / R$ 229; anual −15% | Não |
| Dr. Agenda | R$ 70 (de R$ 90) | Não |
| clina.ai | Grátis / R$ 249 / a partir de R$ 497 / módulos R$ 39–99 | Não |
| SmartDoctor | R$ 99,90 / R$ 350; 30 dias grátis | Não |
| Simples Dental | R$ 149,90/249,90/349,90; anual −25% (Basic/Plus), Pro −8%; mensal −20% por 10 meses; Secretária IA "< R$ 6/dia" | **Promo ampliada** |
| Clinicorp | R$ 159,90 / R$ 369,90; Black November sem preço | **Promo** |
| Dietbox | Premium semestral 6x R$ 53,90 (DB Friday, −55%); Profissional R$ 72,60 no semestral | **Promo** |
| WebDiet | R$ 49,90 por 3 meses, depois R$ 94,90 · R$ 139,90 | Não |
| PsicoManager | R$ 89; Plus anual R$ 1.070,90 Pix (Black November) | **Promo** |
| ZenFisio | R$ 79/179/439; 25% em 3 meses do anual | Faixa nova |
| Vitalia Pro | R$ 63/119/223 no anual; R$ 149 no mensal | Não |
| Voa Health | Free / Pro R$ 289–349 / Ultra R$ 2.490–2.900 | Não |
| Heidi Health | Free / US$ 110 / sob consulta; sem pt-BR | Não |
| Freed | US$ 39–59 / 59–79 / 104–119 | Não |
| Telepatia AI | US$ 0 de lançamento (US$ 99 riscado) | Não |
| Dora Health | Grátis 10/mês · R$ 79 | Não |
| Vokkari | R$ 0 com 5 h · R$ 179,99 · R$ 449,99 | Não |
| Escriba Médico | R$ 97 / R$ 997 no ano | Não |
| Dr. Assistente | R$ 150 / 250 / 450 | Não |
| Assist4Doc | R$ 197/397/997 | Não |
| Nabla, Abridge, Suki, Dragon Copilot | Não público; nenhum no Brasil | — |
| Secretar.AI | R$ 360/720/1.080 | Não |
| Singulare | R$ 197/397 + humano a partir de R$ 297 | Não |
| AgendaCare | R$ 0 / 79,90 / 147 / 297 / 497 / 797 / 1.297 | Não |
| Desler AI | R$ 159 / 198 / 298; acesso extra R$ 79–150 | Não |
| Sofia (clina.ai) | Grátis; Triagem e Acompanhamento R$ 49 cada | Não |
| THM Saúde | Avulsa R$ 49,90 · plano R$ 79,90 | Não |
| Einstein Conecta | Avulsa R$ 389,90 · R$ 129,90 / R$ 99,90 | Não |
| Dr. Consulta | Clínica geral online R$ 125; psiquiatria online R$ 190 | Não |
| Conexa | 12x R$ 26,90 / 32,90 / 89,90; avulsa não pública | Não |
| Doctoralia (teleconsulta) | Não público | — |
| Meta WhatsApp (Brasil) | Utility e authentication US$ 0,0068; Business Agent US$ 0,04–0,05; marketing não lido | Primeira leitura da Business Agent |

**Lacunas:**
- O agente web (MCP `agente-web`) não estava disponível nesta sessão de nuvem, então a rotina usou a reserva: Firecrawl e WebSearch.
- A tarifa de marketing do WhatsApp para o Brasil não foi lida (o CSV da Meta deu 403).
- A aba mensal da Dietbox não carregou, então os R$ 91,90 / 133,90 não foram reconfirmados.
- Nenhum número foi estimado.

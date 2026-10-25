---
title: Vigia de Concorrência — 2026-10-25
date: 2026-10-25
area: Concorrencia
tags: [concorrencia, mercado]
source: routine
---

## TL;DR

- Telepatia AI zerou o plano individual ("US$ 0, preço de lançamento", antes US$ 99). É um scribe grátis que já atua no Brasil, a maior pressão de preço sobre os R$ 49,90.
- Voa Health: Free com 10 atendimentos/mês e Pro a R$ 349/mês. O Ultra já junta scribe e secretária no WhatsApp.
- Correção: os R$ 229,08 do Simples Dental são o plano Plus anual, não a Secretária IA (que é "menos de R$ 6/dia").
- O Dr. Agenda inclui secretária IA 24x7 no plano de R$ 70/médico, abaixo dos R$ 99,90 do add-on.
- Nutrição e enfermagem seguem sem scribe por voz em pt-BR; a psicologia já tem (PsicoManager, R$ 89).

> Comparado com o relatório de **2026-10-23**. Este é o **primeiro relatório no formato novo** (Calima com plano único de R$ 49,90, teleconsulta avulsa a R$ 49,90 e add-on de Secretária por médico em estudo a R$ 99,90). Os anteriores ficam como histórico de preço dos concorrentes.
> **Varredura completa:** sim. A lista de alvos ficou maior e nenhuma varredura completa nesse formato tinha sido registrada. Preços lidos em 25/10/2026 nas páginas oficiais, pelo Firecrawl.
> Preço do Calima conferido no repo: `site/index.html` mostra R$ 49,90/mês com 7 dias grátis sem cartão; `VENDAVEIS = ['staff']`; o default de `PLANO_STAFF_CENTS` e de `CONSULTA_AVULSA_CENTS` é 4990.

## Achados

1. **Telepatia AI: conta individual a US$ 0 como "launch price" (antes US$ 99/mês).** A empresa atua no Brasil, com depoimentos de médicos com CRM e Instagram @telepatia_br, e captou US$ 33 mi com a a16z em jun/2026. Em 21/10 anunciou Lara Paiva como VP de Estratégia em Saúde e Expansão.
   - Fontes: [telepatia.ai/en/for-doctors](https://telepatia.ai/en/for-doctors) (25/10/2026) e [saudedigitalnews](https://saudedigitalnews.com.br/21/10/2026/telepatia-anuncia-lara-paiva-como-vp-de-estrategia-em-saude-e-expansao/) (21/10/2026).
   - **E daí pro Calima:** um scribe grátis e bem financiado mira o mesmo médico, então o argumento contra ele tem de ser o que o Calima tem e ele não: plantão, receita/atestado, teleconsulta, portal do paciente e LGPD no aparelho. Preço não é esse argumento.

2. **Voa Health tem preço público.** Free com 10 atendimentos/mês e 30 min por consulta. Pro a R$ 349/mês no mensal ou R$ 289/mês no anual (promoção "Mês do Médico" até 31/10: R$ 2.799/ano no Pix). Ultra a R$ 2.490–2.900/mês por organização, com recepção e agenda no WhatsApp. Em outubro, conta nova ganha 7 dias de Pro sem cartão.
   - Fonte: [voa.health/precos](https://voa.health/precos) (25/10/2026).
   - **E daí pro Calima:** os R$ 49,90 ilimitados custam 1/7 do Voa Pro; vale citar o "ilimitado" contra o limite de 10/mês do free deles.

3. **Correção do relatório de 23/10 sobre o Simples Dental:** os R$ 229,08 são o **plano Plus no anual** (o mensal é R$ 249,90), não a Secretária IA. A Secretária IA segue em pré-lançamento, paga à parte, anunciada como "menos de R$ 6/dia" (menos de ~R$ 180/mês), sem preço exato. Há ainda um "Assistente IA por voz" pago à parte, também sem preço.
   - Fonte: [simplesdental.com/planos-e-precos](https://www.simplesdental.com/planos-e-precos) (25/10/2026).
   - **E daí pro Calima:** a âncora de R$ 229 para secretária no WhatsApp cai; o teto de referência real é menor.

4. **O Dr. Agenda inclui "secretária virtual com IA 24x7" no Padrão Flexível de R$ 70/médico** (promoção, de R$ 90). A AgendaCare cobra R$ 147/mês para 1 a 3 profissionais com agente de IA (o plano de R$ 79,90 para 1 profissional não traz IA), mais R$ 2,20 por conversa acima da franquia.
   - Fontes: [dragenda.com.br/planos](https://dragenda.com.br/planos) e [agendacare.com.br](https://agendacare.com.br) (25/10/2026).
   - **E daí pro Calima:** a secretária IA já vem embutida em agenda barata, e o add-on a R$ 99,90 tem de se justificar pela integração com prontuário, sala e Asaas, não pelo preço.

5. **O clina.ai mudou a tabela: Pro R$ 219/mês e Clínica R$ 397/mês** (antes "Completo a partir de R$ 199"). A base grátis com página, agenda e Sofia no WhatsApp continua. O módulo Scribe isolado não tem preço público.
   - Fonte: [clina.ai/perguntas-frequentes](https://clina.ai/perguntas-frequentes) (25/10/2026).
   - **E daí pro Calima:** o pacote tudo-em-um com scribe ficou mais caro; o Calima com o add-on (R$ 49,90 + R$ 99,90 = R$ 149,80) fica abaixo do Pro deles.

6. **O Assist4Doc deixou de ser scribe e virou secretária IA no WhatsApp e no Instagram ("MedIA")**: Starter R$ 197, Pro R$ 397 e Enterprise R$ 997 por mês, com 10 dias grátis. A tabela antiga (Gratuito/R$ 79/R$ 147/R$ 247) sumiu.
   - Fonte: [assist4doc.com.br](https://assist4doc.com.br) (25/10/2026).
   - **E daí pro Calima:** sai um scribe barato em pt-BR e entra mais um sinal de que o dinheiro está na secretária no WhatsApp.

7. **Apple: as App Review Guidelines mudaram em 16/10, com a nova regra 2.5.19 contra recurso oculto ou dormente ("bait-and-switch").** Nada mudou em 1.4.1 nem em 5.1.x.
   - Fonte: [developer.apple.com/news](https://developer.apple.com/news/) (16/10/2026).
   - **E daí pro Calima:** reforça a regra do repo: liberar escores e alertas no iOS só com versão nova enviada à Apple, nunca tirando a trava `isNativo()` no servidor.

8. **CFM 2.454/2026: o pedido de suspensão está concluso no TRF1 desde 07/10** (desembargador Pedro Braga Filho), sem decisão até 19/10. A 21ª Vara/DF tinha extinguido a ação em 25/09, sem julgar o mérito. A norma está em vigor. A ação é da CNSaúde, da FENAESS e da SBH (o "dez entidades" dos relatórios antigos não se confirmou).
   - Fonte: [O Globo/Dino](https://oglobo.globo.com/patrocinado/dino/noticia/2026/10/19/trf1-analisa-pedido-de-suspensao-da-regra-de-ia-na-medicina-1.ghtml) (19/10/2026).
   - **E daí pro Calima:** nada a fazer agora; se o TRF1 suspender a norma, o selo "conforme 2.454" perde peso.

**Regulação sem mudança que afete o Calima:**
- Conselhos (CFP, CFN, CFO, COFFITO, COFEN): nada novo desde 15/10.
- Anvisa: sem minuta da revisão da RDC 657. A CP 1.427/2026 sobre sandbox abriu em 13/10.
- ANPD: abriu em 15/10 a consulta pública de dosimetria de sanções (até 30/11; audiência em 29/10 às 14h30), que não é específica de saúde. [gov.br/anpd](https://www.gov.br/anpd/pt-br/assuntos/noticias/anpd-consulta-publica-dosimetria-e-sancoes)
- WhatsApp Cloud API: o Brasil não teve a tarifa alterada em 01/10 (utility/authentication a US$ 0,0068, segundo a página da Meta). A página "AI Providers" mudou em 15/10 só para incluir a Türkiye. [developers.facebook.com](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing)

## Pressão de preço

- **Scribe abaixo de R$ 49,90:** dois casos.
  - **Telepatia AI** a US$ 0 (preço de lançamento, sem prazo dito).
  - **Voa Free** com 10 atendimentos/mês.
  - Entre os pagos em pt-BR, ninguém fica abaixo: PsicoManager R$ 89 (psicologia), Amplimed Pro R$ 139 (com Amélia Copilot), Feegow VIP R$ 249 (Noa Notes), Doctoralia + Noa Notes R$ 199 de add-on, Voa Pro R$ 289–349.
- **Tudo-em-um:** nenhum pacote com scribe fica abaixo de R$ 49,90. As agendas baratas não trazem scribe confirmado: Dr. Agenda R$ 70 (a página fala em "prontuário… IA" sem detalhe), Shosp Free + ativação de R$ 299, Ninsaúde R$ 199. Em nutrição, Dietbox e WebDiet custam R$ 49,90 só nos 3 primeiros meses (depois R$ 91,90 e R$ 94,90), sem voz.
- **Teleconsulta avulsa ao paciente:** nenhum preço público abaixo de R$ 49,90.
  - Dr. Consulta: "depende da especialidade"; a imprensa (dez/2025) fala em R$ 59–109.
  - Conexa: vendida só como benefício de empresa ou operadora.
  - Einstein Conecta: preço não público.
  - Doctoralia: o profissional define o preço.
- **Secretária no WhatsApp abaixo de R$ 99,90 por profissional:** sim, quando vem embutida.
  - clina.ai Sofia: grátis.
  - Dr. Agenda: incluída nos R$ 70.
  - AgendaCare: R$ 147 divididos por 2 ou 3 profissionais (R$ 49–74 cada).
  - Avulsa para quem atende sozinho, ninguém cobra menos: AgendaCare R$ 147, Singulare R$ 197, Assist4Doc R$ 197, Desler IA Básico R$ 198, Secretar.AI R$ 360.
  - Simples Dental: menos de ~R$ 180, ainda em pré-lançamento.

## Comoditização

- **Scribe embutido em ERP:**
  - Feegow traz "digitação por voz" em todos os planos.
  - Amplimed põe o Amélia Copilot no Pro (R$ 139) e cobra a Amélia Transcrição à parte (preço não público).
  - PsicoManager tem transcrição e resumo de sessão nativos.
  - Simples Dental tem "Assistente IA por voz" pago à parte.
- **Scribe + WhatsApp no mesmo produto:** Voa Ultra e clina.ai. É a mesma soma que o Calima faz com o add-on.
- **Meta, WhatsApp e n8n:** nada novo de graça.
- **Big tech:** nenhum ditado clínico em pt-BR. O Dragon Copilot não é vendido no Brasil, e os modelos médicos de voz do Google são só en-US.

## Posicionamento — recomendações

1. **Manter R$ 49,90 com 7 dias grátis sem cartão: segue defensável.**
   - Mais barato que todo scribe pago em pt-BR e ilimitado contra os 10/mês do Voa Free.
   - O risco é o grátis (Telepatia).
   - Resposta sugerida, sem mexer no preço: deixar claro na landing o que um scribe sozinho não entrega (receita/atestado, teleconsulta com link fixo, plantão, portal do paciente, nome cifrado no aparelho).
   - Rever se a Telepatia mantiver o US$ 0 depois do lançamento.
2. **Add-on Secretária por médico: R$ 99,90 é um bom número; não passar de R$ 147.**
   - R$ 147 é o piso avulso para quem atende sozinho (AgendaCare); Singulare e Assist4Doc cobram R$ 197.
   - Com agenda embutida, o mercado chega a R$ 0–70, então vender como "secretária ligada ao seu prontuário, sala e Pix" e nunca como secretária solta.
   - Se o custo medido no piloto ficar acima de ~R$ 60/mês por médico, R$ 129,90 ainda cabe abaixo de todos.
3. **Profissão menos servida: nutrição** (e, em seguida, enfermagem).
   - Dietbox e WebDiet, os dois líderes, não têm voz.
   - Os R$ 49,90 do Calima batem com o preço de entrada deles, que depois sobe para R$ 91–95.
   - Enfermagem (Vitalia Pro) e fisioterapia (ZenFisio) também não têm scribe; só o Kynesia, segundo terceiros.
   - A psicologia já é atendida pelo PsicoManager (R$ 89–119, IA ilimitada no Plus).

## Varredura completa — preços lidos em 25/10/2026

| Alvo | Preço lido | Mudou? |
|---|---|---|
| iClinic | R$ 99/129/169/299 (sem scribe na página; add-on de WhatsApp a partir de R$ 29,90) | Não |
| Ninsaúde Apolo | Individual R$ 199 | Primeira leitura |
| Feegow | R$ 129/199/249 (Noa Notes no VIP) | Não |
| Amplimed | Lite R$ 89 · Pro R$ 139; Amélia Transcrição não pública | Pro é dado novo |
| Doctoralia Pro | R$ 429/529/679 + Noa Notes R$ 199 | Não |
| Shosp | R$ 0 + ativação R$ 299 / R$ 149 / R$ 229 | Não |
| Dr. Agenda | R$ 70 promo (de R$ 90) + R$ 40 por agenda de exames; secretária IA incluída | Não (IA incluída é dado novo) |
| clina.ai | Grátis / Pro R$ 219 / Clínica R$ 397 | **Sim** |
| Simples Dental | R$ 149,90/249,90/349,90; Secretária menos de R$ 6/dia | Correção |
| Clinicorp | Standard R$ 159,90 · Premium R$ 369,90; combos de IA sob consulta (o FAQ ainda diz R$ 149,90) | Não |
| Dietbox | R$ 49,90 por 3 meses, depois R$ 91,90 · Premium R$ 133,90 | Primeira leitura |
| WebDiet | R$ 49,90 por 3 meses, depois R$ 94,90 · Black R$ 139,90 | Primeira leitura |
| PsicoManager | Pró R$ 89 · Plus R$ 119 (transcrição por IA) | Primeira leitura |
| ZenFisio | R$ 79/179/439 (sem transcrição) | Primeira leitura |
| Vitalia Pro (enfermagem) | R$ 63/119/223 no anual (a página se contradiz) | Primeira leitura |
| Voa Health | Free / Pro R$ 289–349 / Ultra R$ 2.490–2.900 | Primeira leitura |
| Heidi Health | Free / Clinician US$ 110 (anual) / Teams sob consulta | Não |
| Freed | US$ 39 / 59–79 / 104–119 (EUA) | Primeira leitura |
| Telepatia AI | US$ 0 de lançamento (antes US$ 99) | **Novo** |
| Nabla, Abridge, Suki, Dragon Copilot | Não público | — |
| Assist4Doc | R$ 197/397/997 (virou secretária) | **Sim** |
| Secretar.AI | R$ 360/720/1.080 | Não |
| Singulare | R$ 197/397 + atendimento humano R$ 297 | Não |
| AgendaCare | R$ 79,90 sem IA; R$ 147 (1 a 3 profissionais) com IA | Primeira leitura |
| Desler AI | R$ 159 / 198 / 298 | Primeira leitura |
| Dr. Consulta | Não público ("depende da especialidade") | — |
| Conexa, Einstein Conecta | Não público | — |

URLs: iclinic.com.br/precos/, apolo.ninsaude.com/service/comprar/, feegowclinic.com.br/precos-e-planos, amplimed.com.br/consultorio-planos/, pro.doctoralia.com.br/preco, shosp.com.br/precos, dragenda.com.br/planos, clina.ai/perguntas-frequentes, simplesdental.com/planos-e-precos, clinicorp.com/planos, pay.dietbox.me, webdiet.com.br/site/, psicomanager.com.br/planos, zenfisio.com/planos-precos, vitalia.enf.br, voa.health/precos, heidihealth.com/en-us/pricing, getfreed.ai/pricing, telepatia.ai/en/for-doctors, assist4doc.com.br, secretar.ai/#precos, singulare.org, agendacare.com.br, desler.com.br/planos-precos, drconsulta.com/telemedicina.

**Lacunas:**
- O Einstein Conecta não carregou.
- Ainda sem preço público: Amélia Transcrição, Secretária IA do Simples Dental, módulo Scribe do clina.ai e combos da Clinicorp.
- O Firecrawl bateu no limite por minuto, mas todos os alvos foram lidos.
- Nenhum número foi estimado.

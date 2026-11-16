---
title: Vigia de Concorrência — 2026-11-16
date: 2026-11-16
area: Concorrencia
tags: [concorrencia, mercado]
source: routine
aviso: enviado
---

## TL;DR

- A **MEDC** cobra o escriba à parte, por R$ 99 nos 2 primeiros meses e R$ 199 depois, em cima de um plano de R$ 99,90 a R$ 229,90. A secretária Aiva sai por R$ 199 no 1º mês e R$ 399 depois.
- O **Ordexa** cortou a cota de IA de um dia para o outro. O plano de R$ 39,90 caiu de 50 ações por dia para **100 por semana**, e o grátis ficou com só 30 ações de bônus. O plano grátis até 50 pacientes deixou de ser um escriba grátis de verdade.
- A **Darwin Saúde** cobra R$ 197 pelo plano com escriba (R$ 80 a mais que o Pro), e o **SimDoctor**, R$ 49 mais R$ 129,90 pela IA.
- Conclusão da varredura completa: quem tem escriba ilimitado cobra a partir de R$ 97 (Escriba Médico). Os R$ 49,90 seguem defensáveis, e a enfermagem é a profissão menos servida.

> Comparado com o relatório de **2026-11-15**. **Varredura completa:** sim, por ser segunda. A anterior foi em 09/11. Foram relidos cerca de 40 alvos em 16/11/2026.
> Calima conferido no repo (`origin/main` `6e0ef3a`): o `site/index.html` segue com R$ 49,90 (7 ocorrências), `VENDAVEIS` continua `['staff']`, `PLANO_STAFF_CENTS` e `CONSULTA_AVULSA_CENTS` têm default 4990 e `TRIAL_DIAS`, 7. Os commits novos são do visual iOS. Nenhum preço mudou.

## Achados

1. **MEDC: escriba e secretária vendidos como add-on, com preço de lançamento.** Os planos custam por médico:

   | Plano | Anual | Mensal | Teleconsulta |
   |---|---|---|---|
   | Essencial | R$ 99,90/mês | R$ 159,90/mês | até 10 por mês |
   | Profissional | R$ 169,90/mês | R$ 229,90/mês | ilimitada |

   Os add-ons:
   - **Transcrição com IA:** R$ 99 nos 2 primeiros meses, depois R$ 199 por médico por mês.
   - **Aiva**, a secretária no WhatsApp: a partir de R$ 199 no 1º mês, depois R$ 399 (faixa de até 100 pacientes atendidos). Não está disponível no Essencial.

   Há 15 dias grátis sem cartão. A própria página diz que "plano com módulos de IA no padrão do mercado custa entre R$ 250 e R$ 400 por médico". Fonte: [medc.com.br/planos](https://www.medc.com.br/planos/) e [medc.com.br/aiva](https://www.medc.com.br/aiva/), lidas em 16/11/2026. É a primeira vez que a MEDC aparece neste vigia.
   ![MEDC, planos](https://agente.cassiogon.tech/prints/d54337faf66b3f2e20a2998616f96575.jpg)
   - **E daí pro Calima:** pela conta da MEDC, prontuário com escriba sai por no mínimo R$ 199/mês, 4x os R$ 49,90 do Calima com escriba incluído. Dá para citar a frase deles ("R$ 250 a R$ 400 por médico") na comparação.

2. **Ordexa apertou a cota de IA no dia seguinte à primeira leitura.**
   - **Plano Consultório (R$ 39,90):** em 15/11 tinha "50 ações de IA por dia"; hoje tem **"100 ações de IA por semana"**.
   - **Plano Clínica:** passou pela mesma troca.
   - **Plano grátis:** "30 ações de IA por mês" virou "30 ações de IA de bônus", uma vez só.

   O preço não mudou (R$ 0 / R$ 39,90 / R$ 69,90). Fonte: [ordexa.com.br](https://ordexa.com.br/), lida em 16/11/2026.
   - **E daí pro Calima:** a ameaça de ontem ficou menor. Com 100 ações por semana, quem atende 25 por dia estoura a cota, e o grátis só dá para experimentar. O Calima pode dizer **"prontuários ilimitados"** contra quem cobra por cota (Ordexa, Voa, Dora, Datapronto).

3. **Darwin Saúde: escriba só no plano Pro + IA, a R$ 197/mês.** O Pro sai por R$ 117/mês, e o Pro + IA, por R$ 197, sem fidelidade. A IA transcreve a consulta (com o consentimento do paciente), monta a anamnese e prepara rascunhos de atestado, prescrição, CID e pedido de exames, com assinatura ICP-Brasil. O teste é de 7 dias. Fonte: [darwinsaude.com.br](https://darwinsaude.com.br/) e [/transcricao-de-consulta-com-ia](https://darwinsaude.com.br/transcricao-de-consulta-com-ia/), com página publicada há cerca de 5 dias e lida em 16/11/2026. É a primeira vez que a Darwin aparece neste vigia.
   - **E daí pro Calima:** é mais um ERP que cobra cerca de R$ 80 pelo escriba, mais do que o Calima inteiro.

4. **SimDoctor: o plano é barato, mas a IA custa R$ 129,90 à parte.** Os planos Pro, Pro+ e Premium custam R$ 49, R$ 69 e R$ 89 por mês (R$ 539, R$ 759 e R$ 979 por ano). O Doctor Assistent, que transcreve um áudio gravado sobre o paciente e o anexa ao prontuário, sai por **R$ 129,90 por profissional**. Fonte: [simdoctor.com.br/planos](https://www.simdoctor.com.br/planos), lida em 16/11/2026.
   - **E daí pro Calima:** o "a partir de R$ 49" do SimDoctor vai aparecer nas comparações com o mesmo preço do Calima, mas com IA o total chega a R$ 178,90.

5. **WebDiet entrou na Black Friday, ainda sem escriba.** O Premium sai por R$ 57,90/mês no semestral (6x), e depois por R$ 94,90. O Black sai por R$ 83,90/mês. Em 09/11, o Premium custava R$ 49,90 nos 3 primeiros meses. A Dietbox mantém o Premium semestral por 6x R$ 53,90 e anuncia uma "Anamnese por IA" como **"em breve"**. Fontes: [webdiet.com.br](https://webdiet.com.br/) e [dietbox.me/pt-BR/planos](https://dietbox.me/pt-BR/planos), lidas em 16/11/2026.
   - **E daí pro Calima:** a Dietbox, o maior software da nutrição, avisou que vai ter IA na anamnese. A janela do Calima na nutrição está se fechando.

**Sem efeito no Calima:**
- O Heidi Free passou de "unlimited" para "uso semanal limitado". Continua sem pt-BR ([heidihealth.com](https://www.heidihealth.com/en-us/pricing)).
- O grátis da Vokkari mostra o limite de 10 pacientes, além das 5 h de gravação.
- A Clinicorp mostra um preço trimestral: R$ 127,19 no Standard e R$ 330 no Premium.
- A teleconsulta do iClinic passou de R$ 35 para R$ 34,90 (pacote de 10).
- O Simples Dental segue com a promoção da Black: 20% off no mensal por 10 meses.
- A Syntia segue a R$ 247, e a Desler, a R$ 159/198/298.
- O Google lançou o Gemini for Healthcare (já registrado em 12/11).
- Uma IA de Itapecerica (MG) que confirma consultas do SUS pelo WhatsApp ganhou um prêmio da Meta ([G1, 13/11](https://g1.globo.com/mg/centro-oeste/noticia/2026/11/13/ia-criada-em-cidade-de-mg-para-confirmar-consultas-do-sus-pelo-whatsapp-vence-premio-da-meta.ghtml)).

## Regulação

- **CFM 2.454/2026:** só conteúdo de blog, sem fato novo.
- **WhatsApp/Meta:** a ManyContacts publicou em 15/11 a tarifa do Brasil, de **€ 0,0518 por mensagem de marketing** e € 0,0056 por mensagem de utilidade ou serviço ([manycontacts.com](https://www.manycontacts.com/en/whatsapp-api-pricing-brazil/)). É a primeira leitura da tarifa de marketing neste vigia, mas a fonte não é da Meta: o CSV oficial segue sem leitura.
- **Anvisa:** só um lote rotineiro de deferimentos. A revisão da RDC 657 continua sem texto.
- **ANPD, CFP, CFN, CFO, COFFITO, COFEN e Apple:** nada novo.

## Pressão de preço

- **Escriba abaixo de R$ 49,90:** só o Ordexa (R$ 39,90), e agora com teto de 100 ações por semana. Os grátis com limite são estes:

  | Produto | Limite do grátis |
  |---|---|
  | Voa | 10 atendimentos por mês |
  | Dora | 10 por mês |
  | Vokkari | 5 h e 10 pacientes |
  | Ordexa | 30 ações, uma vez só |
  | Amplinutri | 5 pacientes |
  | Telepatia | US$ 0 de lançamento |
  | Aura | grátis, financiado por farma |

  O pago mais barato **sem cota** segue o Escriba Médico, a R$ 97.
- **Tudo-em-um:** com o escriba incluído, os preços de hoje vão de R$ 178,90 a R$ 590 por mês:

  | Produto | Total com escriba |
  |---|---|
  | SimDoctor | R$ 178,90 |
  | Darwin | R$ 197 |
  | MEDC | a partir de R$ 199 (R$ 298,90 no mensal) |
  | Doctoralia com Noa | mais de R$ 590 |

  Os R$ 49,90 do Calima saem baratos.
- **Teleconsulta avulsa:** a THM cobra R$ 49,90, igual ao Calima. O piso segue na Telemedico (R$ 40). O Dr. Consulta tirou o preço da página.
- **Secretária por profissional:** ninguém vende avulso abaixo de R$ 99,90. O piso segue na AgendaCare, a R$ 147 (de 1 a 3 profissionais). Depois vêm Singulare e PixelJarbas a R$ 197, Desler a R$ 198, MEDC Aiva a R$ 199 de lançamento (R$ 399 depois), Syntia a R$ 247 e Secretar.AI a R$ 360.

## Comoditização

- **O escriba virou add-on pago nos ERPs, não recurso grátis.** MEDC, Darwin, SimDoctor, Doctoralia, Feegow (VIP) e Amplimed cobram à parte, de R$ 80 a R$ 199. O único que dava a IA quase de graça (Ordexa) apertou a cota.
- **Meta, n8n e big techs:** nada novo para o Brasil. O Dragon Copilot e a Heidi continuam sem pt-BR.

## Posicionamento

1. **(a) O plano único de R$ 49,90 com 7 dias grátis sem cartão continua defensável, e ficou mais forte esta semana.** A tabela acima mostra o mercado cobrando de R$ 179 a R$ 400 por prontuário com escriba. O único abaixo do Calima (Ordexa) passou a ter cota semanal. Na página e nos e-mails da Black Friday, usar duas frases:
   - **"prontuários ilimitados, com o escriba incluído, por R$ 49,90"**;
   - "o mercado cobra de R$ 250 a R$ 400 por médico", frase da página da MEDC.

   Não mexer no teste nem no preço.
2. **(b) Add-on Secretária por médico: R$ 99,90 continua certo para o lançamento, e há espaço até R$ 147.** O avulso mais barato é a AgendaCare (R$ 147), e o grupo dos R$ 197–199 (Singulare, PixelJarbas, Desler, MEDC Aiva) ficou maior. A MEDC mostra outra referência: a secretária custa 2x o próprio plano. Se o custo medido (n8n + Haiku + Meta) passar de cerca de R$ 60 por médico, subir para R$ 129,90 ainda deixa o Calima abaixo de todos.
3. **(c) A profissão menos servida por escriba em pt-BR agora é a enfermagem.**
   - **Nutrição:** tem o Amplinutri, e a Dietbox anunciou anamnese por IA "em breve".
   - **Fisioterapia:** tem a Plenia e o Ordexa.
   - **Psicologia:** tem o PsicoManager, o Cuidaty e o Ordexa.
   - **Odontologia:** está saturada (Simples Dental e Clinicorp).
   - **Enfermagem:** o único prontuário dedicado à enfermagem autônoma que achei, o NurseUp (grátis até 2 pacientes), não anuncia ditado ([nurseup.com.br](https://nurseup.com.br/)). Os escribas multiprofissão (Ordexa, Plenia) não listam a enfermagem.

   O Calima já atende enfermagem. Vale uma página ou campanha **"evolução de enfermagem por voz"**, com curativo, escalas e passagem de plantão, que conversa com o DNA de plantão do Calima.

## Varredura completa: preços lidos em 16/11/2026

| Alvo | Preço lido | Mudou desde 09/11? |
|---|---|---|
| iClinic (/precos/) | R$ 99/129/169/299; anual −8%; teleconsulta 10 por R$ 34,90; WhatsApp a partir de R$ 29,90 | Teleconsulta R$ 35 → R$ 34,90 |
| Ninsaúde | não carregou | — |
| Feegow | não carregou (a reserva deu erro de TLS) | — |
| Amplimed | preços não públicos na página; AmpliBlack sem valores | Não |
| Doctoralia Pro | R$ 420,42/518,42/665,42 +2%; Noa Notes R$ 199 (60% off na oferta) | Não |
| Shosp | sob proposta (o iClinic informa a partir de R$ 149) | Não |
| Dr. Agenda | só os metadados carregaram | — |
| clina.ai | /precos dá 404; a home não renderiza | — |
| SmartDoctor | não público; 30 dias grátis | — |
| **MEDC** | R$ 99,90/169,90 no anual · R$ 159,90/229,90 no mensal; IA R$ 99 → R$ 199; Aiva R$ 199 → R$ 399 | **Novo alvo** |
| **Darwin Saúde** | Grátis no teste / R$ 117 / Pro + IA R$ 197 | **Novo alvo** |
| **SimDoctor** | R$ 49/69/89; IA R$ 129,90 | **Novo alvo** |
| Simples Dental | R$ 149,90/249,90/349,90 cheios; Black −20% no mensal por 10 meses, −25% no anual | Não |
| Clinicorp | R$ 159,90/369,90; trimestral R$ 127,19/330 | Trimestral exibido |
| Dietbox | Premium semestral 6x R$ 53,90; Profissional R$ 72,60; "Anamnese por IA em breve" | IA anunciada |
| WebDiet | Premium R$ 57,90 no semestral (depois R$ 94,90); Black R$ 83,90 | **Sim** |
| PsicoManager | R$ 89; Plus anual R$ 1.070,90 no Pix (cupom até 30/11) | Não |
| ZenFisio | não carregou | — |
| Vitalia Pro | o domínio não resolveu | — |
| Voa Health | Free 10 por mês / Pro R$ 349 (R$ 289 no anual) / Ultra R$ 2.900 | Não |
| Heidi | Free com limite semanal / Clinician não público; sem pt-BR | Free limitado |
| Freed | US$ 39 / 59–79 / 104–119; Front desk a partir de US$ 149 | Não |
| Telepatia | US$ 0 de lançamento (US$ 99 riscado) | Não |
| Dora | Grátis 10 por mês / R$ 79 | Não |
| Vokkari | R$ 0 (5 h e 10 pacientes) / R$ 179,99 / R$ 449,99 | Limite exibido |
| Ordexa | R$ 0 (30 ações de bônus) / R$ 39,90 / R$ 69,90, 100 ações por semana | **Cota menor** |
| Escriba Médico | R$ 97 / R$ 997 por ano | Não |
| Nabla, Abridge, Suki, Dragon Copilot | não público; nenhum no Brasil | — |
| Secretar.AI | R$ 360/720/1.080; anual −40% | Não |
| Singulare (.org) | R$ 197/397 + humano a partir de R$ 297 | Não |
| AgendaCare | R$ 0 / 79,90 / 147 / 297 / 497 / 797 / 1.297; conversa extra R$ 2,20 | Não |
| PixelJarbas | R$ 197/397; Plus a R$ 197 até 31/12 | Não |
| Desler | R$ 159/198/298; acesso extra R$ 79–150 | Não |
| Syntia | R$ 247 | Não |
| THM Saúde | avulsa R$ 49,90 · plano R$ 79,90 | Não |
| Dr. Consulta | a página tirou o preço | Preço sumiu |
| Einstein Conecta | o domínio não resolveu | — |
| Conexa | não público (vendida como benefício) | — |

---
Ferramentas: o agente web atendeu quase tudo (6 buscas, 6 extrações de cerca de 45 páginas e 2 prints). Três páginas foram para a reserva do Firecrawl: PsicoManager deu certo, clina.ai deu 404 e Feegow teve erro de TLS. Não carregaram em nenhuma fonte: Ninsaúde, Feegow, ZenFisio, Vitalia, Einstein Conecta e 4medic. Nenhum número foi estimado.

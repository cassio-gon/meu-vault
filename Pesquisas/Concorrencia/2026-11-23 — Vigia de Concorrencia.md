---
title: Vigia de Concorrência — 2026-11-23
date: 2026-11-23
area: Concorrencia
tags: [concorrencia, mercado]
source: routine
aviso: enviado
---

## TL;DR

- **NurseUp, o prontuário de enfermagem, ganhou ditado por voz campo a campo**, com o áudio descartado e funcionamento offline. Custa R$ 39,95/mês nos 3 primeiros meses e R$ 79,90 depois. É o mesmo desenho do Calima, e a enfermagem deixou de ser terreno vazio.
- **Recinto** (novo): escriba 100% local, para médico, psicólogo, fisioterapeuta e fono, por **R$ 879 de licença única**. No beta, a licença sai de graça.
- **Desler** dá o escriba de graça "por tempo limitado" no plano básico. **Pronova** subiu: de R$ 132,30 para R$ 189,90 por mês no anual.
- Calima sem mudança (R$ 49,90). Recomendação (c) ajustada: enfermagem **de plantão**, não de consultório.

> Comparado com o relatório de **2026-11-22**. **Varredura completa:** sim, por ser segunda. A anterior foi em 16/11. Cerca de 45 páginas relidas em 23/11/2026.
> Calima conferido no repo (`origin/main` `be3cc06`, o mesmo de ontem): R$ 49,90 no site (7 ocorrências), `VENDAVEIS = ['staff']`, `PLANO_STAFF_CENTS` e `CONSULTA_AVULSA_CENTS` com default 4990.

## Achados

1. **NurseUp passou a ter registro por voz.**
   - A enfermeira aperta o microfone e conta o atendimento. A IA distribui o texto campo a campo, como sugestão, e ela aceita, edita ou descarta item por item. O áudio é descartado depois da transcrição. O app funciona sem internet e sincroniza quando a conexão volta.
   - Também tem: escalas (Braden, Morse, Glasgow, Norton) dentro do atendimento, diagnósticos sugeridos, metas com prazo, fichas de feridas, estomia, podiatria e obstetrícia, documentos assinados com o COREN e uma assistente de IA, a "Tami".
   - **Preço:** grátis para até 2 pacientes, sem prazo. Depois, R$ 79,90/mês, com lançamento a R$ 39,95 nos 3 primeiros meses. A telenfermagem e a conta de clínica estão "em breve".
   - Em 16/11, a mesma página não anunciava ditado.

   Fonte: [nurseup.com.br](https://nurseup.com.br/), lida em 23/11/2026.
   ![NurseUp, capa no celular](https://agente.cassiogon.tech/prints/cd687c9988cb56242a89e810729dbeeb.jpg)
   - **E daí pro Calima:** a NurseUp copia o desenho do Calima (o profissional dita, a IA preenche campo por campo, ele revisa e o áudio não fica guardado) com fichas próprias de enfermagem e a metade do preço por 3 meses. Ela mira o consultório e o atendimento domiciliar (feridas, estomia). O que segue sem dono é a enfermagem de plantão: passagem de caso, turno e teleconsulta.

2. **Recinto: escriba que roda dentro do computador, por licença única.**
   - Grava a consulta ou a sessão, transcreve (whisper.cpp) e gera a nota da profissão: médico, psicólogo, fisioterapeuta e fonoaudiólogo. Também faz receita, atestado e laudo em PDF.
   - Não usa nuvem. Pede Mac com chip M1 ou mais novo, ou Windows 10/11, e 16 GB de RAM. Na primeira vez, baixa cerca de 6 GB de modelos.
   - **Preço:** R$ 879 à vista ou 10x de R$ 87,90, uma vez só, sem mensalidade. Há 30 dias grátis. No programa de beta, quem testa por 1 mês ganha a licença definitiva da Edição 2026 sem pagar.

   Fonte: [recintoapp.com.br](https://recintoapp.com.br/), lida em 23/11/2026. Primeira vez neste vigia.
   ![Recinto, capa no celular](https://agente.cassiogon.tech/prints/6f286eb4d9533d3c12534273688f3a8a.jpg)
   - **E daí pro Calima:** R$ 879 equivalem a cerca de 18 meses de Calima. Com o slogan "LGPD por arquitetura", o Recinto disputa o argumento de privacidade. O Calima rebate com celular e plantão, onde não existe Mac de 16 GB, e com a teleconsulta e o portal, que o Recinto não tem.

3. **Desler dá o escriba de graça, por tempo limitado.**
   - O "Copiloto no Prontuário e Laudo" escuta a consulta e preenche o prontuário estruturado, e também preenche laudos de ultrassom e ergométrico falando. A página diz que ele está "disponível gratuitamente no plano básico por tempo limitado", sem dizer até quando.
   - Os planos seguem iguais: Gestão R$ 159, IA Básico R$ 198 (com a secretária no WhatsApp) e IA Pro R$ 298, todos com 2 acessos. O anual tem 20% de desconto.

   Fonte: [desler.com.br](https://desler.com.br/) e [/planos-precos](https://desler.com.br/planos-precos), lidas em 23/11/2026.
   - **E daí pro Calima:** é o primeiro ERP deste vigia a dar escriba sem cobrar à parte, mas em cima de um plano de R$ 159. O Calima inteiro segue mais barato.

4. **Pronova Tech subiu o preço.**
   - O Solo Plus custava R$ 132,30/mês no anual, com 30% de desconto (lido em 10/11). Agora custa **R$ 189,90/mês no anual** (R$ 2.278,80/ano), com 17% de desconto.
   - O Clínica, para 2 médicos, sai por R$ 343,90/mês. Há 7 dias grátis sem cartão.

   Fonte: [pronovatech.com.br](https://pronovatech.com.br/), lida em 23/11/2026.
   - **E daí pro Calima:** é mais um escriba que fica mais caro, e não mais barato. A distância para os R$ 49,90 aumentou.

5. **Clinicorp (odontologia): o Standard baixou e há Black November.** O Standard passou de R$ 159,90 para **R$ 149,90/mês**; o Premium continua em R$ 369,90. A página anuncia "até 50% OFF", sem detalhar a oferta. O registro por voz da Clinicorp IA segue como módulo pago à parte, sem preço público. O Simples Dental agora dá de brinde uma peça de mão Schuster e mais 1 mês no Pro Anual (ou 20% off no mensal por 10 meses). Fontes: [clinicorp.com](https://www.clinicorp.com/) e [simplesdental.com](https://www.simplesdental.com/), lidas em 23/11/2026.
   - **E daí pro Calima:** na odontologia, o escriba continua pago à parte e caro. Nada muda.

6. **Medora publicou preço: a partir de R$ 111,33 por profissional, com mínimo de 3.** O Starter custa R$ 300,59/mês no anual (R$ 333,99 no mensal), o Business R$ 500,39 e o Enterprise R$ 1.124,99. O escriba Téo ("Evolução Inteligente") e a secretária DoraChat são add-ons sem preço. Fonte: [medora.com.br/planos](https://medora.com.br/planos), lida em 23/11/2026.
   - **E daí pro Calima:** a Medora é para clínica, não para o autônomo, e não vende para 1 profissional. Não pressiona o preço.

7. **Theravus (psicologia) na Black Friday.** O anual sai com 50% de desconto até 30/11: R$ 479,40/ano no Individual (cerca de R$ 40/mês). O mensal fica em R$ 79,90, com o preço garantido por 12 meses. Os planos incluem "IA clínica", mas a página não diz se ela transcreve a sessão. Fonte: [theravus.com.br, comparativo de 20/11](https://www.theravus.com.br/blog/comparativo-sistemas-para-psicologos), lida em 23/11/2026. Primeira vez neste vigia.
   - **E daí pro Calima:** se a IA dela transcrever, é um sistema completo de psicologia abaixo dos R$ 49,90 até 30/11. Vale conferir na próxima varredura.

8. **Teleconsulta ao paciente:**
   - O Dr. Consulta voltou a mostrar preço: "consultas a partir de R$ 45", sem separar a presencial da online. A assinatura online custa 12x de R$ 9,90. Fonte: [drconsulta.com](https://drconsulta.com/), lida em 23/11/2026.
   - A Vem Consulta vende um plano mensal de R$ 9,90 (de R$ 34,30). Fonte: [vemconsulta.com.br/twin](https://www.vemconsulta.com.br/twin), visto só no trecho da busca.
   - **E daí pro Calima:** a avulsa de R$ 49,90 continua no meio da faixa. Contra assinaturas de R$ 9,90, o Calima vende o médico do próprio paciente, não um plantonista qualquer.

## Regulação

- **Nada novo.**
- **CFM 2.454/2026:** só artigos de escritório de advocacia e de fornecedores.
- **Telemedicina:** a JusConsulta reabriu o debate sobre a consulta presencial a cada 180 dias da CFM 2.314/2022, mas a regra é de 2022 e não mudou.
- **Meta/WhatsApp:** só guias repetindo a cobrança por mensagem de serviço desde 01/10.
- **Anvisa, ANPD, CFP, CFN, CFO, COFFITO, COFEN e Apple:** nada na semana.

## Pressão de preço

- **Escriba abaixo de R$ 49,90:**
  - **NurseUp:** R$ 39,95 por 3 meses, só na enfermagem; depois R$ 79,90.
  - **Recinto:** de graça no beta; depois R$ 879 uma vez só.
  - **Ordexa:** R$ 39,90, com 100 ações por semana.
  - **Desler:** grátis "por tempo limitado", mas dentro de um plano de R$ 159.

  O pago mais barato **sem cota e por assinatura** segue o Escriba Médico, a R$ 97.
- **Tudo-em-um:** sem mudança. Com escriba, o mercado cobra de R$ 159 (Desler, por enquanto) a R$ 590 (Doctoralia com Noa). Os R$ 49,90 seguem baratos.
- **Teleconsulta avulsa:** o Dr. Consulta diz "a partir de R$ 45", sem separar online e presencial. A THM e a ClickSaúde cobram R$ 49,90, igual ao Calima.
- **Secretária por profissional:** nada abaixo de R$ 99,90. O piso segue na AgendaCare, a R$ 147 para 1 a 3 profissionais.

## Comoditização

- **Primeiro ERP com escriba de graça:** a Desler, temporariamente e dentro de um plano pago. Os demais seguem cobrando à parte: MEDC, Darwin, SimDoctor, Clinicorp, Amplimed e Medora.
- **O desenho "dita, a IA preenche campo a campo, o profissional revisa" virou padrão de nicho.** NurseUp na enfermagem, DietSystem na nutrição. O diferencial do Calima está menos no ditado e mais no pacote: plantão, teleconsulta, portal do paciente e o preço único.
- **Meta, n8n e big techs:** nada novo em pt-BR. O Dragon Copilot ganhou um instalador para desktop, ainda sem pt-BR.

## Posicionamento

1. **(a) O plano único de R$ 49,90 com 7 dias grátis sem cartão continua defensável.**
   - Quem cobra menos tem cota (Ordexa), está em promoção de entrada (NurseUp), cobra licença de R$ 879 (Recinto) ou dá o escriba de graça dentro de um plano de R$ 159 (Desler). E a Pronova subiu.
   - Sobre o teste: Recinto, VoicIA, Singulare e WebDiet dão 30 dias. Sem dado de conversão do teste à mão, manter os 7 dias. Se a conversão estiver baixa, testar 14 dias antes de chegar a 30.
2. **(b) Add-on Secretária por médico: manter R$ 99,90 no lançamento.** A faixa não mudou:

   | Concorrente | Preço/mês |
   |---|---|
   | AgendaCare | R$ 147 |
   | Singulare | R$ 197 |
   | Desler | R$ 198 |
   | MEDC Aiva | R$ 199, depois R$ 399 |
   | Secretar.AI | R$ 360 |
   | Clara | R$ 690 |

   Teto seguro de R$ 129,90 se o custo medido passar de cerca de R$ 60 por médico.
3. **(c) A profissão menos servida segue sendo a enfermagem, mas o foco agora é o plantão.**
   - A NurseUp ocupou a enfermagem de consultório e domiciliar, com ditado.
   - Ninguém atende a **enfermagem de plantão e hospitalar**: evolução do turno, passagem de plantão, escalas e cronômetro. É exatamente o DNA do Calima.
   - Fisioterapia ganhou o Recinto, além de Plenia e Ordexa. Psicologia e nutrição seguem cheias.
   - Para a campanha "evolução de enfermagem por voz", falar de **plantão**, não de curativo de consultório, onde a NurseUp já está.

## Varredura completa: preços lidos em 23/11/2026

| Alvo | Preço lido | Mudou desde 16/11? |
|---|---|---|
| iClinic | R$ 99/129/169/299; anual −8%; teleconsulta 10 por R$ 34,90; teste 5 dias | Não |
| Ninsaúde | /precos dá 404; home sem preço | — |
| Feegow | não carregou (agente web e Firecrawl: erro de TLS) | — |
| Amplimed | Lite R$ 89 / Pro R$ 139; Amélia Transcrição sem preço; AmpliBlack sem valores | Não |
| Doctoralia Pro | sem preço na página; Noa Notes 60% off nos planos Plus e VIP, "por tempo limitado" | Não |
| Shosp | a partir de R$ 149 por prestador (pela página do iClinic) | Não |
| Dr. Agenda | secretária IA 24h; preço não público | — |
| clina.ai | não carregou | — |
| MEDC | R$ 99,90/169,90 no anual · R$ 159,90/229,90 no mensal; IA R$ 99 → R$ 199; Aiva R$ 199 → R$ 399 | Não |
| Darwin Saúde | R$ 117 / Pro + IA R$ 197 | Não |
| SimDoctor | R$ 49/69/89; IA R$ 129,90 | Não |
| **Medora** | a partir de R$ 111,33 por profissional (mínimo 3); Starter R$ 300,59 no anual | **Preço novo** |
| **Desler** | R$ 159/198/298; escriba grátis por tempo limitado no básico | **Escriba grátis** |
| **Pronova Tech** | Solo Plus R$ 189,90 no anual (−17%); Clínica R$ 343,90 | **Subiu** (era R$ 132,30) |
| Simples Dental | sem preço na home; MEGABLACK: peça de mão + 1 mês no anual, ou −20% no mensal por 10 meses | Brinde novo |
| **Clinicorp** | Standard R$ 149,90 / Premium R$ 369,90; até 50% off | **Standard −R$ 10** |
| Dietbox | página de planos não mostrou preço | — |
| WebDiet | Premium R$ 57,90 (semestral; depois R$ 94,90) / Black R$ 83,90; 30 dias grátis | Não |
| DietSystem | R$ 29,90 → R$ 49,90 → R$ 79,90 | Não |
| PsicoManager | Pró R$ 89; Plus anual R$ 1.070,90 no Pix (cupom até 30/11) | Não |
| **Theravus** | R$ 89,90/159,90; Black anual R$ 479,40 e R$ 779,40 até 30/11 | **Novo alvo** |
| **NurseUp** | grátis até 2 pacientes; R$ 39,95 por 3 meses → R$ 79,90; **ditado por voz** | **Ditado novo** |
| Voa Health | Free 10 por mês / Pro R$ 349 (R$ 289 no anual) / Ultra R$ 2.900; Black até 30/11 | Não |
| Vokkari | R$ 0 (5 h, 10 pacientes) / R$ 179,99 / R$ 449,99 | Não |
| Ordexa | R$ 0 / R$ 39,90 / R$ 69,90; 100 ações por semana | Não |
| Escriba Médico | R$ 97 / R$ 997 por ano | Não |
| VoicIA | R$ 197 no anual; 30 dias grátis | Não |
| **Recinto** | licença única R$ 879 (10x R$ 87,90); grátis no beta | **Novo alvo** |
| Dora | não carregou | — |
| Heidi | Free com cota semanal; Clinician sem preço; sem pt-BR | Não |
| Freed | US$ 39–119 (página ambígua entre mensal e anual) | Não |
| Nabla, Abridge, Suki, Dragon Copilot | não público; nenhum em pt-BR | — |
| Secretar.AI | R$ 360/720/1.080; anual −40% | Não |
| Singulare | R$ 197/397; humano a partir de R$ 297; 30 dias grátis | Não |
| AgendaCare | R$ 0 / 79,90 / 147 / 297 / 497 / 797 / 1.297 | Não |
| Clara | R$ 690 ou pré-pago com R$ 150 de crédito | Não |
| THM Saúde | avulsa R$ 49,90 · plano R$ 79,90 | Não |
| **Dr. Consulta** | consultas a partir de R$ 45; assinatura online 12x R$ 9,90 | **Preço voltou** |
| Telemedico | preço por médico, não público na home | — |
| Einstein Conecta | o domínio não resolve | — |
| Conexa | não público | — |

---
Checado hoje: 9 buscas (prontuário com IA, secretária no WhatsApp, rodadas, regulação, outras profissões, WhatsApp/Meta, big techs, teleconsulta avulsa, Black Friday), 5 extrações (cerca de 45 páginas) e 3 leituras diretas, mais 2 prints.

Já registrados e não repetidos: Aionmed (de novo no noticiário), Aura, Klinity, Skedia (rodada já vista), Clara, Cloudia, Secretária IA (usesecretariaia), Instituto Consenso.

Reserva: 1 página foi para a reserva (Feegow no Firecrawl, que deu o mesmo erro de TLS). Dentro do próprio agente web, Freed e Dr. Consulta vieram pelo Firecrawl cloud. Nenhum número foi estimado; "cerca de 18 meses" e "cerca de R$ 40/mês" são contas feitas sobre os preços publicados.

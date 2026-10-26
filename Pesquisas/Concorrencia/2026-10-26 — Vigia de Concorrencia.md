---
title: Vigia de Concorrência — 2026-10-26
date: 2026-10-26
area: Concorrencia
tags: [concorrencia, mercado]
source: routine
---

## TL;DR

- A THM Saúde vende teleconsulta avulsa a R$ 49,90, 24h, o mesmo preço da consulta do Calima. Também vende plano ilimitado a R$ 79,90/mês. É o primeiro preço público nesse patamar.
- O clina.ai publicou a tabela em /planos: Clina Completo para médico a R$ 249/mês (ontem, R$ 219) e módulo Atendimento (prontuário + IA) a R$ 99/mês avulso.
- Os outros 40 preços não mudaram. A Telepatia segue a US$ 0, e o TRF1 ainda não decidiu sobre a CFM 2.454.

> Comparado com o relatório de **2026-10-25**. **Varredura completa:** sim, por ser segunda-feira. Todas as páginas oficiais foram relidas em 26/10/2026 pelo Firecrawl, com `maxAge: 0`.
> Preço do Calima conferido no repo: o `site/index.html` mostra R$ 49,90/mês com 7 dias grátis sem cartão; `VENDAVEIS = ['staff']`; o default de `PLANO_STAFF_CENTS` e de `CONSULTA_AVULSA_CENTS` é 4990. Nada mudou.

## Achados

1. **THM Saúde: teleconsulta avulsa a R$ 49,90 (pagamento único), clínico geral 24h, e "plano ilimitado" a R$ 79,90/mês, sem fidelidade.** Especialidades (cardio, derma, pediatria, gineco, endócrino, orto, otorrino) são atendidas com hora marcada. Os médicos são da rede credenciada deles. Um reel novo com esses preços saiu por volta de 24/10. A oferta já existia, mas não estava nos relatórios.
   - Fonte: [thmsaude.com.br](https://thmsaude.com.br/), lido em 26/10/2026.
   - **E daí pro Calima:** na consulta avulsa, os R$ 49,90 do Calima deixam de ser o preço mais baixo e passam a ser o preço de mercado. O diferencial tem de ser continuidade: o mesmo médico, prontuário e documentos no portal. Contra 24h com clínico de plantão, o Calima não ganha.

2. **clina.ai: a tabela oficial agora fica em [clina.ai/planos](https://clina.ai/planos) e é por profissão.**
   - **Pacote:** Clina Completo — Médico a R$ 249/mês (R$ 2.490/ano). A tabela de 25/10 dizia "Pro R$ 219"; hoje não existe plano "Pro". O Clina Clínica segue a partir de R$ 397. O núcleo grátis (página, agenda e Sofia) continua.
   - **Módulos avulsos:** Atendimento ("prontuário e IA") R$ 99; Atendimento online R$ 39; Documentos & Modelos R$ 69.
   - **Módulos novos de secretária:** Sofia Triagem pré-consulta e Sofia Acompanhamento & Retorno, a R$ 49 cada.
   - A home ainda diz "a partir de R$ 199" e o FAQ não mostra mais preço.
   - **E daí pro Calima:** para ter o que o Calima entrega por R$ 49,90 (Atendimento + Atendimento online + Documentos), o médico paga R$ 207/mês no clina.ai, quatro vezes mais. A Sofia vendida em módulos de R$ 49 é a referência mais próxima para dividir o add-on da secretária em partes.

3. **SmartDoctor (prontuário, agenda e teleconsulta) lançou o "Escriba IA" em 21/10.** Ele grava a teleconsulta e gera o resumo por IA, e o lançamento trouxe também assinatura VIDaaS/BirdID e escalas PHQ-9 e GAD-7. A página não mostra preço.
   - Fonte: [smartdoctor.com.br/novidades](https://www.smartdoctor.com.br/novidades), página de 21/10/2026, que não estava no relatório anterior.
   - **E daí pro Calima:** mais um tudo-em-um com scribe embutido, agora dentro da teleconsulta. Vale pôr o SmartDoctor na lista de alvos da varredura.

4. **Clinicorp (odontologia) mostra os "Agentes Clinicorp IA" no WhatsApp**: agendamento, desmarcação, faltas, inadimplência, CRM e orçamento. Cita também "Voice Control" e a gravação da negociação do orçamento. O preço é sob consulta. A Secretária IA do Simples Dental passou a anunciar que "entende áudios".
   - Fontes: [clinicorp.com/planos](https://clinicorp.com/planos) e [simplesdental.com/planos-e-precos](https://www.simplesdental.com/planos-e-precos), lidos em 26/10/2026.
   - **E daí pro Calima:** os dois ERPs líderes da odontologia já têm secretária IA, então a odontologia fica mais disputada para o Calima.

5. **Einstein Conecta: o índice de busca do site oficial mostra consulta avulsa a R$ 389,90.** A página ao vivo não carregou (Firecrawl falhou e o curl tomou 403). O mesmo trecho traz plano individual a R$ 129,90/mês e familiar a R$ 99,90/mês, os dois anuais. **Não confirmado, data do trecho desconhecida.**
   - Fonte: telemedicina.einstein.br, só o trecho da busca.
   - **E daí pro Calima:** se o valor se confirmar, a avulsa premium custa oito vezes os R$ 49,90, o que mostra a faixa do mercado de ponta a ponta.

**Regulação sem mudança que afete o Calima:**
- **CFM 2.454/2026:** sem decisão do TRF1. A matéria de 24/10 repete o estado de 19/10. ([portalolavodutra](https://www.portalolavodutra.com.br/materias/medicos_recorrem_a_justica_para_garantir_que_uso_de_ia_siga_a_vontade_do_paciente))
- **Apple:** a 1.4.1 e a 5.1.1(ix) foram relidas na página oficial (revisão de 16/10). O texto sobre app médico e o envio da documentação regulatória "se houver" é o mesmo de antes, sem exigência nova. ([developer.apple.com](https://developer.apple.com/app-store/review/guidelines/))
- **CFP:** um post de cerca de 23/10 cita um grupo de trabalho sobre IA na psicologia, aprovado num congresso no Chile. Ainda não há norma.
- **CFN, CFO, COFFITO, COFEN, ANPD, Anvisa (RDC 657) e WhatsApp Cloud API:** nada datado depois de 24/10.

## Pressão de preço

- **Scribe abaixo de R$ 49,90:** os mesmos de ontem, a Telepatia AI (US$ 0 de lançamento, ainda no ar em 26/10) e o Voa Free (10 atendimentos/mês). O pago mais barato em pt-BR continua sendo o PsicoManager, a R$ 89.
- **Tudo-em-um:** o clina.ai ficou mais caro (pacote médico de R$ 219 para R$ 249). O módulo de prontuário com IA, sozinho, custa R$ 99, o dobro do Calima. Ninguém com scribe fica abaixo de R$ 49,90.
- **Teleconsulta avulsa ao paciente:** **empate**. A THM Saúde cobra R$ 49,90 com clínico 24h. Ninguém cobra menos pela avulsa. Por assinatura, a Portal Telessaúde anuncia "médico 24h" a R$ 18,99/mês num post de cerca de 24/10, sem dizer quem atende.
- **Secretária no WhatsApp abaixo de R$ 99,90 por profissional:** igual a ontem.
  - Embutida em outro produto: Sofia do clina.ai grátis, Dr. Agenda R$ 70, AgendaCare R$ 147 para 1 a 3 profissionais.
  - Nova referência: o clina.ai cobra R$ 49 por função extra da Sofia (triagem ou retorno).
  - Avulsa: o piso continua em R$ 147.

## Comoditização

- **Scribe embutido:** entraram o SmartDoctor (Escriba IA na teleconsulta) e a Clinicorp ("Voice Control"). Já estavam na lista Feegow, Amplimed, PsicoManager, Simples Dental e Doctoralia (Noa Notes, em campanha do Mês do Médico).
- **A Conexa diz que a IA transcreve e sugere o prontuário em mais de 98% das consultas**, num post de cerca de 23/10. É uso interno, não produto vendido.
- **Meta, WhatsApp e n8n:** nada novo de graça.
- **Big tech:** nenhum ditado clínico em pt-BR. O Dragon Copilot segue sem venda no Brasil. O MAI-DxO, da Microsoft (Science, 23/10), é IA de diagnóstico, não scribe.

## Posicionamento — recomendações

1. **O plano único de R$ 49,90 com 7 dias grátis sem cartão continua defensável.** O equivalente no clina.ai custa R$ 207–249, e todo scribe pago em pt-BR custa mais. O risco segue sendo o grátis da Telepatia. Na teleconsulta avulsa ao paciente, o preço deixou de ser argumento por causa da THM. No portal, vender "consulta com o seu médico, com prontuário e documentos no mesmo lugar", não "consulta barata".
2. **Add-on Secretária por médico: manter R$ 99,90 e estudar a venda em partes.** O clina.ai já cobra R$ 49 por função da Sofia (triagem ou retorno), em cima de uma secretária base grátis. Opção: R$ 99,90 com agendar, remarcar e cobrar, e funções extras a ~R$ 39–49. O teto continua em R$ 147, o piso avulso do mercado (AgendaCare).
3. **Profissão menos servida: segue a nutrição, com a enfermagem logo atrás.** Dietbox e WebDiet foram relidos: só têm IA de plano alimentar e documentos, nada de voz. A odontologia ficou mais disputada (Clinicorp e Simples Dental com secretária IA e voz), então não deve ser a próxima frente.

## Varredura completa — preços lidos em 26/10/2026

| Alvo | Preço lido | Mudou? |
|---|---|---|
| iClinic | R$ 99/129/169/299; add-on de WhatsApp a partir de R$ 29,90; 10 teleconsultas por R$ 35/mês | Não (a teleconsulta é dado novo) |
| Ninsaúde Apolo | R$ 199 (1 agenda) | Não |
| Feegow | R$ 129/199/249 | Não |
| Amplimed | R$ 89 / R$ 139 | Não |
| Doctoralia Pro | R$ 429/529/679 + Noa Notes R$ 199 + site R$ 99 | Não |
| Shosp | R$ 0 + ativação R$ 299 / R$ 149 / R$ 229 | Não |
| Dr. Agenda | R$ 70 promo (de R$ 90), com secretária IA | Não |
| clina.ai | Grátis / Completo Médico R$ 249 / Clínica a partir de R$ 397; módulos de R$ 39 a R$ 99 | **Sim** |
| Simples Dental | R$ 149,90/249,90/349,90 (anual R$ 137,41/229,08/320,74); Secretária IA por menos de R$ 6/dia | Não |
| Clinicorp | R$ 159,90 / R$ 369,90; combos de IA sob consulta | Não |
| Dietbox | R$ 49,90 por 3 meses, depois R$ 91,90 · R$ 133,90 | Não |
| WebDiet | R$ 49,90 por 3 meses, depois R$ 94,90 · R$ 139,90 | Não |
| PsicoManager | R$ 89 / R$ 119 | Não |
| ZenFisio | R$ 79/179/439 | Não |
| Vitalia Pro | R$ 63/119/223 no anual | Não |
| Voa Health | Free / Pro R$ 289–349 / Ultra R$ 2.490–2.900 | Não |
| Heidi Health | Free / US$ 110 / sob consulta | Não |
| Freed | US$ 39–59 / 59–79 / 104–119 | Não |
| Telepatia AI | US$ 0 de lançamento (US$ 99 riscado) | Não |
| Nabla, Abridge, Suki, Dragon Copilot | Não público (as páginas de preço da Nabla e da Suki dão 404) | — |
| Assist4Doc | R$ 197/397/997 | Não |
| Secretar.AI | R$ 360/720/1.080 | Não |
| Singulare | R$ 197/397 + atendimento humano R$ 297 | Não |
| AgendaCare | R$ 0 (60 agendamentos) / R$ 79,90 / R$ 147 / R$ 297 / R$ 497 / R$ 797 / R$ 1.297 | Não (as outras faixas são dado novo) |
| Desler AI | R$ 159/198/298 | Não |
| THM Saúde | Avulsa R$ 49,90 · plano R$ 79,90/mês | **Novo alvo** |
| Dr. Consulta, Conexa, Doctoralia (teleconsulta) | Não público | — |
| Einstein Conecta | Ao vivo não carregou; R$ 389,90 avulsa só no trecho da busca | Não confirmado |

**Lacunas:**
- O Einstein Conecta não carregou ao vivo.
- O Firecrawl bateu no limite por minuto, mas todos os outros alvos foram lidos.
- Os dados tirados do Instagram e do Facebook (THM, Portal Telessaúde, Conexa, CFP) vêm só do trecho da busca, com data aproximada.
- Nenhum número foi estimado.

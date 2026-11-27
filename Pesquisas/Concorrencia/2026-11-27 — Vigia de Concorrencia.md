---
title: Vigia de Concorrência — 2026-11-27
date: 2026-11-27
area: Concorrencia
tags: [concorrencia, mercado]
source: routine
aviso: brief
---

## TL;DR

- **A Conclínica cobra o escriba por uso: R$ 1 por consulta ou R$ 99/mês ilimitado.** É preciso um plano de R$ 89 a R$ 169, e com ele o pacote parte de R$ 90 + R$ 1 por consulta.
- **A Villo vende a secretária de IA no WhatsApp (Luna) como extra a partir de R$ 89,90 por clínica.** É o primeiro preço público de add-on abaixo dos R$ 99,90 em estudo, mas exige um plano de R$ 249,90 ou mais por profissional.
- **Na psicologia o escriba já custa R$ 29,90 a R$ 49,90:** Brainn Care (15 sessões/mês) e Sinthoma (grátis com 3 pacientes).
- Calima sem mudança (R$ 49,90). A recomendação (b) ganha uma âncora nova; (a) e (c) seguem iguais.

> Comparado com o relatório de **2026-11-26**. **Varredura completa:** não (sexta; a última foi em 23/11). Reabertas só as páginas de quem apareceu na busca.
> Calima conferido no repo (`origin/main` `e7b3963`): R$ 49,90 no site (7 ocorrências), `VENDAVEIS = ['staff']`, `PLANO_STAFF_CENTS` e `CONSULTA_AVULSA_CENTS` com default 4990.

## Achados

1. **Conclínica: escriba a R$ 1 por consulta ou R$ 99/mês ilimitado.**
   - Num artigo de 26/11, a Conclínica diz que o escriba escuta a consulta, no consultório ou na telemedicina, e preenche os campos do prontuário: queixa principal, HDA, antecedentes, exame físico e conduta.
   - **Preço:** os planos vão de R$ 89 a R$ 169/mês e já trazem confirmação automática pelo WhatsApp, que não é conversacional. A transcrição é cobrada à parte, a **R$ 1 por consulta** ou **R$ 99/mês ilimitada**. O teste dura 7 dias, sem cartão.
   - O artigo diz que as transcrições avulsas custam R$ 250 a R$ 400/mês por profissional e que os agentes de WhatsApp contratados por fora custam R$ 500 a R$ 1.800/mês. São números dela, não conferidos.

   Fonte: [conclinica.com.br, 26/11/2026](https://conclinica.com.br/agentes-de-ia-para-clinicas/). Primeira vez neste vigia.
   ![Conclínica, artigo de 26/11](https://agente.cassiogon.tech/prints/14eedf3edaa2e0eb2ca1faf0971a7a1c.jpg)
   - **E daí pro Calima:** é o primeiro escriba cobrado por consulta. Para quem atende pouco, R$ 89 + R$ 1 por consulta chega perto dos R$ 49,90 em número de consultas, mas nunca fica abaixo, porque só o plano já passa disso. O argumento do Calima continua sendo "ilimitado por R$ 49,90, com teleconsulta".

2. **Villo: secretária "Luna" no WhatsApp oficial a partir de R$ 89,90 por clínica, como extra.**
   - É um sistema para 10 áreas da saúde (psicologia, medicina, nutrição, odontologia, fisioterapia, fono, TO e outras). Tem escriba ao vivo com os falantes separados, assinatura ICP-Brasil, teleconsulta a partir do plano Clínica e Pix.
   - A Luna atende no WhatsApp pela API oficial da Meta: oferece horário, agenda, remarca, cancela e cobra Pix. Ela também entende áudio, foto e PDF.
   - **Preço por profissional por mês:**
     - Essencial, sem IA: R$ 129,90.
     - Consultório: R$ 249,90 (15 h de transcrição por semana).
     - Clínica: R$ 379,90.
     - Completo: R$ 639,90, já com a Luna.
     - A Luna sai a partir de R$ 89,90 por clínica, como extra dos planos Consultório e Clínica.
   - O teste dura 7 dias, sem cartão.

   Fonte: [byvillo.com](https://byvillo.com/), lida em 27/11/2026. Primeira vez neste vigia.
   ![Villo, capa no celular](https://agente.cassiogon.tech/prints/8c40ad9646122afd3af79f5fa19bbddb.jpg)
   - **E daí pro Calima:** é a primeira âncora pública de secretária vendida como extra, e fica abaixo dos R$ 99,90 em estudo. Para o profissional, o mínimo da Villo com escriba e Luna dá R$ 339,80/mês. O Calima com a secretária daria R$ 149,80.

3. **Brainn Care: escriba para psicologia a partir de R$ 29,90/mês.**
   - Transcreve a sessão ao vivo e gera a evolução no padrão CFP. Funciona no presencial (o celular vira o microfone), no Meet, no Zoom e na sala própria.
   - **Preço (anual / mensal):**
     - Entrada: R$ 29,90 / R$ 49,90, até 15 sessões por mês.
     - Básico: R$ 69,90 / R$ 99,90, ilimitado.
     - Premium: R$ 149,90 / R$ 199,90, "em lançamento", com análise de risco.
   - O teste dura 7 dias, sem cartão.

   Fonte: [brainn.care](https://brainn.care/), lida em 27/11/2026. Primeira vez neste vigia.
   ![Brainn Care, capa no celular](https://agente.cassiogon.tech/prints/7120cd9912740765b56d7cdf1ecc8e41.jpg)
   - **E daí pro Calima:** no mensal, o Entrada empata com os R$ 49,90, mas com teto de 15 sessões. O Calima ilimitado só fica abaixo da Brainn quando ela é paga no anual e o volume é baixo.

4. **Sinthoma: prontuário com escriba para psicologia, com plano grátis.**
   - Gera a evolução em 7 formatos (DAP, SOAP, BIRP etc.). Diz ter "checagem anti-alucinação" e alerta de risco. Tem teleconsulta própria e Pix sem taxa.
   - **Preço:**
     - Free: R$ 0, com 3 pacientes ativos e 30 análises de IA por mês.
     - Pro: R$ 89,90 no mensal ou R$ 67,40 no anual.
     - Clínica: R$ 199 a R$ 499.
   - A assinatura começa com 14 dias de Pro.

   Fonte: [sinthoma.com.br](https://sinthoma.com.br/), lida em 27/11/2026. Primeira vez neste vigia.
   - **E daí pro Calima:** "anti-alucinação" deixou de ser termo exclusivo do Calima, até em nicho. O diferencial que se pode provar continua sendo o texto montado por código.

5. **Escuta Med: escriba para medicina, odontologia, nutrição e psicologia, com 15 dias grátis.**
   - Transcreve em tempo real com os falantes separados e gera o relatório no modelo da especialidade. O áudio é descartado. Tem assinatura ICP-Brasil, guia CMED, agendamento por voz e escalas.
   - "Sem limite de pacientes ou consultas" e sem módulos à parte. O preço não é público (passa pelo comercial).

   Fonte: [aescutamed.com.br](https://www.aescutamed.com.br/), lida em 27/11/2026 (a página de conformidade é de 26/11/2026). Primeira vez neste vigia.
   - **E daí pro Calima:** é mais um escriba multiprofissional com áudio descartado. O teste de 15 dias, contra os 7 do Calima, é o ponto a vigiar.

6. **Certu: secretária no WhatsApp para clínicas a R$ 349/mês.**
   - Responde preço, convênio e horário e marca a consulta na agenda de cada profissional. Não responde dúvida de saúde e, em urgência, manda ligar para o 192.
   - Integra com Google Agenda e Feegow. A API oficial da Meta custa R$ 50/mês à parte no plano Start.
   - **Preço:** Start R$ 349/mês (5 pessoas) e Pro R$ 629/mês. Não há teste grátis.

   Fonte: [certu.com.br, atualizada em 25/11/2026](https://certu.com.br/secretaria-virtual-para-clinica). Primeira vez neste vigia.
   - **E daí pro Calima:** a secretária avulsa para clínica fica na faixa dos R$ 350. Os R$ 99,90 por médico do add-on ficam bem abaixo dela.

7. **Guia Odonto lança a Secretária IA no WhatsApp para dentistas.**
   - Atende 24 h, agenda, remarca e cancela, e liga a secretária ao marketing de retorno (por exemplo, um contato 6 meses depois do implante). O preço não é público.

   Fonte: [blog Guia Odonto, 23/11/2026](https://blog.guiaodonto.com/2026/11/23/secretaria-ia-do-guia-odonto-atendimento-24-horas-e-agendamento-automatico-pelo-whatsapp/).
   - **E daí pro Calima:** na odontologia, a secretária no WhatsApp vira item de série. Já são três: Simples Dental, Clinicorp e agora Guia Odonto.

## Regulação

- **Nada novo.**
- **CFM 2.454/2026:** só textos que repetem a regra (JOTA, AI Brasil, Brasil em Folhas, Conclínica). O AI Brasil cita a IA na telessaúde da Hapvida (Em Tempo, 25/11), mas o CFM não publicou nada novo.
- **Meta/WhatsApp:** os guias repetem o que já foi registrado: cobrança por mensagem, mensagem de serviço paga desde 01/10 e restrição a assistentes genéricos desde 15/01. O WhatsApp libera aos poucos o agendamento de mensagens para os usuários (20/11), um recurso do app comum, não da API.
- **Anvisa, ANPD, CFP, CFN, CFO, COFFITO, COFEN e Apple:** nada nas últimas 24 h.

## Pressão de preço

- **Escriba abaixo de R$ 49,90:**
  - Na psicologia, a Brainn Care custa R$ 29,90 no anual, até 15 sessões, e a Sinthoma tem plano grátis com 3 pacientes.
  - A Conclínica cobra R$ 1 por consulta, mas exige um plano de R$ 89 ou mais.
  - Continuam valendo os casos de antes: PsicoProntuários R$ 19,90, a Vedius na Black (até 30/11) e os grátis com limite.
- **Tudo-em-um:** Villo de R$ 249,90 a R$ 639,90 e Conclínica a partir de R$ 89 + escriba. O Calima a R$ 49,90 com teleconsulta segue barato.
- **Teleconsulta avulsa:** sem mudança.
- **Secretária por profissional:** **sim, agora há preço abaixo de R$ 99,90.** A Luna da Villo sai a partir de R$ 89,90 por clínica, mas só como extra de um plano de R$ 249,90 ou mais. Avulsa, a Certu custa R$ 349 por clínica.

## Comoditização

- **Escriba nativo em ERP:** a lista ganha a Conclínica (cobrada por uso) e a Villo (já nos planos). O escriba passou a ser cobrado por consulta, como um item de consumo.
- **Secretária no WhatsApp:** a Villo traz a Luna de série no plano Completo, e a Guia Odonto lançou a dela. Meta, n8n e big techs: nada novo.

## Posicionamento

- **(b) muda:** a âncora de mercado para a secretária vendida como extra é R$ 89,90 (Villo, por clínica), e não fica mais só nos R$ 350 ou mais da secretária avulsa. Recomendação: manter R$ 99,90 só se a página mostrar o total do Calima com a secretária (R$ 149,80) contra o mínimo da Villo (R$ 339,80). Se o add-on for vendido sozinho, testar R$ 89,90.
- **(a) sem mudança:** o plano único de R$ 49,90, ilimitado e com teleconsulta, segue defensável. A cobrança por uso da Conclínica só é mais barata para quem já paga o plano dela.
- **(c) sem mudança:** a psicologia é a profissão mais bem servida (Brainn, Sinthoma, Tríade, PsiNota, DocsPSI). A enfermagem segue como a aposta.

---
Checado hoje: 10 buscas (prontuário com IA, secretária no WhatsApp, rodadas, CFM, Black Friday, escribas globais, Meta/WhatsApp, teleconsulta avulsa, outras profissões, Anvisa/ANPD) e 12 páginas lidas (Conclínica, SoulClinic, Guia Odonto, Certu, PoliHealth, Escuta Med, Sinthoma, Brainn Care, Villo, Tríade psi, AI Brasil e TribeMD pela busca), com 3 prints. Calima conferido no repo.

Já registrados e não repetidos: PoliHealth (Black a R$ 49 por 2 meses, em 11/11), HiDoctor LIVE (o recurso novo de retomar a transcrição é pequeno), Pronova, Cloudia, Clinicorp Black, Vem Consulta, Vokkari, Life Up, Versatilis, Medcloud Laraa Max (radiologia) e Skedia.

Vistos sem preço público ou fora do foco: SoulScribe (SoulClinic, escriba SOAP, 7 dias grátis), Tríade psi (escriba só no plano Especialista de R$ 149), TribeMD Assist (Black via sindicato, sem preço legível) e Black Fridays de ERP sem escriba (Gestão Clinic, ClickClínicas, Clínica nas Nuvens).

Reserva: nenhuma página precisou de reserva. Nenhum número foi estimado.

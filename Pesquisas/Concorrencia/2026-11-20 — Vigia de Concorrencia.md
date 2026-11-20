---
title: Vigia de Concorrência — 2026-11-20
date: 2026-11-20
area: Concorrencia
tags: [concorrencia, mercado]
source: routine
aviso: enviado
---

## TL;DR

- **Aionmed** (nova, lançada em 03/11, no noticiário em 19/11): escriba + histórico do paciente alimentado pelo WhatsApp do médico. A partir de R$ 109/mês (R$ 99 no anual), 14 dias grátis. Mais que o dobro do Calima.
- **AgenteClin** (nova): secretária IA no WhatsApp a R$ 164/mês por profissional (anual, R$ 1.970). Os R$ 99,90 do add-on seguem abaixo do mercado.
- **CFM 2.454:** a ação da CNSaúde está em recurso no TRF1; estudo do Instituto Consenso (18/11) diz que 55% dos prestadores não conseguem se adequar no prazo. Atinge clínica, não o médico autônomo.
- Calima sem mudança (R$ 49,90). Recomendações mantidas.

> Comparado com o relatório de **2026-11-19**. Varredura completa: não (é sexta, e a última foi em 16/11). Só reabri as páginas que apareceram no noticiário.
> Calima conferido no repo (`origin/main` `be3cc06`): R$ 49,90 no site, `VENDAVEIS = ['staff']`, defaults 4990/4990.

## Achados

1. **Aionmed: escriba que junta o que o paciente manda pelo WhatsApp.**
   - **O que faz:** o médico encaminha exame, foto, áudio e mensagem do paciente para um número da Aionmed, e tudo cai no histórico. Na consulta, grava, transcreve e monta a nota para o médico aprovar. Também analisa exames com alertas ("LDL fora da meta"), traz um assistente que responde citando os registros do paciente, faz receita, atestado e pedido de exame com QR Code e alerta de interação. Cita a LGPD e a CFM 2.454 na capa.
   - **Preço (mensal / anual):** Básico R$ 109 / R$ 99 (1.000 créditos de IA, transcrição, exames, documentos, agenda). Essencial R$ 339 / R$ 279 (5.000 créditos, assistente, exames pelo WhatsApp, financeiro, 1 acesso da equipe). Profissional R$ 509 / R$ 379 (9.000 créditos, 3 acessos). Teste: 14 dias ou 1.000 créditos.
   - **Quem:** fundada por médico (Christian Felizola, clínico e cardiologista) e André Pacheco (CEO). Só para médicos. Diz que os dados não treinam a IA.
   Fontes: [aionmed.com.br](https://aionmed.com.br/), lida em 20/11/2026; [Estado de Minas, 19/11/2026](https://www.em.com.br/tecnologia/2026/11/7541634-startup-cria-ia-que-reune-exames-e-historico-de-pacientes-para-medicos.html); [TV SIM Brasil, 20/11/2026](https://tvsimbrasil.com.br/sp/sao-paulo/tecnologia/noticia/2026/11/20/startup-brasileira-ia-organizar-prontuario-pacientes). Primeira vez neste vigia.
   ![Aionmed, capa no celular](https://agente.cassiogon.tech/prints/02a8a27ce6202b78a0cda004cf8cd1e6.jpg)
   - **E daí pro Calima:** o escriba básico deles custa mais que o dobro do Calima e não tem teleconsulta nem portal. A ideia boa é o "encaminha pelo WhatsApp e vira prontuário", que conversa com a secretária que o Calima já tem. Já a análise de exame com alerta é justamente o que a Apple barrou no Calima como diagnóstico; se eles chegarem à App Store, vale ver como passaram.

2. **AgenteClin: secretária IA no WhatsApp com preço público por profissional.**
   - **Planos (anual, equivalente mensal):** Presença R$ 164 (R$ 1.970/ano), com 1 profissional, 1 WhatsApp e 1 Google Agenda, agenda, remarca, cancela, lembrete e entende áudio. Equilíbrio R$ 331 (até 4 profissionais). Domínio R$ 664 (até 8). O preço do plano mensal não aparece na página (só o anual).
   - **Como vende:** só entra no ar depois de a clínica testar as respostas; consulta só os horários livres, sem expor a agenda; não responde dúvida clínica nem urgência.
   Fonte: [agenteclin.com.br](https://agenteclin.com.br/), lida em 20/11/2026. Primeira vez neste vigia.
   ![AgenteClin, capa no celular](https://agente.cassiogon.tech/prints/aae77c31af54497c391ebb68d6ca89ad.jpg)
   - **E daí pro Calima:** mais uma âncora acima dos R$ 99,90 do add-on, e já com o pagamento anual. A frase "ativação só após testes" é boa de copiar no onboarding do piloto multi-médico.

## Regulação

- **CFM 2.454/2026: a ação subiu de instância.** A ação da CNSaúde, da Fenaess e do SBH aguarda julgamento de recursos no TRF1, e se limita às obrigações das instituições (comissão de IA e telemedicina, auditoria, avaliação de risco), não à ética do médico. O estudo do Instituto Consenso, lançado em 18/11 em Brasília, ouviu 43 organizações: 55% dos prestadores dizem que não conseguem se adequar no prazo, e 61% veem risco alto de sobreposição com o PL 2.338/2023 (multa de até 2% do faturamento, teto de R$ 50 milhões). Fonte: [consenso.org.br, 18/11/2026](https://consenso.org.br/estudo-do-instituto-consenso-analisa-os-desafios-de-adequacao-a-regulacao-da-inteligencia-artificial-na-saude-suplementar/). E daí: nada muda para o Calima hoje; o PL, se aprovado, é a peça que pode alcançar o fornecedor de software.
- **Meta/WhatsApp:** só repercussão da cobrança da mensagem de serviço desde 01/10 (O Tempo e Terra, 17/11), já registrada.
- **Anvisa, ANPD, CFP, CFN, CFO, COFFITO, COFEN e Apple:** nada novo na semana.

## Pressão de preço

- **Escriba:** nada novo abaixo de R$ 49,90. A Aionmed entra a R$ 99–109.
- **Tudo-em-um:** sem mudança.
- **Teleconsulta avulsa:** sem mudança no piso (R$ 39,90: Linkadoc, Consultar Médico).
- **Secretária por profissional:** nada abaixo de R$ 99,90. A AgenteClin cobra R$ 164 no anual.

## Comoditização

- Nenhum ERP passou a embutir escriba de graça além do que já foi registrado (Aura). A Meta, o n8n e as big techs não lançaram nada novo em pt-BR.

## Posicionamento

Sem mudança de recomendação.

---
Checado hoje:
- 8 buscas: escriba e prontuário com IA, secretária no WhatsApp, rodadas, CFM e telemedicina, teleconsulta avulsa, scribes globais, WhatsApp/Meta, conselhos e Anvisa, ERPs (iClinic, Feegow, Amplimed, Doctoralia, Simples Dental, Dietbox).
- 6 páginas: Estado de Minas (Aionmed), Aionmed (capa e preços), AgenteClin, Instituto Consenso e os 2 prints.

Já registrados e não repetidos: Aura, Klinity, Santé, Tivita, HiDoctor, THM Saúde, Teledoc, ClickSaúde, Linkadoc, LoopMed, Olá Doutor, Clara, Cloudia, Clinia, MEDC/Aiva, Darwin Saúde, Secretar.AI, The SecretárIA, Telepatia, Doctoralia Noa Evidence e Meta Business Agent. Fora do escopo: Skedia (rodada seed, financeiro de clínica), Tacchini (IA hospitalar interna) e Elsevier ClinicalKey AI (só EUA).

Reserva: nenhuma página precisou de reserva, tudo veio pelo agente web. Nenhum número foi estimado; os preços da Aionmed vieram da extração da página pelo agente web (as subpáginas /precos e /planos não existem).

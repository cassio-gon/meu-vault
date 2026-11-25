---
title: Vigia de Concorrência — 2026-11-25
date: 2026-11-25
area: Concorrencia
tags: [concorrencia, mercado]
source: routine
aviso: brief
---

## TL;DR

- **PsicoProntuários grava a sessão inteira e entrega a evolução por R$ 19,90/mês**, com 20 h de áudio por mês. O Pro, com 70 h, custa R$ 49,90, o mesmo preço do Calima. É o escriba mais barato deste vigia em um sistema completo.
- **A psicologia ganhou mais dois escribas:** Plenne (R$ 79,90, ou R$ 55,75/mês no anual, 25 h) e Tempo Refleto (Premium R$ 89,90, ilimitado). O PsicoManager publicou hoje uma ajuda sobre transcrever sessão do Google Meet.
- **Salux (Grupo Bringel) pôs o escriba da Telepatia no prontuário hospitalar INITIA.** É B2B de hospital e não mexe no preço do Calima.
- Calima sem mudança (R$ 49,90). Recomendações sem mudança: a psicologia confirma que está cheia.

> Comparado com o relatório de **2026-11-24**. **Varredura completa:** não (quarta; a última foi em 23/11). Reabertas só as páginas de quem apareceu no noticiário.
> Calima conferido no repo (`origin/main` `0ff5e06`): R$ 49,90 no site (7 ocorrências), `VENDAVEIS = ['staff']`, `PLANO_STAFF_CENTS` e `CONSULTA_AVULSA_CENTS` com default 4990.

## Achados

1. **PsicoProntuários: escriba de sessão a partir de R$ 19,90/mês.**
   - Grava a sessão de até 60 min, com autorização do paciente, transcreve e monta o registro para o psicólogo revisar. O processamento vai para uma fila e leva até 24 h. Tem agenda, financeiro, lembrete por WhatsApp (no número do próprio psicólogo), Carnê-Leão, site com agendamento, portal do paciente e um bot no Telegram. Funciona no navegador e como PWA.
   - **Preço:** Básico R$ 19,90 (20 h de sessão por mês), Pro R$ 49,90 (70 h, mais o "resumo por voz" ditado depois da sessão, com 10 h), Pro+ R$ 89,90 (120 h) e Super R$ 129,90 (150 h). O teste dura 14 dias sem cartão, com 2 h de áudio.

   Fonte: [psicoprontuarios.com.br](https://psicoprontuarios.com.br/), lida em 25/11/2026. Primeira vez neste vigia.
   ![PsicoProntuários, capa no celular](https://agente.cassiogon.tech/prints/89906da31a7c218dbedbe8065d417d5f.jpg)
   - **E daí pro Calima:** é a primeira vez que um sistema completo cobra menos da metade do Calima com escriba incluído. Mas ele só atende psicologia, entrega em até 24 h e não tem teleconsulta própria (usa Meet ou Zoom). O ditado depois do atendimento, que é o jeito do Calima, só aparece no plano de R$ 49,90.

2. **Plenne: psicologia com "prontuário com IA" em um plano só.**
   - Grava ou transcreve a sessão e a IA escreve o rascunho da evolução nos modelos SOAP, TCC, PEP e psicodinâmico. Também tem lembretes no WhatsApp 24 h e 2 h antes, que o paciente confirma com um toque, link de agendamento e financeiro. A capa diz "Novo: Prontuários com IA".
   - **Preço:** R$ 79,90/mês, ou R$ 669/ano (R$ 55,75/mês), com 25 h de transcrição por mês. O teste é de 5 dias, sem cartão.

   Fonte: [plenne.com.br](https://plenne.com.br/), lida em 25/11/2026. Primeira vez neste vigia.
   ![Plenne, capa no celular](https://agente.cassiogon.tech/prints/7e8e1d37371e908c9906e26298ae9521.jpg)
   - **E daí pro Calima:** a Plenne se vende como "sem secretária": o lembrete com confirmação vem incluso. É a mesma promessa do add-on Secretária, que no Calima seria vendida à parte.

3. **Tempo Refleto: escriba de psicologia que marca frase que ninguém disse.**
   - No Premium, grava a sessão (até 1h30, inclusive o áudio da aba do Meet no Chrome) e escreve o rascunho de evolução na abordagem escolhida (TCC, ACT, DBT e outras). Antes de entregar, confere cada frase com a transcrição: remédio, diagnóstico, risco ou número que não foram ditos ganham a marca [conferir]. O áudio é apagado depois da transcrição, e os nomes são retirados antes de o texto ir para a IA.
   - **Preço:** Premium R$ 89,90/mês ou R$ 899/ano, uso ilimitado "dentro do uso justo". São 15 dias de Premium grátis, sem cartão.

   Fonte: [temporefleto.com.br, transcrição com IA](https://www.temporefleto.com.br/psicologos/transcricao-de-sessao-com-ia), texto revisado em 21/11/2026 e lido em 25/11/2026. Primeira vez neste vigia.
   ![Tempo Refleto, transcrição no celular](https://agente.cassiogon.tech/prints/17b2086c2292a9c15df5f3e04d3dc2f7.jpg)
   - **E daí pro Calima:** é o mesmo discurso anti-alucinação e LGPD do Calima (nome fora antes da IA, áudio apagado, revisão obrigatória). Esse argumento já não é exclusivo. O que segue só do Calima é o texto final montado por código, sem a IA escrever.

4. **Salux leva o escriba da Telepatia para o prontuário hospitalar INITIA.**
   - A Salux, do Grupo Bringel, integrou a Telepatia ao INITIA, sua plataforma de gestão em saúde. O médico documenta enquanto conversa com o paciente, com os protocolos da instituição, e a direção ganha auditoria de prontuário e painel de adesão aos protocolos. É a primeira parceria do novo Programa de Parceiros da Salux. Preço não público.

   Fonte: [Medicina S/A, 24/11/2026](https://medicinasa.com.br/salux-e-telepatia/) (também no [Saúde Digital News, 23/11](https://saudedigitalnews.com.br/23/11/2026/salux-e-telepatia-levam-inteligencia-artificial-clinica-ao-prontuario-do-initia/)).
   - **E daí pro Calima:** é o escriba virando recurso nativo do prontuário de hospital, por parceria de canal. Fica no hospital e não chega ao plantonista que paga do bolso, que é o público do Calima.

5. **PsicoManager publicou ajuda sobre "Transcrição de Sessão com IA" pela extensão do Google Meet,** atualizada em 25/11/2026. A página só tem uma imagem, sem texto, então o preço e o plano não são públicos. Fonte: [central de ajuda do PsicoManager](https://core.psicomanager.com/central-de-ajuda/psicomanager/artigo/integracao-google-meet-transcricao-de-sessao-extensao), lida em 25/11/2026.
   - **E daí pro Calima:** se confirmar, o maior sistema de psicologia passa a ter escriba. Vale reabrir na varredura de segunda (30/11).

## Regulação

- **Nada novo.**
- **CFM 2.454/2026:** só guias e blogs repetindo o que já se sabe (em vigor desde 26/08/2026, uso da IA registrado no prontuário e informado ao paciente).
- **Meta/WhatsApp:** guias de 21 a 24/11 repetem a tabela de novembro (marketing R$ 0,32 e utilidade R$ 0,035 por mensagem entregue) e a franquia de 1.000 mensagens de serviço grátis.
- **Anvisa, ANPD, CFP, CFN, CFO, COFFITO, COFEN e Apple:** nada nas últimas 24 h.

## Pressão de preço

- **Escriba abaixo de R$ 49,90: há um novo.** PsicoProntuários Básico, R$ 19,90 com 20 h por mês, só para psicologia e com entrega em até 24 h. Continuam os de antes: NurseUp R$ 39,95 por 3 meses, Recinto grátis no beta, Ordexa R$ 39,90 com cota e Desler grátis dentro de R$ 159.
- **Tudo-em-um:** na psicologia, a faixa é de R$ 49,90 a R$ 89,90 com escriba (PsicoProntuários Pro, Plenne, Tempo Refleto). Para médico, os R$ 49,90 seguem baratos.
- **Teleconsulta avulsa:** sem mudança.
- **Secretária por profissional:** sem mudança desde ontem (XuzIA a R$ 99). A Plenne põe a confirmação de consulta pelo WhatsApp dentro de R$ 79,90, mas não é um assistente que conversa.

## Comoditização

- **Escriba como recurso nativo:** a Salux/INITIA, por parceria (hospital), e na psicologia quase todo sistema novo já nasce com gravação de sessão (PsicoProntuários, Plenne, Tempo Refleto e, pelo visto, o PsicoManager).
- **WhatsApp:** o app passou a liberar no Brasil o agendamento de mensagens para o consumidor (notícias de 24/11). Não substitui a secretária, que conversa e agenda.
- **Big techs:** nada novo em pt-BR.

## Posicionamento

- **Sem mudança de recomendação.**
- Os achados confirmam o que estava em (c): a psicologia está cheia, agora com escriba a R$ 19,90. A aposta segue na enfermagem de plantão.
- Para (a): o "sem a IA escrever o texto final" passa a ser o único argumento anti-alucinação que nenhum concorrente repete. O "nome sai antes da IA e o áudio é apagado" o Tempo Refleto também promete.

---
Checado hoje: 12 buscas (prontuário com IA, secretária no WhatsApp, rodadas, regulação, outras profissões, teleconsulta, Salux/Telepatia, Medcloud, Plenne, Meta/WhatsApp, escribas globais), 6 páginas lidas e 3 prints. Calima conferido no repo.

Já registrados e não repetidos: XuzIA, Maia, Hub Médica, Medics, MedScribe, Theravus (Black até 30/11), Aionmed, Aura, Telepatia (o produto em si). Fora: Medcloud Laraa Max (laudo de radiologia, lançada em 21/10).

Reserva: nenhuma página precisou de reserva. Nenhum número foi estimado.

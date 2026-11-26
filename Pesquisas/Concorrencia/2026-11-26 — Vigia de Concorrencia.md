---
title: Vigia de Concorrência — 2026-11-26
date: 2026-11-26
area: Concorrencia
tags: [concorrencia, mercado]
source: routine
aviso: brief
---

## TL;DR

- **O Consultório Fácil lançou a Lina, um escriba de R$ 39 por profissional por mês** que atende médico, psicologia, odontologia, fisioterapia, nutrição e enfermagem. Ela troca o nome do paciente por marcador antes da IA, não guarda o áudio e marca as doses que não foram ditas. Somada ao plano Básico, de R$ 29, fica em R$ 68, e o Básico não tem teleconsulta.
- **A fisioterapia já tem escriba:** a Vedius (mais de 20 mil fisioterapeutas) dita a evolução por voz com IA por R$ 79,90/mês. Na Black, o anual sai a R$ 45,83/mês até 30/11.
- **iazzo:** escriba, recepcionista de IA no WhatsApp e telemedicina numa plataforma só, para médico. O preço não é público.
- Calima sem mudança (R$ 49,90). Muda a recomendação (c): a fisioterapia saiu da lista de profissões sem escriba.

> Comparado com o relatório de **2026-11-25**. **Varredura completa:** não (quinta; a última foi em 23/11). Reabertas só as páginas de quem apareceu na busca.
> Calima conferido no repo (`origin/main` `2a062c8`): R$ 49,90 no site (7 ocorrências), `VENDAVEIS = ['staff']`, `PLANO_STAFF_CENTS` e `CONSULTA_AVULSA_CENTS` com default 4990.

## Achados

1. **Consultório Fácil: escriba "Lina" por R$ 39 por profissional, para seis profissões.**
   - Com o consentimento do paciente, a Lina escuta a consulta pelo microfone do aparelho e preenche o modelo de prontuário (SOAP, anamnese, evolução de sessão). Ela marca o que deve ser conferido (por exemplo, "Confirmar dose... que não foram ditas"), gera orientações ao paciente, pedido de exame e encaminhamento, e põe no registro a menção de que houve apoio de IA, como pede a CFM 2.454.
   - **Privacidade:** o áudio nunca é guardado. Nome, CPF, cartão SUS, telefone, e-mail e CEP viram marcadores antes de chegar à IA. O texto é apagado depois de salvo. A Lina também ignora ordens ditas durante a consulta.
   - **O que não faz:** não transcreve teleconsulta, não sugere diagnóstico nem conduta e fica de fora de atestado, receita e laudo.
   - **Preço:** R$ 39 por profissional por mês, somados a um plano pago: Básico R$ 29 (1 profissional, sem teleconsulta), Profissional R$ 39 (2 profissionais), Avançado R$ 119 (5 profissionais, com teleconsulta) e Enterprise R$ 229. O teste dura 7 dias, com 5 consultas transcritas.

   Fonte: [consultoriofacil.com.br, Lina](https://consultoriofacil.com.br/transcricao-de-consultas-com-ia) e [planos](https://consultoriofacil.com.br/planos), lidos em 26/11/2026. Primeira vez neste vigia.
   ![Consultório Fácil, Lina no celular](https://agente.cassiogon.tech/prints/9594d3294fd55b8f1d5ae595e5d244af.jpg)
   - **E daí pro Calima:** é a cópia mais próxima do discurso do Calima até agora: nome fora antes da IA, áudio descartado, marca no que não foi dito e várias profissões. O mínimo dela para 1 profissional sai em R$ 68, sem teleconsulta, e com teleconsulta passa de R$ 150. Nessa conta o Calima segue mais barato. O que só o Calima tem: o texto final montado por código e o uso no plantão.

2. **Vedius: escriba por voz para fisioterapia, com Black até 30/11.**
   - É um sistema para fisioterapeutas com agenda e lembrete no WhatsApp, financeiro, prescrição de exercício em vídeo e "prontuário completo por voz com IA" (o profissional dita os pontos da sessão e o sistema escreve a evolução). Diz ter mais de 20 mil fisioterapeutas.
   - **Preço:** Individual mensal R$ 79,90. Na Black, o anual à vista sai a R$ 549,90 (R$ 45,83/mês) e o anual em 12x a R$ 49,99. Equipe: R$ 69,90 por colaborador. São 7 dias grátis, sem cartão. A IA vem com uma cota mensal incluída, de tamanho não público.

   Fonte: [vedius.com.br/precos](https://vedius.com.br/precos/), lida em 26/11/2026. Primeira vez neste vigia.
   ![Vedius, capa no celular](https://agente.cassiogon.tech/prints/258f963a656bd85e17cf3ee8db34664b.jpg)
   - **E daí pro Calima:** em 23/11 este vigia anotou que a fisioterapia não tinha escriba (só o ZenFisio, sem transcrição). Isso caiu: o líder do nicho já dita por voz, e o anual da Black sai abaixo dos R$ 49,90.

3. **iazzo: escriba, recepcionista no WhatsApp e telemedicina para médico.**
   - O médico grava a consulta e a IA monta a nota no modelo de anamnese. Um assistente atende o WhatsApp da clínica 24 h, entende áudio, oferece horários e confirma. A assistente "Íris" opera o sistema pelo WhatsApp do médico (agenda, remarca, lança recebimento, sempre pedindo confirmação) e busca evidência no PubMed. A telemedicina tem sala de espera, e há app para o paciente.
   - **Preço:** não público. A demonstração é pedida pelo WhatsApp.

   Fonte: [iazzo.com.br](https://www.iazzo.com.br/), lida em 26/11/2026. Primeira vez neste vigia.
   - **E daí pro Calima:** é mais um pacote com escriba e secretária de WhatsApp juntos. A secretária deixa de ser um extra e vira item de série, o que pesa no preço do add-on.

4. **IntelliDoctor.ai acompanhou 2 mil atendimentos no PS do São Camilo Pompeia em seis meses.**
   - A iniciativa foi levada pela Hexa (TI), e os prontuários viraram painel de gestão. Preço não público.

   Fonte: [Saúde Digital News, 25/11/2026](https://saudedigitalnews.com.br/25/11/2026/em-seis-meses-ia-do-hospital-sao-camilo-acompanhou-2-mil-atendimentos-e-transformou-prontuarios-em-inteligencia-de-gestao/).
   - **E daí pro Calima:** a IA entra pelo pronto-socorro de hospital, vendida à instituição. Não chega ao plantonista que paga do bolso.

## Regulação

- **Nada novo.**
- **CFM 2.454/2026:** só guias e notas repetindo a regra (Portal Telemedicina em 24/11, Saúde Digital News em 25/11).
- **Meta/WhatsApp:** guias repetem a tabela de novembro. A decisão do Cade sobre chatbots de IA que voltou à busca é de 23/04/2026 e já foi registrada.
- **Anvisa, ANPD, CFP, CFN, CFO, COFFITO, COFEN e Apple:** nada nas últimas 24 h.

## Pressão de preço

- **Escriba abaixo de R$ 49,90:** a Vedius anual da Black sai a R$ 45,83/mês, só para fisioterapia e só até 30/11. A Lina custa R$ 39, mas exige um plano pago, e o mínimo fica em R$ 68 sem teleconsulta. Continuam valendo os casos de antes: PsicoProntuários R$ 19,90, NurseUp, Recinto, Ordexa e Desler.
- **Tudo-em-um:** para ter escriba e teleconsulta juntos no Consultório Fácil, são pelo menos R$ 158 (Avançado + Lina). Os R$ 49,90 do Calima seguem baratos.
- **Teleconsulta avulsa:** sem mudança (ClickSaúde a R$ 49,90; a tabela da THM vai de R$ 29,97 a R$ 59,90).
- **Secretária por profissional:** nada novo com preço público. O iazzo inclui a secretária, sem preço.

## Comoditização

- **Escriba como recurso nativo de ERP:** o Consultório Fácil (add-on de R$ 39) e a Vedius (incluída no plano) entram na lista. ERP pequeno e vertical já vem com escriba.
- **WhatsApp e big techs:** nada novo.

## Posicionamento

- **(c) muda:** a fisioterapia saiu da lista de "menos servidas" (Vedius e Lina). A enfermagem segue como a aposta: a Lina cita enfermagem só de passagem, e ninguém atende o plantão.
- **(a) sem mudança:** os R$ 49,90 com teleconsulta seguem defensáveis. A Lina mostra que "nome fora antes da IA, áudio descartado e marca no que não foi dito" virou padrão, e só o texto montado por código segue exclusivo do Calima.
- **(b) sem mudança.**

---
Checado hoje: 12 buscas (prontuário com IA, secretária no WhatsApp, rodadas, CFM, Black Friday, outras profissões, escribas globais, teleconsulta, Meta/WhatsApp, Vedius, iazzo, Aionmed), 8 páginas lidas e 2 prints. Calima conferido no repo.

Já registrados e não repetidos: Memed (R$ 80 mi), Skedia, Avie, Super Márcia, SophiaCRM, MEDX Medbot, Amplimed Amélia, Aura, Aionmed, 4Medic (Black 40% no anual), Heidi (a rodada de US$ 340 mi é de setembro), Cade × Meta (abril). Fora: Medcloud Laraa Max (radiologia), Matria (copiloto hospitalar, outubro).

Reserva: nenhuma página precisou de reserva. Nenhum número foi estimado.

---
title: Vigia de Concorrência — 2026-11-19
date: 2026-11-19
area: Concorrencia
tags: [concorrencia, mercado]
source: routine
aviso: enviado
---

## TL;DR

- **Anthoia Cuidar** (novo no vigia): tudo-em-um multiprofissional com escriba. Base R$ 79/prof/mês; transcrição +R$ 89, teleconsulta +R$ 49. Voz + teleconsulta + portal saem a R$ 236 (R$ 189 no anual).
- **The SecretárIA** (novo): secretária IA no WhatsApp a partir de R$ 250/mês (100 pacientes). Âncora confortável para os R$ 99,90 do add-on.
- **Teledoc** e **ClickSaúde**: pronto-atendimento avulso a R$ 49,90, empatado com o Calima. O piso segue R$ 39,90 (Linkadoc, Consultar Médico).
- ElevenLabs lançou o Scribe v3 / v3 Live (STT, US$ 3,33 por mil min). Calima sem mudança (R$ 49,90). Recomendações mantidas.

> Comparado com o relatório de **2026-11-18**. Varredura completa: não (é quinta, e a última foi em 16/11). Só reabri as páginas que apareceram no noticiário.
> Calima conferido no repo (`origin/main` `8ef63da`): R$ 49,90 no site, `VENDAVEIS = ['staff']`, defaults 4990/4990.

## Achados

1. **Anthoia Cuidar: prontuário multiprofissional com transcrição, montado por módulos.**
   - **Preço por profissional/mês:** base Essencial R$ 79 (pacientes ilimitados, agenda, prontuário, Memed, sigilo por profissional). Módulos: transcrição +R$ 89 (até 200 h/mês), teleconsulta +R$ 49, portal do paciente +R$ 19, lembretes WhatsApp +R$ 19 (300 msgs), exames com IA +R$ 39. Exemplo deles: "Clínica multidisciplinar com IA" a R$ 216. Anual com 20% de desconto. 14 dias grátis sem cartão.
   - **Como funciona o escriba:** envia o áudio gravado, recebe rascunho por categorias, revisa antes de salvar; consentimento por finalidade.
   - **Público:** psicologia, fono, nutrição e medicina no mesmo paciente.
   Fonte: [anthoia.com.br/precos](https://anthoia.com.br/precos), lida em 19/11/2026. Primeira vez neste vigia.
   ![Anthoia, preços por módulo](https://agente.cassiogon.tech/prints/8966082786b7c379fbbb3dbd8b588b80.jpg)
   - **E daí pro Calima:** voz + teleconsulta + portal custam R$ 79 + 89 + 49 + 19 = R$ 236 lá (ou ~R$ 189 no anual) contra R$ 49,90 no Calima. Bom argumento de preço para as outras profissões; o ponto deles que o Calima não tem é o sigilo por profissional dentro de equipe.

2. **The SecretárIA: secretária IA no WhatsApp por crédito de uso, a partir de R$ 250/mês.**
   - **Planos:** Tester R$ 250 (~100 pacientes), Starter R$ 900 (~900, "consultórios médicos"), Pro R$ 1.300, Ultra R$ 2.000, Enterprise R$ 3.500. O plano é crédito de IA; acabou o crédito, a assistente para de responder.
   - **O que faz:** Google Agenda, lembrete de véspera, fila de espera para vaga que abre, entende áudio, imagem e PDF, responde em áudio, campanhas de aniversário e avaliação no Google. Conecta pela API oficial da Meta (mensagem cobrada da clínica) ou por QR Code (com aviso de risco de bloqueio).
   - **Em construção:** ligação com IA e transcrição da consulta para o prontuário.
   Fonte: [thesecretaria.com/planos](https://thesecretaria.com/planos), lida em 19/11/2026. Primeira vez neste vigia.
   ![The SecretárIA, planos](https://agente.cassiogon.tech/prints/881ee0011ee77be52f02261f4730e8ef.jpg)
   - **E daí pro Calima:** reforça que R$ 99,90 por profissional fica abaixo do mercado. A "fila de espera que oferece a vaga desmarcada" é um recurso barato de copiar e com valor claro para o add-on.

3. **Teledoc e ClickSaúde: pronto-atendimento por vídeo avulso a R$ 49,90.**
   - **Teledoc:** "pronto-atendimento online 24 horas por R$ 49,90, sem mensalidade" (título e descrição do site; a página carrega por JavaScript e não abriu o detalhe). [teledoc.med.br](https://teledoc.med.br/), 19/11/2026.
   - **ClickSaúde:** "consulta médica a partir de R$ 49,90, sem assinatura", Pix ou cartão, 24 h, atestado ICP-Brasil no WhatsApp. [assine.clicksaude.com.br](https://assine.clicksaude.com.br/medico-que-da-atestado), 19/11/2026.
   - **Médico Online Saúde** (BH): avulso não público na página; plano a partir de R$ 39,90/mês (R$ 29,90 no anual) com pronto-atendimento ilimitado, psicólogo a R$ 49,90. [medicoonlinesaude.med.br](https://medicoonlinesaude.med.br/), 19/11/2026.
   - **E daí pro Calima:** o avulso do Calima está no preço médio do pronto-atendimento, mas entrega o médico do próprio paciente. Reforça a nota de ontem: vender "consulta com o seu médico".

4. **ElevenLabs: Scribe v3 e Scribe v3 Live (anúncio de 12/11).**
   - Cerca de 25% menos erro de palavra que a versão anterior, 102 idiomas, vocabulário personalizado com milhares de termos, diarização em tempo real. Preço de referência US$ 3,33 por mil minutos, mais lento que Microsoft e xAI.
   Fonte: [aibrasil.ai](https://aibrasil.ai/saude/elevenlabs-lanca-modelo-de-voz-que-entende-quando-o-paciente-fez-uma-pausa-para), de ~13/11/2026, que cita o The Decoder. Preço não conferido na página oficial.
   - **E daí pro Calima:** junto com o MAI-Transcribe-2 de ontem, há duas alternativas de STT com vocabulário médico. O vocabulário customizado (nomes de remédio) é o que o Groq Whisper não tem; vale um teste de WER em ditado real.

## Regulação

- **CFM 2.454/2026:** só artigos de opinião (O Diário de Curitiba, 17/11; Evalmind, 17/11). Nada oficial novo.
- **Meta/WhatsApp:** só repercussão da cobrança da mensagem de serviço desde 01/10, já registrada.
- **Anvisa, ANPD, CFP, CFN, CFO, COFFITO, COFEN e Apple:** nada novo.

## Pressão de preço

- **Escriba:** nada novo abaixo de R$ 49,90. A Anthoia cobra R$ 168/prof só por base + transcrição.
- **Tudo-em-um:** a Anthoia deixa os R$ 49,90 do Calima baratos para quem quer voz + teleconsulta.
- **Teleconsulta avulsa:** sem mudança no piso (R$ 39,90). Teledoc e ClickSaúde entram empatados a R$ 49,90.
- **Secretária por profissional:** nada abaixo de R$ 99,90. The SecretárIA começa em R$ 250.

## Comoditização

- **STT:** ElevenLabs Scribe v3 entra na disputa com o motor da Microsoft. Nenhum dos dois é produto clínico em pt-BR.
- **ERPs:** nenhum passou a embutir o escriba de graça. A Unimed (EmTech, iMasters, 17/11) disse que centraliza a IA de prontuário num sistema próprio para 337 cooperativas, sem detalhe de produto.

## Posicionamento

Sem mudança de recomendação.

---
Checado hoje:
- 10 buscas: escriba, secretária, rodadas, regulação, Unimed, teleconsulta, escriba por profissão, WhatsApp/Meta, scribes globais e ERPs.
- 9 páginas: The SecretárIA (home e planos), Anthoia (home e preços), Teledoc, ClickSaúde, Médico Online Saúde, AI Brasil (ElevenLabs) e os 2 prints.

Já registrados e não repetidos: Aura, Analu, FluKAI, Clinia, MEDC, Darwin Saúde, Cloudia, Clara, NAIA, SmartDoctor, HiDoctor, Dora Health, Consulta+, LoopMed, Linkadoc, Meta Business Agent, Voa (1 milhão de consultas) e Doctoralia Noa Evidence. Fora do escopo: Skedia, Tacchini e Samel (IA hospitalar interna).

Reserva: nenhuma página precisou de reserva, tudo veio pelo agente web. Nenhum número foi estimado; a soma do pacote Anthoia é conta sobre os preços da página.

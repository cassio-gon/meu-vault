---
title: Vigia de Concorrência — 2026-11-14
date: 2026-11-14
area: Concorrencia
tags: [concorrencia, mercado]
source: routine
aviso: enviado
---

## TL;DR

- Desde 10/11, o **Amplinutri** (prontuário de nutrição) grava e transcreve a consulta e escreve o resumo. O plano grátis vai até 5 pacientes, e o Pro custa R$ 99/mês (R$ 74,25 na Black Friday). Com isso, a nutrição deixa de ser a profissão sem escriba.
- A **AxônioMed** cobra a partir de R$ 800/mês pela secretária IA no WhatsApp, para um médico, com a tarifa da Meta incluída. É mais uma âncora alta para os R$ 99,90 do add-on.
- A **Telemedico.med.br** é um marketplace de teleconsulta sem mensalidade. A consulta mínima é de R$ 40, e a plataforma fica com 25%.
- A regulação não mudou.

> Comparado com o relatório de **2026-11-12**. Não houve relatório em 13/11. **Varredura completa:** não. Hoje é sábado, e a última completa foi em 09/11, há 5 dias. Só foram abertas as páginas que apareceram no noticiário.
> Calima conferido no repo (`origin/main` `73c6d02`): o `site/index.html` segue com R$ 49,90 (7 ocorrências) e `VENDAVEIS` continua `['staff']`. No `env.js`, só mudou um comentário (ntfy → Iluminat). Nenhum preço mudou.

## Achados

1. **Amplinutri põe escriba na nutrição.** O Amplinutri lançou "nove ferramentas de IA" dentro do prontuário:
   - gravação e transcrição da consulta, no consultório ou por vídeo, com resumo no formato que a nutricionista pedir;
   - leitura de laudo laboratorial, de bioimpedância e de DXA;
   - leitura de rótulo;
   - tradução do plano alimentar;
   - imagem da refeição;
   - reescrita de texto.

   Os planos são o **Gratuito** ("para sempre", até 5 pacientes) e o **Pro a R$ 99/mês**, com 25% de desconto na Black Friday até 30/11, o que dá **R$ 74,25/mês** (R$ 891 no anual). A página não diz se a IA tem cota ou custo à parte: isso é não público. Fonte: [amplinutri.com/novidades/a-ia-chegou-no-amplinutri](https://amplinutri.com/novidades/a-ia-chegou-no-amplinutri) (10/11/2026) e [amplinutri.com](https://amplinutri.com/), lidos em 14/11/2026. É a primeira vez que o Amplinutri aparece neste vigia.
   ![Amplinutri, a IA chegou](https://agente.cassiogon.tech/prints/b2d6eeb307cc9a3a5f21608cc4efb556.jpg)
   - **E daí pro Calima:** a nutrição era a aposta (c) por ser a menos servida. Agora ela tem escriba dentro de um ERP vertical que custa R$ 74–99. O Calima ainda sai pela metade do preço, mas não tem plano alimentar nem as tabelas de alimentos. A janela da nutrição está se fechando.

2. **AxônioMed: secretária IA no WhatsApp a partir de R$ 800/mês por médico.** A empresa tem uma página por especialidade (a de urologia é de 11/11) e três faixas de preço, todas "a partir de":
   - **Consultório:** R$ 800/mês, para 1 médico
   - **Clínica:** R$ 1.200/mês, de 2 a 4 profissionais
   - **Rede:** R$ 2.800/mês

   A IA e a tarifa da Meta por conversa estão dentro da mensalidade. Não cobra implantação nos casos típicos, e o valor exato sai na demonstração. A integração com a agenda cobre 41 sistemas (iClinic, Feegow, Amplimed, Doctoralia, entre outros). A IA "nunca interpreta exame", e o caso que ela publica é a conversão no WhatsApp passando de 23,3% para 31,2%. Fonte: [axoniomed.com.br/precos](https://axoniomed.com.br/precos/) (atualizada em 30/10/2026) e [/ia-para-urologista](https://axoniomed.com.br/ia-para-urologista/), lidas em 14/11/2026.
   ![AxônioMed, preço](https://agente.cassiogon.tech/prints/56f71bc4677040a9268b25068a1e12d4.jpg)
   - **E daí pro Calima:** é mais uma âncora alta. Para um médico só, ela fica acima da Aria (R$ 449–649). A AxônioMed cita "planos self-service de R$ 149 a R$ 249" como alternativa barata. Os R$ 99,90 do add-on seguem abaixo de tudo. A promessa de a tarifa da Meta vir incluída merece ser copiada na oferta.

3. **Telemedico.med.br: marketplace de teleconsulta sem mensalidade.** O médico entra de graça, com o CRM conferido um a um, e define o próprio preço, com **mínimo de R$ 40**. A plataforma fica com **25%** de cada consulta, o repasse é por Pix e há agenda própria sem custo para os pacientes do próprio médico. A plataforma tem 380 médicos em 24 estados (dados de 10/11) e já inclui prontuário, receita ICP e sala de vídeo no navegador. Fonte: [telemedico.med.br/para-medicos](https://telemedico.med.br/para-medicos/), lida em 14/11/2026.
   - **E daí pro Calima:** do lado do paciente, abre teleconsulta avulsa a partir de R$ 40, abaixo dos R$ 49,90. Do lado do médico, o modelo "grátis, pago só quando atende" compete com o plano mensal de quem atende pouco por vídeo.

4. **Plenia Bem-Estar: escriba multiprofissão com medição pelo celular.** A Plenia ouve a consulta, separa quem falou o quê e sugere cada campo. Cada sugestão vem com o trecho da fala que a sustenta, e a IA sugere CID. O Tricorder usa o celular para medir goniometria, repetições e postura, para fisioterapia, nutrição e estética. A ficha muda por profissão, e há teste de 15 dias sem cartão. O preço dos planos Solo e Clínica não é público. Fonte: [plenia.top](https://www.plenia.top/), lida em 14/11/2026.
   - **E daí pro Calima:** a fisioterapia também ganha um escriba de nicho. A sugestão de CID, que o Calima tirou por causa da Apple e da Anvisa, aparece aqui como recurso, mas só na web.

**Sem efeito no Calima:**
- A Telepatia, parceira da Aura, falou na FISWeek Rio em 13/11 ([Brasil Inovador](https://brasilinovador.com.br/telepatia-projeta-avanco-de-inteligencia-artificial-clinica-em-debate-na-fisweek-rio/)). Não houve preço nem produto novo.
- A Lidera Health tem prontuário, teleconsulta e a assistente "Sophia" no WhatsApp, mas é nicho de cannabis.
- A PsicoManager atualizou em 14/11 o artigo de ajuda sobre a extensão de transcrição no Google Meet. A IA ilimitada segue só no plano Individual Plus.

## Regulação

- **CFM 2.454/2026:** só conteúdo de blog (Cliniq+, termos de uso da Lidera), sem fato novo.
- **WhatsApp/Meta:** só guias sobre a tabela de 1º/10/2026, que já estava registrada em 08–09/11. Nada novo.
- **Anvisa, ANPD, CFP, CFN, CFO, COFFITO, COFEN e Apple:** nada novo desde 12/11.

## Pressão de preço

- **Escriba abaixo de R$ 49,90:** os grátis com limite ganharam mais um, o Amplinutri (até 5 pacientes, para nutrição). A Aura segue grátis e sem cota aparente. O Pro do Amplinutri (R$ 74,25–99) fica acima do Calima.
- **Teleconsulta avulsa:** a Telemedico permite consulta a partir de R$ 40, abaixo dos R$ 49,90. A THM segue em R$ 49,90.
- **Secretária por profissional:** a AxônioMed cobra R$ 800 ou mais. O piso avulso segue em R$ 147 (AgendaCare).

## Comoditização

Os ERPs verticais estão embutindo o escriba como recurso nativo: o Amplinutri na nutrição e o PsicoManager na psicologia (este só no plano Plus). Meta, n8n e as big techs não mudaram nada desde 12/11.

## Posicionamento

A recomendação (c) muda. As recomendações (a) e (b) seguem iguais.

- **(a)** Sem mudança: R$ 49,90 com o argumento "seus dados não viram produto" diante da Aura.
- **(b)** Sem mudança: R$ 99,90 segue muito abaixo do mercado (de R$ 147 a mais de R$ 800). Vale considerar "tarifa da Meta inclusa" na oferta.
- **(c)** A nutrição já tem escriba no ERP dela (Amplinutri), e a fisioterapia tem a Plenia. A sugestão é reavaliar na varredura de segunda (16/11), conferindo se a **enfermagem** é hoje a menos servida em pt-BR. Até lá, não abrir campanha só para nutrição.

---
Ferramentas: o agente web atendeu tudo (8 buscas, 9 páginas, 2 extrações e 2 prints). Nenhuma página precisou de reserva. Nenhum número foi estimado.

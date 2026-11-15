---
title: Vigia de Concorrência — 2026-11-15
date: 2026-11-15
area: Concorrencia
tags: [concorrencia, mercado]
source: routine
aviso: enviado
---

## TL;DR

- O **Ordexa** vende prontuário com escriba por IA a **R$ 39,90/mês** (R$ 10 abaixo do Calima), para médico e mais 6 profissões, e tem plano **grátis até 50 pacientes** (30 ações de IA por mês). Pela primeira vez, alguém cobra menos que o Calima por uma assinatura paga com escriba.
- A **PixelJarbas** cobra **R$ 197/mês** pela secretária no WhatsApp de consultório solo, com a tarifa da Meta à parte (até 31/12, o plano Plus sai por R$ 197 em vez de R$ 397). É mais uma referência acima dos R$ 99,90 do add-on.
- Na psicologia, o **Cuidaty** tem escriba só no plano Plus, a R$ 159,90/mês.
- A regulação não mudou.

> Comparado com o relatório de **2026-11-14**. **Varredura completa:** não. Hoje é domingo, e a última completa foi em 09/11, há 6 dias. A próxima é na segunda, 16/11. Só foram abertas as páginas que apareceram no noticiário.
> Calima conferido no repo (`origin/main` `c7afe78`): o `site/index.html` segue com R$ 49,90 (7 ocorrências) e `VENDAVEIS` continua `['staff']`. Nenhum preço mudou.

## Achados

1. **Ordexa: escriba por IA a R$ 39,90 e plano grátis para sempre.** É um prontuário eletrônico para médico, psicólogo, nutricionista, fisioterapeuta, dentista, fonoaudiólogo e veterinário. O profissional grava ou dita a consulta, a IA monta um rascunho em SOAP (ou DAP, BIRP ou o modelo do profissional), e ele revisa antes de salvar. Segundo o site, o áudio é apagado depois da transcrição e a IA não treina com os dados.

   | Plano | Preço | O que inclui |
   |---|---|---|
   | Grátis | R$ 0, sem prazo | até 50 pacientes, 1 usuário, 30 ações de IA por mês |
   | Consultório | R$ 39,90/mês ou R$ 399/ano | pacientes ilimitados, 3 usuários, 50 ações de IA por dia |
   | Clínica | R$ 69,90/mês ou R$ 699/ano | 8 usuários, 50 ações de IA por dia |

   Os 10 primeiros dias têm tudo liberado, sem cartão. Há lembrete pelo WhatsApp (não é secretária) e sala de vídeo em beta. Pagamento por Pix ou cartão, sem fidelidade. A página para médicos é de cerca de 10/11. Fonte: [ordexa.com.br/sistema-para-medicos](https://ordexa.com.br/sistema-para-medicos/) e [ordexa.com.br](https://ordexa.com.br/), lidas em 15/11/2026. É a primeira vez que o Ordexa aparece neste vigia.
   ![Ordexa, grátis até 50 pacientes](https://agente.cassiogon.tech/prints/13cea37960ab59b970e0ceaaa538103a.jpg)
   - **E daí pro Calima:** o discurso do Ordexa é quase o do Calima (rascunho revisado, áudio apagado, nada de treino), por R$ 10 a menos e com 3 usuários. O Calima ainda leva vantagem no ditado campo a campo com campo vazio destacado, no nome cifrado no aparelho, na teleconsulta pronta, no plantão e no app iOS. O preço deixa de ser argumento: a venda passa a depender desses diferenciais.

2. **PixelJarbas: secretária no WhatsApp para o consultório solo a partir de R$ 197/mês.** O plano Essential custa R$ 197/mês (até 500 pacientes diferentes por mês) e o Plus, R$ 397 (até 1.500). Na promoção de fim de ano, quem contratar até 31/12/2026 leva o Plus por R$ 197, com o preço travado por 12 meses. Não cobra implantação, não tem fidelidade nem teste grátis, e oferece garantia de 30 dias. A tarifa da Meta é à parte, no cartão do consultório, com estimativa de R$ 0 a 30/mês para quem atende sozinho (cerca de R$ 0,035 por mensagem de serviço acima de 1.000). A secretária não ouve áudio nem lê foto. O alvo declarado é psicologia, fisioterapia, fonoaudiologia, nutrição e odontologia. Fonte: [pixeljarbas.com.br/precos](https://www.pixeljarbas.com.br/precos), lida em 15/11/2026. A Cloudia publicou um comparativo com ela em 12/11 ([cloudia.com.br](https://cloudia.com.br/cloudia-ou-pixeljarbas-para-clinicas-qual-escolher/)).
   ![PixelJarbas, preços](https://agente.cassiogon.tech/prints/c1a98a77e34bcd342d514e602dc3b117.jpg)
   - **E daí pro Calima:** é o concorrente mais parecido com o add-on, porque mira o profissional solo, e mesmo assim cobra o dobro dos R$ 99,90. A secretária do Calima entende áudio (a da PixelJarbas não), o que vale pôr na oferta.

3. **Cuidaty: escriba para psicologia só no plano mais caro.** O plano Gratuito vale até 10 pacientes. O Básico custa R$ 69,90 e o Premium, R$ 89,90 (WhatsApp e assistente "Cuty AI"). A transcrição e o resumo da sessão, presencial ou por vídeo, ficam só no Plus, a **R$ 159,90/mês**. Os planos pagos têm 3 dias de teste. Fonte: [cuidaty.com](https://cuidaty.com/), lida em 15/11/2026.
   - **E daí pro Calima:** na psicologia, o escriba ainda custa caro (PsicoManager no Plus, Cuidaty a R$ 159,90). Os R$ 49,90 do Calima são competitivos ali, mas o Ordexa já oferece a mesma coisa a R$ 39,90.

**Sem efeito no Calima:**
- A Santé Sistemas faz Black November (cupom BLACK2026: paga 12 meses e usa até 14) e tem transcrição por IA no prontuário. O preço não é público ([santesistemas.io/transcricao-ia](https://www.santesistemas.io/transcricao-ia)).
- A ClickSaúde vende consulta avulsa 24h com clínico geral por R$ 49,90, o mesmo preço do Calima. A informação veio do trecho da busca no Reclame Aqui; a página não abriu.
- A Microsoft mudou a interface do Dragon Copilot em 10/11 ([Microsoft Learn](https://learn.microsoft.com/en-us/industry/healthcare/dragon-copilot/whats-new/new-ui)). Continua sem pt-BR para o Brasil.
- O dr.consulta limitou a autonomia da IA nas decisões clínicas, uma notícia institucional de 10/11 ([TI Inside](https://tiinside.com.br/10/11/2026/dr-consulta-limita-autonomia-da-ia-em-decisoes-clinicas-para-preservar-seguranca-dos-pacientes/)). Não houve preço nem produto novo.
- Psidigital (psicologia, Google Play), Clinu e OnlineClinic anunciam transcrição por IA sem data nova nem preço lido hoje. Ficam para a varredura de segunda.

## Regulação

- **CFM 2.454/2026:** só conteúdo de blog e redes sociais, sem fato novo. O CFM faz um webinar de reumatologia em 19/11 que inclui IA e telemedicina.
- **WhatsApp/Meta:** só guias sobre a cobrança por mensagem de 1º/10/2026, já registrada. Nada novo.
- **Anvisa, ANPD, CFP, CFN, CFO, COFFITO, COFEN e Apple:** nada novo desde 14/11.

## Pressão de preço

- **Escriba abaixo de R$ 49,90:** **sim, agora pago também.** O Consultório do Ordexa custa R$ 39,90, com IA de até 50 ações por dia. Entre os grátis com limite estão o Ordexa (50 pacientes, 30 ações de IA por mês), o Amplinutri (5 pacientes) e a Aura.
- **Tudo-em-um:** o Ordexa dá prontuário, agenda e vídeo em beta por R$ 39,90. Os R$ 49,90 do Calima só se justificam pelos diferenciais (iOS, plantão, privacidade no aparelho, teleconsulta pronta).
- **Teleconsulta avulsa:** a ClickSaúde cobra R$ 49,90, igual ao Calima. O piso segue na Telemedico (R$ 40).
- **Secretária por profissional:** a PixelJarbas cobra R$ 197 mais a tarifa da Meta. O piso avulso segue em R$ 147 (AgendaCare).

## Comoditização

O escriba virou recurso de prontuário barato: o Ordexa o inclui até no plano grátis. A Meta, o n8n e as big techs não mudaram nada para o Brasil desde 14/11.

## Posicionamento

A recomendação (a) muda; as outras seguem iguais.

- **(a)** O plano de R$ 49,90 ainda se defende, mas não pelo preço. A página do Calima deveria dizer, contra o Ordexa, o que ele não tem: **"nome do paciente cifrado no seu aparelho"**, **"campo não ditado fica vazio"**, **app na App Store** e **teleconsulta incluída**. Vale avaliar na varredura de segunda se o teste de 7 dias com 3 prontuários por dia perde para o "grátis até 50 pacientes".
- **(b)** Sem mudança: os R$ 99,90 seguem abaixo de tudo (PixelJarbas R$ 197, AgendaCare R$ 147, AxônioMed R$ 800). Diferencial a anunciar: a secretária entende áudio.
- **(c)** Sem mudança: reavaliar na segunda.

---
Ferramentas: o agente web atendeu tudo (8 buscas, 1 extração de 5 páginas e 2 prints). Nenhuma página precisou de reserva. Uma página (Reclame Aqui/ClickSaúde) falhou em todas as fontes, e o Firecrawl cloud estava sem crédito até 16/11. Nenhum número foi estimado.

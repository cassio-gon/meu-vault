---
title: Follow-up B2B — 2026-09-28
date: 2026-09-28
area: B2B
tags: [b2b, followup]
source: routine
---

# Follow-up da semana — 28/09/2026

## TL;DR

🚨 **10º relatório consecutivo sem nenhum disparo — mesmo estado exato de 14/09, valor a valor** (e a
rotina pulou a leitura de 21/09: sem commit, sem relatório naquela semana). 19 parados · 2 quentes ·
0 marcados Frio (automaticamente) · 3 mais urgentes: **Pâmella Braggion** (respondeu há 75 dias,
resposta simples ainda não enviada), **Leonice Castro** (pediu preço há 76 dias, reabertura pelo
piloto não enviada) e a **decisão sobre o formato desta rotina, pedida em 17/08 e repetida toda
semana desde então, agora sem resposta há 6 semanas (42 dias).**

---

## O que mudou desde 14/09: nada

Comparei as 3 colunas de rastreio (`Ultimo_contato`/`Ultimo_toque`/`Proximo_toque`) dos 8 CSVs
(incluindo `leads-raio20km-rj.csv`) e o painel `contatos-realizados.md` com a leitura de duas
semanas atrás — **idênticos, campo a campo**. `contatos-realizados.md` segue com o cabeçalho
"Atualizado em 2026-07-15"; os checkboxes de Pâmella e Leonice continuam desmarcados; "Entregues" e
"Lidos" do placar NUTRI seguem em branco. O único commit no repo `claude-config` que tocou esta
pasta desde 14/09 foi um auto-sync (`2619a37`, 22/09) que só formalizou no git arquivos que já
existiam — conferido diff a diff, sem mudança de conteúdo. **A leitura de 21/09 não aconteceu**
(não há relatório nem commit dessa data) — vale confirmar se o gatilho da rotina falhou naquela
segunda. Não repito os 12 textos por extenso pela 10ª vez — eles não mudaram nem precisam mudar
(nenhum sinal novo apareceu) — estão prontos e reusáveis em **`2026-08-17 — Follow-up B2B.md`**
(mesma pasta) e nos arquivos-fonte indicados abaixo. O que muda esta semana é só a idade de cada
item.

---

## Quentes (responderam) — ação hoje

### 🎯 Dra. Pâmella Braggion (NutriClin) — Ilha · wa.me/5521993964481

Respondeu em 15/07 às 16h19, 5 minutos após o Toque 0: *"não entendi nada rs"*. **75 dias de
silêncio numa conversa que ela mesma abriu.** Texto de resposta pronto, nunca marcado como enviado,
pela 10ª semana:

> Bom dia, Dra. Pâmella! Falha minha, compliquei demais rs. Simplificando: é uma secretária virtual
> pro WhatsApp do consultório. A paciente manda mensagem, ela responde na hora, marca a consulta e
> depois confirma o retorno. Tudo sozinha, mesmo quando a Dra. está atendendo. O jeito mais fácil de
> entender é ver: manda um "oi" pro (21) 99362-6483 e conversa com ela como se fosse uma paciente
> marcando horário. Leva um minuto.

*(`abordagem-nutri.md`, seção A1 — reusado sem alteração.)*

### 🎯 Leonice Castro — Caxias · wa.me/5521993171367

Perguntou o preço em 14/07, recebeu a cotação (sem piloto) e sumiu. **76 dias parada.**

> Leonice, sobre o valor que passei: acho melhor você ver funcionando do que decidir pelo número.
> Posso deixar a IA rodando 7 dias no seu WhatsApp, sem custo, pra você testar. Se não for pra você,
> é só me dizer. Preparo?

*(`abordagem-nutri.md`, seção B7/objeção de preço — reusado sem alteração.)*

---

## Follow-ups prontos → onde estão (12, teto semanal — inalterados)

Todos os textos seguem válidos e copiáveis diretamente de **`2026-08-17 — Follow-up B2B.md`**
(seção "Follow-ups prontos"), agora com 14 dias a mais de atraso cada (pulamos a leitura de 21/09):

| # | Lead | Praça | Toque devido | Dias parado hoje |
|---|---|---|---|---|
| 1 | Centro Médico CEMMA | Caxias | T2 (T1 nunca chegou — e-mail quicou) | 91 |
| 2 | Fisiomed Caxias | Caxias | T3 (presencial/voz) | 88 |
| 3 | CMPK – Pres. Kennedy | Caxias | T3 (presencial/voz) | 88 |
| 4 | ProntoAme | Caxias | T3 (presencial/voz) | 88 |
| 5 | Vitória Saúde (ocup.) | Caxias | T3 (presencial/voz) | 88 |
| 6 | JFF Medicina (ocup.) | Caxias | T3 (presencial/voz) | 88 |
| 7 | Centro Médico Ilha | Ilha | T1 | 91 |
| 8 | Taís Ferreira (nutri) | Ilha | T1 | 75 |
| 9 | Natália Vidal (nutri) | Ilha | T1 | 75 |
| 10 | Taiane Reis (nutri) | Ilha | T1 | 75 |
| 11 | Hanelle Lysias (nutri) | Ilha | T1 | 75 |
| 12 | Lilia Fernandes (nutri) | Ilha | T1 | 75 |

Números de WhatsApp e canais: iguais aos de `contatos-realizados.md` / CSVs de cada praça — não
mudaram.

---

## Confirmar antes (onda SOLO — quem respondeu?)

Disparada em **02/07**, ninguém registrou quem respondeu. `Ultimo_toque=T0`,
`Proximo_toque=2026-07-06` (**84 dias vencido**), `Status` contendo "CONFIRMAR" nos 7 CSVs. **10ª
semana consecutiva pedindo essa confirmação:**

- **Dra. Letícia Antunes** — Ilha · IG @leticiageas / WA (21) 96674-6574
- **Dream Smile Odontologia (Dr. Flávio Pinheiro)** — Ilha · WA (21) 99512-5162
- **Dr. Flávio Hércules (Dermato)** — Ilha · WA (21) 98993-0837
- **Fábio Lins Fisioterapia** — Ilha · WA (21) 99637-3173
- **Dra. Márcia Faria Beniste** — Ilha · IG @mfbeniste
- **Dr. Leonardo Freitas (Odonto Solo)** — Caxias · IG @odontodrleonardofreitas
- **Asanti Odonto** — Caxias · WA (21) 96020-7474

## Marcar como Frio (revisitar em 30-45 dias)

Nenhum lead atinge o critério automático (T3 vencido >10 dias registrado no CSV) porque nenhum tem
T3 formalmente lançado. Mas o Toque 3 dos itens 2-6 da tabela acima (Fisiomed, CMPK, ProntoAme,
Vitória Saúde, JFF Medicina) é presencial/voz por definição do plano original, está pronto desde
20/07 e segue sem sair — **81 dias vencido**. Recomendação inalterada há 8 semanas: (a) ligar/passar
pessoalmente (todos na Ilha ou Caxias/Jd. 25 de Agosto), ou (b) marcar `Status=Frio` manualmente.
Continuar gerando o mesmo texto sem enviá-lo não resolve.

## O que o Cássio precisa atualizar na base

1. **A pergunta de 17/08 segue sem resposta — 6ª semana pedindo a mesma decisão.** Três caminhos
   propostos em 17/08: **(a)** reduzir o teto semanal para 3-4 leads realmente enviáveis; **(b)**
   pausar esta rotina até haver janela real para disparar, retomando quando fizer sentido; **(c)**
   manter 12/semana, mas aí a rotina passa a só confirmar se algo mudou em vez de gerar texto novo
   toda vez (é basicamente o que já está acontecendo desde 24/08). Sem uma escolha, a rotina de
   segunda seguirá reportando o mesmo estado indefinidamente — este é o momento de decidir, não só
   de registrar.
2. **A leitura de 21/09 não rodou.** Não há relatório nem commit dessa data no `meu-vault` ou no
   `claude-config`. Vale checar se o gatilho semanal falhou ou se a instância daquela segunda não
   conseguiu commitar — é a primeira falha de execução desde que a rotina começou em 20/07.
3. **Placar da onda NUTRI segue vazio há 10 semanas.** "Entregues"/"Lidos" de
   `contatos-realizados.md` continuam em branco desde o disparo (14-15/07); só "Responderam" está
   preenchida (2/13 ≈ 15%). É esse número que decide se os 38 leads P2/P3 restantes valem a próxima
   onda.
4. **Onda Nutri-B (Caxias, 6 leads) segue adiada** pelo teto de 12/semana: Swheelen Vieira, Jorge
   Tulosa, Igor Fernandes, Jéssica Nascimento, Bruna Moreira, Rayana Cruz — textos prontos em
   `abordagem-nutri.md`. Rayana: conferir perfil antes de enviar (pode ser do Studio Laisa Patricio;
   reserva Daiane França (21) 99993-0992).
5. **Medcentro RJ segue adiado** (rede, decisor comercial central) — T0→T1 devido.
6. **Resposta à Pâmella e reabertura da Leonice** — confirmar se algo foi enviado por fora do painel
   antes de reenviar, para não duplicar.
7. **Natália Vidal** — se o WhatsApp principal não entregar, diretório cita número alternativo
   (96425-5354), ainda não confirmado.

---

*Gerado automaticamente pela rotina semanal de follow-up B2B (segundas, 9h). Fonte: colunas
`Ultimo_contato`/`Ultimo_toque`/`Proximo_toque` dos CSVs em `claude-config/workstations/B2B-Secretaria-IA/`.*

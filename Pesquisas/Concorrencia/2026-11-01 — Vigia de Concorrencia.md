---
title: Vigia de Concorrência — 2026-11-01
date: 2026-11-01
area: Concorrencia
tags: [concorrencia, mercado]
source: routine
---

## TL;DR

- Dois scribes em pt-BR que ainda não estavam nos relatórios. Os dois cobram mais que o Calima.
- **Escriba Médico** (Neurium, Joinville): R$ 97/mês. Tem os mesmos 7 dias grátis sem cartão, mas não faz receita, agenda nem teleconsulta.
- **Dr. Assistente:** de R$ 150 a R$ 450/mês e diz ter mais de 10 mil profissionais.
- Nada novo em regulação, secretária no WhatsApp ou teleconsulta. Não muda nenhuma recomendação.

> Comparado com o relatório de **2026-10-31**. **Varredura completa:** não. Hoje é domingo, e a última completa foi em 26/10, há 6 dias. A próxima é amanhã, segunda, 02/11.
> Preço do Calima conferido no repo (`origin/main` `3029a5a`): o `site/index.html` mostra R$ 49,90 (7 ocorrências); `VENDAVEIS = ['staff']`; `PLANO_STAFF_CENTS` e `CONSULTA_AVULSA_CENTS` têm default 4990.

## Achados

1. **Escriba Médico, um scribe em pt-BR que ainda não estava nos relatórios.** É da Neurium, de Joinville (SC).
   - **O que faz:** grava a consulta pelo navegador, no celular ou no computador, até 150 min por consulta, e o áudio é descartado depois do processamento. Organiza o texto num template, com 10 prontos (Clínica Médica, Pediatria, Cardiologia, Psiquiatria etc.) ou personalizado. Aceita PDF de exame anexado e, na teleconsulta, captura o áudio compartilhando a tela.
   - **O que não faz:** não tem integração com prontuário (o médico copia e cola), nem receita, atestado, agenda ou teleconsulta própria.
   - **Preço:** R$ 97,00/mês ou R$ 997,00/ano, ilimitado, com 7 dias grátis sem cartão. Quem indica um colega que assina ganha R$ 97 de crédito, e o colega ganha R$ 30 de desconto.
   - Fonte: [escribamedico.com.br](https://escribamedico.com.br/), lido em 01/11/2026 (maxAge 0).
   - **E daí pro Calima:** os 7 dias grátis sem cartão e o "ilimitado" são iguais aos do Calima, pelo dobro do preço e com menos coisa. Para quem só quer o scribe, o Calima é a mesma oferta pela metade, com receita, atestado, teleconsulta e agenda. A indicação que dá uma mensalidade inteira de crédito é uma ideia que vale copiar.
2. **Dr. Assistente (app.doutorassistente.com.br), outro scribe novo nos relatórios.** Gera anamnese, evolução, receita e atestado, funciona sobre qualquer prontuário e tem app web, iOS e Android. Na teleconsulta, grava a aba do Google Meet pelo Chrome.
   - **Escala:** diz ter mais de 10.000 profissionais e ser "o mais usado do Brasil" na categoria. É afirmação do próprio fornecedor, sem verificação.
   - **Preço:** de R$ 150 a R$ 450/mês, com teste grátis sem cartão. O valor vem do comparativo do próprio fornecedor, atualizado em agosto de 2026. A página de planos não foi aberta.
   - Fonte: [drassistente.com.br/comparar/melhor-prontuario-eletronico-com-ia](https://drassistente.com.br/comparar/melhor-prontuario-eletronico-com-ia/), lido em 01/11/2026.
   - **E daí pro Calima:** é o scribe em pt-BR com mais usuários declarados, e cobra pelo menos 3 vezes o preço do Calima. O fornecedor publica páginas "comparar/" que concorrem no Google pela busca "prontuário com IA", um espaço de SEO em que o Calima ainda não aparece.

**Descartados nas buscas:**
- **Telepatia (US$ 33 mi), Memed (R$ 80 mi) e HiDoctor (IA no prontuário):** notícias antigas, já registradas.
- **Doctoralia, iClinic, Feegow, Ninsaúde e Amplimed:** nada novo.
- **Secretária IA no WhatsApp:** só vagas no Workana, e-books na Hotmart e a Sofia do clina.ai, já registrada.
- **Teleconsulta avulsa (Conexa, Dr. Consulta, Einstein Conecta):** nada novo.
- **Sites com blog de prontuário com IA** (gestaods, apphealth, carecode.ai): não abri. Ficam para a varredura completa de amanhã.

## Regulação

- **CFM 2.454/2026:** a ação na 21ª Vara Federal do DF, que pede a suspensão, segue sem decisão noticiada.
- **Conselhos e órgãos:** nenhuma norma nova do CFP, CFN, CFO, COFFITO, COFEN, ANPD ou Anvisa, nem da Apple.
- **WhatsApp:** nada além da regra de 15/01/2026, já registrada. Ela proíbe chatbot de uso geral e permite IA de atendimento e agendamento.

## Pressão de preço

- **Nenhuma pressão para baixo.** Os dois scribes novos estão acima dos R$ 49,90: o Escriba cobra R$ 97 e o Dr. Assistente, de R$ 150 a R$ 450.
- **Ficou mais forte que o Calima está no piso do scribe pago em pt-BR.** O que segue abaixo dele é só o free tier com limite, como o do Vokkari (5 h grátis), já registrado.

## Comoditização

Sem mudança desde 30/10.

## Posicionamento

Sem mudança de recomendação. A varredura completa de amanhã deve incluir o Escriba Médico e o Dr. Assistente (página de planos) na lista de scribes.

## O que foi checado em 01/11/2026

- **Notícias:** WebSearch, standard e extended.
  - Prontuário e scribe com IA.
  - Rodadas de healthtech.
  - Secretária IA no WhatsApp.
  - CFM 2.454.
  - iClinic, Feegow, Doctoralia, Ninsaúde e Amplimed.
  - Teleconsulta avulsa.
  - Regras da WhatsApp API.
- **Páginas lidas com Firecrawl:** escribamedico.com.br e o comparativo do drassistente.com.br.
- **Lacunas:**
  - O agente web (MCP `agente-web`) não estava disponível nesta sessão de nuvem, então a rotina usou a reserva: WebSearch e Firecrawl.
  - Nenhum número foi estimado.

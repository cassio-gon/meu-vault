---
title: "Pesquisa: Ditado por voz em prontuário eletrônico"
date: 2026-08-10
tags: [pesquisa, last30days, calima]
tema: Ditado por voz em prontuário eletrônico
raws: [ditado-por-voz-prontu-rio-eletr-nico-ia-m-dica-raw-v3.md]
source: last30days
---

## O que a pesquisa encontrou

- **Versatilis** (versatilis.com.br) é concorrente brasileiro direto: prontuário eletrônico com reconhecimento de voz que transcreve, "remove vícios de fala" e organiza nos campos do prontuário — a mesma proposta do Calima.
- **VoxClinic.ai** faz o mesmo em espanhol, divulgando por TikTok com números pequenos (395 views no vídeo capturado).
- O mercado de língua inglesa está **saturado e com preço-âncora público**: Freed a partir de US$ 39/mês, Abridge para grandes redes, Heidi para consultório privado; a PatientNotes publica comparativo de 12 ferramentas.
- As ferramentas mais recomendadas em 2026 são DeepCura, Heidi, Abridge, Suki, Nuance DAX, Twofold e Cleo — e **r/medicine e r/FamilyMedicine são as comunidades de referência** para review por clínicos.
- No GitHub, "ditado por voz" apareceu em vários PRs de apps brasileiros comuns (diário devocional, log de refeições, registro de visitantes) quase sempre via **Web Speech API do navegador, pt-BR, grátis no Chrome** — o caminho barato é conhecido e trivial de copiar.
- Um projeto tribal nos EUA (`lakeraven-integrations`) especifica agente de ditado clínico com inferência em hardware próprio e modelos open-weight, **para que nenhum PHI transite por API de terceiro** — mesma preocupação de privacidade que o Calima resolve com anonimização.
- Um PR de outro projeto **reverteu** o ditado por voz justamente porque "mandava o áudio do usuário para um serviço externo através da API".

## Ressalva de qualidade

Dos 35 itens, boa parte era ruído completo (drama chinês no YouTube, tutorial de
dança do Michael Jackson, ambient occlusion no Hacker News). O sinal veio do
`WebSearch Supplemental` e dos itens de Web/GitHub.

## Fontes

- https://versatilis.com.br/prontuario-eletronico-com-reconhecimento-de-voz/
- https://pabau.com/blog/7-best-ai-medical-scribe/
- https://patientnotes.ai/resources/best-ai-scribes
- https://www.deepcura.com/resources/heidi-health-review
- https://github.com/lakeraven/lakeraven-integrations/issues/16
- https://github.com/Mateuus/PrometheonCode/pull/17
- https://www.reddit.com/r/healthIT/comments/1vf6r9d/where_would_ai_recorders_fit_in_a_healthcare_org/

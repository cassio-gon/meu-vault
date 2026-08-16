---
title: "Pesquisa: Banimento de WhatsApp com Baileys e Evolution"
date: 2026-06-30
tags: [pesquisa, last30days, secretaria-ia]
tema: Risco de banimento no WhatsApp não-oficial
raws: [baileys-banimento-whatsapp-evolution-raw-v3.md]
source: last30days
---

## O que a pesquisa encontrou

- **Desde 15/01/2026 os termos da Meta proíbem explicitamente a distribuição de chatbot de IA de terceiro no WhatsApp.** Isso muda a natureza do risco: não é mais só detecção técnica, é violação declarada de termo.
- A issue #1869 do Baileys ("High number of bans on WhatsApp!") relata **banimento até em contas rodando há mais de 3 anos sem bot**, nas versões v7.0.0-rc.5 e v6.7.19.
- A issue #2441 investiga **erro 463** em envio e chamada, concentrado em contas banidas/desbanidas e ligado à migração de LID.
- A issue #2309 registra **banimento permanente ao publicar status pelo Baileys** em servidor de produção.
- No Evolution API, as issues #439, #1650 e #1840 registram "bloqueio/banimento de instância", "número banido logo após ler o QR Code" e pedido de função nativa de aquecimento de número.
- **Baileys, WAHA, Evolution API e whatsmeow têm todos janela de 2 a 8 semanas** — todos "fingem ser um navegador WhatsApp Web" e caem quando a Meta atualiza o protocolo.
- A detecção evoluiu: a Meta identifica por **assinatura de rede e cadência de mensagem**, sem depender de denúncia. O ML pesa taxa de resposta (**abaixo de 10% = risco alto**), distância no grafo de contatos (desconhecidos) e timing robótico.
- Guias em pt-BR convergem no aquecimento de chip: **10 a 30 mensagens/dia subindo ao longo de 1 a 2 semanas**, cuidado redobrado nos 10 primeiros dias, opt-in e intervalos humanos.
- **Banimento por ferramenta não-oficial é quase sempre permanente e sem recurso efetivo.** A Cloud API oficial é o único caminho sem risco.

## Ressalva de qualidade

Excelente rendimento — o `WebSearch Supplemental` mapeou issue por issue no
GitHub. Os clusters sociais foram lixo completo (edits de Transformers, memes).
Esta é a busca-modelo: quando o tema é técnico e tem repositório público, o valor
está no GitHub e na web, nunca na rede social.

## Fontes

- https://github.com/WhiskeySockets/Baileys/issues/1869
- https://github.com/WhiskeySockets/Baileys/issues/2441
- https://github.com/WhiskeySockets/Baileys/issues/2309
- github.com/EvolutionAPI/evolution-api — issues #439, #1650, #1840
- https://github.com/kobie3717/baileys-antiban
- chatboq.com — termos da Meta de 15/01/2026
- achiya-automation.com — pesos do ML de detecção
- socialhub.pro, ajuda.zdg.com.br — permanência do banimento
- unred.com.br, horadecodar.com.br, blu.direct — guias de aquecimento de chip

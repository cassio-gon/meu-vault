---
title: Calima — Avaliação semanal 2026-08-26
date: 2026-08-26
area: Calima
tags: [calima, produto, auditoria]
source: routine
---

## TL;DR

- Semana recorde (26 commits, todos em `main`): a telemedicina Fase 1 foi mesclada e ganhou, no mesmo ciclo, a Fase 2 inteira — portal do paciente com cadastro/assinatura/agendamento, **sala de espera em tempo real** (paciente chega, médico chega, a consulta liga sozinha) e aviso automático ao médico (push + e-mail com `.ics`) quando um paciente marca ou desmarca.
- **3 bugs reais achados nesta revisão, nenhum anotado em commit nem no `PENDENCIAS.md`** (revisão adversarial de todo o delta, ver seção abaixo): (1) o vínculo cadastro↔conta do paciente autocadastrado nunca é gravado quando a sala abre sozinha (`ws-tele.js:77` não passa `pacienteId`, e a única função que passaria — `abrirSalaDaEspera` — está morta, zero chamadores no repo); (2) `POST /api/portal/plano/assinar` tem a mesma falha de duplo clique já documentada como pendência do médico em `billing.js`, mas reintroduzida no router novo do paciente, sem trava nem teste de concorrência; (3) `avisarCadastroPaciente` (`server.js:150`) vaza o e-mail do paciente em claro no push (tela de bloqueio) e no e-mail ao admin — contrariando a mesma regra de privacidade escrita pelo autor, na mesma semana, em `billing.js` e `aviso-consulta.js`.
- Dois fixes de segurança reais, com medição antes/depois no próprio commit: timing attack no login (32ms conta existente vs. 0,4ms inexistente → parelho em ~32,5ms) e brecha no limitador de tentativas (e-mail sem trim deixava passar 60 chutes em 3,8s).
- **Hoje, 26/08, a Resolução CFM 2.454/2026 entra em vigor sem prorrogação e sem transição para sistemas já em uso** — confirmado por busca própria desta rodada. É o prazo que o `PENDENCIAS.md` já marcava "decidir antes de 26/08"; o Calima segue sem carimbar uso de IA no prontuário exportado e sem TCLE específico. Pendência antiga, prazo agora vencido.
- Site vivo: 200 OK, probe de 25/08 18h15 BRT (fresco), TLS válido até 24/10, headers de segurança completos.

## O que mudou na semana

Volume alto demais para listar commit a commit — agrupado por assunto, do maior para o menor.

**Telemedicina + portal do paciente vira produto completo (`765b230`…`2071703`…`e5c0752`, 19–21/08).** A Fase 1 (WebRTC 1:1, portal com login zero-knowledge) estava documentada no `MEMORY.md` como "NÃO mergeada, NÃO deployada" — mas o próprio dia do merge (`555f245`/`c2f407b`, 19/08) já está no `main`, e a semana emendou direto a Fase 2: paciente cancela o próprio plano (`5b2e825`), grade de horários por dia da semana (`968f528`), médico único (`47b41ef`), correção de cobrança avulsa sem CPF (`3cfdffb`), webhook do Asaas sem eventos inexistentes (`569ce80`) e o pacote grande de plano+agendamento do paciente (`9e1c6e9`, 21 arquivos). **O `MEMORY.md` ficou defasado** — vale atualizar o status de "NÃO mergeada" para o estado real antes que alguém tome decisão baseado nele.

**Sala de espera — a ponte que faltava (`2071703`, `cf654b8`, `e5c0752`).** Resolve o buraco que a própria `PENDENCIAS.md` linha 133 descrevia: `POST /teleconsultas` exigia paciente já cadastrado pelo médico, e quem se cadastra sozinho no portal não tem cadastro. Agora o paciente "chega" (marca simples em `consultas_agendadas`, sem depender de sala), o médico vê a fila em tempo real via WebSocket (`server/lib/ws-tele.js`), e abrir a sala **deveria** fazer o vínculo cadastro↔conta na hora — só que não faz, para o caso mais comum. Ver Bug 1 abaixo.

### Bugs achados nesta revisão (revisão adversarial do delta, não anotados em commit nem no `PENDENCIAS.md`)

**Bug 1 — o vínculo cadastro↔conta do paciente autocadastrado nunca é gravado.** `PENDENCIAS.md` e o docstring de `sala-espera.js` descrevem "abrir a sala faz o vínculo, uma vez por paciente" como resolvido. Não está, para quem se cadastra sozinho pelo portal (via convite automático ou campanha, sem o médico ter cadastrado antes): `server/lib/ws-tele.js:77`, no caminho automático que abre a sala quando os dois lados chegam (`ambosPresentes`), chama `abrirSalaDaConsulta(db, { consulta: a, agoraIso })` **sem** `pacienteId`. A única função que passaria esse id — `abrirSalaDaEspera(consultaId, pacienteId)` em `public/js/tele/tele-api.js:18` — está importada em `teleatendimento-ui.js` mas **nunca chamada** em lugar nenhum do repo (conferido por grep: zero invocações). Efeito prático: `pacientes_contas.paciente_id` fica `NULL` para sempre nesse fluxo — a fila de espera mostra o e-mail em vez do nome indefinidamente, e o vínculo que o resto do produto assume (ficha do paciente reconhecendo atendimentos anteriores, por exemplo) nunca se forma para quem entrou pelo portal sozinho.

**Bug 2 — duplo clique em "Assinar" no portal do paciente cria duas assinaturas Asaas.** `server/routes/portal-plano.js:82-118` (`POST /plano/assinar`) lê `conta.plano_status` e só depois, em sequência assíncrona (`faturaPendente` → `asaas.criarCustomer` → `asaas.criarSubscription`), grava o resultado. Duas requisições simultâneas (duplo toque no celular) passam as duas pelo mesmo guard e criam dois customers/duas subscriptions para a mesma conta. É a MESMA classe de bug que o `PENDENCIAS.md` já lista aberta para o médico (`routes/billing.js:40-67`, "`/subscribe` sem trava de duplo clique") — só que reintroduzida no router novo do paciente, sem o claim condicional que aquela pendência já recomenda, e sem teste de concorrência em `tests/portal-plano.test.js`.

**Bug 3 — e-mail do paciente vaza em claro na notificação de cadastro, contrariando a regra escrita na mesma semana.** `server/server.js:150` (`avisarCadastroPaciente`, do commit `a665a10`) monta `` `${email} criou conta no portal...` `` e manda para `notificarAdmin` (aparece na tela de bloqueio do celular) e para o e-mail do admin em claro. Isso contraria explicitamente o princípio escrito pelo mesmo autor, na mesma semana, em código vizinho: `routes/billing.js` (`AVISO_PACIENTE`, commit `47b41ef`) diz "nada de identificar o paciente aqui... o e-mail não vai para a tela de notificação de ninguém", e `lib/aviso-consulta.js` (commit `64ecda6`) diz "nem o push nem o e-mail... identificam o paciente". O commit de cadastro não seguiu a própria regra.

Fora desses três, a revisão (própria + de um agente em paralelo, cobrindo os commits de `server/`/`public/` com leitura de arquivo completo, não só o patch) não achou problema de isolamento por `user_id`, SQL sem parametrização ou XSS nas rotas novas — checado explicitamente e está correto (JOINs por `user_id`/`conta_id`, 404 em vez de 403).

**Agenda avisa o médico (`64ecda6`).** Até aqui uma consulta marcada pelo paciente não gerava nenhum sinal do lado do médico além do webhook de pagamento (que não diz *quando*). Agora `server/lib/aviso-consulta.js` dispara push + e-mail com `.ics` anexado (e cancela com um segundo `.ics` `METHOD:CANCEL` do mesmo UID). Nem nome nem paciente aparecem no aviso — só data/hora/origem, mantendo a promessa de LGPD do resto do produto.

**Segurança — dois achados reais corrigidos no mesmo dia (`c61164a`, 20/08).** (1) Timing attack: só a conta existente pagava o custo do scrypt, então um único request classificava com certeza se um e-mail tinha conta — corrigido pagando o KDF contra hash dummy mesmo quando a conta não existe. (2) O limitador de tentativas comparava e-mail com/sem `trim()` em pontos diferentes, permitindo 60 tentativas em 3,8s por variação de espaço; normalizado numa função única usada pela chave e pela consulta. Ambos tinham medição de antes/depois no commit — não é suposição.

**Convite automático ao paciente (`63fb49b`, 23/08).** Substitui o CSV manual por fila no servidor com disparo diário às 14h. Reconhece explicitamente ser "a única fronteira onde PII de paciente fica em claro no servidor" e limita o dano: só e-mail + primeiro nome, sem FK pro prontuário, claro apagado no envio (`marcarEnviado` zera os campos no mesmo UPDATE que carimba o envio). Descadastro em um clique com token HMAC assinado por segredo de instância, GET confirma / POST efetiva (RFC 8058, evita que antivírus de link do Gmail descadastre sozinho). Revisado linha a linha: desenho consistente, sem achado.

**Campanha de e-mail (`d4b0965`…`20cb061`, 20–24/08).** E-mail de lançamento do teleatendimento + scripts de disparo do Mac sem abrir o Coolify. Fora do escopo de produção (scripts/), não revisado a fundo.

## Site vivo

Probe de **2026-08-25 18:15:46 America/Sao_Paulo** (~15h antes deste relatório — fresco): `/` → 200, 0,65s total, TTFB 0,45s; gzip ativo; TLS Let's Encrypt válido até 24/10/2026; headers com CSP restritiva, HSTS, `X-Frame-Options: DENY`, `X-Content-Type-Options: nosniff`, `Referrer-Policy: no-referrer`, `Cross-Origin-Opener-Policy: same-origin`. Nada a apontar.

## Tema da semana — índice 6: Mercado e novidades do nicho

Foco: feature nova que apareceu no nicho e caberia no Calima (preço/movimento de concorrente já é coberto pela rotina "Vigia de Concorrência" — não duplicado aqui).

1. **Concorrente brasileiro novo lançado em 27/07/2026 replica quase exatamente o que o Calima construiu esta semana.** Kurai (kurai.app) anuncia "gestão médica inteligente com IA": scribe por voz → SOAP em segundos, agenda, telemedicina, financeiro e **portal do paciente** — o mesmo pacote (scribe + teleconsulta + portal) que o Calima整completou nesta semana. Fonte: [kurai.app](https://kurai.app/), checado 26/08/2026 (data de lançamento vem da própria página, não confirmada em fonte terceira). **E daí pro Calima:** o timing é uma coincidência favorável — o Calima não está correndo atrás de uma lacuna, já fechou o mesmo gap no mesmo mês. Vale um mystery-shop leve do Kurai (preço, se cobra por volume como o Calima) numa rodada futura da Vigia de Concorrência.

2. **OpenAI lançou "Health" dentro do ChatGPT para usuários dos EUA em 23/07/2026** — conecta Apple Health e prontuários de hospitais/One Medical/Function Health, com IA respondendo sobre exames e histórico. Fonte: [openai.com/index/health-in-chatgpt](https://openai.com/index/health-in-chatgpt/), checado 26/08/2026. Só EUA, não é ferramenta de consultório. **E daí pro Calima:** não é ameaça direta (é ferramenta do paciente, não do médico), mas é sinal de que "IA lendo histórico de saúde" está virando produto mainstream de consumo — reforça que pacientes vão chegar cada vez mais acostumados a interfaces de IA conversacional, o que facilita a adoção do próprio portal do paciente do Calima.

3. **Artigo acadêmico (npj Digital Medicine, aceito 06/03/2026) aponta que scribes ambientais falham em atribuir falas corretamente quando há mais de duas pessoas na sala** (médico + enfermeiro + paciente + família, por exemplo) — achado relevante porque a transcrição simultânea do Calima já mixa duas pontas (médico + paciente) na teleconsulta. Fonte: [nature.com/articles/s41746-026-02554-0](https://www.nature.com/articles/s41746-026-02554-0), aceito em março — publicação pode ser mais antiga que a janela de 30 dias, sinalizado aqui por honestidade. **E daí pro Calima:** hoje o app resolve isso não separando falantes, e sim jogando o áudio misto no fluxo de ditado normal após a chamada — funciona porque não promete diarização. Não é uma ação a tomar, é validação de que a decisão de design atual evita um problema que a literatura está documentando como não-resolvido nem pelos grandes players.

Nenhum achado de preço/concorrente direto nesta seção — isso é papel da Vigia de Concorrência (última rodada: 21/08, sem pressão de preço nova sobre a escada do Calima).

## Layout/UX e Funções

Sem gap novo de layout esta semana (nenhum commit de CSS/HTML fora do necessário para as telas novas do portal). Em Funções, o único ponto que merece nota não é um gap de código, é de **documentação**: o `MEMORY.md` (seção "Status 2026-08-19") ainda descreve a telemedicina como não mesclada — o `main` já tem ela e mais uma semana de trabalho em cima. Vale uma atualização na próxima sessão que mexer nessa workstation.

## Sugestões novas

Nenhuma sugestão de feature nova nesta rodada — a semana foi dominada por construção de feature grande, e o que vale registrar são os 3 bugs da seção acima (já adicionados ao `BACKLOG.md` como correções pendentes, não como melhorias de produto).

**Melhorias (0) · Integrações (0).**

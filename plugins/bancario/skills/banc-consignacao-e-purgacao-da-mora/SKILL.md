---
name: banc-consignacao-e-purgacao-da-mora
description: >
  Redige a consignação em pagamento (extrajudicial em banco ou ação
  consignatória) de parcelas de contrato bancário — financiamento de veículo,
  cédula de crédito bancário, empréstimo, consórcio — para afastar ou purgar a
  mora quando o banco recusa o pagamento, não emite boleto ou exige valor
  controvertido (CPC, arts. 539 a 549; CC, arts. 334 a 337 e 401), com alerta
  do Tema 967/STJ sobre depósito insuficiente. Use quando o usuário pedir para
  depositar em juízo as parcelas do financiamento, banco que não manda boleto,
  banco recusa receber parcela atrasada, purgar a mora antes da busca e
  apreensão, consignatória bancária ou depósito judicial das prestações.
metadata:
  area: bancario
  tipo_peca: inicial
  verificado_em: 2026-11-25
---
# Consignação em pagamento e purgação da mora (contrato bancário)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: (a) banco recusa sem justa causa receber ou dar quitação (CC, art. 335, I); (b) não fornece meio de pagamento (boleto, débito) no tempo e modo devidos (art. 335, II); (c) dúvida sobre quem deve receber, como em cessão de crédito não comunicada (art. 335, IV); (d) litígio pendente sobre o objeto do pagamento (art. 335, V); (e) devedor quer purgar a mora oferecendo a prestação com os acréscimos até a data (art. 401, I), **antes** de ajuizada a busca e apreensão.
- Não usar:
  - Busca e apreensão já ajuizada e liminar cumprida: a purgação é o pagamento integral em 5 dias no próprio processo → `banc-busca-e-apreensao-contestacao`.
  - Imóvel com alienação fiduciária (Lei 9.514/1997): purgação perante o registro de imóveis → `imob-revisao-de-financiamento-sfh`.
  - Discussão ampla de cláusulas com depósito do incontroverso → `consumidor-contratos-bancarios-revisional` (CPC, art. 330, §§ 2º e 3º); se cumular, manter aqui só o capítulo do depósito.
  - Quer negociar desconto → `banc-renegociacao-extrajudicial-de-divida`.
  - Aluguel → `imob-*`.

## Entradas mínimas (perguntar o que faltar; nunca supor fatos)
1. Contrato, plano de pagamento e extrato com parcelas pagas e em aberto.
2. Prova da recusa ou da impossibilidade de pagar: protocolos de atendimento, e-mails, prints do aplicativo sem boleto, carta do banco.
3. Valor que o banco exige e valor que o cliente reconhece; origem da diferença (tarifa, seguro, encargo moratório).
4. Já houve notificação de mora, protesto, negativação ou ação do banco?
5. Capacidade real de depositar **tudo** o que reconhece devido, inclusive as parcelas que vencerem no curso.
6. Houve cessão do crédito a outra instituição ou securitizadora?

## Prazo e contagem
- **Extrajudicial (dinheiro):** depósito em banco oficial do lugar do pagamento, com carta ao credor; 10 dias para recusa (CPC, art. 539, § 1º). Sem recusa, o devedor fica liberado (§ 2º). Com recusa escrita, a ação deve ser proposta em **1 mês**, com prova do depósito e da recusa (§ 3º); sem ação, o depósito fica sem efeito (§ 4º).
- **Ação:** pedir o depósito em **5 dias** do deferimento (art. 542, I); sem depósito, extinção sem mérito (art. 542, parágrafo único).
- **Prestações periódicas:** consignada uma, as seguintes podem ser depositadas nos mesmos autos até **5 dias** do vencimento (art. 541).
- **Complementação:** alegada insuficiência, o autor pode completar em **10 dias** (art. 545).
- Contagem: `prazos-processuais`.

## Estrutura da peça
Endereçamento (foro do lugar do pagamento) → fatos e prova da recusa → cabimento (CC, art. 335) → valor devido e memória → efeitos (cessação de juros e riscos; afastamento ou purgação da mora) → prestações vincendas → tutela (abstenção de negativação e de busca e apreensão) → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- O depósito só tem força de pagamento se observar pessoas, objeto, modo e tempo do pagamento válido (CC, art. 336). Depósito no lugar do pagamento; feito, cessam juros e riscos, salvo improcedência (CC, art. 337; CPC, art. 540).
- **Tema 967/STJ:** na consignatória, depósito insuficiente leva à improcedência, porque pagamento parcial não extingue a obrigação. Por isso a memória deve incluir os acréscimos da mora até a data da oferta (CC, art. 401, I), e a complementação do art. 545 deve ser usada.
- Defesas do banco (CPC, art. 544): não houve recusa ou mora; recusa justa; depósito fora de prazo ou lugar; depósito incompleto — neste caso o réu deve indicar o valor que entende devido.
- O banco pode levantar o incontroverso e o processo segue sobre a diferença (art. 545, § 1º); sentença que reconhece insuficiência fixa o saldo e vale como título para o credor (§ 2º).
- Ajuizar revisional sem depósito não afasta a mora (Súmula 380/STJ).

## Fundamentos verificados
- CPC, arts. 539, 540, 541, 542, 544, 545 e 546; art. 330, §§ 2º e 3º (cumulação com revisional).
- CC, arts. 334, 335, 336, 337, 394, 396 e 401.
- Tema 967/STJ (tese transcrita no AREsp 1.635.102, 4ª Turma, 2025).
- Súmula 380/STJ.
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Autorização do depósito do valor ofertado em 5 dias, e das vincendas nos mesmos autos (arts. 541 e 542, I).
- Citação do banco para levantar o depósito ou contestar (art. 542, II).
- Tutela de urgência (CPC, art. 300): enquanto houver depósito regular, abstenção de negativação, protesto e ajuizamento de busca e apreensão pelas parcelas consignadas [o juízo decide; sem garantia de deferimento].
- Procedência: declaração de extinção da obrigação quanto às parcelas depositadas e custas e honorários pelo réu (art. 546).
- Juros e correção sobre eventuais diferenças: núcleo `juros-e-correcao`.

## Checklist pré-protocolo
- [ ] Prova documental da recusa ou da falta de meio de pagamento
- [ ] Memória com principal e acréscimos até a data do depósito (nunca só o principal)
- [ ] Cliente ciente de que deve depositar as vincendas em até 5 dias de cada vencimento
- [ ] Credor correto (cedente ou cessionário) identificado
- [ ] Foro do lugar do pagamento
- [ ] Se houve depósito extrajudicial com recusa: ação dentro de 1 mês
- [ ] Prazos conferidos em `prazos-processuais`

## Erros a evitar
- Depositar só o valor "justo" na visão do cliente sem memória séria — risco do Tema 967.
- Parar de depositar as vincendas no curso do processo.
- Usar consignatória para recuperar veículo já apreendido (a via é o art. 3º, § 2º, do DL 911).
- Confundir consignatória com revisional: aqui a tese central é a recusa, não a abusividade.
- Deixar passar 1 mês da recusa do depósito extrajudicial sem ajuizar.

## Integração com o núcleo
`prazos-processuais`, `juros-e-correcao` (acréscimos da mora e diferenças), `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

---
name: adm-recurso-em-licitacao
description: >
  Redige recurso administrativo, contrarrazões ou pedido de reconsideração em
  licitação regida pela Lei 14.133/2021 (arts. 165 a 168): julgamento de propostas,
  habilitação/inabilitação, anulação, revogação e extinção unilateral do contrato.
  Use quando o usuário pedir recurso no pregão, recurso contra inabilitação ou
  desclassificação, manifestar intenção de recorrer, razões recursais,
  contrarrazões, recurso contra habilitação do concorrente ou reconsideração.
metadata:
  area: administrativo-licitacoes
  tipo_peca: recurso-administrativo
  verificado_em: 2026-11-01
---
# Recurso em licitação (Lei 14.133/2021, arts. 165 a 168)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar contra os atos do art. 165, I: pré-qualificação e registro cadastral; julgamento das propostas; habilitação ou inabilitação; anulação ou revogação da licitação; extinção unilateral do contrato.
- Pedido de reconsideração (art. 165, II): ato do qual não caiba recurso hierárquico.
- Contrarrazões: quando o concorrente recorre contra resultado favorável ao cliente.
- Não usar para sanções de multa, impedimento ou inidoneidade (ver `adm-defesa-em-processo-sancionador-licitacao`, que trata dos arts. 166 e 167).
- Não usar para atacar cláusula do edital depois da abertura sem que o vício se manifeste no julgamento (a via própria era a impugnação, `adm-impugnacao-ao-edital`).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Ata da sessão (ou registro do sistema eletrônico) com data/hora e decisão recorrida.
2. Se o cliente manifestou intenção de recorrer na sessão e como isso ficou registrado.
3. Edital e anexos, proposta e documentos de habilitação do cliente e do concorrente questionado.
4. Motivação da decisão do agente de contratação/pregoeiro/comissão.
5. Data da intimação ou da lavratura da ata (início do prazo).
6. Inversão de fases adotada? (art. 17, § 1º).

## Prazo e contagem
- Julgamento de propostas e habilitação (art. 165, I, "b" e "c"): intenção de recorrer manifestada imediatamente, sob pena de preclusão; razões em 3 dias úteis contados da intimação ou da lavratura da ata de habilitação/inabilitação (ou da ata de julgamento se houver inversão de fases); apreciação em fase única (art. 165, § 1º).
- Demais hipóteses do inciso I e reconsideração do inciso II: 3 dias úteis da intimação ou da lavratura da ata.
- Contrarrazões: mesmo prazo, a contar da intimação pessoal ou da divulgação da interposição (art. 165, § 4º).
- Tramitação: autoridade recorrida reconsidera em 3 dias úteis ou encaminha; autoridade superior decide em até 10 dias úteis (art. 165, § 2º).
- Contagem em dias úteis do órgão (art. 183). Conferir com `prazos-processuais`.
- Efeito suspensivo automático até a decisão final (art. 168).

## Estrutura da peça (resumo; detalhe em [estrutura](references/estrutura.md))
Endereçamento à autoridade que proferiu o ato (com pedido de reconsideração ou encaminhamento) → tempestividade e registro da intenção → síntese da decisão → razões → pedido de vista/diligência → pedidos.

## Requisitos e preliminares
- Prova da manifestação imediata da intenção de recorrer (print do sistema, ata).
- Vista dos elementos indispensáveis à defesa (art. 165, § 5º) — requerer por escrito se negada.
- Aproveitamento de atos: o acolhimento invalida só o ato insuscetível de aproveitamento (art. 165, § 3º); pedir expressamente a extensão da invalidação necessária.
- Saneamento: antes de pedir desclassificação de concorrente, verificar se o vício é sanável por diligência (art. 59, I e V; art. 64, I e II e § 1º: falhas que não alterem a substância dos documentos); antecipar essa defesa nas contrarrazões.

## Fundamentos verificados (resumo; detalhe em [fundamentos](references/fundamentos.md))
Lei 14.133/2021: arts. 5º, 17, 59, 64, 71, 165, 168, 183. Lei 9.784/1999 (aplicação subsidiária no âmbito federal): arts. 56 e 64, parágrafo único. Súmula 473 do STF.

## Pedidos e requerimentos
- Reconsideração pela autoridade recorrida ou encaminhamento à autoridade superior com motivação (art. 165, § 2º).
- Reforma da decisão: habilitar/classificar o recorrente, ou inabilitar/desclassificar o concorrente, com indicação do item do edital.
- Anulação limitada aos atos insuscetíveis de aproveitamento (art. 165, § 3º).
- Vista integral dos documentos (art. 165, § 5º).
- Manifestação do órgão de assessoramento jurídico (art. 168, parágrafo único).

## Checklist pré-protocolo
- [ ] Intenção de recorrer registrada na sessão (propostas/habilitação).
- [ ] Prazo de 3 dias úteis contado da intimação/lavratura da ata.
- [ ] Ato recorrido enquadrado em uma alínea do art. 165, I.
- [ ] Cada argumento ligado a item do edital e a documento.
- [ ] Vício do concorrente é insanável (ou demonstrada a impossibilidade de diligência).
- [ ] Protocolo pelo canal do edital/sistema, com comprovante.
- [ ] Plano B: MS em até 120 dias da decisão final (`adm-mandado-de-seguranca`).

## Erros a evitar
- Não manifestar a intenção de recorrer na sessão e apresentar só as razões depois.
- Contar o prazo em dias corridos.
- Inovar nas razões com motivos não ligados à intenção manifestada, quando o sistema exigir a motivação sintética da intenção [VERIFICAR: regra do regulamento do ente e do edital].
- Pedir anulação de todo o certame quando bastaria refazer o ato viciado.
- Fundamentar em artigos da Lei 8.666/1993 em certame regido pela Lei 14.133/2021.

## Integração com o núcleo
- `prazos-processuais`: contagem em dias úteis e efeito suspensivo.
- `verificacao-de-citacoes`: decisões de tribunais de contas e acórdãos acrescentados.
- `fidelidade-factual`: conferência de documentos de habilitação e números.
- `estilo-forense`: revisão final.

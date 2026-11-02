---
name: civel-agravo-de-instrumento
description: >
  Redige agravo de instrumento cível (CPC arts. 1.015 a 1.020) contra decisão
  interlocutória do rol do art. 1.015 ou, excepcionalmente, fora dele pela
  taxatividade mitigada (urgência por inutilidade do julgamento na apelação),
  com pedido de efeito suspensivo ou tutela recursal. Use quando o usuário
  pedir agravo de instrumento, "agravar" de decisão, recorrer de liminar, de
  decisão sobre gratuidade, desconsideração, cumprimento de sentença ou execução.
metadata:
  area: processo-civil
  tipo_peca: agravo
  verificado_em: 2026-11-01
---
# Agravo de instrumento

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: interlocutória dos incisos do art. 1.015 ou do seu parágrafo único (liquidação, cumprimento de sentença, execução, inventário); decisão parcial de mérito (art. 356, §5º).
- Usar fora do rol só com urgência demonstrada (taxatividade mitigada — ver fundamentos).
- Não usar: decisão de relator (agravo interno — `civel-agravo-interno`); despacho (art. 1.001); interlocutória não agravável sem urgência (vai em preliminar de apelação, art. 1.009, §1º); juizado especial cível (Lei 9.099 não prevê agravo; nos juizados federal e da Fazenda, só contra medidas cautelares/antecipatórias — Lei 10.259, art. 5º; Lei 12.153, art. 4º).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
- Decisão agravada e certidão/registro de intimação.
- Petição que provocou a decisão; inicial e contestação (se autos físicos).
- Procurações de agravante e agravado; nomes e endereços dos advogados.
- Fato concreto de urgência e prejuízo, se pedido efeito suspensivo ou se a hipótese estiver fora do rol.

## Prazo e contagem
- 15 dias úteis (arts. 1.003, §5º, e 219); dobra para Fazenda, MP, Defensoria.
- Autos físicos: juntar na origem cópia do agravo em 3 dias (art. 1.018, §2º), sob pena de inadmissão se o agravado arguir e provar (§3º). Autos eletrônicos: providência facultativa.
- Resposta do agravado em 15 dias (art. 1.019, II). Use `prazos-processuais`.

## Estrutura da peça
Petição ao tribunal → qualificação e advogados (art. 1.016) → tempestividade e preparo → cabimento (inciso do art. 1.015 ou urgência) → decisão agravada → razões → efeito suspensivo / tutela recursal → pedidos → peças. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Requisitos do art. 1.016; instrução do art. 1.017 (dispensada em autos eletrônicos — §5º).
- Preparo e porte de retorno, quando devidos (art. 1.017, §1º).
- Vício sanável: relator concede 5 dias (arts. 1.017, §3º, e 932, p.ú.).
- Efeito suspensivo ou antecipação da pretensão recursal pelo relator em 5 dias (art. 1.019, I).

## Fundamentos verificados
CPC arts. 356, §5º, 932, 1.001, 1.003, 1.009, §1º, 1.015 a 1.020; Tema 988 do STJ (REsp 1.696.396/MT e 1.704.520/MT, Corte Especial); REsp 2.129.011 (STJ, 2026). Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Efeito suspensivo ou tutela antecipada recursal, liminarmente.
- Intimação do agravado e do MP, se for o caso.
- Provimento para reformar ou anular a decisão.
- Comunicação ao juízo de origem.

## Checklist pré-protocolo
- [ ] Hipótese de cabimento identificada (inciso ou parágrafo único do art. 1.015, art. 356, §5º, lei especial) ou urgência demonstrada.
- [ ] Prazo e feriados locais conferidos.
- [ ] Peças obrigatórias (autos físicos) ou declaração de inexistência (art. 1.017, II).
- [ ] Nomes e endereços completos dos advogados.
- [ ] Preparo pago (se devido no tribunal).
- [ ] Pedido liminar com fato concreto de dano.
- [ ] Agenda da comunicação de 3 dias à origem (autos físicos).

## Erros a evitar
- Agravar de decisão fora do rol sem demonstrar a inutilidade do julgamento posterior na apelação.
- Deixar de agravar decisão do rol achando que poderá discutir na apelação: há preclusão.
- Confundir agravo de instrumento com agravo interno ou com agravo em REsp/RE (art. 1.042).
- Pedir efeito suspensivo sem descrever o dano concreto.
- Esquecer a comunicação em 3 dias nos autos físicos.

## Integração com o núcleo
- `prazos-processuais` para prazo e comunicação à origem.
- `verificacao-de-citacoes` para o Tema 988 e qualquer outro precedente.
- `juros-e-correcao` se a decisão agravada for de cálculo em cumprimento ou execução.
- `fidelidade-factual` e `estilo-forense` na revisão.

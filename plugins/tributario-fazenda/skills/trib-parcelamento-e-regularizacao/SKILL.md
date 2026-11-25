---
name: trib-parcelamento-e-regularizacao
description: >
  Orienta o pedido de parcelamento de débito tributário e a adesão a programa de
  regularização fiscal, com base no CTN (arts. 151, VI, 155-A e 174) e, no plano
  federal, nos arts. 10 a 14-F da Lei 10.522/2002, sem presumir que programa
  especial esteja aberto. Use quando o usuário pedir parcelamento de tributo,
  reparcelamento, adesão a Refis ou programa de regularização, rescisão de
  parcelamento, suspensão da execução fiscal por parcelamento ou efeitos do
  parcelamento sobre prescrição e denúncia espontânea.
metadata:
  area: tributario-fazenda
  tipo_peca: requerimento
  verificado_em: 2026-11-25
---
# Parcelamento e programas de regularização fiscal

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: (a) parcelamento ordinário ou simplificado de débito federal; (b) parcelamento estadual ou municipal (aplicando a lei do ente); (c) reparcelamento; (d) adesão a programa especial **cuja abertura tenha sido conferida na fonte oficial no dia**; (e) defesa contra rescisão; (f) pedido de suspensão da execução fiscal pelo parcelamento.
- Não usar: quando há chance real de reduzir principal, multa e juros por acordo com a PGFN — compare com `trib-transacao-tributaria` antes de parcelar; quando o débito é indevido (o parcelamento é confissão): `trib-defesa-administrativa-e-carf`, `trib-acao-anulatoria`, `trib-embargos-a-execucao-fiscal`.
- Débito prescrito: o pedido de parcelamento interrompe a prescrição ainda que indeferido (Súmula 653 STJ) — antes de parcelar, rode `trib-prescricao-intercorrente` e confira a prescrição ordinária.

## Entradas mínimas (perguntar o que faltar; nunca supor fatos)
1. Ente credor e situação de cada débito: em cobrança na Receita/Secretaria, inscrito em dívida ativa, ajuizado, com garantia ou depósito.
2. Relatório de situação fiscal / extrato da dívida ativa atualizado, com datas de vencimento e de constituição.
3. Parcelamentos anteriores (ativos, rescindidos, reparcelados) e quantas parcelas pagas.
4. Natureza dos débitos (retido na fonte, estimativas, Simples Nacional etc.), por causa das vedações.
5. Capacidade de pagamento mensal e se existe garantia a oferecer.
6. Se há discussão administrativa ou judicial que precise ser desistida.

## Prazo e contagem
- Pedido de parcelamento: em regra sem prazo, mas a consolidação ocorre na data do pedido (Lei 10.522, art. 12) — atenção à data de corte de programas especiais.
- Rescisão federal: 3 parcelas em atraso, consecutivas ou não, ou 1 parcela quando as demais estiverem pagas (art. 14-B).
- Prescrição: interrompida por ato inequívoco de reconhecimento do débito (CTN art. 174, § 1º, IV) — o pedido de parcelamento se enquadra (Súmula 653 STJ).
- Prazos processuais: `prazos-processuais`.

## Estrutura da peça
Requerimento: identificação → débitos e situação → modalidade escolhida e base legal → número de parcelas → garantia (quando exigida) → desistências → pedidos. Petição na execução fiscal: notícia do parcelamento → suspensão da exigibilidade (CTN art. 151, VI) → pedido de suspensão do feito e levantamento de restrições cabíveis. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- O parcelamento segue a lei específica de cada ente (CTN art. 155-A) e, salvo lei em contrário, não exclui juros e multas (§ 1º).
- Federal ordinário: até 60 parcelas mensais, a critério da autoridade (Lei 10.522, art. 10); primeira parcela paga para formalizar; garantia para débito inscrito, salvo exceções (art. 11); pedido é confissão (art. 12); deferimento tácito em 90 dias sem manifestação (art. 12).
- Vedações do art. 14 (ex.: tributos retidos e não recolhidos, estimativas mensais de IRPJ/CSLL, débito com depósito judicial integral).
- Reparcelamento: entrada de 10% ou 20% conforme histórico (art. 14-A).
- Parcelamento simplificado: limites fixados por ato infralegal são válidos (Tema 997 STJ).
- Denúncia espontânea: não se configura com o parcelamento (orientação reafirmada no AgInt no REsp 2.238.871, STJ, 2026); nem para tributo declarado e pago a destempo (Súmula 360 STJ).
- Programas especiais (Refis e similares): só citar com a lei instituidora aberta na fonte oficial; nunca afirmar que estão vigentes de memória [VERIFICAR a cada uso].

## Fundamentos verificados
- CTN arts. 151, VI; 155-A; 174, § 1º, IV (redação da LC 236/2026).
- Lei 10.522/2002, arts. 10, 11, 12, 13, 14, 14-A, 14-B e 14-C.
- Súmula 653 e Súmula 360 do STJ; Tema 997 do STJ; AgInt no REsp 2.238.871.
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Deferimento do parcelamento na modalidade e no número de parcelas indicados.
- Suspensão da exigibilidade e expedição de certidão positiva com efeitos de negativa enquanto regular.
- Na execução fiscal: suspensão do processo; manutenção ou liberação de penhora conforme a lei do programa (não presumir).
- Defesa contra rescisão: demonstração de pagamento ou de erro no cálculo das parcelas, pedido de restabelecimento.
- Atualização das parcelas: segue a lei do ente; não calcular por conta própria — `juros-e-correcao`.

## Checklist pré-protocolo
- [ ] Prescrição e decadência conferidas antes de confessar
- [ ] Transação comparada (pode reduzir mais que o parcelamento)
- [ ] Nenhum débito em vedação legal
- [ ] Lei do programa especial aberta na fonte oficial, com prazo de adesão vigente
- [ ] Desistências exigidas avaliadas com o cliente (efeito sobre teses em curso)
- [ ] Primeira parcela e garantia providenciadas

## Erros a evitar
- Parcelar débito prescrito ou decaído sem antes verificar (o pedido interrompe a prescrição).
- Afirmar que "o Refis está aberto" sem conferir a lei e o prazo no dia.
- Esquecer que confissão no parcelamento não impede discutir aspectos jurídicos do débito, mas fragiliza a discussão de fatos [VERIFICAR o alcance no caso concreto].
- Prometer denúncia espontânea com parcelamento.
- Deixar o cliente atrasar 3 parcelas sem alerta de rescisão.

## Integração com o núcleo
`juros-e-correcao`, `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`. Vizinhas: `trib-transacao-tributaria`, `trib-prescricao-intercorrente`, `trib-embargos-a-execucao-fiscal`, `banc-renegociacao-extrajudicial-de-divida` (dívida não tributária bancária).

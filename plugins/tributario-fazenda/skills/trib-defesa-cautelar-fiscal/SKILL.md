---
name: trib-defesa-cautelar-fiscal
description: >
  Redige a contestação em medida cautelar fiscal (Lei 8.397/1992, art. 8º: 15
  dias), o agravo contra a liminar de indisponibilidade (art. 7º) e o pedido de
  substituição da indisponibilidade por garantia (art. 10), atacando a falta de
  prova literal do crédito e da hipótese do art. 2º, o excesso sobre bens fora
  do ativo permanente e a perda de eficácia (arts. 11 e 13). Use quando o
  usuário pedir defesa em cautelar fiscal, bloqueio de bens pedido pela
  Fazenda, indisponibilidade de bens da empresa, do controlador ou do
  administrador, ou liberação de bens bloqueados em cautelar fiscal.
metadata:
  area: tributario-fazenda
  tipo_peca: contestacao
  verificado_em: 2026-11-25
---
# Defesa em medida cautelar fiscal

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: a Fazenda (União, Estado, Município ou autarquia) ajuizou medida cautelar fiscal, preparatória ou incidental à execução, e obteve ou pede indisponibilidade de bens do devedor, do controlador ou de administradores.
- Não usar:
  - bloqueio feito dentro da própria execução fiscal (penhora, CTN art. 185-A): defesa na execução — `trib-excecao-pre-executividade-fiscal` ou `trib-embargos-a-execucao-fiscal`;
  - inclusão do sócio na execução: `trib-defesa-redirecionamento-socio`;
  - terceiro não requerido na cautelar com bem atingido: `trib-embargos-de-terceiro-execucao-fiscal`;
  - discussão do mérito do crédito: `trib-acao-anulatoria`, `trib-defesa-administrativa-e-carf`.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Inicial da Fazenda, documentos e decisão liminar; data da juntada do mandado de citação ou do mandado de execução da medida.
2. Créditos que fundamentam o pedido: constituídos definitivamente? impugnados? suspensos? inscritos? (processos administrativos e situação).
3. Hipótese do art. 2º invocada (ex.: débitos acima de 30% do patrimônio conhecido; alienação de bens; inscrição inapta).
4. Patrimônio real: balanço, ativo permanente × circulante, bens em nome de terceiros ou de sócios atingidos.
5. Quem foi atingido: pessoa jurídica, controlador, administradores — e quando cada um tinha poderes.
6. Bens bloqueados (lista, valores) e impacto operacional (estoque, caixa, folha).
7. Garantia que o cliente pode oferecer em substituição (depósito, fiança, seguro).
8. Se já há execução fiscal e, na cautelar preparatória, a data em que o crédito ficou irrecorrível.

## Prazo e contagem
- Contestação: 15 dias, contados da juntada do mandado de citação cumprido ou, se concedida liminar, da juntada do mandado de execução da medida (art. 8º).
- Revelia: fatos presumidos verdadeiros e decisão em 10 dias (art. 9º).
- Liminar: agravo de instrumento (art. 7º, parágrafo único) — prazo em `prazos-processuais`.
- Substituição por garantia: a qualquer tempo; Fazenda ouvida em 5 dias, silêncio = concordância (art. 10).
- Execução da dívida: 60 dias da irrecorribilidade administrativa, na cautelar preparatória (art. 11); fora disso, a medida perde eficácia (art. 13, I).

## Estrutura da peça
Tempestividade → requisitos ausentes (art. 3º) → inadequação da hipótese do art. 2º → limites da indisponibilidade (art. 4º) → perda de eficácia (arts. 11 e 13) → substituição por garantia (art. 10) → bens impenhoráveis → provas → pedidos. Roteiro em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Cabimento temporal**: a cautelar é instaurada após a constituição do crédito, inclusive no curso da execução; a constituição prévia é dispensada só nas hipóteses do art. 2º, V, "b", e VII (art. 1º e parágrafo único).
- **Prova exigida da Fazenda**: prova literal da constituição do crédito e prova documental de alguma hipótese do art. 2º (art. 3º). Sem as duas, indeferimento ou revogação.
- **Hipóteses (art. 2º)**: sem domicílio certo e intenção de ausentar-se ou alienar bens; ausência para fugir da obrigação; insolvente alienando bens; dívidas que comprometam a liquidez; após notificação, deixar de pagar no prazo **salvo exigibilidade suspensa** (V, "a") ou pôr bens em nome de terceiros (V, "b"); débitos acima de 30% do patrimônio conhecido (VI); alienar bens sem a comunicação exigida (VII); inscrição declarada inapta (VIII); outros atos que frustrem a satisfação do crédito (IX). Ataque a prova de cada elemento (ex.: no inciso VI, mostre o patrimônio real e os créditos com exigibilidade suspensa).
- **Limites da indisponibilidade (art. 4º)**: até o limite da obrigação; na pessoa jurídica, só o **ativo permanente** (§ 1º); extensão ao controlador e a quem tenha poderes para cumprir as obrigações fiscais, observado o marco do fato gerador (lançamento de ofício) ou do inadimplemento (§ 1º). Bloqueio de caixa, estoque ou recebíveis da PJ excede a lei.
- **Bem de família**: a jurisprudência do STJ não admite indisponibilidade em cautelar fiscal (AgInt no REsp 1.966.111, 2ª Turma, 2022).
- **Corresponsáveis fora da execução**: a cautelar contra eles tem caráter preparatório; sem redirecionamento da execução no prazo de 60 dias, perde a eficácia (AgInt no REsp 2.165.589, 2ª Turma, 2025).
- **Eficácia**: cessa se a execução não for proposta no prazo, não for efetivada em 30 dias, for extinta, ou se houver quitação; a Fazenda não pode repetir o pedido com o mesmo fundamento (art. 13). Indeferimento não impede a execução, salvo se acolhida extinção do crédito (pagamento, compensação, transação, remissão, prescrição, decadência) (art. 15).
- **Recursos**: apelação contra a sentença sem efeito suspensivo, salvo garantia do art. 10 (art. 17). Contra liminar, o recurso especial esbarra na Súmula 735/STF (AgInt no REsp 2.177.301, 1ª Turma, 2025): concentre-se no agravo e na contestação.

## Fundamentos verificados
Lei 8.397/1992, arts. 1º a 15 e 17; LEF art. 9º; Súmula 735/STF (como aplicada no AgInt no REsp 2.177.301); AgInt no REsp 1.966.111; AgInt no REsp 2.165.589. Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Revogação da liminar e improcedência do pedido cautelar.
- Subsidiariamente: limitação ao ativo permanente da PJ, ao valor da obrigação e aos responsáveis no marco temporal do art. 4º, § 1º; exclusão de bem de família e de bens de terceiros.
- Substituição da indisponibilidade por garantia (art. 10; LEF art. 9º).
- Declaração de perda de eficácia (arts. 11 e 13), se for o caso.
- Provas (perícia contábil sobre o patrimônio, documentos) e audiência (art. 9º).
- Valores e atualização: `juros-e-correcao`.

## Checklist pré-protocolo
- [ ] Data da juntada do mandado (citação ou execução da medida) e 15 dias contados
- [ ] Agravo contra a liminar avaliado em paralelo
- [ ] Situação de cada crédito (constituído, suspenso, impugnado) documentada
- [ ] Hipótese do art. 2º rebatida elemento a elemento
- [ ] Bens fora do ativo permanente identificados para liberação
- [ ] Marco temporal de cada administrador atingido
- [ ] Prazos dos arts. 11 e 13 conferidos
- [ ] Proposta de garantia substitutiva pronta

## Erros a evitar
- Perder o prazo de 15 dias contando da ciência em vez da juntada do mandado (ou o inverso, sem conferir).
- Discutir o mérito do tributo em vez dos requisitos da cautelar.
- Deixar de pedir a substituição por garantia, que a Fazenda só recusa motivadamente em 5 dias.
- Aceitar bloqueio de capital de giro da PJ sem invocar o limite do ativo permanente.
- Ignorar a perda de eficácia quando a execução não veio no prazo.

## Integração com o núcleo
`prazos-processuais`, `juros-e-correcao`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`, `civel-agravo-de-instrumento`.

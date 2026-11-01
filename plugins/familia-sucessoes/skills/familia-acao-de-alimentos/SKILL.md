---
name: familia-acao-de-alimentos
description: >
  Redige petição inicial de ação de alimentos (Lei 5.478/1968; CC arts. 1.694 a 1.710),
  inclusive alimentos gravídicos (Lei 11.804/2008) e alimentos avoengos, com pedido de
  provisórios. Use quando o usuário pedir ação de alimentos, pensão alimentícia, fixação
  de pensão, alimentos provisórios, alimentos gravídicos, pensão para gestante, alimentos
  contra avós, alimentos entre ex-cônjuges ou companheiros.
metadata:
  area: familia-sucessoes
  tipo_peca: inicial
  verificado_em: 2026-11-01
---
# Ação de alimentos (inicial)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: primeira fixação de alimentos para filho, ex-cônjuge, ex-companheiro, parente; alimentos gravídicos; ação contra avós (complementar).
- Não usar: alimentos já fixados que se quer mudar (use `familia-revisional-e-exoneracao-de-alimentos`); cobrança de parcelas atrasadas (use `familia-execucao-de-alimentos`); alimentos cumulados com investigação de paternidade (use `familia-investigacao-de-paternidade`, que remete a esta skill para o capítulo de alimentos).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Qualificação do alimentando e de quem o representa; idade; com quem reside.
2. Prova do vínculo: certidão de nascimento/casamento, prova da união estável; na gestação, indícios de paternidade (mensagens, fotos, testemunhas, exames).
3. Necessidades concretas, com documentos: escola, saúde, plano, moradia, alimentação, transporte, terapias.
4. Possibilidades do alimentante: emprego formal ou informal, empregador e endereço, padrão de vida visível (veículos, viagens, redes sociais), outros filhos.
5. Recursos do representante/genitor guardião (trinômio: proporcionalidade).
6. Endereço do réu para citação; dados bancários para depósito.
7. Comarca: domicílio do alimentando.

## Prazo e contagem
- Não há prazo decadencial para pedir; alimentos não pagos antes da citação não são devidos (os fixados retroagem à citação, Lei 5.478 art. 13 §2º).
- Gravídicos: réu responde em 5 dias (Lei 11.804 art. 7º). Demais prazos: ver despacho inicial (rito da Lei 5.478 ou CPC 693 e seguintes). Contagem com `prazos-processuais`.

## Estrutura da peça
Endereçamento (Vara de Família do domicílio do alimentando) → qualificação → gratuidade → segredo de justiça → fatos → direito (vínculo, necessidade, possibilidade, proporcionalidade) → alimentos provisórios → pedidos → provas → valor da causa. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Competência: foro do alimentando (CPC art. 53, II).
- Segredo de justiça (CPC art. 189, II).
- Valor da causa: 12 vezes a prestação pedida (CPC art. 292, III).
- MP intervém quando há incapaz (CPC art. 698); o MP também tem legitimidade ativa para alimentos de criança ou adolescente (Súmula 594 STJ).
- Avós: só em caráter complementar e subsidiário (Súmula 596 STJ); demonstrar a impossibilidade total ou parcial dos pais.

## Fundamentos verificados
- CC arts. 1.694 (necessidade x recursos), 1.695, 1.696 a 1.698 (ordem e concurso de obrigados), 1.701, 1.707 (irrenunciabilidade), 1.710 (atualização).
- Lei 5.478 arts. 1º, 2º, 4º (provisórios de plano), 13 §2º (retroação à citação).
- Lei 11.804 arts. 2º, 6º (indícios bastam; conversão automática em pensão ao filho).
- Súmulas STJ 594, 596 e 621 (efeitos retroativos da sentença de revisão/exoneração, sem compensação nem repetição). Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- [ ] Gratuidade; segredo de justiça; prioridade se houver criança.
- [ ] Alimentos provisórios em valor ou percentual definido.
- [ ] Ofício ao empregador para informar rendimentos (Lei 5.478 art. 5º §7º) e para desconto em folha.
- [ ] Definitivos em percentual sobre rendimentos líquidos (indicar se incidem sobre 13º, férias e verbas rescisórias) e, alternativamente, em salários mínimos para o caso de desemprego ou trabalho informal.
- [ ] Citação; intimação do MP; produção de provas; honorários.
- [ ] Atualização dos valores: aplicar `juros-e-correcao` (não escrever índice próprio).

## Checklist pré-protocolo
- [ ] Vínculo provado documentalmente (ou indícios, nos gravídicos).
- [ ] Planilha de despesas com comprovantes e cota do alimentante calculada.
- [ ] Base de incidência e forma de pagamento definidas sem ambiguidade.
- [ ] Pedido subsidiário para alimentante sem vínculo formal.
- [ ] Avós no polo passivo só com prova da insuficiência dos pais.
- [ ] Valor da causa = 12 prestações.

## Erros a evitar
- Pedir "30% do salário" sem dizer se é bruto ou líquido e quais verbas entram.
- Esquecer o pedido de provisórios: o juiz os fixa de plano, mas o valor sugerido orienta.
- Incluir avós como devedores principais.
- Prometer retroação a data anterior à citação.
- Descrever padrão de vida do réu sem nenhum elemento probatório (sinais exteriores de riqueza precisam de prova).

## Integração com o núcleo
`prazos-processuais` (prazos do despacho e do rito), `juros-e-correcao` (atualização e qualquer pedido condenatório), `verificacao-de-citacoes` (todo julgado acrescentado), `fidelidade-factual` (fatos e números do cliente), `estilo-forense` (redação final).

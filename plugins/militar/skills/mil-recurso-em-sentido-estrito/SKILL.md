---
name: mil-recurso-em-sentido-estrito
description: >
  Redige recurso em sentido estrito no processo penal militar (CPPM arts. 516 a
  525): cabimento pelas alíneas do art. 516, prazo de três dias para interpor e
  cinco para arrazoar, juízo de retratação, efeito suspensivo e traslado. Use
  quando o usuário pedir RESE na Justiça Militar contra decisão sobre prisão
  preventiva ou menagem, rejeição da denúncia, incompetência da Justiça Militar,
  extinção da punibilidade, prescrição, livramento condicional, sursis ou
  decisão que não recebeu apelação no CPPM.
metadata:
  area: militar
  tipo_peca: recurso
  verificado_em: 2026-11-25
---
# Recurso em sentido estrito no CPPM

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: decisão de juiz federal da JM, juiz de direito do juízo militar ou Conselho de Justiça que se enquadre numa das alíneas do art. 516 do CPPM.
- Não usar: sentença definitiva de condenação ou absolvição — apelação (art. 526; quando cabível apelação, não cabe RESE, nem de parte da decisão — art. 526, parágrafo único); prisão a desfazer com urgência — `mil-habeas-corpus` pode correr junto; processo comum — `penal-recurso-em-sentido-estrito`.

## Entradas mínimas (perguntar o que faltar; nunca supor fatos)
1. Decisão recorrida integral e certidão de intimação (ou data da leitura em audiência).
2. Quem recorre (defesa, MP, assistente) e o interesse recursal.
3. Peças de que se precisa traslado, se o recurso não subir nos próprios autos.
4. Fatos e provas que sustentam a reforma.

## Prazo e contagem
- Interposição: três dias da intimação, da publicação ou da leitura em audiência com as partes presentes (art. 518), por requerimento que indica as peças a trasladar.
- Traslado: dez dias, prorrogável até o dobro (arts. 518, parágrafo único, e 521).
- Razões: cinco dias da vista dos autos ou do traslado; depois, igual prazo ao recorrido (art. 519).
- Retratação: juiz ou Conselho tem cinco dias para reformar ou sustentar (art. 520). Reformada a decisão, a parte prejudicada recorre por simples petição (art. 520, parágrafo único).
- Contagem, início e feriados: `prazos-processuais`.

## Estrutura da peça
Petição de interposição (alínea do art. 516, tempestividade, peças a trasladar, pedido de retratação) + razões ao tribunal (STM na JMU; TJ ou TJM na JME). Roteiro em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Cabimento taxativo: indicar a alínea exata do art. 516. As mais usadas pela defesa: h (decretar, ou não, a preventiva, ou revogá-la), i (menagem), e (incompetência), f (procedência de exceção, salvo suspeição), l (indeferir prescrição ou extinção da punibilidade), m (livramento condicional e suspensão condicional da pena), q (não receber a apelação ou o recurso).
- Efeito suspensivo: em regra não há; há nos recursos sobre competência, extinção da ação penal e concessão de livramento condicional (art. 516, parágrafo único). Precisa de efeito imediato fora disso? Avaliar `mil-habeas-corpus`.
- Sobem nos próprios autos os recursos das alíneas a, b, d, e, i, j, m, n e p (art. 517); nos demais, requerer o traslado com a interposição.
- No tribunal: vista ao procurador-geral por oito dias e sustentação oral de dez minutos (arts. 523 e 524).

## Fundamentos verificados
- CPPM arts. 516 a 526 e 529 (prazo da apelação, para distinguir); CF art. 125, § 3º (segundo grau da JME); Lei 8.457/1992, art. 6º, II, c (STM julga recursos das decisões de primeiro grau).
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Na interposição: recebimento, traslado das peças indicadas (se for o caso) e retratação (art. 520).
- Nas razões: conhecimento e provimento para reformar a decisão (revogar a preventiva, conceder menagem, receber ou rejeitar a denúncia, declarar extinta a punibilidade etc.).
- Efeito suspensivo, só nas hipóteses do art. 516, parágrafo único.

## Checklist pré-protocolo
- [ ] Alínea do art. 516 identificada e transcrita
- [ ] Não é caso de apelação (art. 526, parágrafo único)
- [ ] Interposição em três dias, contados da intimação certificada
- [ ] Peças de traslado listadas (se não sobe nos próprios autos)
- [ ] Razões em cinco dias após a vista
- [ ] Pedido de retratação feito ao juízo de origem

## Erros a evitar
- Interpor no prazo de cinco dias da apelação: o RESE do CPPM é de três.
- Esquecer de indicar as peças de traslado e o recurso subir incompleto.
- Pedir efeito suspensivo fora das hipóteses legais em vez de impetrar HC.
- Usar RESE contra sentença definitiva.

## Integração com o núcleo
`prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

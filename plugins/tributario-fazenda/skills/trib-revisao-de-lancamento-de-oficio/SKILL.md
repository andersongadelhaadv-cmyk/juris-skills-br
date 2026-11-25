---
name: trib-revisao-de-lancamento-de-oficio
description: >
  Orienta e redige pedido de revisão de lançamento tributário fora do rito da
  impugnação (CTN arts. 145 e 149) e a defesa contra revisão feita pelo Fisco,
  distinguindo erro de fato (revisável) de erro de direito ou mudança de
  critério jurídico (art. 146) e controlando a decadência (arts. 149, parágrafo
  único, e 173). Use quando o usuário pedir revisão de ofício de lançamento,
  revisão de débito por erro de fato, cancelamento de lançamento após perder o
  prazo de impugnação, lançamento complementar ou suplementar do Fisco,
  mudança de critério jurídico ou revisão de débito inscrito em dívida ativa.
metadata:
  area: tributario-fazenda
  tipo_peca: requerimento
  verificado_em: 2026-11-25
---
# Revisão de lançamento de ofício

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: (a) o contribuinte perdeu o prazo de impugnação, mas há erro de fato demonstrável (dado cadastral, base de cálculo, duplicidade, pagamento não considerado) e quer que a autoridade reveja de ofício; (b) o Fisco fez lançamento complementar ou revisou o anterior e é preciso atacar a revisão (erro de direito, mudança de critério, decadência); (c) revisão de débito já inscrito, por petição à procuradoria.
- Não usar: lançamento notificado e ainda dentro do prazo de defesa — impugne (`trib-defesa-administrativa-e-carf`), porque só a impugnação suspende a exigibilidade (CTN art. 151, III); revisão já negada e é preciso ir a juízo — `trib-acao-anulatoria` ou `trib-mandado-de-seguranca`; débito em execução — `trib-excecao-pre-executividade-fiscal` ou `trib-embargos-a-execucao-fiscal`.

## Entradas mínimas (perguntar o que faltar; nunca supor fatos)
1. Lançamento original e eventual lançamento revisado: data da notificação, tributo, período, valores, fundamentação.
2. O que está errado e qual a prova (documento, cadastro, laudo, comprovante de pagamento).
3. Se o erro era conhecido ou comprovável pelo Fisco na época do lançamento (decisivo para erro de fato x erro de direito).
4. Data do fato gerador, se houve declaração e pagamento antecipado (cálculo da decadência).
5. Situação atual: em cobrança, inscrito, ajuizado, parcelado.
6. Ente tributante e lei processual local (a revisão de ofício pode ter rito próprio).

## Prazo e contagem
- A revisão só pode começar enquanto não extinto o direito da Fazenda (art. 149, parágrafo único): 5 anos do art. 173 — com pagamento antecipado em tributo por homologação, o termo inicial pode ser outro [VERIFICAR: art. 150, § 4º, não conferido nesta skill].
- O pedido de revisão de ofício, em regra, **não** suspende a exigibilidade nem reabre o prazo de impugnação [VERIFICAR a lei do ente]; avaliar garantia ou tutela judicial em paralelo.
- Prazos processuais: `prazos-processuais`.

## Estrutura da peça
Pedido do contribuinte: endereçamento → lançamento e erro → enquadramento no art. 149 (especialmente VIII) → prova → decadência não consumada para a revisão a favor (ou consumada contra a revisão do Fisco) → pedidos. Defesa contra revisão do Fisco: vedação de revisar por erro de direito / mudança de critério (art. 146) → decadência (art. 149, p.ú.) → nulidade. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- O lançamento notificado só se altera por impugnação, recurso de ofício ou iniciativa de ofício nos casos do art. 149 (art. 145).
- Erro de fato (fato não conhecido ou não provado no lançamento anterior, art. 149, VIII) autoriza revisão; erro de direito não (AgInt no AREsp 1.765.140, STJ, que remete ao repetitivo REsp 1.130.545/RJ [VERIFICAR: repetitivo não localizado diretamente no JuriBase]).
- O erro de fato exige desconhecimento ou impossibilidade de comprovação à época (AREsp 2.362.445, STJ).
- Mudança de critério jurídico só vale para fatos geradores posteriores (art. 146, redação da LC 236/2026).
- Revisão após o prazo decadencial é inválida (AgInt no REsp 2.097.919, STJ).
- Autotutela: a Administração pode anular atos ilegais (Súmula 473 STF) — fundamento para pedir a revisão a favor do contribuinte.

## Fundamentos verificados
- CTN arts. 145, 146, 149 (I a IX e parágrafo único), 151, III, 173.
- Súmula 473 do STF; STJ: AgInt no AREsp 1.765.140; AREsp 2.362.445; AgInt no REsp 2.097.919.
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Revisão de ofício do lançamento para excluir/reduzir o valor, com cancelamento da parte indevida.
- Suspensão de atos de cobrança enquanto analisado [VERIFICAR previsão na norma do ente; se não houver, buscar garantia ou tutela judicial].
- Cancelamento de inscrição em dívida ativa e emissão de certidão, se o débito sair.
- Contra revisão do Fisco: anulação do lançamento revisado por erro de direito, mudança de critério ou decadência.
- Valores: `juros-e-correcao`.

## Checklist pré-protocolo
- [ ] Verificado se o prazo de impugnação ainda corre (se corre, impugne)
- [ ] Erro classificado como de fato, com prova documental
- [ ] Decadência calculada com termo inicial correto
- [ ] Rito e autoridade do ente identificados
- [ ] Medida paralela para suspender a cobrança avaliada
- [ ] Precedentes lidos na íntegra antes de citar

## Erros a evitar
- Usar a revisão de ofício como substituta da impugnação no prazo.
- Pedir revisão com base em nova interpretação jurídica (erro de direito) — será negada pelo mesmo fundamento que protege o contribuinte contra o Fisco.
- Ignorar a decadência quando o Fisco revisa o lançamento para cobrar mais.
- Supor que o pedido suspende a exigibilidade.

## Integração com o núcleo
`juros-e-correcao`, `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`. Vizinhas: `trib-defesa-administrativa-e-carf`, `trib-acao-anulatoria`, `adm-anulacao-de-ato-por-autotutela` (ato administrativo não tributário).

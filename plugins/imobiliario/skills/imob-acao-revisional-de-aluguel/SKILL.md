---
name: imob-acao-revisional-de-aluguel
description: >
  Redige ação revisional de aluguel da Lei 8.245/1991 (arts. 19 e 68 a 70),
  proposta pelo locador para elevar ou pelo locatário para reduzir o aluguel
  ao preço de mercado, com pedido de aluguel provisório e perícia de
  avaliação. Use quando o usuário pedir revisão do valor do aluguel após três
  anos, aluguel defasado ou acima do mercado, aluguel provisório, contestação
  com contraproposta em revisional ou execução das diferenças após a sentença.
metadata:
  area: imobiliario
  tipo_peca: inicial
  verificado_em: 2026-11-25
---
# Ação revisional de aluguel

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: locação urbana (residencial ou não residencial) com mais de três anos de vigência do contrato ou do último acordo/fixação judicial do aluguel, sem acordo entre as partes, e o objetivo é ajustar o valor ao preço de mercado (art. 19).
- Não usar: renovação do contrato comercial ao fim do prazo (`imob-acao-renovatoria` — lá o aluguel é fixado na própria renovatória); despejo (`imob-acao-de-despejo`); discussão de índice de reajuste ou de cobrança indevida sem revisão do valor-base (`civel-peticao-inicial`); desequilíbrio por fato superveniente fora da lógica de mercado do art. 19 (revisão contratual do Código Civil — `contratos-analise-e-revisao-de-contrato`).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Contrato, aditivos e histórico de valores: data de início e data do último acordo ou da última fixação judicial do aluguel.
2. Quem propõe (locador ou locatário) e o valor de aluguel pretendido.
3. Elementos de mercado: laudo ou parecer de avaliação, anúncios e locações comparáveis (com fonte e data).
4. Existe prazo de desocupação pendente ou ajustado (notificação de denúncia, acordo, sentença)? (art. 68, § 1º).
5. Contrato do art. 54-A (imóvel construído ou reformado sob medida) com renúncia à revisão?
6. Índice e periodicidade de reajuste do contrato.

## Prazo e contagem
- Triênio do art. 19: três anos de vigência do contrato ou do acordo anterior. O STJ conta o triênio da última fixação judicial do aluguel (AREsp 2.888.116); ausente o triênio, há carência de ação.
- Pedido de revisão do aluguel provisório (art. 68, III) interrompe o prazo para recorrer da decisão que o fixou (art. 68, V).
- Prazos processuais correm nas férias forenses (art. 58, I); contagem em `prazos-processuais`.

## Estrutura da peça
Endereçamento (foro do imóvel, salvo eleição — art. 58, II) → contrato e histórico de valores → triênio → defasagem em relação ao mercado → valor pretendido (art. 68, I) → aluguel provisório (art. 68, II) → perícia → pedidos → valor da causa (12 meses de aluguel — art. 58, III). Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Procedimento: a lei fala em rito sumário; por força do art. 1.049, parágrafo único, do CPC, aplica-se o procedimento comum com as modificações da lei especial (art. 68).
- A inicial deve indicar o valor do aluguel cuja fixação se pretende (art. 68, I).
- Não cabe revisional na pendência de prazo para desocupação (arts. 46, § 2º, e 57) ou quando esse prazo foi estipulado amigável ou judicialmente (art. 68, § 1º).
- No art. 54-A (locação não residencial sob medida), é válida a renúncia ao direito de revisão durante a vigência (§ 1º).
- Partes podem, a qualquer tempo, fixar novo valor ou alterar a cláusula de reajuste por acordo (art. 18) — tentar antes de ajuizar.

## Fundamentos verificados
- Lei 8.245/1991: arts. 18, 19, 54-A, 58, 68, 69, 70; CPC, art. 1.049, parágrafo único.
- Aluguel provisório, devido desde a citação: em ação do locador, até 80% do pedido; em ação do locatário, não inferior a 80% do aluguel vigente (art. 68, II, a e b); reajustado na periodicidade pactuada ou legal (§ 2º).
- Contestação com contraproposta, se houver discordância do valor (art. 68, IV).
- Aluguel da sentença retroage à citação; diferenças, descontados os provisórios pagos, exigíveis após o trânsito em julgado e executadas nos autos (art. 69 e § 2º).
- A pedido do locador, a sentença pode fixar periodicidade de reajuste e indexador diversos (art. 69, § 1º).
- Triênio contado da última fixação judicial (STJ, AREsp 2.888.116).
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Fixação de aluguel provisório (com os limites do art. 68, II), desde a citação.
- Designação de audiência de conciliação e, frustrada, perícia de avaliação do valor locativo.
- Fixação do novo aluguel no valor indicado (ou no apurado), retroativo à citação.
- Pagamento das diferenças após o trânsito, com execução nos autos (art. 69, § 2º); correção e juros pelo núcleo `juros-e-correcao`.
- Se o autor for o locador: periodicidade e/ou indexador diversos (art. 69, § 1º).
- Custas e honorários.

## Checklist pré-protocolo
- [ ] Triênio comprovado a partir do contrato, do último acordo ou da última fixação judicial
- [ ] Nenhum prazo de desocupação pendente ou ajustado
- [ ] Contrato não é art. 54-A com renúncia à revisão
- [ ] Valor pretendido indicado na inicial
- [ ] Laudo/parecer de mercado com comparativos identificados
- [ ] Pedido de aluguel provisório dentro dos limites de 80%
- [ ] Valor da causa: 12 meses de aluguel
- [ ] Juros e correção remetidos ao núcleo

## Erros a evitar
- Contar o triênio do início do contrato quando houve acordo ou fixação judicial posterior.
- Confundir revisão (valor-base de mercado) com reajuste (índice) — a revisional não serve para trocar índice sem discutir o valor.
- Pedir aluguel provisório acima de 80% do pedido (locador) ou abaixo de 80% do vigente (locatário).
- Ajuizar revisional depois de notificado para desocupar ou com acordo de saída (art. 68, § 1º).
- Exigir as diferenças antes do trânsito em julgado (art. 69).

## Integração com o núcleo
`juros-e-correcao`, `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

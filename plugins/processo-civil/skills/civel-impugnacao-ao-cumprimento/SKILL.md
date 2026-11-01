---
name: civel-impugnacao-ao-cumprimento
description: >
  Redige impugnação ao cumprimento de sentença (CPC art. 525; Fazenda, art. 535)
  com as matérias do §1º, excesso de execução com valor e demonstrativo (§§4º e
  5º) e pedido de efeito suspensivo (§6º). Use quando o usuário pedir impugnação
  ao cumprimento de sentença, defesa do executado na fase de cumprimento,
  alegar excesso de execução, inexigibilidade do título ou prescrição posterior à
  sentença.
metadata:
  area: processo-civil
  tipo_peca: impugnacao
  verificado_em: 2026-11-01
---
# Impugnação ao cumprimento de sentença

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: executado intimado em cumprimento definitivo ou provisório (art. 520, §1º) de quantia; também, no que couber, em obrigação de fazer/não fazer (art. 536, §4º).
- Fazenda Pública: impugnação do art. 535 (30 dias).
- Não usar: execução de título extrajudicial (embargos — `civel-embargos-a-execucao`); fato superveniente ao prazo ou vício de penhora posterior (simples petição — art. 525, §11); matéria de ordem pública sem prova a produzir fora do prazo (avaliar `civel-excecao-de-pre-executividade` ou petição do art. 518).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
- Requerimento de cumprimento, demonstrativo do exequente e decisão que mandou intimar.
- Data da intimação para pagar (início dos 15 dias) e se houve pagamento parcial.
- Título exequendo e seus parâmetros (índices, termo inicial, honorários).
- Fatos extintivos posteriores à sentença (pagamento, novação, compensação, transação, prescrição).
- Bens já penhorados e se há garantia para pedir efeito suspensivo.

## Prazo e contagem
- 15 dias úteis, iniciados automaticamente ao fim do prazo de pagamento voluntário, sem nova intimação e independentemente de penhora (art. 525, caput).
- Litisconsortes com advogados distintos: dobra só em autos físicos (§3º c/c art. 229, §2º).
- Fazenda: 30 dias (art. 535). Use `prazos-processuais`.

## Estrutura da peça
Endereçamento nos próprios autos → tempestividade → síntese do cumprimento → matérias do §1º, cada uma em tópico → excesso com valor correto e planilha → efeito suspensivo → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Matérias admitidas (art. 525, §1º): falta/nulidade de citação em processo revel; ilegitimidade; inexequibilidade ou inexigibilidade; penhora incorreta ou avaliação errônea; excesso ou cumulação indevida; incompetência; causa modificativa ou extintiva superveniente à sentença.
- Excesso: declarar de imediato o valor correto com demonstrativo (§4º); sem isso, rejeição liminar se for o único fundamento (§5º).
- Efeito suspensivo: só com garantia do juízo (penhora, caução ou depósito) + fundamentos relevantes + risco de dano grave (§6º).
- Inexigibilidade por decisão do STF (§§12 a 15): a decisão do STF deve ser anterior ao trânsito; se posterior, a via é a rescisória.
- Impedimento e suspeição seguem os arts. 146 e 148 (§2º).

## Fundamentos verificados
CPC arts. 518, 520, §1º, 523, 525, 535, 854, §3º; Súmulas 517 e 519 do STJ. Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Efeito suspensivo (garantido o juízo).
- Acolhimento para extinguir o cumprimento, reconhecer a inexigibilidade ou reduzir ao valor correto.
- Liberação do excesso penhorado; honorários em favor do executado se acolhida a impugnação.
- Valor incontroverso: depósito ou indicação, para evitar multa sobre essa parte (art. 523, §2º).

## Checklist pré-protocolo
- [ ] Prazo contado a partir do fim dos 15 dias de pagamento.
- [ ] Cada matéria enquadrada em inciso do §1º.
- [ ] Causas extintivas posteriores à sentença (não reabrir o mérito).
- [ ] Excesso com valor declarado e planilha discriminada (gerada por `juros-e-correcao`).
- [ ] Garantia do juízo comprovada, se pedido efeito suspensivo.
- [ ] Impenhorabilidade de valores bloqueados alegada em 5 dias (art. 854, §3º), se for o caso.

## Erros a evitar
- Rediscutir o mérito já decidido (coisa julgada).
- Alegar excesso sem apontar o valor e sem planilha: rejeição liminar.
- Pedir efeito suspensivo sem garantia.
- Perder o prazo de 5 dias do art. 854, §3º, para a impenhorabilidade do valor bloqueado.
- Contar o prazo da intimação para pagar, e não do fim do prazo de pagamento.

## Integração com o núcleo
- `juros-e-correcao` para refazer o cálculo e demonstrar o excesso.
- `prazos-processuais` para os prazos encadeados (pagamento, impugnação, art. 854).
- `verificacao-de-citacoes` para precedentes e decisões do STF invocadas nos §§12 a 15.
- `fidelidade-factual` e `estilo-forense` na revisão.

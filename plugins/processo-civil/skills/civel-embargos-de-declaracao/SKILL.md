---
name: civel-embargos-de-declaracao
description: >
  Redige embargos de declaração cíveis (CPC arts. 1.022 a 1.026) contra
  omissão, contradição, obscuridade ou erro material, inclusive para
  prequestionamento (art. 1.025) e com pedido de efeito modificativo. Use quando
  o usuário pedir embargos de declaração, embargos declaratórios, "aclaratórios",
  "ED", sanar omissão da sentença ou do acórdão, ou prequestionar para REsp/RE.
metadata:
  area: processo-civil
  tipo_peca: embargos-declaracao
  verificado_em: 2026-11-01
---
# Embargos de declaração (cível)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: contra qualquer decisão judicial (art. 1.022) — sentença, interlocutória, decisão monocrática, acórdão — com vício de obscuridade, contradição, omissão ou erro material.
- Usar para prequestionar matéria que o tribunal não enfrentou, antes do REsp/RE.
- Não usar para rediscutir o mérito sem vício: o risco é multa (art. 1.026, §2º).
- Juizado especial: mesma hipótese, prazo de 5 dias (Lei 9.099, arts. 48 a 50).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
- Íntegra da decisão e data da intimação/publicação.
- Trecho exato da peça anterior em que o ponto omitido foi suscitado (folha/ID).
- Dispositivos legais ou constitucionais a prequestionar.
- Se haverá REsp/RE depois e se a outra parte já recorreu.

## Prazo e contagem
- 5 dias úteis (art. 1.023 c/c art. 219); sem preparo.
- Prazo em dobro para litisconsortes com advogados distintos só em autos físicos (art. 1.023, §1º, c/c art. 229, §2º); Fazenda, MP e Defensoria em dobro.
- Interrompem o prazo dos demais recursos para ambas as partes (art. 1.026, caput).
- Contrarrazões em 5 dias se houver efeito modificativo (art. 1.023, §2º).
- Use `prazos-processuais`.

## Estrutura da peça
Endereçamento ao prolator → tempestividade → cabimento → um tópico por vício (onde está, o que deveria constar, por que importa) → prequestionamento → efeito modificativo (se houver) → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Indicação precisa do vício (art. 1.023, caput). Omissão inclui não enfrentar tese de repetitivo ou IAC aplicável e qualquer conduta do art. 489, §1º (art. 1.022, p.ú.).
- Prequestionamento ficto (art. 1.025): o tribunal superior considera incluídos os elementos suscitados, se reconhecer o vício. Para o STJ aplicar o art. 1.025, o REsp precisa alegar violação ao art. 1.022 (orientação conferida em julgados de 2022 a 2026; ver fundamentos).
- Em tribunal: o relator apresenta em mesa na sessão seguinte; não julgados nela, inclusão automática em pauta (art. 1.024, §1º).

## Fundamentos verificados
CPC arts. 489, §1º, 1.022 a 1.026; Lei 9.099, arts. 48 a 50; Súmulas 98, 211 e 579 do STJ; 282 e 356 do STF. Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Conhecimento e acolhimento para sanar cada vício apontado.
- Efeito modificativo, quando o saneamento altera o resultado, com intimação do embargado (art. 1.023, §2º).
- Declaração expressa sobre os dispositivos indicados, para fins de prequestionamento.
- Se cabível: suspensão da eficácia da decisão (art. 1.026, §1º).

## Checklist pré-protocolo
- [ ] Prazo de 5 dias úteis conferido.
- [ ] Cada vício com localização na decisão e na peça em que foi suscitado.
- [ ] Dispositivos a prequestionar listados nominalmente.
- [ ] Nenhum argumento novo, não suscitado antes (salvo matéria de ordem pública).
- [ ] Linguagem que mostra vício, não inconformismo.
- [ ] Se os ED forem do tribunal: anotar a sessão subsequente para acompanhar a inclusão automática em pauta.

## Erros a evitar
- ED "de inconformismo": geram multa de até 2% do valor atualizado da causa; reiteração, até 10% e depósito prévio para recorrer (art. 1.026, §§2º e 3º).
- Terceiros ED após dois considerados protelatórios: não são admitidos (§4º).
- Deixar de alegar violação ao art. 1.022 no REsp quando o tribunal manteve a omissão: o STJ aplica a Súmula 211.
- Ratificar desnecessariamente o recurso já interposto (art. 1.024, §5º; Súmula 579 do STJ).
- Apontar "omissão" sobre argumento incapaz de infirmar a conclusão sem explicar a relevância.

## Integração com o núcleo
- `prazos-processuais` para o prazo de 5 dias e a interrupção.
- `verificacao-de-citacoes` para precedentes que se queira apontar como não enfrentados.
- `fidelidade-factual` para os trechos citados da decisão.
- `estilo-forense` para manter tom técnico e objetivo.

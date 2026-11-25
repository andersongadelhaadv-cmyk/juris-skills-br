---
name: prev-embargos-de-declaracao-previdenciarios
description: >
  Redige embargos de declaração contra sentença ou acórdão em causa
  previdenciária, no procedimento comum (CPC, arts. 1.022 a 1.026) ou no JEF
  (Lei 9.099, arts. 48 a 50), com foco em omissões típicas — período especial
  ou rural não examinado, reafirmação da DER, DIB, tese repetitiva ignorada — e
  no prequestionamento para REsp, RE ou pedido de uniformização. Use quando o
  usuário pedir embargos de declaração previdenciários, aclaratórios contra o
  INSS, prequestionar para a TNU ou STJ, ou sanar omissão de sentença de benefício.
metadata:
  area: previdenciario
  tipo_peca: recurso
  verificado_em: 2026-11-25
---
# Embargos de declaração previdenciários

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: sentença ou acórdão (TRF, Turma Recursal) que deixou de examinar um período, um agente nocivo, um pedido subsidiário (reafirmação da DER, melhor benefício), a DIB, os honorários, ou que ignorou tese repetitiva aplicável; contradição entre fundamentação e dispositivo; erro material em datas, NB ou períodos.
- Usar para prequestionar dispositivo federal ou constitucional antes de REsp/RE (`civel-recurso-especial`, `civel-recurso-extraordinario`) ou antes do pedido de uniformização (`prev-pedido-de-uniformizacao-tnu`).
- Não usar para rediscutir prova ou mérito já enfrentado: o caminho é `prev-apelacao-previdenciaria` ou o recurso próprio. Técnica geral: `civel-embargos-de-declaracao`.

## Entradas mínimas (perguntar o que faltar; nunca supor fatos)
1. Decisão embargada integral e data da intimação.
2. Onde, nos autos, o ponto omitido foi suscitado (petição, folha/ID) — sem isso não há omissão.
3. Lista de pedidos e de períodos da inicial, para conferir um a um contra o dispositivo.
4. Se o objetivo é recurso a tribunal superior ou à TNU: quais dispositivos e teses precisam constar.
5. Juízo: procedimento comum (CPC) ou JEF (Lei 9.099).

## Prazo e contagem
- 5 dias, no CPC (art. 1.023) e no JEF (Lei 9.099, art. 49). O prazo é em dias úteis no CPC; no JEF, conferir a regra de contagem aplicável em `prazos-processuais`.
- Interrompem o prazo do recurso principal (CPC, art. 1.026; Lei 9.099, art. 50).
- O INSS tem prazo em dobro fora do JEF (CPC, art. 183); no JEF, não (Lei 10.259, art. 9º).

## Estrutura da peça
Endereçamento ao prolator → tempestividade → decisão embargada → um tópico por vício (omissão, contradição, obscuridade, erro material), cada um com o trecho da decisão e a peça em que o ponto foi suscitado → prequestionamento → pedido de efeito modificativo, se houver → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Cabimento: obscuridade, contradição, omissão e erro material (CPC, art. 1.022); no JEF, as mesmas hipóteses por remissão ao CPC (Lei 9.099, art. 48).
- É omissa a decisão que não se manifesta sobre tese de repetitivo ou IAC aplicável, ou que incorre em fundamentação deficiente (CPC, art. 1.022, parágrafo único, I e II). Em matéria previdenciária, os repetitivos são frequentes (Temas 995, 1124 e 1105 do STJ, por exemplo).
- Pedido de efeito modificativo exige intimação do embargado (CPC, art. 1.023, § 2º).
- Prequestionamento ficto: consideram-se incluídos no acórdão os elementos suscitados, se o tribunal superior reconhecer o vício (CPC, art. 1.025). Mesmo assim, as Súmulas 282 e 356/STF e 211/STJ seguem sendo invocadas pelos tribunais: embargue e, se a omissão persistir, alegue no REsp violação ao art. 1.022.
- Multa de até 2% se manifestamente protelatórios (CPC, art. 1.026, § 2º).

## Fundamentos verificados
- CPC, arts. 183, 1.022 a 1.026; Lei 9.099, arts. 48 a 50; Lei 10.259, arts. 1º e 9º.
- Súmula 282/STF, Súmula 356/STF, Súmula 211/STJ.
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Acolhimento para sanar a omissão/contradição/obscuridade/erro material apontados.
- Efeito modificativo, com intimação do INSS (art. 1.023, § 2º), quando a correção alterar o resultado (ex.: período omitido completa o tempo).
- Manifestação expressa sobre os dispositivos X, Y e Z, para fins de prequestionamento.
- Correção de erro material (datas, NB, períodos).

## Checklist pré-protocolo
- [ ] Cada vício aponta o trecho da decisão e a peça em que o ponto foi suscitado
- [ ] Pedidos e períodos da inicial conferidos um a um contra o dispositivo
- [ ] Tese repetitiva aplicável citada com número e tribunal
- [ ] Dispositivos para prequestionamento listados de forma objetiva
- [ ] Pedido de efeito modificativo, se for o caso
- [ ] Prazo de 5 dias conferido e regime certo (CPC x JEF)

## Erros a evitar
- Embargar para reabrir valoração da prova (PPP "mal lido", laudo "errado"): isso é apelação, e o risco de multa cresce.
- Apontar "omissão" sobre argumento nunca deduzido nos autos.
- Deixar de embargar o acórdão e depois ver o REsp barrado por falta de prequestionamento (Súmula 211/STJ).
- Protocolar no limite sem conferir o prazo, contando com a interrupção: se os embargos forem tidos por intempestivos, o recurso principal fica em risco [VERIFICAR: efeito de embargos intempestivos sobre o prazo, via `verificacao-de-citacoes`].

## Integração com o núcleo
`prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

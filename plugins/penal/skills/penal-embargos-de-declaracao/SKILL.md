---
name: penal-embargos-de-declaracao
description: >
  Redige embargos de declaração em matéria criminal contra sentença (CPP art. 382)
  e contra acórdão (CPP arts. 619 e 620), no prazo de 2 dias corridos, e no Juizado
  Especial Criminal (Lei 9.099/1995, art. 83), para sanar ambiguidade, obscuridade,
  contradição, omissão ou erro material e prequestionar matéria para recurso
  especial ou extraordinário. Use quando o usuário pedir embargos declaratórios
  penais, aclaratórios em processo criminal, sentença ou acórdão omisso,
  prequestionamento, efeitos infringentes ou correção de erro material na pena.
metadata:
  area: penal
  tipo_peca: recurso
  verificado_em: 2026-11-25
---
# Embargos de declaração penais

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: (a) sentença criminal com obscuridade, ambiguidade, contradição ou omissão (CPP 382); (b) acórdão de câmara ou turma com os mesmos vícios (CPP 619); (c) sentença ou acórdão do JECRIM (Lei 9.099, art. 83); (d) erro material (pena somada errado, regime incompatível com a pena fixada); (e) prequestionar tese para REsp/RE.
- Não usar: rediscutir prova ou mérito já decidido (use `penal-apelacao-criminal`, `penal-recurso-em-sentido-estrito`); voto vencido favorável ao réu em acórdão não unânime (`penal-embargos-infringentes-e-de-nulidade`); processo cível ou trabalhista (`civel-embargos-de-declaracao`, `trabalhista-embargos-de-declaracao`).

## Entradas mínimas (perguntar o que faltar; nunca supor fatos)
1. Íntegra da decisão embargada e data da intimação ou da publicação.
2. Rito: comum/júri (CPP) ou JECRIM (Lei 9.099).
3. Pontos exatos: qual pedido ou tese não foi apreciado; onde está a contradição (entre fundamentos, ou entre fundamento e dispositivo).
4. Peças em que a tese omitida foi suscitada (página/ID), para provar que a omissão é real.
5. Recurso seguinte pretendido (apelação, REsp, RE, HC) e se a meta é prequestionar.

## Prazo e contagem
- CPP: 2 dias da intimação da sentença (382) ou da publicação do acórdão (619). O prazo é corrido: o STJ não aplica o prazo nem a contagem em dias úteis do CPC (EDcl no AgRg nos EAREsp 2.436.660, Terceira Seção, 2025), e conta pelo art. 798 do CPP (exclui o dia do começo, inclui o do vencimento, prorroga se cair em domingo ou feriado).
- JECRIM: 5 dias da ciência da decisão, por escrito ou oralmente; os embargos interrompem o prazo para recurso (Lei 9.099, art. 83, §§ 1º e 2º).
- Efeito sobre o prazo do recurso seguinte no rito do CPP: o CPP não regula; embargos não conhecidos (intempestivos ou inadmitidos) não interrompem o prazo, e o recurso posterior fica intempestivo (AgRg no AREsp 2.697.783, STJ, 2025). Não conte com interrupção se houver risco de não conhecimento.
- Recesso: suspensão entre 20/12 e 20/01, salvo réu preso e Maria da Penha (CPP 798-A). Detalhes: `prazos-processuais`.

## Estrutura da peça
Endereçamento (juiz prolator ou relator) → tempestividade → cabimento → vícios, um tópico por vício, com transcrição do trecho → efeitos (integrativo; infringente, se a correção altera o resultado) → prequestionamento → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Petição deve indicar os pontos em que a decisão é ambígua, obscura, contraditória ou omissa; sem isso o relator indefere de plano (CPP 620 e §2º). Julgamento na primeira sessão, sem revisão (620 §1º).
- Erro material é admitido pela jurisprudência do STJ, inclusive com modificação excepcional do julgado (EDcl no AgRg nos EAREsp 2.361.087, Corte Especial, 2024).
- Contradição relevante é interna à decisão — não entre a decisão e a prova ou a jurisprudência.
- Omissão relevante: pedido ou tese suscitada e não apreciada, capaz de mudar o resultado; ou fundamento sem enfrentamento (CF art. 93, IX).
- Prequestionamento: ponto omisso sem embargos não sobe em RE (Súmula 356 do STF); questão não apreciada mesmo após embargos inviabiliza REsp (Súmula 211 do STJ) — nesse caso o REsp deve alegar violação ao art. 619 do CPP. Embargos com notório propósito de prequestionar não são protelatórios (Súmula 98 do STJ).

## Fundamentos verificados
CPP arts. 382, 619, 620, 798 e 798-A; Lei 9.099/1995, art. 83; CF art. 93, IX; Súmula 356 do STF; Súmulas 98 e 211 do STJ; precedentes do STJ sobre prazo corrido, erro material e não interrupção. Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Conhecimento e acolhimento para sanar cada vício apontado.
- Efeitos infringentes, quando a correção alterar o resultado — com pedido de intimação da parte contrária para responder [VERIFICAR: exigência no rito penal conforme o regimento do tribunal].
- Pronunciamento expresso sobre os dispositivos indicados, para fins de prequestionamento.
- Correção do erro material (pena, regime, detração, substituição).

## Checklist pré-protocolo
- [ ] Prazo de 2 dias corridos (ou 5, no JECRIM) contado pelo art. 798
- [ ] Cada vício ligado a um trecho transcrito da decisão
- [ ] Prova de que a tese omitida foi suscitada antes (ID/página)
- [ ] Dispositivos a prequestionar listados
- [ ] Sem rediscussão de prova ou de mérito puro
- [ ] Recurso seguinte calendarizado sem depender de interrupção duvidosa

## Erros a evitar
- Usar o prazo de 5 dias úteis do CPC no processo penal comum — os embargos não são conhecidos.
- Chamar de "omissão" a discordância com a valoração da prova.
- Opor dois embargos contra a mesma decisão (preclusão consumativa).
- Embargos manifestamente incabíveis antes do REsp: não interrompem, e o REsp morre intempestivo.
- Esquecer de alegar violação ao art. 619 no REsp quando o tribunal manteve a omissão (Súmula 211 STJ).

## Integração com o núcleo
`prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`. Recursos seguintes: `penal-apelacao-criminal`, `penal-embargos-infringentes-e-de-nulidade`, `penal-recurso-especial-criminal`, `penal-recurso-extraordinario-criminal`.

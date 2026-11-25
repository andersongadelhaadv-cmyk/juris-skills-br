---
name: trib-recurso-especial-tributario
description: >
  Complementa a skill civel-recurso-especial com o recorte tributário do recurso
  especial ao STJ (CF art. 105, III): separar a questão de lei federal (CTN e
  leis tributárias federais) da questão constitucional (RE) e da lei local
  (Súmula 280 do STF), evitar o reexame de prova típico de decadência,
  prescrição e erro de fato (Súmula 7 do STJ) e usar a relevância presumida pelo
  valor da causa. Use quando o usuário pedir recurso especial em matéria
  tributária, REsp contra acórdão de TRF ou TJ em execução fiscal, mandado de
  segurança, anulatória ou repetição de indébito.
metadata:
  area: tributario-fazenda
  tipo_peca: recurso
  verificado_em: 2026-11-25
---
# Recurso especial tributário (recorte)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar **junto com** `civel-recurso-especial`, que traz o procedimento completo (prazo, preparo, relevância do art. 1.035-A do CPC, prequestionamento, dissídio, agravos). Esta skill só acrescenta o que é próprio da matéria tributária.
- Não usar sozinha. Matéria só constitucional (imunidade, princípios, competência tributária): `civel-recurso-extraordinario`. Acórdão de turma recursal: não cabe REsp (ver vizinha). Sentença em execução fiscal de alçada (Lei 6.830/1980, art. 34): o recurso é de embargos infringentes ao próprio juízo, sem acórdão de tribunal — não há "causa decidida" por TRF ou TJ (CF art. 105, III).

## Entradas mínimas (perguntar o que faltar; nunca supor fatos)
1. Acórdão recorrido e dos embargos de declaração, com datas de publicação.
2. Ente e tributo: federal, estadual ou municipal; qual lei rege a obrigação (CTN, lei federal, lei local).
3. Dispositivos de lei federal debatidos (CTN, LEF, Lei 9.430/1996, Lei 10.522/2002 etc.) e onde foram prequestionados.
4. Se o acórdão também tem fundamento constitucional (exige RE simultâneo) ou de lei local.
5. Valor da causa ou da execução atualizado (relevância presumida acima de 500 salários mínimos).
6. Se há tema repetitivo do STJ ou repercussão geral do STF sobre a questão (afetado, julgado, com modulação).

## Prazo e contagem
- Prazo, interrupção pelos ED, feriado local e transição da relevância: seguir `civel-recurso-especial` e `prazos-processuais`.
- Fazenda Pública recorrida ou recorrente: confirme o prazo em dobro e a intimação pessoal da procuradoria em `prazos-processuais`.

## Estrutura da peça
Usar a estrutura de `civel-recurso-especial`, inserindo, nas razões: delimitação da questão federal tributária → afastamento da lei local e da matéria constitucional → premissas fáticas fixadas no acórdão (para não esbarrar na Súmula 7) → violação por dispositivo → tema repetitivo aplicável ou distinção. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares (recorte tributário)
- **Lei federal x lei local.** ICMS, ISS, IPTU, ITBI, IPVA, ITCMD costumam ter o núcleo da discussão em lei estadual ou municipal: o REsp não serve para rever interpretação de direito local (Súmula 280 do STF, aplicada por analogia). Ancore a tese no CTN, em lei complementar nacional ou em lei federal.
- **Questão constitucional.** Imunidade, anterioridade, competência tributária, vedação de confisco: é matéria do RE. Se o acórdão tem fundamento constitucional suficiente e autônomo, interponha RE simultâneo (ver `civel-recurso-especial` sobre a Súmula 126 do STJ).
- **Súmula 7 do STJ.** Decadência e prescrição dependentes de datas controvertidas, erro de fato, prova do repasse do encargo, existência de crédito em compensação: só sobem se o acórdão fixou as premissas fáticas. Transcreva-as e discuta só a qualificação jurídica.
- **Prequestionamento (Súmula 211 do STJ).** Comum em tributário: o tribunal decide por fundamento constitucional e silencia sobre o CTN. Opor ED e alegar violação ao art. 1.022 do CPC (procedimento em `civel-recurso-especial`).
- **Relevância.** Valor da causa acima de 500 salários mínimos presume a relevância (CF art. 105, § 3º, III); contrariedade à jurisprudência dominante do STJ também (§ 3º, V). Mesmo assim, faça o tópico.
- **Repetitivos.** Questões tributárias são frequentemente afetadas: verifique tema, tese e modulação em `verificacao-de-citacoes`; se o tema está afetado, peça a observância do sobrestamento ou demonstre a distinção.

## Fundamentos verificados
- CF art. 105, III, e §§ 2º e 3º.
- Lei 6.830/1980, art. 34 (execução fiscal de alçada).
- Súmula 280 do STF; Súmulas 7 e 211 do STJ.
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Os de `civel-recurso-especial` (admissão, relevância, provimento, efeito suspensivo se necessário).
- Tributário: pedir que o STJ aplique o direito federal às premissas fáticas do acórdão (sem reexame); em discussão de encargos, tese conforme `juros-e-correcao`.
- Se o crédito tributário estiver exigível, avaliar tutela para suspender a exigibilidade enquanto pende o recurso (CTN art. 151, V; via `civel-recurso-especial`, efeito suspensivo).

## Checklist pré-protocolo (além do checklist de `civel-recurso-especial`)
- [ ] Tese ancorada em lei federal (CTN/LC/lei federal), não em lei local
- [ ] Fundamento constitucional autônomo identificado → RE simultâneo
- [ ] Premissas fáticas transcritas do acórdão; nenhum pedido de reexame de prova
- [ ] ED opostos para prequestionar dispositivos do CTN
- [ ] Valor da causa atualizado para a presunção de relevância
- [ ] Tema repetitivo e repercussão geral pesquisados (tese, modulação, sobrestamento)

## Erros a evitar
- Discutir alíquota, base de cálculo ou benefício previsto em lei estadual/municipal como se fosse lei federal.
- Alegar ofensa a princípio constitucional tributário no REsp.
- Pedir ao STJ que reconte prazo decadencial com datas que o acórdão não fixou.
- Recorrer ao STJ de sentença de execução fiscal de alçada.
- Ignorar tema repetitivo julgado contra a tese (o recurso será negado na origem).

## Integração com o núcleo
`prazos-processuais`, `verificacao-de-citacoes`, `juros-e-correcao`, `fidelidade-factual`, `estilo-forense`. Vizinhas: `civel-recurso-especial` (base obrigatória), `civel-recurso-extraordinario`, `civel-agravo-interno`, `trib-embargos-a-execucao-fiscal`, `trib-mandado-de-seguranca`.

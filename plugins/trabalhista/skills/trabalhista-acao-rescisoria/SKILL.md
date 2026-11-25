---
name: trabalhista-acao-rescisoria
description: >
  Redige ação rescisória na Justiça do Trabalho (CLT art. 836, com o regime dos
  arts. 966 a 975 do CPC), com depósito prévio de 20%, prazo decadencial de dois
  anos (Súmula 100/TST), prova do trânsito em julgado (Súmula 299/TST) e
  competência TRT x TST (Súmula 192/TST). Use quando o usuário pedir rescisória
  trabalhista, desconstituir sentença ou acórdão trabalhista transitado em
  julgado, anular termo de conciliação homologado, rescindir por violação
  manifesta de norma, prova nova, erro de fato ou colusão, ou contestar
  rescisória.
metadata:
  area: trabalhista
  tipo_peca: inicial
  verificado_em: 2026-11-25
---
# Ação rescisória trabalhista

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: decisão de mérito trabalhista transitada em julgado (sentença, acórdão, termo de conciliação homologado), ou decisão não de mérito que impeça nova demanda ou a admissibilidade do recurso (CPC art. 966, §2º).
- Também: contestação do réu na rescisória (inverter o roteiro: decadência, falta de prova do trânsito, matéria controvertida, reexame de provas).
- Não usar: decisão ainda recorrível (`trabalhista-recurso-ordinario`, `trabalhista-recurso-de-revista`); ato homologatório praticado no curso da execução, que se anula pela via própria (CPC art. 966, §4º; ver `trabalhista-embargos-a-execucao`); rescisória cível comum (não há skill específica no `processo-civil`; adapte com cautela); revisão criminal (`penal-revisao-criminal`).

## Entradas mínimas (perguntar o que faltar; nunca supor fatos)
1. Decisão rescindenda e todas as decisões posteriores no processo (para identificar a última e o órgão que julgou o mérito).
2. Certidão de trânsito em julgado e a data dele.
3. Hipótese do art. 966 do CPC pretendida e a prova correspondente (norma violada, documento novo e quando foi descoberto, erro de fato nos autos, prova da colusão).
4. Valor da causa e condição financeira do autor (depósito de 20% ou prova de miserabilidade).
5. Estado da execução (há risco de levantamento de valores? cabe tutela provisória?).

## Prazo e contagem
- Decadência de 2 anos contados do trânsito em julgado da última decisão proferida no processo (CPC art. 975), lida com a Súmula 100/TST (recurso intempestivo ou incabível não adia o início, salvo dúvida razoável; acordo homologado transita na data da homologação; prorrogação para o primeiro dia útil).
- Prova nova: termo inicial na descoberta, limite de 5 anos do trânsito (CPC art. 975, §2º). Colusão: para o MP que não interveio, da ciência (art. 975, §3º; Súmula 100, VI).
- Contagem e prazos internos (contestação, recurso ordinário de 8 dias — CLT art. 895, II): `prazos-processuais`.

## Estrutura da peça
Competência → cabimento (decisão de mérito transitada) → tempestividade → depósito prévio → hipótese rescisória (juízo rescindente) → novo julgamento (juízo rescisório, CPC art. 968, I) → tutela provisória → pedidos. Roteiro em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Depósito prévio de 20% do valor da causa**, salvo prova de miserabilidade jurídica (CLT art. 836) — não confundir com os 5% do CPC (art. 968, II), que não é a regra trabalhista.
- **Prova do trânsito em julgado** com a inicial; faltando, o relator abre 15 dias; trânsito posterior ao ajuizamento não salva a ação (Súmula 299/TST).
- **Competência:** TRT, se o TST não conheceu do recurso; TST quando seu acórdão examinou o mérito, inclusive o que não conhece da revista ou dos embargos analisando violação de lei material ou aplicando súmula de direito material (Súmula 192/TST). Rescisória de sentença normativa: SDC do TST nas suas próprias sentenças (Lei 7.701/1988, art. 2º); de acórdão de Turma do TST: SDI (art. 3º).
- **Termo de conciliação** (CLT art. 831, parágrafo único): só por rescisória (Súmula 259/TST).

## Fundamentos verificados
- CLT art. 836 (rescisória na forma do CPC, depósito de 20%); CPC art. 1.046, §4º (remissão ao CPC revogado passa ao atual); CLT art. 769.
- CPC arts. 966 (hipóteses e §§1º a 4º), 968, I, 969 (rescisória não suspende o cumprimento, salvo tutela provisória), 975.
- Súmulas do TST: 83 (violação de lei de interpretação controvertida não procede), 100, 192, 259, 299, 410 (sem reexame de fatos e provas na rescisória por violação de lei).
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Rescisão da decisão (ou do capítulo — CPC art. 966, §3º), indicando-o com precisão.
- Novo julgamento da causa, quando cabível (art. 968, I).
- Tutela provisória para suspender a execução (art. 969), com perigo concreto (levantamento iminente).
- Comprovante do depósito de 20% ou pedido de dispensa fundamentado.
- Citação do réu; valor da causa; juros e correção de eventual devolução: `juros-e-correcao`.

## Checklist pré-protocolo
- [ ] Última decisão do processo identificada e prazo de 2 anos calculado
- [ ] Certidão de trânsito juntada
- [ ] Competência TRT x TST definida pela Súmula 192
- [ ] Depósito de 20% recolhido ou miserabilidade provada
- [ ] Inciso do art. 966 indicado e provado
- [ ] Se violação de norma: tese não era controvertida (Súmula 83) e não depende de reexame de prova (Súmula 410)
- [ ] Pedido rescisório e rescindente separados

## Erros a evitar
- Usar a rescisória como recurso para rediscutir prova (Súmula 410).
- Recolher 5% (regra cível) em vez de 20%.
- Contar o prazo de uma decisão intermediária, ou de recurso intempestivo, sem dúvida razoável (Súmula 100, III).
- Pedir a rescisão da sentença quando ela foi substituída pelo acórdão no que foi objeto de recurso (CPC art. 1.008; Súmula 192, III, editada ainda sob o CPC/1973).
- Ajuizar antes do trânsito em julgado (Súmula 299, III).

## Integração com o núcleo
`prazos-processuais`, `juros-e-correcao`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

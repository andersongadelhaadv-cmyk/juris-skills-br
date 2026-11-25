---
name: trib-recurso-especial-csrf
description: >
  Redige recurso especial de divergência do contribuinte à Câmara Superior de
  Recursos Fiscais (CSRF) contra acórdão de turma do CARF, com cotejo analítico
  de até dois paradigmas por matéria, prequestionamento e preliminar de
  tempestividade (Decreto 70.235/1972 art. 37, §2º; Regimento Interno do CARF,
  Portaria MF 1.634/2023, arts. 118 a 122), além de contrarrazões ao recurso
  especial da Fazenda e agravo contra o despacho que nega seguimento. Use quando
  o usuário pedir recurso especial ao CARF, recurso à CSRF, Câmara Superior,
  divergência entre turmas do CARF, paradigma, contrarrazões a recurso especial
  da PGFN ou agravo de admissibilidade no CARF.
metadata:
  area: tributario-fazenda
  tipo_peca: recurso
  verificado_em: 2026-11-25
---
# Recurso especial à Câmara Superior de Recursos Fiscais

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: acórdão de turma ordinária do CARF (recurso voluntário ou de ofício) desfavorável ao contribuinte, quando outra turma deu à mesma legislação tributária interpretação diferente; contrarrazões ao recurso especial da Procuradoria da Fazenda Nacional; agravo contra despacho que negou seguimento total ou parcial.
- Não usar: impugnação na DRJ ou recurso voluntário ao CARF (`trib-defesa-administrativa-e-carf`); memorial e sustentação oral do julgamento (`trib-memorial-e-sustentacao-oral-carf`); contencioso estadual (`trib-recurso-administrativo-estadual`); discussão já levada ao Judiciário ou a levar (`trib-acao-anulatoria`, `trib-mandado-de-seguranca`).
- O recurso especial não é terceira instância de revisão de provas: só cabe por divergência de interpretação (Decreto 70.235 art. 37, §2º, II; RICARF art. 118).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
- Inteiro teor do acórdão recorrido, data da ciência e forma (DTE, postal, pessoal).
- Se houve embargos de declaração, a data da ciência do despacho ou do acórdão de embargos.
- Matérias vencidas, separadas uma a uma, e o trecho do acórdão em que cada uma foi decidida (prequestionamento).
- Acórdãos paradigmas candidatos: número, turma, data, ementa e inteiro teor ou indicação no sítio do CARF.
- Se algum paradigma foi reformado, se a matéria é objeto de súmula do CARF ou de precedente vinculante, e se há ação judicial com o mesmo objeto.

## Prazo e contagem
- Recurso especial: 15 dias da ciência do acórdão (Decreto 70.235 art. 37, §2º; RICARF art. 119). O Decreto conta em dias corridos, salvo disposição em contrário, excluindo o dia do início (art. 5º, I e II).
- Contrarrazões e recurso especial da parte vencida, quando a Fazenda recorre: 15 dias da ciência do despacho de admissão (RICARF arts. 120 e 121).
- Agravo: 5 dias da ciência do despacho de admissibilidade (RICARF art. 122, §1º).
- Só embargos de declaração tempestivos interrompem o prazo do recurso especial (RICARF art. 116, §6º).
- Contencioso de CBS: o art. 37, §5º, do Decreto traz regra própria de prazo [VERIFICAR: texto do §5º não lido na íntegra na fonte oficial].
- Normas gerais do CTN (arts. 208-A a 208-J, LC 236/2026) preveem 20 dias úteis para o recurso especial, mas o art. 211-B dá 2 anos para a adaptação da legislação; até lá, protocole pelo prazo do Decreto. Confira a contagem em `prazos-processuais`.

## Estrutura da peça
Endereçamento ao Presidente da Câmara da turma recorrida → qualificação → tempestividade (preliminar fundamentada) → cabimento → síntese do processo → uma seção por matéria: prequestionamento, legislação interpretada, paradigmas e cotejo analítico → mérito da interpretação correta → pedidos. Roteiro em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Petição dirigida ao Presidente da Câmara à qual está vinculada a turma que julgou (RICARF art. 119).
- Demonstrar a legislação tributária interpretada de forma divergente (art. 118, §1º).
- Até dois paradigmas por matéria; se indicar mais, só os dois primeiros contam (art. 118, §§6º e 7º).
- Cotejo analítico: apontar o ponto do paradigma que diverge do ponto específico do recorrido (art. 118, §8º). Semelhança de tema não basta; os fatos relevantes precisam ser comparáveis.
- Instruir com inteiro teor do paradigma, cópia da publicação no DOU, ementa integral transcrita no corpo ou indicação da publicação no sítio do CARF (art. 118, §§9º a 11).
- Prequestionamento com indicação precisa do trecho do acórdão recorrido, do despacho que rejeitou embargos ou do acórdão de embargos (art. 118, §5º).
- Não serve como paradigma: acórdão de turma extraordinária; acórdão reformado na matéria; acórdão que contrarie súmula vinculante, repetitivo ou repercussão geral transitados, súmula do CARF ou resolução do Pleno da CSRF (art. 118, §12). Não use acórdão da própria turma ou câmara que proferiu o recorrido (art. 122, §2º, III).
- Não cabe recurso especial de acórdão que adota súmula do CARF (art. 118, §3º), nem do que anula a decisão de primeira instância por vício próprio (art. 118, §4º).
- Documentos e alegações apresentados depois do prazo não contam para a admissibilidade (art. 118, §13). Tudo vai na petição.

## Fundamentos verificados
Decreto 70.235/1972 arts. 5º, 25 (§§9º, 9º-A e 12), 26-A e 37, §2º; Regimento Interno do CARF (Portaria MF 1.634/2023) arts. 115, 116, §6º, 118 a 122; CTN arts. 151, III, 208-C, 208-D e 211-B (LC 236/2026). Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Admissão do recurso, total ou por matéria, e encaminhamento à Turma da CSRF.
- Provimento para adotar a interpretação do paradigma e cancelar, total ou parcialmente, a exigência; subsidiariamente, exclusão ou redução da multa.
- Manutenção da suspensão da exigibilidade (CTN art. 151, III).
- Intimação do procurador e pedido de sustentação oral no julgamento (Decreto art. 25, §12).

## Checklist pré-protocolo
- [ ] Data da ciência conferida; prazo de 15 dias corridos contado; embargos tempestivos considerados.
- [ ] Preliminar de tempestividade escrita com documentos, se houver qualquer dúvida (é a única via para salvar agravo por intempestividade: art. 122, §2º, I).
- [ ] Cada matéria com prequestionamento localizado (página/trecho).
- [ ] No máximo dois paradigmas por matéria, nenhum da mesma turma, nenhum reformado, nenhum de turma extraordinária.
- [ ] Inteiro teor ou ementa integral ou link do sítio do CARF para cada paradigma.
- [ ] Súmulas do CARF e precedentes vinculantes sobre a matéria conferidos no portal oficial.
- [ ] Declaração sobre ação judicial com o mesmo objeto.

## Erros a evitar
- Rediscutir prova: a CSRF julga divergência de interpretação, não o acerto da valoração dos fatos.
- Cotejo genérico ("o paradigma decidiu de forma diversa") sem confronto de trechos.
- Contar o prazo em dias úteis com base no CTN art. 208-D antes de vencido o prazo de adaptação do art. 211-B.
- Paradigma com moldura fática diferente, ou já superado por súmula do CARF.
- Juntar paradigma ou documento depois do protocolo esperando que seja considerado (art. 118, §13).
- Deixar de recorrer da parte vencida quando a Fazenda recorre: o prazo é o das contrarrazões (art. 120).

## Integração com o núcleo
- `prazos-processuais`: contagem em dias corridos do Decreto 70.235 e suspensão de fim de ano.
- `verificacao-de-citacoes`: paradigmas e súmulas do CARF; súmula do CARF só entra conferida no portal oficial.
- `juros-e-correcao`: atualização do crédito em discussão.
- `fidelidade-factual`: confronto entre o acórdão recorrido e os paradigmas.
- `estilo-forense`: revisão final.

---
name: civel-acao-rescisoria
description: >
  Redige petição inicial de ação rescisória cível (CPC, arts. 966 a 975) contra
  decisão de mérito transitada em julgado — ou terminativa que impeça nova
  demanda ou o recurso —, com enquadramento em um dos incisos do art. 966,
  pedido de rescisão e de novo julgamento, depósito de 5% (art. 968, II),
  prazo decadencial de 2 anos (art. 975) e as Súmulas 343/STF, 514/STF e
  401/STJ. Use quando o usuário pedir para desfazer sentença ou acórdão
  transitado em julgado, rescindir decisão por violação manifesta de norma,
  prova nova, erro de fato, juiz impedido, dolo, colusão ou ofensa à coisa
  julgada, ou perguntar se ainda dá tempo de rescindir.
metadata:
  area: processo-civil
  tipo_peca: inicial
  verificado_em: 2026-11-25
---
# Ação rescisória cível

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar contra **decisão de mérito transitada em julgado** (sentença, acórdão, decisão monocrática ou interlocutória de mérito), inclusive um só capítulo (CPC, art. 966, § 3º), ou contra decisão **não de mérito** que impeça nova propositura da demanda ou a admissibilidade do recurso (art. 966, § 2º).
- Cabe ainda que não esgotados os recursos contra a decisão (Súmula 514/STF).
- Não usar:
  - Ainda cabe recurso → `civel-apelacao`, `civel-recurso-especial`, `civel-embargos-de-declaracao` etc.
  - Ato de disposição de direitos homologado (acordo) ou ato homologatório na execução: a via é a anulação, nos termos da lei (art. 966, § 4º) → `civel-peticao-inicial`.
  - Causa do juizado especial: não se admite rescisória (Lei 9.099/1995, art. 59) → `civel-juizado-especial`.
  - Sentença penal → `penal-revisao-criminal`. Rescisória trabalhista → outro regime (`trabalhista-*`).
  - Inexigibilidade do título por decisão do STF anterior ao trânsito: alegar na impugnação (`civel-impugnacao-ao-cumprimento`); se a decisão do STF for posterior ao trânsito, cabe rescisória com prazo contado do trânsito da decisão do STF (arts. 525, § 15, e 535, § 8º).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Cópia integral do processo originário, com a decisão rescindenda e a **certidão de trânsito em julgado**.
2. Data do trânsito da **última decisão** proferida no processo (art. 975; Súmula 401/STJ).
3. O vício, com o documento que o prova: norma violada e onde a decisão a contrariou; prova nova (quando foi descoberta e por que não pôde ser usada); erro de fato verificável nos autos; impedimento do juiz; dolo, coação, simulação, colusão; prova falsa; coisa julgada anterior.
4. O que se quer no novo julgamento (iudicium rescissorium).
5. Gratuidade ou condição de ente público (dispensa do depósito, art. 968, § 1º).
6. A decisão está sendo cumprida? Há urgência para suspender (art. 969)?

## Prazo e contagem
- **2 anos** contados do trânsito em julgado da última decisão proferida no processo (art. 975); o prazo só se inicia quando não for cabível qualquer recurso do último pronunciamento (Súmula 401/STJ).
- Vencimento em férias, recesso, feriado ou dia sem expediente: prorroga para o primeiro dia útil seguinte (art. 975, § 1º).
- **Prova nova** (inciso VII): conta da descoberta, limitado a 5 anos do trânsito (art. 975, § 2º).
- **Simulação ou colusão**: para terceiro prejudicado e MP que não interveio, conta da ciência (art. 975, § 3º).
- O art. 975 fala em extinção do "direito à rescisão": prazo decadencial, ao qual, salvo lei em contrário, não se aplicam as causas que impedem, suspendem ou interrompem a prescrição (CC, art. 207). Conferência de datas: `prazos-processuais`.

## Estrutura da peça
Endereçamento ao tribunal competente → qualificação → cabimento (decisão, trânsito, tempestividade) → hipótese(s) do art. 966 → iudicium rescindens → iudicium rescissorium → tutela provisória → depósito → pedidos → provas → valor da causa. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Competência originária do tribunal**: STF e STJ julgam as rescisórias de seus julgados (CF, arts. 102, I, "j", e 105, I, "e"); o TRF, as de seus julgados e dos juízes federais da região (art. 108, I, "b"); TJ conforme a Constituição estadual e o regimento interno [VERIFICAR: não conferidos nesta skill; consultar o do tribunal do caso]. Indicar o órgão pelo regimento. Se o tribunal for incompetente, há emenda para adequar o objeto (art. 968, §§ 5º e 6º).
- **Requisitos da inicial**: art. 319 + cumulação do pedido de novo julgamento, se for o caso (art. 968, I) + **depósito de 5% do valor da causa** (art. 968, II), limitado a 1.000 salários-mínimos (§ 2º); sem depósito, indeferimento (§ 3º). Dispensados: entes públicos, MP, Defensoria e beneficiários da gratuidade (§ 1º).
- **Legitimidade**: parte ou sucessor, terceiro juridicamente interessado, MP nas hipóteses do art. 967, III, e quem não foi ouvido quando sua intervenção era obrigatória (art. 967).
- **Polo passivo**: todos os que foram partes no processo originário e se beneficiam da decisão.
- **Violação manifesta de norma (inciso V)**: não cabe quando a decisão se baseou em texto de interpretação controvertida nos tribunais (Súmula 343/STF). Contra decisão baseada em súmula ou repetitivo que ignorou distinção, cabe pelo inciso V, com o ônus do art. 966, §§ 5º e 6º.
- **Erro de fato (inciso VIII)**: o fato não pode ter sido ponto controvertido sobre o qual o juiz deveria ter se pronunciado (art. 966, § 1º).

## Fundamentos verificados
CPC arts. 966 a 975, 525 § 15, 535 § 8º; CF arts. 102, I, "j", 105, I, "e", 108, I, "b"; Lei 9.099/1995, art. 59; CC art. 207; Súmulas 343/STF, 514/STF e 401/STJ. Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Tutela provisória para suspender o cumprimento da decisão rescindenda (art. 969), com probabilidade e perigo concretos.
- Rescisão da decisão (ou do capítulo) e, se for o caso, novo julgamento com o resultado pretendido (art. 968, I; art. 974).
- Restituição do depósito na procedência (art. 974).
- Citação do réu (prazo de resposta fixado pelo relator entre 15 e 30 dias, art. 970); custas e honorários.
- Comprovante do depósito ou pedido de dispensa fundamentado.

## Checklist pré-protocolo
- [ ] Certidão de trânsito e data da última decisão do processo
- [ ] Prazo de 2 anos (ou regra especial dos §§ 2º e 3º do art. 975) calculado e anotado
- [ ] Inciso do art. 966 indicado e provado; Súmula 343 enfrentada no inciso V
- [ ] Tribunal e órgão competentes conferidos no regimento interno
- [ ] Depósito de 5% recolhido (respeitado o teto) ou dispensa demonstrada
- [ ] Pedido rescindente e rescisório formulados separadamente
- [ ] Todos os beneficiários da decisão no polo passivo

## Erros a evitar
- Usar a rescisória como recurso para rediscutir prova ou justiça da decisão: só as hipóteses do art. 966.
- Contar o prazo do trânsito da decisão que se quer rescindir, e não da última decisão do processo.
- Esquecer o depósito: indeferimento (art. 968, § 3º).
- Alegar "violação de lei" em matéria que era controvertida à época (Súmula 343/STF).
- Pedir só a rescisão quando o caso exige novo julgamento (ou o contrário).

## Integração com o núcleo
`prazos-processuais` (decadência), `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`, `juros-e-correcao` (se o novo julgamento envolver condenação).

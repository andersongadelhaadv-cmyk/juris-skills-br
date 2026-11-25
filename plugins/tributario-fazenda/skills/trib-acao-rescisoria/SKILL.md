---
name: trib-acao-rescisoria
description: >
  Redige ação rescisória em matéria tributária (CPC arts. 966 a 975), pelo
  contribuinte ou pela Fazenda, com foco na violação manifesta de norma
  jurídica (art. 966, V), no prazo decadencial de 2 anos (art. 975), nos
  limites da Súmula 343 e do Tema 136 do STF e na relação com o Tema 885 STF
  (coisa julgada em trato continuado). Use quando o usuário pedir rescisória
  tributária, rescindir acórdão ou sentença sobre tributo transitada em
  julgado, desconstituir coisa julgada tributária, rescisória após decisão do
  STF em repercussão geral, ou defesa contra rescisória da Fazenda.
metadata:
  area: tributario-fazenda
  tipo_peca: inicial
  verificado_em: 2026-11-25
---
# Ação rescisória tributária

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: decisão de mérito transitada em julgado sobre relação tributária (ou decisão terminativa que impeça nova demanda ou a admissibilidade de recurso — CPC art. 966, §2º) que se enquadre num dos incisos do art. 966; mais comum, violação manifesta de norma jurídica (V), prova nova (VII) e erro de fato verificável nos autos (VIII).
- Cabe mesmo sem esgotar os recursos contra a decisão (Súmula 514 STF).
- Também orienta a **defesa** do réu na rescisória (contestação centrada em decadência, Súmula 343 e Tema 136).
- Não usar: decisão ainda recorrível (`civel-apelacao`, `civel-recurso-especial`, `civel-recurso-extraordinario`); relação de trato continuado em que decisão posterior do STF em ação direta ou repercussão geral já faz cessar, por si, os efeitos futuros da coisa julgada (Tema 885 STF): para o período futuro a Fazenda não precisa de rescisória; matéria penal (`penal-revisao-criminal`).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Decisão rescindenda (inteiro teor) e certidão de trânsito em julgado da **última** decisão do processo.
2. Inciso do art. 966 invocado e a norma violada, com a leitura que a decisão fez dela.
3. Estado da jurisprudência **na data do acórdão rescindendo**: havia divergência nos tribunais? Havia entendimento do Plenário do STF?
4. Decisão do STF superveniente (ação direta ou repercussão geral), número do tema e data do trânsito.
5. Valor econômico em jogo e se a decisão rescindenda está em cumprimento (precatório, compensação, execução fiscal).
6. Gratuidade ou natureza do autor (Fazenda é dispensada do depósito).

## Prazo e contagem
- O direito à rescisão se extingue em **2 anos** do trânsito em julgado da última decisão proferida no processo (CPC art. 975); prorroga-se ao primeiro dia útil se vencer em férias, recesso, feriado ou dia sem expediente (§1º).
- Prova nova (art. 966, VII): conta da descoberta, limitado a 5 anos do trânsito (art. 975, §2º).
- Decisão do STF posterior ao trânsito, com base na qual se diga inexigível o título (CPC arts. 525, §15, e 535, §8º): a lei prevê rescisória; termo inicial e limites aplicados pelo STF a esses dispositivos não conferidos [VERIFICAR antes de calcular].
- Prazo é decadencial: não se suspende nem dobra para a Fazenda. Confira com `prazos-processuais`.

## Estrutura da peça
Endereçamento ao tribunal competente → partes → tempestividade → depósito de 5% → cabimento (decisão de mérito transitada + inciso) → juízo rescindente → juízo rescisório (novo julgamento) → tutela para suspender o cumprimento → pedidos. Roteiro em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Competência: o próprio tribunal que proferiu a decisão de mérito rescindenda — STF (CF art. 102, I, j), STJ (art. 105, I, e), TRF quanto a julgados seus ou dos juízes federais da região (art. 108, I, b), TJ conforme a constituição estadual.
- Inicial com os requisitos do art. 319 e, se for o caso, cumulação do pedido de novo julgamento (CPC art. 968, I).
- Depósito de 5% do valor da causa, convertido em multa se a ação for declarada inadmissível ou improcedente por unanimidade (art. 968, II); dispensados União, Estados, DF, Municípios, autarquias e fundações públicas, MP, Defensoria e beneficiários da gratuidade (§1º).
- A rescisória não impede o cumprimento da decisão, salvo tutela provisória (art. 969).
- **Súmula 343 STF**: não cabe rescisória por ofensa a literal disposição de lei quando a decisão se baseou em texto de interpretação controvertida nos tribunais.
- **Tema 136 STF**: não cabe rescisória quando o julgado estava em harmonia com o entendimento do Plenário do STF à época, ainda que o precedente seja depois superado.
- Rescisória não é recurso de prazo longo: o autor precisa mostrar violação **manifesta**, não apenas interpretação diversa da sua.

## Fundamentos verificados
CPC arts. 319, 525, §15, 535, §8º, 966, 968, 969 e 975; CF arts. 102, I, j, 105, I, e, 108, I, b; Súmulas 343 e 514 STF; Tema 136 STF (RE 590.809); Tema 885 STF (RE 955.227). Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Tutela provisória para suspender o cumprimento da decisão rescindenda (art. 969), com demonstração de probabilidade e perigo concreto.
- Juízo rescindente: desconstituição da decisão transitada em julgado.
- Juízo rescisório: novo julgamento da causa (art. 968, I), com o resultado tributário pretendido.
- Citação do réu (prazo de 15 a 30 dias fixado pelo relator — art. 970).
- Comprovação do depósito de 5% ou indicação da dispensa legal.
- Devolução do depósito ao final se procedente; honorários.

## Checklist pré-protocolo
- [ ] Certidão de trânsito da última decisão e contagem dos 2 anos conferida
- [ ] Inciso do art. 966 escolhido e demonstrado
- [ ] Pesquisa do estado da jurisprudência na data do acórdão (Súmula 343 e Tema 136 enfrentados)
- [ ] Tribunal competente identificado
- [ ] Depósito de 5% recolhido ou dispensa comprovada
- [ ] Verificado se o Tema 885 já resolve o período futuro sem rescisória
- [ ] Pedido de novo julgamento cumulado

## Erros a evitar
- Contar o prazo do trânsito de uma decisão intermediária, e não da última do processo.
- Ignorar a divergência jurisprudencial da época: a Súmula 343 derruba a ação.
- Ajuizar rescisória da Fazenda para alcançar períodos futuros já atingidos pelo Tema 885.
- Esquecer o depósito de 5% (particular) ou o pedido de novo julgamento.
- Tratar o prazo como processual e aplicar dobra da Fazenda.

## Integração com o núcleo
`prazos-processuais`, `juros-e-correcao`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

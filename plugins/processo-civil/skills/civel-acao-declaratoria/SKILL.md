---
name: civel-acao-declaratoria
description: >
  Redige petição inicial de ação declaratória cível (CPC, arts. 19 e 20) para
  obter certeza sobre a existência, a inexistência ou o modo de ser de uma
  relação jurídica, ou sobre a autenticidade ou falsidade de documento, com
  enfrentamento do interesse de agir, valor da causa (art. 292, II) e alerta
  sobre prescrição do pedido condenatório cumulado. Use quando o usuário pedir
  ação declaratória de inexistência de relação jurídica ou de débito fora do
  consumo, declaração de interpretação de cláusula contratual (Súmula 181/STJ),
  declaração de falsidade de documento ou "quero que o juiz diga que não devo".
metadata:
  area: processo-civil
  tipo_peca: inicial
  verificado_em: 2026-11-25
---
# Ação declaratória cível

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar quando o bem da vida é **a certeza jurídica**: (a) existência ou inexistência de relação jurídica (contrato, sociedade, débito, servidão, vínculo obrigacional); (b) modo de ser da relação (alcance de cláusula, índice aplicável, titularidade); (c) autenticidade ou falsidade de documento (CPC, art. 19, I e II).
- Cabe mesmo depois de violado o direito (art. 20): o autor pode preferir só a declaração, por estratégia ou porque a condenação está prescrita [ver Prazo].
- Não usar:
  - Negativação, cobrança ou contrato de consumo → `consumidor-negativacao-indevida` ou `consumidor-repeticao-em-dobro`.
  - Relação tributária → `trib-declaratoria-inexistencia-relacao-tributaria`.
  - Ato administrativo → `adm-acao-anulatoria-de-ato-administrativo`.
  - União estável, paternidade e demais estados de família → `familia-uniao-estavel`, `familia-investigacao-de-paternidade`.
  - Desfazer o negócio (anular, resolver, rescindir): o pedido é constitutivo; use `civel-peticao-inicial` ou `contratos-distrato-e-rescisao`. Se só quer certeza sobre a nulidade absoluta, esta skill serve.
  - Fato puro (sem relação jurídica): não cabe declaratória; só o documento admite declaração sobre fato (falsidade/autenticidade).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Qual relação jurídica (ou documento) e qual a declaração exata pretendida (existe / não existe / tem tal alcance / é falso).
2. A **incerteza objetiva**: quem afirma o contrário, como e quando (notificação, cobrança, protesto, uso do documento em outro processo).
3. Documentos da relação: contrato, aditivos, recibos, troca de mensagens, o documento impugnado (original, se possível).
4. Se já houve violação: há pedido condenatório a cumular (restituição, indenização, abstenção)? Datas para a prescrição.
5. Valor do ato ou da parte controvertida (art. 292, II).
6. Urgência concreta (cobrança iminente, protesto, execução anunciada).

## Prazo e contagem
- Não há prazo processual para propor; há prazo material **do pedido cumulado**. A tese de que a declaratória pura não se sujeita a prescrição não foi conferida em precedente nesta skill [VERIFICAR: buscar no JuriBase precedente atual do STJ antes de afirmá-la].
- Se o caso é de nulidade relativa (anulabilidade), o prazo é decadencial e o pedido não é declaratório: conferir o dispositivo do CC aplicável.
- Pedido condenatório cumulado: prazo próprio (ex.: reparação civil, CC art. 206, § 3º, V; responsabilidade contratual, art. 205). Prazos processuais: `prazos-processuais`.

## Estrutura da peça
Endereçamento → qualificação → síntese → fatos e incerteza → interesse de agir (art. 19/20) → mérito (por que a relação existe/não existe ou o documento é falso) → tutela provisória → pedidos → provas → valor da causa → audiência (art. 334). Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Interesse de agir**: demonstrar a incerteza objetiva e atual (alguém afirma o contrário). Sem dúvida concreta, risco de extinção por falta de interesse (art. 330, III).
- **Polo passivo**: quem afirma a relação ou quem se beneficia do documento; todos os sujeitos da relação a declarar (litisconsórcio necessário se a declaração os atinge).
- **Falsidade documental**: se o documento já foi juntado em processo em curso, a via é a arguição naquele processo (CPC, art. 430: contestação, réplica ou 15 dias da intimação da juntada), podendo a parte pedir que seja decidida como questão principal (art. 430, parágrafo único, e art. 433). A ação autônoma é para documento ainda não usado em juízo.
- **Reconvenção**: o réu pode reconvir (Súmula 258/STF); antecipe a resposta à condenação que ele pode pedir.

## Fundamentos verificados
- CPC arts. 19 e 20 (objeto e cabimento mesmo após a violação); art. 292, II (valor); art. 503, § 1º (questão prejudicial); art. 515, I (decisão que reconhece exigibilidade de obrigação é título executivo).
- Súmula 181/STJ (declaratória sobre exata interpretação de cláusula contratual); Súmula 258/STF (reconvenção em declaratória).
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Tutela de urgência (art. 300) para suspender cobrança, protesto ou uso do documento, se houver perigo concreto.
- Declaração, em termos precisos, do que se pede (redigir como deverá constar do dispositivo da sentença).
- Pedido condenatório cumulado, se houver (restituição, indenização, abstenção), com juros e correção pelo núcleo `juros-e-correcao`.
- Citação; custas e honorários (art. 85); provas (perícia grafotécnica na falsidade).

## Checklist pré-protocolo
- [ ] Declaração pretendida redigida como dispositivo, sem ambiguidade
- [ ] Incerteza objetiva provada (documento de quem afirma o contrário)
- [ ] Todos os sujeitos da relação no polo passivo
- [ ] Natureza do vício conferida: nulidade (declaratória) x anulabilidade (constitutiva com prazo decadencial)
- [ ] Prescrição do pedido cumulado conferida e anotada
- [ ] Valor da causa pelo art. 292, II, com memória
- [ ] Opção sobre a audiência do art. 334

## Erros a evitar
- Pedir "declaração de fato" (que algo aconteceu): não cabe, salvo autenticidade/falsidade de documento.
- Chamar de declaratória o pedido de anular negócio anulável e perder o prazo decadencial.
- Valor da causa simbólico quando a relação tem conteúdo econômico (art. 292, § 3º, o juiz corrige).
- Afirmar imprescritibilidade sem fonte e deixar prescrever a condenação que deveria ser cumulada.
- Omitir litisconsorte necessário: a sentença não o vincula.

## Integração com o núcleo
`prazos-processuais`, `juros-e-correcao`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

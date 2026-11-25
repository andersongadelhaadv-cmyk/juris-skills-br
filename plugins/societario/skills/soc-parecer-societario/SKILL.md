---
name: soc-parecer-societario
description: >
  Redige parecer jurídico societário (opinião legal) sobre questão concreta
  de sociedade limitada ou anônima fechada: validade de deliberação e
  quórum, poderes de administrador, cessão de quotas e preferência,
  retirada, exclusão e haveres, reorganização (incorporação, fusão, cisão) e
  riscos de responsabilidade, com base nos arts. 1.053, 1.071, 1.076, 1.085
  e 1.031 do Código Civil e na Lei 6.404/1976. Use quando o usuário pedir
  parecer societário, opinião legal sobre ata ou alteração contratual, "a
  deliberação é válida?", "qual o quórum?", "posso excluir o sócio?", "quanto
  vale a quota de quem sai?" ou análise jurídica de reorganização societária.
metadata:
  area: societario
  tipo_peca: parecer
  verificado_em: 2026-11-25
---
# Parecer societário

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: pergunta jurídica societária concreta, por escrito, para orientar decisão do cliente (sócio, administrador, investidor, sociedade).
- Não usar: auditoria ampla de empresa (`soc-due-diligence-societaria`); redigir o contrato da operação (`soc-ma-compra-de-quotas-e-acoes`); ajuizar dissolução ou exclusão (`soc-dissolucao-parcial-e-exclusao-de-socio`); parecer sobre contrato não societário (`contratos-parecer-sobre-contrato`); questão tributária da reorganização (plugin `tributario-fazenda`, `trib-*`); partilha de quotas em divórcio ou herança (`familia-*`, `sucessoes-*`).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. A(s) pergunta(s) do consulente, em redação fechada.
2. Quem é o consulente e qual sua posição (sócio majoritário, minoritário, administrador, investidor).
3. Contrato social/estatuto consolidado e alterações; acordo de sócios; regência supletiva (art. 1.053 do CC: sociedade simples ou, se previsto, S.A.).
4. Atas, convocações, listas de presença, procurações e o quadro de capital na data do ato.
5. Documentos do fato (e-mails, notificações, balanços) e cronologia.
6. Urgência e uso do parecer (decisão interna, negociação, instrução de processo).

## Prazo e contagem
- Recesso por alteração, fusão ou incorporação: 30 dias da reunião (art. 1.077).
- Credores em incorporação, fusão ou cisão: 90 dias (art. 1.122 do CC); na S.A., 60 dias na incorporação/fusão (art. 232 da LSA).
- Pagamento de haveres: 90 dias da liquidação, salvo contrato (art. 1.031, § 2º).
- Prazo para anular deliberação de sócios: não conferido nesta skill [VERIFICAR: prazo decadencial aplicável à limitada e à S.A.]. Prazos processuais: `prazos-processuais`.

## Estrutura da peça
Ementa → consulta (quesitos) → documentos examinados e premissas → fatos relevantes → análise por quesito (norma, contrato social, jurisprudência verificada, aplicação) → riscos e alternativas → respostas objetivas aos quesitos → conclusão e ressalvas. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Ordem de análise: lei imperativa → contrato social/estatuto → acordo de sócios → regência supletiva → jurisprudência.
- Quórum na limitada: identifique a matéria no art. 1.071 e o quórum no art. 1.076 (mais da metade do capital para os incisos II a VI e VIII; maioria dos presentes nos demais, salvo quórum maior no contrato), ressalvado o art. 1.061 [VERIFICAR: texto atual do art. 1.061 não conferido nesta versão].
- Exclusão extrajudicial: os quatro requisitos do art. 1.085 (maioria do capital, gravidade que ameace a continuidade, cláusula de justa causa, reunião com ciência e defesa).
- Haveres: data da resolução e critério (art. 1.031 do CC; arts. 605 e 606 do CPC; STJ rejeita fluxo de caixa descontado no contrato omisso — REsp 2.063.134).
- Reorganização de S.A.: protocolo, justificação, laudo, quórum de reforma estatutária, recesso e credores (arts. 223 a 234 da LSA).
- Separe o que é certeza normativa, o que é entendimento jurisprudencial dominante e o que é opinião do parecerista.

## Fundamentos verificados
- CC arts. 421-A (paridade e alocação de riscos), 1.053 (regência supletiva), 1.071 e 1.076 (matérias e quóruns), 1.077 (recesso), 1.085 (exclusão), 1.031 (haveres), 1.116 a 1.122 (operações).
- CPC arts. 605 e 606 (data e critério de haveres).
- Lei 6.404/1976, arts. 223 a 234.
- STJ: REsp 2.063.134 (haveres sem expectativa de lucro futuro); REsp 2.170.665 (exclusão extrajudicial exige previsão contratual).
Detalhe em [fundamentos](references/fundamentos.md).

## Respostas aos quesitos (forma)
- Cada quesito recebe resposta direta (sim / não / depende de X), seguida da razão em 2 a 5 linhas e do grau de segurança (pacífico / majoritário / controvertido).
- Riscos com ação recomendada (notificar, convocar nova reunião, ratificar o ato, ajuizar, negociar).
- Alternativas quando a resposta for "não": caminho lícito para o mesmo objetivo.

## Checklist antes de entregar
- [ ] Quesitos transcritos e todos respondidos
- [ ] Contrato social consolidado conferido na versão vigente na data do ato
- [ ] Quórum calculado sobre o capital correto (excluídas quotas impedidas, se for o caso)
- [ ] Cada citação com fonte no `fontes.yaml`; nada de memória
- [ ] Ressalvas: documentos não examinados, fatos presumidos, data de corte
- [ ] Valores e atualizações pelo núcleo `juros-e-correcao`

## Erros a evitar
- Responder pela lei sem ler o contrato social (muitas regras do CC são supletivas).
- Confundir regência supletiva da limitada (simples x S.A.) e aplicar quórum errado.
- Chamar de "nula" deliberação que é, no máximo, anulável — e sem verificar prazo.
- Opinar sobre valor de quota sem indicar data-base e critério.
- Afirmar jurisprudência "pacífica" com um julgado só.
- Parecer que não responde à pergunta feita.

## Integração com o núcleo
`verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`, `juros-e-correcao`, `prazos-processuais`; skills irmãs `soc-due-diligence-societaria`, `soc-ma-compra-de-quotas-e-acoes`, `soc-dissolucao-parcial-e-exclusao-de-socio`.

---
name: trib-garantia-antecipada-certidao
description: >
  Redige ação de tutela cautelar antecedente de caução (garantia antecipada da
  futura execução fiscal) com seguro garantia, fiança bancária, depósito ou bem,
  para obter certidão positiva com efeito de negativa e afastar protesto e
  cadastros restritivos antes do ajuizamento (CTN art. 206; Tema 237/STJ; CPC
  arts. 305 a 309). Use quando o usuário pedir caução antecipada, antecipação de
  penhora, cautelar de caução, seguro garantia antes da execução fiscal,
  liberar CND/CPEN travada por débito inscrito ainda não executado, ou impedir
  protesto da CDA oferecendo garantia.
metadata:
  area: tributario-fazenda
  tipo_peca: inicial
  verificado_em: 2026-11-25
---
# Garantia antecipada para obter certidão

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: débito vencido (em regra já inscrito) que **ainda não foi executado**; o contribuinte não quer ou não pode discutir o mérito agora, mas precisa da certidão positiva com efeito de negativa (CPEN) — licitação, financiamento, alienação — e quer antecipar a garantia que daria na execução.
- Não usar:
  - execução fiscal já ajuizada: garanta nos próprios autos (LEF art. 9º) e peça a certidão (`trib-certidao-negativa-cpen`); para defender-se, `trib-embargos-a-execucao-fiscal`;
  - débito com exigibilidade já suspensa e certidão negada: `trib-certidao-negativa-cpen` ou `trib-mandado-de-seguranca`;
  - para discutir o mérito do crédito com depósito integral: `trib-acao-anulatoria` ou `trib-declaratoria-inexistencia-relacao-tributaria`;
  - pedido administrativo de oferta antecipada de garantia, quando o ente o prevê [VERIFICAR: ato normativo do ente credor].

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Relatório de situação fiscal ou extrato da dívida: inscrições, valores atualizados, natureza (tributária ou não).
2. Confirmação de que não há execução fiscal ajuizada (consulta processual pelo CNPJ/CPF nos tribunais competentes).
3. Garantia disponível: apólice de seguro garantia, carta de fiança, depósito, bem; valor coberto e prazo de vigência.
4. Finalidade e urgência concretas (edital, contrato, prazo de financiamento) com documentos.
5. Protesto lavrado, inscrição em CADIN ou cadastros de crédito, averbação em registro de bens.
6. Ente credor e competência (Justiça Federal para a União; vara da Fazenda Pública estadual ou municipal).

## Prazo e contagem
- Não há prazo para propor; a medida perde sentido se a execução for ajuizada antes (a garantia passa a ser oferecida nela).
- Rito da cautelar antecedente: contestação em 5 dias (CPC art. 306); efetivada a medida, pedido principal em 30 dias nos mesmos autos (art. 308); a tutela perde eficácia nas hipóteses do art. 309. Quando a garantia é antecipação da penhora, o "pedido principal" é a própria execução fiscal futura — explique isso na inicial e veja o checklist [VERIFICAR: tratamento do art. 308 na cautelar de caução no tribunal local].
- Contagem em dias úteis e demais prazos: `prazos-processuais`.

## Estrutura da peça
Endereçamento → partes → cabimento (Tema 237/STJ) → débito e inexistência de execução → garantia idônea e suficiente → urgência → pedidos (aceitação, CPEN, abstenção de protesto/cadastros, transferência futura da garantia para a execução). Roteiro em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Cabimento: "o contribuinte pode, após o vencimento da obrigação e antes da execução, garantir o juízo de forma antecipada, para o fim de obter a certidão positiva com efeito de negativa" (Tema 237/STJ, REsp 1.123.669, citado no AgInt no REsp 2.006.993, 1ª Turma, 2023). A medida é instrumental: não exige ajuizamento de anulatória como condição (mesmo acórdão).
- Fundamento da certidão: o CTN dá à certidão positiva os efeitos da negativa quando há créditos não vencidos, cobrança executiva com penhora efetivada ou exigibilidade suspensa (art. 206). A caução antecipada é tratada como antecipação da penhora.
- Garantias admitidas na execução fiscal: depósito, fiança bancária ou seguro garantia, nomeação de bens, bens de terceiros aceitos (LEF art. 9º); depósito, fiança e seguro produzem os efeitos da penhora (§ 3º); fiança e seguro só se liquidam após o trânsito de decisão de mérito desfavorável (§ 7º).
- **Crédito tributário**: até a LC 236/2026, o STJ entendia que seguro e fiança autorizavam a CPEN mas não suspendiam a exigibilidade nem impediam o CADIN (AgInt no REsp 2.158.109, 2ª Turma, 2024; Súmula 112/STJ). A LC 236/2026 incluiu no CTN a suspensão da exigibilidade pela aceitação, pelo credor, de seguro garantia ou fiança **oferecidos em execução fiscal** (art. 151, X). Antes do ajuizamento, não conte com a suspensão; peça a certidão e a abstenção de atos com base no Tema 237 [VERIFICAR: posição do STJ sobre a garantia antecipada após a LC 236/2026].
- **Crédito não tributário**: fiança ou seguro de valor igual ao débito atualizado mais 30% suspende a exigibilidade, salvo insuficiência, defeito formal ou inidoneidade demonstrados pelo credor (Tema 1.203/STJ).
- Honorários: a cautelar de caução é tratada como incidente da execução fiscal, sem condenação de qualquer parte em honorários (AgInt no AREsp 2.755.025, 2ª Turma, 2025).

## Fundamentos verificados
CTN arts. 151 (LC 236/2026) e 206; LEF art. 9º; CPC arts. 305 a 309; Súmula 112/STJ; Tema 237/STJ (via AgInt no REsp 2.006.993 e AgInt no REsp 2.158.109); Tema 1.203/STJ; AgInt no AREsp 2.755.025. Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Liminar: aceitação da garantia e ordem de expedição da CPEN quanto aos débitos garantidos.
- Abstenção de protesto (ou sustação/cancelamento) e de inscrição em cadastros restritivos pelos mesmos débitos; no crédito não tributário, suspensão da exigibilidade (Tema 1.203).
- Intimação da Fazenda para se manifestar sobre a idoneidade e a suficiência da garantia.
- Que a garantia seja transferida para a execução fiscal quando ajuizada.
- Sem pedido de honorários contra a Fazenda (AgInt no AREsp 2.755.025).
- Atualização do valor garantido: `juros-e-correcao`.

## Checklist pré-protocolo
- [ ] Nenhuma execução fiscal ajuizada pelos débitos (consulta juntada)
- [ ] Valor da garantia cobre o débito atualizado (e o acréscimo de 30% no não tributário)
- [ ] Apólice/carta conforme a regulamentação do credor (vigência, cláusulas, renovação)
- [ ] Débitos identificados um a um (inscrição, valor)
- [ ] Urgência documentada
- [ ] Tratamento do pedido principal (art. 308) explicado

## Erros a evitar
- Usar a cautelar para discutir o mérito do crédito: a garantia é instrumental.
- Garantia insuficiente ou com prazo que vence antes do fim previsível da discussão.
- Prometer ao cliente suspensão da exigibilidade do crédito tributário antes da execução.
- Não acompanhar o ajuizamento da execução: a garantia precisa ser transferida e o prazo de embargos passa a correr (`trib-embargos-a-execucao-fiscal`).
- Calcular a atualização do débito por índice próprio: `juros-e-correcao`.

## Integração com o núcleo
`prazos-processuais`, `juros-e-correcao`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`, `civel-tutela-provisoria`.

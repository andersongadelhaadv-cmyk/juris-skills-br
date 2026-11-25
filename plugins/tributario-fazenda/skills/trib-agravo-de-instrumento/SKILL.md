---
name: trib-agravo-de-instrumento
description: >
  Redige agravo de instrumento em matéria tributária (CPC arts. 1.015 a 1.019;
  Lei 12.016/2009, art. 7º, §1º) contra decisões em execução fiscal, em ações
  anulatórias, declaratórias e de repetição e em mandado de segurança
  tributário, com pedido de efeito suspensivo ou tutela recursal. Use quando o
  usuário pedir agravo contra liminar negada em MS tributário, contra decisão
  que rejeitou exceção de pré-executividade, que deferiu redirecionamento ao
  sócio, penhora ou bloqueio de contas em execução fiscal, que recusou seguro
  garantia, ou que negou tutela para suspender a exigibilidade do tributo.
metadata:
  area: tributario-fazenda
  tipo_peca: recurso
  verificado_em: 2026-11-25
---
# Agravo de instrumento em matéria tributária

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: decisão interlocutória em processo tributário, especialmente:
  - **execução fiscal** — todas as interlocutórias são agraváveis por estarem no processo de execução (CPC art. 1.015, parágrafo único): rejeição de exceção de pré-executividade, redirecionamento a sócio, penhora, bloqueio de ativos, recusa de garantia, substituição de bens;
  - **tutela provisória** em anulatória, declaratória ou repetição (art. 1.015, I) — concessão, negativa ou revogação da suspensão da exigibilidade;
  - **liminar em mandado de segurança** concedida ou negada pelo juiz de primeiro grau (Lei 12.016, art. 7º, §1º);
  - efeito suspensivo dos embargos à execução fiscal (art. 1.015, X).
- Fora do rol, só com urgência que torne inútil o exame na apelação (Tema 988 STJ, taxatividade mitigada).
- Não usar: sentença em execução fiscal de valor igual ou inferior a 50 ORTN (cabem só embargos infringentes e de declaração — LEF art. 34; Tema 408 STF); decisão de relator (`civel-agravo-interno`); sentença (`civel-apelacao`); agravo sem nenhum componente tributário (`civel-agravo-de-instrumento`); fase trabalhista (`trabalhista-agravo-de-peticao`).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Decisão agravada e data/forma da intimação (para a Fazenda, intimação pessoal).
2. Petição que provocou a decisão (exceção, pedido de liminar, impugnação à penhora) e documentos que a instruíram.
3. Situação do crédito: CDA, valor, garantias oferecidas, parcelamento, depósito.
4. Dano concreto da manutenção da decisão: bloqueio em curso, certidão negada, leilão marcado, licitação, folha de pagamento.
5. Procurações e endereços dos advogados das partes.

## Prazo e contagem
- 15 dias úteis (CPC art. 1.003, §5º); a Fazenda tem prazo em dobro, contado da intimação pessoal (art. 183).
- Resposta do agravado em 15 dias (art. 1.019, II).
- Contagem, feriados locais (comprovar no ato — art. 1.003, §6º) e recesso: `prazos-processuais`.

## Estrutura da peça
Petição ao tribunal (art. 1.016) → tempestividade e preparo → cabimento (inciso do art. 1.015, parágrafo único, Lei 12.016 ou Tema 988) → decisão agravada → razões tributárias → efeito suspensivo ou tutela recursal → pedidos → peças. Roteiro em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Requisitos do art. 1.016 (nomes das partes, fato e direito, razões e pedido, nome e endereço dos advogados).
- Instrução do art. 1.017; em autos eletrônicos, as peças obrigatórias são dispensadas (§5º), mas junte o que for essencial para o relator entender a controvérsia.
- Efeito suspensivo ou antecipação da tutela recursal pelo relator em 5 dias (art. 1.019, I): demonstre probabilidade e risco concreto.
- **Exceção de pré-executividade rejeitada**: o tribunal só examina matérias de ordem pública sem dilação probatória (Súmula 393 STJ); se a matéria exige prova, o caminho é embargos garantidos (`trib-embargos-a-execucao-fiscal`).
- **Tutela para suspender exigibilidade**: lembre que o depósito integral e em dinheiro suspende por si (CTN art. 151, II; Súmula 112 STJ) e torna o agravo desnecessário em muitos casos; tutela é a hipótese do art. 151, V.
- **Redirecionamento ao sócio**: confronte a decisão com o CTN art. 135 e com a prova de atos com excesso de poderes ou infração de lei; o mero inadimplemento não gera, por si só, a responsabilidade do sócio-gerente (Súmula 430 STJ); a dissolução irregular presumida legitima o redirecionamento (Súmula 435 STJ) — enfrente a prova dessa presunção.

## Fundamentos verificados
CPC arts. 183, 1.003, 1.015, 1.016, 1.017, 1.019; Lei 12.016/2009, art. 7º, §1º; LEF art. 34; CTN arts. 135 e 151; Tema 988 STJ; Tema 408 STF; Súmulas 112, 393, 430 e 435 STJ. Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Efeito suspensivo (suspender penhora, bloqueio, leilão, redirecionamento) ou tutela recursal (conceder a suspensão da exigibilidade, a liminar do MS, a aceitação da garantia).
- Comunicação imediata ao juízo de origem.
- Intimação do agravado para resposta.
- Provimento para reformar ou invalidar a decisão; se exceção de pré-executividade, extinção da execução ou exclusão do sócio do polo, com honorários.
- Prequestionamento dos dispositivos federais e constitucionais em debate.

## Checklist pré-protocolo
- [ ] Hipótese de cabimento indicada (inciso do art. 1.015, parágrafo único, Lei 12.016 ou urgência do Tema 988)
- [ ] Verificado que não é sentença de execução fiscal de alçada (LEF art. 34)
- [ ] Prazo conferido (dobro e intimação pessoal se Fazenda)
- [ ] Preparo e porte de retorno, quando devidos
- [ ] Peças essenciais anexadas, mesmo em autos eletrônicos
- [ ] Risco concreto demonstrado para o pedido de efeito suspensivo
- [ ] Matéria de exceção sem dilação probatória (Súmula 393)

## Erros a evitar
- Agravar de sentença de execução fiscal de pequeno valor: o recurso é embargos infringentes no próprio juízo (LEF art. 34).
- Pedir efeito suspensivo com perigo genérico ("dano irreparável") sem bloqueio, leilão ou certidão concretos.
- Levar ao tribunal, em exceção de pré-executividade, matéria que depende de prova.
- Deixar de comprovar feriado local no ato de interposição.
- Esquecer que, para a Fazenda, o prazo é em dobro e corre da intimação pessoal.

## Integração com o núcleo
`prazos-processuais`, `juros-e-correcao`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

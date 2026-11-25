---
name: trib-habilitacao-de-credito-judicial
description: >
  Orienta o aproveitamento de indébito tributário reconhecido em decisão
  judicial transitada em julgado: escolha entre precatório/RPV e compensação
  (Súmula 461 STJ), pedido de habilitação do crédito perante a Receita (CTN art.
  168, §§ 2º e 3º; Lei 9.430/1996, arts. 74 e 74-A) e desistência da execução
  judicial. Use quando o usuário pedir habilitação de crédito judicial na
  Receita, aproveitar crédito de ação tributária ganha, escolher entre precatório
  e compensação, prazo para habilitar o crédito ou indeferimento da habilitação.
metadata:
  area: tributario-fazenda
  tipo_peca: requerimento
  verificado_em: 2026-11-25
---
# Habilitação de crédito tributário reconhecido judicialmente

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: (a) ação de repetição, declaratória ou mandado de segurança transitou em julgado reconhecendo o indébito ou o direito de compensar; (b) é preciso decidir entre receber em dinheiro (precatório/RPV) ou compensar; (c) pedido de habilitação na Receita; (d) despacho que indefere a habilitação.
- Receber em dinheiro (precatório/RPV): o cumprimento de sentença contra a Fazenda é feito em `fazenda-cumprimento-contra-a-fazenda` — esta skill só ajuda a escolher.
- Já habilitado e é hora de transmitir a DCOMP: `trib-compensacao-per-dcomp`.
- Ainda sem trânsito em julgado: a compensação é vedada (CTN art. 170-A); não use esta skill.
- Tributo estadual ou municipal: aplicar a lei do ente; esta skill serve de roteiro.

## Entradas mínimas (perguntar o que faltar; nunca supor fatos)
1. Sentença, acórdãos e **certidão de trânsito em julgado** (data certificada).
2. Dispositivo exato: tributo, período, alcance (declaração do direito de compensar, condenação a restituir, ambos), critérios de atualização fixados.
3. Se houve execução judicial ou cumprimento de sentença iniciado (exige desistência para compensar).
4. Valor estimado do crédito, com memória de cálculo e documentos de pagamento.
5. Titularidade (o crédito é do próprio contribuinte? houve sucessão, incorporação, cisão?).
6. Débitos que se pretende compensar e se há limite mensal (crédito acima de R$ 10 milhões, art. 74-A).

## Prazo e contagem
- Habilitação: 5 anos contados da certificação do trânsito em julgado (CTN art. 168, §§ 2º e 3º, LC 236/2026).
- Primeira DCOMP do crédito sujeito ao limite mensal: em até 5 anos do trânsito ou da homologação da desistência da execução (Lei 9.430, art. 74-A, § 2º).
- Prazo de análise do pedido pela Receita e recurso contra o indeferimento: norma infralegal [VERIFICAR].
- Prazos judiciais: `prazos-processuais`.

## Estrutura da peça
Avaliação da via (dinheiro x compensação) → pedido de habilitação: identificação da ação e do trânsito → título e alcance → titularidade → desistência ou inexistência de execução → demonstrativo do crédito → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Opção do contribuinte: precatório ou compensação do indébito certificado por sentença declaratória transitada (Súmula 461 STJ).
- Compensação de crédito judicial só depois do trânsito (CTN art. 170-A; Lei 9.430, art. 74, § 12, II — decisão não transitada torna a compensação "não declarada").
- O art. 74 da Lei 9.430 admite expressamente crédito judicial transitado em julgado.
- Crédito total igual ou acima de R$ 10 milhões: limite mensal de compensação (art. 74-A, § 1º), não inferior a 1/60 do crédito.
- Execução judicial em curso: precisa ser desistida (e homologada) para compensar; a Receita exige prova disso [VERIFICAR requisito na instrução normativa vigente].
- A habilitação não homologa o valor do crédito: a liquidez é verificada depois, na análise das DCOMPs [VERIFICAR na norma infralegal].

## Fundamentos verificados
- CTN arts. 168 (§§ 2º e 3º), 170, 170-A.
- Lei 9.430/1996, art. 74 (caput e § 12) e art. 74-A.
- Súmula 461 do STJ; Súmula 213 do STJ (MS para declarar o direito de compensar).
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Deferimento da habilitação do crédito decorrente do processo nº ..., transitado em ....
- Juntada do título, da certidão de trânsito, da prova de desistência (ou de inexistência) da execução e dos documentos societários.
- Contra indeferimento: correção do vício apontado ou recurso previsto na norma; persistindo, `trib-mandado-de-seguranca`.
- Atualização do crédito: núcleo `juros-e-correcao` (não fixar índice na peça).

## Checklist pré-protocolo
- [ ] Data da certificação do trânsito anotada e prazo de 5 anos controlado
- [ ] Alcance do título conferido (período, tributo, compensar ou restituir)
- [ ] Escolha precatório x compensação registrada por escrito com o cliente
- [ ] Execução judicial desistida e homologada (se havia)
- [ ] Titularidade e sucessões documentadas
- [ ] Limite mensal do art. 74-A considerado no planejamento

## Erros a evitar
- Transmitir DCOMP antes de habilitar (ou antes do trânsito).
- Perder o prazo de 5 anos aguardando liquidação que não é exigida para habilitar [VERIFICAR na norma].
- Prosseguir com o cumprimento de sentença e ao mesmo tempo pedir habilitação para compensar o mesmo crédito.
- Ignorar o limite mensal do art. 74-A no fluxo de caixa do cliente.

## Integração com o núcleo
`juros-e-correcao`, `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`. Vizinhas: `fazenda-cumprimento-contra-a-fazenda` (precatório/RPV), `trib-compensacao-per-dcomp`, `trib-repeticao-de-indebito`, `trib-transacao-tributaria` (precatório como meio de pagamento).

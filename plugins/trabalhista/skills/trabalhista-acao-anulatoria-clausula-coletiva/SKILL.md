---
name: trabalhista-acao-anulatoria-clausula-coletiva
description: >
  Redige ação anulatória de cláusula de convenção coletiva ou de acordo coletivo
  de trabalho, com controle limitado aos elementos essenciais do negócio jurídico
  (CLT art. 8º, §3º, e art. 611-A), objeto ilícito do art. 611-B, litisconsórcio
  necessário dos sindicatos subscritores e o Tema 1046 do STF. Use quando o
  usuário pedir anulação de cláusula de CCT ou ACT, ação anulatória do MPT,
  nulidade de norma coletiva que suprime direito indisponível, defesa de
  sindicato em ação anulatória ou contestação da validade de instrumento coletivo.
metadata:
  area: trabalhista
  tipo_peca: inicial
  verificado_em: 2026-11-25
---
# Ação anulatória de cláusula de norma coletiva

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: pedido autônomo de declaração de nulidade de uma ou mais cláusulas de CCT ou ACT, com efeito sobre toda a categoria ou empresa abrangida.
- Também: defesa dos sindicatos réus (a mesma skill orienta a contestação, invertendo os argumentos).
- Não usar: nulidade alegada só como questão incidental numa reclamação individual (`trabalhista-reclamacao` ou `trabalhista-contestacao`); criação de novas condições de trabalho (`trabalhista-dissidio-coletivo`); desconstituição de sentença normativa transitada (`trabalhista-acao-rescisoria`); anulação de ato administrativo (`adm-acao-anulatoria-de-ato-administrativo`); contrato civil ou empresarial (`contratos-analise-e-revisao-de-contrato`).

## Entradas mínimas (perguntar o que faltar; nunca supor fatos)
1. Íntegra do instrumento coletivo, com vigência, partes signatárias e base territorial.
2. Cláusulas impugnadas, transcritas, e o direito que cada uma limita ou suprime.
3. Prova do registro/depósito e da assembleia que autorizou a negociação (edital, ata, lista de presença).
4. Quem é o autor (MPT, sindicato, empresa, empregado) e qual o interesse dele.
5. Existe cláusula compensatória ligada à cláusula impugnada?
6. Há reclamações individuais ou ação civil pública sobre as mesmas cláusulas?

## Prazo e contagem
- Não há prazo decadencial específico conferido em lei para esta ação [VERIFICAR: efeito do fim da vigência do instrumento sobre o interesse de agir, conforme jurisprudência da SDC].
- Prazos de resposta e de recurso (recurso ordinário em 8 dias contra decisão de TRT em competência originária — CLT art. 895, II): conferir pelo núcleo `prazos-processuais`.

## Estrutura da peça
Endereçamento → legitimidade e litisconsórcio → instrumento e cláusulas → limites do controle judicial (art. 8º §3º) → causa de nulidade de cada cláusula (vício formal do negócio, objeto ilícito do art. 611-B, direito absolutamente indisponível — Tema 1046) → efeito sobre cláusula compensatória (art. 611-A §4º) → tutela provisória, se houver → pedidos. Roteiro em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Legitimidade:** o MPT tem atribuição legal expressa (LC 75/1993, art. 83, IV). Sindicatos signatários e membros isolados da categoria: a legitimidade é tema jurisprudencial; o TST tem acórdão recente sobre empresa isolada (RR 678-14.2022.5.09.0084) cuja conclusão não foi lida na íntegra [VERIFICAR: ler o inteiro teor antes de afirmar a tese].
- **Litisconsórcio necessário:** os sindicatos subscritores devem integrar o polo passivo (CLT art. 611-A, §5º). Faltando um, a peça nasce com nulidade.
- **Competência:** na prática forense a ação coletiva é ajuizada no TRT da base territorial, com recurso ordinário à SDC do TST (há acórdãos da SDC julgando ROs em anulatórias do MPT). A regra de competência originária vem da jurisprudência e do regimento do tribunal, não de artigo expresso de lei [VERIFICAR: regimento interno do TRT competente].

## Fundamentos verificados
- CLT art. 8º, §3º: a Justiça do Trabalho analisa só a conformidade dos elementos essenciais do negócio jurídico (art. 104 do CC), pelo princípio da intervenção mínima.
- CLT art. 611-A, §§1º, 2º, 4º e 5º; art. 611-B (objeto ilícito).
- STF, Tema 1046 (ARE 1.121.633): validade da norma coletiva que limita ou afasta direito, salvo direitos absolutamente indisponíveis.
- SDC/TST, RO 228-69.2016.5.08.0000: mantida nulidade de jornada 15x15 em turnos de 12x12 mesmo após o Tema 1046 (limite constitucional de jornada e repouso).
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Declaração de nulidade de cada cláusula, identificada por número e texto.
- Se houver cláusula compensatória vinculada: sua anulação conjunta, sem repetição do indébito (art. 611-A, §4º) — o autor deve antecipar esse efeito, não ser surpreendido por ele.
- Tutela provisória para suspender a eficácia da cláusula, com demonstração concreta do dano.
- Citação de todos os sindicatos subscritores; intimação do MPT quando não for autor.
- Juros e correção (se houver pedido pecuniário reflexo): núcleo `juros-e-correcao`.

## Checklist pré-protocolo
- [ ] Instrumento coletivo íntegro juntado, com registro e vigência
- [ ] Todos os sindicatos subscritores no polo passivo
- [ ] Cada cláusula enquadrada: vício do negócio, objeto ilícito (art. 611-B) ou direito indisponível
- [ ] Tema 1046 enfrentado expressamente
- [ ] Cláusula compensatória mapeada
- [ ] Legitimidade ativa fundamentada (e conferida, se o autor não for o MPT)
- [ ] Competência conferida no regimento do TRT

## Erros a evitar
- Atacar a conveniência da cláusula: o controle é de validade, não de mérito da negociação (art. 8º, §3º).
- Alegar falta de contrapartida como causa de nulidade (art. 611-A, §2º afasta isso).
- Esquecer que a nulidade da cláusula pode arrastar a cláusula compensatória.
- Citar o Tema 1046 só pelo resultado, sem identificar qual direito seria "absolutamente indisponível" no caso.

## Integração com o núcleo
`prazos-processuais`, `juros-e-correcao`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

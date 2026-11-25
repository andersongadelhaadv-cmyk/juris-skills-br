---
name: trib-declaratoria-inexistencia-relacao-tributaria
description: >
  Redige ação declaratória de inexistência de relação jurídico-tributária
  (CPC arts. 19, I, e 20), preventiva ou cumulada com repetição, com tutela ou
  depósito integral para suspender a exigibilidade (CTN art. 151, II e V;
  Súmula 112 STJ) e atenção aos limites da coisa julgada em relação de trato
  continuado (Súmula 239 STF; Tema 885 STF). Use quando o usuário pedir ação
  declaratória tributária, declarar que não deve um tributo, afastar a
  incidência para o futuro, declarar imunidade, isenção ou não incidência,
  ação para não pagar tributo inconstitucional ou declaratória com pedido de
  compensação.
metadata:
  area: tributario-fazenda
  tipo_peca: inicial
  verificado_em: 2026-11-25
---
# Ação declaratória de inexistência de relação jurídico-tributária

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: o cliente quer certeza judicial de que **não está obrigado** a um tributo (ou a parte dele) em relação que se repete: não incidência, imunidade, isenção, inconstitucionalidade ou ilegalidade da norma, base de cálculo indevida. Serve antes de qualquer lançamento (preventiva) e também para o futuro de uma cobrança já iniciada.
- Usar cumulada com repetição ou compensação quando já houve pagamento: a sentença declaratória que certifica o indébito permite optar entre precatório e compensação (Súmula 461 STJ).
- Não usar: crédito já lançado ou inscrito que se quer desconstituir (`trib-acao-anulatoria`); ato concreto recente, prova só documental e interesse em rito rápido (`trib-mandado-de-seguranca`); só restituição do que foi pago (`trib-repeticao-de-indebito`); débito em execução fiscal (`trib-embargos-a-execucao-fiscal` ou `trib-excecao-pre-executividade-fiscal`); dúvida entre dois entes que cobram o mesmo tributo (`trib-consignacao-em-pagamento`).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Tributo, ente tributante, períodos e atividade do cliente (contrato social, CNAE, notas, contratos).
2. Norma que institui a cobrança e a tese: inconstitucionalidade, ilegalidade, imunidade, isenção ou não incidência.
3. Já pagou? Desde quando? Quer restituir, compensar ou só deixar de pagar?
4. Há lançamento, auto de infração, inscrição ou execução sobre o mesmo tributo?
5. Existe precedente vinculante (repercussão geral, repetitivo, ADI) a favor ou contra a tese, e se houve modulação.
6. Interesse em depositar em dinheiro ou necessidade de tutela de urgência (certidão, licitação, crédito).

## Prazo e contagem
- Pretensão meramente declaratória: prazo prescricional não conferido em fonte oficial [VERIFICAR: há julgados do STJ que tratam a anulação de lançamento como prescritível; confirme no `verificacao-de-citacoes` antes de afirmar imprescritibilidade].
- Pedido cumulado de repetição ou compensação: prazo do CTN (arts. 165 e 168) tratado em `trib-repeticao-de-indebito`.
- Contestação da Fazenda em dobro com intimação pessoal (CPC art. 183). Contagem: `prazos-processuais`.

## Estrutura da peça
Endereçamento → partes → síntese da relação tributária → cabimento da declaratória (CPC 19, I, e 20) → competência → tutela ou depósito → tese (inconstitucionalidade, ilegalidade, imunidade, não incidência) → precedentes vinculantes e modulação → pedido cumulado (repetição/compensação) → provas → pedidos. Roteiro em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Interesse de agir: basta a incerteza objetiva sobre a relação jurídica; a ação declaratória é admissível ainda que a violação já tenha ocorrido (CPC art. 20).
- Competência: tributo federal ou da União (ou autarquia federal) vai à Justiça Federal (CF art. 109, I); estadual e municipal, à Vara da Fazenda Pública estadual.
- Polo passivo: o ente tributante (pessoa jurídica de direito público), não a autoridade fiscal.
- Suspensão da exigibilidade: depósito integral e em dinheiro (CTN art. 151, II; Súmula 112 STJ) ou tutela provisória (CTN art. 151, V; CPC art. 300). Sem um dos dois, a Fazenda pode lançar e cobrar enquanto o processo corre.
- Coisa julgada e períodos futuros: decisão que declara indevida a cobrança em um exercício não faz coisa julgada para os posteriores (Súmula 239 STF). Por isso, peça declaração sobre a **relação jurídica** (enquanto mantida a norma e os fatos), não sobre um exercício isolado.
- Tema 885 STF: decisão do STF em ação direta ou em repercussão geral interrompe automaticamente os efeitos da coisa julgada em relação tributária de trato sucessivo, respeitadas irretroatividade e anterioridades. Avise o cliente de que a vitória pode perder efeito se o STF decidir em sentido contrário.

## Fundamentos verificados
CPC arts. 19, I, 20, 183 e 300; CTN arts. 151 e 165; CF art. 109, I; Súmula 112 STJ; Súmula 461 STJ; Súmula 239 STF; Tema 885 STF (RE 955.227); AgInt no REsp 2.051.180 (cumulação sucessiva declaratória + repetição). Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Tutela provisória (ou autorização de depósito integral) para suspender a exigibilidade, vedar autuação, inscrição em dívida ativa, protesto e negativa de certidão.
- Citação do ente pela respectiva advocacia pública.
- Declaração de inexistência da relação jurídico-tributária quanto ao tributo/parcela, enquanto vigente a norma e mantida a situação de fato descrita.
- Cumulado (sucessivo): restituição ou compensação do indébito do período não prescrito, com atualização pelo núcleo `juros-e-correcao`.
- Levantamento do depósito ao final se procedente; conversão em renda só após trânsito em julgado.
- Honorários contra a Fazenda (CPC art. 85) e produção de prova documental/pericial.

## Checklist pré-protocolo
- [ ] Tese confrontada com precedentes vinculantes e eventual modulação de efeitos
- [ ] Pedido redigido sobre a relação jurídica (não só sobre um exercício)
- [ ] Juízo competente conforme o ente (Justiça Federal x Fazenda Pública estadual)
- [ ] Depósito integral calculado com a Fazenda ou tutela fundamentada (probabilidade + perigo)
- [ ] Pedido de repetição/compensação, se houver pagamento, com recorte do período não prescrito
- [ ] Cliente avisado do Tema 885 (efeito de decisão futura do STF)
- [ ] Juros e correção remetidos ao núcleo

## Erros a evitar
- Usar declaratória pura quando já há lançamento: o pedido certo é anulatório (`trib-acao-anulatoria`) ou os dois cumulados.
- Esquecer de suspender a exigibilidade e ser surpreendido por autuação com multa durante o processo.
- Pedir declaração para "todos os exercícios" sem amarrar à norma vigente e aos fatos (Súmula 239 STF).
- Prometer ao cliente coisa julgada eterna: o Tema 885 permite a cessação automática.
- Depositar valor parcial ou descontado: só depósito integral suspende (Súmula 112 STJ).

## Integração com o núcleo
`juros-e-correcao`, `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

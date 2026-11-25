---
name: imob-revisao-de-financiamento-sfh
description: >
  Redige ação revisional de contrato de financiamento habitacional (SFH ou SFI),
  com ou sem alienação fiduciária (Lei 9.514/1997), e orienta o uso do FGTS na
  aquisição, amortização ou quitação (Lei 8.036/1990, art. 20), sem fixar taxa
  própria: juros e correção vão ao núcleo. Use quando o usuário pedir revisão
  de financiamento da casa própria, discussão de Tabela Price ou SAC, seguro
  habitacional imposto pelo banco, saldo devedor que não cai, purgação da mora
  antes do leilão, nulidade de consolidação da propriedade ou uso do FGTS para
  abater prestações.
metadata:
  area: imobiliario
  tipo_peca: inicial
  verificado_em: 2026-11-25
---
# Revisão de financiamento habitacional (SFH/SFI) e uso do FGTS

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: (a) revisional de mútuo habitacional (SFH, SFI, crédito associativo, financiamento direto com alienação fiduciária); (b) nulidade do procedimento extrajudicial da Lei 9.514/1997 (intimação, leilão); (c) pedido de purgação da mora; (d) uso do FGTS (aquisição, amortização, liquidação, abatimento de prestações), inclusive negativa da Caixa.
- Não usar: empréstimo bancário sem garantia imobiliária (`consumidor-contratos-bancarios-revisional`); devolução de parcelas pagas à incorporadora (`imob-distrato-imobiliario`); superendividamento global (`consumidor-superendividamento`); execução hipotecária já em fase judicial (`civel-embargos-a-execucao`).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Contrato completo, aditivos e **data de assinatura** (muda a lei e o enquadramento: SFH, SFI, FCVS).
2. Agente financeiro e enquadramento (SFH ou SFI); sistema de amortização (Price, SAC, SACRE, PES).
3. Planilha de evolução do saldo devedor e extratos das prestações pagas.
4. Seguros cobrados (MIP, DFI) e quem é a seguradora; houve escolha?
5. Situação: adimplente, em atraso (quantas parcelas), intimado para purgar a mora, propriedade consolidada, leilão marcado (datas).
6. Matrícula atualizada (registro da alienação fiduciária, averbação da consolidação).
7. FGTS: tempo de trabalho sob o regime, se tem outro imóvel no município de residência ou outro financiamento SFH, último saque para o mesmo contrato.

## Prazo e contagem
- Purgação da mora após intimação: 15 dias (Lei 9.514/1997, art. 26, § 1º). Leilão: em 60 dias do registro da consolidação; segundo leilão nos 15 dias seguintes (art. 27, caput e § 1º).
- Leilão marcado = urgência: tutela antes da data, com prova do registro e da intimação.
- FGTS: amortização ou liquidação com interstício mínimo de 2 anos (Lei 8.036/1990, art. 20, VI), salvo alienação fiduciária dos direitos de saque (§ 27).
- Prescrição de repetição de valores pagos a maior: [VERIFICAR via `verificacao-de-citacoes`]. Prazos processuais: `prazos-processuais`.

## Estrutura da peça
Fatos e contrato → enquadramento (SFH/SFI; data) → cláusulas questionadas, uma a uma, com prova pericial → seguro → situação da mora e do procedimento extrajudicial → tutela (depósito do incontroverso, suspensão do leilão) → pedidos e perícia. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Competência: Justiça Federal quando a Caixa (ou a União/FCVS) integra a lide; estadual nos demais agentes.
- Especificar as obrigações controvertidas e o valor incontroverso; propor depósito do incontroverso.
- Pedir perícia contábil: a capitalização na Tabela Price é questão de fato, não se presume (REsp 2.103.041, 4ª Turma, 2026).
- Alienação fiduciária registrada: a execução extrajudicial é constitucional (Tema 982/STF). Atacar vícios concretos do procedimento (intimação pessoal, prazos, avaliação, leilões), não o procedimento em si.
- Aplicação do CDC ao contrato: depende da data e do caso [VERIFICAR: jurisprudência atual do STJ].

## Fundamentos verificados
- Lei 4.380/1964 (SFH), arts. 5º e 6º; Súmula 422/STJ (art. 6º, e, não limita juros).
- Súmula 450/STJ (atualização do saldo antes da amortização); Súmula 454/STJ (TR quando pactuado índice da poupança, após a Lei 8.177/1991); Súmula 473/STJ (seguro habitacional não pode ser imposto com a mutuante ou seguradora por ela indicada).
- Lei 9.514/1997, arts. 22, 23, 26, 26-A e 27 (redação da Lei 14.711/2023).
- Lei 8.036/1990, art. 20, V, VI, VII, §§ 3º, 17 e 27.
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Revisão das cláusulas específicas (com indicação do dispositivo contratual) e recálculo por perícia.
- Taxa, índice e capitalização: **nenhum percentual na peça sem passar pelo núcleo `juros-e-correcao`**; o pedido é de recálculo conforme o critério jurídico demonstrado.
- Restituição ou compensação do que foi pago a maior (forma simples ou dobrada conforme fundamento; ver `consumidor-repeticao-em-dobro`).
- Declaração de abusividade da venda casada do seguro e restituição do prêmio excedente.
- Tutela: depósito do incontroverso, suspensão do leilão ou de seus efeitos, abstenção de negativação.
- Nulidade da consolidação ou do leilão por vício concreto, com purgação da mora oferecida.
- FGTS: liberação do saldo para a finalidade legal (prova do preenchimento das condições do art. 20).

## Checklist pré-protocolo
- [ ] Data e enquadramento do contrato identificados (SFH x SFI; FCVS)
- [ ] Cláusulas questionadas transcritas e valor incontroverso calculado pelo núcleo
- [ ] Pedido de perícia contábil com quesitos
- [ ] Súmulas 450, 454 e 422 enfrentadas (são favoráveis ao banco)
- [ ] Seguro: prova de que não houve escolha (Súmula 473)
- [ ] Matrícula com registro da garantia e eventual consolidação
- [ ] Datas de intimação e leilão conferidas contra os prazos dos arts. 26 e 27
- [ ] Competência (Caixa → Justiça Federal)
- [ ] FGTS: requisitos do art. 20 e vedações do § 17 checados

## Erros a evitar
- Alegar "Tabela Price é ilegal" em tese, sem perícia.
- Pedir limitação de juros a 10% com base no art. 6º, e, da Lei 4.380/1964 (Súmula 422).
- Pedir que a amortização anteceda a correção do saldo (Súmula 450).
- Atacar a constitucionalidade da execução extrajudicial (Tema 982/STF) em vez de vícios concretos.
- Esquecer o interstício de 2 anos ou a vedação do § 17 no pedido de FGTS.
- Inventar taxa ou índice "justo": isso é do núcleo.

## Integração com o núcleo
`juros-e-correcao` (obrigatório em todo cálculo), `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

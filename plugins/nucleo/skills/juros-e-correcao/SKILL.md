---
name: juros-e-correcao
description: >
  Define o regime de correção monetária e juros de mora de qualquer crédito
  judicial conforme a natureza da dívida e o período (CC arts. 389 e 406 com a
  Lei 14.905/2024; ADC 58 e Tema 1191 do STF no trabalhista; EC 113/2021 e EC
  136/2025 na Fazenda Pública), redige o pedido e monta a memória de cálculo.
  Use quando o usuário pedir juros, correção monetária, atualização do débito,
  SELIC, IPCA, IPCA-E, INPC, taxa legal, consectários, termo inicial dos juros,
  cálculo de liquidação, planilha, excesso de execução ou "como pedir os juros".
metadata:
  area: nucleo
  tipo_peca: outro
  verificado_em: 2026-11-01
---
# Juros e correção monetária

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

Esta é a única fonte de taxas e índices do repositório. Nenhuma skill de área
fixa taxa própria: todas remetem para cá. Nunca escreva "1% ao mês" como regra
geral vigente (sobrevive só como taxa convencionada, regra de lei especial ou
coisa julgada expressa).

## Quando usar / quando não usar
- Usar: todo pedido condenatório em dinheiro, cumprimento de sentença, impugnação
  por excesso de execução, embargos, cálculos de liquidação, acordos com parcelas.
- Não usar para obrigações com índice e taxa pactuados válidos (aplique o contrato,
  verificando limites legais) nem para dívida ativa cobrada pela Fazenda (a regra é
  a da lei do ente credor; ver tributário-fazenda).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Natureza do crédito: cível contratual, cível extracontratual, consumo, trabalhista,
   contra a Fazenda (tributário ou não), previdenciário, alimentos, dano moral.
2. Datas: vencimento de cada parcela ou evento danoso; citação; ajuizamento
   (trabalhista); arbitramento (dano moral); trânsito em julgado; expedição do requisitório.
3. Se há índice ou taxa no contrato, na lei especial ou no título judicial (e se o
   título é expresso ou omisso quanto aos índices).
4. Ente devedor, se Fazenda: União, Estado, DF, Município, autarquia.

## Prazo e contagem
Não se aplica. Para prazos, use `prazos-processuais`.

## Estrutura da peça
Esta skill produz três blocos para inserir na peça da área: (a) o parágrafo de
fundamentação dos consectários, (b) a frase do pedido, (c) a memória de cálculo.
Roteiro completo em [estrutura](references/estrutura.md); linha do tempo de cada
regime em [quadro cronológico](references/quadro-cronologico.md).

## Requisitos e preliminares
- Juros e correção estão compreendidos no principal (CPC art. 322, §1º), mas o
  pedido expresso evita omissão e embargos de declaração.
- Taxa legal negativa vale zero (CC art. 406, §3º). A taxa é calculada pela
  metodologia da Resolução CMN 5.171/2024 e divulgada pelo Banco Central; use a
  série oficial, nunca a subtração manual "SELIC anual menos IPCA anual".
- Índice negativo de correção (deflação) não é taxa legal: a regra do §3º não o
  alcança. [VERIFICAR] o entendimento atual do STJ antes de aplicar ou afastar deflação.
- SELIC já embute correção e juros: nunca cumule SELIC com outro índice no mesmo
  período (STJ, Tema 1368; STF, Tema 1191).

## Fundamentos verificados (tabela de regimes)
| Natureza | Até 29/08/2024 (ou marco próprio) | Regime atual |
|---|---|---|
| Cível sem índice pactuado | Correção pelo índice do tribunal até o termo inicial dos juros; daí em diante só SELIC (art. 406 original; STJ Tema 1368) | Desde 30/08/2024: IPCA (CC 389, p.ú.) + taxa legal = SELIC − IPCA, piso zero (CC 406, §§1º e 3º) |
| Dano moral | Correção desde o arbitramento (Súm. 362/STJ); juros desde o evento danoso, se extracontratual (Súm. 54/STJ; CC 398), ou desde a citação, se contratual (CC 405) | Mesmos termos iniciais; IPCA + taxa legal após 30/08/2024 (STJ, REsp 2.252.259) |
| Dano material | Correção desde o efetivo prejuízo (Súm. 43/STJ) | Idem, com IPCA e taxa legal |
| Trabalhista | Fase pré-judicial: IPCA-E + juros do art. 39, caput, Lei 8.177; do ajuizamento até 29/08/2024: só SELIC (STF Tema 1191, que reafirma ADC 58/59) | Desde 30/08/2024: IPCA + (SELIC − IPCA), piso zero (TST SDI-1, E-ED-RR-713-03.2010.5.04.0029, conforme transcrito em acórdão confirmado; número da SDI-1 [VERIFICAR]) |
| Fazenda Pública (não tributário) | Até 08/12/2021: Tema 810/STF e Tema 905/STJ (índice conforme a natureza [VERIFICAR item do Tema 905]) | 09/12/2021 a 09/09/2025: SELIC única (EC 113, redação original; STF Tema 1419, julgado antes da EC 136). Desde 10/09/2025, até a expedição: [VERIFICAR] – ver alerta |
| Fazenda: requisitório expedido | — | IPCA + juros simples 2% a.a., limitado à SELIC (União: art. 3º EC 113 com redação da EC 136; Estados/DF/Municípios: ADCT art. 97, §§16 e 16-A); sem juros no período de graça (CF 100, §5º; STF Tema 1335) |
| Indébito tributário federal | SELIC desde o pagamento indevido, sem outro índice (Lei 9.250, art. 39, §4º) | Idem (CTN 165-A, LC 236/2026); EC 136: no requisitório tributário, mesmos critérios do crédito tributário |
| Indébito tributário estadual/municipal | Mesma taxa que o ente cobra em atraso (Súm. 523/STJ), limitada à SELIC (STF Temas 1062 e 1217); sem lei local: correção desde o pagamento (Súm. 162/STJ) e juros desde o trânsito (Súm. 188/STJ; CTN 167, p.ú.) | CTN 165-A (LC 236/2026, DOU 04/09/2026): indébito atualizado pelos mesmos índices do crédito tributário do ente; vigência do dispositivo [VERIFICAR] |
| Previdenciário (RGPS) | Correção INPC (Lei 8.213, art. 41-A; Tema 905/STJ, item 3.2); juros da poupança (Tema 810) desde a citação (Súm. 204/STJ) | 09/12/2021 em diante: SELIC (EC 113). Após a EC 136: ver alerta |
| Alimentos | Atualização por índice oficial (CC 1.710); prestação vencida em mora desde o vencimento (CC 397) | Sem índice no título: IPCA + taxa legal após 30/08/2024 (no período anterior, STJ aplicou SELIC: REsp 2.192.918) |

Alerta Fazenda e previdenciário: a EC 136/2025 (DOU 10/09/2025) deu nova redação
ao art. 3º da EC 113, que passou a tratar só do período posterior à expedição do
requisitório. A 2ª Turma do STJ (REsp 2.170.124, j. 08/09/2026) entendeu que, após
a EC 136 e até a expedição, voltam os critérios do Tema 905/STJ. É orientação de
Turma, ainda não consolidada: [VERIFICAR] a posição atual do STJ, do STF e do
tribunal local antes de pedir. Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
Frases prontas por regime (adapte datas e termos) em
[estrutura](references/estrutura.md), seção 3. Exemplo cível pós-Lei 14.905:
"Requer a condenação ao pagamento de R$ [valor], corrigido pelo IPCA desde [data
do prejuízo/vencimento] e acrescido de juros de mora pela taxa legal do art. 406,
§1º, do Código Civil (SELIC deduzido o IPCA, considerada zero se negativa), desde
[citação/evento danoso/vencimento], até o efetivo pagamento."

## Checklist pré-protocolo
- [ ] Natureza do crédito identificada e regime da tabela escolhido.
- [ ] Período fatiado nos marcos: 09/12/2021, 30/08/2024, 10/09/2025, expedição do requisitório.
- [ ] Termo inicial da correção e dos juros justificado por dispositivo ou súmula.
- [ ] Nenhuma cumulação de SELIC com outro índice no mesmo intervalo.
- [ ] Taxa legal extraída da série oficial do Banco Central; meses negativos zerados.
- [ ] Título judicial conferido: índice expresso, omisso ou "critérios legais" (Tema 1191, item II; Tema 1361).
- [ ] Memória de cálculo anexa, com fonte de cada índice e data de consulta.
- [ ] Toda menção marcada [VERIFICAR] resolvida ou mantida visível para o revisor.

## Erros a evitar
- Pedir "juros de 1% ao mês e correção pelo INPC" em dívida civil sem base contratual.
- Aplicar IPCA + taxa legal a períodos anteriores a 30/08/2024 (a lei não retroage).
- Usar SELIC "desde 09/12/2021" contra a Fazenda sem examinar o efeito da EC 136/2025.
- Aplicar Súmula 188/STJ a tributo federal, em que a SELIC corre desde o pagamento, ou
  ignorar o CTN 165-A (índices do crédito tributário do ente).
- Contar juros trabalhistas pela regra antiga de 1% ao mês do art. 39, §1º, Lei 8.177.
- Esquecer que no período de graça do precatório não correm juros.
- Citar o número do Tema 905/STJ ou da ADC 58 como se a ementa tivesse sido lida:
  ambos não foram localizados diretamente na base de verificação; use os
  precedentes confirmados que os aplicam.

## Integração com o núcleo
- `verificacao-de-citacoes`: antes de acrescentar qualquer precedente sobre índices.
- `fidelidade-factual`: datas de citação, ajuizamento e vencimentos vêm dos autos, nunca de suposição.
- `prazos-processuais`: prazo da impugnação ao cálculo (CPC 525; CLT 879, §2º).
- `estilo-forense`: pedido em alínea própria para os consectários.

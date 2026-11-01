---
name: trabalhista-agravo-de-peticao
description: >
  Redige agravo de petição contra decisões do juiz na execução trabalhista
  (CLT art. 897 "a"), com a delimitação justificada das matérias e dos valores
  impugnados exigida pelo §1º, sob pena de não recebimento. Use quando o usuário
  pedir agravo de petição, AP, recorrer de decisão em execução trabalhista, da
  sentença de embargos à execução ou da impugnação aos cálculos, de penhora, de
  desconsideração da personalidade jurídica na execução, ou contraminuta de AP.
metadata:
  area: trabalhista
  tipo_peca: agravo
  verificado_em: 2026-11-01
---
# Agravo de petição

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: sentença de embargos à execução ou de impugnação à liquidação (art. 884); decisões terminativas ou com conteúdo decisório relevante na execução; decisão que acolhe ou rejeita IDPJ na fase de execução, independentemente de garantia (art. 855-A §1º II).
- Não usar: decisões na fase de conhecimento (RO); despacho que denega o próprio AP (use `trabalhista-agravo-de-instrumento`).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
- Decisão agravada, data da intimação.
- Cálculos homologados e cálculo próprio da parte, por rubrica.
- Garantia do juízo (depósito, penhora, seguro) e valor atualizado.
- Pontos já impugnados antes (art. 879 §2º): matéria não impugnada no prazo pode estar preclusa.

## Prazo e contagem
- 8 dias úteis (art. 897 caput; art. 775).

## Estrutura da peça
Interposição ao juízo da execução; razões ao TRT: admissibilidade (tempestividade, garantia, delimitação), matérias delimitadas uma a uma com o valor controvertido e o incontroverso, pedido. Roteiro em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Delimitação** (art. 897 §1º): indicar, justificadamente, as matérias e os valores impugnados. A parte não impugnada pode ser executada de imediato. A falta de delimitação leva ao não recebimento. O prosseguimento da execução quanto ao não impugnado não fere direito líquido e certo (Súmula 416 do TST).
- **Preparo**: execução garantida dispensa novo depósito, salvo elevação do débito, quando se exige complementação da garantia (Súmula 128 II do TST). Custas da execução: tabela do art. 789-A, a cargo do executado e pagas ao final (não são pressuposto do AP).
- **Preclusão**: o que não foi impugnado no prazo do art. 879 §2º, ou nos embargos (art. 884 §3º), não se rediscute no AP.
- **Recurso posterior**: RR contra acórdão em AP só por ofensa direta à CF (Súmula 266; art. 896 §2º). Já preparar a tese constitucional se houver.

## Fundamentos verificados
CLT arts. 855-A, 879 §2º, 884, 896 §2º, 897 "a" e §§1º e 3º; Súmulas 128, 266, 416 do TST. Detalhes em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Recebimento, conhecimento e provimento, com a reforma de cada matéria e o valor correto.
- Liberação do valor incontroverso ao exequente, se for o agravante (§1º), ou reconhecimento de que só o delimitado está suspenso.
- Juros e correção: se for matéria do agravo, fundamentar com a skill `juros-e-correcao` (marcos da ADC 58 e da Lei 14.905/2024), sem taxa escrita aqui.

## Checklist pré-protocolo
- [ ] Cada matéria com: valor homologado, valor correto, diferença.
- [ ] Total controvertido e total incontroverso indicados.
- [ ] Matérias foram impugnadas na fase própria (sem preclusão).
- [ ] Juízo garantido (ou hipótese de dispensa, como IDPJ — art. 855-A §1º II).
- [ ] Planilha anexa.

## Erros a evitar
- AP genérico ("os cálculos estão errados").
- Trazer matéria nova não impugnada antes.
- Rediscutir o mérito da sentença transitada (art. 879 §1º).
- Esquecer a complementação da garantia quando o débito subiu.

## Integração com o núcleo
`juros-e-correcao`, `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

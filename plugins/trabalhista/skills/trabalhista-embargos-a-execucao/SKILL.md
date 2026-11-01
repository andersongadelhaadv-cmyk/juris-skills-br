---
name: trabalhista-embargos-a-execucao
description: >
  Redige embargos à execução trabalhista após a garantia do juízo ou a penhora
  (CLT art. 884), com as matérias do §1º, a impugnação da sentença de liquidação
  (§3º) e a inexigibilidade do título (§5º). Use quando o usuário pedir embargos à
  execução trabalhista, embargos do devedor na Justiça do Trabalho, embargos à
  penhora, defesa do executado após garantir o juízo, ou impugnação do exequente
  aos embargos.
metadata:
  area: trabalhista
  tipo_peca: embargos-execucao
  verificado_em: 2026-11-01
---
# Embargos à execução trabalhista

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: executado (empregador, sócio incluído, responsável subsidiário) após garantir a execução ou sofrer penhora suficiente.
- Também: impugnação do exequente à sentença de liquidação, no mesmo prazo (art. 884 caput e §3º).
- Não usar: impugnação aos cálculos antes da homologação (use `trabalhista-impugnacao-de-calculos`); terceiro que teve bem penhorado (embargos de terceiro, peça diversa); defesa sem garantia, salvo entidades filantrópicas e seus diretores (art. 884 §6º).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
- Título executivo (sentença/acórdão/acordo) e certidão de trânsito.
- Decisão homologatória dos cálculos e a conta homologada.
- Data e forma da garantia (depósito, seguro garantia, bens) e data da intimação da penhora.
- Pagamentos já feitos, acordos, quitações e datas.
- Se houve impugnação aos cálculos no prazo do art. 879 §2º.

## Prazo e contagem
- 5 dias, contados da garantia ou da penhora (art. 884 caput), em dias úteis (art. 775).
- Fazenda Pública: 30 dias (Lei 9.494/1997, art. 1º-B).
- Garantia: depósito atualizado, seguro garantia judicial ou bens à penhora pela ordem do CPC art. 835 (CLT art. 882), após citação para pagar em 48 horas (art. 880).

## Estrutura da peça
Endereçamento ao juízo da execução; tempestividade e garantia; matérias de embargos; impugnação à liquidação (se preservada); pedidos. Roteiro em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Matérias** (art. 884 §1º): cumprimento da decisão ou do acordo, quitação, prescrição da dívida. Na prática também se discutem excesso de execução, nulidade de citação e de penhora, ilegitimidade e prescrição intercorrente (art. 11-A, prazo de 2 anos) — sempre ligados à execução, sem rediscutir o mérito (art. 879 §1º).
- **Sentença de liquidação**: só pode ser impugnada nos embargos se a matéria foi impugnada no prazo do art. 879 §2º; do contrário, preclusão.
- **Título inexigível** (§5º): fundado em lei declarada inconstitucional pelo STF ou em interpretação incompatível com a CF.
- **Penhora em dinheiro**: não viola direito líquido e certo, por ser prioritária (Súmula 417 I do TST).
- Julgamento conjunto dos embargos e das impugnações dos credores trabalhista e previdenciário (art. 884 §4º).

## Fundamentos verificados
CLT arts. 11-A, 775, 789-A, 879, 880, 882, 883, 884; Lei 9.494/1997 art. 1º-B; CPC art. 835; Súmula 417 do TST. Detalhes em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Recebimento dos embargos com efeito sobre a parte controvertida; acolhimento das matérias; redução da execução ao valor correto, com planilha.
- Liberação do excesso de garantia, se for o caso.
- Atualização e juros: se forem objeto, fundamentar com `juros-e-correcao` (marcos da ADC 58 e da Lei 14.905/2024), sem escrever taxa.

## Checklist pré-protocolo
- [ ] Juízo garantido no valor integral atualizado (ou hipótese de dispensa).
- [ ] Prazo de 5 dias (ou 30, Fazenda) conferido a partir da garantia/penhora.
- [ ] Cada matéria com prova documental (recibos, termo de acordo, depósitos).
- [ ] Planilha do valor que se entende devido.
- [ ] Matérias de liquidação estavam impugnadas no prazo do art. 879 §2º.
- [ ] Juros e correção remetidos ao núcleo.

## Erros a evitar
- Embargar sem garantia integral.
- Contar o prazo da citação em vez da garantia/penhora.
- Reabrir discussão de mérito decidida no título.
- Alegar excesso sem demonstrar o valor correto.

## Integração com o núcleo
`juros-e-correcao`, `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

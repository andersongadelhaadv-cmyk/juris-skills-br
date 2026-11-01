---
name: trabalhista-impugnacao-de-calculos
description: >
  Redige impugnação fundamentada aos cálculos de liquidação trabalhista no prazo
  comum de 8 dias (CLT art. 879 §2º), com indicação de itens e valores sob pena de
  preclusão, e com a atualização do crédito aplicada pela skill juros-e-correcao
  (ADC 58 e Lei 14.905/2024). Use quando o usuário pedir impugnação aos cálculos,
  manifestação sobre conta de liquidação, contestar cálculos do perito ou da parte
  contrária, impugnar liquidação trabalhista ou apresentar cálculos de liquidação.
metadata:
  area: trabalhista
  tipo_peca: impugnacao
  verificado_em: 2026-11-01
---
# Impugnação aos cálculos de liquidação

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: após a intimação para se manifestar sobre a conta (da parte, do perito ou da contadoria), antes da homologação.
- Também para apresentar os cálculos de liquidação quando o juízo intimar as partes para isso (art. 879 §1º-B).
- Não usar: depois da homologação (a via passa a ser `trabalhista-embargos-a-execucao`, que só aceita o que foi impugnado aqui).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
- Título executivo integral (sentença, acórdãos, ED) e parâmetros de liquidação fixados.
- Conta impugnada (PDF e, se possível, arquivo do sistema de cálculo).
- Contracheques, cartões de ponto, fichas financeiras, data de ajuizamento.
- Cálculo próprio ou, ao menos, os itens que se acha errados.

## Prazo e contagem
- 8 dias, prazo comum, contados da intimação (art. 879 §2º), em dias úteis (art. 775). Não impugnar ou impugnar sem indicar itens e valores gera preclusão.
- União: 10 dias para manifestação sobre as contribuições (art. 879 §3º).

## Estrutura da peça
Identificação; tempestividade; impugnações por item (rubrica, critério da conta, critério do título, valor correto, diferença); atualização e juros; contribuições e IR; quadro final; pedido. Roteiro em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Fundamentação com itens e valores** (art. 879 §2º): cada discordância precisa da rubrica e do número.
- **Fidelidade ao título** (art. 879 §1º): não se modifica nem inova a sentença.
- **Contribuições previdenciárias** integram a liquidação (art. 879 §1º-A); natureza das parcelas conforme o título (art. 832 §3º).
- **Atualização e juros**: o §7º do art. 879 (TR) tem anotação da ADC 58. Os critérios vigentes — fase pré-judicial, fase judicial até 29/08/2024 e período posterior à Lei 14.905/2024 — devem ser aplicados exclusivamente pela skill `juros-e-correcao`, respeitando o que o título fixou e a modulação do STF. Não escrever índice ou taxa nesta peça sem o núcleo.
- Cálculos complexos: o juiz pode nomear perito (art. 879 §6º).

## Fundamentos verificados
CLT arts. 775, 832 §3º, 879 §§1º a 7º, 883; Lei 8.177/1991 art. 39; Lei 14.905/2024; acórdãos do TST que aplicam a ADC 58 (ver fontes). Detalhes em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Acolhimento da impugnação, com retificação da conta nos itens indicados.
- Homologação do cálculo apresentado pela parte ou remessa ao perito/contadoria com quesitos.

## Checklist pré-protocolo
- [ ] Prazo de 8 dias úteis conferido.
- [ ] Cada item: rubrica, critério usado, critério do título, valor correto, diferença.
- [ ] Quadro-resumo com total impugnado e total incontroverso.
- [ ] Período prescrito excluído, se o título assim decidiu.
- [ ] Divisor, base de cálculo, adicionais e reflexos conferidos com o título.
- [ ] Contribuições e IR com a natureza das parcelas do título.
- [ ] Correção e juros aplicados pelo núcleo `juros-e-correcao`, com os marcos de 2024.

## Erros a evitar
- Impugnação genérica ("discorda-se dos cálculos").
- Pedir critério que contraria o título (inovação).
- Aplicar juros simples fixos mensais ou a TR como regra: critérios superados para créditos trabalhistas; sempre usar o núcleo.
- Deixar de impugnar agora e tentar nos embargos (preclusão).

## Integração com o núcleo
`juros-e-correcao` (obrigatória nesta peça), `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

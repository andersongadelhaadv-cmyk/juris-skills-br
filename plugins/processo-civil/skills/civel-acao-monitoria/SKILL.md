---
name: civel-acao-monitoria
description: >
  Redige ação monitória (CPC arts. 700 a 702), fundada em prova escrita sem
  eficácia de título executivo, e também embargos monitórios do réu. Use quando
  o usuário pedir ação monitória, cobrança de cheque prescrito, nota promissória
  prescrita, contrato sem testemunhas, "mandado de pagamento", embargos à
  monitória ou defesa em monitória.
metadata:
  area: processo-civil
  tipo_peca: inicial
  verificado_em: 2026-11-01
---
# Ação monitória (e embargos monitórios)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: credor com prova escrita sem força executiva que demonstre direito a pagamento, entrega de coisa ou obrigação de fazer/não fazer contra devedor capaz (art. 700). Cabe contra a Fazenda (§6º).
- Usar para os embargos do réu (art. 702).
- Não usar: há título executivo (`civel-execucao-titulo-extrajudicial`); juizado especial (procedimento monitório não previsto na Lei 9.099); quando a prova escrita é frágil — o juiz pode mandar adaptar ao procedimento comum (art. 700, §5º).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
- Documento escrito (cheque, nota, contrato, e-mails, confissão) e datas.
- Valor devido com memória de cálculo; ou valor atual da coisa; ou proveito econômico.
- Dados do devedor e da sua capacidade.
- Para embargos: valor que o réu entende devido e demonstrativo, se alegar excesso.

## Prazo e contagem
- Prescrição: cheque sem força executiva — 5 anos do dia seguinte à emissão (Súmula 503 do STJ). Demais títulos: conferir em `prazos-processuais`.
- Réu: 15 dias úteis para pagar (com honorários de 5%) ou embargar (arts. 701 e 702).
- Autor responde aos embargos em 15 dias (art. 702, §5º).

## Estrutura da peça
Inicial: endereçamento → partes → prova escrita → crédito e memória → fundamentos → pedido de expedição de mandado → valor da causa → pedidos. Embargos: tempestividade → matérias de defesa → excesso com valor → reconvenção (se houver) → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Explicitar, conforme o caso, a importância com memória de cálculo, o valor atual da coisa ou o proveito econômico (art. 700, §2º); valor da causa igual a isso (§3º); sem isso, indeferimento (§4º).
- Prova escrita pode ser prova oral documentada em produção antecipada (§1º).
- Embargos independem de garantia, nos próprios autos; matéria de procedimento comum (art. 702, §1º); excesso exige valor e demonstrativo (§§2º e 3º); suspendem a eficácia do mandado (§4º).
- Reconvenção admitida; vedada reconvenção à reconvenção (§6º).

## Fundamentos verificados
CPC arts. 700 a 702, 916 (por remissão do art. 701, §5º); Súmulas 247, 292, 299, 384, 503 e 531 do STJ. Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Inicial: expedição de mandado de pagamento (entrega/fazer) com prazo de 15 dias e honorários de 5% (art. 701); constituição do título se não houver pagamento nem embargos (§2º).
- Correção e juros conforme `juros-e-correcao` (termo inicial próprio de cada título).
- Embargos: suspensão da eficácia do mandado; improcedência ou redução; multa por monitória indevida e de má-fé (art. 702, §10).

## Checklist pré-protocolo
- [ ] Documento escrito idôneo e sem força executiva.
- [ ] Memória de cálculo anexada; valor da causa coincide (art. 700, §3º).
- [ ] Prescrição conferida.
- [ ] Devedor capaz identificado.
- [ ] Embargos: excesso com valor e demonstrativo; reconvenção decidida.

## Erros a evitar
- Monitória com título executivo válido (falta de interesse; via própria é a execução).
- Valor da causa diferente do crédito explicitado.
- Embargos alegando excesso sem demonstrativo (rejeição do tema).
- Ignorar que o réu pode parcelar (art. 701, §5º, remete ao art. 916).
- Juros com taxa fixa: aplicar o núcleo.

## Integração com o núcleo
- `juros-e-correcao` para a memória de cálculo.
- `prazos-processuais` para prescrição e prazos de 15 dias.
- `verificacao-de-citacoes` para precedentes sobre termo inicial de juros por espécie de título.
- `fidelidade-factual` e `estilo-forense` na revisão.

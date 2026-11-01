---
name: civel-embargos-a-execucao
description: >
  Redige embargos à execução de título extrajudicial (CPC arts. 914 a 920), com
  as matérias do art. 917, excesso de execução com valor e demonstrativo, pedido
  de efeito suspensivo (art. 919, §1º) e alternativa do parcelamento do art. 916.
  Use quando o usuário pedir embargos à execução, embargos do devedor, defesa na
  execução de título extrajudicial, alegar nulidade do título, excesso ou
  impenhorabilidade.
metadata:
  area: processo-civil
  tipo_peca: embargos-execucao
  verificado_em: 2026-11-01
---
# Embargos à execução (título extrajudicial)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: executado citado em execução de título extrajudicial (arts. 784 e ss.).
- Não usar: cumprimento de sentença (`civel-impugnacao-ao-cumprimento`); execução fiscal (Lei 6.830 — skill da área fazendária); matéria de ordem pública com prova pronta, quando se quer evitar custas e autuação apartada (`civel-excecao-de-pre-executividade`); juizado especial (embargos em audiência — Lei 9.099, art. 53, §1º).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
- Petição inicial da execução, título, demonstrativo e mandado de citação (data de juntada).
- Versão do cliente sobre a dívida: pagamentos, contrato subjacente, encargos, garantias.
- Bens penhorados e sua natureza (impenhorabilidade — art. 833).
- Interesse em parcelar (art. 916) — opção que implica renúncia aos embargos.

## Prazo e contagem
- 15 dias úteis, contados na forma do art. 231 (art. 915); independe de penhora (art. 914).
- Vários executados: prazo individual a partir da juntada de cada citação, salvo cônjuges/companheiros (do último) (art. 915, §1º).
- Sem prazo em dobro para litisconsortes (art. 915, §3º).
- Parcelamento do art. 916 deve ser requerido no mesmo prazo. Use `prazos-processuais`.

## Estrutura da peça
Petição inicial distribuída por dependência → qualificação → tempestividade → síntese da execução → matérias do art. 917 → excesso com valor e planilha → efeito suspensivo → pedidos → valor da causa → provas → cópias relevantes. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Natureza de ação: requisitos de inicial (art. 319), distribuição por dependência, autos apartados, cópias das peças relevantes (art. 914, §1º).
- Matérias (art. 917): inexequibilidade/inexigibilidade; penhora incorreta ou avaliação errônea; excesso ou cumulação indevida; retenção por benfeitorias; incompetência; qualquer defesa de processo de conhecimento (VI).
- Excesso: valor correto e demonstrativo na inicial (§3º), sob pena de rejeição liminar ou desconsideração do tema (§4º).
- Efeito suspensivo: requisitos da tutela provisória + garantia por penhora, depósito ou caução (art. 919, §1º).
- Rejeição liminar: intempestivos, inépcia, manifestamente protelatórios (art. 918).

## Fundamentos verificados
CPC arts. 231, 784, 798, 803, 827, 833, 914 a 920; Súmula 375 do STJ (quando houver fraude alegada). Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Efeito suspensivo, comprovada a garantia.
- Intimação do exequente para responder em 15 dias (art. 920, I).
- Procedência para extinguir a execução, declarar nulidade (art. 803) ou reduzir o valor.
- Levantamento de penhora sobre bem impenhorável.
- Honorários e custas; valor da causa (proveito econômico pretendido).

## Checklist pré-protocolo
- [ ] Prazo de 15 dias úteis a partir da juntada do mandado/AR do executado (sem dobra).
- [ ] Distribuição por dependência; cópias do título, da inicial executiva e da citação.
- [ ] Cada tese enquadrada em inciso do art. 917.
- [ ] Excesso com valor e planilha (via `juros-e-correcao`).
- [ ] Garantia descrita, se pedido efeito suspensivo.
- [ ] Valor da causa e custas.
- [ ] Decisão consciente sobre o parcelamento do art. 916 (incompatível com os embargos).

## Erros a evitar
- Contar prazo em dobro por haver litisconsortes.
- Alegar excesso sem valor e demonstrativo.
- Pedir efeito suspensivo sem garantia.
- Embargos genéricos e protelatórios: rejeição e multa por ato atentatório (art. 918, p.ú.; art. 774).
- Esquecer que, rejeitados os embargos, os honorários podem subir até 20% (art. 827, §2º).

## Integração com o núcleo
- `juros-e-correcao` para o demonstrativo do excesso.
- `prazos-processuais` para a contagem individual do art. 915.
- `verificacao-de-citacoes` para precedentes sobre título e encargos.
- `fidelidade-factual` e `estilo-forense` na revisão.

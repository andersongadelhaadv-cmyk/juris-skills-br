---
name: reg-recurso-multa-agencia
description: >
  Redige recurso administrativo contra decisão de agência reguladora que
  aplicou multa ou outra sanção, com pedido de reconsideração, efeito
  suspensivo e reforma, com base nos arts. 56 a 66 da Lei 9.784/1999, na Lei
  13.848/2019, na Súmula Vinculante 21 do STF e na Súmula 373 do STJ. Use quando
  o usuário pedir recurso contra multa da ANEEL, ANATEL, ANP, ANTT, ANVISA,
  ANS ou outra agência, recurso à diretoria colegiada, pedido de
  efeito suspensivo de sanção regulatória, recurso exigindo depósito prévio ou
  pedido de revisão de sanção por fato novo.
metadata:
  area: regulatorio
  tipo_peca: recurso
  verificado_em: 2026-11-25
---
# Recurso contra multa de agência reguladora

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: decisão de primeira instância (superintendência, gerência, diretor) que aplicou multa, advertência, suspensão ou outra sanção regulatória; recurso à diretoria colegiada; pedido de revisão de processo sancionador por fato novo (art. 65 da Lei 9.784/1999).
- Não usar:
  - Ainda sem decisão (fase de defesa): `reg-defesa-processo-sancionador-agencia` ou, na ANS, `reg-defesa-sancionador-ans`.
  - Esfera administrativa esgotada e busca de anulação judicial ou liminar: `adm-mandado-de-seguranca`.
  - Multa em licitação/contrato: `adm-recurso-em-licitacao` ou `adm-defesa-em-processo-sancionador-licitacao`.
  - Multa tributária: `trib-defesa-administrativa-e-carf`.
  - Multa da ANAC (aviação civil): `aero-recurso-multa-anac`.

## Entradas mínimas (perguntar o que faltar; nunca supor fatos)
1. Decisão recorrida integral, com a data da ciência ou da divulgação oficial.
2. Defesa e alegações finais apresentadas (o recurso não deve inovar sem razão; se houver fato novo, documentá-lo).
3. Norma da agência sobre recurso: prazo, autoridade de destino, número de instâncias, efeito suspensivo, desconto por renúncia ao recurso [VERIFICAR na norma do caso].
4. Guia da multa e vencimento; se houve exigência de depósito, caução ou pagamento para recorrer.
5. Risco concreto de dano com a execução imediata (inscrição no CADIN, dívida ativa, impedimento de contratar, suspensão de atividade).

## Prazo e contagem
- Regra geral: 10 dias da ciência ou da divulgação oficial, salvo lei específica (Lei 9.784/1999, art. 59); contagem em dias contínuos, excluído o início e incluído o vencimento (art. 66, § 2º). A norma setorial pode fixar prazo diverso — conferir sempre.
- Reconsideração: o recurso vai à autoridade que decidiu, que tem 5 dias para reconsiderar antes de encaminhar à superior (art. 56, § 1º).
- Prazo para julgar, sem prazo legal específico: 30 dias do recebimento dos autos (art. 59, § 1º).
- Máximo de três instâncias, salvo lei diversa (art. 57).
- Recurso fora do prazo não é conhecido (art. 63, I). Conferência: `prazos-processuais`.

## Estrutura da peça
Petição de interposição à autoridade recorrida (com pedido de reconsideração e de efeito suspensivo) → razões à instância superior: tempestividade e cabimento → síntese da decisão → nulidades (motivação, cerceamento, prescrição) → reforma no mérito → dosimetria → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Cabimento**: legalidade e mérito (art. 56, caput). Legitimados no art. 58.
- **Sem caução**: salvo exigência legal, o recurso independe de caução (art. 56, § 2º); exigir depósito ou arrolamento prévio é inconstitucional (Súmula Vinculante 21/STF) e ilegítimo (Súmula 373/STJ).
- **Efeito suspensivo**: regra é não ter, salvo lei; pode ser concedido havendo justo receio de prejuízo de difícil ou incerta reparação (art. 61). Na ANS, a lei dá efeito suspensivo, salvo risco à saúde dos consumidores (Lei 9.961/2000, art. 10, § 3º).
- **Reformatio in pejus**: se a decisão puder agravar a situação do recorrente, ele deve ser cientificado para alegar antes (art. 64, parágrafo único). Na revisão do art. 65 não há agravamento.
- **Motivação**: decisão que impõe sanção ou decide recurso exige motivação explícita, clara e congruente (art. 50, II e V, e § 1º; Lei 13.848/2019, art. 5º).
- **Prescrição intercorrente**: confira o tempo em que o processo ficou parado entre a defesa e a decisão (Lei 9.873/1999, art. 1º, § 1º).

## Fundamentos verificados
- Lei 9.784/1999, arts. 50, 56 a 59, 61, 63 a 66.
- Lei 13.848/2019, arts. 4º, 5º e 7º (decisão colegiada e reexame da delegação).
- Lei 9.961/2000, art. 10, § 2º e § 3º (ANS).
- Súmula Vinculante 21/STF; Súmula 373/STJ.
- LINDB, arts. 20 e 22.
- STJ: recurso administrativo não afasta juros de mora sobre multa da ANS (AREsp 1.574.873).
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Reconsideração pela autoridade recorrida (art. 56, § 1º).
- Efeito suspensivo, com demonstração do dano de difícil reparação (art. 61, parágrafo único).
- Nulidade da decisão (falta de motivação, prova recusada sem fundamento, prescrição).
- Reforma para afastar a sanção; subsidiariamente, reduzir a multa ou convertê-la em advertência.
- Sustentação oral ou memoriais na sessão do colegiado, se o regimento permitir.
- Ciência prévia em caso de possível agravamento (art. 64, parágrafo único).

## Checklist pré-protocolo
- [ ] Prazo da norma setorial conferido; na falta, 10 dias contínuos
- [ ] Interposição endereçada à autoridade que decidiu, com pedido de reconsideração
- [ ] Efeito suspensivo pedido com fatos concretos de dano
- [ ] Cada fundamento da decisão rebatido (nada sem impugnação)
- [ ] Exigência de depósito, se houver, impugnada com SV 21 e Súmula 373
- [ ] Custo de recorrer sem pagar explicado ao cliente (desconto perdido; encargos pelo núcleo)
- [ ] Prescrição intercorrente conferida

## Erros a evitar
- Endereçar direto à instância superior e perder a etapa de reconsideração.
- Repetir a defesa sem atacar os fundamentos da decisão.
- Supor efeito suspensivo automático: em regra não há, salvo lei ou concessão.
- Perder o desconto por pagamento antecipado sem o cliente decidir conscientemente.
- Protocolar perante órgão incompetente: não se conhece, embora a autoridade deva indicar a competente e devolver o prazo (art. 63, § 1º).

## Integração com o núcleo
`prazos-processuais`, `juros-e-correcao` (encargos da multa durante o recurso), `verificacao-de-citacoes`, `estilo-forense`.

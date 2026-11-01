---
name: consumidor-negativacao-indevida
description: >
  Redige ação declaratória de inexistência de débito cumulada com cancelamento
  de inscrição em cadastro de inadimplentes e indenização por dano moral, com
  base no art. 43 do CDC e nas Súmulas 359, 385, 323, 404 e 548 do STJ. Use
  quando o usuário pedir ação por nome sujo indevidamente, negativação no
  Serasa/SPC/Boa Vista sem dívida, inscrição sem notificação prévia, manutenção
  do nome após pagamento, dívida fraudada em nome do cliente ou limpeza de nome
  com tutela de urgência.
metadata:
  area: consumidor
  tipo_peca: inicial
  verificado_em: 2026-11-01
---
# Negativação indevida

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: (a) débito inexistente, já pago ou fraudado; (b) inscrição sem notificação prévia; (c) manutenção após quitação (mais de 5 dias úteis); (d) registro além de 5 anos ou após prescrição da cobrança.
- Não usar: dívida reconhecida e só se discute o valor (revisional: `consumidor-contratos-bancarios-revisional`); superendividamento (`consumidor-superendividamento`).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Extrato atualizado de **todos** os cadastros (Serasa, SPC, Boa Vista, SCR do Banco Central) com datas de inclusão, credor, valor, contrato.
2. Para cada anotação: é legítima? Está sendo discutida em juízo? (decisivo para a Súmula 385).
3. Relação com o credor: nunca contratou / contratou e pagou / contratou e discute.
4. Comprovantes de pagamento e data da quitação; data da baixa.
5. Recebeu comunicação prévia? Por qual meio e em qual endereço?
6. Prejuízos concretos (crédito negado, compra recusada, constrangimento) com prova.
7. Boletim de ocorrência, se houve fraude.

## Prazo e contagem
- Prescrição da pretensão indenizatória: [VERIFICAR: há leituras distintas — art. 27 do CDC, art. 206 § 3º, V, ou art. 205 do CC — confirme o entendimento atual do STJ para a hipótese concreta via `verificacao-de-citacoes`]. Enquanto a inscrição persiste, registre a data de inclusão e a de exclusão.
- Prazos processuais em dias úteis: `prazos-processuais`.

## Estrutura da peça
Fatos → relação de consumo (ou consumidor equiparado, art. 17/29) → inexistência/inexigibilidade do débito → ilicitude da inscrição (tipo a/b/c/d) → dano moral e Súmula 385 → tutela de urgência para exclusão → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Polo passivo: credor que pediu a inscrição (débito indevido, falta de baixa) e/ou mantenedor do cadastro (falta de notificação prévia — Súmula 359).
- Fraude de terceiro: credor responde por fortuito interno; consumidor é equiparado (art. 17).
- Prova negativa do débito: pedir inversão do ônus e exibição do contrato/gravação pelo credor.

## Fundamentos verificados
- CDC art. 43 §§ 1º, 2º, 3º, 5º; arts. 14, 17, 6º VIII.
- Súmula 359/STJ (notificação pelo mantenedor), Súmula 404/STJ (AR dispensável), Súmula 385/STJ (inscrição preexistente legítima afasta dano moral), Súmula 323/STJ (limite de 5 anos), Súmula 548/STJ (baixa em 5 dias úteis após pagamento), Súmula 550/STJ (escore de crédito).
- Súmula 385 é flexibilizada quando a anotação anterior está sub judice (AREsp 2.777.211).
- Notificação exclusivamente por e-mail não basta (REsp 2.069.520).
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Tutela de urgência (CPC 300) para exclusão/suspensão da anotação, com ofício aos cadastros e multa diária.
- Declaração de inexistência/inexigibilidade do débito.
- Cancelamento definitivo da inscrição.
- Dano moral (valor fundamentado — método bifásico); juros/correção pelo núcleo `juros-e-correcao`.
- Inversão do ônus da prova; exibição do contrato e da prova da notificação.
- Repetição em dobro se houve pagamento indevido (`consumidor-repeticao-em-dobro`).

## Checklist pré-protocolo
- [ ] Extrato de todos os bureaus juntado, com data de emissão recente
- [ ] Cada anotação classificada: indevida / legítima / sub judice
- [ ] Súmula 385 enfrentada expressamente (ou demonstrada sua inaplicabilidade)
- [ ] Réu correto conforme o vício (credor x mantenedor)
- [ ] Comprovante de quitação e cálculo dos 5 dias úteis (se caso de baixa tardia)
- [ ] Pedido de tutela com prazo e multa
- [ ] Prescrição verificada
- [ ] Juros/correção remetidos ao núcleo

## Erros a evitar
- Omitir outras anotações e ser surpreendido pela Súmula 385 na contestação.
- Processar o credor por falta de notificação prévia (a obrigação é do mantenedor — Súmula 359).
- Alegar ausência de AR como ilícito (Súmula 404 a dispensa); a discussão é sobre envio ao endereço correto.
- Pedir dano moral "presumido" sem esclarecer que a inscrição é a única ou que as demais são indevidas/discutidas.
- Confundir o limite de 5 anos do cadastro com a prescrição da dívida (Súmula 323 e art. 43 §§ 1º e 5º).

## Integração com o núcleo
`juros-e-correcao`, `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

---
name: saude-reembolso-plano-de-saude
description: >
  Redige ação de cobrança de reembolso de despesas médico-hospitalares contra
  operadora de plano de saúde, com base no art. 12, VI, da Lei 9.656/1998, na
  orientação do STJ fixada no EAREsp 1.459.849/ES (reembolso fora da rede só em
  hipóteses excepcionais) e no Tema 1375/STJ, afetado e pendente. Use quando o
  usuário pedir reembolso de consulta, cirurgia, exame, internação ou terapia
  paga do próprio bolso, atendimento de urgência em hospital não credenciado,
  rede credenciada inexistente ou insuficiente, reembolso pago a menor pela
  tabela, demora no reembolso ou reembolso integral contra o plano.
metadata:
  area: saude
  tipo_peca: inicial
  verificado_em: 2026-11-25
---
# Reembolso de despesas médicas pelo plano de saúde

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: o beneficiário **já pagou** e quer o dinheiro de volta, total ou parcialmente: (a) urgência/emergência fora da rede; (b) rede credenciada inexistente ou insuficiente no local; (c) plano com livre escolha contratual, reembolsado a menor; (d) reembolso devido e não pago no prazo de 30 dias; (e) gasto feito porque a operadora negou cobertura que era devida.
- Não usar: tratamento ainda a realizar, com negativa e urgência — a peça é tutela de obrigação de fazer (`consumidor-plano-de-saude`); cancelamento do contrato (`saude-rescisao-unilateral-plano-de-saude`); primeira cobrança extrajudicial (`saude-notificacao-extrajudicial-plano-de-saude`); erro médico do profissional ou hospital (`saude-indenizacao-erro-medico`, `saude-responsabilidade-civil-hospitalar`); devolução de mensalidade ou reajuste pagos a mais (`consumidor-repeticao-em-dobro`).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Contrato: tipo (individual, coletivo por adesão/empresarial, autogestão), segmentação, área geográfica, cláusula de reembolso/livre escolha e **tabela de reembolso** (pedir à operadora se não tiver).
2. Relatório médico: diagnóstico, data, caráter de urgência/emergência (com o porquê) ou justificativa técnica da escolha do prestador.
3. Prova sobre a rede: a operadora indicou prestador apto? Em que prazo? Havia credenciado na especialidade e no município? Protocolos de pedido de indicação.
4. Notas fiscais, recibos, comprovantes de pagamento (quem pagou e quando).
5. Pedido de reembolso feito: data, documentos entregues, resposta (negativa, valor pago, silêncio).
6. Houve negativa prévia de cobertura que levou o beneficiário a pagar? Juntar.

## Prazo e contagem
- Prescrição: reembolso por inadimplemento contratual da operadora segue o prazo decenal do art. 205 do CC (REsp 1.992.301, STJ, julg. 20/10/2025, que afasta o Tema 610, próprio do enriquecimento sem causa). Registre a data de cada pagamento e da negativa.
- Prazo legal de pagamento do reembolso: até 30 dias após a entrega da documentação adequada (art. 12, VI). O atraso fixa o termo da mora; taxa de juros e índice de correção: `juros-e-correcao`.
- Prazos processuais: `prazos-processuais`.

## Estrutura da peça
Fatos → contrato e tabela → hipótese de reembolso (urgência, rede inexistente/insuficiente, livre escolha, negativa indevida) → extensão (tabela x integral) → mora → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Enquadrar a hipótese excepcional.** O STJ só admite reembolso fora da rede em casos excepcionais, como inexistência ou insuficiência de credenciado no local e urgência/emergência (EAREsp 1.459.849/ES). Escolha livre do paciente, sem urgência e com rede apta, leva à improcedência (REsp 1.835.265).
- **Extensão — o ponto mais disputado.** Há julgados que limitam o reembolso à tabela do contrato mesmo sem credenciado no local (AgInt no REsp 2.044.182, 4ª Turma) e julgados que mandam reembolsar integralmente quando a rede não tinha profissional apto e o caso era urgente (AgInt no REsp 2.010.604 e AREsp 2.688.415, 3ª Turma). A questão foi afetada como Tema 1375/STJ (REsp 2.167.029 e 2.196.667, afetação em 12/08/2025), com suspensão de recursos especiais e agravos [VERIFICAR: se o tema já foi julgado e qual a tese, antes de protocolar].
- Pedido integral precisa de prova de que **a falha foi da operadora** (rede inexistente/insuficiente, demora, indicação de prestador não credenciado pelo próprio cooperado). Sem isso, peça a tabela como pedido subsidiário.
- Autogestão: retirar fundamentos de CDC (Súmula 608 tratada em `consumidor-plano-de-saude`).
- Juizado Especial: verificar valor e necessidade de perícia (`civel-juizado-especial`).

## Fundamentos verificados
- Lei 9.656/1998, art. 12, VI (reembolso em urgência/emergência, nos limites contratuais, pela tabela do produto, em 30 dias); art. 12, V, "c" (carência de 24 horas em urgência/emergência); art. 35-C (cobertura obrigatória de emergência e urgência).
- CDC, arts. 6º, III e VIII, 47 e 51, IV; CC, art. 205.
- STJ: EAREsp 1.459.849/ES (2ª Seção, julg. 14/10/2020, transcrito na afetação do Tema 1375); REsp 1.835.265; AgInt no REsp 2.044.182; AgInt no REsp 2.010.604; AREsp 2.688.415; REsp 1.992.301.
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Condenação ao reembolso **integral** das despesas (quando a falha da rede ou a urgência estiver provada) e, **subsidiariamente**, ao reembolso pelos valores da tabela do contrato, observados, no mínimo, os preços praticados pelo produto na data do evento (AgInt no REsp 2.106.527, que transcreve essa orientação).
- Exibição da tabela de reembolso e da lista de credenciados da época (exibição de documento) e inversão do ônus (CDC, art. 6º, VIII), salvo autogestão.
- Juros e correção a partir dos marcos definidos pelo núcleo `juros-e-correcao`.
- Dano moral só com fatos concretos (agravamento, endividamento, recusa abusiva), nunca automático.
- Requerimento de sobrestamento ou de distinção, se o Tema 1375 estiver pendente e o caso couber nele.

## Checklist pré-protocolo
- [ ] Hipótese excepcional identificada e provada (urgência, rede inexistente/insuficiente, livre escolha, negativa indevida)
- [ ] Relatório médico com data, CID e justificativa
- [ ] Prova da rede: pedido de indicação de prestador e resposta da operadora
- [ ] Notas e comprovantes em nome de quem pede (legitimidade)
- [ ] Pedido administrativo de reembolso e resposta juntados
- [ ] Tabela de reembolso juntada ou requerida
- [ ] Pedido subsidiário pela tabela
- [ ] Situação do Tema 1375 conferida no portal do STJ
- [ ] Prescrição (art. 205 do CC) checada por pagamento
- [ ] Juros/correção remetidos ao núcleo

## Erros a evitar
- Pedir reembolso integral por simples preferência do paciente, sem urgência nem falha de rede.
- Ajuizar sem ter pedido o reembolso à operadora e sem a lista de documentos que ela exigiu.
- Confundir reembolso (despesa já paga) com obrigação de fazer (tratamento a realizar).
- Aplicar o prazo trienal do enriquecimento sem causa (Tema 610) ao reembolso contratual.
- Ignorar que o tema está afetado e deixar de pedir o reembolso pela tabela como alternativa.
- Fixar taxa de juros ou índice de correção na peça sem passar pelo núcleo.

## Integração com o núcleo
`juros-e-correcao` (mora do reembolso), `prazos-processuais`, `verificacao-de-citacoes` (situação do Tema 1375), `fidelidade-factual`, `estilo-forense`.

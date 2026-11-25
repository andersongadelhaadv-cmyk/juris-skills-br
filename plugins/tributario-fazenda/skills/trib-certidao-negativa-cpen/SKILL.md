---
name: trib-certidao-negativa-cpen
description: >
  Redige requerimento administrativo de certidão negativa de débitos (CND) ou de
  certidão positiva com efeito de negativa (CPEN) e, se negada ou não emitida
  em 10 dias, o roteiro do mandado de segurança ou do pedido judicial (CTN arts.
  151, 205 e 206; Súmula 446/STJ). Use quando o usuário pedir CND, CPEN,
  certidão de regularidade fiscal, certidão negada por débito pago, parcelado,
  garantido ou suspenso, pendência que não é sua, demora na emissão da
  certidão, ou certidão para licitação, financiamento ou venda de imóvel.
metadata:
  area: tributario-fazenda
  tipo_peca: requerimento
  verificado_em: 2026-11-25
---
# Certidão negativa e positiva com efeito de negativa

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: (a) pedir CND ou CPEN ao fisco e demonstrar o enquadramento; (b) contestar a recusa — débito pago, compensado, parcelado, garantido em execução, com exigibilidade suspensa ou que não pertence ao requerente; (c) emissão negada ou não feita no prazo legal.
- Não usar:
  - débito vencido, inscrito e **ainda não executado**, sem causa de suspensão, que o cliente quer garantir: `trib-garantia-antecipada-certidao`;
  - para cancelar a inscrição que trava a certidão: `trib-cancelamento-de-cda`;
  - discussão do mérito do tributo: `trib-acao-anulatoria`, `trib-defesa-administrativa-e-carf`;
  - mandado de segurança com teses amplas além da certidão: `trib-mandado-de-seguranca` (esta skill dá só o recorte da certidão).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Ente e tipo de certidão (federal conjunta, estadual, municipal, de tributo específico) e o período pedido.
2. Relatório de situação fiscal ou tela de pendências, com data.
3. Para cada pendência: inscrição/débito, valor, e a situação real — pago, compensado, parcelado em dia, garantido em execução (com penhora ou seguro aceito), suspenso por liminar, depósito ou impugnação administrativa, ou débito de terceiro.
4. Documentos de prova: guias, recibo de parcelamento, termo de penhora, decisão judicial, protocolo de impugnação.
5. Data do requerimento e resposta (ou silêncio) do fisco.
6. Finalidade e urgência (edital, contrato, escritura).

## Prazo e contagem
- A certidão é expedida nos termos requeridos e entregue "dentro de 10 (dez) dias da data da entrada do requerimento na repartição" (CTN art. 205, parágrafo único).
- Recusa ou silêncio após 10 dias: ato coator para mandado de segurança. Prazo decadencial do MS e demais regras: `trib-mandado-de-seguranca` e `prazos-processuais`.
- A validade da certidão é fixada por norma do ente [VERIFICAR: ato vigente do ente emissor].

## Estrutura da peça
Requerimento: identificação → período e finalidade → pendências e enquadramento em cada hipótese do art. 206 → documentos → pedido de emissão. Se negada: MS com a recusa como ato coator. Roteiro em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **CND (art. 205)**: inexistência de débito. Requerimento com identificação, domicílio fiscal, ramo de atividade e período.
- **CPEN (art. 206)**: três hipóteses, cada uma com prova própria — (1) créditos não vencidos; (2) cobrança executiva com **penhora efetivada**; (3) **exigibilidade suspensa**.
- Causas de suspensão (CTN art. 151, redação da LC 236/2026): moratória; depósito integral; impugnações e recursos administrativos; liminar em MS; liminar ou tutela em outras ações; parcelamento; arbitragem tributária; proposta de transação aceita; acordo de mediação; aceitação, pelo credor, de seguro garantia ou fiança oferecidos em execução fiscal (inciso X).
- Depósito: só suspende se integral e em dinheiro (Súmula 112/STJ).
- Débito declarado e não pago: a recusa da certidão é legítima (Súmula 446/STJ). Não insista sem prova de pagamento, compensação ou suspensão.
- Execução sem penhora: o STJ aplicou o Tema 273 para negar CPEN quando não havia penhora (AgInt no REsp 2.114.228, 2ª Turma, 2024) [VERIFICAR: enunciado literal da tese 273].
- Garantia antes da execução: CPEN pelo Tema 237/STJ (ver `trib-garantia-antecipada-certidao`).
- Onde pedir: o STJ entendeu que a CPEN não é analisada dentro da execução fiscal; exige pedido administrativo ou ação autônoma (REsp 2.124.236, 2ª Turma, 2025). Faça o requerimento administrativo e, se negado, ação própria.

## Fundamentos verificados
CTN arts. 151 (LC 236/2026), 205 e 206; Súmulas 112 e 446/STJ; REsp 2.124.236; AgInt no REsp 2.114.228 (Tema 273); Tema 237/STJ. Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Administrativo: emissão da CND ou da CPEN, com indicação, pendência a pendência, da hipótese do art. 206 e do documento que a prova; correção do sistema (baixa de débito pago, vinculação de parcelamento ou de garantia).
- Judicial (se negada): liminar para expedição da certidão em prazo curto, com multa; notificação da autoridade; confirmação da segurança.
- Atualização de valores, se discutida: `juros-e-correcao`.

## Checklist pré-protocolo
- [ ] Relatório de pendências recente juntado
- [ ] Cada pendência enquadrada em uma hipótese (inexistente, não vencida, penhorada, suspensa) com prova
- [ ] Súmula 446 enfrentada se houver débito declarado
- [ ] Garantia em execução: termo de penhora ou aceitação do seguro/fiança nos autos
- [ ] Data do requerimento registrada (10 dias do art. 205)
- [ ] Urgência documentada para eventual liminar

## Erros a evitar
- Pedir CPEN só com a propositura de ação, sem liminar, depósito ou garantia (não suspende).
- Pedir a certidão nos autos da execução fiscal em vez de requerimento ou ação própria (REsp 2.124.236).
- Garantia parcial apresentada como se bastasse.
- Ignorar débitos de filiais ou de outros tributos do mesmo ente que também constam do relatório.
- Ajuizar MS sem prova pré-constituída de cada pendência.

## Integração com o núcleo
`prazos-processuais`, `juros-e-correcao`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

---
name: trabalhista-revisao-de-contrato-de-trabalho
description: >
  Analisa e revisa contrato individual de trabalho já assinado ou minuta
  recebida, cláusula por cláusula, apontando nulidades (CLT arts. 9º, 444 e
  468), modalidade incompatível com a realidade (arts. 443, 445, 451 e 452-A),
  compensação de jornada fora do instrumento exigido (art. 59), teletrabalho,
  transferência, descontos e cláusulas de hipersuficiente, com parecer de risco
  e redação sugerida. Use quando o usuário pedir revisão de contrato de
  trabalho, análise de minuta de contrato CLT, parecer sobre cláusula
  trabalhista, auditoria de contratos de empregados ou conferir se o contrato
  de experiência ou intermitente é válido.
metadata:
  area: trabalhista
  tipo_peca: parecer
  verificado_em: 2026-11-25
---
# Análise e revisão de contrato de trabalho

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: contrato CLT existente, aditivo ou minuta, revisado a pedido do empregador (prevenção de passivo) ou do empregado (avaliação antes de assinar ou de ajuizar).
- Não usar: redigir contrato do zero (use `trabalhista-contrato-de-trabalho`); contrato civil de prestação de serviços ou PJ (use `contratos-analise-e-revisao-de-contrato` e, se houver indício de subordinação, `trabalhista-vinculo-de-emprego`); acordo de rescisão já em litígio (use `trabalhista-acordo-extrajudicial`).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Contrato, aditivos, regulamento interno e políticas que o contrato incorpora.
2. Para quem revisamos (empregador ou empregado) e o objetivo (assinar, adequar, avaliar passivo, preparar ação).
3. Como o contrato é executado **de fato**: função real, jornada real, local, controle de ponto, remuneração efetiva.
4. Norma coletiva da categoria vigente no período.
5. Datas: admissão, prorrogações, alterações e eventual extinção.
6. Escolaridade e salário do empregado (para o art. 444 parágrafo único e o art. 507-A).

## Prazo e contagem
- Se a revisão for para ação, conferir a prescrição: 5 anos, até 2 anos após a extinção (CLT art. 11); interrupção só pelo ajuizamento e apenas para pedidos idênticos (art. 11 §3º). Pretensão sobre alteração do pactuado: prescrição total, salvo parcela também assegurada em lei (art. 11 §2º).
- Prazos processuais: `prazos-processuais`.

## Estrutura do parecer
Identificação e objetivo → documentos analisados → resumo executivo (riscos altos primeiro) → análise cláusula por cláusula (texto, problema, fundamento, risco, redação sugerida) → descompasso entre contrato e realidade → recomendações e próximos passos. Detalhe em [estrutura](references/estrutura.md).

## Roteiro de análise (o que conferir)
1. **Natureza**: há subordinação, habitualidade, pessoalidade e salário (art. 3º)? Contrato "autônomo" com esses elementos é nulo quanto à forma (art. 9º; art. 442-B não salva fraude).
2. **Modalidade**: prazo determinado só nas hipóteses do art. 443 §2º; limite de 2 anos ou 90 dias de experiência (art. 445); mais de uma prorrogação = prazo indeterminado (art. 451). Intermitente: escrito, valor-hora mínimo e parcelas do art. 452-A §6º.
3. **Jornada e compensação**: banco de horas anual só por norma coletiva; semestral por acordo individual escrito; mensal por acordo tácito ou escrito (art. 59 §§2º, 5º, 6º). Tempo parcial dentro dos limites do art. 58-A.
4. **Teletrabalho**: precisa constar expressamente (art. 75-C); reversão com 15 dias de transição e aditivo.
5. **Alterações**: aditivo que reduz direito do empregado é nulo, mesmo com assinatura (art. 468).
6. **Transferência**: cláusula de transferência exige real necessidade de serviço (art. 469 §1º); adicional na provisória (§3º).
7. **Descontos**: dano culposo só se pactuado (art. 462 §1º).
8. **Hipersuficiente**: confirmar os dois requisitos (diploma superior + salário igual ou superior a duas vezes o teto do RGPS) antes de validar livre estipulação (art. 444 parágrafo único) ou arbitragem (art. 507-A, acima de duas vezes o teto, com iniciativa ou concordância expressa do empregado).
9. **Norma coletiva**: cláusula contratual contrária ao coletivo, nas matérias do art. 611-A, tende a ceder; e o coletivo não pode suprimir os direitos do art. 611-B.
10. **Gestante em contrato a prazo**: estabilidade preservada (Súmula 244, III, do TST).
11. **Não concorrência e confidencialidade**: limites e contrapartida [VERIFICAR: requisitos jurisprudenciais não confirmados].

## Fundamentos verificados
- CLT arts. 3º, 9º, 11, 58-A, 59, 75-B, 75-C, 442-B, 443, 444, 445, 451, 452-A, 462 §1º, 468, 469, 507-A, 611-A, 611-B.
- Súmula 244 do TST.
Detalhe em [fundamentos](references/fundamentos.md).

## Classificação de risco (usar no parecer)
- **Alto**: vínculo mascarado; prazo determinado sem hipótese legal; prorrogação dupla; alteração lesiva; banco de horas anual sem norma coletiva; teletrabalho não escrito com cobrança de presença.
- **Médio**: cláusula de transferência genérica; descontos sem previsão; intermitente sem discriminação no recibo.
- **Baixo**: redação imprecisa sem efeito prático imediato.

## Checklist de entrega
- [ ] Riscos classificados e ordenados (alto → baixo)
- [ ] Cada achado com fundamento conferido e redação sugerida
- [ ] Contrato confrontado com a execução real, não só com o papel
- [ ] Norma coletiva lida e citada no ponto em que prevalece
- [ ] Prescrição apontada, se o parecer servir a ação
- [ ] Pontos em [VERIFICAR] destacados ao cliente

## Erros a evitar
- Validar cláusula só porque o empregado assinou: o art. 468 anula alteração lesiva consentida.
- Tratar o art. 442-B como salvo-conduto para "pejotização".
- Aplicar a livre estipulação do hipersuficiente sem conferir diploma e salário.
- Ignorar a norma coletiva e opinar só com a CLT.
- Dar parecer sem saber para qual parte se trabalha: a mesma cláusula é risco para um e argumento para o outro.

## Integração com o núcleo
`fidelidade-factual`, `verificacao-de-citacoes`, `estilo-forense`, `prazos-processuais`; estimativa de passivo atualizado pelo `juros-e-correcao`.

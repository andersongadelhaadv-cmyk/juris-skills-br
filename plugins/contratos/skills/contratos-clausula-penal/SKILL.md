---
name: contratos-clausula-penal
description: >
  Redige e revisa cláusula penal compensatória e moratória em contratos civis e
  empresariais, com base nos arts. 408 a 416 do Código Civil, no dever de
  redução equitativa do art. 413 e no Tema 970 do STJ. Use quando o usuário
  pedir para criar, calibrar, revisar ou contestar multa contratual, multa
  rescisória, multa por atraso, cláusula de "perdas e danos pré-fixadas",
  indenização suplementar, ou quiser saber se a multa pode ser reduzida pelo juiz.
metadata:
  area: contratos
  tipo_peca: contrato
  verificado_em: 2026-11-25
---
# Cláusula penal

Ferramenta de apoio; o advogado responsável revisa todo documento antes de assinar ou enviar.

## Quando usar / quando não usar
- Usar: (a) redigir cláusula penal nova em qualquer contrato; (b) revisar a multa de minuta recebida da outra parte; (c) parecer sobre exigibilidade ou redução de multa já pactuada; (d) calibrar multa por atraso x multa por inadimplemento total.
- Não usar: multa processual ou astreinte fixada pelo juiz (não é cláusula penal); arras (CC arts. 417 a 420 — regime próprio, mencionar só para distinguir); relação de consumo com cláusula de adesão abusiva — combinar com a skill de consumidor pertinente.

## Entradas mínimas (perguntar o que faltar; nunca supor fatos)
1. Tipo de contrato, partes e se é paritário (empresarial/civil) ou de adesão/consumo.
2. Valor da obrigação principal (teto do art. 412) e forma de pagamento.
3. Qual risco a multa deve cobrir: atraso (moratória), descumprimento de cláusula específica (ex.: exclusividade, confidencialidade) ou inadimplemento total (compensatória).
4. Prejuízo estimado se o risco ocorrer, e se a parte quer poder cobrar dano maior que a multa.
5. Se houver multa já pactuada: texto integral, o que foi cumprido, quando e por quem.

## Prazos relevantes
- Prescrição da pretensão de cobrar a multa (responsabilidade contratual): o STJ aplica, como regra, o prazo decenal do art. 205 do CC, reservando o trienal do art. 206, § 3º, V, à responsabilidade extracontratual (REsp 1.915.139, 3ª Turma, 13/04/2026, que aplica o EREsp 1.280.825/RJ [VERIFICAR: EREsp não localizado diretamente]). Confirmar se há prazo especial para o tipo contratual.
- Mora: com termo certo, a multa moratória incide do vencimento; sem termo, constituir em mora por notificação antes de cobrar.
- Prazos processuais em dias úteis: `prazos-processuais`.

## Estrutura do documento (cláusulas essenciais)
1. Hipótese de incidência precisa: qual obrigação, qual fato gera a multa.
2. Natureza declarada: moratória ou compensatória (o nome não vincula o juiz, mas orienta a leitura).
3. Valor ou critério: percentual sobre a obrigação, valor fixo, ou escalonado conforme o tempo de execução já decorrido.
4. Teto: nunca acima do valor da obrigação principal (art. 412).
5. Cumulação: para a moratória, cumula com a exigência da obrigação (art. 411); para a compensatória, é alternativa ao cumprimento (art. 410).
6. Indenização suplementar: só existe se convencionada expressamente (art. 416, parágrafo único); a multa vale então como mínimo.
7. Forma de cobrança, notificação prévia e prazo de purgação, se houver.
8. Juros e correção sobre a multa: remeter ao núcleo `juros-e-correcao`; nunca fixar taxa nesta skill.
Detalhe em [estrutura](references/estrutura.md).

## Riscos e cláusulas sensíveis
- Redução judicial é **dever**: o STJ trata o art. 413 como norma cogente e de ordem pública, aplicável mesmo sem pedido (REsp 2.209.685, 3ª Turma, 07/04/2026). Multa desproporcional será cortada; calibre antes.
- Multa que já se reduz proporcionalmente ao tempo cumprido tende a não sofrer nova redução por adimplemento parcial (AgInt no REsp 1.889.156, 3ª Turma, 20/03/2023) — vale como técnica de redação.
- Multa pactuada em transação homologada continua sendo cláusula penal, redutível a qualquer tempo (REsp 1.999.836, 3ª Turma, 27/09/2022).
- Compra e venda de imóvel com multa moratória equivalente ao locativo: não cumula com lucros cessantes (tese do Tema 970/STJ transcrita no REsp 2.158.753, 3ª Turma, 16/06/2025 [VERIFICAR: tema conferido só por acórdãos que o aplicam]); se a multa ficar abaixo do locativo, a cumulação é admitida (REsp 2.072.218, 4ª Turma, 27/10/2025).
- Obrigação indivisível com vários devedores: todos incorrem, mas só o culpado responde pela pena inteira (art. 414); divisível: só o infrator, proporcionalmente (art. 415).
- Contrato paritário: presunção de simetria (art. 421-A) ajuda a sustentar a multa, mas não afasta o art. 413.

## Fundamentos verificados
- CC arts. 408 a 416 (cláusula penal); 410 e 411 (efeitos por espécie); 412 (teto); 413 (redução equitativa); 416 (prejuízo dispensado; suplementar só se pactuada).
- CC arts. 421, 421-A, 422 e 113 (função social, paridade, boa-fé, interpretação).
- STJ: REsp 2.209.685; AgInt no REsp 1.889.156; REsp 1.999.836; REsp 2.158.753 (Tema 970); REsp 2.072.218; REsp 1.915.139 (prescrição decenal contratual).
Detalhe em [fundamentos](references/fundamentos.md).

## Checklist antes de assinar/enviar
- [ ] Hipótese de incidência descrita sem ambiguidade (uma multa por risco)
- [ ] Espécie definida (moratória x compensatória) e efeitos coerentes (arts. 410/411)
- [ ] Valor dentro do teto do art. 412 e proporcional ao risco
- [ ] Escalonamento pelo tempo de execução, quando houver prazo longo
- [ ] Indenização suplementar prevista expressamente, se desejada (art. 416, par. único)
- [ ] Não há duplicidade com arras ou com outra multa sobre o mesmo fato
- [ ] Em imóvel/consumo: Tema 970 considerado
- [ ] Juros e correção remetidos ao núcleo

## Erros a evitar
- Fixar multa igual ou superior ao valor do contrato "para intimidar": será reduzida e enfraquece a credibilidade da cláusula.
- Prever multa compensatória e, na mesma cláusula, exigir também o cumprimento integral sem distinguir.
- Esquecer a cláusula de indenização suplementar e depois tentar cobrar prejuízo maior que a multa.
- Chamar de "multa" o que é arras penitenciais (art. 420) ou vice-versa.
- Redigir "renúncia à redução do art. 413": norma cogente, a renúncia não vale.

## Integração com o núcleo
`juros-e-correcao` (encargos sobre a multa), `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

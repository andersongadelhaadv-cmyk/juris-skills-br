---
name: contratos-distrato-e-rescisao
description: >
  Escolhe a via correta de extinção do contrato (distrato, resilição unilateral
  por denúncia, resolução por inadimplemento, cláusula resolutiva expressa ou
  tácita, onerosidade excessiva) e redige o instrumento de distrato ou o
  parecer de rescisão com acerto de contas, quitação e devolução de bens e
  dados (CC arts. 472 a 480). Use quando o usuário pedir distrato, rescisão
  amigável, encerrar contrato, denúncia com aviso prévio, resolver contrato
  por inadimplemento, invocar exceção do contrato não cumprido ou pedir
  revisão/resolução por onerosidade excessiva.
metadata:
  area: contratos
  tipo_peca: instrumento
  verificado_em: 2026-11-25
---
# Distrato e rescisão de contrato

Ferramenta de apoio; o advogado responsável revisa todo documento antes de assinar ou enviar.

## Quando usar / quando não usar
- Usar: encerrar contrato civil ou empresarial por acordo (distrato), por vontade de uma parte quando a lei ou o contrato permitem (resilição unilateral), por inadimplemento (resolução), ou diante de fato superveniente que torna a prestação excessivamente onerosa.
- Não usar: contrato de trabalho (rescisão trabalhista tem regime próprio); apenas mudar cláusulas mantendo o vínculo (`contratos-aditivo-contratual`); constituir o devedor em mora antes de resolver (`contratos-notificacao-de-descumprimento` — normalmente vem antes desta skill); ação judicial de resolução (usar como base, mas a peça é processual).

## Primeiro passo: qualificar a via (não usar "rescisão" como palavra-ônibus)
| Situação | Via | Base |
| --- | --- | --- |
| As duas partes querem encerrar | Distrato | CC art. 472 (mesma forma do contrato) |
| Uma parte quer sair, sem culpa da outra | Resilição unilateral (denúncia) | CC art. 473 e parágrafo único |
| A outra parte descumpriu | Resolução + perdas e danos | CC art. 475 |
| Há cláusula resolutiva expressa | Opera de pleno direito | CC art. 474, 1ª parte |
| Sem cláusula expressa | Depende de interpelação judicial | CC art. 474, 2ª parte |
| Quem cobra ainda não cumpriu | Exceção do contrato não cumprido | CC art. 476 |
| Patrimônio da outra parte ruiu | Exceção de inseguridade | CC art. 477 |
| Fato extraordinário e imprevisível | Onerosidade excessiva | CC arts. 478 a 480 |

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Contrato, aditivos e anexos; cláusulas de prazo, denúncia, aviso prévio, multa, resolutiva expressa, foro.
2. Quem quer encerrar e por quê. Há inadimplemento? De quem, de qual cláusula, desde quando, com que prova?
3. O cliente cumpriu a parte dele? (decisivo para o art. 476)
4. Houve notificação prévia? Cópia e prova de recebimento.
5. Investimentos relevantes feitos pela outra parte para executar o contrato (art. 473, parágrafo único).
6. Valores em aberto dos dois lados; bens, equipamentos, documentos e dados a devolver.
7. Garantias vigentes (fiança, caução, seguro) e o que fazer com elas.
8. Consumidor numa das pontas? Imóvel na planta? (Súmula 543/STJ)

## Prazos relevantes
- Aviso prévio contratual da denúncia: contar a partir do recebimento, nos termos do contrato.
- Art. 473, parágrafo único: com investimentos consideráveis, a denúncia só produz efeito depois de prazo compatível com a natureza e o vulto deles.
- Cobrança de dívida líquida constante de instrumento: prescrição de 5 anos (CC art. 206, § 5º, I); regra geral de 10 anos (art. 205). Registrar o vencimento de cada parcela.
- Notificação extrajudicial **não** interrompe a prescrição (o art. 202, V, exige ato judicial). Se o prazo estiver perto, ajuizar ou obter reconhecimento do devedor.
- Prazos processuais: `prazos-processuais`.

## Estrutura do documento
- **Distrato:** qualificação → contrato-base → declaração de extinção e data de eficácia → acerto de contas → devoluções → garantias → quitação (específica) → obrigações que sobrevivem → assinaturas na mesma forma do contrato.
- **Parecer de rescisão:** fatos → qualificação da via → requisitos atendidos ou faltantes → riscos (art. 476, adimplemento substancial) → recomendação e minuta da comunicação.
Detalhe em [estrutura](references/estrutura.md).

## Riscos e cláusulas sensíveis
- **Forma do distrato.** Se o contrato exigiu escritura ou forma especial, o distrato segue a mesma (art. 472). Distrato informal de contrato solene é atacável.
- **Quitação geral.** Encerra pleitos que o cliente nem mapeou. Preferir quitação limitada aos itens listados e ressalvar o que fica em aberto.
- **Cláusula resolutiva expressa.** Opera de pleno direito, mas a jurisprudência exige que o devedor seja interpelado; desatendida a interpelação, a resolução é viável sem ação prévia (REsp 2.139.100). Em leasing, a notificação prévia é necessária mesmo com cláusula expressa (Súmula 369/STJ).
- **Adimplemento substancial.** Cumprimento expressivo pode afastar a resolução e reduzir o credor à cobrança (AgInt no AREsp 2.656.253). Medir o percentual cumprido antes de prometer ao cliente a extinção.
- **Exceção do contrato não cumprido.** Quem resolve sem ter cumprido a própria prestação vira o inadimplente.
- **Onerosidade excessiva.** Exige contrato de execução continuada ou diferida, fato extraordinário e imprevisível e extrema vantagem para a outra parte (art. 478); a outra parte pode evitar a resolução oferecendo modificação equitativa (art. 479). Em contrato empresarial paritário, a revisão é excepcional e limitada (art. 421-A, III).
- **Multa rescisória.** É cláusula penal: não excede a obrigação principal (art. 412) e pode ser reduzida pelo juiz (art. 413). Remeter a `contratos-clausula-penal` quando a multa for o centro da disputa.
- **Imóvel com consumidor.** Resolução de promessa de compra e venda: restituição imediata, integral ou parcial conforme a culpa (Súmula 543/STJ).
- **Dados pessoais.** Definir o término do tratamento, a devolução ou eliminação e o que pode ser conservado (LGPD, arts. 15 e 16).
- **Consumidor.** Cláusula que exonere o fornecedor de responsabilidade é nula (CDC art. 51, I).

## Fundamentos verificados
- CC arts. 205, 206 § 5º I, 202 V, 412, 413, 421-A, 472 a 480.
- CDC art. 51, I; LGPD arts. 15 e 16.
- Súmulas 369 e 543/STJ; REsp 2.139.100; AgInt no AREsp 2.656.253.
Detalhe em [fundamentos](references/fundamentos.md).

## Checklist antes de assinar/enviar
- [ ] Via qualificada corretamente (tabela acima) e termo técnico coerente no texto
- [ ] Cliente adimplente, ou risco do art. 476 registrado
- [ ] Notificação prévia feita e provada, quando exigida
- [ ] Aviso prévio e prazo do art. 473, parágrafo único, respeitados
- [ ] Acerto de contas item a item, com vencimentos; juros e correção pelo núcleo
- [ ] Quitação específica, com ressalvas
- [ ] Bens, documentos e dados: devolução ou eliminação com prazo
- [ ] Garantias liberadas ou executadas — dito expressamente
- [ ] Cláusulas que sobrevivem (confidencialidade, não concorrência, foro) preservadas
- [ ] Mesma forma do contrato original

## Erros a evitar
- Chamar de "rescisão" o que é distrato, ou de "resolução" o que é denúncia — muda o regime de perdas e danos.
- Resolver sem interpelar quando não há cláusula resolutiva expressa (art. 474).
- Dar quitação geral sem lista.
- Esquecer a prescrição correndo enquanto se negocia o distrato.
- Fixar multa acima do valor da obrigação principal.
- Calcular juros e correção sem o núcleo `juros-e-correcao`.

## Integração com o núcleo
`juros-e-correcao`, `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

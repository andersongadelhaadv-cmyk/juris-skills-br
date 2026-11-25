---
name: contratos-parecer-sobre-contrato
description: >
  Redige parecer jurídico sobre contrato já celebrado: validade (nulidade,
  anulabilidade), interpretação de cláusula controvertida, execução,
  inadimplemento, resolução, revisão por onerosidade excessiva e prescrição,
  com base nos arts. 104 a 184, 205, 206 e 421 a 480 do Código Civil. Use
  quando o usuário pedir parecer, opinião legal, consulta escrita ou "qual a
  nossa posição" sobre um contrato em vigor ou em conflito, inclusive antes de
  notificar, rescindir ou ajuizar ação.
metadata:
  area: contratos
  tipo_peca: parecer
  verificado_em: 2026-11-25
---
# Parecer sobre contrato

Ferramenta de apoio; o advogado responsável revisa todo documento antes de assinar ou enviar.

## Quando usar / quando não usar
- Usar: pergunta jurídica concreta sobre contrato existente — é válido? o que a cláusula X significa? podemos rescindir? cabe revisão? a multa é exigível? está prescrito?
- Não usar: minuta ainda em negociação (`contratos-analise-e-revisao-de-contrato`); redigir contrato (`contratos-elaboracao-de-contrato`); petição inicial ou contestação (skills de processo civil, se houver).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. A pergunta (ou perguntas) que o consulente quer respondida, por escrito.
2. Contrato assinado, aditivos, anexos e comprovante de assinatura (data e forma).
3. Cronologia dos fatos com documentos: e-mails, notificações, atas, notas fiscais, comprovantes de pagamento.
4. Qual parte é o consulente e o que pretende fazer depois do parecer.
5. Houve tolerância reiterada, aditivo informal ou comportamento que altere o sentido do texto?
6. Há ação, arbitragem ou notificação em curso?

## Prazos relevantes
- Nulidade absoluta não convalesce com o tempo (art. 169).
- Anulabilidade: 4 anos, decadencial (art. 178), com termo inicial conforme o vício.
- Pretensão por inadimplemento contratual: 10 anos (art. 205) — orientação da 2ª Seção do STJ; extracontratual: 3 anos (art. 206, § 3º, V).
- Cobrança de dívida cujo valor decorre de critérios já fixados no contrato: 5 anos (art. 206, § 5º, I); se os critérios não estão no contrato, aplica-se o art. 205 (AgInt nos EAREsp 1.850.024).
- Vício redibitório: art. 445. Prazos processuais: `prazos-processuais`.

## Estrutura do documento
Ementa → consulta (perguntas numeradas) → documentos examinados → fatos relevantes (com remissão a documento) → análise por pergunta (norma → interpretação → aplicação → riscos e argumentos contrários) → respostas objetivas → recomendações e próximos passos → ressalvas. Detalhe em [estrutura](references/estrutura.md).

## Eixos de análise
- **Validade:** requisitos do art. 104; nulidades do art. 166 e simulação (art. 167); anulabilidades do art. 171 (erro, dolo, coação, estado de perigo, lesão, fraude contra credores). Distinguir: nulo não se confirma (art. 169); anulável se confirma e decai.
- **Interpretação:** intenção acima da literalidade (art. 112); boa-fé e usos (art. 113); negócios benéficos e renúncia interpretam-se estritamente (art. 114); adesão a favor do aderente (art. 423). Em contrato paritário, a revisão é excepcional e limitada (art. 421, parágrafo único; art. 421-A, III).
- **Execução e inadimplemento:** exceção de contrato não cumprido (art. 476) e de inseguridade (art. 477); resolução ou cumprimento com perdas e danos (art. 475); cláusula resolutiva expressa opera de pleno direito, a tácita exige interpelação judicial (art. 474).
- **Revisão e resolução por fato superveniente:** art. 317 (desproporção manifesta) e arts. 478 a 480 (onerosidade excessiva por fato extraordinário e imprevisível). Evento geral (como a pandemia) não basta por si: exige prova do impacto concreto na relação (AgInt no AREsp 2.552.263).
- **Penalidades:** cláusula penal exigível sem prova de prejuízo (art. 416), mas sujeita a redução obrigatória (art. 413 — REsp 2.209.685).
- **Instância recursal:** a interpretação de cláusula se resolve nas instâncias ordinárias — não enseja recurso especial (Súmula 5 do STJ). O parecer deve preparar a prova e a tese para o primeiro grau.

## Riscos e cuidados sensíveis
- Responder exatamente às perguntas formuladas; questão não perguntada mas relevante vai em "observações".
- Expor o melhor argumento da parte contrária e a probabilidade (alta, média, baixa) com a razão.
- Não afirmar fato não documentado; marcar como premissa informada pelo consulente.
- Valores devidos: indicar a base de cálculo; juros e correção pelo núcleo `juros-e-correcao`.

## Fundamentos verificados
- CC: arts. 104, 112, 113, 114, 166, 167, 169, 171, 178, 205, 206, 317, 393, 413, 416, 421, 421-A, 422, 423, 445, 474 a 480.
- Lei 13.874/2019, art. 7º.
- Súmula 5 do STJ.
- STJ: AgInt nos EREsp 1.685.808 (prazo decenal contratual); AgInt nos EAREsp 1.850.024 (quinquenal para dívida líquida pelo contrato); AgInt no AREsp 2.552.263 (pandemia não autoriza revisão automática); REsp 2.209.685 (art. 413 cogente).
Detalhe em [fundamentos](references/fundamentos.md).

## Checklist antes de enviar
- [ ] Cada pergunta da consulta tem resposta objetiva (sim / não / depende de X)
- [ ] Todo fato remete a documento examinado ou está marcado como premissa
- [ ] Prescrição e decadência calculadas com data de início e fundamento
- [ ] Argumento contrário enfrentado
- [ ] Recomendação prática (notificar, negociar, aguardar, ajuizar) com prazo
- [ ] Citações conferidas (`verificacao-de-citacoes`)
- [ ] Ressalva de que o parecer se limita aos documentos e fatos informados

## Erros a evitar
- Confundir nulidade com anulabilidade e perder o prazo decadencial.
- Tratar contrato empresarial paritário como se fosse de consumo.
- Recomendar resolução imediata quando não há cláusula resolutiva expressa (art. 474 exige interpelação judicial).
- Invocar onerosidade excessiva sem demonstrar evento extraordinário, imprevisível e o desequilíbrio concreto.
- Contar com o STJ para rediscutir cláusula (Súmula 5).

## Integração com o núcleo
`juros-e-correcao`, `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

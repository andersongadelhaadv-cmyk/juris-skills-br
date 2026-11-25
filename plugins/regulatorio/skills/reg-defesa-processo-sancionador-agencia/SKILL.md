---
name: reg-defesa-processo-sancionador-agencia
description: >
  Redige defesa administrativa contra auto de infração ou notificação de
  processo sancionador instaurado por agência reguladora federal (ANEEL,
  ANATEL, ANP, ANTT, ANTAQ, ANAC, ANVISA, ANA, ANM, ANCINE e similares), com
  base na Lei 13.848/2019, na Lei 9.784/1999, na Lei 9.873/1999 e na LINDB. Use
  quando o usuário pedir defesa contra auto de infração de agência, impugnação
  de notificação de processo sancionador regulatório, alegações finais em
  processo de agência, prescrição punitiva ou intercorrente da agência, ou
  redução de multa regulatória ainda em primeira instância.
metadata:
  area: regulatorio
  tipo_peca: contestacao
  verificado_em: 2026-11-25
---
# Defesa em processo sancionador de agência reguladora

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: auto de infração, termo de notificação ou despacho de instauração de processo sancionador de agência reguladora federal, ainda sem decisão de primeira instância; também para as alegações finais (art. 44 da Lei 9.784/1999).
- Não usar:
  - Decisão já proferida aplicando multa: `reg-recurso-multa-agencia`.
  - Operadora de plano de saúde autuada pela ANS: `reg-defesa-sancionador-ans`.
  - Sanção em licitação ou contrato administrativo: `adm-defesa-em-processo-sancionador-licitacao`.
  - Processo da ANPD (LGPD): `digital-defesa-em-processo-sancionador-anpd`.
  - Auto de infração tributário: `trib-defesa-administrativa-e-carf`.
  - Ação judicial para anular a multa ou suspender o processo: `adm-mandado-de-seguranca`.

## Entradas mínimas (perguntar o que faltar; nunca supor fatos)
1. Cópia integral do auto/notificação, com a data da ciência e o meio de intimação.
2. Agência, norma setorial e resolução da agência que regem o rito (prazo de defesa, instâncias, pagamento com desconto, termo de ajustamento) — o advogado confere a versão vigente.
3. Dispositivo tido por violado e a descrição da conduta imputada; período da infração.
4. Data do fato (ou da cessação, se permanente/continuada) e as datas de todos os atos do processo — para a prescrição.
5. Ato de outorga do autuado (concessão, permissão, autorização, registro) e histórico de sanções anteriores.
6. Documentos técnicos, medições, relatórios, comunicações com a agência, providências corretivas já adotadas.
7. Porte e faturamento, se a norma de dosimetria usar esses critérios.

## Prazo e contagem
- Prazo de defesa: o da norma setorial ou resolução da agência. [VERIFICAR: prazo na norma da agência do caso]. Na falta de norma específica, a Lei 9.784/1999 manda contar da ciência oficial, excluindo o dia do começo e incluindo o do vencimento, em dias **contínuos** (art. 66, caput e § 2º) — não aplique automaticamente a contagem em dias úteis do CPC.
- Alegações finais: até 10 dias após o fim da instrução, salvo prazo legal diverso (art. 44).
- Prescrição punitiva federal: 5 anos do ato ou da cessação; intercorrente: processo parado mais de 3 anos pendente de julgamento ou despacho (Lei 9.873/1999, art. 1º, caput e § 1º).
- Conferência de contagem: `prazos-processuais`.

## Estrutura da peça
Endereçamento à autoridade indicada na intimação → qualificação e representação → tempestividade → síntese da imputação → preliminares (nulidade, prescrição, competência, tipicidade) → mérito (fato, prova técnica, excludentes) → dosimetria subsidiária → provas → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Intimação válida**: deve conter os fatos e fundamentos legais pertinentes, entre outros elementos (Lei 9.784/1999, art. 26, § 1º). Imputação genérica impede a defesa.
- **Tipicidade e legalidade**: a conduta descrita precisa corresponder ao dispositivo citado; sanção sem base em lei ou em norma vigente na data do fato é nula. Nova interpretação não retroage (art. 2º, parágrafo único, XIII).
- **Prescrição**: punitiva (5 anos) e intercorrente (3 anos) — ver Fundamentos. Despacho meramente ordinatório não interrompe a intercorrente (precedente confirmado em [fundamentos](references/fundamentos.md)).
- **Competência**: autoridade que lavrou e que julgará, conforme o regimento da agência; delegação interna exige reexame possível pelo colegiado (Lei 13.848/2019, art. 7º).
- **Agência estadual ou municipal**: a Lei 9.873/1999 é federal; ver a lei local antes de alegar prescrição (Tema 1294/STJ).

## Fundamentos verificados
- Lei 13.848/2019: art. 4º (vedação de sanção além do necessário), art. 5º (motivação), art. 7º (decisão colegiada).
- Lei 9.784/1999: arts. 2º, 3º, 26 § 1º, 38, 44, 50, 65.
- Lei 9.873/1999: arts. 1º e 2º.
- LINDB: arts. 20, 22 (§§ 1º a 3º) e 24.
- STJ: Tema 1293 (intercorrente da Lei 9.873 nas infrações administrativas não tributárias); AREsp 3.090.385 (despacho ordinatório não interrompe); Tema 1294 (estados e municípios).
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Reconhecimento da prescrição (punitiva ou intercorrente) e arquivamento.
- Nulidade do auto (intimação deficiente, atipicidade, incompetência).
- Improcedência da autuação no mérito.
- Subsidiariamente: conversão em advertência ou redução da multa, com atenuantes e a dosimetria do art. 22, § 2º, da LINDB e da norma setorial.
- Produção de prova: documental, pericial/técnica, diligências e oitiva (Lei 9.784/1999, art. 38); recusa só fundamentada (art. 38, § 2º).
- Vista integral dos autos e cópia (art. 3º, II).
- Intimação das próximas decisões no nome do advogado.

## Checklist pré-protocolo
- [ ] Prazo conferido na norma da agência e contado da ciência
- [ ] Linha do tempo com todos os atos (para prescrição punitiva e intercorrente)
- [ ] Dispositivo imputado transcrito na versão vigente na data do fato
- [ ] Cada fato da autuação respondido com documento
- [ ] Pedido subsidiário de dosimetria com os critérios da norma setorial
- [ ] Procuração e atos societários juntados
- [ ] Avaliado o pagamento com desconto ou termo de ajustamento previsto na norma da agência (efeitos sobre a defesa)

## Erros a evitar
- Contar prazo em dias úteis por hábito do CPC sem conferir a norma da agência.
- Defesa só de tese: o recurso especial não revê resolução de agência nem prova; a prova técnica tem de entrar já na esfera administrativa.
- Esquecer o pedido subsidiário de dosimetria por apostar só na nulidade.
- Alegar prescrição da Lei 9.873 contra agência estadual sem lei local.
- Tratar ato meramente ordinatório como interruptivo (ou o contrário) sem ler o ato.

## Integração com o núcleo
`prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`, `juros-e-correcao` (encargos sobre multa).

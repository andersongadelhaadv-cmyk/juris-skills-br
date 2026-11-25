---
name: amb-termo-ajustamento-conduta
description: >
  Elabora, revisa e negocia termo de ajustamento de conduta (TAC) ambiental
  com o Ministério Público ou órgão público legitimado (Lei 7.347/1985, art.
  5º, § 6º), e orienta sobre termo de compromisso do órgão ambiental (Lei
  9.605/1998, art. 79-A) e do PRA (Lei 12.651/2012, art. 59). Use quando o
  usuário pedir minuta ou revisão de TAC, contraproposta ao MP em inquérito
  civil, cronograma de PRAD, cláusula de multa por descumprimento, aditamento,
  ou análise de execução e prescrição de TAC já assinado.
metadata:
  area: ambiental
  tipo_peca: contrato
  verificado_em: 2026-11-25
---
# Termo de ajustamento de conduta ambiental

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: negociação ou redação de TAC em inquérito civil ou no curso de ACP; revisão de cláusulas; diagnóstico de TAC já firmado (cumprimento, aditamento, execução).
- Não usar:
  - defesa em ACP já ajuizada sem acordo: `amb-defesa-acao-civil-publica`;
  - regularização de reserva legal via CAR/PRA sem conflito com o MP: `amb-reserva-legal-e-car`;
  - embargos à execução do TAC: `civel-embargos-a-execucao` (use os fundamentos daqui);
  - acordo penal (transação, ANPP): `amb-defesa-crime-ambiental` e `penal-anpp`.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Quem é o tomador (MP, órgão ambiental, ente federativo) e qual o procedimento (número do inquérito civil, ACP).
2. Representação do lado privado: ato societário com poderes para assumir obrigações.
3. Fatos e área: diagnóstico técnico (laudo, PRAD, mapa, CAR).
4. O que é tecnicamente exequível e em quanto tempo (responsável técnico).
5. Há auto de infração, PRA, termo de compromisso ou processo penal sobre o mesmo fato?
6. Haverá transferência do imóvel ou reorganização societária no horizonte?

## Prazo e contagem
- Não há prazo legal para firmar o TAC; o prazo relevante é o do cronograma e o da resposta à proposta do MP (fixado no procedimento).
- Execução da multa do TAC por descumprimento de obrigação ambiental: o STJ tratou a multa como cláusula penal (sanção civil), afastou a Súmula 467 e reconheceu a imprescritibilidade (REsp 2.091.242).
- Obrigações do TAC sem conteúdo de reparação ambiental: prazo quinquenal por analogia ao art. 21 da Lei 4.717/1965 (AREsp 1.941.907).
- Prazos processuais da execução: `prazos-processuais`.

## Estrutura do documento
Partes e legitimidade → considerandos (fatos e procedimento) → objeto → obrigações de fazer e não fazer com cronograma → medidas compensatórias/indenizatórias → fiscalização e relatórios → multas → hipóteses de caso fortuito e revisão → efeitos sobre o procedimento → eficácia executiva e foro. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Só órgãos públicos legitimados tomam compromisso (Lei 7.347, art. 5º, § 6º); associação não firma TAC com eficácia executiva.
- O TAC tem eficácia de título executivo extrajudicial; homologado em juízo, passa a ser título judicial (CPC, art. 515, II; AgInt no REsp 1.520.347).
- Regulamentação do MP sobre TAC (Resolução CNMP 179/2017): conteúdo não conferido em fonte oficial [VERIFICAR antes de citar].
- Obrigação é *propter rem*: a venda do imóvel não extingue a obrigação de reflorestar prevista em TAC (AgInt no AREsp 1.995.069).

## Fundamentos verificados
- Lei 7.347/1985, art. 5º, § 6º.
- Lei 9.605/1998, art. 79-A — termo de compromisso com órgão do SISNAMA: título executivo, prazo de 90 dias a 3 anos prorrogável, cronograma e multas que não superem o investimento, suspensão das sanções administrativas, rescisão por descumprimento.
- Lei 12.651/2012, art. 59, §§ 3º a 5º (termo do PRA) e art. 60 (suspensão da punibilidade dos crimes dos arts. 38, 39 e 48 da Lei 9.605).
- TAC é ato jurídico perfeito; o Código Florestal de 2012 não retroage para alterar TAC anterior: AgInt nos EDcl no REsp 1.817.291 e AgInt no AREsp 2.123.237.
- Majoração judicial da multa do TAC exige fundamentação: AREsp 1.701.224.
- Execução individual de TAC sobre direitos individuais homogêneos: REsp 2.100.105.
Detalhe em [fundamentos](references/fundamentos.md).

## Cláusulas essenciais
- Objeto delimitado (área, coordenadas, fatos) e cláusula de que o TAC encerra a apuração daqueles fatos no procedimento (arquivamento do inquérito civil ou extinção da ACP).
- Obrigações com marcos mensuráveis (área replantada, taxa de sobrevivência, laudos de monitoramento).
- Responsável técnico e aprovação do PRAD pelo órgão ambiental competente.
- Multa por item descumprido, proporcional e com teto; notificação prévia e prazo de cura antes da exigência.
- Caso fortuito, força maior e atraso do órgão licenciador como causas de suspensão do cronograma.
- Revisão por fato técnico superveniente (ex.: área não regenera por causa alheia).
- Destino de valores indenizatórios (fundo do art. 13 da LACP ou projeto específico).
- Cláusula de sucessão em caso de alienação do imóvel.
- Ressalva expressa de que o TAC não importa confissão para fins penais ou administrativos (negociar; o MP pode recusar).

## Checklist pré-assinatura
- [ ] Tomador é órgão público legitimado
- [ ] Signatário privado com poderes societários
- [ ] Cronograma validado pelo responsável técnico
- [ ] Multas proporcionais, com prazo de cura e teto
- [ ] Efeito sobre inquérito civil/ACP expresso
- [ ] Relação com auto de infração, PRA e processo penal mapeada
- [ ] Sucessão e transferência do imóvel tratadas

## Erros a evitar
- Assumir cronograma inexequível para encerrar logo o inquérito: a multa é executável e, se ambiental, imprescritível.
- Supor que o TAC extingue automaticamente o processo penal ou o auto de infração: cada esfera tem regra própria (Lei 9.605, art. 79-A; Lei 12.651, art. 60 só alcança arts. 38, 39 e 48).
- Invocar regras mais brandas do Código Florestal de 2012 para rever TAC anterior a ele.
- Vender o imóvel sem tratar a obrigação no contrato de compra e venda.

## Integração com o núcleo
`prazos-processuais`, `juros-e-correcao` (atualização de valores), `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`; minuta contratual: `contratos-elaboracao-de-contrato`.

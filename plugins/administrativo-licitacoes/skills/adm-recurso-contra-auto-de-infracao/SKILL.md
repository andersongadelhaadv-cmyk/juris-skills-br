---
name: adm-recurso-contra-auto-de-infracao
description: >
  Redige defesa e recurso administrativo contra auto de infração e multa
  aplicados no exercício do poder de polícia (vigilância sanitária, fiscalização
  municipal, posturas, metrologia, agências e conselhos), com base na Lei
  9.784/1999 (arts. 2º, 38, 50, 56 a 66, 68 e 69), na prescrição da Lei
  9.873/1999 no âmbito federal e na vedação de depósito prévio (Súmula Vinculante
  21). Use quando o usuário pedir defesa contra auto de infração, recurso contra
  multa administrativa, interdição, apreensão, embargo de estabelecimento,
  prescrição intercorrente da multa ou revisão de sanção administrativa.
metadata:
  area: administrativo-licitacoes
  tipo_peca: recurso
  verificado_em: 2026-11-25
---
# Defesa e recurso contra auto de infração administrativo

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: auto de infração ou decisão sancionadora de órgão ou entidade no exercício do poder de polícia (multa, advertência, interdição, apreensão, suspensão de atividade), na fase de defesa ou de recurso.
- Lei específica manda: a Lei 9.784/1999 só se aplica subsidiariamente a processos com rito próprio (art. 69). Antes de redigir, identificar a lei e o regulamento do setor (trânsito, ambiental, sanitário, consumidor, regulatório, estatuto municipal) e usar os prazos dele [VERIFICAR: rito setorial].
- Não usar:
  - autuação tributária: `trib-defesa-administrativa-e-carf`;
  - multa contratual ou sanção a licitante: `adm-defesa-em-processo-sancionador-licitacao`;
  - servidor público em PAD: `adm-defesa-em-pad`;
  - processo da ANPD: `digital-defesa-em-processo-sancionador-anpd`;
  - prazo recursal perdido: `adm-anulacao-de-ato-por-autotutela`; via judicial: `adm-acao-anulatoria-de-ato-administrativo` ou `adm-mandado-de-seguranca`.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Auto de infração completo: órgão, agente autuante, data, local, descrição da conduta, dispositivo legal infringido, penalidade proposta.
2. Data da ciência (pessoal, postal, edital, eletrônica) e prazo indicado no auto.
3. Lei e regulamento do setor; se o ente é federal, estadual ou municipal.
4. Versão do cliente sobre os fatos e provas (fotos, laudos, licenças, notas, testemunhas).
5. Datas do fato, da autuação, de cada ato do processo e da última movimentação (prescrição e intercorrente).
6. Antecedentes do autuado e circunstâncias atenuantes.
7. Exigência de depósito, caução ou pagamento para recorrer, se houver.

## Prazo e contagem
- Recurso: 10 dias da ciência ou divulgação oficial da decisão, salvo lei específica (Lei 9.784/1999, art. 59); decisão em 30 dias, prorrogáveis uma vez (§§ 1º e 2º).
- Contagem da Lei 9.784/1999: exclui o dia do começo, inclui o do vencimento; prorroga se o vencimento cair em dia sem expediente; prazos em dias são contínuos (art. 66). Não aplicar dias úteis do CPC sem previsão.
- Prescrição federal: 5 anos da prática do ato ou da cessação da infração permanente ou continuada (Lei 9.873/1999, art. 1º); intercorrente com processo parado por mais de 3 anos (§ 1º); interrupções do art. 2º. Execução da multa federal: 5 anos após a constituição definitiva (art. 1º-A). Multa ambiental: Súmula 467/STJ.
- Estados e Municípios: lei local [VERIFICAR: a Lei 9.873/1999 rege a Administração federal].
- Revisão de sanção a qualquer tempo por fato novo (art. 65). Conferir com `prazos-processuais`.

## Estrutura da peça (resumo; detalhe em [estrutura](references/estrutura.md))
Endereçamento (autoridade que decidiu, com pedido de reconsideração em 5 dias ou de encaminhamento) → tempestividade → efeito suspensivo → preliminares (prescrição, nulidade do auto, cerceamento) → mérito → dosimetria subsidiária → provas → pedidos.

## Requisitos e preliminares
- Recurso por requerimento com os fundamentos e documentos (art. 60), dirigido à autoridade que decidiu; se não reconsiderar em 5 dias, encaminha à superior (art. 56, § 1º).
- Não se exige caução salvo lei (art. 56, § 2º); exigência de depósito prévio para recorrer é inconstitucional (Súmula Vinculante 21) e ilegítima (Súmula 373/STJ).
- Efeito suspensivo: em regra não há; pedir com base em prejuízo de difícil reparação (art. 61, parágrafo único).
- Garantias nos processos sancionadores: comunicação, alegações finais, provas e recurso (art. 2º, parágrafo único, X); prova só recusada por decisão fundamentada (art. 38, § 2º).
- Decisão sancionadora motivada com fatos e fundamentos (art. 50, II e V).
- Agravamento no recurso exige ciência prévia ao recorrente para alegações (art. 64, parágrafo único).
- Recurso endereçado ao órgão errado: a autoridade indica o competente e devolve o prazo (art. 63, § 1º).

## Fundamentos verificados (resumo; detalhe em [fundamentos](references/fundamentos.md))
- CF, art. 5º, LIV e LV.
- Lei 9.784/1999: arts. 2º, 3º, 26, 38, 50, 56, 58 a 61, 63 a 66, 68, 69. Súmula 633/STJ.
- Lei 9.873/1999: arts. 1º, 1º-A e 2º.
- LINDB, art. 22, §§ 2º e 3º.
- Súmula Vinculante 21; Súmula 373/STJ; Súmula 467/STJ.

## Pedidos e requerimentos
- Efeito suspensivo (art. 61, parágrafo único), com suspensão da exigibilidade e de medidas acessórias.
- Reconsideração pela autoridade ou encaminhamento à instância superior.
- Reconhecimento da prescrição (inclusive intercorrente) e arquivamento.
- Nulidade do auto ou da decisão por vício formal, falta de motivação ou cerceamento.
- No mérito, insubsistência do auto (fato não ocorreu, atipicidade, excludente).
- Subsidiariamente, conversão em advertência ou redução da multa pelos critérios do art. 22, § 2º, da LINDB e da lei do setor.
- Produção das provas especificadas; restituição de valor pago, com atualização pelo núcleo `juros-e-correcao`.

## Checklist pré-protocolo
- [ ] Lei e regulamento do setor identificados; prazo próprio conferido
- [ ] Data de ciência e contagem em dias corridos (ou conforme a lei específica)
- [ ] Prescrição e intercorrente calculadas com as datas do processo
- [ ] Auto conferido: agente competente, descrição do fato, dispositivo infringido
- [ ] Provas anexadas e especificadas
- [ ] Pedido de efeito suspensivo fundamentado
- [ ] Depósito prévio recusado com SV 21, se exigido
- [ ] Dosimetria subsidiária

## Erros a evitar
- Contar o prazo em dias úteis por analogia ao CPC e perder o recurso.
- Aplicar a Lei 9.784/1999 quando a lei do setor tem rito e prazo próprios.
- Pagar a multa com desconto sem avaliar a renúncia ao recurso prevista na norma setorial.
- Deixar de pedir efeito suspensivo e sofrer inscrição em dívida ativa durante o recurso.
- Alegar só mérito e esquecer prescrição intercorrente e vícios do auto.

## Integração com o núcleo
`prazos-processuais`, `juros-e-correcao`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

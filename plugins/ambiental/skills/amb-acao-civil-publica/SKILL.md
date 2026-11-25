---
name: amb-acao-civil-publica
description: >
  Redige ação civil pública ambiental para reparação de dano coletivo ao meio
  ambiente (Lei 7.347/1985; Lei 6.938/1981, art. 14, § 1º; CF, art. 225, § 3º),
  com obrigação de fazer/não fazer cumulada com indenização, dano moral coletivo
  e tutela de urgência. Use quando o usuário (associação, Defensoria, ente
  público ou advogado de legitimado) pedir ACP por desmatamento, poluição,
  ocupação de APP, descarte irregular de resíduos, dano a unidade de
  conservação ou recomposição de área degradada.
metadata:
  area: ambiental
  tipo_peca: inicial
  verificado_em: 2026-11-25
---
# Ação civil pública ambiental

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: dano ao meio ambiente como bem difuso (flora, fauna, água, solo, ar, paisagem), com pedido de recomposição, cessação da atividade e indenização ao fundo do art. 13 da Lei 7.347/1985.
- Não usar:
  - prejuízo próprio de vítima identificada (lavoura, imóvel, saúde, pesca): `amb-indenizacao-dano-ambiental-individual`;
  - defesa do réu: `amb-defesa-acao-civil-publica`;
  - acordo extrajudicial com o MP ou órgão público: `amb-termo-ajustamento-conduta`;
  - anulação de ato lesivo pelo cidadão: `adm-acao-popular`;
  - responsabilidade do Estado como foco principal: `adm-responsabilidade-civil-do-estado`.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Quem é o autor e por que é legitimado (art. 5º): estatuto da associação, data de constituição (mínimo de 1 ano, salvo dispensa do § 4º) e finalidade ambiental.
2. Local exato do dano (coordenadas, matrícula, CAR, bacia) — define o foro (art. 2º).
3. O que foi degradado, quando, em que extensão, e se o dano continua.
4. Quem causou, quem se beneficia, quem é o proprietário/possuidor atual e os anteriores, e se houve omissão de fiscalização.
5. Provas já existentes: autos de infração, laudos, imagens de satélite, inquérito civil, licenças (ou a falta delas).
6. Houve TAC, termo de compromisso ou PRA sobre a mesma área?

## Prazo e contagem
- A pretensão de reparação civil do dano ambiental é imprescritível (Tema 999/STF). Pedidos acessórios de outra natureza podem ter regime próprio [VERIFICAR caso a caso via `verificacao-de-citacoes`].
- Prazos processuais em dias úteis: `prazos-processuais`.

## Estrutura da peça
Endereçamento (foro do local do dano) → legitimidade e interesse → fatos e prova técnica → responsabilidade objetiva e risco integral → solidariedade e natureza *propter rem* → dano material ecológico, interinos e dano moral coletivo → inversão do ônus → tutela de urgência → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Competência: foro do local do dano, funcional (art. 2º); Justiça Federal se houver interesse da União, autarquia federal ou bem federal.
- Polo passivo: poluidor direto e indireto (Lei 6.938, art. 3º, IV); proprietário atual e/ou anteriores (Súmula 623 e Tema 1.204/STJ); ente público omisso na fiscalização (Súmula 652/STJ: solidário, execução subsidiária).
- MP intervém como fiscal da lei se não for autor (art. 5º, § 1º).
- Sem adiantamento de custas; associação só paga honorários se houver má-fé (art. 18).

## Fundamentos verificados
- CF, art. 225, *caput* e § 3º; art. 129, III.
- Lei 6.938/1981: art. 3º (II, III, IV), art. 4º, VII, art. 14, § 1º (responsabilidade independente de culpa).
- Lei 7.347/1985: arts. 1º, I, 2º, 3º, 4º, 5º, 11, 12, 13, 18, 21.
- Súmulas 613 (sem fato consumado), 618 (inversão do ônus), 623 (*propter rem*), 629 (cumulação fazer/não fazer + indenizar) e 652 do STJ; Tema 1.204/STJ; Tema 999/STF.
- Risco integral e irrelevância de medidas mitigadoras: REsp 2.102.646 (STJ, 4ª T., 2026).
- Dano moral coletivo ambiental aferido de forma objetiva e *in re ipsa*: AgInt no REsp 2.233.780 (STJ, 1ª T., 2026).
- Dano notório dispensa perícia e admite inversão quanto ao nexo: REsp 2.065.347 (STJ, 2ª T., 2024).
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Tutela de urgência (art. 12 da LACP; CPC, art. 300): paralisação da atividade, proibição de novas intervenções, indisponibilidade de bens se houver risco de dissipação, multa diária (art. 11).
- Obrigação de fazer: PRAD aprovado pelo órgão ambiental, com cronograma e responsável técnico.
- Obrigação de não fazer: abster-se de explorar, construir ou suprimir.
- Indenização pelos danos irreversíveis e interinos (período entre o dano e a recuperação), revertida ao fundo do art. 13.
- Dano moral coletivo.
- Inversão do ônus da prova (Súmula 618).
- Juros e correção: núcleo `juros-e-correcao`.

## Checklist pré-protocolo
- [ ] Legitimidade comprovada (estatuto, ata, pré-constituição ou pedido de dispensa)
- [ ] Foro do local do dano e justiça competente conferidos
- [ ] Todos os responsáveis no polo (direto, indireto, proprietário atual/anterior, ente omisso)
- [ ] Prova técnica mínima juntada (laudo, imagem, auto de infração)
- [ ] Pedidos de fazer, não fazer e indenizar cumulados (Súmula 629)
- [ ] Tutela com prazo, multa e medida de execução concreta
- [ ] Verificado se há TAC/PRA anterior (litispendência, interesse, execução direta)
- [ ] Juros/correção remetidos ao núcleo

## Erros a evitar
- Pedir só indenização em dinheiro quando a recomposição *in natura* é possível — a reparação prioriza a restauração.
- Esquecer o dano interino e o dano moral coletivo, que não se confundem com a recomposição.
- Aceitar a tese do fato consumado ou da licença como excludente (Súmula 613; risco integral).
- Incluir o ente público como devedor principal: a execução contra ele é subsidiária (Súmula 652).
- Ajuizar ACP para direito exclusivamente individual de quem pode demandar sozinho.

## Integração com o núcleo
`juros-e-correcao`, `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`; tutela: `civel-tutela-provisoria`.

---
name: amb-recurso-no-licenciamento
description: >
  Redige impugnação e recurso administrativo no licenciamento ambiental: pedido
  de revisão de condicionantes, recurso contra alteração de condicionante,
  contra indeferimento de licença ou contra suspensão ou cancelamento de
  licença, com base na Lei 15.190/2025 (Lei Geral do Licenciamento Ambiental),
  na LC 140/2011, na Lei 9.784/1999 e na Resolução CONAMA 237/1997. Use quando
  o empreendedor quiser contestar condicionante abusiva ou inexequível, exigência
  de complementação repetida, indeferimento de LP, LI, LO ou LAU, demora na
  análise, suspensão ou cancelamento da licença, ou questionar a competência do
  órgão licenciador.
metadata:
  area: ambiental
  tipo_peca: recurso
  verificado_em: 2026-11-25
---
# Impugnação e recurso no licenciamento ambiental

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: dentro do processo de licenciamento, contra ato do órgão licenciador que fixa, altera ou mantém condicionante, indefere licença, suspende ou cancela licença, ou exige complementações fora da lei.
- Não usar:
  - atividade já operando sem licença e que quer se regularizar → `amb-licenca-de-operacao-corretiva`;
  - auto de infração por descumprir condicionante → `amb-defesa-auto-de-infracao`;
  - ilegalidade provada por documentos, com urgência ou após o recurso → `amb-mandado-de-seguranca-licenciamento`;
  - impugnação de terceiro (vizinho, associação) contra licença concedida → ação civil pública ou ação popular (`adm-acao-popular`); esta skill é do empreendedor.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Ato impugnado na íntegra (licença com condicionantes, parecer técnico, ofício de indeferimento, de suspensão ou de cancelamento) e data de ciência ou de emissão.
2. Tipo de licença, procedimento (trifásico, bifásico, LAU, LAC) e data de abertura do processo — antes ou depois da vigência da Lei 15.190/2025 (art. 60).
3. Ente licenciador e por que ele é (ou não) o competente (LC 140/2011, arts. 7º a 9º e 13).
4. Estudos entregues (EIA/RIMA, RCA, outros) e histórico de exigências de complementação, com datas.
5. Para condicionante: por que é ilegal, desproporcional, sem nexo com o impacto ou inexequível — com parecer técnico próprio.
6. Para suspensão/cancelamento: qual hipótese o órgão invocou e o que houve de contraditório.
7. Prejuízo da execução imediata (obra parada, prazo contratual, financiamento).
8. Legislação estadual ou municipal de licenciamento aplicável.

## Prazo e contagem
- **Revisão de condicionantes:** até 30 dias da emissão da licença, de forma fundamentada; resposta motivada no mesmo prazo (Lei 15.190/2025, art. 14, § 6º).
- **Alteração de condicionante ou negativa de pedido de alteração:** recurso em 30 dias, respondido no mesmo prazo (art. 16, § 2º).
- **Indeferimento, suspensão, cancelamento e demais decisões:** a Lei 15.190/2025 não traz prazo geral visível de recurso contra a decisão da licença. No âmbito federal, aplica-se subsidiariamente a Lei 9.784/1999 (10 dias, art. 59); nos estados e municípios, a lei local. Confira sempre o regulamento do órgão.
- Contagem: `prazos-processuais`. Vigência da Lei 15.190/2025: 180 dias da publicação (art. 67); processos em curso adaptam-se nas etapas seguintes (art. 60, parágrafo único).

## Estrutura da peça
Endereçamento → tempestividade e cabimento → pedido de efeito suspensivo/sobrestamento → síntese do licenciamento → preliminares (competência, contraditório) → mérito por condicionante ou fundamento → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Efeito suspensivo:** a autoridade pode dar efeito suspensivo ao pedido de revisão, mantendo a condicionante sobrestada (art. 14, § 7º), e pode sobrestar a condicionante enquanto pende o recurso do art. 16 (§ 3º). Peça sempre, com prova do dano. Subsidiariamente, Lei 9.784/1999, art. 61, parágrafo único.
- **Competência:** licenciamento por um único ente (LC 140/2011, art. 13); os demais podem se manifestar sem vincular (§ 1º). Exigência de licença paralela por outro ente é tese preliminar.
- **Exigências de complementação:** devem ser feitas de uma só vez, salvo fato novo (LC 140/2011, art. 14, § 1º); suspendem o prazo de análise (§ 2º).
- **Demora:** prazos máximos de análise no art. 47 da Lei 15.190/2025 (ex.: 3 meses para LI, LO, LOC e LAU). O decurso não gera licença tácita, mas, a pedido do empreendedor, instaura a competência supletiva (art. 47, § 3º; LC 140/2011, art. 14, § 3º), com aproveitamento dos estudos já aceitos (art. 47, § 4º).
- **Suspensão ou cancelamento:** só nas hipóteses do art. 16 da Lei 15.190/2025 (omissão relevante ou falsa informação, graves riscos supervenientes, acidente com dano significativo), por decisão motivada, com ampla defesa e contraditório (§ 4º). A Resolução CONAMA 237/1997, art. 19, traz rol semelhante (inclui violação de condicionantes) — verifique qual regra vale para o processo.
- **Renovação:** pedida com 120 dias de antecedência, a licença fica prorrogada até a decisão (LC 140/2011, art. 14, § 4º; Lei 15.190/2025, art. 7º).

## Fundamentos verificados
- Lei 15.190/2025, arts. 3º, 5º, 7º, 14, §§ 6º e 7º, 16, 47, 60 e 67.
- LC 140/2011, arts. 13 e 14; Lei 6.938/1981, art. 10.
- Lei 9.784/1999, arts. 2º, 50, 56, 59, 61 e 64; CF, art. 5º, LV.
- Resolução CONAMA 237/1997, arts. 1º, 8º, 18 e 19 (aplicação a conferir diante da Lei 15.190/2025).
- Súmula 613/STJ (sem fato consumado em direito ambiental) — limite às teses do empreendedor.
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Efeito suspensivo ou sobrestamento da condicionante/decisão até o julgamento.
- Exclusão, readequação ou substituição de cada condicionante impugnada (com proposta alternativa tecnicamente fundamentada).
- Anulação do indeferimento por falta de motivação ou por exigência fora do termo de referência, com retomada da análise.
- Revogação da suspensão ou do cancelamento, ou substituição por medida menos gravosa.
- Reconhecimento da prorrogação automática da licença (renovação tempestiva).
- Subsidiariamente: abertura de prazo para complementação, com lista única de exigências.

## Checklist pré-protocolo
- [ ] Data de emissão/ciência e prazo (30 dias ou o da lei aplicável) conferidos
- [ ] Regime aplicável definido: processo anterior ou posterior à vigência da Lei 15.190/2025; lei estadual/municipal
- [ ] Cada condicionante impugnada com fundamento jurídico e técnico próprio
- [ ] Parecer técnico do empreendedor juntado (ART do responsável)
- [ ] Efeito suspensivo pedido com prova do dano
- [ ] Competência do licenciador conferida (LC 140/2011)
- [ ] Histórico de exigências de complementação em tabela
- [ ] Alternativa ao judicial avaliada (MS: 120 dias da ciência)

## Erros a evitar
- Perder os 30 dias da revisão de condicionantes e só discutir quando autuado por descumpri-las.
- Impugnar a condicionante só no jurídico, sem laudo técnico: o órgão decide com base técnica.
- Sustentar licença tácita pelo decurso do prazo: a lei nega expressamente.
- Invocar a Resolução CONAMA 237/1997 contra a Lei 15.190/2025 em processo novo: a lei prevalece.
- Pedir "fato consumado" para manter atividade irregular (Súmula 613/STJ).
- Ignorar ações de controle de constitucionalidade contra a Lei 15.190/2025 [VERIFICAR: situação no STF na data do protocolo].

## Integração com o núcleo
`prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

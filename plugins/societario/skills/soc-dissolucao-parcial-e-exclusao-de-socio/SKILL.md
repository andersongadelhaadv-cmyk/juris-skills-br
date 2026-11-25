---
name: soc-dissolucao-parcial-e-exclusao-de-socio
description: >
  Redige ação de dissolução parcial de sociedade com apuração de haveres
  (retirada, recesso, morte ou exclusão de sócio), a exclusão extrajudicial
  por justa causa em reunião ou assembleia e a defesa do sócio excluído, com
  base nos arts. 1.028 a 1.038, 1.077, 1.085 e 1.086 do Código Civil e nos
  arts. 599 a 609 do CPC. Use quando o usuário pedir dissolução parcial,
  retirada de sócio, apuração de haveres, exclusão de sócio por falta grave,
  sócio remisso, haveres de herdeiros de sócio falecido, impugnação de
  balanço/laudo de haveres, ou anular exclusão de sócio.
metadata:
  area: societario
  tipo_peca: inicial
  verificado_em: 2026-11-25
---
# Dissolução parcial, apuração de haveres e exclusão de sócio

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: (a) sócio quer sair e os demais não formalizam; (b) recesso de dissidente; (c) morte de sócio sem ingresso dos sucessores; (d) exclusão judicial por falta grave ou incapacidade superveniente (art. 1.030); (e) exclusão extrajudicial pela maioria do capital (art. 1.085); (f) só apurar haveres de quem já saiu; (g) ex-cônjuge ou ex-companheiro apurando haveres (art. 600, parágrafo único, do CPC).
- Não usar: dissolução total e liquidação da sociedade (arts. 1.033 a 1.038 do CC; peça própria a partir de `civel-peticao-inicial`); partilha de quotas no divórcio sem apuração contra a sociedade (`familia-divorcio`); inventário (`sucessoes-inventario-judicial`); contestação genérica (`civel-contestacao`); recurso (`civel-apelacao`, `civel-agravo-de-instrumento`).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Contrato social consolidado (exigido pelo art. 599, § 1º, do CPC) e alterações; tipo societário e prazo (determinado ou indeterminado).
2. Cláusulas sobre retirada, exclusão por justa causa, critério e forma de pagamento de haveres.
3. Fato gerador e data: notificação de retirada (data de recebimento), deliberação dissidente, óbito, ata de exclusão.
4. Para exclusão: fatos concretos de falta grave, provas, convocação da reunião e ciência do acusado.
5. Últimos balanços, DREs, distribuições de lucros, pró-labore, contas bancárias; quem detém a contabilidade.
6. Número de sócios (com 2 sócios a reunião é dispensada — art. 1.085, parágrafo único).
7. Se S.A. fechada: participação dos autores (mínimo de 5% para o pedido do art. 599, § 2º).

## Prazo e contagem
- Retirada imotivada em sociedade por prazo indeterminado: notificação com 60 dias de antecedência (art. 1.029); os demais podem optar pela dissolução em 30 dias da notificação (parágrafo único). Data da resolução: 60º dia após o recebimento da notificação pela sociedade (art. 605, II, do CPC).
- Recesso em alteração, fusão ou incorporação: 30 dias da reunião (art. 1.077); data da resolução: recebimento da notificação do dissidente (art. 605, III).
- Retirado/recedente pode ajuizar se a alteração não for formalizada em 10 dias (art. 600, IV).
- Citação: 15 dias para concordar ou contestar (art. 601).
- Pagamento dos haveres: 90 dias da liquidação, salvo acordo ou contrato (art. 1.031, § 2º; art. 609 do CPC).
- Prescrição da pretensão de apuração de haveres por exclusão: decenal (AgInt no REsp 2.066.005).
- Prazo para anular deliberação de exclusão extrajudicial: não conferido [VERIFICAR: prazo decadencial/prescricional aplicável]. Contagem processual: `prazos-processuais`.

## Estrutura da peça
Endereçamento → partes (todos os sócios e, se conveniente, a sociedade — art. 601) → fatos e fato gerador com data → cabimento e legitimidade (art. 599 e 600) → resolução da sociedade em relação ao sócio → data da resolução (art. 605) → critério de apuração (contrato ou art. 606) → depósito do incontroverso (art. 604, § 1º) → perícia → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Legitimidade ativa conforme o art. 600 (espólio, sucessores após partilha, sociedade, retirante, excluído). O sócio excluído pode propor ação só para apurar haveres (REsp 2.203.772).
- Polo passivo: sócios e sociedade; citados todos os sócios, a sociedade é dispensada, mas fica vinculada (art. 601, parágrafo único).
- Exclusão judicial: iniciativa da maioria dos demais sócios, por falta grave ou incapacidade superveniente (art. 1.030). A quebra da affectio societatis, sozinha, não basta; é preciso falta grave concreta (REsp 2.142.834).
- Exclusão extrajudicial (art. 1.085): maioria de mais da metade do capital; atos de inegável gravidade que ponham em risco a continuidade da empresa; previsão contratual de exclusão por justa causa; reunião/assembleia especialmente convocada com ciência do acusado em tempo hábil para defesa (salvo sociedade com 2 sócios). Documento assinado por todos os sócios que preveja a exclusão pode valer como aditamento ao contrato social (REsp 2.170.665).
- Sócio remisso: notificado, 30 dias de mora; maioria pode excluí-lo ou reduzir a quota ao realizado (art. 1.004, parágrafo único).
- Exclusão de pleno direito: falido e quota liquidada a pedido de credor (art. 1.030, parágrafo único).

## Fundamentos verificados
- CC arts. 1.004, 1.028 a 1.032, 1.077, 1.085, 1.086.
- CPC arts. 599 a 609.
- Súmula 265/STF (balanço não aprovado pelo sócio que saiu não prevalece na apuração).
- STJ: contrato omisso → balanço de determinação; fluxo de caixa descontado e expectativa de lucro futuro excluídos (REsp 2.063.134); fundo de comércio integra o balanço de determinação (REsp 2.174.631).
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Decretação da resolução da sociedade em relação ao sócio (ou declaração da exclusão/retirada) com ordem de alteração contratual e averbação.
- Fixação da data da resolução conforme o art. 605.
- Definição do critério: o do contrato social; na omissão, balanço de determinação a preço de saída, incluídos intangíveis (art. 606).
- Depósito judicial da parte incontroversa e levantamento imediato (art. 604, §§ 1º e 2º).
- Perícia contábil por especialista em avaliação de sociedades (art. 606, parágrafo único); exibição dos livros e documentos.
- Lucros, juros sobre capital próprio e pró-labore até a data da resolução (art. 608); depois, só correção e juros — taxa e termo inicial pelo núcleo `juros-e-correcao`.
- Pagamento na forma do contrato ou em 90 dias (art. 609; art. 1.031, § 2º).
- Na defesa da sociedade: pedido de indenização compensável com os haveres (art. 602).
- Consenso unânime: sem honorários e custas rateadas pelo capital (art. 603, § 1º).

## Checklist pré-protocolo
- [ ] Contrato social consolidado juntado (art. 599, § 1º)
- [ ] Fato gerador e data da resolução provados (notificação com recebimento, ata, certidão de óbito)
- [ ] Todos os sócios no polo passivo
- [ ] Cláusula de haveres transcrita; se omissa, pedido do art. 606
- [ ] Exclusão extrajudicial: cláusula de justa causa, convocação, ciência, quórum e ata conferidos
- [ ] Pedido de depósito do incontroverso
- [ ] Juros/correção remetidos ao núcleo

## Erros a evitar
- Pedir exclusão só por "quebra da affectio societatis", sem falta grave concreta.
- Excluir extrajudicialmente sem cláusula de justa causa no contrato social ou sem dar ao acusado ciência e chance de defesa.
- Pedir avaliação por fluxo de caixa descontado quando o contrato é omisso.
- Usar balanço ordinário não aprovado pelo sócio que saiu (Súmula 265/STF).
- Errar a data da resolução (cada hipótese do art. 605 tem marco próprio) — ela muda o valor.
- Deixar de requerer exibição da contabilidade em poder dos remanescentes.

## Integração com o núcleo
`juros-e-correcao`, `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`, `civel-tutela-provisoria` (afastamento de administrador ou bloqueio de lucros, se houver urgência).

---
name: penal-agravo-em-execucao
description: >
  Redige agravo em execução penal e contrarrazões (Lei 7.210/1984, art. 197),
  processado pelo rito do recurso em sentido estrito, contra decisões do juiz da
  execução sobre progressão, regressão, falta grave, remição, livramento, indulto,
  unificação e detração. Use quando o usuário pedir agravo em execução, agravo da
  LEP, recurso contra decisão da VEP, contra indeferimento de progressão,
  reconhecimento de falta grave, regressão ou perda de dias remidos.
metadata:
  area: penal
  tipo_peca: recurso-penal
  verificado_em: 2026-11-01
---
# Agravo em execução penal

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: qualquer decisão do juiz da execução (LEP 197; competências do art. 66): progressão e regressão, falta grave e suas consequências, remição, saída temporária, livramento, indulto e comutação, unificação e soma de penas, detração, conversões, monitoração eletrônica.
- Não usar: decisões do juízo do conhecimento (apelação, RESE); urgência extrema com ilegalidade evidente pode justificar HC concomitante (ver `penal-habeas-corpus`).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Decisão agravada e data da intimação da defesa.
2. Guia de execução, cálculo de pena (atestado de pena a cumprir) e boletim/atestado de conduta.
3. Procedimento disciplinar (PAD), se houver falta grave: termo de declarações, defesa técnica, decisão administrativa.
4. Laudo de exame criminológico, se realizado.
5. Datas-base (prisão, última falta, última progressão) e frações aplicadas.

## Prazo e contagem
- 5 dias (Súmula 700 do STF), contínuos (CPP 798), a contar da intimação.
- Rito do RESE: razões em 2 dias (CPP 588), retratação em 2 dias (589). Use `prazos-processuais`.
- Sem efeito suspensivo (LEP 197). Para urgência, pedir efeito ativo ao relator ou impetrar HC.

## Estrutura da peça
Resumo (detalhe em [estrutura](references/estrutura.md)): interposição ao juízo da execução com pedido de retratação; razões ao tribunal: cabimento, síntese da execução, fundamentos, pedidos.

## Requisitos e preliminares
- Falta grave exige PAD instaurado pelo diretor, com defesa técnica (Súmula 533 STJ); crime doloso como falta grave dispensa o trânsito em julgado da condenação (Súmula 526 STJ).
- Efeitos da falta grave: interrompe o prazo da progressão (LEP 112 §6º; Súmula 534 STJ); não interrompe para livramento (Súmula 441 STJ) nem para indulto ou comutação (Súmula 535 STJ).
- Regressão exige oitiva prévia do condenado (LEP 118 §2º).
- Exame criminológico obrigatório pela Lei 14.843/2024 (LEP 112 §1º): o STJ trata como novatio legis in pejus, inaplicável a crimes anteriores; para estes, só por decisão concreta (Súmula 439 STJ).
- Frações do art. 112 mudaram em 2026 (Leis 15.358 e 15.402): ver `penal-progressao-de-regime`.

## Fundamentos verificados
Resumo (detalhe em [fundamentos](references/fundamentos.md)): LEP 50, 52, 57, 66, 112, 118, 126, 127, 197; CPP 581 a 592 (rito); Súmula 700 STF; Súmulas 439, 441, 491, 526, 533, 534, 535 STJ; Súmula Vinculante 26; STJ sobre a irretroatividade do exame criminológico obrigatório.

## Pedidos e requerimentos
- Retratação.
- Reforma: concessão da progressão; afastamento da falta grave (nulidade do PAD, atipicidade, desclassificação para média ou leve); restabelecimento dos dias remidos ou redução da perda (LEP 127, até 1/3); fixação correta da data-base; dispensa do exame criminológico para fatos anteriores à Lei 14.843/2024.
- Subsidiário: anulação para nova decisão fundamentada.

## Checklist pré-protocolo
- [ ] Prazo de 5 dias contado da intimação da defesa.
- [ ] Cálculo de pena revisado: data do crime (define a lei aplicável), frações, datas-base.
- [ ] PAD analisado: defesa técnica presente? Oitiva? Prazo?
- [ ] Fração do art. 112 identificada conforme a data do fato (lei mais grave não retroage — CF 5º XL).
- [ ] Pedido de retratação feito.
- [ ] Precedentes conferidos em `verificacao-de-citacoes`.

## Erros a evitar
- Interpor RESE ou apelação em vez de agravo.
- Usar o prazo de 10 ou 15 dias: são 5 (Súmula 700 STF).
- Aplicar frações de 2026 a crimes anteriores quando forem mais gravosas.
- Aceitar a interrupção do prazo de livramento por falta grave (vedado pela Súmula 441 STJ).
- Não impugnar a perda de dias remidos acima de 1/3 ou sem fundamentação (LEP 127).

## Integração com o núcleo
- `prazos-processuais`: 5 dias para interpor; 2 dias para razões.
- `verificacao-de-citacoes`, `fidelidade-factual` (datas do cálculo), `estilo-forense`.
- Skills relacionadas: `penal-progressao-de-regime`, `penal-livramento-condicional`.

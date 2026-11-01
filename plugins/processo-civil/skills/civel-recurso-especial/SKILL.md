---
name: civel-recurso-especial
description: >
  Redige recurso especial cível ao STJ (CF art. 105, III; CPC art. 1.029), com
  tópico obrigatório de relevância da questão federal (CPC art. 1.035-A, Lei
  15.484/2026), prequestionamento (art. 1.025) e prevenção dos óbices das
  Súmulas 5, 7, 211 e 518 do STJ e 282, 284 e 356 do STF. Use quando o usuário
  pedir recurso especial, REsp, recorrer ao STJ, violação de lei federal,
  dissídio jurisprudencial ou demonstração de relevância.
metadata:
  area: processo-civil
  tipo_peca: recurso-especial
  verificado_em: 2026-11-01
---
# Recurso especial (cível)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: acórdão de TJ ou TRF, em única ou última instância, que contrarie ou negue vigência a lei federal (alínea "a"), julgue válido ato de governo local contestado em face de lei federal ("b") ou divirja de outro tribunal na interpretação da lei federal ("c").
- Não usar: acórdão de turma recursal de juizado (Súmula 203 do STJ — cabe RE, se houver questão constitucional, Súmula 640 do STF); decisão monocrática ainda recorrível por agravo interno (esgotar a instância); matéria só constitucional (`civel-recurso-extraordinario`).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
- Acórdão recorrido, acórdão dos ED e datas de publicação.
- Dispositivos de lei federal violados e onde foram debatidos (peças e ED).
- Para a alínea "c": acórdão paradigma de outro tribunal, com fonte.
- Valor da causa atualizado (presunção de relevância acima de 500 salários mínimos) e dados sobre impacto econômico, social, político ou jurídico.
- Se o acórdão também tem fundamento constitucional autônomo (exige RE simultâneo — Súmula 126 do STJ).

## Prazo e contagem
- 15 dias úteis (art. 1.003, §5º); ED interrompem.
- Feriado local: comprovar no ato (art. 1.003, §6º).
- Preparo (custas do STJ e porte, quando devido) no ato (art. 1.007).
- Relevância: exigida em tópico próprio nos recursos contra acórdãos publicados a partir da vigência da Lei 15.484/2026 (30 dias após a publicação de 04/08/2026, ou seja, 03/09/2026; regra de transição no art. 4º da lei). Use `prazos-processuais`.

## Estrutura da peça
Interposição ao presidente/vice do tribunal de origem → razões: cabimento e tempestividade → **relevância da questão federal (tópico específico)** → exposição do fato e do direito → prequestionamento → violação ao art. 1.022 (se houver omissão) → violação de lei federal (por dispositivo) → dissídio (cotejo analítico) → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Petição distinta do RE, com fato e direito, cabimento e razões de reforma (art. 1.029).
- **Relevância**: tópico específico e fundamentado (art. 1.035-A, §2º); sem ele, inadmissão (§3º). Presumida nas hipóteses do art. 105, §3º, da CF (§4º) — mesmo assim, demonstrar o enquadramento.
- Prequestionamento: matéria efetivamente decidida; se o tribunal se omitiu após ED, alegar violação ao art. 1.022 para o STJ aplicar o art. 1.025.
- Questão de direito: não pedir reexame de prova (Súmula 7) nem reinterpretação de cláusula (Súmula 5).
- Indicar o dispositivo e como foi violado (Súmula 284 do STF); atacar todos os fundamentos suficientes (Súmula 283 do STF).

## Fundamentos verificados
CF art. 105, III e §§2º-3º (EC 125/2022); CPC arts. 1.025, 1.029, 1.030, 1.035-A, 1.042; Súmulas 5, 7, 13, 83, 126, 203, 211, 518 do STJ; 282, 283, 284, 356 do STF. Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Admissão e remessa ao STJ; reconhecimento da relevância.
- Provimento para reformar o acórdão (ou anular, se acolhida violação ao art. 1.022).
- Efeito suspensivo, se necessário, por requerimento próprio (art. 1.029, §5º).
- Juros e correção, se objeto do recurso: tese conforme `juros-e-correcao`.

## Checklist pré-protocolo
- [ ] Tópico "Da relevância da questão de direito federal infraconstitucional" presente, específico e fundamentado.
- [ ] Enquadramento em presunção do art. 105, §3º, da CF verificado (valor da causa > 500 SM, jurisprudência dominante contrariada etc.).
- [ ] Cada dispositivo violado indicado com artigo, parágrafo e inciso.
- [ ] Prequestionamento demonstrado (trecho do acórdão) ou violação ao art. 1.022 alegada.
- [ ] Nenhum pedido de reexame de prova ou cláusula.
- [ ] Dissídio com cotejo analítico e fonte do paradigma (art. 1.029, §1º); paradigma de outro tribunal (Súmula 13).
- [ ] RE simultâneo, se houver fundamento constitucional autônomo.
- [ ] Preparo, procuração (Súmula 115) e feriado local.

## Erros a evitar
- Omitir o tópico de relevância (inadmissão por vício formal — art. 1.035-A, §3º).
- Relevância genérica ("a questão é importante para todos"): mostre o efeito para além das partes.
- Alegar violação de súmula (Súmula 518) ou de dispositivo constitucional no REsp.
- Dissídio com julgado do mesmo tribunal (Súmula 13) ou superado pela jurisprudência do STJ (Súmula 83).
- Esquecer de alegar violação ao art. 1.022 quando o tribunal não enfrentou o ponto (Súmula 211).
- Confundir os agravos: inadmissão pelo art. 1.030, V → agravo do art. 1.042; negativa por precedente qualificado → agravo interno.

## Integração com o núcleo
- `prazos-processuais` para prazo, interrupção e regra de transição da relevância.
- `verificacao-de-citacoes` para paradigmas e precedentes (obrigatório).
- `juros-e-correcao` quando o recurso discutir encargos.
- `fidelidade-factual` para trechos do acórdão.
- `estilo-forense` na revisão.

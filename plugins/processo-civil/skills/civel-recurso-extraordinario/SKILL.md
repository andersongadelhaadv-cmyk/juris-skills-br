---
name: civel-recurso-extraordinario
description: >
  Redige recurso extraordinário cível ao STF (CF art. 102, III; CPC arts. 1.029
  e 1.035), com preliminar formal e fundamentada de repercussão geral e
  prequestionamento da questão constitucional. Use quando o usuário pedir
  recurso extraordinário, RE, recorrer ao STF, violação da Constituição,
  repercussão geral ou RE contra acórdão de turma recursal de juizado.
metadata:
  area: processo-civil
  tipo_peca: recurso-extraordinario
  verificado_em: 2026-11-01
---
# Recurso extraordinário (cível)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: causa decidida em única ou última instância (inclusive turma recursal de juizado — Súmula 640 do STF) em que a decisão contrarie a Constituição (alínea "a"), declare inconstitucional tratado ou lei federal ("b"), julgue válida lei ou ato local contestado em face da Constituição ("c") ou lei local contestada em face de lei federal ("d").
- Não usar: ofensa reflexa (que depende de interpretar lei infraconstitucional antes); reexame de prova (Súmula 279); acórdão que defere liminar (Súmula 735).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
- Acórdão recorrido e acórdão dos ED, com datas.
- Dispositivos constitucionais violados e onde foram debatidos.
- Existência de tema de repercussão geral já afetado ou julgado sobre a matéria.
- Se há fundamento infraconstitucional autônomo (exige REsp simultâneo).

## Prazo e contagem
- 15 dias úteis (art. 1.003, §5º); ED interrompem; feriado local comprovado no ato (§6º).
- Preparo no ato (art. 1.007). Use `prazos-processuais`.

## Estrutura da peça
Interposição ao presidente/vice do tribunal de origem → razões: cabimento e tempestividade → **preliminar de repercussão geral** → exposição do fato e do direito → prequestionamento → violação constitucional (por dispositivo) → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Petição distinta do REsp (art. 1.029).
- Repercussão geral demonstrada pelo recorrente (CF art. 102, §3º; CPC art. 1.035, §2º): questões relevantes do ponto de vista econômico, político, social ou jurídico que ultrapassem o interesse subjetivo (§1º). Presumida quando o acórdão contraria súmula ou jurisprudência dominante do STF ou declarou inconstitucional tratado ou lei federal (§3º).
- Prequestionamento: Súmulas 282 e 356 do STF; art. 1.025 do CPC.
- Ofensa direta à Constituição.

## Fundamentos verificados
CF art. 102, III e §3º; CPC arts. 1.025, 1.029, 1.030, 1.035, 1.042; Súmulas 279, 282, 283, 284, 356, 640 e 735 do STF. Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Reconhecimento da repercussão geral, admissão e remessa ao STF.
- Provimento para reformar o acórdão.
- Efeito suspensivo, por requerimento próprio (art. 1.029, §5º), se necessário.
- Distinção, se houver tema de repercussão geral cuja tese não se aplique ao caso.

## Checklist pré-protocolo
- [ ] Preliminar de repercussão geral em tópico próprio, com fundamentos concretos.
- [ ] Hipótese de presunção (art. 1.035, §3º) verificada.
- [ ] Tema de repercussão geral pesquisado e passado por `verificacao-de-citacoes`.
- [ ] Dispositivo constitucional indicado e ofensa direta demonstrada.
- [ ] Prequestionamento (trecho do acórdão) ou ED opostos.
- [ ] REsp simultâneo, se houver fundamento infraconstitucional autônomo.
- [ ] Preparo, procuração e feriado local.

## Erros a evitar
- Repercussão geral genérica ou ausente: o recurso não é conhecido.
- Ofensa reflexa apresentada como direta.
- Pedir revaloração de prova (Súmula 279).
- Não atacar todos os fundamentos suficientes (Súmula 283).
- Ignorar que, negada a repercussão geral no tema, o tribunal de origem nega seguimento aos recursos sobrestados (art. 1.035, §8º).

## Integração com o núcleo
- `prazos-processuais` para prazo e interrupção.
- `verificacao-de-citacoes` para temas de repercussão geral e precedentes do STF.
- `fidelidade-factual` para trechos do acórdão.
- `estilo-forense` na revisão.

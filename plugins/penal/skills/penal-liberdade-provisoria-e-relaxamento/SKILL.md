---
name: penal-liberdade-provisoria-e-relaxamento
description: >
  Redige pedidos de relaxamento de prisão ilegal, liberdade provisória com ou sem
  fiança, revogação ou substituição de preventiva por cautelares e manifestação
  em audiência de custódia (CF art. 5º, LXV e LXVI; CPP arts. 282, 310, 312 a 321).
  Use quando o usuário pedir relaxamento de flagrante, liberdade provisória,
  revogação da preventiva, revisão nonagesimal, cautelares do art. 319, fiança,
  prisão domiciliar ou roteiro para audiência de custódia.
metadata:
  area: penal
  tipo_peca: requerimento
  verificado_em: 2026-11-01
---
# Liberdade provisória, relaxamento e revogação da preventiva

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Relaxamento: prisão ilegal na origem ou na forma (flagrante inexistente, auto viciado, custódia não realizada no prazo — CPP 310 §4º).
- Liberdade provisória: flagrante formalmente válido, mas ausentes os requisitos da preventiva (CPP 310, III; 321).
- Revogação/substituição: preventiva já decretada, sem fundamento atual (CPP 282 §5º, 316) ou suficiente cautelar diversa (319) ou domiciliar (318).
- Não usar: se o juízo já indeferiu e nada mudou — vá direto ao `penal-habeas-corpus` (ou RESE pela acusação, CPP 581 V).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Auto de prisão em flagrante ou decisão que decretou/manteve a preventiva (íntegra).
2. Ata da audiência de custódia, se realizada; data e hora da prisão.
3. Antecedentes (FAC), processos e inquéritos em curso; reincidência.
4. Comprovantes de residência, trabalho, filhos ou dependentes, saúde.
5. Data da última revisão da preventiva (CPP 316 p.ú.).

## Prazo e contagem
- Sem prazo preclusivo; pedido cabível a qualquer tempo e reiterável diante de fatos novos.
- Audiência de custódia em até 24 h da prisão (CPP 310 caput, redação da Lei 15.358/2026, por videoconferência; presencial só em força maior, §13). Passadas 24 h após esse prazo sem motivação idônea, a prisão torna-se ilegal (§4º).
- Revisão obrigatória da preventiva a cada 90 dias, de ofício, pelo órgão que a decretou (CPP 316 p.ú.).

## Estrutura da peça
Resumo (detalhe em [estrutura](references/estrutura.md)): endereçamento; síntese da prisão; ilegalidade (relaxamento); ausência dos requisitos da preventiva; suficiência de cautelares; condições pessoais; pedidos em ordem de preferência.

## Requisitos e preliminares
- Preventiva exige: prova da existência do crime, indício suficiente de autoria e perigo gerado pela liberdade (CPP 312), uma das hipóteses do 313 e fatos novos ou contemporâneos (312 §2º; 315 §1º). Gravidade abstrata não basta (312 §4º, Lei 15.272/2025).
- Proibida a preventiva como antecipação de pena ou como consequência automática da denúncia (313 §2º).
- Vedada a decretação de ofício: depende de requerimento do MP, do querelante, do assistente ou de representação policial (CPP 282 §2º e 311).
- Atenção às vedações legais e aos fatores que "recomendam" a conversão (310 §§2º e 5º; 312 §3º, Lei 15.272/2025): enfrente-os um a um, porque o juiz é obrigado a examiná-los (310 §6º).
- Fiança: inafiançáveis os crimes do art. 323 (racismo, tortura, tráfico, terrorismo, hediondos, ação de grupos armados); mesmo assim cabe liberdade provisória sem fiança.

## Fundamentos verificados
Resumo (detalhe em [fundamentos](references/fundamentos.md)): CF 5º LXV e LXVI; CPP 3-B (juiz das garantias), 282, 310, 311, 312, 313, 315, 316, 318, 319, 321, 323, 324; Súmulas 21 e 52 do STJ; STJ sobre a revisão nonagesimal.

## Pedidos e requerimentos
1. Relaxamento da prisão (se ilegal), com expedição de alvará.
2. Subsidiariamente, liberdade provisória sem fiança, ou com fiança em valor compatível com a renda.
3. Subsidiariamente, substituição por cautelares do art. 319, indicando quais e por quê bastam.
4. Subsidiariamente, prisão domiciliar (CPP 318), com prova idônea do requisito.
5. Se preventiva já decretada: revisão imediata (316 p.ú.) e revogação.

## Checklist pré-protocolo
- [ ] Data e hora da prisão e da audiência de custódia conferidas (CPP 310 e §4º).
- [ ] Decisão de conversão transcrita nos trechos que mostram a falta de fatos concretos.
- [ ] Enfrentados os §§2º e 5º do art. 310 e o §3º do art. 312.
- [ ] Hipótese do art. 313 checada (pena máxima > 4 anos, reincidência, violência doméstica etc.).
- [ ] Cautelares do art. 319 sugeridas de forma concreta (endereço para comparecimento, horário de recolhimento).
- [ ] Documentos pessoais juntados (residência, trabalho, filhos, saúde).
- [ ] Data da última revisão da preventiva registrada.
- [ ] Precedentes adicionais conferidos em `verificacao-de-citacoes`.

## Erros a evitar
- Confundir relaxamento (ilegalidade) com liberdade provisória (ausência de necessidade): pedir ambos, em ordem.
- Argumentar só com "primariedade e residência fixa" sem atacar o fundamento concreto da decisão.
- Ignorar as alterações de 2025-2026 (Lei 15.272/2025 nos arts. 310 e 312; Lei 15.358/2026 no 310 e no 313, V; Lei 15.487/2026 no 313, VI).
- Pedir fiança em crime inafiançável em vez de liberdade provisória sem fiança.
- Sustentar que a falta de revisão em 90 dias gera soltura automática: o STJ tem decidido que não (ver fundamentos).

## Integração com o núcleo
- `prazos-processuais`: prazos da custódia e da revisão.
- `verificacao-de-citacoes`: precedentes sobre fundamentação, excesso de prazo, domiciliar.
- `fidelidade-factual`: datas e horas de prisão e de audiência.
- `estilo-forense`: peça curta, pedidos escalonados.
- Skill relacionada: `penal-habeas-corpus` quando o pedido for indeferido.

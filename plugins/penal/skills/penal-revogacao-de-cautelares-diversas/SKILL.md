---
name: penal-revogacao-de-cautelares-diversas
description: >
  Redige pedido de revogação, substituição ou flexibilização de medidas
  cautelares diversas da prisão já impostas a investigado ou réu solto (CPP
  arts. 282 e 319): monitoração eletrônica, recolhimento noturno, proibição de
  ausentar-se da comarca, suspensão de função, comparecimento periódico. Use
  quando o usuário pedir para tirar a tornozeleira, revogar ou abrandar
  cautelares, autorizar viagem ou mudança de endereço, impugnar cautelar sem
  fundamento atual ou desproporcional pelo tempo, ou pedir detração do
  recolhimento noturno.
metadata:
  area: penal
  tipo_peca: requerimento
  verificado_em: 2026-11-25
---
# Revogação, substituição e flexibilização de cautelares diversas da prisão

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: cliente em liberdade, submetido a uma ou mais medidas do art. 319 do CPP, e a defesa quer (a) revogá-las por falta de motivo atual, (b) substituí-las por medida mais branda, (c) flexibilizá-las (horário, perímetro, autorização de viagem, trabalho noturno), ou (d) impugnar a imposição por falta de contraditório prévio ou de fundamentação concreta.
- Não usar: cliente preso (relaxamento, liberdade provisória, revogação da preventiva: `penal-liberdade-provisoria-e-relaxamento`); medidas protetivas da Lei Maria da Penha (`penal-maria-da-penha-medidas-protetivas`); pedido negado ou cautelar mantida com restrição à locomoção que justifique levar ao tribunal (`penal-habeas-corpus`); cautelares na execução da pena (`penal-agravo-em-execucao`).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Decisão que impôs as cautelares: data, juízo, quais medidas, fundamentos usados.
2. Houve intimação da defesa para se manifestar antes (CPP 282 §3º)? Havia urgência declarada?
3. Fase do feito: inquérito, denúncia recebida, instrução, sentença; data prevista de audiências.
4. Tempo de cumprimento até hoje e histórico de cumprimento (relatórios da central de monitoração, comparecimentos, ausência de incidentes).
5. Fatos novos favoráveis: encerramento da instrução, testemunhas já ouvidas, emprego, tratamento de saúde, filhos, necessidade de viagem (com datas e comprovantes).
6. Pena máxima do crime imputado e perspectiva de pena e regime (proporcionalidade).
7. Prejuízo concreto causado pela medida (perda de emprego, impossibilidade de estudo, lesões pelo equipamento).

## Prazo e contagem
- Não há prazo legal para pedir revogação: o juiz pode revogar ou substituir a qualquer tempo quando faltar motivo para a manutenção (CPP 282 §5º).
- A revisão a cada 90 dias do art. 316, parágrafo único, foi escrita para a preventiva; sua extensão às cautelares diversas não é automática. O STJ examina a duração e a atualidade das cautelares caso a caso (ver fundamentos), por isso o argumento é proporcionalidade e contemporaneidade, não "prazo vencido".
- Recurso: o art. 581, V, do CPP lista decisões sobre fiança, preventiva, liberdade provisória e flagrante; contra o indeferimento de revogação de cautelar diversa, a via usual é o habeas corpus quando houver restrição à liberdade de locomoção [VERIFICAR: cabimento de RESE na sua jurisprudência local]. Prazos: `prazos-processuais`.

## Estrutura da peça
Endereçamento ao juízo do feito → síntese das medidas e de quanto tempo já duram → cumprimento integral → ausência de motivo atual (282 §5º) ou desproporção (282 I e II) → pedido principal (revogação) e subsidiários (substituição, flexibilização pontual) → detração, se houver recolhimento noturno. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Necessidade e adequação são requisitos de toda cautelar (CPP 282, I e II): se a finalidade que justificou a medida (ex.: proteger a instrução) se esgotou, a medida perde a base.
- Contraditório prévio: em regra, a parte contrária é intimada para se manifestar em 5 dias antes da decisão; a exceção exige urgência ou risco de ineficácia, justificados concretamente (CPP 282 §3º). Ausência sem justificativa é argumento de nulidade.
- Vedação de decretação de ofício: a redação vigente do 282 §2º exige requerimento das partes ou, na investigação, representação policial ou requerimento do MP.
- Infrações sem pena privativa de liberdade não admitem cautelares (CPP 283 §1º).
- Fundamentação concreta e contemporânea é exigida para "qualquer outra cautelar" (CPP 315 §1º).

## Fundamentos verificados
- CPP 282 (I, II, §§ 1º a 6º), 283 §1º, 315, 319 (I a IX), 320, 321.
- STJ, Tema Repetitivo 1155: o período de recolhimento noturno e nos dias de folga é detraído da pena, sem exigência de monitoração eletrônica associada.
- STJ, AgRg no HC 876.451: monitoramento revogado por excesso de prazo e desproporcionalidade (ordem de ofício).
- STJ, REsp 2.242.932: monitoramento exige fundamentação concreta, necessidade, adequação e contemporaneidade.
- Contraponto: STJ, AgRg na Pet 16.308 e AgRg na CauInomCrim 95 mantiveram cautelares longas; o tempo, sozinho, não basta.
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
1. Revogação integral das medidas (CPP 282 §5º).
2. Subsidiariamente, substituição por medida menos gravosa, nomeando qual (ex.: comparecimento mensal no lugar da monitoração).
3. Subsidiariamente, flexibilização específica: horário de recolhimento compatível com o trabalho, ampliação do perímetro, autorização de viagem com datas, destino e endereço.
4. Ofício à central de monitoração para retirada do equipamento, se deferido.
5. Registro do período de recolhimento noturno para futura detração (Tema 1155).

## Checklist pré-protocolo
- [ ] Cópia da decisão que impôs as medidas e de eventuais prorrogações
- [ ] Relatório de cumprimento da central de monitoração ou certidão de comparecimentos
- [ ] Linha do tempo: imposição, atos de instrução já realizados, próximos atos
- [ ] Prova de cada fato novo (contrato de trabalho, matrícula, laudo, passagem)
- [ ] Pedido subsidiário concreto, não genérico
- [ ] Contraditório prévio verificado (282 §3º)
- [ ] Prazos de eventual impugnação conferidos em `prazos-processuais`

## Erros a evitar
- Pedir revogação "pelo decurso de 90 dias" como se o art. 316, parágrafo único, valesse automaticamente para cautelares diversas.
- Repetir os argumentos já rejeitados sem fato novo; o juiz responde com "inalterado o quadro".
- Omitir o pedido subsidiário: o juiz que não revoga muitas vezes flexibiliza.
- Pedir viagem sem datas, endereço e comprovante.
- Esquecer de requerer o registro do recolhimento noturno para a detração.

## Integração com o núcleo
`prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`. Pena e detração: `penal-dosimetria`.

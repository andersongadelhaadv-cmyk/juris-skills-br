---
name: penal-remicao-de-pena
description: >
  Redige pedido de reconhecimento e declaração de remição de pena por trabalho,
  estudo, leitura e aprovação em ENEM/ENCCEJA perante o juiz da execução (LEP
  arts. 126 a 130), com cálculo dos dias remidos e defesa contra a perda por
  falta grave (art. 127). Use quando o usuário pedir remição, contagem de dias
  remidos, remição por trabalho, por estudo, por leitura, por ENEM ou ENCCEJA,
  remição em prisão domiciliar ou cautelar, ou quiser saber quantos dias o
  cliente já remiu.
metadata:
  area: penal
  tipo_peca: requerimento
  verificado_em: 2026-11-25
---
# Remição de pena por trabalho e estudo

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: pedido em 1º grau ao juízo da execução para declarar dias remidos (LEP 126 §8º), corrigir o cálculo, incluir períodos omitidos pela unidade, reconhecer remição por leitura ou por aprovação em exame, ou limitar a perda de dias remidos por falta grave.
- Não usar: recorrer da decisão que negou ou cassou a remição (`penal-agravo-em-execucao`); progressão de regime que dependa dos dias remidos (`penal-progressao-de-regime`); livramento (`penal-livramento-condicional`); indulto ou comutação (`penal-indulto-e-comutacao`).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Regime atual e histórico (fechado, semiaberto, aberto, domiciliar, livramento, prisão cautelar).
2. Atestados de trabalho: período, função, jornada diária, se intra ou extramuros, quem fiscaliza.
3. Estudo: instituição, modalidade (presencial ou a distância), horas de frequência por mês, certificados de conclusão.
4. Leitura: projeto da unidade, obras, resenhas e avaliação da comissão.
5. Exames: ENEM ou ENCCEJA, áreas aprovadas, notas, ano; se já houve remição pelo mesmo exame.
6. Dias já declarados remidos pelo juízo e cálculo de pena atual (SEEU).
7. Faltas graves: data, PAD, decisão, quantos dias foram perdidos.

## Prazo e contagem
- Não há prazo para pedir: a remição é declarada pelo juiz, ouvidos MP e defesa (LEP 126 §8º); peça periodicamente, sem esperar o benefício seguinte.
- Fórmula: 1 dia de pena a cada 12 horas de frequência escolar divididas em no mínimo 3 dias; 1 dia de pena a cada 3 dias de trabalho (LEP 126 §1º). Conclusão de ensino fundamental, médio ou superior durante a pena acrescenta 1/3 às horas de estudo (§5º).
- Os dias remidos contam como pena cumprida para todos os efeitos (LEP 128).
- Agravo em execução contra a decisão: 5 dias (Súmula 700/STF); contagem em `prazos-processuais`.

## Estrutura da peça
Endereçamento ao juízo da execução → dados da execução → tabela de períodos e atividades → cálculo dia a dia → fundamento de cada modalidade → pedidos de declaração e de retificação do cálculo. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Quem pode remir: condenado em regime fechado ou semiaberto, por trabalho ou estudo (LEP 126); aberto, semiaberto e livramento pela frequência a curso regular ou profissionalizante (§6º); também na prisão cautelar (§7º) e no regime domiciliar (§9º, Lei 15.402/2026).
- Trabalho extramuros em regime fechado ou semiaberto remite (Súmula 562/STJ); estudo formal remite (Súmula 341/STJ).
- Jornada: o STJ calcula pelos dias efetivamente trabalhados, em jornada de 6 a 8 horas, incluídos domingos e feriados trabalhados; não soma horas de dias com jornada menor que 6 horas, salvo jornada especial autorizada (LEP 33, parágrafo único), em que contam os dias; horas além de 8 diárias podem gerar dia adicional; não há remição ficta por falta de trabalho oferecido.
- Comprovação: a unidade envia mensalmente o registro de dias e horas; quem estuda fora comprova frequência e aproveitamento por declaração da escola (LEP 129). Falta de fiscalização do trabalho é o motivo mais comum de indeferimento: junte atestado da autoridade administrativa.
- Falta grave: o juiz pode revogar **até** 1/3 dos dias remidos, recomeçando a contagem da data da infração (LEP 127); a perda exige decisão fundamentada e proporcional.

## Fundamentos verificados
- LEP 33, 66 III "c", 126 a 130, 197; CP 299 (falso atestado, por remissão do art. 130).
- Súmulas 341 e 562/STJ; Súmula 700/STF.
- STJ: Temas 1236 (estudo a distância), 1270 (ENEM parcial), 1278 (leitura), 1357 (ENEM e ENCCEJA por fatos geradores distintos); AgRg no AREsp 2.722.057; AgRg nos EDcl no REsp 1.893.570; AgRg no AREsp 2.356.272.
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
1. Declaração de X dias remidos no período tal (com tabela).
2. Requisição à unidade dos atestados faltantes (LEP 129), se houver lacuna.
3. Reconhecimento de remição por leitura ou por exame, nos termos das teses repetitivas.
4. Acréscimo de 1/3 pela conclusão de nível de ensino (LEP 126 §5º), quando cabível.
5. Retificação do cálculo de pena no SEEU, com nova data de benefícios.
6. Em caso de falta grave: perda inferior ao teto de 1/3, fundamentada.

## Checklist pré-protocolo
- [ ] Atestados assinados pela autoridade administrativa, mês a mês
- [ ] Tabela: período, atividade, dias ou horas, dias remidos
- [ ] Jornada conferida (6 a 8 horas; jornada especial autorizada?)
- [ ] Certificados com carga horária e instituição credenciada (EAD)
- [ ] Remição anterior pelo mesmo fato gerador excluída
- [ ] Cálculo atual de pena juntado
- [ ] Reflexo nos benefícios (progressão, livramento) apontado

## Erros a evitar
- Somar horas de dias com jornada inferior a 6 horas sem autorização de jornada especial.
- Pedir remição ficta porque a unidade não ofereceu trabalho.
- Pedir duas vezes pelo mesmo exame ou pelo mesmo curso.
- Aceitar a perda automática de 1/3 por falta grave sem impugnar a fundamentação.
- Deixar o pedido para a véspera da progressão: o juízo precisa ouvir o MP antes de declarar.

## Integração com o núcleo
`prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`. Cálculo é aritmético e determinístico: faça a conta por planilha, nunca por estimativa.

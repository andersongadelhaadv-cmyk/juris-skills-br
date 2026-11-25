---
name: penal-indulto-e-comutacao
description: >
  Redige pedido de indulto (extinção da pena) e de comutação (redução da pena)
  ao juiz da execução com base no decreto presidencial do ano (CF art. 84, XII;
  LEP arts. 187 a 193), com triagem de requisitos objetivos, vedações e falta
  grave no período do decreto. Use quando o usuário pedir indulto natalino,
  comutação de pena, extinção da pena pelo decreto, indulto humanitário por
  doença ou deficiência, indulto da multa, ou quiser saber se o cliente se
  enquadra no decreto vigente.
metadata:
  area: penal
  tipo_peca: requerimento
  verificado_em: 2026-11-25
---
# Indulto e comutação de pena

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Regra de ouro: o decreto do ano manda
O indulto coletivo e a comutação existem **só nos termos do decreto presidencial** (CF 84, XII). Cada decreto tem data-base, frações, vedações e regra de falta grave próprias. Abra o decreto no Planalto e confira artigo por artigo antes de redigir; nunca aplique as frações de um ano a outro.
- Último decreto conferido (25/11/2026): **Decreto 12.790, de 22/12/2025** (DOU 23/12/2025), data-base **25/12/2025**. O decreto natalino de 2026 ainda não havia sido publicado nesta data [VERIFICAR no Planalto a partir de dezembro de 2026]: quando sair, ele rege os fatos até a nova data-base, e esta skill deve ser revista.

## Quando usar / quando não usar
- Usar: pedido ao juízo da execução para declarar extinta a pena (indulto) ou ajustar a execução (comutação) com base no decreto (LEP 192 e 193); indulto da pena de multa; indulto humanitário por doença grave ou deficiência previsto no decreto.
- Não usar: recurso contra o indeferimento (`penal-agravo-em-execucao`); progressão (`penal-progressao-de-regime`); livramento (`penal-livramento-condicional`); remição (`penal-remicao-de-pena`); pedido individual de graça ao Presidente pelo Conselho Penitenciário (LEP 188 a 191) — trâmite administrativo diferente, não coberto aqui.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Guia(s) de execução: crimes, artigos, penas, datas dos fatos, trânsito em julgado.
2. Cálculo de pena com pena cumprida **até a data-base do decreto** (incluir prisão cautelar, domiciliar e dias remidos).
3. Reincidência (o decreto usa frações diferentes).
4. Crime com violência ou grave ameaça? Hediondo, tráfico, violência contra a mulher, organização criminosa, crime contra a administração ou outro da lista de vedações?
5. Acordo de colaboração premiada firmado?
6. Faltas graves: data e se foram reconhecidas pelo juízo nos 12 meses anteriores à data-base.
7. Situação pessoal que reduz frações no decreto: idade, gestação, filhos menores, deficiência, doença grave (com laudo).
8. Pena de multa: valor, inadimplência, capacidade econômica.

## Prazo e contagem
- Não há prazo para requerer; o decreto pode ser aplicado de ofício (Decreto 12.790/2025, arts. 15 e 17). Peça cedo: o decreto manda dar preferência ao incidente e decidir após MP e defesa no prazo sucessivo de 5 dias (art. 15 §4º).
- Requisitos temporais são aferidos **na data-base** do decreto; nada cumprido depois conta para aquele decreto.
- Agravo em execução contra a decisão: 5 dias (Súmula 700/STF); contagem em `prazos-processuais`.

## Estrutura da peça
Juízo da execução → identificação da execução e do decreto → enquadramento no artigo e inciso exatos → cálculo da fração na data-base → ausência de vedação → falta grave → pedido de declaração. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Vedação constitucional e legal: crimes hediondos, tortura, tráfico e terrorismo são insuscetíveis de graça ou anistia (CF 5º, XLIII) e de anistia, graça e indulto (Lei 8.072/1990, art. 2º, I). O decreto costuma ampliar a lista; leia o art. 1º do decreto vigente.
- Falta grave não interrompe o prazo para indulto ou comutação (Súmula 535/STJ); o que importa é a regra do próprio decreto (no Decreto 12.790/2025, sanção por falta grave reconhecida nos 12 meses anteriores à data-base, com contraditório; faltas posteriores à publicação não impedem — art. 6º).
- No Decreto 12.790/2025: sem exigência de exame criminológico (art. 8º); penas de infrações diversas somam-se até a data-base (art. 7º); a multa é alcançada nas hipóteses do art. 12, e o não pagamento da multa cumulada não impede o benefício (art. 4º).
- Efeitos: o indulto extingue os efeitos primários da condenação, não os secundários (Súmula 631/STJ) — avise o cliente que reincidência e efeitos extrapenais permanecem.
- Concedido o indulto, o juiz declara extinta a pena; na comutação, ajusta a execução (LEP 192); no indulto coletivo, pode agir de ofício ou por provocação (LEP 193).

## Fundamentos verificados
- CF 5º XLIII, 84 XII e parágrafo único; CP 107, II; LEP 187 a 197; Lei 8.072/1990, art. 2º, I.
- Decreto 12.790/2025 (arts. 1º, 4º, 6º a 9º, 12, 13, 15, 17).
- Súmulas 535 e 631/STJ; Súmula 700/STF.
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
1. Declaração do indulto, com extinção da pena (LEP 192; CP 107, II), indicando decreto, artigo e inciso.
2. Subsidiariamente, comutação na fração do decreto, com novo cálculo da pena remanescente.
3. Indulto da multa, nas hipóteses do decreto.
4. Requisição do cálculo atualizado e da certidão carcerária, se ausentes.
5. Vista ao MP e decisão no prazo do decreto.
6. Alvará de soltura ou baixa da execução, conforme o caso.

## Checklist pré-protocolo
- [ ] Texto do decreto vigente aberto no Planalto e artigo exato citado
- [ ] Cálculo da fração na data-base, mostrando a conta
- [ ] Cada crime checado contra a lista de vedações do decreto
- [ ] Colaboração premiada descartada
- [ ] Faltas graves no período do decreto verificadas
- [ ] Laudo médico atualizado, se indulto humanitário
- [ ] Cliente avisado dos efeitos secundários que permanecem (Súmula 631/STJ)

## Erros a evitar
- Citar fração de decreto de outro ano.
- Calcular a fração com pena cumprida depois da data-base.
- Tratar crime impeditivo em concurso como se não existisse (o decreto disciplina o concurso).
- Dizer ao cliente que o indulto "limpa a ficha".
- Deixar de pedir a comutação subsidiária quando o indulto não fecha.

## Integração com o núcleo
`prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`. Frações e datas são aritmética determinística: faça a conta por planilha.

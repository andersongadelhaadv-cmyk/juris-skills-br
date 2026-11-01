---
name: trabalhista-reclamacao
description: >
  Redige petição inicial trabalhista (reclamação) com pedidos certos, determinados
  e com valor (CLT art. 840 §1º), escolha de rito ordinário ou sumaríssimo
  (arts. 852-A e ss.), gratuidade (art. 790 §§3º-4º) e honorários de sucumbência
  (art. 791-A, com os efeitos da ADI 5766). Use quando o usuário pedir reclamação
  trabalhista, reclamatória, inicial trabalhista, ação trabalhista, petição inicial
  na Justiça do Trabalho, liquidar pedidos da inicial ou ajuizar contra ex-empregador.
metadata:
  area: trabalhista
  tipo_peca: inicial
  verificado_em: 2026-11-01
---
# Reclamação trabalhista (petição inicial)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: ação individual do trabalhador (ou de seus sucessores) contra empregador ou tomador, em rito ordinário, sumaríssimo ou sumário (alçada).
- Não usar: homologação de acordo extrajudicial (use `trabalhista-acordo-extrajudicial`); pedido focado só em rescisão indireta, vínculo, adicionais ou acidente (use a skill temática e traga para cá apenas a estrutura); ação de cumprimento ou dissídio coletivo.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
- Qualificação completa das partes; CNPJ e endereço correto da reclamada (no sumaríssimo não há citação por edital).
- Datas de admissão e saída, modalidade de extinção, função, último salário e composição da remuneração.
- Jornada real (entrada, saída, intervalo, dias), local de trabalho, norma coletiva aplicável.
- Lista de verbas pretendidas, com documentos (TRCT, holerites, cartões de ponto, CTPS digital, extratos FGTS).
- Situação econômica do reclamante (salário atual ou desemprego) para a gratuidade.
- Se há tomador de serviços, grupo econômico ou ente público no polo passivo.

## Prazo e contagem
- Prescrição: 5 anos contados do ajuizamento, limitada a 2 anos após o fim do contrato (CF art. 7º XXIX; CLT art. 11). Calcule as duas datas e informe ao usuário o marco quinquenal (Súmula 308 I do TST).
- Ação anterior arquivada interrompe a prescrição só para pedidos idênticos (CLT art. 11 §3º; Súmula 268 do TST).
- Pedido declaratório de anotação para fins previdenciários não prescreve (CLT art. 11 §1º).
- Prazos processuais em dias úteis (CLT art. 775); detalhe na skill `prazos-processuais`.

## Estrutura da peça
Endereçamento à Vara do Trabalho; qualificação; rito e valor da causa; gratuidade; fatos por contrato e por tema; fundamentos por pedido; rol de pedidos liquidados; honorários; requerimentos finais. Roteiro completo em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Pedido certo, determinado e com indicação de valor (CLT art. 840 §1º); o pedido sem valor é extinto sem mérito (§3º).
- Rito sumaríssimo quando a soma não exceder 40 salários mínimos na data do ajuizamento e não houver ente público da administração direta, autárquica ou fundacional (arts. 852-A e 852-B). No sumaríssimo, até duas testemunhas por parte (art. 852-H §2º).
- Causas até 2 salários mínimos: alçada da Lei 5.584/1970 (art. 2º §§3º-4º), sem recurso salvo matéria constitucional.
- Valor dos pedidos como estimativa: o TST discute a limitação da condenação aos valores da inicial (Tema 35 da tabela de IRR). Fazer ressalva expressa de que os valores são estimados [VERIFICAR: tese fixada no Tema 35 IRR antes de protocolar].

## Fundamentos verificados
- CLT arts. 840, 852-A a 852-I, 790 §§3º-4º, 791-A, 818, 11; CF art. 7º XXIX.
- Súmula 463 I do TST: para pessoa natural, basta a declaração de hipossuficiência (com poderes específicos na procuração).
- Honorários: 5% a 15% (art. 791-A). O §4º traz anotação de inconstitucionalidade pela ADI 5766 no texto compilado; aplica-se a condição suspensiva de exigibilidade ao beneficiário da gratuidade, sem cobrança automática com créditos obtidos no processo [VERIFICAR alcance exato do acórdão da ADI 5766].
- Detalhe e modo de uso em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Cada pedido com valor próprio e reflexos discriminados.
- Correção monetária e juros: requerer "na forma da tese vinculante do STF e da legislação vigente", aplicando a skill `juros-e-correcao`. Não escrever índice nem taxa na peça sem passar pelo núcleo.
- Gratuidade, honorários de sucumbência, notificação da reclamada, produção de provas (inclusive exibição de documentos sob as penas do art. 400 do CPC, quando cabível).

## Checklist pré-protocolo
- [ ] Prescrição bienal e quinquenal calculadas e indicadas.
- [ ] Todos os pedidos líquidos, com memória de cálculo anexa ou explicada.
- [ ] Soma dos pedidos confere com o valor da causa e com o rito escolhido.
- [ ] Endereço da reclamada conferido (sumaríssimo veda edital).
- [ ] Declaração de hipossuficiência assinada ou procuração com poderes específicos.
- [ ] Ressalva de valores estimados incluída.
- [ ] Juros e correção remetidos ao núcleo, sem taxa escrita.
- [ ] Documentos essenciais anexados e nomeados.

## Erros a evitar
- Pedido genérico ("diferenças a apurar") sem valor: risco de extinção do pedido.
- Somar reflexos em duplicidade (ex.: reflexo de horas extras em DSR e depois DSR majorado em férias sem critério).
- Escolher sumaríssimo com ente público no polo passivo.
- Escrever percentual fixo de juros ou índice superado.
- Afirmar como certa tese de IRR ou ADI sem verificação.

## Integração com o núcleo
`juros-e-correcao` (todos os pedidos condenatórios), `prazos-processuais` (prescrição e prazos), `verificacao-de-citacoes` (qualquer precedente acrescentado), `fidelidade-factual` (fatos só do que o usuário trouxe), `estilo-forense`.

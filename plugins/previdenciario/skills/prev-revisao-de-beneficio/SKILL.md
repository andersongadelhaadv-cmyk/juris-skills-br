---
name: prev-revisao-de-beneficio
description: >
  Avalia e redige ação de revisão de benefício do RGPS, começando pelo controle
  da decadência de 10 anos e da prescrição quinquenal (Lei 8.213/1991, art. 103;
  STF Tema 313), e filtra teses superadas como a revisão da vida toda (ADIs
  2110/2111; Tema 1102 STF). Use quando o usuário pedir revisão de aposentadoria,
  recálculo da RMI, inclusão de tempo ou salários, revisão por melhor benefício,
  decadência previdenciária ou "revisão da vida toda".
metadata:
  area: previdenciario
  tipo_peca: inicial
  verificado_em: 2026-11-01
---
# Revisão de benefício previdenciário

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: revisão para incluir período (comum, especial, rural) ou salários não considerados; correção de erro de cálculo; direito ao melhor benefício (STF Tema 334); revisão de atos de indeferimento/cessação.
- NÃO peticionar revisão da vida toda: a tese está SUPERADA (ver abaixo). Se o cliente pedir, explicar e recusar a propositura.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Carta de concessão (espécie, DIB, RMI, memória de cálculo) e data do primeiro pagamento.
2. Processo administrativo completo (para saber o que foi ou não levado ao INSS).
3. O que se quer incluir/corrigir e a prova.
4. Pedidos de revisão administrativa anteriores e decisões.
5. Simulação da nova RMI (sem simulação positiva não ajuizar).

## Prazo e contagem
- Decadência de 10 anos para revisar o ato de concessão, contada do dia 1º do mês seguinte ao do recebimento da primeira prestação (art. 103, I) ou da ciência da decisão administrativa de revisão (II). Na ADI 6096, o STF declarou inconstitucional o art. 24 da Lei 13.846/2019 na parte em que deu nova redação ao art. 103: não há decadência nem prescrição do fundo de direito contra indeferimento, cancelamento ou cessação; só prescrevem as parcelas anteriores ao quinquênio (STJ, AgInt no REsp 2.067.701).
- Benefícios anteriores à MP 1.523/1997: decadência contada a partir de 01/08/1997 (STF Tema 313).
- Indeferimento, cessação ou cancelamento: TNU Súmula 81 (não se submetem a prazo extintivo quanto ao fundo de direito).
- Prescrição das diferenças anteriores a 5 anos do ajuizamento (art. 103, p.ú.; STJ Súmula 85), ressalvados menores, incapazes e ausentes.

## Estrutura da peça   (detalhe em [estrutura](references/estrutura.md))
1. Competência e interesse (Tema 350: revisão pode ir direto a juízo, salvo fato novo).
2. Tempestividade: quadro de decadência.
3. O ato revisando e o erro.
4. Direito e prova.
5. Nova RMI simulada e diferenças.
6. Pedidos.

## Requisitos e preliminares
- Interesse de agir: revisão pode ser pedida diretamente em juízo, salvo se depender de matéria de fato não levada ao INSS (STF Tema 350, item III). Se o fato é novo (ex.: PPP obtido depois), requerer antes ao INSS.
- Revisões cabíveis (exemplos a avaliar no caso): inclusão de período ou salário omitido; reconhecimento de tempo especial/rural; melhor benefício (Tema 334 STF); correção de erro material de cálculo; inclusão de verbas reconhecidas em sentença trabalhista (sentença homologatória de acordo e anotação dela decorrente só valem como início de prova se houver elementos contemporâneos, STJ Tema 1188). Em todos os casos, prova documental contemporânea de cada período ou remuneração.
- Revisões superadas (não ajuizar): revisão da vida toda. O STF declarou constitucional o art. 3º da Lei 9.876/1999 (ADIs 2110 e 2111) e, no Tema 1102, fixou que o segurado não pode optar pela regra do art. 29, I e II, da Lei 8.213, com modulação: irrepetibilidade dos valores recebidos por decisões até 05/04/2024 e dispensa de sucumbência nas ações pendentes até essa data.
- Riscos: a revisão pode reduzir o benefício (reformatio) se houver erro a favor do segurado em outro ponto: simular tudo.

## Fundamentos verificados   (detalhe em [fundamentos](references/fundamentos.md))
- Lei 8.213, arts. 29, 29-A, 103.
- STF Temas 313, 334, 350 e 1102; ADI 6096; ADIs 2.110 e 2.111; STJ Súmula 85 e Tema 1188; TNU Súmula 81.

## Pedidos e requerimentos
- Revisão da RMI com inclusão de X, desde a DIB, observada a prescrição quinquenal.
- Pagamento das diferenças conforme `juros-e-correcao`.
- Manutenção do benefício atual se a revisão resultar desfavorável (pedido expresso).

## Checklist pré-protocolo
- [ ] Data do primeiro pagamento e prazo decenal conferidos.
- [ ] Tese não consta na lista de teses superadas.
- [ ] Simulação da nova RMI positiva e anexada.
- [ ] Fato novo levado previamente ao INSS, se houver.
- [ ] Prescrição quinquenal considerada no cálculo das diferenças.
- [ ] Juros e correção remetidos ao núcleo.

## Erros a evitar
- Ajuizar revisão da vida toda ou "aguardar mudança" de tese: superada pelo STF.
- Calcular decadência a partir da DIB em vez do mês seguinte ao primeiro pagamento.
- Confundir decadência (fundo do direito, revisão) com prescrição (parcelas).
- Ajuizar sem simulação e descobrir RMI menor.

## Integração com o núcleo
- `juros-e-correcao` (obrigatório para diferenças).
- `prazos-processuais` para decadência e prescrição.
- `verificacao-de-citacoes` para qualquer tese de revisão nova (conferir se não foi superada).
- `fidelidade-factual` (carta de concessão e cálculos); `estilo-forense`.

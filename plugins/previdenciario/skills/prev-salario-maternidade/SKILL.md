---
name: prev-salario-maternidade
description: >
  Prepara a ação de concessão de salário-maternidade contra o INSS (Lei
  8.213/1991, arts. 25, III, 26, VI, 39, p.ú., e 71 a 73), por parto, adoção ou
  guarda para adoção, inclusive da segurada desempregada no período de graça, da
  contribuinte individual, da facultativa e da segurada especial rural. Use quando
  o usuário pedir salário-maternidade negado, licença-maternidade paga pelo INSS,
  benefício da mãe desempregada, da trabalhadora rural, de adotante, do pai
  sobrevivente após óbito da mãe ou cálculo do valor do benefício.
metadata:
  area: previdenciario
  tipo_peca: inicial
  verificado_em: 2026-11-25
---
# Salário-maternidade

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: indeferimento do salário-maternidade pelo INSS por falta de qualidade de segurada, de carência, de prova da atividade rural, ou por entender que o pagamento cabia ao empregador; adoção ou guarda para adoção; óbito da segurada ou do segurado com direito ao benefício (art. 71-B).
- Empregada com vínculo ativo cujo empregador não pagou a licença: a discussão trabalhista (estabilidade, salários) é da Justiça do Trabalho; aqui só o benefício contra o INSS.
- Compensação do salário-maternidade pela empresa ou contribuição patronal sobre ele: tema tributário (`trib-*`).
- Prova do trabalho rural em ação de aposentadoria: `prev-tempo-rural-e-segurado-especial` (esta skill usa os mesmos critérios de prova, aplicados ao período curto do benefício).
- Ainda sem requerimento ao INSS: `prev-requerimento-administrativo`.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Fato gerador e data: parto (certidão de nascimento), natimorto, adoção ou termo de guarda para adoção (idade da criança).
2. Categoria da segurada na data do fato: empregada, doméstica, avulsa, contribuinte individual, MEI, facultativa, segurada especial, desempregada.
3. CNIS e CTPS: último vínculo, data e forma de desligamento, últimas contribuições.
4. Se desempregada: data da última contribuição e prova de desemprego (seguro-desemprego, ausência de vínculo) para o período de graça.
5. Número de contribuições antes do fato (para quem exige carência) e se houve perda e nova filiação.
6. Segurada especial: documentos rurais com data, autodeclaração, cadastro no CNIS, composição do grupo familiar.
7. Requerimento ao INSS: NB, DER, decisão e motivo.
8. Houve internação prolongada da mãe ou do recém-nascido após o parto?

## Prazo e contagem
- O art. 71-D (decadência em 180 dias), incluído pela MP 871/2019, não consta da Lei 13.846/2019, que a converteu; o texto compilado do Planalto ainda o exibe sem nota. Não aceite indeferimento por "decadência" sem conferir a vigência [VERIFICAR: situação do art. 71-D no texto oficial].
- Não há decadência para concessão (STF Tema 313); prescrevem as parcelas vencidas há mais de 5 anos do ajuizamento (art. 103, p.ú.), ressalvados menores e incapazes. Como o benefício dura 120 dias, ação proposta mais de 5 anos após o fim do período tende a estar integralmente prescrita.
- Duração: 120 dias, com início entre 28 dias antes do parto e a data do parto (art. 71). Adoção ou guarda: 120 dias (art. 71-A).
- Prazos processuais: `prazos-processuais`.

## Estrutura da peça   (detalhe em [estrutura](references/estrutura.md))
1. Competência (JEF/Vara Federal) e interesse de agir (requerimento e indeferimento — STF Tema 350).
2. Fato gerador e data.
3. Qualidade de segurada na data do fato (vínculo ativo ou período de graça).
4. Carência ou isenção, conforme a categoria.
5. Valor do benefício (arts. 72 e 73).
6. Pedidos.

## Requisitos e preliminares
- Carência: isenta para empregada, avulsa e doméstica (art. 26, VI). Para contribuinte individual, segurada especial e facultativa, a lei exige 10 contribuições (art. 25, III), reduzidas pelos meses de antecipação do parto (art. 25, p.ú.) e pela metade após perda da qualidade e nova filiação (art. 27-A). Há notícia de que o STF afastou essa carência na ADI 2.110 [VERIFICAR: ADI 2.110 não localizada no JuriBase; conferir dispositivo e modulação no portal do STF antes de alegar].
- Desempregada: o benefício é devido enquanto mantida a qualidade de segurada e é pago diretamente pelo INSS (art. 73, p.ú.; TNU Tema 113). O INSS não pode transferir a obrigação ao ex-empregador.
- Valor: empregada e avulsa recebem a remuneração integral (art. 72); doméstica, o último salário de contribuição (art. 73, I); segurada especial, 1 salário mínimo (art. 39, p.ú.) ou 1/12 da contribuição anual (art. 73, II); demais seguradas, 1/12 da soma dos 12 últimos salários de contribuição em até 15 meses (art. 73, III), assegurado 1 salário mínimo. Para a desempregada cuja última vinculação foi como empregada, aplica-se o art. 73, III (TNU Tema 202).
- Segurada especial: a lei exige atividade rural, ainda que descontínua, nos 12 meses anteriores ao início do benefício (art. 39, p.ú.); julgados do STJ aplicam 10 meses, combinando a lei com o regulamento (AgInt no AREsp 2.630.201). Alegar o prazo mais favorável e provar os 12 meses sempre que possível. A exigência de início de prova material contemporânea pode ser flexibilizada (TNU Temas 11 e 17).
- Indígena menor de 16 anos segurada especial tem direito, atendidos os requisitos (STJ Súmula 657).
- Afastamento da atividade é condição do benefício (art. 71-C): perguntar se a segurada continuou trabalhando.
- Óbito de quem tinha direito: o cônjuge ou companheiro segurado recebe pelo tempo restante (art. 71-B; TNU Tema 236).
- Internação prolongada após o parto: há decisão do STF (ADI 6.327) sobre início do benefício após a alta; o Planalto remete a ela no art. 71 [VERIFICAR: teor e alcance da ADI 6.327 não localizados no JuriBase].

## Fundamentos verificados   (detalhe em [fundamentos](references/fundamentos.md))
- Lei 8.213/1991, arts. 25, III e p.ú.; 26, VI; 27-A; 39, p.ú.; 71; 71-A; 71-B; 71-C; 72; 73; 103, p.ú.
- Lei 13.846/2019 (art. 73, p.ú.; não manteve o art. 71-D).
- STF Temas 313 e 350; STJ Súmula 657; STJ, AgInt no AREsp 2.630.201; TNU Temas 11, 17, 113, 202 e 236.

## Pedidos e requerimentos
- Concessão do salário-maternidade de 120 dias a partir de __ (fato gerador), com pagamento em parcela única das prestações vencidas.
- Valor calculado conforme a categoria (indicar o artigo e anexar memória).
- Correção e juros pelo núcleo `juros-e-correcao`.
- Audiência com testemunhas, se segurada especial.
- Justiça gratuita.

## Checklist pré-protocolo
- [ ] Categoria da segurada na data do fato definida com documento.
- [ ] Qualidade de segurada demonstrada (vínculo ou período de graça com a data-limite calculada).
- [ ] Carência contada ou isenção indicada; ADI 2.110 conferida antes de alegar.
- [ ] Segurada especial: documentos rurais datados dentro dos 10/12 meses anteriores.
- [ ] Prescrição conferida pela data do fato gerador.
- [ ] Memória de cálculo do valor juntada.
- [ ] Juros e correção remetidos ao núcleo.

## Erros a evitar
- Aceitar o argumento de que a empresa deveria pagar quando a segurada já estava desempregada.
- Exigir carência da empregada, doméstica ou avulsa.
- Calcular a desempregada ex-empregada pela última remuneração (a TNU manda usar o art. 73, III).
- Alegar decadência de 180 dias como óbice sem conferir a vigência do art. 71-D.
- Segurada especial só com testemunhas, sem nenhum documento rural.

## Integração com o núcleo
- `juros-e-correcao`; `prazos-processuais`; `verificacao-de-citacoes`; `fidelidade-factual` (datas do fato gerador e das contribuições); `estilo-forense`.

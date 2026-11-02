---
name: prev-pensao-por-morte
description: >
  Monta o pedido de pensão por morte no RGPS (Lei 8.213/1991, arts. 16 e 74 a 77;
  EC 103/2019, art. 23), com dependência, qualidade de segurado do falecido,
  termo inicial, cotas e duração por idade do cônjuge ou companheiro. Use quando o
  usuário pedir pensão por morte, pensão do INSS, união estável para pensão,
  rateio entre dependentes, habilitação de dependente, duração da pensão ou
  cota familiar.
metadata:
  area: previdenciario
  tipo_peca: inicial
  verificado_em: 2026-11-01
---
# Pensão por morte (RGPS)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: indeferimento por falta de qualidade de dependente (união estável, dependência econômica), por perda da qualidade de segurado do falecido, ou disputa de cotas e duração.
- Servidor público: regras do RPPS (ver `prev-rpps-servidor`). Óbito por acidente do trabalho: a pensão segue a Lei 8.213 e a ação é da Justiça Federal, pois o benefício tem natureza previdenciária, não acidentária típica (STJ, CC 197.182; não se aplicam as Súmulas 15/STJ e 501/STF).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Data e causa do óbito (certidão); se decorreu de acidente ou doença do trabalho.
2. Situação do falecido: aposentado, em período de graça, ou com direito à aposentadoria já adquirido.
3. Número de contribuições do falecido e data de início do casamento/união estável.
4. Todos os dependentes possíveis (classes do art. 16), idade de cada um, invalidez ou deficiência.
5. Data do requerimento ao INSS e decisão.
6. Provas de união estável/dependência e datas (para o limite de 24 meses do art. 16, §5º).

## Prazo e contagem
- Termo inicial (art. 74): óbito, se requerida em até 180 dias (filhos menores de 16) ou 90 dias (demais); depois disso, a DER. Morte presumida: decisão judicial.
- Lei aplicável é a da data do óbito (STJ Súmula 340).
- Habilitação posterior só produz efeitos da habilitação (art. 76).

## Estrutura da peça   (detalhe em [estrutura](references/estrutura.md))
1. Competência e interesse de agir.
2. Óbito e qualidade de segurado do instituidor.
3. Qualidade de dependente (classe e prova).
4. Termo inicial.
5. Valor (cota familiar) e duração.
6. Tutela e pedidos.

## Requisitos e preliminares
- Qualidade de segurado do falecido na data do óbito (art. 15), ou direito já adquirido à aposentadoria (STJ Súmula 416).
- Dependentes de 1ª classe (cônjuge, companheiro, filho menor de 21 ou inválido/deficiente) têm dependência presumida (art. 16, §4º); demais classes provam.
- União estável e dependência: início de prova material contemporânea, produzida em até 24 meses antes do óbito; sem prova exclusivamente testemunhal, salvo força maior (art. 16, §5º). Para óbitos anteriores à MP 871/2019, a TNU dispensa prova material da união estável (Súmula 63, redação alterada em 18/09/2025).
- Enteado e menor tutelado equiparam-se a filho mediante declaração e prova da dependência (art. 16, §2º, redação Lei 15.108/2025; EC 103, art. 23, §6º).
- Valor (EC 103, art. 23): cota familiar de 50% da aposentadoria (ou da que teria por incapacidade permanente) + 10 p.p. por dependente, até 100%; cotas não reversíveis (§1º); dependente inválido ou com deficiência grave: 100% até o teto (§2º).
- Duração para cônjuge/companheiro (art. 77, §2º, V): 4 meses se menos de 18 contribuições ou menos de 2 anos de união; caso contrário, conforme a idade no óbito: menos de 21 = 3 anos; 21-26 = 6; 27-29 = 10; 30-40 = 15; 41-43 = 20; 44 ou mais = vitalícia. Óbito por acidente de qualquer natureza (não só do trabalho) ou por doença profissional ou do trabalho dispensa os 18 meses e os 2 anos (§2º-A; TRF1, AC 1032545-82.2021.4.01.9999). As faixas acima são as do texto da lei; o §2º-B permite que ato ministerial eleve as idades, e não foi conferido em fonte oficial se houve ato que as alterou [VERIFICAR o ato ministerial vigente na data do óbito antes de calcular a duração].
- Acumulação com aposentadoria ou outra pensão: redutores do art. 24 da EC 103.

## Fundamentos verificados   (detalhe em [fundamentos](references/fundamentos.md))
- Lei 8.213, arts. 15, 16, 26, I (sem carência), 74 a 77.
- EC 103, arts. 23 e 24.
- STJ Súmulas 340 e 416; TNU Súmula 63; STJ, CC 197.182 (competência federal).

## Pedidos e requerimentos
- Reconhecimento da qualidade de dependente e concessão desde o óbito (ou DER).
- Cálculo da cota familiar com todos os dependentes; duração conforme idade.
- Tutela de urgência.
- Atrasados conforme `juros-e-correcao`.

## Checklist pré-protocolo
- [ ] Certidão de óbito e data conferida (define a lei aplicável).
- [ ] Qualidade de segurado do falecido calculada na data do óbito.
- [ ] Provas materiais de união/dependência com datas dentro dos 24 meses anteriores ao óbito.
- [ ] Todos os dependentes identificados (inclusive outros núcleos familiares) e citados se necessário.
- [ ] Prazo de 90/180 dias verificado para o termo inicial.
- [ ] Cálculo da duração pela idade na data do óbito.

## Erros a evitar
- Aplicar a lei atual a óbito antigo (Súmula 340 STJ).
- Pedir reversão de cotas no RGPS pós-EC 103 (não são reversíveis, art. 23, §1º).
- Omitir outro dependente conhecido: a habilitação posterior pode reduzir a cota e gerar cobrança.
- Instruir união estável só com testemunhas em óbito posterior à MP 871/2019.

## Integração com o núcleo
- `juros-e-correcao`; `prazos-processuais`; `verificacao-de-citacoes`; `fidelidade-factual` (datas de provas e do óbito); `estilo-forense`.

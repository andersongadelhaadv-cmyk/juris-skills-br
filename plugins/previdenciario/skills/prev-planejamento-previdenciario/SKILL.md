---
name: prev-planejamento-previdenciario
description: >
  Monta parecer de planejamento previdenciário no RGPS: diagnóstico do CNIS,
  qualidade de segurado e carência (Lei 8.213, arts. 15, 25 e 27-A), simulação
  das regras de transição da EC 103/2019 (arts. 15 a 18 e 20) e do cálculo
  (art. 26), alíquotas e indenização de períodos (Lei 8.212, arts. 21 e 45-A) e
  escolha da melhor data e regra (STF Tema 334). Use quando o usuário pedir
  planejamento previdenciário, parecer sobre quando se aposentar, "vale a pena
  continuar contribuindo?", qual regra de transição compensa, recolher como
  autônomo ou facultativo, indenizar período antigo ou análise do CNIS para o cliente.
metadata:
  area: previdenciario
  tipo_peca: parecer
  verificado_em: 2026-11-25
---
# Planejamento previdenciário (parecer)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: consulta de quem ainda não se aposentou e quer saber quando, por qual regra e com que valor aproximado; decisão sobre continuar, reduzir ou parar de contribuir; acerto prévio do CNIS; indenização de período como contribuinte individual.
- Não usar para protocolar o pedido (`prev-requerimento-administrativo`), para a ação judicial (`prev-inicial-aposentadoria`, `prev-aposentadoria-especial`, `prev-tempo-rural-e-segurado-especial`), para benefício já concedido (`prev-revisao-de-beneficio`) ou para servidor público (`prev-rpps-servidor`).
- Patrimônio e sucessão do cliente: `sucessoes-planejamento-e-partilha-em-vida`; tributação de rendimentos: `trib-planejamento-tributario`.

## Entradas mínimas (perguntar o que faltar; nunca supor fatos)
1. Data de nascimento, sexo e data da primeira filiação (antes ou depois de 13/11/2019 muda tudo).
2. CNIS completo com remunerações e indicadores; CTPS; carnês/GPS; certidões de tempo de outros regimes.
3. Períodos especiais (PPP/LTCAT), rurais, militares, de aluno-aprendiz, no exterior.
4. Situação atual: empregado, autônomo, MEI, facultativo, desempregado (data da última contribuição).
5. Objetivo do cliente: aposentar o quanto antes, maximizar o valor, reduzir custo de contribuição.
6. Renda disponível para contribuir e expectativa de continuidade do trabalho.

## Prazo e contagem
- Não há prazo processual; há janelas de risco: perda da qualidade de segurado (Lei 8.213, art. 15 e § 4º) e mudança anual dos requisitos nas transições (pontos e idade progressivos — EC 103, arts. 15, § 1º, e 16, § 1º).
- Datar o parecer e fixar validade: requisitos e valores mudam todo ano (salário mínimo, teto, pontuação).

## Estrutura do documento
Consulta → documentos analisados → diagnóstico do CNIS (vínculos, lacunas, pendências) → tempo e carência apurados → qualidade de segurado → simulação por regra (data de implemento e RMI estimada) → custos e alternativas de contribuição → riscos → recomendação → pendências. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e cuidados técnicos
- **Cálculo é determinístico:** tempo, carência, pontos e RMI saem de software de cálculo previdenciário conferido, com memória de cálculo anexa. Texto gerado por IA não calcula; o parecer só interpreta os números.
- Qualidade de segurado: período de graça de 12 meses, prorrogável para 24 com mais de 120 contribuições sem perda, e acrescido de 12 para desempregado com registro (Lei 8.213, art. 15, II, §§ 1º e 2º).
- Carência de 180 contribuições para aposentadorias programadas (art. 25, II); após perda da qualidade, metade da carência para os benefícios do art. 27-A.
- Regras de transição para filiados até a EC 103: pontos (art. 15), idade mínima progressiva (art. 16), pedágio de 50% para quem tinha mais de 28/33 anos de contribuição (art. 17), idade (art. 18), pedágio de 100% (art. 20). Cálculo pela média de 100% dos salários desde julho de 1994 (art. 26), salvo exceções do próprio artigo.
- Custeio: contribuinte individual e facultativo, 20% (Lei 8.212, art. 21); planos de 11% e 5% sobre o mínimo excluem a aposentadoria por tempo de contribuição (art. 21, § 2º) [VERIFICAR: alcance dessa exclusão após a EC 103 e a complementação de alíquota].
- Período de contribuinte individual alcançado pela decadência pode ser indenizado (Lei 8.212, art. 45-A) — calcular custo x ganho antes de recomendar.
- Melhor benefício: o segurado tem direito ao cálculo pelo quadro mais favorável (STF Tema 334) — simular todas as datas e regras possíveis.

## Fundamentos verificados
- Lei 8.213, arts. 15, 24, 25, 27-A, 103; Lei 8.212, arts. 21 e 45-A; EC 103/2019, arts. 15, 16, 17, 18, 20 e 26.
- STF Tema 334 (RE 630.501).
Detalhe em [fundamentos](references/fundamentos.md).

## Conteúdo essencial do parecer
- Quadro de tempo e carência por período, com a fonte de cada um (CNIS, CTPS, PPP, sentença).
- Tabela de cenários: regra | data de implemento | idade | tempo | RMI estimada | custo até lá.
- Pendências do CNIS e como saná-las (acerto prévio — ver `prev-requerimento-administrativo`).
- Recomendação clara, com a premissa de cada cenário e o que a invalida.
- Ressalvas: valores estimados, sujeitos a reajuste anual, mudança legislativa e entendimento do INSS.

## Checklist pré-entrega
- [ ] CNIS emitido há menos de 30 dias e conferido vínculo a vínculo
- [ ] Memória de cálculo do software anexada; nenhum número calculado à mão ou por IA
- [ ] Todas as regras aplicáveis simuladas (inclusive direito adquirido até 13/11/2019)
- [ ] Qualidade de segurado verificada na data atual e nas datas projetadas
- [ ] Custo de contribuição e de indenização comparado com o ganho de RMI
- [ ] Salário mínimo e teto do ano conferidos em fonte oficial
- [ ] Validade e premissas do parecer declaradas

## Erros a evitar
- Recomendar parar de contribuir sem medir a perda da qualidade de segurado e da cobertura por incapacidade e morte.
- Indicar plano de 11% ou 5% a quem precisa da aposentadoria por tempo de contribuição.
- Indenizar período caro que não muda a data nem o valor da aposentadoria.
- Ignorar tempo especial ou rural que antecipa a aposentadoria.
- Apresentar RMI como garantida.

## Integração com o núcleo
`fidelidade-factual` (datas e períodos contra o CNIS), `verificacao-de-citacoes`, `estilo-forense`; `juros-e-correcao` e `prazos-processuais` só se o parecer desaguar em ação.

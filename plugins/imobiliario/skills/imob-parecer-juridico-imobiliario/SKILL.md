---
name: imob-parecer-juridico-imobiliario
description: >
  Redige parecer jurídico sobre negócio ou situação imobiliária (aquisição,
  promessa, garantia fiduciária, regularidade registral, desfazimento de compra
  na planta, financiamento), com pergunta delimitada, fatos e documentos
  examinados, análise por norma e precedente verificados, riscos graduados e
  conclusão objetiva. Use quando o usuário pedir parecer, opinião legal ou
  memorando sobre a segurança de comprar um imóvel, sobre o valor de uma
  promessa não registrada, sobre o risco de fraude à execução, sobre quanto a
  construtora pode reter em um distrato ou sobre a viabilidade de discutir um
  financiamento habitacional.
metadata:
  area: imobiliario
  tipo_peca: parecer
  verificado_em: 2026-11-25
---
# Parecer jurídico imobiliário

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: (a) opinião sobre a segurança de um negócio imobiliário; (b) diagnóstico de situação já existente (promessa sem registro, ônus na matrícula, atraso de obra, leilão extrajudicial); (c) memorando para o cliente decidir entre caminhos.
- Não usar: redação do contrato (`imob-compra-e-venda-de-imovel`); levantamento documental da matrícula (`imob-analise-de-matricula-e-due-diligence`, que alimenta este parecer); peça judicial (`imob-distrato-imobiliario`, `imob-revisao-de-financiamento-sfh`); parecer sobre contrato não imobiliário (`contratos-parecer-sobre-contrato`); locação comercial (`contratos-locacao-comercial`); imóvel em sucessão (`sucessoes-*`); tributação do imóvel (`trib-*`).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. A pergunta exata do cliente (uma ou poucas, numeradas).
2. Quem consulta e qual a posição dele (comprador, vendedor, credor, incorporador, mutuário).
3. Documentos: matrícula recente, contrato(s), certidões, notificações, planilhas de pagamento.
4. Datas decisivas: assinatura do contrato (antes ou depois de 28/12/2018 em compra na planta), registro, posse, intimações, leilões.
5. Objetivo prático: fechar, renegociar, desfazer, litigar, apenas conhecer o risco.
6. Prazo do cliente para decidir.

## Prazo e contagem
- Parecer não tem prazo processual, mas deve apontar os prazos que correm contra o cliente (purgação da mora, leilão, arrependimento de 7 dias, tolerância de 180 dias) e remeter a contagem a `prazos-processuais`.
- Datar o parecer e os documentos examinados; a conclusão vale para aquele estado de fatos.

## Estrutura do parecer
Ementa → consulta → documentos examinados → fatos relevantes → questões jurídicas → análise (uma questão por seção: norma, precedente, aplicação ao caso, contra-argumento) → riscos graduados → conclusão e recomendações. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e cuidados
- Separar **fato documentado** de **fato informado pelo cliente** e de **premissa**: cada conclusão diz em qual se apoia.
- Não afirmar "imóvel livre e desembaraçado" sem a due diligence e sem as ressalvas legais da concentração na matrícula.
- Precedentes pendentes (temas afetados e não julgados) entram como risco, nunca como resposta.
- Cálculos (restituição, saldo devedor, multa, juros): só com o núcleo `juros-e-correcao`; o parecer cita o critério, não inventa número.

## Fundamentos verificados (base mais usada)
- Forma e registro: CC, arts. 108, 1.227, 1.245, 1.417, 1.418; Súmula 239/STJ.
- Concentração na matrícula: Lei 13.097/2015, art. 54; fraude à execução: Súmula 375/STJ.
- Compra na planta: Lei 4.591/1964, arts. 43-A e 67-A; Súmula 543/STJ; Tema 1.095/STJ (alienação fiduciária registrada).
- Alienação fiduciária: Lei 9.514/1997, arts. 26 e 27; Tema 982/STF.
- Adquirente × hipoteca da construtora: Súmula 308/STJ.
Detalhe em [fundamentos](references/fundamentos.md). Para aprofundar cada tema, use a skill específica da área e traga só o que foi verificado.

## Conteúdo essencial da conclusão
- Resposta direta a cada pergunta numerada (sim, não, depende — e do quê).
- Grau de risco (alto, médio, baixo) com a razão em uma frase.
- Providências recomendadas, em ordem, com responsável e prazo.
- Ressalvas: documentos não examinados, temas pendentes no STJ/STF, premissas não comprovadas.

## Checklist pré-entrega
- [ ] Pergunta do cliente transcrita e respondida, item por item
- [ ] Lista de documentos examinados com datas
- [ ] Cada norma e precedente consta do `fontes.yaml` desta skill ou da skill de origem
- [ ] Temas pendentes sinalizados como risco
- [ ] Nenhum número sem o núcleo `juros-e-correcao`
- [ ] Prazos em curso destacados no início
- [ ] Linguagem compreensível para o cliente na conclusão

## Erros a evitar
- Parecer que só descreve a lei e não responde à pergunta.
- Conclusão mais forte que os documentos permitem.
- Citar tema repetitivo afetado como se já tivesse tese.
- Ignorar a data do contrato (regime antes e depois da Lei 13.786/2018).
- Omitir o contra-argumento mais provável da outra parte.

## Integração com o núcleo
`verificacao-de-citacoes`, `fidelidade-factual`, `juros-e-correcao`, `prazos-processuais`, `estilo-forense`.

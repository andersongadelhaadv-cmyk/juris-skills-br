---
name: prev-aposentadoria-por-idade-urbana
description: >
  Monta a petição inicial de aposentadoria por idade urbana contra o INSS, pela
  transição do art. 18 ou pela regra permanente do art. 19 da EC 103/2019, com
  foco na disputa de carência de 180 contribuições (Lei 8.213/1991, arts. 25, II,
  27, II, 48 e 55, II; Lei 10.666/2003, art. 3º, §1º). Use quando o usuário pedir
  aposentadoria por idade urbana, indeferimento por falta de carência, vínculo da
  CTPS fora do CNIS, auxílio-doença intercalado contado como carência,
  contribuição em atraso de contribuinte individual ou recolhimento abaixo do
  mínimo após a reforma.
metadata:
  area: previdenciario
  tipo_peca: inicial
  verificado_em: 2026-11-25
---
# Aposentadoria por idade urbana (EC 103/2019, arts. 18 e 19)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: segurado urbano que atingiu a idade e teve o benefício negado por falta de carência ou de tempo de contribuição, ou que precisa provar vínculos e recolhimentos para fechar os 15/20 anos.
- Comparação entre todas as regras de transição (pontos, pedágio, idade progressiva) ou dúvida sobre qual aposentadoria cabe: `prev-inicial-aposentadoria`.
- Tempo rural, segurado especial ou aposentadoria híbrida: `prev-tempo-rural-e-segurado-especial`.
- Só averbar um período (sem pedir o benefício agora): `prev-averbacao-tempo-de-contribuicao`.
- Ainda não houve requerimento ao INSS: `prev-requerimento-administrativo`. Indeferimento recente com prova nova simples: avaliar `prev-recurso-crps`.
- Benefício já concedido com valor errado: `prev-revisao-de-beneficio`.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Sexo, data de nascimento e data da primeira filiação ao RGPS (antes ou depois de 13/11/2019; antes ou depois de 24/07/1991).
2. Extrato CNIS completo, com indicadores de pendência, e todas as CTPS.
3. Carta de indeferimento: NB, DER e o motivo exato (falta de carência? de tempo? vínculo não reconhecido?).
4. Contagem do INSS (resumo de tempo e carência) para confrontar mês a mês.
5. Períodos controvertidos e a prova de cada um: CTPS, holerites, ficha de registro, reclamatória trabalhista, carnês, guias.
6. Benefícios por incapacidade já recebidos (NB, DIB, DCB) e se houve contribuição antes e depois de cada um.
7. Se foi contribuinte individual ou facultativo: data do primeiro recolhimento em dia e competências pagas com atraso.
8. Recolhimentos após 13/11/2019 abaixo do salário mínimo (intermitente, autônomo de baixa renda).

## Prazo e contagem
- Não há decadência para a concessão inicial (STF Tema 313).
- Prescrevem as parcelas vencidas há mais de 5 anos do ajuizamento (Lei 8.213, art. 103, p.ú.).
- Contar carência em meses de contribuição e tempo de contribuição em dias, separadamente: são requisitos diferentes e o INSS costuma indeferir por um deles.
- Prazos processuais: `prazos-processuais`.

## Estrutura da peça   (detalhe em [estrutura](references/estrutura.md))
1. Endereçamento (JEF ou Vara Federal; estadual só em competência delegada, CF, art. 109, §3º).
2. Interesse de agir: requerimento, indeferimento e prova levada ao INSS (STF Tema 350).
3. Enquadramento: art. 18 (filiado até 13/11/2019) ou art. 19 (filiado depois), ou direito adquirido (EC 103, art. 3º; Lei 8.213, art. 48).
4. Tabela de carência mês a mês: o que o INSS contou, o que falta e por quê.
5. Cada período controvertido em tópico próprio, com a prova.
6. Cálculo da renda (EC 103, art. 26) e eventual reafirmação da DER.
7. Pedidos, provas e valor da causa.

## Requisitos e preliminares
- Art. 18 (filiado até 13/11/2019): 15 anos de contribuição para ambos os sexos; idade de 65 anos (homem) e de 60 anos (mulher), acrescida de 6 meses por ano a partir de 01/01/2020 até chegar a 62.
- Art. 19 (filiado depois de 13/11/2019): 62 anos e 15 anos de contribuição (mulher); 65 anos e 20 anos (homem).
- Direito adquirido: requisitos cumpridos até 13/11/2019 dão direito à regra da época (EC 103, art. 3º): 65/60 anos e carência (Lei 8.213, art. 48).
- Carência: 180 contribuições mensais (Lei 8.213, art. 25, II). A tabela progressiva do art. 142 (inscritos até 24/07/1991) terminou em 2011 com 180 meses; só importa para quem completou a idade antes disso.
- Perda da qualidade de segurado não impede a aposentadoria por idade se, na DER, o segurado tem o tempo correspondente à carência (Lei 10.666/2003, art. 3º, §1º). Não ajuizar "restabelecimento de qualidade de segurado": é desnecessário.
- Tempo intercalado em auxílio por incapacidade conta como tempo de contribuição (Lei 8.213, art. 55, II) e como carência (STF Tema 1125; TNU Súmula 73), desde que haja contribuição antes e depois.
- Contribuinte individual e facultativo: competências pagas com atraso, anteriores ao primeiro pagamento em dia, não contam para carência (Lei 8.213, art. 27, II). Podem contar como tempo, se indenizadas, mas não fecham os 180 meses.
- Recolhimento abaixo do mínimo depois de 13/11/2019 só vale como tempo se complementado, compensado ou agrupado dentro do mesmo ano civil (EC 103, art. 29; CF, art. 195, §14). Pedir ao cliente que regularize no Meu INSS antes de calcular.
- Vínculo da CTPS sem registro no CNIS: CTPS sem defeito formal tem presunção relativa de veracidade (TNU Súmula 75).
- Sentença trabalhista homologatória de acordo só serve como início de prova se apoiada em prova material contemporânea (STJ Tema 1188).

## Fundamentos verificados   (detalhe em [fundamentos](references/fundamentos.md))
- EC 103/2019, arts. 3º, 18, 19, 26 e 29; CF, arts. 109, §3º, e 195, §14.
- Lei 8.213/1991, arts. 25, II; 27, II; 48; 55, II e §3º; 103, p.ú.; 142.
- Lei 10.666/2003, art. 3º, §1º.
- STF Temas 313, 350 e 1125; STJ Tema 1188; TNU Súmulas 73 e 75.

## Pedidos e requerimentos
- Reconhecimento e cômputo, como carência e tempo de contribuição, de cada período controvertido (com datas).
- Concessão da aposentadoria por idade desde a DER; subsidiariamente, com reafirmação da DER para a data em que os requisitos se completarem (ver `prev-inicial-aposentadoria`, que traz o fundamento).
- Parcelas vencidas com correção e juros pelo núcleo `juros-e-correcao` (não escrever índice na peça).
- Tutela de urgência para implantação, se idade avançada ou risco alimentar demonstrado.
- Prioridade de tramitação, justiça gratuita, exibição do processo administrativo pelo INSS.

## Checklist pré-protocolo
- [ ] Planilha separada de carência (meses) e de tempo de contribuição (dias), na DER e em 13/11/2019.
- [ ] Regra correta pela data de filiação (art. 18 x art. 19) e idade da mulher conferida no ano exato.
- [ ] Cada período controvertido com prova e com a informação de que foi apresentado ao INSS.
- [ ] Benefícios por incapacidade intercalados identificados e incluídos na carência.
- [ ] Recolhimentos em atraso de contribuinte individual separados do que conta para carência.
- [ ] Competências abaixo do mínimo após 13/11/2019 regularizadas ou excluídas.
- [ ] Juros e correção remetidos ao núcleo.

## Erros a evitar
- Somar como carência o tempo do contribuinte individual pago em atraso.
- Aplicar o art. 19 (20 anos para o homem) a quem já era filiado antes de 13/11/2019.
- Usar a idade de 62 anos para a mulher que completou 60 anos e 6 meses em 2020 (conferir o ano em que fechou os requisitos).
- Pedir o cômputo de auxílio-doença que não foi intercalado com contribuição.
- Juntar só a sentença trabalhista homologatória, sem prova contemporânea.
- Não discutir o motivo concreto do indeferimento.

## Integração com o núcleo
- `juros-e-correcao` para atrasados; `prazos-processuais` para prazos.
- `verificacao-de-citacoes` para todo precedente acrescentado.
- `fidelidade-factual` para conferir competências com CNIS e CTPS.
- `estilo-forense` para a redação final.

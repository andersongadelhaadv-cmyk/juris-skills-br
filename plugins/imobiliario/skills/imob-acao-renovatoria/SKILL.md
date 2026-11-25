---
name: imob-acao-renovatoria
description: >
  Redige ação renovatória de locação não residencial (Lei 8.245/1991, arts.
  51 a 57 e 71 a 75): requisitos do art. 51, janela decadencial do § 5º,
  instrução obrigatória do art. 71, defesa do locador do art. 72, aluguel
  provisório e diferenças. Use quando o usuário pedir renovação compulsória
  de aluguel comercial, proteção do ponto/fundo de comércio, renovatória de
  loja em shopping, contestação de renovatória pelo locador ou cálculo da
  data-limite para propor a ação.
metadata:
  area: imobiliario
  tipo_peca: inicial
  verificado_em: 2026-11-25
---
# Ação renovatória

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: locatário de imóvel destinado ao comércio (e situações equiparadas do art. 51, §§ 1º a 4º — cessionário, sucessor, sociedade, indústria) que quer a renovação compulsória por igual prazo; locador que precisa contestar a renovatória.
- Não usar: só ajustar o aluguel ao mercado durante o contrato (`imob-acao-revisional-de-aluguel`); retomada pelo locador após o termo, sem renovatória ajuizada (`imob-acao-de-despejo`, art. 57 ou art. 59, § 1º, VIII); redigir ou revisar o contrato comercial (`contratos-locacao-comercial`); locação residencial (não há direito à renovatória).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Todos os contratos e aditivos, com datas de início e fim — para somar os prazos ininterruptos (art. 51, II).
2. Data exata do término do contrato em curso (define a janela do art. 51, § 5º).
3. Ramo explorado e desde quando, no mesmo ramo (art. 51, III — mínimo de três anos ininterruptos).
4. Prova de cumprimento do contrato: aluguéis e encargos quitados (art. 71, II) e impostos e taxas a cargo do locatário (art. 71, III).
5. Condições oferecidas para a renovação: aluguel, índice, prazo (art. 71, IV) — com base em avaliação de mercado.
6. Fiador: o mesmo ou outro, com qualificação completa, prova de idoneidade financeira atual e aceite por escrito com outorga do cônjuge (art. 71, V e VI).
7. Título de cessão ou sucessão oponível ao proprietário, se for o caso (art. 71, VII).
8. Locação em shopping center? Há indício de retomada pelo locador (uso próprio, obras, proposta de terceiro)?

## Prazo e contagem
- Janela decadencial: a ação deve ser proposta no intervalo de um ano, no máximo, até seis meses, no mínimo, antes do fim do prazo do contrato em vigor (art. 51, § 5º). Fora dela, perde-se o direito à renovação e o locatário fica exposto à denúncia do art. 57 e ao despejo — o STJ manteve improcedência por decadência com desocupação em 30 dias (REsp 1.846.676).
- Calcular a data-limite com folga e conferir o calendário em `prazos-processuais`; prazos processuais correm nas férias forenses (art. 58, I).

## Estrutura da peça
Endereçamento (foro do imóvel, salvo eleição — art. 58, II) → requisitos do art. 51 → cumprimento do contrato → proposta de renovação → fiador → pedidos → valor da causa (12 meses de aluguel — art. 58, III). Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Cumulativos (art. 51): contrato escrito e por prazo determinado; prazo mínimo de cinco anos, somados os contratos escritos ininterruptos; três anos ininterruptos no mesmo ramo.
- Instrução obrigatória (art. 71, I a VII). O ônus de provar esses requisitos é do locatário e não se inverte (STJ, REsp 2.005.621).
- O fiador que aceita a renovação pode ser incluído no cumprimento de sentença mesmo sem ter participado da fase de conhecimento (STJ, REsp 2.060.759) — por isso o aceite do art. 71, VI, deve ser expresso e completo.
- Cláusula que afaste o direito à renovação ou cobre por ele é nula (art. 45).

## Fundamentos verificados
- Lei 8.245/1991: arts. 45, 51, 52, 58, 71, 72, 73, 74, 75.
- Defesa do locador limitada, quanto aos fatos, ao art. 72 (requisitos, valor locativo, proposta de terceiro, exceções do art. 52), com os ônus dos §§ 1º a 3º.
- Aluguel provisório a pedido do locador na contestação, até 80% do pedido, vigente desde o primeiro mês do prazo renovado (art. 72, § 4º); periodicidade e indexador diversos a pedido do locador (art. 72, § 5º).
- Diferenças executadas nos próprios autos, de uma só vez (art. 73); a procedência tem efeitos desde o dia seguinte ao fim do contrato primitivo (STJ, REsp 1.883.486).
- Prazo da renovação limitado a cinco anos (STJ, REsp 1.971.600; AgInt no AREsp 2.346.420).
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Renovação do contrato por igual prazo (observado o limite de cinco anos fixado pelo STJ), nas condições propostas.
- Fixação do aluguel nos termos da proposta ou no valor apurado em perícia.
- Prova pericial de avaliação do valor locativo.
- Execução das diferenças nos próprios autos (art. 73); correção e juros pelo núcleo `juros-e-correcao`.
- Do lado do locador (contestação): improcedência, retomada (art. 52), aluguel provisório (art. 72, § 4º), novo indexador (art. 72, § 5º) e mandado de despejo com 30 dias se houver pedido na contestação (art. 74).

## Checklist pré-protocolo
- [ ] Data-limite do art. 51, § 5º calculada e respeitada
- [ ] Soma dos contratos escritos ininterruptos igual ou superior a cinco anos
- [ ] Três anos no mesmo ramo comprovados
- [ ] Quitação de aluguéis, encargos, impostos e taxas juntada
- [ ] Proposta clara e precisa (valor, índice, prazo) com laudo de mercado
- [ ] Fiador qualificado, com idoneidade atual e aceite com outorga conjugal
- [ ] Shopping center: avaliado o art. 52, § 2º
- [ ] Juros e correção remetidos ao núcleo

## Erros a evitar
- Perder a janela do art. 51, § 5º por contar do início, e não do fim, do contrato em vigor.
- Pedido genérico de "aluguel justo" sem proposta definida (art. 71, IV) — o STJ discute a vinculação do juiz aos valores ofertados pelas partes (REsp 2.192.753; conferir o inteiro teor antes de usar).
- Somar contratos com intervalo entre eles, ou contrato verbal.
- Pedir prazo de renovação superior a cinco anos.
- Esquecer que o locador que alega proposta de terceiro deve juntá-la assinada pelo terceiro e por duas testemunhas, em ramo diverso (art. 72, § 2º) — e o locatário pode cobri-la na réplica.

## Integração com o núcleo
`juros-e-correcao`, `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

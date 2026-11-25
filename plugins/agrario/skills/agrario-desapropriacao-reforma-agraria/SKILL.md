---
name: agrario-desapropriacao-reforma-agraria
description: >
  Redige a contestação do expropriado na ação de desapropriação por interesse
  social para reforma agrária (CF arts. 184 a 186; LC 76/1993; Lei 8.629/1993),
  com impugnação do laudo do INCRA, defesa de produtividade e de pequena ou
  média propriedade, esbulho que impede a vistoria, justa indenização (terra
  nua em TDA e benfeitorias em dinheiro), levantamento de 80% e honorários; e
  orienta a inicial de desapropriação indireta de imóvel rural. Use quando o
  usuário pedir defesa em desapropriação do INCRA, contestar laudo agronômico
  de fiscalização, discutir GUT e GEE, impugnar o valor da terra nua ou cobrar
  indenização por apossamento ou unidade de conservação em área rural.
metadata:
  area: agrario
  tipo_peca: contestacao
  verificado_em: 2026-11-25
---
# Desapropriação para reforma agrária — defesa do expropriado

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: (a) contestação na ação de desapropriação ajuizada pelo INCRA (LC 76/1993); (b) manifestação sobre imissão, perícia, levantamento do depósito e acordo; (c) estratégia contra a declaração de improdutividade (ação própria contra o processo administrativo/decreto, já que a contestação não discute o interesse social); (d) inicial de indenização por desapropriação indireta de imóvel rural (apossamento, criação de unidade de conservação com esvaziamento econômico).
- Não usar: desapropriação por utilidade pública ou por interesse social fora da reforma agrária — `adm-desapropriacao-defesa`; expropriação confiscatória (cultura ilegal de psicotrópicos, trabalho escravo) — tema próprio, sem indenização; servidão administrativa de linha de transmissão — regime e prazo diferentes.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Decreto declaratório (data de publicação no DOU) e a inicial com a oferta (terra nua em TDA + benfeitorias em dinheiro).
2. Íntegra do processo administrativo: comunicação prévia da vistoria (data), laudo agronômico de fiscalização, cálculo de GUT e GEE, impugnações e recursos administrativos.
3. Matrícula, CCIR, ITR, CAR; área registrada x área medida; georreferenciamento.
4. Área do imóvel em módulos fiscais e se o proprietário tem outro imóvel rural (pequena/média propriedade).
5. Prova de exploração no período: notas de produtor, vacinação, GTA, contratos de arrendamento, projeto técnico aprovado.
6. Ocupações/invasões: datas, boletins, ações possessórias — antes, durante ou depois da vistoria.
7. Benfeitorias, cobertura vegetal, reserva legal e APP (averbada ou registrada no CAR).
8. Ônus reais, enfiteuse, condôminos, espólio.

## Prazo e contagem
- Ação proposta em até 2 anos da publicação do decreto (LC 76/1993, art. 3º) — conferir a caducidade.
- Contestação em 15 dias (LC 76/1993, art. 9º); contagem e forma: `prazos-processuais`.
- Audiência de conciliação pode ser designada nos 10 primeiros dias após a citação e não suspende a ação (art. 6º, §§ 3º e 7º).
- Desapropriação indireta: prazo decenal referido pela 1ª Seção do STJ com base no art. 1.238, parágrafo único, do CC, com regra de transição do art. 2.028 (EREsp 1.548.180); fatos antigos podem atrair a Súmula 119 (vinte anos) pelo CC/1916.

## Estrutura da peça
Tempestividade → preliminares (caducidade do decreto, vícios da inicial do art. 5º, legitimidade/citação) → mérito defensivo (insusceptibilidade: produtividade, pequena/média propriedade, projeto técnico, esbulho) → impugnação do laudo e da área → justa indenização (terra nua, benfeitorias, cobertura vegetal) → levantamento de 80% → quesitos e assistente técnico → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Matéria da contestação: só defesa; vedado discutir o interesse social declarado (LC 76/1993, art. 9º). A nulidade do processo administrativo e a produtividade costumam ir em ação própria (declaratória/anulatória), conexa — avaliar no caso e alegar na contestação o que for matéria de defesa.
- Inicial do INCRA deve vir com decreto, certidões, documento cadastral, laudo com valores separados de terra nua e benfeitorias, comprovante de lançamento dos TDA e depósito das benfeitorias (art. 5º).
- Citação do proprietário; enfiteuse (domínios útil e direto); espólio sem inventariante (cônjuge ou herdeiro na posse); titulares de direitos reais intimados; confrontantes que impugnaram divisas (art. 7º).
- Intervenção obrigatória do MPF (art. 18, § 2º); preferência e prejudicialidade sobre outras ações relativas ao imóvel (art. 18).

## Fundamentos verificados
- CF arts. 184 (TDA para a terra nua; benfeitorias úteis e necessárias em dinheiro), 185 (insuscetíveis: pequena e média propriedade de quem não tem outra; propriedade produtiva) e 186 (função social).
- Lei 8.629/1993: art. 2º, §§ 2º a 4º (comunicação prévia; alterações até 6 meses depois não contam) e § 6º (imóvel invadido não vistoriado por 2 anos); art. 4º (pequena até 4 e média de 4 a 15 módulos fiscais); art. 6º (GUT ≥ 80% e GEE ≥ 100%; § 7º força maior); art. 7º (projeto técnico); art. 9º (função social); art. 12 (justa indenização a preço de mercado; vegetação natural integra o preço da terra).
- LC 76/1993: arts. 3º, 5º, 6º (imissão; levantamento de 80%), 7º, 9º, 12, 13, 16, 18, 19 (honorários até 20% da diferença).
- Súmula 354/STJ e sua leitura após a ADI 2.213 (esbulho anterior ou contemporâneo à vistoria e que afete a medição da produtividade — AgInt no AREsp 1.279.478).
- Juros compensatórios condicionados à produtividade e à perda de renda (ADI 2.332, aplicada no AgInt no REsp 2.067.135); afastados em imóvel improdutivo (REsp 1.717.047). Taxa e cálculo: núcleo `juros-e-correcao`.
- Indenização pela área efetivamente desapropriada/medida (REsp 2.058.315).
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Acolhimento das preliminares (caducidade, inépcia por falta de documento do art. 5º).
- Reconhecimento da insuscetibilidade (pequena/média propriedade; produtividade; projeto técnico; esbulho que comprometeu a vistoria), com extinção ou improcedência — ou suspensão (Súmula 354, conforme a leitura atual).
- Perícia judicial nos pontos impugnados (art. 9º, § 1º), com quesitos e assistente técnico.
- Fixação da justa indenização a preço de mercado, individualizando terra nua, benfeitorias e demais componentes (art. 12, § 3º), pela área medida.
- Levantamento de 80% do depósito (art. 6º, § 1º), com comprovação de quitação de tributos e editais.
- Juros e correção pelo núcleo `juros-e-correcao`; honorários de até 20% sobre a diferença entre oferta e indenização (art. 19, § 1º).
- Intimação do MPF.

## Checklist pré-protocolo
- [ ] Data do decreto x data da propositura (2 anos)
- [ ] Contestação no prazo de 15 dias
- [ ] Cópia integral do processo administrativo e da comunicação prévia da vistoria
- [ ] Módulos fiscais e certidão negativa de outro imóvel (pequena/média)
- [ ] Recalculo de GUT/GEE com áreas não aproveitáveis (APP, reserva legal) e prova de produção
- [ ] Linha do tempo das ocupações frente à data da vistoria
- [ ] Área registrada x medida; georreferenciamento
- [ ] Quesitos e assistente técnico (agrônomo/engenheiro)
- [ ] Pedido de levantamento de 80% com certidões
- [ ] Juros/correção remetidos ao núcleo

## Erros a evitar
- Discutir na contestação o mérito do interesse social declarado (art. 9º veda).
- Alegar invasão ocorrida muito depois da vistoria como se bastasse para suspender o processo.
- Somar a vegetação nativa como verba autônoma por fora do preço da terra (art. 12, § 2º).
- Pedir juros compensatórios sem provar produtividade e perda de renda.
- Ignorar o projeto técnico aprovado 6 meses antes da comunicação (art. 7º).
- Tratar a desapropriação indireta com o prazo quinquenal das ações pessoais contra a Fazenda.

## Integração com o núcleo
`juros-e-correcao`, `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`. Recursos: `civel-apelacao`, `civel-agravo-de-instrumento`, `civel-recurso-especial`.

---
name: trabalhista-trabalho-intermitente
description: >
  Orienta a contratação e o litígio do contrato de trabalho intermitente (CLT
  arts. 443, §3º, e 452-A): contrato escrito com valor-hora não inferior ao
  mínimo-hora nem ao dos demais empregados da função, convocação com três dias
  corridos, resposta em um dia útil, multa de 50% pelo descumprimento sem justo
  motivo, pagamento ao fim de cada prestação, recolhimentos mensais e férias.
  Use quando o usuário pedir contrato intermitente, convocação de intermitente,
  validade do intermitente, descaracterização para contrato comum, diferenças de
  verbas do intermitente ou defesa da empresa.
metadata:
  area: trabalhista
  tipo_peca: outro
  verificado_em: 2026-11-25
---
# Trabalho intermitente (CLT arts. 443, § 3º, e 452-A)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar (consultivo): redigir contrato intermitente, modelo de convocação e recibo discriminado; checar conformidade de contratos existentes.
- Usar (contencioso): pedido de descaracterização do intermitente (prestação contínua, sem alternância real de inatividade), diferenças de valor-hora, verbas não pagas ao fim de cada período, multa do § 4º, férias. A peça é a reclamação (`trabalhista-reclamacao`) ou a contestação (`trabalhista-contestacao`) com os tópicos desta skill.
- Não usar: trabalho temporário por agência (`trabalhista-terceirizacao`); autônomo ou eventual sem subordinação (`trabalhista-vinculo-de-emprego`); aeronauta, excluído pelo § 3º do art. 443 (legislação própria).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Contrato escrito? Valor da hora? Função?
2. Valor-hora (ou salário-hora) dos demais empregados da mesma função no estabelecimento, intermitentes ou não.
3. Histórico de convocações: datas, antecedência, meio usado, resposta, horas efetivamente trabalhadas por mês.
4. Pagamentos: feitos ao fim de cada prestação? Com recibo discriminado (remuneração, férias proporcionais com 1/3, 13º proporcional, repouso semanal remunerado, adicionais)?
5. Recolhimentos de INSS e FGTS mensais e entrega de comprovantes.
6. Férias: a cada 12 meses, o empregado usufruiu de um mês sem convocação?
7. Houve recusa ou desistência de convocação aceita? Por quem e por quê (multa do § 4º)?

## Prazo e contagem
- Convocação: com pelo menos três dias corridos de antecedência, informando a jornada (art. 452-A, § 1º).
- Resposta: um dia útil; silêncio presume recusa (§ 2º).
- Multa por descumprimento da convocação aceita: 50% da remuneração que seria devida, paga em 30 dias, permitida compensação no mesmo prazo (§ 4º).
- Férias: a cada 12 meses, direito a usufruir, nos 12 meses seguintes, um mês sem convocação pelo mesmo empregador (§ 9º).
- Prescrição: cinco anos, até dois anos após a extinção (CF art. 7º, XXIX).
- Prazos processuais: `prazos-processuais`.

## Estrutura da peça
Consultivo: contrato escrito → valor-hora e paridade → convocação e resposta → pagamento e recibo → recolhimentos → férias → multa. Contencioso: forma do contrato → prática real (alternância ou continuidade) → diferenças e verbas → pedidos. Roteiro em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Conceito** (art. 443, § 3º): prestação subordinada não contínua, com alternância de períodos de prestação e inatividade, em horas, dias ou meses, qualquer que seja a atividade, exceto aeronautas.
- **Forma e valor** (art. 452-A, caput): contrato escrito, com valor da hora não inferior ao valor-hora do salário mínimo nem ao devido aos demais empregados do estabelecimento na mesma função.
- **Subordinação preservada**: a recusa da oferta não descaracteriza a subordinação (§ 3º).
- **Inatividade**: não é tempo à disposição; o empregado pode prestar serviço a outros contratantes (§ 5º).
- **Pagamento por período** (§§ 6º e 7º): ao fim de cada prestação, pagamento imediato de remuneração, férias proporcionais com 1/3, 13º proporcional, repouso semanal remunerado e adicionais legais, discriminados no recibo.
- **Recolhimentos** (§ 8º): INSS e FGTS com base nos valores pagos no período mensal, com entrega de comprovante.
- **Descaracterização**: se a prestação foi contínua, sem a alternância que define o instituto, sustentar contrato por prazo indeterminado comum, com salário fixo e jornada — argumento fático, a demonstrar com o histórico de convocações [VERIFICAR: jurisprudência atual do TST sobre descaracterização — não localizada na base consultada].
- **Constitucionalidade**: o STF examinou o contrato intermitente em ações diretas (ADI 5826 e outras) [VERIFICAR: resultado e tese — ações não localizadas na base consultada; não afirmar o desfecho sem conferir no portal do STF].

## Fundamentos verificados
CLT arts. 443 caput e § 3º, 452-A (caput e §§ 1º a 9º), na redação da Lei 13.467/2017, conferida também na compilação do Senado (nenhum parágrafo marcado como revogado); CF art. 7º, XXIX. Detalhes em [fundamentos](references/fundamentos.md).

## Cláusulas essenciais (contrato intermitente)
- Identificação, função e local; menção expressa ao regime intermitente (arts. 443, § 3º, e 452-A).
- Valor da hora, com declaração da paridade com o mínimo-hora e com a função.
- Procedimento de convocação (meio eficaz, três dias corridos, jornada informada) e de resposta (um dia útil; silêncio = recusa).
- Multa de 50% por descumprimento sem justo motivo e regra de compensação (§ 4º).
- Forma e momento de pagamento ao fim de cada prestação, com recibo discriminado.
- Recolhimentos mensais e entrega de comprovantes.
- Férias: período anual sem convocação.

## Checklist pré-protocolo
- [ ] Contrato escrito anexado (ou a sua ausência explorada).
- [ ] Valor-hora comparado com o mínimo-hora e com colegas da mesma função.
- [ ] Tabela de convocações (data, antecedência, resposta, horas) montada.
- [ ] Recibos conferidos parcela a parcela (§ 6º).
- [ ] Extratos de FGTS e INSS conferidos mês a mês.
- [ ] Férias do § 9º verificadas.
- [ ] Pedidos liquidados; juros e correção pelo núcleo `juros-e-correcao`.

## Erros a evitar
- Contratar intermitente sem contrato escrito ou sem valor-hora definido.
- Pagar só a hora e deixar férias, 13º e repouso para o fim do contrato.
- Usar o intermitente para jornada fixa e contínua (risco de descaracterização).
- Convocar com menos de três dias corridos ou durante o mês de férias.
- Afirmar o resultado do STF sobre o intermitente sem conferir a fonte oficial.

## Integração com o núcleo
`juros-e-correcao`, `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

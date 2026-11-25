---
name: imob-acao-de-despejo
description: >
  Redige ação de despejo da Lei 8.245/1991 — por falta de pagamento (com ou
  sem cobrança cumulada), por denúncia vazia, por denúncia cheia e por
  infração contratual —, com pedido de liminar de desocupação do art. 59,
  § 1º, e enfrentamento da purgação da mora do art. 62. Use quando o usuário
  pedir despejo de inquilino inadimplente, retomada de imóvel locado, liminar
  de desocupação em 15 dias, despejo por fim de prazo, despejo por infração
  ou defesa/estratégia diante da purga da mora.
metadata:
  area: imobiliario
  tipo_peca: inicial
  verificado_em: 2026-11-25
---
# Ação de despejo

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: locação urbana regida pela Lei 8.245/1991 (residencial ou não residencial) e o locador quer reaver o imóvel por (a) falta de pagamento de aluguel e encargos (art. 9º, III); (b) infração legal ou contratual (art. 9º, II); (c) denúncia vazia — art. 46, § 2º (residencial de 30 meses ou mais, prorrogada), art. 57 (contrato por prazo indeterminado) ou art. 8º (adquirente); (d) denúncia cheia — hipóteses do art. 47 e do art. 9º, IV.
- Não usar: discussão só do valor do aluguel (`imob-acao-revisional-de-aluguel`); locatário comercial que quer renovar (`imob-acao-renovatoria`); cobrança de aluguel sem pedido de retomada, com contrato e prova do débito (`civel-execucao-titulo-extrajudicial`); ocupação sem contrato de locação (possessória, `civel-peticao-inicial`); redação do contrato (`imob-locacao-residencial` ou `contratos-locacao-comercial`); defesa do locatário (`civel-contestacao`, usando os fundamentos desta skill).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Contrato de locação: data, prazo, destinação (residencial/não residencial), valor, vencimento, índice e garantia (caução, fiança, seguro-fiança, cessão fiduciária de cotas ou nenhuma).
2. Fundamento do despejo pretendido e a data em que ele nasceu (vencimento da primeira parcela em aberto, fim do prazo, data da infração).
3. Planilha do débito, parcela por parcela, com aluguel e encargos separados (cálculo atualizado é feito pelo núcleo `juros-e-correcao`).
4. Notificações já enviadas (denúncia, constituição em mora, pedido de nova garantia) com prova de entrega.
5. Situação da garantia: existe, foi extinta, o fiador se exonerou? (decisivo para a liminar do art. 59, § 1º, IX).
6. O locatário purgou a mora nos últimos 24 meses em outra ação? (art. 62, parágrafo único).
7. Há sublocatários ou ocupantes? (art. 59, § 2º). O autor é proprietário? (art. 60).

## Prazo e contagem
- Denúncia vazia: notificação com 30 dias para desocupar (arts. 46, § 2º, e 57) ou 90 dias se a denúncia for do adquirente (art. 8º); a denúncia do adquirente deve ocorrer em 90 dias do registro, sob pena de presumir-se a concordância com a locação.
- Liminar por fim de prazo de locação não residencial ou de temporada: ação proposta em até 30 dias do termo (art. 59, § 1º, III e VIII).
- Purga da mora: 15 dias contados da citação (art. 62, II); complementação em 10 dias da intimação (art. 62, III).
- Prazos processuais correm nas férias forenses (art. 58, I). Contagem em dias úteis e calendário: `prazos-processuais`.

## Estrutura da peça
Endereçamento (foro do imóvel, salvo eleição — art. 58, II) → qualificação → contrato e garantia → fundamento do despejo → (cobrança cumulada, se for o caso) → liminar do art. 59, § 1º, com caução → requerimentos de citação e de ciência a sublocatários → pedidos → valor da causa (12 meses de aluguel — art. 58, III). Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Rito: procedimento comum, com as modificações da Lei 8.245/1991 (art. 59, caput).
- Cumulação com cobrança só no despejo por falta de pagamento, com cálculo discriminado (art. 62, I). Incluir o fiador no polo se quiser executá-lo depois: o fiador que não integrou a ação de despejo não responde pela execução do julgado (Súmula 268/STJ).
- Prova da propriedade ou do compromisso registrado nas ações dos arts. 9º, IV, 47, IV, e 53, II (art. 60).
- Citação por correspondência com AR é possível se o contrato a autorizar (art. 58, IV).
- Recursos com efeito só devolutivo (art. 58, V).

## Fundamentos verificados
- Lei 8.245/1991: arts. 8º, 9º, 46, 47, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66.
- Liminar de desocupação em 15 dias, sem ouvir o réu, com caução de três meses de aluguel, só nas hipóteses do art. 59, § 1º (I a IX); no inciso IX (falta de pagamento sem garantia), o réu afasta a liminar depositando o débito em 15 dias (art. 59, § 3º).
- Purga: aluguéis e acessórios vencidos até o pagamento, multas exigíveis, juros e custas com honorários de 10%, salvo disposição contratual diversa (art. 62, II, a a d). Os honorários do art. 62, II, "d", só valem para a purga; sem purga, honorários pela regra geral do CPC (STJ, REsp 2.060.118).
- Liminar negada quando não demonstrados o prazo de ajuizamento e a caução (STJ, AgInt no AREsp 2.349.376).
- Súmula 268/STJ (fiador fora da ação de despejo).
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Liminar de desocupação em 15 dias (art. 59, § 1º, inciso específico), com oferta de caução de três meses de aluguel.
- Rescisão do contrato e despejo, com mandado de desocupação voluntária em 30 dias — ou 15 dias nos casos do art. 63, § 1º.
- Cobrança cumulada dos aluguéis e encargos vencidos e dos que vencerem no curso da ação (art. 62, I e V); correção e juros pelo núcleo `juros-e-correcao`.
- Citação do locatário e dos fiadores; ciência aos sublocatários (art. 59, § 2º).
- Autorização para execução provisória do despejo com caução de 6 a 12 meses de aluguel, salvo nas ações fundadas no art. 9º (art. 64).
- Custas e honorários.

## Checklist pré-protocolo
- [ ] Fundamento escolhido bate com a prova (planilha, notificação, prova da infração)
- [ ] Notificação prévia juntada nas denúncias vazias, com prazo esgotado
- [ ] Inciso do art. 59, § 1º, indicado e caução oferecida (se pedir liminar)
- [ ] Situação da garantia descrita (inciso IX exige ausência ou extinção da garantia)
- [ ] Fiadores no polo passivo, se houver interesse em executá-los
- [ ] Purga anterior em 24 meses pesquisada
- [ ] Valor da causa: 12 meses de aluguel
- [ ] Cálculo do débito pelo núcleo `juros-e-correcao`

## Erros a evitar
- Pedir liminar fora do rol do art. 59, § 1º, sem fundamentar tutela de urgência autônoma (CPC, art. 300).
- Propor despejo por denúncia vazia sem notificação prévia ou antes de vencido o prazo dela.
- Usar a via do art. 46, § 2º, em contrato residencial com prazo inferior a 30 meses (ali a retomada segue o art. 47).
- Deixar o fiador fora da ação e tentar executá-lo depois (Súmula 268/STJ).
- Cobrar honorários contratuais de 20% como se fossem os 10% do art. 62, II, "d", quando não houve purga (REsp 2.060.118).
- Esquecer que o despejo não se executa até o 30º dia após falecimento de cônjuge, ascendente, descendente ou irmão de morador (art. 65).

## Integração com o núcleo
`juros-e-correcao` (débito, correção e juros), `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`; tutela fora do rol: `civel-tutela-provisoria`.

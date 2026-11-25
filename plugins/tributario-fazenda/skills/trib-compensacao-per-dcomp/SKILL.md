---
name: trib-compensacao-per-dcomp
description: >
  Orienta e redige o pedido de restituição e a declaração de compensação de
  tributos federais (PER/DCOMP) com base no art. 74 da Lei 9.430/1996 e nos
  arts. 170 e 170-A do CTN, inclusive a manifestação de inconformidade contra
  despacho que não homologa a compensação. Use quando o usuário pedir
  compensação tributária, PER/DCOMP, compensar crédito com débito federal,
  defesa contra compensação não homologada, compensação considerada não
  declarada ou multa isolada de 50% por compensação.
metadata:
  area: tributario-fazenda
  tipo_peca: requerimento
  verificado_em: 2026-11-25
---
# Compensação tributária federal (PER/DCOMP)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: (a) crédito federal administrado pela Receita (pagamento indevido ou a maior, saldo negativo, ressarcimento) a compensar com débito próprio; (b) despacho decisório que não homologou a DCOMP (manifestação de inconformidade); (c) compensação considerada "não declarada"; (d) multa isolada do art. 74, § 17.
- Crédito reconhecido em ação judicial transitada em julgado: antes da DCOMP vem a habilitação — use `trib-habilitacao-de-credito-judicial`.
- Ainda não há crédito reconhecido e se quer declarar o direito de compensar em juízo: `trib-mandado-de-seguranca` (Súmula 213 STJ) ou `trib-repeticao-de-indebito`.
- Tributo estadual ou municipal: a compensação depende de lei do ente (CTN art. 170); esta skill só serve de roteiro.
- Débito já inscrito em dívida ativa: não cabe DCOMP (art. 74, § 3º, III) — avalie `trib-transacao-tributaria` ou `trib-parcelamento-e-regularizacao`.

## Entradas mínimas (perguntar o que faltar; nunca supor fatos)
1. Origem do crédito: tipo (pagamento indevido, saldo negativo de IRPJ/CSLL, ressarcimento de IPI/PIS/Cofins etc.), período, DARFs e escrita fiscal que o comprovam.
2. Se o crédito decorre de discussão judicial: há trânsito em julgado? Foi habilitado? Houve desistência da execução?
3. Débitos a compensar: tributo, código, competência, vencimento; se estão em parcelamento, em cobrança ou já enviados à PGFN.
4. Para defesa: despacho decisório, data da ciência, valores não homologados, motivação do Fisco.
5. Situação de DCTF, EFD e ECF (retificadas? coerentes com o crédito?).

## Prazo e contagem
- Direito de pleitear restituição/compensar: 5 anos (CTN art. 168); confira o termo inicial no caso.
- Homologação tácita: 5 anos da entrega da DCOMP (Lei 9.430, art. 74, § 5º).
- Não homologada: o contribuinte é intimado a pagar em 30 dias (§ 7º), e no mesmo prazo pode apresentar manifestação de inconformidade (§ 9º).
- Contagem de prazos administrativos e judiciais: `prazos-processuais`.

## Estrutura da peça
Pedido/declaração: identificação do crédito → demonstrativo → débitos → base legal. Manifestação de inconformidade: tempestividade → síntese do despacho → preliminares → existência, liquidez e certeza do crédito com prova → afastamento da multa isolada → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- A DCOMP extingue o débito sob condição resolutória de homologação (§ 2º) e é confissão de dívida (§ 6º): débito mal informado vira cobrança direta.
- Vedações do § 3º (entre outras: débito já enviado à PGFN, débito parcelado, estimativas mensais de IRPJ/CSLL, crédito acima do limite mensal do art. 74-A).
- Hipóteses de compensação "não declarada" (§ 12): crédito de terceiro, decisão judicial não transitada, tributo não administrado pela Receita, entre outras. Nelas não há manifestação de inconformidade com efeito suspensivo (§ 13).
- Tributo discutido judicialmente: só após o trânsito em julgado (CTN art. 170-A).
- Rito da defesa: Decreto 70.235/1972 (§ 11); a manifestação suspende a exigibilidade do débito (CTN art. 151, III).

## Fundamentos verificados
- CTN arts. 151, III; 168; 170; 170-A.
- Lei 9.430/1996, art. 74 (§§ 1º a 18) e art. 74-A.
- Súmulas 213, 460, 461 e 464 do STJ; Súmula 212 do STJ **cancelada** em 2022 (não usar como óbice nem como fundamento).
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Reconhecimento integral do crédito e homologação da compensação declarada.
- Subsidiariamente, homologação parcial com recálculo do saldo devedor.
- Cancelamento da multa isolada do § 17 (ou suspensão de sua exigibilidade enquanto pendente a defesa, § 18).
- Diligência ou perícia, com quesitos, quando a prova contábil exigir.
- Atualização do crédito: remeter ao núcleo `juros-e-correcao`.

## Checklist pré-protocolo
- [ ] Crédito demonstrado com documento contábil e fiscal, não só com planilha
- [ ] DCTF/EFD/ECF coerentes com o crédito (retificadas antes, se preciso)
- [ ] Nenhum débito em vedação do § 3º
- [ ] Crédito judicial: trânsito, habilitação deferida e limite do art. 74-A conferidos
- [ ] Manifestação no prazo de 30 dias da ciência, com toda a prova documental
- [ ] Multa isolada enfrentada em tópico próprio

## Erros a evitar
- Transmitir DCOMP com crédito de ação ainda não transitada (vira "não declarada" e expõe à multa).
- Usar a DCOMP para débito já inscrito em dívida ativa.
- Defender só com teses jurídicas, sem provar liquidez e certeza do crédito.
- Citar a Súmula 212 do STJ como vigente.
- Confundir o prazo de homologação (5 anos da entrega) com o prazo para pedir o crédito (5 anos do art. 168).

## Integração com o núcleo
`juros-e-correcao`, `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`. Vizinhas: `trib-habilitacao-de-credito-judicial`, `trib-defesa-administrativa-e-carf` (recurso ao CARF após a DRJ), `trib-mandado-de-seguranca`.

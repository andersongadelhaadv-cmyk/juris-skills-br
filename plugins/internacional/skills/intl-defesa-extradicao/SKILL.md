---
name: intl-defesa-extradicao
description: >
  Redige a defesa do extraditando no processo de extradição passiva perante
  o STF (Lei 13.445/2017, arts. 81 a 99; CF, art. 5º, LI e LII, e art. 102,
  I, g), incluindo pedido de prisão domiciliar ou liberdade, controle da
  prisão cautelar para fins de extradição e exigência dos compromissos do
  Estado requerente. Use quando o usuário pedir defesa em extradição,
  impugnação a pedido de extradição, soltura de preso para extradição,
  alegação de crime político, prescrição, falta de dupla tipicidade,
  brasileiro nato ou refugiado, ou extradição voluntária.
metadata:
  area: internacional
  tipo_peca: contestacao
  verificado_em: 2026-11-25
---
# Defesa em processo de extradição (STF)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: extradição passiva (Estado estrangeiro pede a entrega de pessoa que está no Brasil) — defesa após o interrogatório, pedidos sobre a prisão, extradição voluntária, fase de entrega.
- Não usar: extradição ativa (Brasil pede a entrega) — é providência do juízo do processo penal brasileiro via órgão do Executivo (art. 88); expulsão ou deportação (medidas de retirada distintas, fora desta skill); cooperação para provas (`intl-cooperacao-auxilio-direto`); habeas corpus contra ato de outra autoridade (`penal-habeas-corpus`).

## Entradas mínimas (perguntar o que faltar; nunca supor fatos)
1. Nacionalidade do extraditando: brasileiro nato, naturalizado (data da naturalização x data do fato), estrangeiro; condição de refugiado ou asilado.
2. Estado requerente, tratado de extradição aplicável (ou promessa de reciprocidade) e cópia integral do pedido e dos documentos que o instruem.
3. Fatos imputados, tipificação estrangeira, pena cominada ou aplicada; datas dos fatos, do recebimento da acusação e da condenação (prescrição nos dois países).
4. O mesmo fato é objeto de processo, condenação ou absolvição no Brasil? O Brasil é competente para julgá-lo?
5. Natureza política ou de opinião do fato; tribunal de exceção no Estado requerente; risco de tortura, pena de morte ou perpétua.
6. Situação prisional: data da prisão cautelar, data da ciência do Estado e se o pedido formal veio em 60 dias (art. 84, § 4º).
7. Laços no Brasil, residência, trabalho, saúde (fundamentam pedido do art. 86 e adiamento do art. 95, § 1º).

## Prazo e contagem
- Defesa: **10 dias contados do interrogatório** (art. 91, § 1º).
- Pedido formal após prisão cautelar: 60 dias da ciência da prisão, salvo tratado (art. 84, § 4º); não formalizado, soltura (§ 5º).
- Diligência pedida pelo MPF: prazo improrrogável de 60 dias da notificação à missão diplomática (art. 91, §§ 3º e 4º).
- Retirada após autorização da entrega: 60 dias da comunicação; não retirado, liberdade (arts. 92 e 93).
- Contagem e prazos regimentais: `prazos-processuais` [VERIFICAR: RISTF não conferido].

## Estrutura da peça
Endereçamento ao relator no STF → qualificação → síntese do pedido → limites da defesa (art. 91, § 1º) → identidade → defeitos de forma → ilegalidade (vedações do art. 82, condições do art. 83) → compromissos do art. 96 → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Matéria de defesa (art. 91, § 1º):** identidade da pessoa reclamada, defeito de forma dos documentos, ilegalidade da extradição. Não se discute culpa ou prova do mérito da acusação estrangeira.
- **Vedações (art. 82):** brasileiro nato (I; CF, art. 5º, LI); fato não criminoso no Brasil ou no Estado requerente (II); competência brasileira para julgar o crime (III); pena de prisão inferior a 2 anos pela lei brasileira (IV); processo, condenação ou absolvição no Brasil pelo mesmo fato (V); prescrição por qualquer das duas leis (VI); crime político ou de opinião (VII; CF, art. 5º, LII), ressalvados §§ 1º e 4º; tribunal ou juízo de exceção (VIII); refugiado ou asilado territorial (IX).
- **Naturalizado:** só nas hipóteses da CF (§ 5º): crime comum anterior à naturalização ou envolvimento comprovado em tráfico ilícito de entorpecentes; observa-se a anterioridade do fato (§ 3º).
- **Condições (art. 83):** crime no território do Estado requerente ou sujeito à sua lei penal; extraditando processado ou condenado a pena privativa de liberdade lá.
- **Compromissos (art. 96)** como condição da entrega: não processar por fato anterior; detrair a prisão cumprida no Brasil; comutar pena corporal, perpétua ou de morte, respeitado o limite máximo de 30 anos previsto no inciso III [VERIFICAR: compatibilização com o atual art. 75 do Código Penal não conferida]; não reextraditar sem consentimento; não agravar por motivo político; não submeter a tortura ou tratamento cruel.
- **Laços familiares não impedem a extradição** (Súmula 421/STF) — use esses laços para o art. 86, não como obstáculo.
- **Habeas corpus contra omissão do relator** não é conhecido se baseado em fato ou direito estrangeiro sem prova nos autos e sem provocação prévia (Súmula 692/STF): **prove o direito estrangeiro e provoque o relator primeiro**.
- **Decisão do STF** sobre legalidade e procedência é irrecorrível (art. 90); negada a extradição, não cabe novo pedido pelo mesmo fato (art. 94).

## Fundamentos verificados
- CF art. 5º, LI e LII; art. 102, I, g.
- Lei 13.445/2017, arts. 81 a 99.
- Súmulas 421 e 692 do STF (vigência a conferir no portal do STF).
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Indeferimento da extradição pela vedação ou condição faltante específica.
- Prisão domiciliar, prisão-albergue ou resposta em liberdade com cautelas (art. 86).
- Soltura por falta de formalização no prazo (art. 84, §§ 4º e 5º) ou por não retirada (art. 93).
- Subsidiariamente: deferimento condicionado aos compromissos do art. 96 e à detração; adiamento da entrega por doença grave com laudo oficial (art. 95, § 1º) ou até o fim do processo/pena no Brasil (art. 95).
- Produção da prova do direito estrangeiro (texto e vigência da lei penal e das regras de prescrição).

## Checklist pré-protocolo
- [ ] Defesa dentro de 10 dias do interrogatório
- [ ] Nacionalidade e data de naturalização comprovadas
- [ ] Prescrição calculada pelas duas leis, com documentos do direito estrangeiro
- [ ] Dupla tipicidade e pena mínima do art. 82, IV, enfrentadas
- [ ] Bis in idem e competência brasileira (art. 82, III e V) verificados
- [ ] Prazo do art. 84, § 4º, conferido (se houve prisão cautelar)
- [ ] Compromissos do art. 96 pedidos subsidiariamente
- [ ] Pedido do art. 86 instruído (residência, trabalho, família, saúde)

## Erros a evitar
- Discutir autoria e prova da acusação estrangeira (fora do art. 91, § 1º).
- Basear a defesa só em cônjuge ou filho brasileiro (Súmula 421/STF).
- Alegar direito estrangeiro sem prová-lo nos autos (Súmula 692/STF).
- Esquecer a prescrição pela lei do Estado requerente (art. 82, VI admite qualquer das duas).
- Não pedir os compromissos do art. 96 como pedido subsidiário.

## Integração com o núcleo
`prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`. Vizinhas: `penal-habeas-corpus`, `penal-liberdade-provisoria-e-relaxamento`, `intl-cooperacao-auxilio-direto`.

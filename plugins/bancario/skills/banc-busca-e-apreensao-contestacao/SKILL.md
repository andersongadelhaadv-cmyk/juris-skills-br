---
name: banc-busca-e-apreensao-contestacao
description: >
  Redige a contestação (resposta) do devedor fiduciante na ação de busca e
  apreensão de veículo ou outro bem móvel alienado fiduciariamente (Decreto-Lei
  911/1969, art. 3º), com controle da comprovação da mora (Súmula 72 e Tema
  1.132/STJ), purgação pelo pagamento integral em 5 dias (Tema 722/STJ),
  descaracterização da mora por encargos abusivos da normalidade e pedido de
  restituição de valores. Use quando o usuário pedir defesa em busca e
  apreensão, carro apreendido pelo banco, liminar de apreensão de veículo
  financiado, "quero o carro de volta", notificação de mora inválida,
  contestação no DL 911 ou purgar a mora para recuperar o veículo.
metadata:
  area: bancario
  tipo_peca: contestacao
  verificado_em: 2026-11-25
---
# Contestação em busca e apreensão (DL 911/1969)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: ação **judicial** de busca e apreensão de bem móvel com alienação fiduciária (veículo, máquina, equipamento), liminar já cumprida ou por cumprir; também arrendamento mercantil com reintegração de posse, no que o DL 911 se aplica (art. 3º, § 15).
- Não usar:
  - Bem não encontrado e ação já **convertida em execução** (art. 4º), ou execução direta (art. 5º), ou cobrança do **saldo** após a venda → `banc-defesa-execucao-alienacao-fiduciaria`.
  - Procedimento **extrajudicial** em cartório ou órgão de trânsito (arts. 8º-B a 8º-E) → `banc-defesa-execucao-alienacao-fiduciaria`.
  - Imóvel (Lei 9.514/1997) → `imob-revisao-de-financiamento-sfh`.
  - Quer só depositar parcelas antes de qualquer ação → `banc-consignacao-e-purgacao-da-mora`.
  - Revisão ampla do contrato como ação autônoma → `consumidor-contratos-bancarios-revisional`.
  - Proposta de acordo com o banco → `banc-renegociacao-extrajudicial-de-divida`.

## Entradas mínimas (perguntar o que faltar; nunca supor fatos)
1. Contrato (cédula de crédito bancário ou equivalente), com taxa mensal, anual e, se houver capitalização diária, **taxa diária**; CET; tarifas e seguros.
2. Petição inicial, notificação extrajudicial (ou protesto) e comprovante de envio: **endereço usado x endereço do contrato**.
3. Data da execução da liminar (auto de apreensão) — dela correm os prazos.
4. Parcelas pagas, atrasadas e vincendas; planilha do credor que instruiu a inicial.
5. O cliente tem como pagar a **integralidade** da dívida em 5 dias? Quer o bem de volta ou só discutir valores?
6. Estado do bem, pertences dentro dele, se já houve venda ou transferência a terceiro.
7. Houve pagamentos não computados, renegociação ou acordo anterior?

## Prazo e contagem
- **Pagamento integral (purgação)**: 5 dias após a execução da liminar (art. 3º, §§ 1º e 2º). Termo inicial = execução da liminar (Tema 1.279/STJ). Natureza do prazo (material ou processual) e contagem: `prazos-processuais`.
- **Resposta**: 15 dias da execução da liminar (art. 3º, § 3º), mesmo se houve pagamento integral, para pedir restituição do que se pagou a mais (§ 4º).
- Consolidação: sem pagamento em 5 dias, propriedade e posse plena consolidam-se no credor (§ 1º) — a defesa não suspende isso por si.
- Apelação só no efeito devolutivo (art. 3º, § 5º).

## Estrutura da peça
Tempestividade → síntese → preliminares (mora não comprovada; inépcia/planilha) → mérito (descaracterização da mora; encargos abusivos; pagamentos não computados) → purgação (se houver depósito) → restituição e multa do § 6º → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Comprovação da mora é requisito da ação** (Súmula 72/STJ). Basta notificação enviada ao **endereço do contrato**, sem prova de recebimento pessoal (Tema 1.132/STJ; art. 2º, § 2º) — a tese defensiva útil é envio a endereço **diverso** do contratual, ausência de qualquer notificação ou protesto, ou notificação anterior ao vencimento.
- A notificação não precisa indicar o valor do débito (Súmula 245/STJ) — não alegue isso.
- Mora descaracterizada só por abusividade dos encargos do **período da normalidade** (juros remuneratórios e capitalização); encargos moratórios abusivos não afastam a mora.
- Abusividade dos encargos pode ser deduzida na contestação da busca e apreensão (AREsp 3.093.037, 4ª Turma, 2026).
- Ajuizar revisional, sozinho, não afasta a mora (Súmula 380/STJ).

## Fundamentos verificados
- DL 911/1969, arts. 2º (§§ 2º e 3º), 3º (§§ 1º a 8º e 15), 4º e 5º.
- CC, arts. 394, 396 e 401 (mora e sua purgação).
- Súmulas 72, 245 e 380 do STJ; Temas 722, 1.132 e 1.279 do STJ.
- Adimplemento substancial é incompatível com o DL 911 (REsp 2.195.400, 3ª Turma, 2025).
- Capitalização diária exige taxa diária expressa; sem ela, mora descaracterizada (REsp 2.241.205, 3ª Turma, 2025).
- Súmula 284/STJ (purga só com 40% pagos) é anterior à Lei 10.931/2004 e não rege contratos posteriores, regidos pelo Tema 722 [VERIFICAR: situação formal da súmula no portal do STJ].
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Acolhimento da preliminar: extinção sem mérito por falta de comprovação da mora e **restituição imediata do bem**.
- Reconhecimento da descaracterização da mora (encargos da normalidade abusivos), improcedência e devolução do bem.
- Se houve depósito integral em 5 dias: restituição do bem livre de ônus (art. 3º, § 2º) e restituição do que se pagou a mais (§ 4º).
- Improcedência com bem já vendido: multa de 50% do valor originalmente financiado, atualizado (§ 6º), sem prejuízo de perdas e danos (§ 7º). A multa não cabe se o pedido for julgado procedente (REsp 1.994.381, 3ª Turma, 2023).
- Exibição da planilha de evolução da dívida; perícia contábil se necessária.
- Juros e correção sobre restituições: núcleo `juros-e-correcao`.

## Checklist pré-protocolo
- [ ] Data da execução da liminar anotada e prazos de 5 e 15 dias calculados
- [ ] Endereço da notificação comparado ao do contrato
- [ ] Taxa diária conferida, se o contrato prevê capitalização diária
- [ ] Separados encargos da normalidade x encargos moratórios
- [ ] Decidido com o cliente: pagar a integralidade, depositar valor controvertido ou só contestar
- [ ] Pedido de restituição do bem e da multa do § 6º, se cabível
- [ ] Citações conferidas em `verificacao-de-citacoes`

## Erros a evitar
- Depositar só as parcelas vencidas como "purga" — exige-se a integralidade apresentada pelo credor (Tema 722).
- Invocar adimplemento substancial ("já paguei 90%") como tese principal.
- Alegar que a notificação não foi recebida pessoalmente, quando foi enviada ao endereço do contrato (Tema 1.132).
- Atacar só multa e juros moratórios esperando afastar a mora.
- Contar os 5 dias da citação ou da juntada do mandado, e não da execução da liminar.
- Prometer ao cliente que a contestação devolve o veículo sem depósito ou sem tese de mora.

## Integração com o núcleo
`prazos-processuais` (5 e 15 dias), `juros-e-correcao` (restituições e multa), `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

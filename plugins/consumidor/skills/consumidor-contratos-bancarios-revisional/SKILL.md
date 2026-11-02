---
name: consumidor-contratos-bancarios-revisional
description: >
  Redige ação revisional de contrato bancário de consumo (empréstimo, financiamento,
  cartão, cheque especial), com aplicação do CDC às instituições financeiras
  (Súmula 297 do STJ), controle de juros remuneratórios, capitalização, comissão
  de permanência e tarifas (Súmulas 382, 530, 539, 541, 472, 565 e 566 do STJ).
  Use quando o usuário pedir revisão de juros abusivos, revisional de financiamento
  de veículo, contestação de tarifas bancárias (TAC, TEC, cadastro), recálculo de
  parcelas, devolução de encargos cobrados a mais ou consignação incidental.
metadata:
  area: consumidor
  tipo_peca: inicial
  verificado_em: 2026-11-02
---
# Revisional de contrato bancário (consumo)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: contrato bancário com consumidor (pessoa física ou PJ vulnerável) em que se discutem encargos específicos e documentados.
- Não usar: dívidas múltiplas comprometendo o mínimo existencial (`consumidor-superendividamento`); contrato inexistente/fraude (`consumidor-negativacao-indevida` ou `consumidor-acao-indenizatoria`); crédito rural, cédulas com regime próprio e SFH — exigem adaptação.
- **Atenção:** a suficiência da taxa média do Bacen como critério exclusivo de abusividade está afetada ao **Tema 1378/STJ**, com suspensão determinada (art. 1.037, II, CPC). Avaliar o sobrestamento antes de ajuizar e informar o cliente.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Cópia integral do contrato (ou pedido de exibição), data de celebração, modalidade, valor financiado, prazo, parcelas pagas.
2. Taxas mensal e anual pactuadas, CET, encargos de mora, tarifas e seguros cobrados (com valores).
3. Taxa média de mercado do Bacen para a modalidade e o mês da contratação.
4. **Peculiaridades do caso** que demonstrem a abusividade além da comparação com a média: perfil do cliente, garantias, risco, relacionamento, situação econômica, custo de captação.
5. Planilha de evolução da dívida e cálculo do valor incontroverso.
6. Há mora? Há busca e apreensão/execução em curso?

## Prazo e contagem
- Revisional com repetição de indébito: prescrição decenal (art. 205 CC), por ser pretensão de natureza pessoal (REsp 2.230.380).
- Valor incontroverso deve ser discriminado na inicial, sob pena de inépcia (CPC 330 §§ 2º e 3º), e continuar sendo pago.
- Prazos processuais em dias úteis: `prazos-processuais`.

## Estrutura da peça
Fatos e contrato → CDC aplicável → cláusulas impugnadas (uma por tópico, com parâmetro) → valor incontroverso → descaracterização da mora (se encargos da normalidade abusivos) → tutela (consignação/abstenção) → repetição → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **O juiz não conhece de ofício a abusividade** em contrato bancário (Súmula 381): impugnar cada cláusula expressamente.
- Indicar as obrigações controvertidas e quantificar o incontroverso (CPC 330 § 2º).
- Ausente o contrato nos autos: pedir exibição; sem prova da taxa pactuada aplica-se a taxa média, salvo se a cobrada for mais vantajosa (Súmula 530).

## Fundamentos verificados
- Súmula 297 (CDC aplicável), 381 (sem conhecimento de ofício), 382 (juros acima de 12% a.a. não são, por si, abusivos), 530 (taxa média na falta de contrato), 539 e 541 (capitalização), 472 (comissão de permanência), 565 e 566 (TAC/TEC e tarifa de cadastro).
- Tema 27/STJ (REsp 1.061.530/RS): revisão de juros remuneratórios só em situação excepcional, com abusividade cabalmente demonstrada pelas peculiaridades do caso concreto; taxa média do Bacen é referencial, não critério absoluto.
- Tema 958/STJ: tarifa de avaliação do bem e despesa de registro são válidas, salvo serviço não prestado ou onerosidade excessiva no caso.
- CDC arts. 6º V, 39 V, 51 IV e § 1º, 52, 54-B (CET).
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Revisão de cada cláusula, com o parâmetro substitutivo e sua justificativa.
- Recálculo do saldo e das parcelas; compensação/repetição do indébito (dobro: ver `consumidor-repeticao-em-dobro` e modulação).
- Tutela: autorização de depósito do incontroverso, abstenção de negativação e manutenção na posse (requisitos rigorosos — a simples propositura não afasta a mora).
- Exibição de documentos; perícia contábil.
- Juros/correção sobre o indébito: `juros-e-correcao` (nunca escrever taxa própria).

## Checklist pré-protocolo
- [ ] Contrato completo juntado (ou exibição requerida)
- [ ] Tema 1378 avaliado (suspensão) e cliente informado
- [ ] Cada cláusula impugnada em tópico próprio (Súmula 381)
- [ ] Peculiaridades do caso descritas (não só a comparação com a média)
- [ ] Data do contrato confrontada com 30/04/2008 para tarifas
- [ ] Capitalização: verificada pactuação expressa (Súmulas 539/541)
- [ ] Valor incontroverso quantificado e planilha anexa
- [ ] Juros/correção do indébito remetidos ao núcleo

## Erros a evitar
- Pedir limitação de juros a 12% ao ano (Súmula 382 e Tema 27/STJ).
- Usar apenas "taxa acima da média do Bacen" como prova de abusividade.
- Impugnar capitalização quando o contrato prevê taxa anual superior ao duodécuplo da mensal (Súmula 541).
- Contestar tarifa de cadastro cobrada no início do relacionamento em contrato posterior a 30/04/2008 (Súmula 566).
- Deixar de pagar o incontroverso e perder a tutela.

## Integração com o núcleo
`juros-e-correcao`, `prazos-processuais`, `verificacao-de-citacoes` (todo precedente sobre o Tema 1378 deve ser checado na data do protocolo), `fidelidade-factual`, `estilo-forense`.

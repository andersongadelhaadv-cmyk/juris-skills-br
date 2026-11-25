---
name: trabalhista-verbas-rescisorias
description: >
  Roteiro de cálculo e conferência das verbas rescisórias por modalidade de
  extinção (sem justa causa, justa causa, pedido de demissão, acordo do art.
  484-A, culpa recíproca, término e rompimento antecipado de contrato a prazo),
  com saldo de salário, aviso prévio proporcional (Lei 12.506/2011), 13º
  proporcional (Lei 4.090/1962), férias vencidas e proporcionais com 1/3, FGTS
  e indenização de 40% ou 20% (Lei 8.036/1990, art. 18), prazo de 10 dias e
  multas dos arts. 477 §8º e 467 da CLT. Use quando o usuário pedir cálculo de
  rescisão, conferência de TRCT, quanto o empregado tem a receber na demissão,
  verbas rescisórias devidas ou checar se a rescisão foi paga certo.
metadata:
  area: trabalhista
  tipo_peca: outro
  verificado_em: 2026-11-25
---
# Cálculo e conferência de verbas rescisórias

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: montar ou conferir o TRCT de uma extinção contratual (empregador, empregado ou advogado de qualquer lado), antes do pagamento ou para instruir ação/defesa.
- Não usar: conta de liquidação de sentença (use `trabalhista-impugnacao-de-calculos`); acordo sobre as verbas com homologação (use `trabalhista-acordo-extrajudicial`); discutir se houve justa causa ou rescisão indireta (use `trabalhista-rescisao-indireta` e `trabalhista-contestacao`); benefício previdenciário decorrente da extinção (use `prev-*`).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Admissão, último dia trabalhado, data da comunicação e modalidade de extinção.
2. Aviso prévio: trabalhado, indenizado ou dispensado; quem deu.
3. Salário-base e médias de variáveis habituais (horas extras, comissões, adicionais) — compõem a base.
4. Períodos de férias: gozadas, vencidas (simples ou em dobro), faltas injustificadas por período (art. 130).
5. 13º já adiantado no ano; adiantamentos e descontos a compensar.
6. Saldo do FGTS para fins rescisórios (extrato) e depósitos em atraso.
7. Contrato a prazo: termo final previsto e cláusula de rescisão antecipada, se houver.
8. Norma coletiva (pode prever verbas ou indenizações adicionais).

## Prazo e contagem
- Pagamento e entrega dos documentos de comunicação da extinção em **até 10 dias do término do contrato** (art. 477 §6º); atraso gera multa equivalente a um salário, salvo mora causada pelo empregado (art. 477 §8º), inclusive se o vínculo só for reconhecido em juízo (Súmula 462 do TST).
- Aviso prévio: 30 dias até 1 ano, mais 3 dias por ano completo, até 90 dias (Lei 12.506/2011, art. 1º); só para rescisões a partir de 13/10/2011 (Súmula 441 do TST). O aviso indenizado integra o tempo de serviço (art. 487 §1º) — projeta 13º e férias.
- Frações: 13º conta mês com 15 dias ou mais (Lei 4.090/1962, art. 1º §2º); férias proporcionais contam fração superior a 14 dias (art. 146 parágrafo único).
- Prazos processuais: `prazos-processuais`.

## Estrutura do cálculo
Dados do contrato → modalidade → quadro de verbas devidas → base de cálculo de cada verba → projeção do aviso → descontos e compensação (limite de um salário, art. 477 §5º) → FGTS e indenização → conferência com o TRCT → multas. Detalhe em [estrutura](references/estrutura.md).

## Quadro por modalidade (verbas típicas; conferir a norma coletiva)
- **Sem justa causa**: saldo de salário; aviso prévio (trabalhado ou indenizado, proporcional); 13º proporcional (Lei 4.090, art. 3º); férias vencidas e proporcionais + 1/3 (arts. 146-147; CF art. 7º, XVII); FGTS do mês e do anterior não recolhidos + indenização de 40% sobre todos os depósitos do contrato (Lei 8.036, art. 18, caput e §1º).
- **Justa causa** (art. 482): saldo de salário; férias vencidas + 1/3. Sem férias proporcionais (art. 146 parágrafo único; Súmula 171 do TST), sem aviso e sem a indenização do FGTS. 13º proporcional: a Lei 4.090 o assegura na rescisão sem justa causa (art. 3º) — não incluir na justa causa sem fundamento específico.
- **Pedido de demissão**: saldo; 13º proporcional (Súmula 157 do TST); férias vencidas e proporcionais + 1/3, mesmo com menos de 1 ano (Súmula 261 do TST); aviso prévio a cumprir pelo empregado ou desconto (art. 487 §2º); sem indenização do FGTS.
- **Acordo (art. 484-A)**: metade do aviso prévio indenizado e metade da indenização sobre o FGTS (20%); demais verbas integrais; saque de até 80% do FGTS; sem seguro-desemprego.
- **Culpa recíproca** (art. 484): 50% do aviso, do 13º e das férias proporcionais (Súmula 14 do TST); indenização do FGTS de 20% (Lei 8.036, art. 18 §2º).
- **Contrato a prazo — término no termo**: saldo, 13º e férias proporcionais (Lei 4.090, art. 1º §3º; art. 147); sem aviso e sem indenização do art. 479.
- **Contrato a prazo — dispensa antecipada pelo empregador**: além das proporcionais, indenização de metade da remuneração até o termo (art. 479). Pelo empregado: indeniza o empregador dos prejuízos, até o limite do art. 480 §1º.

## Fundamentos verificados
- CLT arts. 130, 146, 147, 467, 477 (§§2º, 4º, 5º, 6º, 8º), 479, 480, 482, 484, 484-A, 487.
- CF art. 7º, XVII e XXI; Lei 12.506/2011, art. 1º; Lei 4.090/1962, arts. 1º e 3º; Lei 8.036/1990, art. 18.
- TST: Súmulas 14, 157, 171, 261, 441, 462.
Detalhe em [fundamentos](references/fundamentos.md).

## Tributos, juros e correção
- INSS e IRRF sobre as verbas: usar a tabela oficial vigente na competência, buscada na fonte oficial no dia; **nunca de memória**. Indicar quais verbas a lei trata como indenizatórias apenas com fonte conferida [VERIFICAR: natureza tributária de cada verba não conferida nesta skill].
- Atualização de valores pagos com atraso ou cobrados em juízo: exclusivamente pelo núcleo `juros-e-correcao`.

## Checklist de conferência
- [ ] Modalidade de extinção definida e documentada
- [ ] Aviso proporcional calculado pelos anos completos e projetado
- [ ] Médias de variáveis habituais na base (art. 487 §5º para horas extras no aviso)
- [ ] Férias: períodos vencidos (simples/dobro) e proporcionais com faltas do art. 130
- [ ] 13º descontado o adiantamento
- [ ] Compensações até um salário (art. 477 §5º)
- [ ] FGTS: depósitos em atraso e indenização no percentual certo
- [ ] TRCT discrimina natureza e valor de cada parcela (art. 477 §2º)
- [ ] Data do pagamento dentro de 10 dias (art. 477 §6º)
- [ ] Parcela incontroversa separada, se houver litígio (art. 467)

## Erros a evitar
- Calcular o aviso proporcional contando frações de ano como ano completo, ou esquecer a projeção no 13º e nas férias.
- Pagar férias proporcionais na justa causa (ou negá-las no pedido de demissão com menos de 1 ano).
- Aplicar 40% de FGTS no acordo do art. 484-A ou na culpa recíproca.
- Usar tabela de INSS/IR "de cabeça" ou de ano errado.
- Contar o prazo de 10 dias a partir do fim do aviso trabalhado quando o aviso foi indenizado, sem conferir o termo do contrato.
- Quitação genérica no TRCT: só vale para as parcelas especificadas (art. 477 §2º).

## Integração com o núcleo
`juros-e-correcao` (atualização e encargos), `prazos-processuais`, `fidelidade-factual`, `verificacao-de-citacoes`, `estilo-forense`.

---
name: civel-execucao-titulo-extrajudicial
description: >
  Redige petição inicial de execução de título extrajudicial por quantia certa
  (CPC arts. 784, 798, 829 e seguintes), com demonstrativo do débito, indicação
  de bens, averbação (art. 828) e pedido fundamentado de medidas executivas
  atípicas (art. 139, IV, conforme Tema 1137 do STJ). Use quando o usuário pedir
  ação de execução, executar cheque, nota promissória, duplicata, contrato com
  testemunhas, aluguel, condomínio, confissão de dívida, ou pedir bloqueio de
  CNH, passaporte ou cartões.
metadata:
  area: processo-civil
  tipo_peca: execucao
  verificado_em: 2026-11-01
---
# Execução de título extrajudicial

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: título do art. 784 (cambiais e cheque; escritura ou documento público; documento particular com duas testemunhas; transação referendada; contratos com garantia real; aluguel e encargos; condomínio; seguro de vida; títulos eletrônicos com assinatura válida — §4º; outros por lei).
- Também para entrega de coisa (art. 806) e obrigação de fazer (art. 815), adaptando o rito.
- Não usar: título judicial (`civel-cumprimento-de-sentenca`); documento sem força executiva (`civel-acao-monitoria`); execução fiscal (skill fazendária); juizado (até 40 SM — Lei 9.099, art. 53, ver `civel-juizado-especial`).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
- Título original (ou eletrônico com assinatura conferível) e vencimento.
- Valores, pagamentos parciais, encargos contratados (sem presumir taxa).
- Executados (devedor, avalistas, fiadores, garantidores) com CPF/CNPJ.
- Bens conhecidos; garantias reais; prova de condição/termo ou de contraprestação.
- Histórico de tentativas de cobrança (para medidas atípicas).

## Prazo e contagem
- Prescrição da pretensão executiva conforme o título (cheque, promissória, contrato) — conferir em `prazos-processuais`.
- Executado: 3 dias para pagar (art. 829); pagamento integral nesse prazo reduz honorários à metade (art. 827, §1º); 15 dias para embargos (art. 915).
- Comunicar averbações em 10 dias (art. 828, §1º).
- Prescrição intercorrente (art. 921, §§1º a 5º).

## Estrutura da peça
Endereçamento → partes → título e exigibilidade → demonstrativo (art. 798, p.ú.) → pedido de citação para pagar em 3 dias → honorários (art. 827) → penhora e bens (art. 835) → averbação (art. 828) → medidas atípicas (subsidiárias) → valor da causa → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Art. 798, I: título; demonstrativo atualizado; prova da condição/termo; prova da contraprestação.
- Art. 798, II: espécie de execução preferida; nomes e CPF/CNPJ; bens penhoráveis, se possível.
- Demonstrativo (p.ú.): índice, taxa de juros, termos inicial e final, capitalização, descontos.
- Obrigação certa, líquida e exigível, sob pena de nulidade (art. 803, I). Inicial incompleta: emenda em 15 dias (art. 801).
- Intimações obrigatórias de terceiros com direitos sobre o bem penhorado (art. 799).

## Fundamentos verificados
CPC arts. 139, IV, 774, 784, 792, 798, 799, 801, 803, 805, 827 a 830, 833, 835, 854, 921; STF, ADI 5.941/DF (constitucionalidade do art. 139, IV); Tema 1137 do STJ; Súmula 375 do STJ. Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Citação para pagar em 3 dias, com ordem de penhora e avaliação (art. 829, §1º); arresto se não encontrado o executado (art. 830).
- Fixação de honorários de 10% (art. 827).
- Bloqueio de ativos (art. 854) e penhora na ordem do art. 835.
- Certidão para averbação (art. 828).
- Medidas atípicas, em caráter subsidiário e fundamentado (Tema 1137).
- Intimação do executado para indicar bens, sob pena de ato atentatório (art. 774, V).

## Checklist pré-protocolo
- [ ] Título no rol do art. 784, exigível e no prazo prescricional.
- [ ] Demonstrativo completo (art. 798, p.ú.), gerado com `juros-e-correcao` e com os encargos efetivamente contratados.
- [ ] Todos os coobrigados qualificados.
- [ ] Bens indicados e terceiros do art. 799 a intimar.
- [ ] Medidas atípicas só depois das típicas, com fundamentação concreta.
- [ ] Valor da causa = débito atualizado.

## Erros a evitar
- Demonstrativo sem os itens do art. 798, p.ú. (emenda ou extinção).
- Aplicar juros de 1% ao mês por padrão: usar a taxa contratada válida ou o regime legal do núcleo.
- Pedir CNH/passaporte de saída, sem esgotar meios típicos e sem demonstrar ocultação patrimonial ou utilidade da medida.
- Esquecer de comunicar averbações em 10 dias ou não cancelar as excedentes (art. 828, §§1º, 2º e 5º).
- Título eletrônico sem verificação da assinatura (art. 784, §4º).

## Integração com o núcleo
- `juros-e-correcao` (obrigatório) para o demonstrativo.
- `prazos-processuais` para prescrição, citação, embargos e prescrição intercorrente.
- `verificacao-de-citacoes` para o Tema 1137 e precedentes sobre o título.
- `fidelidade-factual` para os dados do título.
- `estilo-forense` na revisão.

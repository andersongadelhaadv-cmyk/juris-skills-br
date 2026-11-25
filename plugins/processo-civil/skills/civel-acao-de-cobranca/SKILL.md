---
name: civel-acao-de-cobranca
description: >
  Redige petição inicial de ação de cobrança pelo procedimento comum, depois de
  escolher a via certa entre execução de título extrajudicial, monitória e
  cobrança (CPC, arts. 700 e 784), com prescrição do CC (arts. 205 e 206),
  constituição em mora (art. 397), valor da causa do art. 292, I, e memória de
  cálculo. Use quando o usuário pedir ação de cobrança, cobrar dívida de
  contrato verbal ou sem título, cobrar serviço prestado e não pago, cobrar
  empréstimo entre particulares, saldo de compra e venda, reembolso de
  despesas ou "o devedor não paga e não tenho título executivo".
metadata:
  area: processo-civil
  tipo_peca: inicial
  verificado_em: 2026-11-25
---
# Ação de cobrança (procedimento comum)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar quando há crédito em dinheiro exigível e **não há título executivo** (CPC, art. 784) nem prova escrita apta para a monitória — ou quando, havendo prova escrita, a liquidez depende de instrução (perícia, testemunha).
- Triagem obrigatória antes de redigir:
  1. Há título do art. 784 (cheque, nota promissória, duplicata, documento particular assinado pelo devedor e por 2 testemunhas, escritura pública etc.)? → `civel-execucao-titulo-extrajudicial`.
  2. Há prova escrita sem eficácia de título (art. 700: e-mail de reconhecimento, cheque prescrito, contrato sem testemunhas)? → avalie `civel-acao-monitoria`; prefira cobrança se a prova for frágil (art. 700, § 5º, manda emendar para o procedimento comum).
  3. Valor e partes cabem no juizado? → `civel-juizado-especial`.
- Não usar: taxa condominial (`imob-cobranca-de-taxas-condominiais`); aluguel (`imob-acao-de-despejo`); multa contratual como tema central (`contratos-clausula-penal`); relação de consumo em que o consumidor é o autor (`consumidor-repeticao-em-dobro`); crédito contra a Fazenda (`fazenda-*`).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Origem do crédito (contrato escrito ou verbal, serviço, venda, mútuo, reembolso) e documentos que o provam.
2. Valor principal, vencimento de cada parcela e o que já foi pago (datas e comprovantes).
3. Há termo de vencimento? Se não, houve interpelação (data e meio)? (CC, art. 397).
4. Encargos contratados: multa, juros convencionais, índice de correção, honorários contratuais.
5. Cobranças extrajudiciais feitas e respostas do devedor (reconhecimento interrompe a prescrição — art. 202, VI).
6. Bens conhecidos do devedor e risco de dilapidação (para tutela de urgência ou arresto).
7. Qualificação completa do devedor e de eventuais fiadores ou coobrigados.

## Prazo e contagem
- Prescrição (conferir o enquadramento antes de redigir):
  - Dívida líquida constante de instrumento público ou particular: 5 anos (CC, art. 206, § 5º, I).
  - Honorários de profissional liberal: 5 anos da conclusão dos serviços ou cessação do contrato (art. 206, § 5º, II).
  - Título de crédito: 3 anos do vencimento, ressalvada lei especial (art. 206, § 3º, VIII).
  - Pretensão contratual sem prazo específico: 10 anos (art. 205), na linha da 2ª Seção do STJ (AgInt nos EREsp 1.685.808, 2024).
  - Enriquecimento sem causa: 3 anos (art. 206, § 3º, IV).
- Interrupção: despacho que ordena a citação, protesto, reconhecimento pelo devedor (art. 202); uma única vez.
- Prazos processuais e contagem: `prazos-processuais`.

## Estrutura da peça
Endereçamento → qualificação → síntese → fatos (origem, inadimplemento, cobranças) → fundamentos (existência do crédito, exigibilidade, mora) → tutela provisória → pedidos → provas → valor da causa com memória → audiência. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Foro**: domicílio do réu (CPC, art. 46) ou lugar onde a obrigação deve ser satisfeita (art. 53, III, "d"); conferir cláusula de eleição.
- **Liquidez**: apresentar memória de cálculo com principal, abatimentos e encargos até a propositura (art. 292, I). Pedido genérico só nas hipóteses do art. 324, § 1º.
- **Mora**: obrigação positiva e líquida com termo constitui em mora de pleno direito (CC, art. 397); sem termo, exige interpelação (parágrafo único) — junte a notificação.
- **Coobrigados**: fiador e devedor solidário no polo passivo se quiser título contra eles.

## Fundamentos verificados
CC arts. 205, 206 (§ 3º, IV e VIII; § 5º, I e II), 202, 940, 941, 389, 394, 395, 397, 402, 404; CPC arts. 46, 53, 85, 292, 300, 311, 319, 324, 700, 784. Precedente: STJ, 2ª Seção, prazo decenal da pretensão contratual. Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Condenação ao pagamento do principal, com correção, juros, multa contratual (se houver) e honorários; índice, taxa e termo inicial pelo núcleo `juros-e-correcao` (não escrever taxa fixa na peça).
- Prestações vincendas incluídas no pedido, se a obrigação for periódica (art. 292, §§ 1º e 2º).
- Tutela da evidência (art. 311, IV) se a prova documental for robusta; tutela de urgência cautelar (arresto) se houver risco concreto de dilapidação (art. 300).
- Citação; custas e honorários (art. 85); provas.

## Checklist pré-protocolo
- [ ] Triagem feita: não há título executivo; monitória descartada com motivo
- [ ] Prescrição enquadrada no inciso certo, com data-limite anotada
- [ ] Memória de cálculo anexa, com abatimentos e data-base
- [ ] Prova da mora (termo contratual ou interpelação)
- [ ] Coobrigados no polo passivo
- [ ] Encargos pedidos apenas se contratados; correção e juros pelo núcleo
- [ ] Valor da causa = soma do art. 292, I (e vincendas, se houver)

## Erros a evitar
- Ajuizar cobrança tendo título executivo: falta de interesse ou, no mínimo, perda de tempo.
- Enquadrar como reparação civil (3 anos) uma pretensão contratual e reconhecer prescrição que não existe — ou o inverso.
- Pedir juros "de 1% ao mês" ou escolher índice por memória: usar `juros-e-correcao`.
- Esquecer o abatimento de pagamentos parciais: quem demanda dívida já paga sem ressalvar o recebido paga o dobro, e quem pede mais do que o devido paga o equivalente ao que exigiu (CC, art. 940), salvo desistência antes da contestação (art. 941). O STJ exige má-fé para essa sanção (AREsp 3.058.724, 3ª Turma, 2025).
- Valor da causa sem os juros vencidos e penalidades até a propositura (art. 292, I).

## Integração com o núcleo
`juros-e-correcao` (obrigatório para a memória de cálculo), `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

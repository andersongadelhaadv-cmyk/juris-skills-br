---
name: trib-embargos-a-execucao-fiscal
description: >
  Redige embargos à execução fiscal (LEF arts. 16 a 20), com garantia prévia do
  juízo (art. 16, §1º), prazo de 30 dias e concentração de toda a defesa
  (art. 16, §2º). Use quando o usuário pedir embargos à execução fiscal, embargos
  do devedor contra a Fazenda, defesa em execução fiscal garantida, impugnar CDA
  após penhora, depósito, seguro garantia ou fiança, ou pedir efeito suspensivo
  na execução fiscal.
metadata:
  area: tributario-fazenda
  tipo_peca: embargos-execucao
  verificado_em: 2026-11-01
---
# Embargos à execução fiscal

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: execução fiscal (dívida ativa tributária ou não tributária) já garantida por depósito, fiança, seguro garantia ou penhora; defesa que exija prova (perícia, testemunhas) ou matéria ampla.
- Não usar: matéria de ordem pública com prova pronta e sem garantia (use `trib-excecao-pre-executividade-fiscal`); prescrição intercorrente pura (veja `trib-prescricao-intercorrente`); embargos da Fazenda como devedora (use `fazenda-cumprimento-contra-a-fazenda`).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
- Cópia integral da execução, CDA(s) e processo administrativo de origem.
- Tipo de garantia e data do evento que inicia o prazo (depósito, juntada da fiança/seguro, intimação da penhora).
- Se a garantia é integral; se houve reforço ou substituição.
- Teses: nulidade da CDA, ilegitimidade (sócio redirecionado), decadência, prescrição, pagamento, parcelamento, mérito do tributo, excesso.
- Ação anulatória ou MS anterior sobre o mesmo crédito (litispendência/conexão).

## Prazo e contagem
- 30 dias contados do depósito, da juntada da prova da fiança ou seguro, ou da intimação da penhora (LEF art. 16, I a III).
- Contagem em dias úteis ou corridos: há divergência na aplicação do CPC art. 219 à LEF [VERIFICAR posição atual do tribunal local e do STJ]. Por segurança, protocole dentro de 30 dias corridos.
- Impugnação da Fazenda: 30 dias (LEF art. 17). Use `prazos-processuais`.

## Estrutura da peça
Endereçamento ao juízo da execução (ou deprecado, art. 20) → partes → tempestividade e garantia → efeito suspensivo → preliminares e nulidades da CDA → prejudiciais (decadência, prescrição) → ilegitimidade → mérito → excesso → provas → pedidos. Roteiro em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Garantia prévia: sem ela, não se admitem embargos (art. 16, §1º). Garantia insuficiente: peça prazo para reforço em vez de deixar o prazo correr.
- Toda a defesa no prazo (art. 16, §2º): requerer provas, juntar documentos e rol de até 3 testemunhas.
- Não cabem reconvenção nem compensação como pedido (art. 16, §3º); a compensação de IR retido com restituição apurada na declaração é admitida (Súmula 394 STJ). Exceções de suspeição, incompetência e impedimento correm à parte.
- Efeito suspensivo: não é automático; requer garantia e requisitos de tutela provisória (CPC art. 919, §1º, aplicado subsidiariamente).
- Seguro garantia e fiança só são liquidados após o trânsito em julgado de decisão de mérito desfavorável ao contribuinte (LEF art. 9º, §7º, Lei 14.689/2023).
- CDA: requisitos do LEF art. 2º, §5º e CTN art. 202 (redação LC 236/2026); emenda ou substituição até a sentença dos embargos, sem trocar o sujeito passivo (Súmula 392 STJ; CTN art. 203).
- Meação do cônjuge: só responde se provado que o ilícito beneficiou o casal (Súmula 251 STJ).
- Impenhorabilidade de até 40 salários mínimos em conta não é reconhecida de ofício: alegue tempestivamente (Tema 1235 STJ).

## Fundamentos verificados
LEF arts. 2º, 3º, 8º, 9º, 12, 15 a 20; CTN arts. 135, 142, 150, 173, 174, 202 a 204; CPC arts. 496, II, e 919; Súmulas 251, 392, 394, 409, 430, 435 STJ; Tema 1235 STJ. Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Recebimento com efeito suspensivo (garantia + relevância + risco).
- Intimação da Fazenda para impugnar (art. 17).
- Extinção da execução (nulidade da CDA, decadência, prescrição, ilegitimidade) ou redução ao valor devido, com planilha.
- Produção de provas (perícia, documentos, até 3 testemunhas).
- Liberação da garantia e honorários contra a Fazenda (CPC art. 85, §3º).

## Checklist pré-protocolo
- [ ] Data do termo inicial do art. 16 comprovada; prazo contado de forma conservadora.
- [ ] Garantia integral nos autos; se insuficiente, pedido de reforço antes do fim do prazo.
- [ ] Todas as teses e provas na inicial (art. 16, §2º); rol de testemunhas juntado.
- [ ] CDA conferida item a item (art. 2º, §5º da LEF; art. 202 do CTN).
- [ ] Decadência e prescrição calculadas com `prazos-processuais`.
- [ ] Sem pedido de compensação (salvo Súmula 394 STJ) nem reconvenção.

## Erros a evitar
- Embargar sem garantia ou deixar o prazo correr esperando decisão sobre reforço.
- Reservar teses para depois: preclusão.
- Pedir efeito suspensivo sem demonstrar os requisitos da tutela.
- Tratar o seguro garantia como liquidável antes do trânsito (LEF art. 9º, §7º).
- Calcular excesso com índice próprio: use `juros-e-correcao`.

## Integração com o núcleo
- `prazos-processuais`: termo inicial do art. 16 e prescrição.
- `juros-e-correcao`: cálculo do excesso e dos encargos.
- `verificacao-de-citacoes`: todo precedente acrescentado.
- `fidelidade-factual`: datas de penhora, intimações e pagamentos.
- `estilo-forense`: revisão final.

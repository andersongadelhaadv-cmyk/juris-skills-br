---
name: familia-execucao-de-alimentos
description: >
  Redige o requerimento de cumprimento de sentença ou execução de alimentos pelo rito da
  prisão ou da expropriação (CPC arts. 528 a 533 e 911 a 913), com protesto, desconto em
  folha e inscrição em cadastros. Use quando o usuário pedir execução de alimentos, cobrança
  de pensão atrasada, prisão do devedor de alimentos, cumprimento de sentença de alimentos,
  rito da prisão, rito da penhora, desconto em folha da pensão ou protesto da pensão.
metadata:
  area: familia-sucessoes
  tipo_peca: execucao
  verificado_em: 2026-11-01
---
# Execução / cumprimento de sentença de alimentos

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: alimentos fixados em sentença, decisão interlocutória (provisórios), acordo homologado ou título extrajudicial (escritura, acordo referendado) e não pagos.
- Não usar: defesa do devedor (justificativa) — a skill traz um roteiro curto em [estrutura](references/estrutura.md), mas a impugnação geral segue o processo civil; pedido de redução (use `familia-revisional-e-exoneracao-de-alimentos`).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Título: cópia da decisão/sentença/acordo, data, valor ou percentual, base de incidência.
2. Parcelas vencidas: mês a mês, valor devido, valor pago, saldo.
3. Data pretendida de ajuizamento (define as 3 parcelas do rito da prisão).
4. Empregador ou fonte pagadora do devedor; bens conhecidos; endereço para intimação pessoal.
5. Se o título é judicial (CPC 528) ou extrajudicial (CPC 911).

## Prazo e contagem
- Devedor intimado pessoalmente tem 3 dias para pagar, provar que pagou ou justificar (CPC 528 caput; 911 caput para título extrajudicial).
- Prisão por prazo entre um e três meses; o cumprimento é no regime fechado, apartado dos demais presos (CPC 528 §§3º e 4º).
- Prescrição das prestações: 2 anos a partir de cada vencimento (CC 206 §2º), mas não corre entre ascendentes e descendentes durante o poder familiar (CC 197, II) — confirmar caso a caso.
- Contagem em dias úteis via `prazos-processuais`.

## Estrutura da peça
Endereçamento → qualificação → título e débito → escolha do rito (prisão, expropriação ou ambos em requerimentos separados) → cálculo discriminado → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Rito da prisão: alcança apenas as três parcelas vencidas imediatamente antes do protocolo, somadas às que vencerem durante o processo (CPC 528 §7º; Súmula 309 STJ). Parcelas mais antigas vão pelo rito da expropriação.
- Rito da expropriação (CPC 528 §8º e 530; 913 no extrajudicial): sem prisão; penhora em dinheiro permite levantamento mensal mesmo com efeito suspensivo.
- Competência: juízo da sentença ou domicílio do exequente (CPC 528 §9º).
- Provisórios ou sentença não transitada: autos apartados (CPC 531 §1º).
- A jurisprudência do STJ admite cumular os dois ritos no mesmo processo se não houver prejuízo ao devedor nem tumulto, exigindo discriminação dos débitos por rito (precedentes conferidos em [fundamentos](references/fundamentos.md)).

## Fundamentos verificados
CF art. 5º, LXVII; CPC 528 a 533, 911 a 913, 517 (protesto), 782 §§3º e 5º (cadastros de inadimplentes); Súmula 309 STJ (redação de 2006); CC 1.707 (crédito incompensável). Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- [ ] Intimação pessoal do executado para pagar em 3 dias.
- [ ] Protesto do pronunciamento judicial (CPC 528 §1º e 517).
- [ ] Decretação da prisão civil, em regime fechado (CPC 528 §§3º e 4º), se não houver pagamento ou justificativa aceita.
- [ ] Desconto em folha das parcelas vincendas e do débito, parcelado, sem ultrapassar 50% dos ganhos líquidos (CPC 529 §3º).
- [ ] Inclusão do nome em cadastros de inadimplentes (CPC 782 §§3º e 5º).
- [ ] No rito da expropriação: penhora on-line, levantamento mensal (CPC 528 §8º).
- [ ] Ciência ao MP de indícios de abandono material, se houver conduta procrastinatória (CPC 532).
- [ ] Atualização do débito pelo núcleo `juros-e-correcao`.

## Checklist pré-protocolo
- [ ] Planilha com cada parcela, vencimento, pagamento parcial e saldo.
- [ ] Separação clara: parcelas do rito da prisão x parcelas do rito da expropriação.
- [ ] Título juntado com certidão de intimação/trânsito, quando houver.
- [ ] Endereço atualizado para intimação pessoal.
- [ ] Dados do empregador para ofício de desconto (CPC 529 §2º: nomes, CPFs, valor, duração, conta).

## Erros a evitar
- Incluir no rito da prisão parcelas anteriores às 3 últimas antes do ajuizamento.
- Escrever "prisão em regime semiaberto" ou "domiciliar" como regra: o CPC 528 §4º manda regime fechado (a substituição é excepcional e decidida pelo juiz).
- Planilha sem abater pagamentos parciais (abre espaço para justificativa e excesso).
- Pedir prisão na execução de alimentos indenizatórios por ato ilícito sem verificar o entendimento atual do tribunal [VERIFICAR: posição do STJ sobre prisão civil por alimentos indenizatórios].
- Aplicar juros e índice "de cabeça": use o núcleo.

## Integração com o núcleo
`juros-e-correcao` (atualização do débito), `prazos-processuais` (3 dias, contagem e intimação), `verificacao-de-citacoes` (todo precedente adicional), `fidelidade-factual` (planilha e datas), `estilo-forense`.

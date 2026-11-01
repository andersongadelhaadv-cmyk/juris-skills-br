---
name: civel-excecao-de-pre-executividade
description: >
  Redige exceção (ou objeção) de pré-executividade em execução ou cumprimento de
  sentença, restrita a matérias conhecíveis de ofício que dispensam dilação
  probatória (Súmula 393 do STJ; CPC art. 803, p.ú., e art. 518). Use quando o
  usuário pedir exceção de pré-executividade, objeção de pré-executividade,
  defesa sem garantia do juízo, alegar nulidade do título, prescrição,
  ilegitimidade evidente ou falta de citação por simples petição.
metadata:
  area: processo-civil
  tipo_peca: excecao-pre-executividade
  verificado_em: 2026-11-01
---
# Exceção de pré-executividade

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: matéria de ordem pública ou nulidade evidente, provada por documento já disponível, a qualquer tempo da execução (inclusive após o prazo dos embargos ou da impugnação). Exemplos: título sem liquidez, certeza ou exigibilidade (art. 803, I); falta de citação (II); execução antes da condição (III); prescrição; ilegitimidade comprovável por documento; pagamento comprovado por recibo inequívoco; incompetência absoluta.
- Não usar: tese que depende de perícia, testemunhas ou cálculo controvertido (excesso de execução discutível); nesse caso, embargos (`civel-embargos-a-execucao`) ou impugnação (`civel-impugnacao-ao-cumprimento`).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
- Autos da execução (título, inicial, citação, atos de constrição).
- Documento que prova a tese de plano.
- Se o prazo dos embargos/impugnação ainda está aberto (preferir a via típica quando possível).

## Prazo e contagem
- Não há prazo legal; cabe enquanto não extinta a execução. Mas a demora pode gerar preclusão de questões não cognoscíveis de ofício e acúmulo de atos executivos.
- Se ainda houver prazo para embargos (15 dias) ou impugnação, avaliar usar ambos ou a via típica. Use `prazos-processuais`.

## Estrutura da peça
Petição simples nos autos → cabimento (ordem pública + prova pré-constituída) → matéria → documento → pedido de suspensão de atos constritivos (se cabível) → extinção/nulidade → honorários. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Base normativa: arts. 803, p.ú. (nulidade pronunciada de ofício ou a requerimento, independentemente de embargos), 518 (validade do cumprimento arguida nos próprios autos) e 485, §3º (matérias cognoscíveis de ofício).
- Súmula 393 do STJ: admite a exceção na execução fiscal para matérias cognoscíveis de ofício sem dilação probatória; aplicada por analogia na execução civil, como mostram julgados de 2025 e 2026 da base.
- Não suspende a execução por si; peça suspensão de atos expropriatórios fundamentadamente.

## Fundamentos verificados
CPC arts. 485, §3º, 518, 525, §11, 803, 921, §5º, 924, V; Súmula 393 do STJ; STJ, AREsp 2.820.812 e REsp 2.181.389. Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Acolhimento para extinguir a execução (art. 924) ou declarar a nulidade (art. 803).
- Suspensão de atos de expropriação até a decisão, se houver risco concreto.
- Levantamento de constrições.
- Honorários em favor do excipiente, se acolhida com extinção total ou parcial.

## Checklist pré-protocolo
- [ ] Matéria cognoscível de ofício (ou nulidade evidente).
- [ ] Prova documental pronta, sem necessidade de perícia ou testemunha.
- [ ] Documento anexado e indicado.
- [ ] Verificado se a via típica (embargos/impugnação) ainda está aberta.
- [ ] Pedido de honorários incluído.

## Erros a evitar
- Usar a exceção para discutir excesso que depende de cálculo controvertido ou perícia: o STJ rejeita (Súmula 7 em REsp).
- Alegar fatos sem prova pré-constituída.
- Deixar passar o prazo dos embargos confiando apenas na exceção, quando há teses que exigem prova.
- Tratar a exceção como se suspendesse automaticamente a execução.

## Integração com o núcleo
- `prazos-processuais` para prescrição (inclusive intercorrente, art. 921) e janela dos embargos.
- `verificacao-de-citacoes` para qualquer precedente.
- `fidelidade-factual` para o documento que sustenta a tese.
- `estilo-forense` na revisão.

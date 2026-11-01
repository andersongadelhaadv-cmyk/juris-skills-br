---
name: trib-excecao-pre-executividade-fiscal
description: >
  Redige exceção de pré-executividade em execução fiscal, sem garantia do juízo,
  restrita a matérias conhecíveis de ofício que não exijam dilação probatória
  (Súmula 393 STJ). Use quando o usuário pedir exceção ou objeção de
  pré-executividade, defesa sem penhora, alegar prescrição, decadência, nulidade
  da CDA, ilegitimidade passiva ou pagamento com prova documental em execução fiscal.
metadata:
  area: tributario-fazenda
  tipo_peca: excecao-pre-executividade
  verificado_em: 2026-11-01
---
# Exceção de pré-executividade em execução fiscal

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: vício que o juiz pode conhecer de ofício e que se prova só com documentos já disponíveis: prescrição (originária ou intercorrente), decadência evidente, nulidade formal da CDA, ilegitimidade passiva demonstrável por documento, pagamento ou parcelamento anterior ao ajuizamento, suspensão da exigibilidade prévia, inexistência do executado, incompetência absoluta.
- Não usar: tese que dependa de perícia, testemunha ou discussão de fatos controvertidos (vá para `trib-embargos-a-execucao-fiscal`); prescrição intercorrente com cálculo detalhado (veja também `trib-prescricao-intercorrente`).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
- Cópia integral da execução e da CDA; datas: constituição definitiva, ajuizamento, despacho citatório, citação, pedidos da Fazenda, suspensões e arquivamento.
- Documento que prova o vício (comprovante de pagamento, parcelamento, contrato social, alteração registrada na Junta, decisão administrativa).
- Se já houve penhora ou bloqueio (para pedir levantamento) e se correm prazos de embargos.

## Prazo e contagem
- Não há prazo legal: pode ser oferecida enquanto pendente a execução. Mas a exceção NÃO suspende o prazo dos embargos; se houve garantia, controle o prazo do art. 16 da LEF em paralelo.
- Resposta da Fazenda: prazo fixado pelo juiz; intimação pessoal (LEF art. 25). Use `prazos-processuais`.

## Estrutura da peça
Endereçamento → qualificação → cabimento (Súmula 393 STJ) → síntese do processo → matéria de ordem pública com prova documental → pedido de suspensão de atos constritivos → pedidos. Roteiro em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Os dois requisitos são cumulativos: matéria cognoscível de ofício + prova pré-constituída (Súmula 393 STJ).
- Prescrição anterior ao ajuizamento pode ser decretada de ofício (Súmula 409 STJ).
- Crédito declarado e não pago: constituído pela declaração (Súmula 436 STJ); prescrição conta da constituição definitiva (CTN art. 174) [confirme a data de entrega ou vencimento, o que for posterior, com `prazos-processuais`].
- Ilegitimidade de sócio: só cabe na exceção se demonstrável por documento; se o nome consta da CDA, o ônus de provar a ausência dos requisitos do art. 135 é do executado e, havendo necessidade de prova, a via é a dos embargos.
- Honorários: acolhida a exceção com extinção, em regra cabem honorários; NÃO cabem quando o acolhimento se dá por prescrição intercorrente (Tema 1229 STJ).

## Fundamentos verificados
LEF arts. 3º, 16, 25 e 40; CTN arts. 135, 151, 156, 173, 174, 202 e 203; CPC arts. 85, 485, IV e VI, 487, II e 803; Súmulas 393, 409, 430, 435 e 436 STJ; Tema 1229 STJ. Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Intimação da Fazenda para se manifestar.
- Suspensão de atos de constrição até a decisão, se houver risco concreto.
- Extinção da execução (com ou sem mérito, conforme a matéria) ou exclusão do excipiente do polo passivo.
- Levantamento de penhoras e bloqueios; cancelamento de restrições.
- Honorários contra a Fazenda (CPC art. 85, §3º), salvo hipótese do Tema 1229 STJ.

## Checklist pré-protocolo
- [ ] Cada tese é cognoscível de ofício e provada só por documento já juntado.
- [ ] Linha do tempo completa (constituição, ajuizamento, despacho, citação, suspensões).
- [ ] Prazo de embargos controlado se já houve garantia.
- [ ] Pedido de honorários ajustado ao Tema 1229 STJ.
- [ ] Teses que dependem de prova reservadas para embargos, não misturadas.

## Erros a evitar
- Usar a exceção para discutir base de cálculo, multa ou fatos que exigem perícia.
- Acreditar que a exceção suspende o prazo dos embargos.
- Alegar ilegitimidade de sócio constante da CDA sem prova documental robusta.
- Pedir honorários na extinção por prescrição intercorrente (Tema 1229 STJ).
- Recalcular o débito com índice próprio: use `juros-e-correcao`.

## Integração com o núcleo
- `prazos-processuais`: cálculo da prescrição e controle do prazo de embargos.
- `juros-e-correcao`: se a tese envolver excesso evidente por documento.
- `verificacao-de-citacoes`: todo precedente acrescentado.
- `fidelidade-factual`: conferir datas nos autos.
- `estilo-forense`: revisão final.

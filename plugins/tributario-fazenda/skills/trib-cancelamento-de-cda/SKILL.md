---
name: trib-cancelamento-de-cda
description: >
  Redige requerimento administrativo de revisão e cancelamento de inscrição em
  dívida ativa e de sua CDA perante a procuradoria (União, Estado ou Município),
  com o checklist de nulidades do termo de inscrição (LEF art. 2º, §§ 3º, 5º, 6º
  e 8º; CTN arts. 202 a 204) e o mapa de qual via judicial usar se o pedido
  falhar. Use quando o usuário pedir cancelamento de CDA, nulidade da certidão
  de dívida ativa, revisão de dívida inscrita, CDA sem fundamento legal, CDA
  com devedor ou valor errado, ou baixa de inscrição já paga, parcelada,
  prescrita ou com exigibilidade suspensa antes ou depois do ajuizamento.
metadata:
  area: tributario-fazenda
  tipo_peca: requerimento
  verificado_em: 2026-11-25
---
# Cancelamento e nulidade de CDA

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: (a) pedir à procuradoria que reveja e cancele a inscrição, ainda sem execução ou já com ela; (b) auditar a CDA antes de escolher a defesa judicial; (c) baixa de inscrição por pagamento, parcelamento, compensação ou suspensão anterior à inscrição; (d) vício no termo de inscrição (devedor, valor, fundamento legal, processo de origem).
- Não usar como peça judicial. Se já há execução fiscal:
  - nulidade provada só por documento, sem garantia: `trib-excecao-pre-executividade-fiscal`;
  - com garantia ou tese que exige prova: `trib-embargos-a-execucao-fiscal`;
  - prescrição ou decadência como tese central: `trib-prescricao-intercorrente`.
- Sem execução, para discutir o próprio lançamento em juízo: `trib-acao-anulatoria`; para obter certidão enquanto discute: `trib-garantia-antecipada-certidao` e `trib-certidao-negativa-cpen`.
- Sócio incluído na CDA ou no polo passivo: `trib-defesa-redirecionamento-socio`.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Cópia da CDA e, se possível, do termo de inscrição e do extrato da dívida no portal da procuradoria.
2. Ente credor e órgão (PGFN, procuradoria estadual ou municipal) — o rito do pedido administrativo muda conforme o ente.
3. Processo administrativo de origem (auto de infração, declaração do contribuinte, notificação de lançamento) e se houve defesa.
4. Fato que motiva o cancelamento: pagamento, parcelamento, compensação, decisão administrativa ou judicial, suspensão da exigibilidade, prescrição, erro de sujeito passivo, erro de valor ou de fundamento.
5. Se já existe execução fiscal, protesto, inscrição em cadastro restritivo ou averbação em registro de bens — e as datas.
6. Prazo administrativo que eventualmente esteja correndo (notificação de inscrição).

## Prazo e contagem
- Após a inscrição em dívida ativa da União, o devedor é notificado para pagar em 5 dias; a notificação se presume entregue 15 dias após a expedição (Lei 10.522/2002, art. 20-B, caput e § 1º). Não pago, a Fazenda pode comunicar a inscrição a cadastros de crédito e averbar a CDA em registros de bens (art. 20-B, § 3º).
- O prazo e os efeitos do pedido de revisão (por exemplo, se suspende protesto ou ajuizamento) estão em ato da PGFN, previsto no art. 20-E da mesma lei, e em normas próprias de cada Estado ou Município [VERIFICAR: ato vigente da PGFN sobre revisão de dívida inscrita e norma local do ente].
- O pedido administrativo NÃO suspende prazo judicial (embargos, exceção, recurso). Controle tudo com `prazos-processuais`.

## Estrutura da peça
Endereçamento à procuradoria → qualificação e identificação da inscrição → síntese → fundamento do cancelamento (fato extintivo ou suspensivo, ou nulidade do termo) → prova documental → pedidos (cancelamento, baixa de protesto e de cadastros, comunicação ao juízo se houver execução). Roteiro em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- A inscrição é ato de controle de legalidade feito pelo órgão competente (LEF art. 2º, § 3º): o pedido de revisão invoca o dever de a própria procuradoria conferir certeza e liquidez.
- Requisitos do termo de inscrição (LEF art. 2º, § 5º): devedor e corresponsáveis com domicílio; valor originário, termo inicial e forma de calcular juros e encargos; origem, natureza e fundamento legal ou contratual; atualização monetária com fundamento e termo inicial; data e número da inscrição; número do processo administrativo ou do auto de infração. A CDA repete esses elementos (§ 6º).
- O CTN traz rol paralelo (art. 202, com redação da LC 236/2026 no inciso I e no § 1º).
- Omissão ou erro em requisito gera nulidade da inscrição e da cobrança (CTN art. 203), sanável até a decisão de primeira instância, com devolução de prazo só quanto à parte modificada; a LEF permite emenda ou substituição até a sentença, devolvendo o prazo de embargos (art. 2º, § 8º).
- Limites à emenda: só erro material ou formal, vedado trocar o sujeito passivo (Súmula 392/STJ); e não é possível substituir ou emendar a CDA para incluir, completar ou modificar o fundamento legal do crédito tributário (Tema 1.350/STJ).
- A presunção de certeza e liquidez é relativa (CTN art. 204; LEF art. 3º): o pedido precisa de prova inequívoca.
- A nulidade da CDA, em juízo, tende a exigir demonstração de prejuízo à defesa (STJ, REsp 2.257.689, 2ª Turma, 2026). Mostre o prejuízo concreto.

## Fundamentos verificados
LEF arts. 2º (§§ 3º, 5º, 6º, 8º) e 3º; CTN arts. 202 a 204 (LC 236/2026); Lei 10.522/2002, arts. 20-B e 20-E; Súmulas 392 e 559/STJ; Tema 1.350/STJ; REsp 2.257.689. Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Revisão e cancelamento total da inscrição (ou parcial, com retificação do valor ou do devedor).
- Baixa de protesto, de inscrição em cadastros de crédito e de averbações em registros de bens.
- Se houver execução fiscal: que a procuradoria peça a extinção nos autos; em paralelo, peticione no processo informando o pedido.
- Emissão de certidão atualizada após o cancelamento (`trib-certidao-negativa-cpen`).
- Encargos e atualização de eventual saldo: `juros-e-correcao`.

## Checklist pré-protocolo
- [ ] CDA conferida item a item contra o art. 2º, § 5º, da LEF e o art. 202 do CTN
- [ ] Fato extintivo ou suspensivo provado por documento oficial
- [ ] Fundamento legal da CDA conferido (Tema 1.350/STJ, se ausente ou deficiente)
- [ ] Rito do ente credor conferido (PGFN, Estado ou Município)
- [ ] Prazos judiciais em curso controlados à parte — o pedido não os suspende
- [ ] Pedido de baixa de protesto, cadastros e averbações

## Erros a evitar
- Esperar a resposta administrativa e perder o prazo de embargos ou de recurso.
- Alegar nulidade formal genérica sem apontar o requisito faltante e o prejuízo.
- Pedir cancelamento por falta de demonstrativo de cálculo na execução (Súmula 559/STJ afasta essa exigência na inicial).
- Tratar erro de sujeito passivo como corrigível por emenda (Súmula 392/STJ).
- Recalcular o débito com índice próprio: use `juros-e-correcao`.

## Integração com o núcleo
`prazos-processuais`, `juros-e-correcao`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

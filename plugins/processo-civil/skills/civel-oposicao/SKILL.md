---
name: civel-oposicao
description: >
  Redige a petição inicial de oposição (CPC, arts. 682 a 686), ação do terceiro
  que pretende, no todo ou em parte, a coisa ou o direito disputado entre autor
  e réu de processo em curso, e orienta a contestação dos opostos. Use quando o
  usuário disser que um bem ou direito discutido em ação entre outras pessoas é
  na verdade do cliente, quiser entrar num processo alheio para reivindicar o
  objeto da disputa antes da sentença, ou precisar contestar uma oposição.
metadata:
  area: processo-civil
  tipo_peca: inicial
  verificado_em: 2026-11-25
---
# Oposição (CPC, arts. 682 a 686)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: terceiro afirma ser titular, no todo ou em parte, da **mesma coisa ou do mesmo direito** sobre o qual controvertem autor e réu, e quer que isso seja decidido contra ambos, antes da sentença.
- Exemplos: imóvel disputado em reivindicatória ou em partilha que pertence ao opoente; crédito ou indenização disputada por duas pessoas que o opoente diz ser seu.
- Não usar:
  - bem do terceiro **constrito** (penhora, arresto, busca e apreensão) sem que a titularidade seja o objeto da ação: embargos de terceiro (`imob-embargos-de-terceiro`);
  - interesse apenas em que uma das partes vença: assistência (pedir ingresso nos próprios autos);
  - mera pretensão de **substituir** uma das partes no polo (STJ — ver Fundamentos): sucessão processual ou ação conexa;
  - processo já sentenciado: ação autônoma (`civel-peticao-inicial`).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Número do processo originário, juízo, partes, advogados constituídos e objeto exato do pedido nele formulado.
2. Fase do processo: já há sentença? Começou a audiência de instrução?
3. Título do opoente sobre a coisa ou o direito (matrícula, contrato, cessão, documento de crédito) e por que ele exclui o direito de autor e réu.
4. Se a pretensão é total ou parcial (qual parte do bem ou do direito).
5. Provas disponíveis e as que precisará produzir.
6. Urgência (risco de alienação, levantamento de valores): avaliar tutela provisória.

## Prazo e contagem
- Cabe **até a sentença** do processo originário (art. 682). Depois dela, só ação autônoma.
- Opostos citados na pessoa dos advogados para contestar em **15 dias**, prazo comum (art. 683, parágrafo único).
- Oposição proposta após iniciada a audiência de instrução: o juiz pode suspender o processo originário ao fim da produção das provas (art. 685, parágrafo único).
- Prescrição da pretensão do opoente: depende do direito material [VERIFICAR no caso]. Contagem processual: `prazos-processuais`.

## Estrutura da peça
Endereçamento ao juízo da causa originária, por dependência → qualificação do opoente e dos dois opostos (autor e réu do processo originário) → síntese do processo originário → cabimento e tempestividade → fatos e título do opoente → direito: por que a coisa/direito é do opoente e não de nenhum dos opostos → tutela provisória, se houver → pedidos contra ambos → provas → valor da causa. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- A oposição é **ação**: a inicial observa os requisitos da petição inicial (art. 683, caput) — ver `civel-peticao-inicial`.
- Pedido dirigido **contra autor e réu** simultaneamente (art. 682).
- Distribuição por dependência; admitida, é apensada e julgada na mesma sentença da ação originária (arts. 683, parágrafo único, e 685).
- A oposição é decidida **em primeiro lugar** quando julgada com a ação originária (art. 686): estruture o pedido sabendo que, se procedente, prejudica a disputa entre os opostos.
- Se um dos opostos reconhecer o pedido, o processo segue contra o outro (art. 684).
- Competência, custas e valor da causa: conferir regra local [VERIFICAR: custas da oposição no tribunal].

## Fundamentos verificados
- CPC arts. 682 a 686 (conferidos no Planalto).
- STJ, REsp 1.889.164 (3ª Turma, rel. Min. Paulo de Tarso Sanseverino, julg. 21/06/2022): a oposição não serve para mera substituição de um dos polos da demanda; admitido o aproveitamento como ação conexa, pela instrumentalidade.
- STJ, REsp 1.963.885 (3ª Turma, rel. Min. Nancy Andrighi, julg. 03/05/2022): oposição em ação de dissolução de união estável e partilha, para reconhecer a propriedade de imóvel que se pretendia partilhar; imissão na posse como decorrência lógica do acolhimento.
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Distribuição por dependência e apensamento aos autos originários.
- Citação dos opostos, na pessoa de seus advogados, para contestar em 15 dias.
- Tutela provisória (indisponibilidade do bem, depósito judicial do valor disputado) — `civel-tutela-provisoria`.
- Procedência para declarar que a coisa ou o direito pertence ao opoente (no todo ou na parte indicada), com as consequências práticas (entrega, imissão, levantamento do depósito).
- Julgamento da oposição antes da ação originária (art. 686).
- Provas; custas e honorários contra os opostos.

## Checklist pré-protocolo
- [ ] Processo originário ainda sem sentença
- [ ] Objeto da oposição é o mesmo objeto da disputa entre autor e réu
- [ ] Ambos os opostos no polo passivo, com seus advogados identificados
- [ ] Título do opoente documentado e explicação de por que exclui o direito dos dois
- [ ] Requisitos da petição inicial atendidos; valor da causa
- [ ] Distribuição por dependência requerida
- [ ] Avaliado se o caso é, na verdade, de embargos de terceiro ou assistência

## Erros a evitar
- Usar oposição para atacar penhora sobre bem próprio (é embargos de terceiro).
- Demandar só contra uma das partes do processo originário.
- Protocolar depois da sentença.
- Pedir apenas para "entrar no lugar" do autor ou do réu.
- Formular pedido sobre bem ou direito diferente do discutido na ação originária.

## Integração com o núcleo
`prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`. Contestação dos opostos: `civel-contestacao`. Recurso contra a sentença única: `civel-apelacao`.

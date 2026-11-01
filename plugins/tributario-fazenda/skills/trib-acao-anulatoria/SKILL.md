---
name: trib-acao-anulatoria
description: >
  Redige ação anulatória de débito fiscal (LEF art. 38 e CTN arts. 151 e 204),
  com pedido de tutela ou depósito integral para suspender a exigibilidade (CTN
  art. 151, II e V). Use quando o usuário pedir anulatória, ação para anular auto
  de infração, lançamento ou CDA, desconstituir crédito tributário, ação
  declaratória de inexistência de débito fiscal com depósito judicial ou antecipação
  de garantia antes da execução fiscal.
metadata:
  area: tributario-fazenda
  tipo_peca: inicial
  verificado_em: 2026-11-01
---
# Ação anulatória de débito fiscal

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: crédito já constituído (lançamento, auto de infração, decisão administrativa definitiva ou inscrição) que precise de prova pericial, testemunhal ou ampla discussão de fatos; também quando o prazo do MS já passou.
- Não usar: matéria só de direito com prova documental e ato recente (avalie `trib-mandado-de-seguranca`); tributo já pago (use `trib-repeticao-de-indebito`); crédito já em execução fiscal com garantia (avalie `trib-embargos-a-execucao-fiscal`).
- Anulatória de decisão administrativa que negou restituição tem prazo próprio de 2 anos (CTN art. 169): trate em `trib-repeticao-de-indebito`.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
- Auto de infração/notificação de lançamento, decisões administrativas e número do processo administrativo.
- Se a defesa administrativa ainda está pendente (a ação implica renúncia ao recurso administrativo: LEF art. 38, p.ú.; CTN art. 208-E, p.ú.).
- Se já existe execução fiscal ajuizada e em qual juízo.
- Disponibilidade de depósito em dinheiro, seguro garantia ou fiança.
- Vícios: formais (art. 208-B e 208-H do CTN; Decreto 70.235 art. 10 e 59 no plano federal), decadência, mérito (base de cálculo, não incidência, multa confiscatória).

## Prazo e contagem
- A pretensão anulatória segue a regra geral contra a Fazenda (5 anos, Decreto 20.910/1932) contada da constituição definitiva; confirme o termo com `prazos-processuais`.
- Não há prazo para o depósito: pode ser feito a qualquer tempo, na inicial ou depois.
- Contestação da Fazenda em dobro (CPC art. 183).

## Estrutura da peça
Endereçamento → partes → síntese do lançamento → cabimento e efeitos sobre o processo administrativo → tutela/depósito → preliminares de mérito (decadência) → nulidades formais → mérito material → multa → provas → pedidos. Roteiro em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Depósito: o art. 38 da LEF fala em "depósito preparatório", mas exigir depósito prévio como condição de admissibilidade é inconstitucional (Súmula Vinculante 28). O depósito é faculdade que suspende a exigibilidade se integral e em dinheiro (CTN art. 151, II; Súmula 112 STJ).
- Sem depósito, peça tutela provisória (CTN art. 151, V, redação da LC 236/2026).
- Seguro garantia/fiança: na ação anulatória, servem como garantia antecipada para fins de certidão (CTN art. 206), mas não estão no rol do art. 151 quando oferecidos fora da execução fiscal; o inciso X do art. 151 (LC 236/2026) trata da aceitação dessas garantias em execução fiscal. Explique ao cliente a diferença.
- Decadência: CTN art. 173 (lançamento de ofício) e art. 150, §4º (homologação com pagamento); com a LC 236/2026, pagamento parcial conta do fato gerador (art. 150, §6º) e dolo, fraude ou simulação desloca para o art. 173, I (art. 150, §5º). Sem declaração: Súmula 555 STJ.
- Multa: limites do CTN art. 113-A (75%, 100% com dolo comprovado, 150% na reincidência), incluídos pela LC 236/2026 [VERIFICAR: aplicação a fatos anteriores; examinar CTN art. 106, II, c].

## Fundamentos verificados
LEF arts. 3º e 38; CTN arts. 106, 113-A, 142, 150, 151, 173, 204, 206, 208-B, 208-E e 208-H; CPC arts. 183, 300 e 319; Súmula Vinculante 28; Súmulas 112, 436 e 555 STJ. Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Autorização para depósito integral (ou tutela provisória) com suspensão da exigibilidade e ordem para não inscrever/protestar e emitir certidão positiva com efeitos de negativa.
- Citação do ente pelo órgão de advocacia pública (CPC art. 242, §3º).
- Anulação total ou parcial do lançamento/CDA; subsidiariamente, redução da multa.
- Levantamento do depósito ao final se procedente; conversão em renda só após trânsito em julgado.
- Produção de prova pericial contábil (quesitos anexos) e documental.
- Honorários contra a Fazenda pelo CPC art. 85, §3º.

## Checklist pré-protocolo
- [ ] Cliente ciente de que a ação extingue o recurso administrativo pendente sobre o mesmo objeto.
- [ ] Decadência calculada com a regra correta (art. 150, §§4º a 6º, ou art. 173).
- [ ] Depósito: valor integral atualizado conferido com a Fazenda (sem desconto de multa).
- [ ] Quesitos periciais elaborados quando a tese depender de fatos.
- [ ] Execução fiscal já ajuizada? Peça reunião/conexão ou ajuste a estratégia.
- [ ] Precedentes checados em `verificacao-de-citacoes`.

## Erros a evitar
- Tratar o depósito como requisito de admissibilidade (Súmula Vinculante 28).
- Depositar valor parcial esperando suspensão da exigibilidade (Súmula 112 STJ).
- Ajuizar sem avisar o cliente da desistência tácita do processo administrativo.
- Contar decadência pelo art. 150, §4º quando não houve pagamento nem declaração.
- Calcular atualização do depósito ou do débito com taxa própria: use `juros-e-correcao`.

## Integração com o núcleo
- `prazos-processuais`: prescrição da pretensão e prazos do processo.
- `juros-e-correcao`: valor atualizado do depósito e da condenação em honorários.
- `verificacao-de-citacoes`: todo precedente acrescentado.
- `fidelidade-factual`: datas do lançamento, ciência e pagamentos.
- `estilo-forense`: revisão final.

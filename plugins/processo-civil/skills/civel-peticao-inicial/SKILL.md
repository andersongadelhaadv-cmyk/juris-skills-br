---
name: civel-peticao-inicial
description: >
  Redige petição inicial de procedimento comum cível conforme os arts. 319 e 320
  do CPC, com cálculo do valor da causa (art. 292), pedido de tutela provisória e
  opção sobre a audiência do art. 334. Use quando o usuário pedir petição inicial,
  ação de cobrança, ação indenizatória, ação declaratória, ação de obrigação de
  fazer, "entrar com ação", "ajuizar demanda" ou "peça vestibular" no cível.
metadata:
  area: processo-civil
  tipo_peca: inicial
  verificado_em: 2026-11-01
---
# Petição inicial cível (procedimento comum)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: ação de conhecimento pelo procedimento comum (CPC, Livro I da Parte Especial).
- Não usar: juizado especial (use `civel-juizado-especial`), monitória (`civel-acao-monitoria`), execução de título extrajudicial (`civel-execucao-titulo-extrajudicial`), tutela antecedente isolada (`civel-tutela-provisoria`), procedimentos especiais de família ou consumo que tenham skill própria.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
- Qualificação completa de autor e réu (nome, estado civil, união estável, profissão, CPF/CNPJ, e-mail, domicílio).
- Narrativa dos fatos com datas, valores e documentos que provam cada um.
- O que o cliente quer obter (bem da vida) e se há urgência concreta.
- Foro: domicílio do réu, local do fato, cláusula de eleição (checar art. 63, §§1º e 5º).
- Interesse ou não na audiência de conciliação; pedido de gratuidade, se houver.
- Valores para o cálculo do valor da causa.

## Prazo e contagem
- Não há prazo processual para a inicial; há prazo material. Verifique prescrição e decadência antes de redigir e registre a data-limite.
- Se a inicial vier depois de tutela cautelar antecedente efetivada, o pedido principal deve ser feito em 30 dias (art. 308). Use `prazos-processuais`.

## Estrutura da peça
Endereçamento → qualificação → síntese → fatos → fundamentos jurídicos → tutela provisória (se houver) → pedidos → provas → valor da causa → opção sobre audiência → fecho. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Art. 319, I a VII: todos os incisos precisam aparecer de forma identificável.
- Art. 320: documentos indispensáveis juntados com a inicial (contrato, título, prova da relação).
- Art. 330: evitar inépcia (pedido certo e determinado, conclusão lógica, pedidos compatíveis). Em revisional de empréstimo, financiamento ou alienação, discriminar as obrigações controvertidas e o valor incontroverso (art. 330, §§2º e 3º).
- Art. 292: o valor da causa segue critério legal; o juiz pode corrigi-lo de ofício (§3º).

## Fundamentos verificados
Resumo: CPC arts. 63, 292, 294, 300, 303, 311, 319, 320, 330, 332, 334. Detalhe e forma de uso em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Citação do réu (indicar meio: eletrônico, correio, oficial).
- Tutela provisória, se cabível, com pedido destacado.
- Procedência com pedidos especificados, um a um, em correspondência com a causa de pedir.
- Condenação em custas e honorários (art. 85).
- Correção e juros: formular o pedido com termo inicial e índice indicados pela skill `juros-e-correcao` do núcleo; não escrever taxa fixa.
- Produção de provas especificadas; gratuidade, se for o caso.

## Checklist pré-protocolo
- [ ] Todos os incisos do art. 319 presentes, inclusive e-mail e existência de união estável.
- [ ] Documentos indispensáveis (art. 320) anexados e referidos no texto.
- [ ] Valor da causa calculado pelo inciso correto do art. 292 e com memória de cálculo.
- [ ] Custas recolhidas ou gratuidade fundamentada com declaração e prova.
- [ ] Opção expressa pela audiência do art. 334 (ou desinteresse justificado).
- [ ] Pedidos certos e determinados; cada fato tem prova correspondente.
- [ ] Prescrição/decadência conferidas e anotadas.
- [ ] Procuração com poderes adequados.

## Erros a evitar
- Valor da causa "para fins de alçada" sem relação com o proveito econômico: o juiz corrige e cobra custas complementares.
- Dano moral sem valor pretendido: o art. 292, V, exige o valor pretendido.
- Pedido genérico fora das hipóteses legais (art. 324).
- Escolher foro sem vínculo com partes ou negócio: o art. 63, §5º, autoriza declinação de ofício.
- Pedir tutela de urgência só com "perigo da demora" abstrato, sem fato concreto.
- Fixar juros de 1% ao mês: regra superada; usar o núcleo.

## Integração com o núcleo
- `juros-e-correcao` para todo pedido condenatório (índice, taxa legal e termo inicial).
- `prazos-processuais` para prescrição, decadência e prazos da tutela antecedente.
- `verificacao-de-citacoes` para qualquer precedente acrescentado.
- `fidelidade-factual` para conferir que os fatos narrados correspondem aos documentos.
- `estilo-forense` para revisão final de linguagem.

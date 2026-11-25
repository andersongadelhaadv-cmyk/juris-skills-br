---
name: trib-consignacao-em-pagamento
description: >
  Redige ação de consignação em pagamento de crédito tributário (CTN arts. 156,
  VIII, e 164; CPC arts. 539 a 549) nas três hipóteses legais: recusa ou
  condicionamento do recebimento, exigência sem fundamento legal e cobrança do
  mesmo tributo por mais de um ente sobre o mesmo fato gerador. Use quando o
  usuário pedir consignatória tributária, depositar tributo que o fisco recusa
  receber, guia negada porque há outro débito, dois municípios cobrando o mesmo
  ISS, bitributação entre Estado e Município, ou pagar com efeito liberatório
  sem saber a quem.
metadata:
  area: tributario-fazenda
  tipo_peca: inicial
  verificado_em: 2026-11-25
---
# Consignação em pagamento tributária

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar só nas hipóteses do CTN art. 164: (I) recusa de receber, ou recebimento condicionado ao pagamento de outro tributo, de penalidade ou ao cumprimento de obrigação acessória; (II) recebimento subordinado a exigência administrativa sem fundamento legal; (III) exigência, por mais de uma pessoa jurídica de direito público, de tributo idêntico sobre o mesmo fato gerador.
- O cliente **quer pagar** o valor que entende devido e extinguir o crédito.
- Não usar: quando o objetivo é discutir se o tributo é devido e suspender a exigibilidade (depósito em `trib-declaratoria-inexistencia-relacao-tributaria` ou `trib-acao-anulatoria`; o STJ afasta a consignatória quando não há intuito de quitação); para impor parcelamento ou pagar menos do que o fisco exige por discordar do valor (`trib-acao-anulatoria`); tributo já pago em duplicidade (`trib-repeticao-de-indebito`); consignação de obrigação privada (`civel-peticao-inicial`).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Tributo, período, fato gerador e valor que o cliente se dispõe a pagar (com memória de cálculo).
2. Prova da recusa ou do condicionamento: protocolo, e-mail, tela do sistema que nega a guia, resposta do órgão.
3. Na hipótese III: prova de que **cada** ente efetivamente exige o tributo (notificação, auto, guia, lei local aplicada), local da prestação e do estabelecimento.
4. Vencimento do tributo e se já há lançamento, inscrição ou execução.
5. Disponibilidade imediata do valor em dinheiro.

## Prazo e contagem
- Não há prazo próprio para ajuizar; mas, enquanto não houver depósito, correm juros e multa de mora. Ajuíze e deposite o quanto antes.
- Depósito em 5 dias contados do deferimento (CPC art. 542, I).
- Alegada insuficiência na contestação: complemento em 10 dias (CPC art. 545).
- Fazenda: prazo em dobro com intimação pessoal (CPC art. 183). Contagem: `prazos-processuais`.

## Estrutura da peça
Endereçamento → partes (um ou vários entes) → fatos e hipótese do art. 164 → valor e memória de cálculo → requerimento de depósito → efeito liberatório → pedidos. Roteiro em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- A consignação só pode versar sobre o crédito que o consignante se propõe a pagar (CTN art. 164, §1º). Depósito parcial do tributo exigido não serve para extinguir a obrigação: o STJ já extinguiu consignatória sem mérito por impossibilidade de pagamento parcial, com conversão em renda do depositado (REsp 2.146.757).
- Hipótese III (dois entes): ambos no polo passivo; o STJ exige que a cobrança seja **efetiva** por todos os entes, não mera possibilidade (AREsp 2.397.496). A situação equivale à dúvida sobre quem deva receber (CPC art. 547): os réus disputam entre si, e o autor sai liberado.
- Competência: se um dos réus é a União ou autarquia federal, a causa vai à Justiça Federal (CF art. 109, I).
- Defesa possível dos réus: não houve recusa, a recusa foi justa, depósito fora do prazo ou do lugar, depósito não integral (CPC art. 544).
- Depósito extrajudicial em banco (CPC art. 539, §1º): uso para crédito tributário não conferido em fonte oficial [VERIFICAR]; prefira o depósito judicial.

## Fundamentos verificados
CTN arts. 156, VIII, e 164; CPC arts. 183, 539, 540, 542, 544, 545 e 547; CF art. 109, I; STJ REsp 2.146.757, AREsp 2.397.496 e EDcl no AgInt no REsp 2.124.350. Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Autorização para depositar o valor (dentro de 5 dias do deferimento), com cessação dos juros e riscos a partir do depósito (CPC art. 540).
- Citação do(s) ente(s) para levantar o depósito ou contestar (CPC art. 542, II).
- Procedência: pagamento reputado efetuado e conversão do valor em renda do ente legitimado, com extinção do crédito (CTN arts. 156, VIII, e 164, §2º).
- Na hipótese III: declaração de qual ente é o sujeito ativo e exclusão do outro, com ordem para não inscrever nem executar o consignante.
- Certidão positiva com efeitos de negativa quanto ao crédito consignado, se cabível no caso.
- Honorários e custas pelos réus vencidos.

## Checklist pré-protocolo
- [ ] Hipótese do art. 164 identificada e provada (recusa documentada ou cobrança efetiva por dois entes)
- [ ] Valor consignado = tributo integral do período que se quer quitar (não parcela, não desconto)
- [ ] Todos os entes que cobram no polo passivo; juízo competente conferido
- [ ] Dinheiro disponível para depositar em 5 dias
- [ ] Cliente ciente: se improcedente, o crédito é cobrado com juros de mora e penalidades (art. 164, §2º)
- [ ] Atualização do valor remetida ao núcleo `juros-e-correcao`

## Erros a evitar
- Usar a consignatória para discutir o mérito do tributo ou forçar parcelamento: a via não serve e o STJ a afasta sem intuito de quitação.
- Consignar menos que o exigido por discordar do valor: a ação certa é anulatória.
- Ajuizar contra um só município quando os dois cobram: o outro continua livre para executar.
- Alegar bitributação apenas hipotética, sem cobrança efetiva do segundo ente.
- Deixar de depositar no prazo do art. 542, I: leva à extinção.

## Integração com o núcleo
`juros-e-correcao`, `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

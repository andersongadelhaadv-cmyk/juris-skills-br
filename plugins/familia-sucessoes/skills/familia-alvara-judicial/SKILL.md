---
name: familia-alvara-judicial
description: >
  Redige pedido de alvará judicial em jurisdição voluntária (CPC arts. 719 a 725) —
  levantamento de valores deixados pelo falecido sem inventário (Lei 6.858/1980 e CPC
  art. 666: FGTS, PIS-PASEP, verbas trabalhistas, restituição de IR, pequenos saldos) e
  autorização para vender, gravar ou movimentar bens de criança, adolescente, tutelado ou
  curatelado (CC arts. 1.691, 1.748, 1.750, 1.754 e 1.781). Use quando o usuário pedir
  alvará judicial, sacar FGTS ou PIS de falecido, levantar saldo bancário do falecido,
  alvará para vender imóvel de menor, autorização judicial para movimentar conta de
  filho menor ou de interditado.
metadata:
  area: familia-sucessoes
  tipo_peca: requerimento
  verificado_em: 2026-11-25
---
# Alvará judicial (jurisdição voluntária)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: (a) **alvará da Lei 6.858/1980** — valores não recebidos em vida pelo titular (verbas do empregador, FGTS, PIS-PASEP) e, não havendo outros bens a inventariar, restituições de tributos e pequenos saldos bancários, de poupança e fundos; (b) **alvará de autorização** — alienação, oneração ou administração extraordinária de bens de criança, adolescente, órfão ou interdito (CPC 725, III), levantamento de valores de tutelado ou curatelado.
- Não usar: falecido com bens a inventariar (`sucessoes-inventario-judicial` ou `sucessoes-inventario-extrajudicial`; alvarás incidentais no inventário ficam lá); emancipação ou outra hipótese do CPC 725 com rito próprio; conflito entre herdeiros (vira litígio — avaliar `civel-peticao-inicial`); levantamento de depósito em processo já existente (pedir nos próprios autos).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Tipo: valores de falecido (Lei 6.858) ou autorização para bem de incapaz?
2. **Falecido:** certidão de óbito; existência de outros bens (imóveis, veículos, investimentos acima de pequeno valor); dependentes habilitados no INSS (certidão de dependentes) ou, na falta, sucessores pela lei civil; extratos ou declarações das instituições (FGTS, PIS, banco, empregador, Receita).
3. Há herdeiro incapaz? Testamento? Herdeiros todos de acordo?
4. **Incapaz:** quem representa (pais, tutor, curador) e título (certidão, termo de tutela/curatela); bem, valor, matrícula; necessidade ou evidente interesse do incapaz; avaliação; destino do dinheiro.
5. Prova de que a venda é vantajosa (proposta, laudo, comparação de mercado).

## Prazo e contagem
- Citação dos interessados e intimação do MP (casos do CPC 178) para manifestação em 15 dias (CPC 721). O juiz decide em 10 dias (CPC 723) — prazo impróprio.
- Apelação contra a sentença (CPC 724). Contagem: `prazos-processuais`.

## Estrutura da peça
Endereçamento → qualificação de todos os requerentes (ou anuência dos demais interessados) → fatos → fundamento legal do alvará pedido → documentos → providência judicial exata (valor, instituição, conta, destinatário, quotas) → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Jurisdição voluntária: o pedido é do interessado, do MP ou da Defensoria, instruído com documentos e com a **indicação da providência judicial** (CPC 720). Seja específico: o banco só cumpre o que o alvará descreve.
- Todos os interessados são citados (CPC 721); juntar desde logo a anuência dos demais acelera.
- O juiz pode decidir por conveniência e oportunidade, sem legalidade estrita (CPC 723, p.ú.) — argumente com o interesse concreto.
- Lei 6.858: pagamento em quotas iguais aos dependentes habilitados na Previdência; na falta, aos sucessores da lei civil, independentemente de inventário (art. 1º; CPC 666). Quotas de menores ficam em poupança até os 18 anos, salvo autorização para imóvel de moradia ou subsistência e educação (art. 1º, § 1º).
- Saldos bancários, poupança e fundos: só se não houver outros bens sujeitos a inventário e até 500 ORTN (art. 2º) [VERIFICAR: a lei não atualiza o teto de 500 ORTN; conferir o critério de conversão adotado pelo tribunal de destino].
- Competência: Justiça Estadual para levantar FGTS e PIS-PASEP por falecimento do titular (Súmula 161/STJ).
- Bens de filhos menores: pais só alienam ou gravam imóveis com prévia autorização judicial, por necessidade ou evidente interesse da prole (CC 1.691). Tutela: imóvel só com manifesta vantagem, avaliação judicial e aprovação do juiz (CC 1.750); valores depositados só saem por ordem do juiz nas hipóteses do CC 1.754. Curatela segue as regras da tutela (CC 1.781).
- MP intervém quando houver interesse de incapaz (CPC 178, II).

## Fundamentos verificados
CPC 178, 666, 719 a 725; Lei 6.858/1980, arts. 1º e 2º; CC 1.691, 1.748, 1.750, 1.753, 1.754, 1.781; Súmula 161/STJ. Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Expedição de alvará autorizando [instituição] a pagar/liberar [valor ou saldo da conta nº] a [beneficiários], em quotas de [x], com dados bancários.
- Para quota de menor: depósito em poupança vinculada ao juízo (Lei 6.858, art. 1º, § 1º), ou autorização fundamentada de uso.
- Para bem de incapaz: autorização de venda por valor não inferior à avaliação, com destinação do produto (depósito judicial, aquisição de outro bem, despesas comprovadas) e prestação de contas.
- Citação/anuência dos interessados; intimação do MP; ouvida da Fazenda se houver interesse (CPC 722).
- Gratuidade, se cabível. Atualização de valores: núcleo `juros-e-correcao` (não fixar índice).

## Checklist pré-protocolo
- [ ] Certidão de óbito e declaração de inexistência de outros bens (Lei 6.858) — ou inventário indicado.
- [ ] Certidão de dependentes habilitados no INSS ou prova da ordem de sucessores.
- [ ] Extratos/declarações de cada instituição com valores e números de conta.
- [ ] Anuência dos demais interessados juntada, ou pedido de citação.
- [ ] Incapaz: título de representação, avaliação do bem, demonstração de necessidade/vantagem, destino do dinheiro.
- [ ] Providência descrita de forma executável pelo banco/cartório.
- [ ] Teto do art. 2º conferido no tribunal local.

## Erros a evitar
- Usar alvará para escapar do inventário quando há imóvel, veículo ou investimento relevante.
- Pedir alvará "genérico" sem instituição, conta e valor: o banco recusa.
- Esquecer o herdeiro menor: a quota dele não é entregue ao representante sem autorização.
- Vender imóvel de menor sem avaliação e sem dizer para onde vai o dinheiro.
- Ajuizar na Justiça Federal o levantamento de FGTS/PIS de falecido (Súmula 161/STJ).
- Fixar índice de correção na peça (remeter ao núcleo).

## Integração com o núcleo
`prazos-processuais`, `juros-e-correcao` (atualização de valores), `verificacao-de-citacoes`, `fidelidade-factual` (valores e contas), `estilo-forense`. Inventário: `sucessoes-inventario-judicial`, `sucessoes-inventario-extrajudicial`.

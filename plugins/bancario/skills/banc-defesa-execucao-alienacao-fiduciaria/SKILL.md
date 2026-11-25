---
name: banc-defesa-execucao-alienacao-fiduciaria
description: >
  Organiza a defesa do devedor em execução de crédito garantido por alienação
  fiduciária de bem móvel: conversão da busca e apreensão em execução (DL
  911/1969, art. 4º), ação executiva direta (art. 5º), cobrança do saldo
  remanescente após a venda do bem (art. 2º; CC, art. 1.366), procedimento
  extrajudicial em cartório ou no Detran (arts. 8º-B a 8º-E, Lei 14.711/2023) e
  a extinção da dívida após leilão de imóvel residencial (Lei 9.514/1997, art.
  26-A, § 4º). Use quando o usuário pedir embargos à execução do banco com
  carro alienado, defesa na execução do saldo devedor depois que o banco
  vendeu o veículo, prestação de contas da venda, notificação de cartório
  para pagar em 20 dias, consolidação extrajudicial de veículo ou execução de
  saldo após leilão do imóvel.
metadata:
  area: bancario
  tipo_peca: contestacao
  verificado_em: 2026-11-25
---
# Defesa em execução com alienação fiduciária

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar:
  - (a) busca e apreensão **convertida em execução** porque o bem não foi achado (DL 911, art. 4º), ou execução direta do contrato (art. 5º);
  - (b) execução ou cobrança do **saldo remanescente** depois que o credor vendeu o bem apreendido;
  - (c) notificação no procedimento **extrajudicial** de consolidação (art. 8º-B) ou busca e apreensão extrajudicial (art. 8º-C);
  - (d) execução de saldo após **leilão de imóvel** alienado fiduciariamente.
- Não usar:
  - Busca e apreensão judicial em curso, liminar cumprida → `banc-busca-e-apreensao-contestacao`.
  - Nulidade do procedimento extrajudicial do **imóvel** (intimação, leilão, purgação) → `imob-revisao-de-financiamento-sfh`.
  - Forma e requisitos gerais dos embargos (prazo, efeito suspensivo, excesso) → `civel-embargos-a-execucao`; matéria de ordem pública sem garantia → `civel-excecao-de-pre-executividade`.
  - Revisional autônoma → `consumidor-contratos-bancarios-revisional`.

## Entradas mínimas (perguntar o que faltar; nunca supor fatos)
1. Título executado (cédula de crédito bancário, contrato) e demonstrativo do débito.
2. Histórico: houve busca e apreensão? O bem foi apreendido? Quando e por quanto foi vendido? Há **prestação de contas** da venda?
3. Valor de mercado do bem na data da venda (tabela de referência, laudo, anúncios).
4. Para imóvel: era financiamento de aquisição/construção de **imóvel residencial** do devedor? Houve 2º leilão sem lance mínimo?
5. Para o procedimento extrajudicial: cláusula **em destaque** no contrato autorizando a via extrajudicial; data da notificação; canal (cartório ou órgão de trânsito).
6. Bens penhorados e sua natureza (bem de família, salário etc.).
7. Garantidores (avalistas, fiadores) e se assinaram a renegociação, se houve.

## Prazo e contagem
- Embargos e demais defesas na execução: prazos, termo inicial e contagem pelo núcleo `prazos-processuais` e pelo roteiro de `civel-embargos-a-execucao`.
- Procedimento extrajudicial de móvel: notificação para pagar em **20 dias** ou apresentar prova de cobrança indevida (art. 8º-B). Após a apreensão extrajudicial, quitação em **5 dias úteis** (art. 8º-C).
- Registre sempre: data da venda do bem, valor obtido, data da notificação.

## Estrutura da peça
Tempestividade → síntese do título e do histórico da garantia → preliminares (título, liquidez, via eleita) → saldo: prestação de contas e preço da venda → extinção legal da dívida (imóvel) → encargos e excesso → penhora → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Saldo remanescente só depois de contas prestadas.** O credor vende o bem, aplica o preço na dívida e entrega o saldo ao devedor, **com prestação de contas** (art. 2º, caput). Sem demonstração do preço obtido e das despesas, o saldo cobrado é ilíquido.
- O devedor responde pelo restante se o preço não bastar (CC, art. 1.366) — a defesa ataca o **valor de venda**, as despesas lançadas e os encargos, não a existência do saldo em si.
- Cláusula que permite ao credor ficar com o bem sem vendê-lo é nula (CC, art. 1.365).
- **Imóvel residencial financiado (art. 26-A):** sem lance que alcance o referencial mínimo no 2º leilão, a dívida é **extinta** com quitação recíproca (art. 26-A, § 4º), inclusive se o credor optou pela via judicial (§ 5º). Fora dessa hipótese, o saldo pode ser executado (art. 27, § 5º-A).
- **Procedimento extrajudicial (arts. 8º-B a 8º-E):** exige cláusula expressa em destaque e mora comprovada; a via extrajudicial não impede o devedor de ir a juízo (art. 8º-C); cobrança indevida sujeita o credor à multa e indenização do art. 3º, §§ 6º e 7º (art. 8º-D). Há ADIs no STF contra esses dispositivos [VERIFICAR: ADI 7600, 7601 e 7608 — estado do julgamento].
- Na execução convertida ou direta, penhoram-se bens bastantes para garantir a execução (art. 5º); o parágrafo único afasta algumas impenhorabilidades [VERIFICAR: alcance do parágrafo único frente ao CPC/2015].

## Fundamentos verificados
- DL 911/1969, arts. 2º, 3º (§§ 6º e 7º), 4º, 5º e 8º-B a 8º-E.
- CC, arts. 1.361, 1.364, 1.365 e 1.366.
- Lei 9.514/1997, arts. 26-A (§§ 3º a 5º) e 27 (§§ 4º, 5º e 5º-A), redação da Lei 14.711/2023.
- Súmula 286/STJ: renegociação ou confissão de dívida não impede discutir ilegalidades dos contratos anteriores.
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Extinção da execução do saldo por iliquidez, sem a prestação de contas da venda; ou suspensão até que o credor a apresente.
- Recálculo do saldo pelo valor de mercado do bem, se a venda foi por preço vil, e exclusão de despesas não comprovadas.
- Declaração de extinção da dívida (art. 26-A, § 4º) no imóvel residencial financiado.
- Decote de encargos abusivos e reconhecimento de excesso, com valor que entende devido (forma em `civel-embargos-a-execucao`).
- No extrajudicial: suspensão ou anulação do procedimento, multa e indenização (art. 8º-D c/c art. 3º, §§ 6º e 7º).
- Levantamento de penhora sobre bem impenhorável.
- Juros e correção: núcleo `juros-e-correcao`.

## Checklist pré-protocolo
- [ ] Identificada a via (art. 4º, art. 5º, saldo pós-venda, extrajudicial, imóvel)
- [ ] Prestação de contas da venda exigida ou analisada
- [ ] Valor de mercado do bem documentado
- [ ] Hipótese do art. 26-A conferida (imóvel residencial financiado)
- [ ] Cláusula em destaque conferida (via extrajudicial)
- [ ] Valor incontroverso indicado, se alegar excesso
- [ ] Prazos conferidos em `prazos-processuais`
- [ ] Citações conferidas em `verificacao-de-citacoes`

## Erros a evitar
- Negar o saldo remanescente em tese — a lei o admite (CC, art. 1.366; Lei 9.514, art. 27, § 5º-A); o ataque é ao cálculo.
- Esquecer de pedir as contas da venda antes de discutir o valor.
- Aplicar a extinção do art. 26-A, § 4º, a imóvel que não era financiamento residencial do devedor ou a consórcio.
- Tratar o procedimento extrajudicial como inexistente: responder no prazo de 20 dias com a prova da cobrança indevida.
- Repetir aqui teses de nulidade do leilão do imóvel que pertencem a `imob-revisao-de-financiamento-sfh`.

## Integração com o núcleo
`prazos-processuais`, `juros-e-correcao`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

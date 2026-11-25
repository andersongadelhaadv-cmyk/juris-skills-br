---
name: imob-cobranca-de-taxas-condominiais
description: >
  Redige execução de título extrajudicial de cotas condominiais (CPC, art.
  784, X) ou ação de cobrança pelo procedimento comum, com parcelas
  vincendas, multa de até 2% e definição do devedor (proprietário,
  promissário comprador imitido na posse, adquirente) pelo CC, arts. 1.336 e
  1.345. Use quando o usuário pedir para cobrar condomínio atrasado, executar
  inadimplente de condomínio, penhorar a unidade devedora, incluir cotas
  vincendas, definir contra quem cobrar após venda da unidade ou responder
  sobre prescrição de cota condominial.
metadata:
  area: imobiliario
  tipo_peca: inicial
  verificado_em: 2026-11-25
---
# Cobrança de taxas condominiais

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: condomínio edilício credor de contribuições ordinárias ou extraordinárias (previstas na convenção ou aprovadas em assembleia) contra o titular da unidade.
- Não usar: taxa de associação de moradores ou loteamento sem condomínio edilício (regime próprio — conferir os Temas 882/STJ e 492/STF antes [VERIFICAR: não conferidos nesta skill]); condômino que quer exigir contas (`imob-prestacao-de-contas-de-condominio`); locador cobrando condomínio do inquilino junto com aluguel (`imob-acao-de-despejo`); defesa do executado (`civel-embargos-a-execucao` ou `civel-excecao-de-pre-executividade`).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Convenção e regimento; atas que aprovaram orçamento, rateio e cotas extras, com lista de presença.
2. Demonstrativo por competência: vencimento, valor original, natureza (ordinária/extraordinária), boletos.
3. Matrícula atualizada da unidade e dados de quem ocupa: proprietário registral, promissário comprador, inquilino.
4. O condomínio foi comunicado de venda ou promessa? Quando houve imissão na posse do comprador?
5. Ata de eleição do síndico em vigor (representação — CC, art. 1.348, II).
6. Acordos anteriores, confissões ou parcelamentos (podem interromper a prescrição).
7. Devedor em recuperação judicial ou falência? Há outros credores com penhora sobre a unidade?

## Prazo e contagem
- Prescrição: cinco anos para dívidas líquidas constantes de instrumento (CC, art. 206, § 5º, I). O STJ aplica esse prazo à cobrança de taxas de manutenção (REsp 2.053.466); o repetitivo específico sobre cotas de condomínio edilício não foi confirmado no JuriBase [VERIFICAR: número e tese do repetitivo]. Contar cada parcela do seu vencimento.
- Acordo que configure novação interrompe a prescrição (STJ, AgInt no AREsp 2.919.485).
- Execução: citação para pagar em 3 dias (CPC, art. 829). Demais prazos em `prazos-processuais`.

## Estrutura da peça
Endereçamento → qualificação do condomínio (representado pelo síndico) e do devedor → título (convenção/atas + demonstrativo) → legitimidade passiva → débito → parcelas vincendas → penhora da unidade → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Título extrajudicial: crédito de contribuições ordinárias ou extraordinárias previstas na convenção ou aprovadas em assembleia, documentalmente comprovadas (CPC, art. 784, X). O condomínio pode optar pelo processo de conhecimento mesmo tendo título (STJ, REsp 2.025.425, que aplica o art. 785 do CPC).
- Parcelas vincendas incluem-se no pedido e na condenação enquanto durar a obrigação (CPC, art. 323; REsp 2.025.425).
- Obrigação propter rem: o adquirente responde pelos débitos do alienante, inclusive multas e juros (CC, art. 1.345); o imóvel gerador do débito pode ser penhorado mesmo que o proprietário não tenha figurado na fase de conhecimento (STJ, REsp 2.055.415).
- Promissário comprador: o que define a responsabilidade é a imissão na posse e a ciência inequívoca do condomínio (Tema 886/STJ, aplicado no REsp 2.156.030). A tese está em revisão no Tema 1349/STJ, afetado em 2025 [VERIFICAR: situação do julgamento antes de protocolar]. Na dúvida, incluir ambos e justificar.
- Não há litisconsórcio necessário entre coproprietários; juros de mora correm do vencimento de cada parcela (STJ, AREsp 3.122.301).

## Fundamentos verificados
- CC: arts. 206, § 5º, I; 1.315; 1.334, I e § 2º; 1.336, I e § 1º; 1.345; 1.348, II e VII.
- CPC: arts. 323, 784, X, 829.
- Multa moratória de até 2% sobre o débito; juros convencionados ou, na falta, os do art. 406 do CC (CC, art. 1.336, § 1º) — taxa e índice sempre pelo núcleo `juros-e-correcao`.
- Cotas condominiais anteriores à recuperação judicial têm natureza extraconcursal (Tema 1391/STJ, REsp 2.206.633, julg. 13/05/2026).
- O crédito trabalhista prevalece sobre o condominial no concurso de credores (STJ, REsp 2.258.516).
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Execução: citação para pagar em 3 dias, sob pena de penhora, preferencialmente da própria unidade; averbação da execução na matrícula.
- Conhecimento: condenação ao pagamento das cotas vencidas e vincendas até o efetivo pagamento.
- Multa de até 2%, correção e juros desde cada vencimento (cálculo pelo núcleo `juros-e-correcao`).
- Honorários e custas.

## Checklist pré-protocolo
- [ ] Ata que aprovou o orçamento/rateio de cada período cobrado
- [ ] Ata de eleição do síndico vigente e procuração
- [ ] Matrícula atualizada; checada posse do promissário comprador e ciência do condomínio
- [ ] Parcelas prescritas excluídas (cinco anos de cada vencimento)
- [ ] Multa limitada a 2%; taxas e índices pelo núcleo
- [ ] Situação do Tema 1349/STJ conferida, se houver promessa de compra e venda
- [ ] Recuperação judicial do devedor pesquisada (Tema 1391/STJ)

## Erros a evitar
- Executar cota extraordinária sem a ata que a aprovou (perde-se a força do art. 784, X).
- Cobrar multa acima de 2% com base em convenção antiga.
- Cobrar só do proprietário registral quando o condomínio sabia da venda e da posse do comprador (ou o contrário).
- Esquecer as vincendas e precisar de nova ação a cada mês.
- Aplicar taxa de juros "de memória": remeter ao núcleo.

## Integração com o núcleo
`juros-e-correcao`, `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`; execução em geral: `civel-execucao-titulo-extrajudicial`.

---
name: imob-prestacao-de-contas-de-condominio
description: >
  Redige ação de exigir contas do condomínio contra síndico, ex-síndico ou
  administradora (CC, art. 1.348, VIII; CPC, arts. 550 a 553), nas duas
  fases do procedimento, e orienta o condômino individual sobre as vias
  internas (assembleia, conselho fiscal, destituição). Use quando o usuário
  pedir prestação de contas do síndico, ex-síndico que não entregou contas,
  auditoria de administradora de condomínio, apuração de saldo contra o
  gestor ou quando um condômino quiser exigir contas sozinho.
metadata:
  area: imobiliario
  tipo_peca: inicial
  verificado_em: 2026-11-25
---
# Prestação de contas de condomínio

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: o condomínio (por novo síndico ou por quem a assembleia indicar) quer que síndico, ex-síndico ou administradora preste contas da gestão e, se houver saldo, que seja condenado a pagá-lo.
- Não usar: condômino isolado que quer exigir contas em juízo — falta-lhe legitimidade (ver abaixo); anulação de assembleia que aprovou contas (ação anulatória, prazo decadencial — ver Prazo); cobrança de cotas (`imob-cobranca-de-taxas-condominiais`); reparação por desvio já apurado (indenizatória — `civel-peticao-inicial`); contas de locação em shopping center (art. 54 da Lei 8.245/1991, regime próprio — conferir antes [VERIFICAR: art. 54, § 2º, não conferido nesta skill]).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Quem será autor: o condomínio, representado por quem (ata de eleição do novo síndico ou deliberação que outorgou poderes — CC, art. 1.348, § 1º).
2. Quem será réu e por qual período geriu (atas de eleição e de destituição, contrato com a administradora).
3. As contas foram prestadas à assembleia? Foram aprovadas ou rejeitadas? (atas).
4. Pedidos extrajudiciais de contas e documentos já feitos, com resposta.
5. Indícios de irregularidade: extratos, notas, contratos, parecer do conselho fiscal (CC, art. 1.356), auditoria.
6. Período a ser abrangido (atenção à prescrição).

## Prazo e contagem
- Prescrição da pretensão de exigir contas do ex-síndico: o STJ manteve a prescrição decenal, alcançando só o decênio anterior ao ajuizamento (AgInt nos EDcl no AREsp 2.664.565).
- Anulação de assembleia que aprovou as contas: ato anulável, prazo decadencial de dois anos (CC, art. 179), conforme o STJ (AgInt no AREsp 2.662.240) [VERIFICAR: art. 179 do CC não conferido nesta skill].
- Prazos do rito: 15 dias para o réu prestar contas ou contestar; 15 dias para o autor se manifestar; 15 dias para cumprir a condenação (CPC, art. 550). Contagem em `prazos-processuais`.

## Estrutura da peça
Endereçamento → qualificação (condomínio e gestor) → dever de prestar contas → período e pedido extrajudicial → razões e documentos (CPC, art. 550, § 1º) → pedidos das duas fases → valor da causa. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Legitimidade ativa: o síndico presta contas à assembleia (CC, art. 1.348, VIII), e não ao condômino individualmente; o condômino isolado é parte ilegítima para a ação de exigir contas (STJ, REsp 2.050.372; AgInt no AREsp 2.803.656).
- Interesse de agir: contas prestadas e aprovadas em assembleia afastam o interesse na ação de exigir contas; irregularidade se discute em ação própria (STJ, AgInt no AREsp 2.027.906). Se as contas não foram prestadas, o condomínio tem interesse (STJ, AgInt no AREsp 2.426.154).
- A inicial especifica as razões do pedido e vem com os documentos existentes (CPC, art. 550, § 1º).

## Fundamentos verificados
- CC: arts. 1.348, VIII e § 1º; 1.349; 1.350 e § 1º; 1.355; 1.356.
- CPC: arts. 550 a 553 (duas fases; contas em forma adequada, com receitas, despesas e investimentos; sentença que apura o saldo é título executivo judicial).
- Vias do condômino individual: convocação de assembleia por um quarto dos condôminos (CC, arts. 1.350, § 1º, e 1.355); destituição do síndico que não presta contas, pela maioria absoluta da assembleia especialmente convocada (CC, art. 1.349); parecer do conselho fiscal (CC, art. 1.356); se a assembleia não se reunir, o juiz decide a requerimento de qualquer condômino (CC, art. 1.350, § 2º).
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Citação do réu para, em 15 dias, prestar as contas do período indicado ou contestar (CPC, art. 550).
- Procedência para condenar o réu a prestar contas em 15 dias, sob pena de não poder impugnar as que o autor apresentar (art. 550, § 5º).
- Não prestadas, autorização para o autor apresentá-las, com perícia se necessária (art. 550, § 6º).
- Exibição dos documentos dos lançamentos impugnados (art. 551, § 1º).
- Apuração do saldo e condenação ao pagamento, constituindo título executivo (art. 552); correção e juros pelo núcleo `juros-e-correcao`.
- Custas e honorários.

## Checklist pré-protocolo
- [ ] Autor é o condomínio, com representação comprovada (ata/deliberação)
- [ ] Período de gestão do réu documentado
- [ ] Contas não prestadas, ou prestadas e não aprovadas (se aprovadas, avaliar anulatória)
- [ ] Pedido extrajudicial anterior juntado (reforça o interesse)
- [ ] Razões específicas do pedido e documentos (art. 550, § 1º)
- [ ] Período limitado ao decênio anterior ao ajuizamento
- [ ] Saldo e encargos calculados pelo núcleo

## Erros a evitar
- Ajuizar em nome de um condômino isolado (ilegitimidade — REsp 2.050.372).
- Exigir em juízo contas já aprovadas em assembleia, sem atacar a aprovação (falta de interesse — AgInt no AREsp 2.027.906).
- Pedido genérico sem período e sem razões (art. 550, § 1º).
- Confundir exigir contas com indenização por desvio: a primeira apura saldo; a segunda exige prova do dano.
- Deixar passar o prazo para anular a assembleia que aprovou contas irregulares.

## Integração com o núcleo
`juros-e-correcao`, `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

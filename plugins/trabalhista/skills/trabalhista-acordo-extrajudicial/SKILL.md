---
name: trabalhista-acordo-extrajudicial
description: >
  Redige a petição conjunta de homologação de acordo extrajudicial na Justiça do
  Trabalho (CLT arts. 855-B a 855-E), com advogados distintos para cada parte,
  discriminação das parcelas e de sua natureza, e quitação limitada ao que for
  especificado. Use quando o usuário pedir homologação de acordo extrajudicial,
  jurisdição voluntária trabalhista, acordo trabalhista fora do processo,
  formalizar rescisão com quitação homologada, ou recorrer da recusa de homologação.
metadata:
  area: trabalhista
  tipo_peca: requerimento
  verificado_em: 2026-11-01
---
# Homologação de acordo extrajudicial

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: empregado e empregador já acordaram e querem sentença homologatória (CLT art. 652 "f"; arts. 855-B e ss.).
- Não usar: acordo em processo já ajuizado (petição de acordo nos autos); quitação anual perante sindicato (art. 507-B, instrumento diverso); quando uma das partes não tem advogado próprio.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
- Dados do contrato (admissão, saída, função, salário) e motivo da extinção.
- Verbas rescisórias já pagas e prazo de pagamento (art. 477 §6º).
- Parcelas objeto do acordo, valores, natureza (salarial ou indenizatória), forma e datas de pagamento, multa por atraso.
- Advogado de cada parte (não pode ser comum).
- Alcance da quitação pretendido.

## Prazo e contagem
- Juiz decide em 15 dias da distribuição, podendo designar audiência (art. 855-D).
- A petição suspende a prescrição quanto aos direitos nela especificados; negada a homologação, a prescrição volta a correr no dia útil seguinte ao trânsito (art. 855-E).
- O acordo não afasta o prazo de 10 dias para verbas rescisórias nem a multa do art. 477 §8º (art. 855-C).

## Estrutura da peça
Petição conjunta; qualificação; resumo do contrato; termos do acordo por parcela; natureza e encargos fiscais e previdenciários; quitação; cláusula penal; pedido de homologação. Roteiro em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Petição conjunta, advogado obrigatório, sem advogado comum; o trabalhador pode ser assistido pelo advogado do sindicato (art. 855-B e §§).
- Discriminar a natureza das parcelas e a responsabilidade pelo recolhimento previdenciário (art. 832 §3º, aplicável às decisões homologatórias).
- **Quitação**: a jurisprudência do TST se divide sobre quitação geral do contrato. Há acórdão localizado (2ª Turma, Ag-RR-1000860-73.2025.5.02.0083, 05/05/2026) discutindo a homologação com quitação ampla; ler o inteiro teor antes de prometer quitação geral ao cliente [VERIFICAR orientação atual da SDI-1]. Recomendação prudente: quitar parcelas especificadas.
- A homologação é faculdade do juiz: não há direito líquido e certo, logo não cabe MS contra a recusa (Súmula 418 do TST). Contra a sentença que nega a homologação, a via é o recurso ordinário [VERIFICAR posicionamento atual].

## Fundamentos verificados
CLT arts. 477 §§6º e 8º, 507-B, 652 "f", 832 §3º, 855-B a 855-E; Súmula 418 do TST; Súmula 100 V do TST (termo homologado transita na data da homologação). Detalhes em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Homologação do acordo nos termos da petição.
- Discriminação da natureza das parcelas na sentença.
- Designação de audiência, se o juízo entender necessária.
- Correção e juros em caso de inadimplemento: remeter à skill `juros-e-correcao` ou fixar cláusula penal, sem estipular taxa de juros por conta própria.

## Checklist pré-protocolo
- [ ] Dois advogados distintos, com procurações.
- [ ] Verbas rescisórias pagas no prazo legal (ou multa prevista).
- [ ] Cada parcela com valor e natureza.
- [ ] Quitação delimitada às parcelas e ao contrato indicados.
- [ ] Cláusula penal e vencimento antecipado definidos.
- [ ] Recolhimentos fiscais e previdenciários atribuídos.

## Erros a evitar
- Advogado único para as duas partes.
- Usar o acordo para escapar da multa do art. 477 §8º.
- Rotular tudo como indenizatório sem lastro.
- Prometer quitação geral como certa.

## Integração com o núcleo
`juros-e-correcao`, `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

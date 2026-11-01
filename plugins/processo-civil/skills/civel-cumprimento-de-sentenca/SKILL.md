---
name: civel-cumprimento-de-sentenca
description: >
  Redige requerimento de cumprimento de sentença cível (CPC arts. 513 a 538):
  pagar quantia (art. 523, com multa de 10% e honorários de 10% do §1º),
  provisório (art. 520), obrigação de fazer/não fazer e entregar coisa (arts. 536
  a 538) e contra a Fazenda Pública (arts. 534 e 535). Use quando o usuário pedir
  cumprimento de sentença, execução de sentença, "executar a condenação",
  intimar o devedor para pagar, cobrar astreintes ou executar a Fazenda.
metadata:
  area: processo-civil
  tipo_peca: execucao
  verificado_em: 2026-11-01
---
# Cumprimento de sentença (cível)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: título judicial do art. 515 (sentença, homologação de acordo, sentença arbitral, sentença penal condenatória, sentença estrangeira homologada etc.).
- Provisório: sentença impugnada por recurso sem efeito suspensivo (art. 520).
- Não usar: título extrajudicial (`civel-execucao-titulo-extrajudicial`); defesa do executado (`civel-impugnacao-ao-cumprimento`); alimentos e execução fiscal (skills próprias de família e fazenda).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
- Título (sentença/acórdão), certidão de trânsito ou indicação do recurso pendente e seus efeitos.
- Parâmetros da condenação: principal, índices, termo inicial de juros e correção, honorários, multas.
- Dados do executado (CPF/CNPJ) e bens conhecidos.
- Data do trânsito em julgado (se o requerimento vier após 1 ano, a intimação é pessoal — art. 513, §4º).
- Para Fazenda: ente, valor (precatório ou RPV).

## Prazo e contagem
- Pagamento voluntário em 15 dias úteis após intimação (art. 523). Sem pagamento, incidem multa de 10% e honorários de 10% (§1º); pagamento parcial reduz a base (§2º).
- Impugnação corre a partir do fim desse prazo, em mais 15 dias (art. 525).
- Fazenda: impugnação em 30 dias; sem multa do art. 523 (art. 534, §2º).
- Prescrição intercorrente também no cumprimento (art. 921, §7º). Use `prazos-processuais`.

## Estrutura da peça
Endereçamento ao juízo da causa → exequente e executado (art. 524, I) → título e exigibilidade → demonstrativo discriminado → pedido de intimação para pagar → penhora/indicação de bens → medidas complementares (protesto, averbação, SISBAJUD) → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Requerimento do exequente (art. 513, §1º).
- Demonstrativo com índice, juros e taxas, termos inicial e final, capitalização e descontos (art. 524, II a VI; para a Fazenda, art. 534).
- Não pode ser promovido contra fiador ou coobrigado que não participou da fase de conhecimento (art. 513, §5º).
- Provisório: caução para levantamento e atos de alienação (art. 520, IV), com dispensas do art. 521; multa e honorários também são devidos (art. 520, §2º).
- Astreintes: exige intimação pessoal prévia do devedor (Súmula 410 do STJ).

## Fundamentos verificados
CPC arts. 513, 515, 517, 520, 523, 524, 526, 534 a 537, 835, 854, 921; Súmulas 410, 517 e 519 do STJ. Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Intimação do executado para pagar em 15 dias, sob pena de multa de 10% e honorários de 10% (art. 523, §1º).
- Não havendo pagamento: penhora e avaliação (§3º), com bloqueio de ativos (art. 854) e penhora preferencial de dinheiro (art. 835, §1º).
- Protesto da decisão (art. 517) e inclusão em cadastros, se cabível.
- Fazenda: intimação para impugnar em 30 dias; expedição de precatório ou RPV (art. 535, §3º).
- Obrigação de fazer: fixação ou execução da multa e medidas do art. 536, §1º.

## Checklist pré-protocolo
- [ ] Título exequível e exigível; trânsito em julgado ou efeito do recurso pendente.
- [ ] Demonstrativo com todos os itens do art. 524 (ou art. 534).
- [ ] Juros e correção calculados pela skill `juros-e-correcao` (sem taxa fixa).
- [ ] Multa e honorários do §1º só depois do prazo de 15 dias (não incluir antes).
- [ ] Intimação pessoal pedida se passou 1 ano do trânsito (art. 513, §4º) ou se for cobrança de astreintes.
- [ ] Bens indicados (art. 524, VII).
- [ ] Fazenda: sem multa do art. 523; honorários conforme art. 85, §7º.

## Erros a evitar
- Incluir a multa de 10% e os honorários de 10% no cálculo inicial.
- Calcular juros de 1% ao mês por hábito; aplicar o regime vigente via núcleo.
- Cumprimento contra quem não foi parte na fase de conhecimento.
- Pedir multa do art. 523 contra a Fazenda.
- Cobrar astreintes sem intimação pessoal do devedor.

## Integração com o núcleo
- `juros-e-correcao` (obrigatório) para o demonstrativo.
- `prazos-processuais` para prazo de pagamento, impugnação e prescrição intercorrente.
- `verificacao-de-citacoes` para precedentes acrescentados.
- `fidelidade-factual` para os parâmetros do título.
- `estilo-forense` na revisão.

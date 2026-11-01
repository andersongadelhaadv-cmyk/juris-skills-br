---
name: fazenda-contestacao-fazendaria
description: >
  Redige contestação em nome da Fazenda Pública (União, Estados, DF, Municípios,
  autarquias e fundações de direito público), com prazo em dobro e intimação
  pessoal (CPC art. 183), indisponibilidade do interesse público (art. 345, II)
  e atenção à remessa necessária (art. 496). Use quando o usuário for procurador
  ou advogado público e pedir contestação do ente público, defesa da União, do
  Estado ou do Município, resposta em ação contra a Fazenda, defesa em repetição
  de indébito, anulatória ou ação de cobrança contra o poder público.
metadata:
  area: tributario-fazenda
  tipo_peca: contestacao
  verificado_em: 2026-11-01
---
# Contestação da Fazenda Pública

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: defesa do ente público em procedimento comum (ações tributárias do contribuinte, ações de cobrança, indenizatórias, de servidores), inclusive juizado da Fazenda com as adaptações locais.
- Não usar: informações em mandado de segurança (peça da autoridade coatora, prazo de 10 dias, sem dobra); impugnação ao cumprimento de sentença (veja `fazenda-cumprimento-contra-a-fazenda`); embargos à execução de título extrajudicial (CPC art. 910). Para a estrutura geral da contestação, combine com `civel-contestacao`.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
- Inicial e documentos; data e forma da intimação pessoal (carga, remessa ou meio eletrônico).
- Subsídios do órgão de origem (Receita, Secretaria, autarquia): processo administrativo, cálculos, pareceres, atos normativos internos.
- Existência de orientação vinculante interna, dispensa de contestar ou parecer que reconheça o pedido (relevante para CPC art. 496, §4º, IV e para eventual reconhecimento).
- Valor da causa e proveito econômico estimado.

## Prazo e contagem
- Prazo em dobro para todas as manifestações, contado da intimação pessoal (CPC art. 183, caput e §1º): contestação em 30 dias úteis no procedimento comum (art. 335 c/c 183 e 219).
- Sem dobra quando a lei fixar prazo próprio (art. 183, §2º), p.ex. juizados especiais da Fazenda e prazos específicos de leis especiais.
- Use `prazos-processuais`.

## Estrutura da peça
Endereçamento → qualificação do ente e representação (órgão de advocacia pública) → tempestividade (art. 183) → síntese → preliminares (art. 337) → prejudiciais (prescrição quinquenal, decadência) → mérito → eventualidade (juros, correção, honorários, termo inicial) → provas → pedidos. Roteiro em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Prerrogativas: intimação pessoal; dispensa de preparo (CPC art. 1.007, §1º; LEF art. 39 na execução fiscal); citação na pessoa do órgão de advocacia pública (CPC art. 242, §3º).
- Revelia: não induz presunção de veracidade, pois o litígio versa sobre direitos indisponíveis (CPC art. 345, II). Ainda assim, impugne especificamente cada fato.
- Prescrição: quinquenal contra a Fazenda (Decreto 20.910/1932); em trato sucessivo, só as parcelas anteriores ao quinquênio (Súmula 85 STJ). Repetição de indébito: CTN art. 168 e Súmula 625 STJ.
- Tributos indiretos: exija a prova do encargo (CTN art. 166; Súmula 546 STF).
- Eventualidade sobre atualização: remeta ao regime constitucional vigente e ao `juros-e-correcao` (EC 113/2021 com a redação da EC 136/2025; Tema 1419 STF). Não escreva taxa própria.
- Honorários: escalonamento do CPC art. 85, §3º; sentença ilíquida define o percentual na liquidação (§4º, II).

## Fundamentos verificados
CPC arts. 85, §§3º e 4º, 183, 219, 242, §3º, 335, 336, 337, 341, 345, II, 496 e 1.007, §1º; Decreto 20.910/1932; CTN arts. 166 e 168; Súmulas 85, 325, 483 e 490 STJ; Súmula 546 STF; Tema 1419 STF. Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Acolhimento das preliminares; extinção sem mérito.
- Pronúncia da prescrição (total ou das parcelas anteriores ao quinquênio).
- Improcedência; subsidiariamente, limitação da condenação, termo inicial correto de juros e correção pelo regime constitucional vigente e honorários pelo art. 85, §3º.
- Intimações pessoais ao órgão de representação; remessa necessária, se cabível.

## Checklist pré-protocolo
- [ ] Data da intimação pessoal e prazo em dobro (dias úteis) conferidos; verificar se há prazo próprio sem dobra.
- [ ] Subsídios técnicos do órgão de origem anexados.
- [ ] Orientação vinculante interna consultada (pode impor reconhecimento ou dispensar recurso).
- [ ] Prescrição quinquenal e Súmula 85 STJ examinadas.
- [ ] Pedido subsidiário sobre juros/correção remetido ao núcleo, sem taxa própria.
- [ ] Pedido de honorários pelo art. 85, §3º.

## Erros a evitar
- Contar 15 dias ou deixar de contar da intimação pessoal.
- Confiar na indisponibilidade e deixar de impugnar fatos específicos.
- Omitir a eventualidade sobre juros, correção e honorários.
- Sustentar tese contrária a orientação vinculante do próprio ente (afasta a remessa necessária e expõe a recurso inútil).
- Aplicar a dobra a prazo próprio fixado em lei.

## Integração com o núcleo
- `prazos-processuais`: prazo em dobro, termo inicial e exceções.
- `juros-e-correcao`: regime de atualização das condenações da Fazenda.
- `verificacao-de-citacoes`: todo precedente acrescentado.
- `fidelidade-factual`: subsídios do órgão contra a narrativa da inicial.
- `estilo-forense`: revisão final.

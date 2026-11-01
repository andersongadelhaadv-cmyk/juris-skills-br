---
name: civel-replica
description: >
  Redige réplica (manifestação do autor sobre a contestação) nos termos dos arts.
  350, 351 e 437 do CPC, rebatendo preliminares, fatos impeditivos, modificativos
  ou extintivos e documentos novos. Use quando o usuário pedir réplica,
  "impugnação à contestação", "manifestação sobre a contestação", resposta às
  preliminares do réu ou falar sobre documentos juntados pelo réu.
metadata:
  area: processo-civil
  tipo_peca: replica
  verificado_em: 2026-11-01
---
# Réplica (manifestação sobre a contestação)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: intimação do autor para falar sobre contestação que trouxe preliminar (art. 351), fato impeditivo/modificativo/extintivo (art. 350) ou documento (art. 437).
- Não usar: resposta à reconvenção (é contestação do reconvindo, art. 343, §1º — use `civel-contestacao`); juizado especial (a resposta ao pedido contraposto é oral ou em nova data — Lei 9.099, art. 31, p.ú.).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
- Contestação e documentos do réu; data da intimação para réplica.
- Posição do cliente sobre cada fato novo trazido pelo réu e documentos de contraprova.
- Se houve reconvenção (resposta separada, mesmo prazo).

## Prazo e contagem
- 15 dias úteis da intimação (arts. 350, 351 e 219). Documentos: 15 dias (art. 437, §1º).
- Falsidade documental deve ser suscitada na réplica, se o documento veio com a contestação (art. 430).
- Use `prazos-processuais`.

## Estrutura da peça
Endereçamento → tempestividade → síntese da contestação → resposta às preliminares → resposta às prejudiciais → resposta aos fatos novos → impugnação de documentos → reforço do mérito → provas → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- A réplica não amplia pedido nem causa de pedir: após a citação, isso exige consentimento do réu, e após o saneamento é vedado (art. 329).
- Ilegitimidade arguida pelo réu: avaliar substituição ou inclusão do indicado em 15 dias (arts. 338 e 339) — prazo que corre junto com a réplica.
- Impugnação de autenticidade ou falsidade exige argumentação específica (art. 436, p.ú.).

## Fundamentos verificados
CPC arts. 329, 338, 339, 350, 351, 430, 436, 437. Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Rejeição das preliminares e prejudiciais.
- Desconsideração/desentranhamento ou valoração adequada dos documentos impugnados.
- Reiteração da procedência; especificação de provas para os fatos novos (o art. 350 garante a produção de prova).
- Se for o caso: substituição do réu ou inclusão de litisconsorte (art. 339, §§1º e 2º).

## Checklist pré-protocolo
- [ ] Toda preliminar respondida, uma a uma.
- [ ] Todo fato impeditivo, modificativo ou extintivo enfrentado, com prova.
- [ ] Documentos novos analisados (admissibilidade, autenticidade, conteúdo).
- [ ] Decisão tomada sobre a indicação de legitimado feita pelo réu.
- [ ] Nenhum pedido novo ou causa de pedir nova introduzida.
- [ ] Provas especificadas.

## Erros a evitar
- Réplica genérica que só "reitera a inicial": fatos novos não rebatidos fortalecem a defesa.
- Perder o prazo de 15 dias para substituir o réu, quando a ilegitimidade é procedente.
- Alegar falsidade sem fundamento concreto.
- Usar a réplica para aditar o pedido.

## Integração com o núcleo
- `prazos-processuais` para os prazos simultâneos (réplica, documentos, substituição do réu).
- `juros-e-correcao` se o réu impugnou o cálculo.
- `verificacao-de-citacoes` para qualquer precedente acrescentado.
- `fidelidade-factual` e `estilo-forense` na revisão final.

---
name: civel-agravo-interno
description: >
  Redige agravo interno contra decisão monocrática de relator ou outra decisão
  unipessoal em tribunal (CPC art. 1.021), com impugnação específica dos
  fundamentos e prevenção da multa do §4º. Use quando o usuário pedir agravo
  interno, agravo regimental, "AgInt", recurso contra decisão monocrática do
  relator, contra decisão do presidente que nega seguimento a REsp/RE com base
  em repetitivo, repercussão geral ou relevância.
metadata:
  area: processo-civil
  tipo_peca: agravo
  verificado_em: 2026-11-01
---
# Agravo interno

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: decisão do relator (art. 1.021) em qualquer recurso ou ação originária; decisão do presidente/vice que nega seguimento a REsp/RE por conformidade com repetitivo, repercussão geral ou relevância, ou que sobrestá (art. 1.030, I e III, c/c §2º).
- Não usar: inadmissão de REsp/RE com base no art. 1.030, V (cabe agravo em REsp/RE, art. 1.042); decisão colegiada (ED, REsp, RE).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
- Decisão monocrática integral e data da intimação.
- Lista dos fundamentos usados pelo relator (cada um será atacado).
- Recurso ou peça original e documentos já nos autos.
- Se a decisão aplicou precedente qualificado: elementos para distinção ou superação.

## Prazo e contagem
- 15 dias úteis (arts. 1.003, §5º, 1.070 e 219); contrarrazões em 15 dias (art. 1.021, §2º).
- Use `prazos-processuais`.

## Estrutura da peça
Endereçamento ao relator → tempestividade → cabimento → síntese da decisão agravada → impugnação de cada fundamento → distinção/superação (se aplicado precedente) → pedido de retratação ou julgamento colegiado → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Impugnação específica dos fundamentos da decisão agravada (art. 1.021, §1º).
- O relator não pode julgar improcedente o agravo apenas repetindo a decisão (§3º) — se o fizer, cabe ED por falta de fundamentação.
- Multa de 1% a 5% do valor atualizado da causa se o agravo for declarado manifestamente inadmissível ou improcedente por unanimidade (§4º); outro recurso fica condicionado ao depósito (§5º), salvo Fazenda e beneficiário da gratuidade.

## Fundamentos verificados
CPC arts. 932, 1.021, 1.030, §2º, 1.035, §7º, 1.042, 1.070; Súmula 182 do STJ; precedente de 2026 sobre fundamento autônomo não impugnado. Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Retratação pelo relator; não havendo, julgamento pelo colegiado com inclusão em pauta (§2º).
- Provimento para reformar a decisão e dar seguimento/provimento ao recurso original.
- Afastamento da multa do §4º (demonstrar fundamentação séria e dissídio razoável).
- Sustentação oral, quando o regimento permitir.

## Checklist pré-protocolo
- [ ] Todos os fundamentos da decisão listados e cada um enfrentado.
- [ ] Distinção concreta, se aplicado precedente qualificado (fatos e ratio).
- [ ] Prazo de 15 dias úteis conferido.
- [ ] Nada de mera reprodução do recurso anterior.
- [ ] Pedido de retratação e, subsidiariamente, de julgamento colegiado.

## Erros a evitar
- Copiar as razões do recurso original: atrai o não conhecimento e a multa do §4º.
- Deixar fundamento autônomo sem ataque (risco de manutenção da decisão por ele).
- Usar agravo interno contra inadmissão do art. 1.030, V (o recurso certo é o do art. 1.042) — ou o inverso.
- Ignorar o depósito da multa ao interpor recurso seguinte.

## Integração com o núcleo
- `prazos-processuais` para o prazo.
- `verificacao-de-citacoes` para todo precedente usado na distinção.
- `fidelidade-factual` para citar a decisão com exatidão.
- `estilo-forense` na revisão.

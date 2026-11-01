---
name: civel-reconvencao
description: >
  Redige reconvenção (pretensão própria do réu contra o autor, CPC art. 343),
  dentro da contestação ou isolada, com conexão, valor da causa próprio e
  requisitos de petição inicial. Use quando o usuário pedir reconvenção,
  "contra-ataque do réu", "pedido do réu contra o autor", ação reconvencional ou
  quiser cobrar/declarar algo contra o autor no mesmo processo.
metadata:
  area: processo-civil
  tipo_peca: reconvencao
  verificado_em: 2026-11-01
---
# Reconvenção

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: o réu quer tutela própria (condenação, declaração, constituição) conexa com a ação principal ou com o fundamento da defesa.
- Usar também na monitória, após os embargos (art. 702, §6º; Súmula 292 do STJ).
- Não usar: juizado especial — lá não cabe reconvenção; o réu formula pedido contraposto fundado nos mesmos fatos (Lei 9.099, art. 31); veja `civel-juizado-especial`.
- Não usar para mera defesa (compensação como exceção, improcedência): isso é contestação.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
- Pretensão do réu, fatos, documentos e valores.
- Demonstração do vínculo de conexão (mesmo pedido ou causa de pedir) ou da ligação com o fundamento da defesa.
- Se a reconvenção envolve terceiro (no polo ativo ou passivo — art. 343, §§3º e 4º).
- Se o réu também vai contestar (a reconvenção pode vir sem contestação — §6º).

## Prazo e contagem
- No prazo da contestação: 15 dias úteis (art. 335). Proposta fora desse momento, a via é ação autônoma.
- O autor-reconvindo responde em 15 dias, intimado na pessoa do advogado (art. 343, §1º).
- Use `prazos-processuais`.

## Estrutura da peça
Tópico destacado na contestação ("Da reconvenção") ou peça própria → qualificação do reconvinte e reconvindo → cabimento e conexão → fatos → fundamentos → tutela (se houver) → pedidos → provas → valor da causa → custas. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Requisitos do art. 319 e documentos do art. 320, como em qualquer inicial.
- Valor da causa próprio (art. 292, caput, refere expressamente a reconvenção).
- Custas da reconvenção, conforme o regimento de custas local.
- Pedido determinado (art. 324, §2º, aplica a regra à reconvenção).
- Autonomia: a extinção da ação principal não impede o julgamento da reconvenção (art. 343, §2º).
- Substituto processual: regra do §5º.

## Fundamentos verificados
CPC arts. 85, §1º, 292, 319, 320, 324, 329, p.ú., 343, 702, §6º; Lei 9.099, art. 31; Súmula 292 do STJ. Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Intimação do reconvindo para responder em 15 dias (art. 343, §1º).
- Procedência dos pedidos reconvencionais, especificados.
- Honorários próprios da reconvenção (art. 85, §1º) e custas.
- Juros e correção do pedido condenatório pela skill `juros-e-correcao`.

## Checklist pré-protocolo
- [ ] Conexão ou ligação com a defesa demonstrada em tópico próprio.
- [ ] Tópico ou peça claramente identificado como reconvenção.
- [ ] Valor da causa da reconvenção indicado e calculado.
- [ ] Custas da reconvenção recolhidas (ou gratuidade).
- [ ] Pedidos certos e determinados.
- [ ] Terceiros, se incluídos, qualificados e com pedido de citação.
- [ ] Protocolo dentro do prazo da contestação.

## Erros a evitar
- Esquecer o valor da causa e as custas da reconvenção.
- Diluir a pretensão no meio da contestação, sem tópico próprio e sem pedido expresso.
- Reconvir em juizado especial.
- Reconvenção à reconvenção em monitória (vedada pelo art. 702, §6º).
- Pedido de compensação que é só defesa, tratado como reconvenção (ou o inverso, quando há saldo a cobrar).

## Integração com o núcleo
- `prazos-processuais` (prazo único com a contestação).
- `juros-e-correcao` para os pedidos condenatórios.
- `verificacao-de-citacoes` para precedentes acrescentados.
- `fidelidade-factual` e `estilo-forense` na revisão.

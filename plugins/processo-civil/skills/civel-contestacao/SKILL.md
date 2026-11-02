---
name: civel-contestacao
description: >
  Redige contestação no procedimento comum cível (CPC arts. 335 a 342), com
  preliminares do art. 337, impugnação específica dos fatos (art. 341) e
  concentração de toda a defesa (art. 336). Use quando o usuário pedir
  contestação, defesa do réu, resposta à inicial, "contestar a ação",
  preliminar de ilegitimidade, incompetência ou impugnação ao valor da causa.
metadata:
  area: processo-civil
  tipo_peca: contestacao
  verificado_em: 2026-11-01
---
# Contestação cível

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: defesa do réu em procedimento comum (inclusive após conversão de procedimento).
- Não usar: juizado especial (use `civel-juizado-especial`), embargos monitórios (`civel-acao-monitoria`), embargos à execução (`civel-embargos-a-execucao`). Pretensão própria do réu vai em `civel-reconvencao`, que pode ser deduzida na mesma peça.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
- Cópia integral da inicial e documentos; data e forma da citação; data da audiência do art. 334 (ou do pedido de cancelamento).
- Versão do cliente sobre cada fato alegado, item por item, e documentos que a sustentam.
- Existência de outra ação idêntica ou conexa, cláusula arbitral, contrato com eleição de foro.
- Se há litisconsortes com advogados diferentes e se os autos são físicos ou eletrônicos.

## Prazo e contagem
- 15 dias úteis (arts. 335 e 219). Termo inicial: audiência sem acordo (I); protocolo do pedido de cancelamento pelo réu (II); ou a data do art. 231 conforme o modo de citação (III).
- Dobra: Fazenda, MP e Defensoria (arts. 183, 180, 186); litisconsortes com escritórios distintos só em autos físicos (art. 229, §2º).
- Calcule com `prazos-processuais`; considere a suspensão de 20/12 a 20/01 (art. 220).

## Estrutura da peça
Endereçamento → qualificação/remissão → síntese da inicial → tempestividade → preliminares (art. 337) → prejudiciais de mérito (prescrição, decadência) → mérito com impugnação ponto a ponto → provas → reconvenção (se houver, em tópico próprio) → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Art. 336: toda a defesa de uma vez (eventualidade). Depois só cabem as matérias do art. 342.
- Art. 337: preliminares antes do mérito. Arbitragem e incompetência relativa não são conhecidas de ofício (§5º). Se omitidas, a consequência vem de regras distintas: sem alegar a convenção de arbitragem, o réu aceita a jurisdição estatal e renuncia ao juízo arbitral (§6º); sem alegar a incompetência relativa em preliminar, a competência se prorroga (art. 65).
- Ilegitimidade: indicar o legitimado, se souber, sob pena de responder por despesas (art. 339).
- Incompetência: a contestação pode ser protocolada no foro do domicílio do réu (art. 340).
- Abusividade da cláusula de foro deve ser alegada na contestação, sob pena de preclusão (art. 63, §4º).

## Fundamentos verificados
CPC arts. 63, 65, 219, 229, 231, 335 a 342, 343, 344, 345, 373. Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Acolhimento das preliminares com extinção sem mérito (art. 485) ou correção do vício.
- Improcedência dos pedidos; condenação do autor em custas e honorários (art. 85).
- Revogação da gratuidade indevida (art. 337, XIII), se for o caso.
- Especificação de provas; intimações em nome do advogado indicado.

## Checklist pré-protocolo
- [ ] Prazo calculado em dias úteis, com termo inicial correto do art. 335.
- [ ] Todas as preliminares cabíveis do art. 337 avaliadas (inclusive XIII, gratuidade).
- [ ] Cada fato da inicial impugnado de forma específica, ou admitido de modo estratégico.
- [ ] Prescrição/decadência examinadas.
- [ ] Indicação do legitimado, se arguida ilegitimidade.
- [ ] Documentos da defesa juntados e referidos.
- [ ] Reconvenção decidida (agora ou nunca nesta via).
- [ ] Procuração e substabelecimento nos autos.

## Erros a evitar
- Negativa geral ("impugna-se tudo"): fatos não impugnados presumem-se verdadeiros (art. 341).
- Deixar a convenção de arbitragem ou a incompetência relativa para depois: a arbitragem fica renunciada (art. 337, §6º) e a competência relativa se prorroga (art. 65).
- Contestar fora do prazo por contar dias corridos ou ignorar o termo do art. 335.
- Alegar ilegitimidade sem apontar quem seria o réu correto.
- Formular pedido contraposto no procedimento comum: o meio é a reconvenção.
- Discutir juros com taxa própria: usar `juros-e-correcao`.

## Integração com o núcleo
- `prazos-processuais` para o termo inicial e a contagem.
- `juros-e-correcao` para impugnar cálculos e encargos.
- `verificacao-de-citacoes` para precedentes acrescentados.
- `fidelidade-factual` para checar a versão do cliente contra os documentos.
- `estilo-forense` na revisão final.

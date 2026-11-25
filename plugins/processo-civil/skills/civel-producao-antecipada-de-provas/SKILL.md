---
name: civel-producao-antecipada-de-provas
description: >
  Redige a ação de produção antecipada de provas (CPC, arts. 381 a 383) — perícia,
  inspeção, testemunha, exibição de documentos —, com ou sem urgência (risco de
  perecimento, viabilizar acordo ou avaliar se vale a pena processar), o
  arrolamento de bens só para documentação e a justificação sem caráter
  contencioso, além da manifestação do requerido. Use quando o usuário pedir
  vistoria ou perícia antes da ação, ouvir testemunha que pode morrer ou
  mudar-se, obter documentos para decidir se processa, medir o risco do litígio
  antes de negociar ou justificar um fato para fazer prova documental.
metadata:
  area: processo-civil
  tipo_peca: inicial
  verificado_em: 2026-11-25
---
# Produção antecipada de provas (CPC, arts. 381 a 383)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar em qualquer das hipóteses do art. 381:
  - **I — urgência:** fundado receio de que a verificação dos fatos fique impossível ou muito difícil na pendência da ação (obra que será demolida, vício que será reparado, testemunha idosa ou doente);
  - **II — autocomposição:** a prova pode viabilizar acordo ou outro meio adequado de solução;
  - **III — avaliar a demanda:** conhecer os fatos antes pode justificar ou evitar o ajuizamento.
- Também: arrolamento de bens só para documentação, sem apreensão (art. 381, § 1º); justificação de fato ou relação jurídica para simples documento, sem caráter contencioso (art. 381, § 5º).
- Não usar:
  - processo já em curso: requerer a prova nos próprios autos;
  - apreensão ou bloqueio de bens: tutela cautelar (`civel-tutela-provisoria`);
  - partes com cláusula compromissória e sem urgência: a via é a arbitragem (STJ, REsp 2.023.615 — ver Fundamentos);
  - quer-se apurar e cobrar saldo de gestão de bens alheios: `civel-acao-de-exigir-contas`;
  - documentos de saúde, plano ou dados pessoais com regime próprio: avaliar `consumidor-plano-de-saude` ou `digital-resposta-a-titular-de-dados`.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Qual fato precisa ser provado, com precisão (não "tudo sobre o contrato").
2. Qual prova: perícia (de quê, por qual especialidade), inspeção, oitiva (quem, por quê), exibição (quais documentos, em poder de quem).
3. Qual hipótese do art. 381 e os fatos que a sustentam (risco concreto; tentativa de acordo; necessidade de avaliar a ação).
4. Quem deve ser citado como interessado e endereço.
5. Pedido extrajudicial prévio de documentos ou vistoria, e a resposta (relevante para honorários).
6. Existe cláusula compromissória ou de eleição de foro?

## Prazo e contagem
- Não há prazo próprio; a urgência da hipótese I recomenda ajuizar logo. A ação **não interrompe** por si a prescrição do direito material [VERIFICAR: efeito sobre a prescrição no caso via `verificacao-de-citacoes`].
- Concluída a produção, os autos ficam em cartório por **1 mês** para cópias e certidões; depois são entregues ao requerente (art. 383).
- Contagem: `prazos-processuais`.

## Estrutura da peça
Endereçamento (foro onde a prova deva ser produzida ou do domicílio do réu) → qualificação do requerente e dos interessados → fatos a provar, um a um → hipótese do art. 381 e razões da necessidade de antecipar (art. 382) → prova pretendida e forma (quesitos, rol, lista de documentos) → liminar, se urgente → pedidos → valor da causa. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- A petição apresenta as **razões que justificam a necessidade de antecipação** e menciona **com precisão os fatos** sobre os quais a prova recairá (art. 382, caput).
- Competência: juízo do foro onde a prova deva ser produzida ou do domicílio do réu (art. 381, § 2º); não previne a competência para a ação principal (§ 3º); justiça estadual pode produzir prova contra ente federal onde não houver vara federal (§ 4º).
- Citação dos interessados, salvo inexistência de caráter contencioso (art. 382, § 1º). O STJ exige citação e contraditório mínimo (REsp 2.190.043).
- O juiz **não se pronuncia** sobre a ocorrência do fato nem sobre suas consequências jurídicas (art. 382, § 2º).
- Os interessados podem requerer outras provas sobre o mesmo fato no mesmo procedimento, salvo demora excessiva (art. 382, § 3º).
- Pela letra do art. 382, § 4º, não se admite defesa nem recurso, salvo contra o indeferimento total; o STJ não aplica essa regra de modo literal e admite contraditório e recurso em situações excepcionais (REsp 2.037.088).

## Fundamentos verificados
- CPC arts. 381 a 383 (conferidos no Planalto).
- STJ: REsp 2.037.088 (contraditório apesar do § 4º); REsp 2.023.615 (sem urgência, juízo estatal não atua antes da arbitragem); REsp 2.190.043 (citação necessária); AgInt no AREsp 2.396.021 (honorários só com resistência).
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Citação dos interessados (ou dispensa justificada, se não contencioso).
- Liminar para produção imediata, se urgente (perito nomeado, vistoria em data próxima), com contraditório diferido justificado.
- Nomeação de perito, quesitos e assistente técnico; ou designação de audiência para oitiva; ou exibição dos documentos listados em prazo fixado.
- Homologação da prova produzida, sem juízo sobre o fato (art. 382, § 2º), e entrega dos autos após 1 mês (art. 383).
- Honorários de sucumbência apenas se houver resistência do requerido; sem resistência, pedir só o ressarcimento de custas conforme a regra local [VERIFICAR: custas e adiantamento de honorários periciais].

## Checklist pré-protocolo
- [ ] Hipótese do art. 381 identificada e demonstrada com fatos
- [ ] Fatos a provar descritos com precisão
- [ ] Prova pretendida especificada (quesitos, rol, lista de documentos)
- [ ] Foro correto (local da prova ou domicílio do réu)
- [ ] Interessados indicados para citação
- [ ] Cláusula compromissória verificada
- [ ] Pedido extrajudicial prévio juntado (se houver)
- [ ] Não há pedido de declaração do direito ou de condenação

## Erros a evitar
- Pedir ao juiz que declare o fato ou suas consequências (art. 382, § 2º veda).
- Petição genérica, sem precisar os fatos a provar.
- Pedir apreensão ou bloqueio de bens na mesma ação (é cautelar).
- Ajuizar no Judiciário, sem urgência, prova sobre contrato com cláusula arbitral.
- Esperar honorários contra requerido que não resistiu.
- Supor que a ação deixou o juízo prevento para a demanda principal (§ 3º).

## Integração com o núcleo
`prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`. Ação principal depois da prova: `civel-peticao-inicial`.

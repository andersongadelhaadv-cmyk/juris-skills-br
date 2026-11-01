---
name: civel-tutela-provisoria
description: >
  Redige pedido de tutela provisória cível (CPC arts. 294 a 311): urgência
  antecipada ou cautelar, em caráter antecedente ou incidental, e tutela da
  evidência. Use quando o usuário pedir liminar, tutela de urgência, tutela
  antecipada, medida cautelar, arresto, sequestro, tutela antecedente,
  "pedido urgente", tutela da evidência ou estabilização da tutela.
metadata:
  area: processo-civil
  tipo_peca: tutela
  verificado_em: 2026-11-01
---
# Tutela provisória (urgência e evidência)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: (a) petição só com pedido de tutela antecipada antecedente (art. 303); (b) tutela cautelar antecedente (art. 305); (c) pedido incidental em processo em curso; (d) tutela da evidência (art. 311).
- Não usar sozinha quando a tutela é parte da inicial completa: a inicial é feita em `civel-peticao-inicial` e esta skill fornece o tópico.
- Efeito suspensivo de recurso tem regras próprias: apelação (art. 1.012, §§3º e 4º), agravo (art. 1.019, I), REsp/RE (art. 1.029, §5º).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
- Fato concreto de urgência (o que acontece, quando, e qual o dano) e prova dele.
- Prova da probabilidade do direito.
- Medida exata pretendida (ordem, destinatário, prazo, multa).
- Se é possível oferecer caução (art. 300, §1º).
- Se o cliente aceita a estabilização (art. 304) ou quer prosseguir com o pedido final.

## Prazo e contagem
- Antecedente antecipada: concedida a tutela, aditar a inicial em 15 dias ou prazo maior fixado (art. 303, §1º, I), sob pena de extinção (§2º). Se o juiz negar, emendar em até 5 dias (§6º).
- Cautelar antecedente: réu contesta em 5 dias (art. 306); efetivada a medida, pedido principal em 30 dias (art. 308); eficácia cessa se não deduzido ou não efetivada em 30 dias (art. 309).
- Estabilização: se o réu não recorrer da decisão concessiva (art. 304); ação para rever em 2 anos (§5º).
- Contagem com `prazos-processuais`.

## Estrutura da peça
Endereçamento → qualificação → indicação de que se vale do art. 303 (§5º) ou do art. 305 → lide e direito → urgência → reversibilidade/caução → medida pedida → pedido final indicado → valor da causa (pelo pedido final, art. 303, §4º) → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Urgência (art. 300): probabilidade do direito + perigo de dano ou risco ao resultado útil; não cabe antecipada se houver perigo de irreversibilidade (§3º).
- Evidência (art. 311): independe de urgência; liminar só nos incisos II e III (p.ú.). Inciso II exige prova só documental + tese em repetitivo ou súmula vinculante.
- Fungibilidade: o juiz pode converter cautelar em antecipada (art. 305, p.ú.).
- Competência: juízo da causa ou do pedido principal; no tribunal, órgão competente para o mérito (art. 299).

## Fundamentos verificados
CPC arts. 294 a 311, 537, 1.012, 1.019, 1.029, §5º; Súmula 735 do STF. Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Concessão liminar, sem oitiva (art. 300, §2º), ou após justificação prévia.
- Medida específica com prazo de cumprimento e multa diária (art. 537), com limite e destinatário claros.
- Dispensa de caução por hipossuficiência, se for o caso (art. 300, §1º).
- Citação e intimação para audiência do art. 334 (art. 303, §1º, II).
- Na antecedente: indicação do pedido de tutela final e do valor da causa.

## Checklist pré-protocolo
- [ ] Urgência descrita com fato, data e prova — não com fórmula genérica.
- [ ] Irreversibilidade enfrentada (ou caução oferecida).
- [ ] Medida redigida para ser cumprida sem interpretação (quem, o quê, prazo, multa).
- [ ] Na antecedente: menção expressa ao benefício do art. 303 (§5º) e valor da causa pelo pedido final.
- [ ] Agenda do aditamento (15 dias) ou do pedido principal (30 dias) registrada.
- [ ] Na evidência: inciso do art. 311 identificado; tese ou súmula vinculante verificada.

## Erros a evitar
- Perder o prazo de aditamento e ter o processo extinto (art. 303, §2º).
- Tratar a estabilização como coisa julgada: não é (art. 304, §6º).
- Pedir liminar de evidência pelo inciso I ou IV: só II e III admitem liminar.
- Multa diária sem prazo razoável para cumprir.
- Esquecer a responsabilidade objetiva pelo dano da efetivação (art. 302) ao aconselhar o cliente.

## Integração com o núcleo
- `prazos-processuais` para aditamento, pedido principal e estabilização.
- `verificacao-de-citacoes` para a tese do art. 311, II, e qualquer julgado.
- `fidelidade-factual` para a prova da urgência.
- `juros-e-correcao` se houver pedido de pagamento antecipado.
- `estilo-forense` na revisão.

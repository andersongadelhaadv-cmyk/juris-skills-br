---
name: adm-defesa-em-improbidade
description: >
  Redige contestação, manifestação e peças de defesa em ação de improbidade
  administrativa (Lei 8.429/1992 com a redação da Lei 14.230/2021): dolo
  específico, tipicidade estrita, prescrição do art. 23 e irretroatividade
  definida no Tema 1199 do STF. Use quando o usuário pedir defesa em improbidade,
  contestação em ação de improbidade, LIA, ato ímprobo, dano ao erário,
  enriquecimento ilícito, violação a princípios, indisponibilidade de bens ou
  acordo de não persecução civil.
metadata:
  area: administrativo-licitacoes
  tipo_peca: contestacao
  verificado_em: 2026-11-01
---
# Defesa em ação de improbidade administrativa

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: contestação (art. 17, § 7º), manifestação sobre tipificação (§ 10-C), especificação de provas (§ 10-E), defesa contra indisponibilidade de bens, análise de acordo de não persecução civil (art. 17-B).
- Para recurso de apelação ou agravo, usar esta skill como base de mérito e a skill recursal correspondente do plugin `processo-civil`.
- Não usar para processo administrativo disciplinar (ver `adm-defesa-em-pad`) nem para sanções a licitante (ver `adm-defesa-em-processo-sancionador-licitacao`).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Inicial integral, documentos e decisão que a recebeu; data da citação/juntada (art. 231 do CPC).
2. Tipo imputado a cada réu (art. 9º, 10 ou 11, com inciso) e a conduta individualizada.
3. Data dos fatos (ou da cessação da permanência), datas de instauração do inquérito civil, do ajuizamento e de decisões condenatórias (prescrição).
4. Função do cliente à época, pareceres jurídicos e técnicos que embasaram o ato, decisões de tribunal de contas.
5. Existência de processo penal ou administrativo sobre os mesmos fatos e seu resultado.
6. Bens bloqueados e impacto na subsistência ou na atividade empresarial.

## Prazo e contagem
- Contestação: 30 dias, iniciado na forma do art. 231 do CPC (art. 17, § 7º), em dias úteis (CPC art. 219) — conferir com `prazos-processuais`.
- Possível interrupção do prazo de contestação por até 90 dias para solução consensual (art. 17, § 10-A).
- Prescrição: 8 anos do fato ou da cessação da permanência (art. 23, caput); suspensão por até 180 dias com o inquérito civil (§ 1º); marcos interruptivos do § 4º; prescrição intercorrente (§ 8º).
- Atenção ao § 5º do art. 23: nas ADIs 7.156 e 7.236 (julgamento concluído em 01/07/2026; decisão publicada no DOU de 05/08/2026), o STF declarou inconstitucional a expressão "pela metade do prazo previsto no caput deste artigo", com prazo máximo de 20 anos de prescrição, e declarou constitucionais os incisos II a V do § 4º. Interrompida a prescrição, o prazo não recomeça mais pela metade (4 anos). Na decisão publicada, a modulação de efeitos aparece só nos votos vencidos. Reflexo sobre a prescrição intercorrente (§ 8º): não conferido em fonte oficial [VERIFICAR].
- Tema 1199 do STF: novo regime prescricional não retroage; os novos marcos valem a partir da publicação da Lei 14.230/2021 (26/10/2021).

## Estrutura da peça (resumo; detalhe em [estrutura](references/estrutura.md))
Tempestividade → preliminares (inépcia por falta de individualização e de indícios de dolo, ilegitimidade, prescrição, litispendência, incompetência de foro) → fatos → mérito (atipicidade, ausência de dolo específico, ausência de dano efetivo, divergência interpretativa, boa-fé com base em parecer) → sanções subsidiárias → provas → pedidos.

## Requisitos e preliminares
- Inicial deve individualizar a conduta e trazer elementos mínimos de autoria e dolo (art. 17, § 6º); senão, rejeição (§ 6º-B).
- Um único tipo por ato (§ 10-D); vedado ao juiz modificar o fato principal e a capitulação (§ 10-C); condenação por tipo diverso é nula (§ 10-F, I).
- Legitimidade ativa: nas ADIs 7.042 e 7.043 (acórdão de 31/08/2022), o STF fixou a legitimidade concorrente e disjuntiva do Ministério Público e da pessoa jurídica interessada (art. 17, caput; art. 17-B, caput).
- Absolvição criminal colegiada pelos mesmos fatos impede o trâmite (art. 21, § 4º). O dispositivo foi julgado pelo STF nas ADIs 7.156/7.236 em sessão de 25/06/2026; o resultado não foi conferido em fonte oficial [VERIFICAR].
- Não há presunção de veracidade por revelia nem inversão do ônus da prova (art. 17, § 19, I e II).

## Fundamentos verificados (resumo; detalhe em [fundamentos](references/fundamentos.md))
Lei 8.429/1992: arts. 1º, §§ 1º a 4º e 8º; 3º; 9º; 10; 11, §§ 1º a 4º; 12; 16; 17; 17-B; 17-C; 21; 23. STF: Tema 1199 (dolo; irretroatividade); Tema 897 (ressarcimento por ato doloso imprescritível). STJ: Súmula 634.

## Pedidos e requerimentos
- Rejeição da inicial ou extinção (prescrição, inépcia, ilegitimidade).
- Improcedência por inexistência de ato doloso tipificado (art. 17, § 11).
- Subsidiariamente: sanção isolada e proporcional (art. 12, caput e § 5º; art. 17-C, IV), limitação à participação e ao benefício de cada réu, sem solidariedade (art. 17-C, § 2º) [VERIFICAR: dispositivo impugnado na ADI 7.156; resultado não conferido em fonte oficial], dedução de ressarcimentos já feitos (art. 12, § 6º) e compensação de sanções de outras esferas (art. 21, § 5º).
- Interrogatório do réu (art. 17, § 18) e provas especificadas (§ 10-E).
- Levantamento ou redução da indisponibilidade: exige perigo concreto e probabilidade, urgência não presumida, limite ao dano indicado, sem incidir sobre multa civil, preservados 40 salários mínimos e bem de família (art. 16, §§ 3º, 4º, 5º, 10, 13 e 14) [VERIFICAR: §§ 3º, 4º e 10 impugnados na ADI 7.156; resultado não conferido em fonte oficial]; substituição por caução ou seguro-garantia (§ 6º).
- Qualquer valor de ressarcimento discutido: atualização pela skill `juros-e-correcao`.

## Checklist pré-protocolo
- [ ] Prazo de 30 dias úteis conferido a partir do art. 231 do CPC.
- [ ] Prescrição calculada pelo regime aplicável à data dos fatos (Tema 1199) e com a decisão das ADIs 7.156/7.236.
- [ ] Cada imputação confrontada com o inciso indicado na inicial.
- [ ] Dolo específico rebatido com fatos (parecer, controle, ausência de proveito).
- [ ] Decisões de tribunal de contas e de outras esferas juntadas (art. 21, §§ 1º a 4º).
- [ ] Provas especificadas e pedido de interrogatório.
- [ ] Nenhum precedente citado sem passar por `verificacao-de-citacoes`.

## Erros a evitar
- Defender "ausência de culpa grave": após a Lei 14.230/2021 só há improbidade dolosa (art. 1º, § 1º; art. 10, caput).
- Pedir aplicação retroativa da prescrição nova a fatos com prazo correndo antes de 26/10/2021 (Tema 1199, item 4).
- Sustentar que a revogação da modalidade culposa desconstitui condenação transitada em julgado (Tema 1199, item 2).
- Usar o prazo de 4 anos do § 5º do art. 23 sem considerar as ADIs 7.156/7.236.
- Esquecer que o ressarcimento por ato doloso é imprescritível (Tema 897): a prescrição das sanções não extingue esse pedido.

## Integração com o núcleo
- `prazos-processuais`: contestação e prescrição.
- `juros-e-correcao`: valores de ressarcimento e multa civil.
- `verificacao-de-citacoes`: todo julgado acrescentado.
- `fidelidade-factual`: cronologia e documentos.
- `estilo-forense`: revisão final.

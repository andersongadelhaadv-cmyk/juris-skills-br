---
name: penal-anpp
description: >
  Prepara requerimento de acordo de não persecução penal, pedido de remessa ao
  órgão superior do Ministério Público após recusa e impugnação de condições
  (CPP art. 28-A, Lei 13.964/2019), incluindo a aplicação a processos em curso.
  Use quando o usuário pedir ANPP, acordo de não persecução, proposta de acordo
  ao MP, recusa de ANPP, remessa ao procurador-geral, revisão ministerial,
  retroatividade do ANPP ou rescisão do acordo.
metadata:
  area: penal
  tipo_peca: requerimento
  verificado_em: 2026-11-01
---
# Acordo de não persecução penal (ANPP)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: investigação ou processo por infração sem violência ou grave ameaça, pena mínima inferior a 4 anos, não sendo caso de arquivamento (CPP 28-A caput).
- Usar também: recusa do MP (pedido de remessa ao órgão superior — 28-A §14); recusa de homologação pelo juiz (RESE — CPP 581, XXV; ver `penal-recurso-em-sentido-estrito`); defesa em rescisão (28-A §10).
- Não usar: cabível transação penal (28-A §2º, I); reincidente ou conduta criminal habitual, reiterada ou profissional (salvo infrações pretéritas insignificantes — §2º, II); beneficiado nos 5 anos anteriores por ANPP, transação ou suspensão do processo (§2º, III); violência doméstica ou familiar, ou crime contra a mulher por razões da condição do sexo feminino (§2º, IV).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Fato, capitulação e pena mínima, com causas de aumento e de diminuição aplicáveis (28-A §1º).
2. Fase: inquérito, denúncia oferecida, recebida, sentença, recurso; data do trânsito, se houver.
3. Antecedentes e benefícios anteriores (5 anos).
4. Disposição do cliente para confessar formal e circunstanciadamente — explicar riscos.
5. Capacidade de reparar o dano e de cumprir condições (renda, trabalho).

## Prazo e contagem
- Não há prazo legal fixo para o pedido, mas o momento importa: na fase de investigação, antes da denúncia; em processos em curso, na primeira oportunidade (ver Fundamentos).
- Recusa do MP: pedido de remessa ao órgão superior "na forma do art. 28" (28-A §14) — confira prazo regimental do MP local.
- RESE contra recusa de homologação: 5 dias (CPP 586), contínuos (CPP 798). Use `prazos-processuais`.

## Estrutura da peça
Resumo (detalhe em [estrutura](references/estrutura.md)): requerimento ao MP (ou ao juízo, para remessa); preenchimento dos requisitos; ausência das vedações; proposta de condições; pedidos.

## Requisitos e preliminares
- Confissão formal e circunstanciada, feita perante o MP com defensor; não é exigida antes da proposta.
- Condições (cumulativas e alternativas): reparar o dano; renunciar a bens instrumento ou produto; prestação de serviços pelo período da pena mínima reduzida de 1/3 a 2/3; prestação pecuniária; outra condição proporcional (28-A, I a V).
- Homologação em audiência com oitiva do investigado e defensor (§4º); juiz pode devolver para reformular (§5º) ou recusar (§7º).
- Cumprido o acordo, extinção da punibilidade (§13); não consta de certidão de antecedentes, salvo para a vedação dos 5 anos (§12).
- O juiz das garantias homologa ANPP celebrado na investigação (CPP 3-B, XVII), onde implantado [VERIFICAR: estado da implantação e da decisão do STF nas ADIs 6.298 e outras, ver `penal-liberdade-provisoria-e-relaxamento`].

## Fundamentos verificados
Resumo (detalhe em [fundamentos](references/fundamentos.md)): CPP 28, 28-A, 581 XXV; CF 5º XL; Lei 9.099/1995 (transação e suspensão); STJ sobre aplicação do ANPP a processos em curso.

## Pedidos e requerimentos
- Ao MP: designação de audiência para proposta e formalização do acordo.
- Após recusa: remessa ao órgão superior (28-A §14) com crítica aos fundamentos da recusa.
- Ao juízo (processo em curso): suspensão do feito e vista ao MP para manifestação motivada sobre o ANPP.
- Em homologação: adequação de condições abusivas (§5º).
- Em rescisão: oitiva prévia, justificativa do descumprimento, repactuação.

## Checklist pré-protocolo
- [ ] Pena mínima calculada com causas de aumento (mínimo) e diminuição (máximo) — §1º.
- [ ] Ausência de violência ou grave ameaça na conduta descrita.
- [ ] Vedações do §2º checadas uma a uma, com certidões.
- [ ] Cliente orientado sobre a confissão e suas consequências.
- [ ] Proposta de condições compatível com a renda.
- [ ] Em processo em curso: pedido feito na primeira oportunidade e antes do trânsito.
- [ ] Precedentes conferidos em `verificacao-de-citacoes`.

## Erros a evitar
- Tratar o ANPP como direito subjetivo absoluto: o STJ entende que não é, mas a recusa deve ser motivada e sujeita a controle.
- Deixar passar a primeira oportunidade em processo antigo e ver o pedido declarado precluso.
- Ignorar a vedação de violência doméstica e de crime contra a mulher por razões de gênero (§2º, IV).
- Fazer confissão escrita na petição: a confissão é ato formal perante o MP, no acordo.
- Aceitar condições desproporcionais sem pedir ao juiz a devolução para reformular (§5º).

## Integração com o núcleo
- `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.
- `juros-e-correcao`: para atualizar o valor de reparação do dano, aplicar o núcleo; nunca fixar taxa na peça.

---
name: amb-indenizacao-dano-ambiental-individual
description: >
  Redige ação indenizatória de vítima individual de dano ambiental (dano
  reflexo ou por ricochete) e ação de vizinhança contra interferência poluidora,
  com base na Lei 6.938/1981, art. 14, § 1º (reparação a terceiros sem culpa),
  e nos arts. 1.277 a 1.279 do Código Civil. Use quando o usuário pedir
  indenização por contaminação de poço ou lavoura, mortandade de peixes que
  tirou a renda do pescador, fumaça, poeira, odor ou ruído de empresa vizinha,
  rompimento de barragem, vazamento de óleo ou desvalorização do imóvel por
  poluição.
metadata:
  area: ambiental
  tipo_peca: inicial
  verificado_em: 2026-11-25
---
# Indenização por dano ambiental individual e vizinhança

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: pessoa física ou jurídica identificada que sofreu prejuízo próprio (patrimonial, lucros cessantes, moral, saúde) em razão de degradação ambiental; ou vizinho que quer fazer cessar e/ou ser indenizado por interferência prejudicial.
- Não usar:
  - reparação do bem ambiental difuso: `amb-acao-civil-publica`;
  - defesa do poluidor: `amb-defesa-acao-civil-publica` (lógica de defesa) ou `civel-contestacao`;
  - execução individual de TAC coletivo já firmado: ver `amb-termo-ajustamento-conduta`;
  - barulho/obra sem componente ambiental: `civel-peticao-inicial` (direito de vizinhança comum).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Evento: o que aconteceu, onde, quando (data exata — decisiva para a prescrição).
2. Atividade e identificação do causador (CNPJ, licença, atividade potencialmente poluidora).
3. Prejuízo próprio do autor e prova dele: notas, produção histórica, laudo de água/solo, atestado médico, registro de pescador, avaliação do imóvel.
4. Nexo: distância, direção do vento/fluxo, laudos técnicos, autos de infração lavrados contra o réu.
5. Existe ACP, TAC ou acordo coletivo sobre o mesmo evento? Autor já aderiu ou recebeu algo?
6. Interferência continua? (define pedido de cessação, além da indenização)

## Prazo e contagem
- Prescrição da pretensão individual: não presuma a imprescritibilidade do Tema 999/STF, que trata da reparação civil do dano ambiental; sua extensão ao dano individual reflexo não foi conferida em fonte oficial [VERIFICAR via `verificacao-de-citacoes`].
- Desastre ambiental por atividade empresarial: o STJ reconheceu acidente de consumo, vítimas como consumidoras por equiparação (CDC, art. 17) e prazo de 5 anos do art. 27 do CDC; a tese fixada no Tema 1.280 é restrita ao desastre de Brumadinho, e o mesmo acórdão afirma a interrupção da prescrição individual por ACPs sobre o mesmo evento. Fora desse caso, use como argumento, não como tese vinculante.
- Prazos processuais: `prazos-processuais`.

## Estrutura da peça
Fatos e evento → legitimidade e prejuízo próprio → responsabilidade objetiva (art. 14, § 1º) e risco integral → nexo causal e prova → danos (emergentes, lucros cessantes, moral, desvalorização) → cessação da interferência → tutela → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Polo passivo: operador da atividade, controladora/beneficiária quando houver base, e demais poluidores indiretos (Lei 6.938, art. 3º, IV).
- Ônus: a inversão é cabível, mas a parte autora precisa trazer prova mínima do dano e da sua condição (ex.: de pescador) — AgInt no AREsp 2.816.896.
- Interesse: verificar adesão a acordo coletivo e quitação já dada.
- Repetitivo pendente: dano moral por mau cheiro de estação de esgoto está afetado ao Tema 1.400/STJ com suspensão dos recursos sobre a matéria — conferir o andamento antes de ajuizar caso análogo.

## Fundamentos verificados
- Lei 6.938/1981, art. 14, § 1º — reparação dos danos "a terceiros, afetados por sua atividade", sem culpa; art. 3º, IV.
- Código Civil, art. 927, parágrafo único; arts. 1.277 a 1.279 (vizinhança).
- Risco integral e irrelevância da licitude e das medidas mitigadoras: REsp 2.102.646 (STJ, 4ª T., 2026).
- Tema 1.280/STJ (consumidor por equiparação, 5 anos, interrupção por ACP) — Brumadinho.
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Cessação ou redução da interferência (CC, arts. 1.277 e 1.279), com multa diária.
- Danos emergentes (perda de lavoura, animais, tratamento de água, despesas médicas).
- Lucros cessantes (renda que deixou de ter), com prova documental ou apuração em liquidação.
- Dano moral individual.
- Desvalorização do imóvel, se houver laudo.
- Inversão do ônus (Súmula 618/STJ) e perícia técnica.
- Juros e correção: núcleo `juros-e-correcao`.

## Checklist pré-protocolo
- [ ] Data do evento e da ciência registradas; prescrição enfrentada expressamente
- [ ] Prejuízo próprio individualizado e documentado
- [ ] Prova mínima do nexo (laudo, auto de infração, proximidade)
- [ ] Verificada ACP/TAC/acordo coletivo sobre o evento (interrupção, adesão, quitação)
- [ ] Verificado Tema 1.400/STJ se o caso for de odor de ETE
- [ ] Pedido de cessação quando a interferência continua
- [ ] Juros/correção remetidos ao núcleo

## Erros a evitar
- Afirmar que o dano individual é imprescritível com base no Tema 999 sem ressalva.
- Pedir inversão do ônus e não juntar nenhuma prova do próprio dano.
- Generalizar a tese do Tema 1.280 para qualquer acidente ambiental como se fosse vinculante.
- Esquecer de checar se o autor já assinou termo de quitação em programa de indenização.
- Na vizinhança, ignorar o critério de tolerabilidade do art. 1.277, parágrafo único (zona, natureza do uso, limites ordinários).

## Integração com o núcleo
`juros-e-correcao`, `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`; consumidor por equiparação: `consumidor-acao-indenizatoria`.

---
name: consumidor-acao-coletiva
description: >
  Redige ação coletiva de consumo (ação civil pública consumerista) para tutela
  de direitos difusos, coletivos e individuais homogêneos, com base nos arts. 81
  a 104 do CDC e na Lei 7.347/1985: legitimidade (art. 82), competência (art. 93
  e STF, Tema 1075), sentença genérica, liquidação e coisa julgada (arts. 95 a
  103). Use quando o usuário pedir ação civil pública de consumidor, ação
  coletiva por associação, MP ou Defensoria, dano moral coletivo, tutela de
  grupo de consumidores lesados, liquidação ou execução de sentença coletiva.
metadata:
  area: consumidor
  tipo_peca: inicial
  verificado_em: 2026-11-25
---
# Ação coletiva de consumo (CDC, arts. 81 a 104)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: lesão que atinge grupo de consumidores com origem comum (cobrança em massa, cláusula abusiva em contrato de adesão, prática abusiva reiterada, publicidade enganosa difundida, produto perigoso no mercado), proposta por legitimado do art. 82 do CDC.
- Usar também para a fase de liquidação e execução da sentença coletiva (arts. 97 a 100).
- Não usar: ação individual do consumidor (`consumidor-acao-indenizatoria`, `consumidor-vicio-do-produto-ou-servico`); o consumidor individual só aproveita a coletiva (art. 103, III) ou pede suspensão da sua (art. 104).
- Publicidade como objeto único: ver também `consumidor-publicidade-enganosa` (pedidos de contrapropaganda e cessação).
- Ação popular ou improbidade: `adm-acao-popular`, `adm-defesa-em-improbidade`.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Quem é o autor: MP, Defensoria, ente público, órgão de defesa do consumidor ou associação (estatuto, ata de constituição, data de registro, finalidade institucional).
2. Conduta do fornecedor, período, abrangência geográfica (local, regional, nacional) e estimativa de atingidos.
3. Natureza do direito: difuso, coletivo em sentido estrito ou individual homogêneo (pode haver mais de um).
4. Provas: reclamações (Procon, plataformas públicas), contratos-padrão, peças publicitárias, inquérito civil, perícia, notas técnicas.
5. Há outras ações coletivas sobre o mesmo fato (prevenção) ou ações individuais em curso?
6. Há TAC anterior (art. 5º, § 6º, da Lei 7.347/1985) descumprido?

## Prazo e contagem
- Não há prazo específico no CDC para a ação coletiva; a prescrição da pretensão coletiva não foi conferida em fonte oficial nesta skill [VERIFICAR: prazo prescricional da ACP consumerista via `verificacao-de-citacoes`].
- Liquidação residual pelos legitimados: após 1 ano sem habilitação compatível com a gravidade do dano (art. 100).
- Suspensão da ação individual: 30 dias da ciência da coletiva (art. 104).
- Prazos processuais em dias úteis: `prazos-processuais`.

## Estrutura da peça
Endereçamento (art. 93) → legitimidade e pertinência temática → classificação do direito (art. 81) → fatos e prova da origem comum → fundamentos materiais → tutela de urgência (art. 84, § 3º) → pedidos (fazer/não fazer, indenização genérica, dano moral coletivo) → edital do art. 94 → requerimentos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Legitimidade concorrente (art. 82; Lei 7.347/1985, art. 5º). Associação: 1 ano de constituição e finalidade de defesa do consumidor, sem autorização assemblear (art. 82, IV); o juiz pode dispensar o ano (art. 82, § 1º), como admitido no AREsp 2.949.915 (STJ).
- Pertinência temática: estatuto com finalidades amplas demais descaracteriza a representatividade (REsp 2.035.372, STJ).
- MP tem legitimidade para individuais homogêneos de consumidores, inclusive em serviço público (Súmula 601/STJ).
- Competência: local do dano; dano regional ou nacional, capital do Estado ou DF (art. 93); efeitos nacionais seguem o art. 93, II, com prevenção do primeiro juízo (STF, Tema 1075).
- MP atua como fiscal da lei quando não for parte (Lei 7.347/1985, art. 5º, § 1º).

## Fundamentos verificados
- CDC arts. 6º, VIII; 81; 82; 83; 84; 87; 90; 91; 93; 94; 95; 97; 98; 100; 103; 104.
- Lei 7.347/1985 arts. 1º, 2º, 5º, 11, 12, 13, 18, 21.
- STF, Tema 1075 (RE 1.101.937): inconstitucional a limitação territorial do art. 16 da Lei 7.347/1985.
- STJ: Súmula 601; AREsp 2.949.915; REsp 2.035.372; AgInt no AREsp 2.800.035 (inversão do ônus em favor do MP na coletiva); REsp 2.223.012 (dano moral coletivo e flexibilização temporal da associação).
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Tutela de urgência para cessar a prática, com multa diária (art. 84, §§ 3º e 4º; Lei 7.347/1985, art. 12).
- Obrigação de fazer/não fazer e medidas de apoio (art. 84, § 5º).
- Condenação genérica pelos danos individuais (arts. 91 e 95), com liquidação individual ou coletiva.
- Dano moral coletivo, revertido ao fundo (Lei 7.347/1985, art. 13; CDC art. 100, p.u.).
- Publicação do edital do art. 94 e divulgação pelos órgãos de defesa do consumidor.
- Inversão do ônus da prova (art. 6º, VIII) e dispensa de adiantamento de custas (art. 87).
- Juros e correção: remeter ao núcleo `juros-e-correcao`.

## Checklist pré-protocolo
- [ ] Legitimidade comprovada (estatuto, ata, registro, pertinência temática)
- [ ] Direito classificado (art. 81) e pedidos coerentes com cada classe
- [ ] Competência pelo art. 93 e pesquisa de prevenção (Tema 1075)
- [ ] Prova da origem comum e da extensão do dano
- [ ] Pedido de edital (art. 94) incluído
- [ ] Pedido de tutela com multa e prazo
- [ ] Prescrição enfrentada ou marcada [VERIFICAR]
- [ ] Juros/correção remetidos ao núcleo

## Erros a evitar
- Misturar direito individual heterogêneo (que exige prova caso a caso) com individual homogêneo.
- Pedir condenação líquida a cada consumidor: a sentença é genérica (art. 95).
- Ignorar ações individuais já ajuizadas e o ônus de pedir suspensão (art. 104).
- Invocar a limitação territorial do art. 16 da Lei 7.347/1985 (afastada pelo Tema 1075).
- Associação com estatuto genérico sem enfrentar a pertinência temática.

## Integração com o núcleo
`juros-e-correcao`, `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

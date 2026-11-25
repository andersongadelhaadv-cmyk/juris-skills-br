---
name: familia-emancipacao
description: >
  Orienta e redige a emancipação de menor com 16 anos completos — voluntária, por
  escritura pública dos pais, ou judicial, por sentença em jurisdição voluntária (CC
  art. 5º, parágrafo único, I; CPC art. 725, I) — e o registro no Livro E (Lei 6.015/1973,
  arts. 89 a 91). Use quando o usuário pedir emancipação, emancipar filho, emancipação
  de menor sob tutela, suprimento do consentimento de um dos pais para emancipar,
  escritura de emancipação ou pedido judicial de emancipação.
metadata:
  area: familia-sucessoes
  tipo_peca: requerimento
  verificado_em: 2026-11-25
---
# Emancipação

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: (a) minuta/orientação de escritura pública de emancipação concedida pelos pais (ou por um deles, na falta do outro); (b) pedido judicial de emancipação do menor sob tutela (sentença, ouvido o tutor); (c) pedido de suprimento judicial quando os pais divergem (CC arts. 1.631, parágrafo único, e 1.690, parágrafo único); (d) declaração de que a emancipação legal já ocorreu (casamento, emprego público efetivo, colação de grau, economia própria).
- Não usar: autorização para casamento de quem tem 16 anos (CC arts. 1.517 a 1.519 — pedido próprio de suprimento de consentimento); nomeação ou remoção de tutor (`familia-tutela-de-menor`); alienação de bens do menor (alvará; CPC art. 725, III).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Data de nascimento e certidão do menor (16 anos **completos** na data do ato).
2. Situação familiar: ambos os pais vivos e no exercício do poder familiar? algum falecido, ausente, destituído? há tutor?
3. Os pais estão de acordo? Se não, quem diverge e por quê.
4. Finalidade da emancipação (negócio, trabalho, estudo, mudança) e se há bens do menor.
5. Hipótese legal já ocorrida, se for o caso (certidão de casamento, posse em cargo efetivo, diploma, contrato de trabalho/estabelecimento com prova de economia própria).
6. Existe ação de alimentos, pensão ou benefício em favor do menor? (avaliar impacto com `familia-revisional-e-exoneracao-de-alimentos`).

## Prazo e contagem
- Requisito etário: 16 anos completos para a concessão voluntária ou judicial (CC art. 5º, parágrafo único, I).
- Jurisdição voluntária: citação dos interessados e intimação do MP para manifestação em 15 dias; decisão em 10 dias (CPC arts. 721 e 723).
- Registro: se o juiz conceder e o registro não for feito em 8 dias, comunica de ofício ao oficial; **antes do registro a emancipação não produz efeito** (Lei 6.015/1973, art. 91).
- Prazos concretos e recursos: `prazos-processuais`.

## Estrutura da peça
Voluntária: escritura pública no tabelionato + registro no Livro E. Judicial: endereçamento → qualificação → menor e situação familiar → hipótese legal → maturidade e conveniência → oitiva do tutor/MP → pedidos (sentença + mandado de registro). Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Voluntária:** instrumento público, dispensada homologação judicial; concessão dos pais, ou de um deles na falta do outro (CC art. 5º, parágrafo único, I). "Falta" é ausência, morte ou impedimento — divergência não é falta: vai ao juiz (CC art. 1.631, parágrafo único).
- **Judicial:** menor sob tutela — sentença, ouvido o tutor (CC art. 5º, parágrafo único, I). Rito de jurisdição voluntária (CPC arts. 719 a 725). MP intervém por interesse de incapaz (CPC art. 178, II).
- Competência: Justiça da Infância e Juventude quando faltarem os pais (ECA art. 148, parágrafo único, "e"); demais casos, vara de família ou cível conforme a lei local.
- Registro obrigatório no cartório do 1º Ofício (ou 1ª subdivisão) da comarca do domicílio do menor, em livro especial (Lei 6.015/1973, arts. 89 e 90; CC art. 9º, II).

## Fundamentos verificados
- CC art. 5º e parágrafo único, I a V; art. 9º, II; arts. 1.631, 1.635, II, 1.690; art. 932, I.
- CPC arts. 178, II, 719 a 725 (art. 725, I: emancipação).
- Lei 6.015/1973, arts. 89 a 91. ECA art. 148, parágrafo único, "e".
- STJ, AgInt no REsp 2.102.443: a emancipação voluntária, diferentemente da legal, **não exclui a responsabilidade civil dos pais** pelos atos do filho menor.
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Citação dos interessados (o outro genitor, quando for suprimento) e intimação do MP (CPC art. 721).
- Oitiva do tutor (menor sob tutela).
- Sentença que conceda a emancipação ou supra o consentimento do genitor divergente.
- Expedição de mandado/certidão para registro no Livro E (Lei 6.015/1973, arts. 89 a 91).
- Se houver bens sob administração do tutor: prestação de contas final (`familia-tutela-de-menor`).

## Checklist pré-protocolo
- [ ] 16 anos completos comprovados por certidão atualizada
- [ ] Hipótese correta: voluntária (pais) x judicial (tutela ou divergência) x legal (incisos II a V)
- [ ] Concordância de ambos os pais documentada, ou justificada a "falta" de um deles
- [ ] Cliente informado de que emancipação voluntária não afasta a responsabilidade civil dos pais
- [ ] Impacto em alimentos/benefícios avaliado e comunicado
- [ ] Registro no Livro E providenciado (sem ele, não há efeito)

## Erros a evitar
- Lavrar escritura com assinatura de um só genitor quando o outro está vivo, presente e discorda.
- Entregar a escritura ao cliente sem levar ao registro (Lei 6.015/1973, art. 91, parágrafo único).
- Vender a emancipação como meio de afastar a responsabilidade dos pais por danos do filho.
- Pedir emancipação judicial quando os pais concordam (basta a escritura; falta interesse).
- Confundir emancipação com autorização para casar (regimes e artigos distintos).

## Integração com o núcleo
`prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

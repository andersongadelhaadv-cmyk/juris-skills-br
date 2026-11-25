---
name: eleitoral-recurso-eleitoral
description: >
  Redige recursos na Justiça Eleitoral pelo Código Eleitoral (Lei 4.737/1965)
  e pela CF, art. 121: recurso ao TRE contra decisão de juiz eleitoral,
  recurso ordinário e especial ao TSE, embargos de declaração e recurso
  contra expedição de diploma (RCED), com os prazos curtos e os efeitos de
  cada um. Use quando o usuário pedir recurso eleitoral, recurso contra
  sentença de registro, AIJE, AIME, representação ou contas, recurso
  especial eleitoral, embargos no TRE/TSE, RCED ou efeito suspensivo
  contra cassação.
metadata:
  area: eleitoral
  tipo_peca: recurso
  verificado_em: 2026-11-25
---
# Recurso eleitoral

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: (a) recurso ao TRE contra ato ou decisão de juiz ou junta eleitoral (CE, art. 265); (b) recurso especial ou ordinário ao TSE (CE, art. 276; CF, art. 121, § 4º); (c) embargos de declaração (CE, art. 275); (d) RCED (CE, art. 262); (e) recurso ao STF contra decisão do TSE nas hipóteses do CE, art. 281, e da CF, art. 121, § 3º.
- Não usar: recurso em processo penal eleitoral — `penal-*` (apelação/RESE com regras próprias); mandado de segurança contra ato eleitoral — avaliar `adm-mandado-de-seguranca` com adaptação; peças de primeiro grau — `eleitoral-impugnacao-registro-candidatura`, `eleitoral-aije`, `eleitoral-aime`, `eleitoral-representacao-propaganda-irregular`, `eleitoral-prestacao-de-contas-campanha`.

## Entradas mínimas (perguntar o que faltar; nunca supor fatos)
1. Decisão recorrida integral, órgão prolator e data e forma de publicação (Diário, sessão, mural).
2. Tipo de ação de origem (define o prazo especial: 24 horas, 3 dias).
3. Pontos de inconformismo e se foram prequestionados (para o especial).
4. Se a decisão cassa registro, afasta titular ou causa perda de mandato (efeito suspensivo — CE, art. 257, § 2º).
5. Eleição federal/estadual ou municipal (cabimento do ordinário ao TSE — CF, art. 121, § 4º, III e IV).

## Prazo e contagem
- Regra geral: 3 dias da publicação (CE, art. 258); preclusivos, salvo matéria constitucional (art. 259).
- Prazos especiais: representação do art. 96 — 24 horas (Lei 9.504/1997, art. 96, § 8º); registro — 3 dias (LC 64/1990, arts. 8º e 11); contas — 3 dias (Lei 9.504/1997, art. 30, § 5º); arts. 30-A e 41-A — 3 dias (art. 30-A, § 3º; art. 41-A, § 4º).
- Ao TSE: 3 dias (CE, art. 276, § 1º). Embargos: 3 dias, interrompem o prazo (CE, art. 275, §§ 1º e 5º). Ao STF: 3 dias (CE, art. 281).
- RCED: 3 dias após o último dia fixado para a diplomação, suspenso de 20 de dezembro a 20 de janeiro (CE, art. 262, § 3º).
- Contagem em dias corridos ou úteis e funcionamento em período eleitoral: `prazos-processuais` e resolução do TSE [VERIFICAR: regra de contagem na resolução do pleito].

## Estrutura da peça
Interposição (juízo a quo) → razões (tempestividade, cabimento, legitimidade e interesse) → síntese → preliminares (nulidades) → mérito → efeito suspensivo, se cabível → pedidos. Especial: hipótese do art. 276, I, ou do art. 121, § 4º, I/II, com prequestionamento. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Efeito: em regra, não suspensivo (CE, art. 257); suspensivo no recurso ordinário contra decisão que cassa registro, afasta titular ou leva à perda de mandato (§ 2º), com preferência de julgamento (§ 3º).
- Cabimento do especial: contrariedade a disposição expressa de lei ou divergência entre tribunais eleitorais (CE, art. 276, I; CF, art. 121, § 4º, I e II).
- Cabimento do ordinário: inelegibilidade ou diploma nas eleições federais e estaduais, anulação de diplomas ou perda de mandato federal ou estadual, denegação de HC, MS, HD ou MI (CF, art. 121, § 4º, III a V; CE, art. 276, II).
- Reexame de fatos e provas no especial: [VERIFICAR: Súmula 24 do TSE — JuriBase sem cobertura do TSE]. Construa o especial sobre a moldura fática do acórdão.
- RCED só para inelegibilidade superveniente, constitucional ou falta de condição de elegibilidade (CE, art. 262); a superveniente deve surgir até a data do registro e não pode ter sido arguida no registro (§§ 1º e 2º).
- Embargos: hipóteses do CPC; sem preparo; protelatórios geram multa de até 2 e, reiterados, até 10 salários mínimos (CE, art. 275, §§ 2º, 6º e 7º).

## Fundamentos verificados
- CE: arts. 257, 258, 259, 262, 263, 264, 265, 275, 276, 280, 281.
- CF: art. 121, §§ 3º e 4º.
- LC 64/1990: arts. 8º, 11, 15 (efeito da decisão colegiada sobre registro e diploma).
- Lei 9.504/1997: arts. 30, § 5º; 30-A, § 3º; 41-A, § 4º; 96, §§ 8º a 10.
- STF, Tema 986 (novas eleições após cassação na majoritária).
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Recebimento e processamento; efeito suspensivo quando cabível (CE, art. 257, § 2º) ou pedido cautelar fundamentado nos demais casos.
- Provimento para reformar ou anular a decisão, com indicação precisa do resultado pretendido.
- No especial: conhecimento pela hipótese indicada e provimento; prequestionamento expresso.
- Intimação da parte contrária para contrarrazões no mesmo prazo.

## Checklist pré-protocolo
- [ ] Prazo especial identificado pela ação de origem (24h ou 3 dias)
- [ ] Data e forma da publicação comprovadas
- [ ] Recurso correto (ao TRE, ordinário, especial, embargos, RCED)
- [ ] Efeito suspensivo pedido ou justificado
- [ ] Prequestionamento conferido (especial)
- [ ] Nenhum pedido de reexame de prova no especial
- [ ] Interposição dirigida ao juízo a quo com razões ao ad quem

## Erros a evitar
- Usar 15 dias do CPC: o padrão eleitoral é 3 dias e, na propaganda, 24 horas.
- Contar o prazo da intimação pessoal quando a regra é a publicação ou a sessão.
- Interpor especial pedindo revaloração de prova sem moldura fática no acórdão.
- Usar RCED para abuso de poder (via é AIJE ou AIME).
- Embargos repetitivos: multa (art. 275, §§ 6º e 7º).

## Integração com o núcleo
`prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

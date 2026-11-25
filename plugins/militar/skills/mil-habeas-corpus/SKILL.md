---
name: mil-habeas-corpus
description: >
  Redige habeas corpus na Justiça Militar (CF art. 5º, LXVIII; CPPM arts. 466 a
  470), com escolha do juízo pela autoridade coatora (juiz federal da JM, STM,
  juízo militar estadual, TJ/TJM, STJ ou STF), hipóteses do art. 467 do CPPM,
  liminar e os limites do art. 142, § 2º, da CF para punição disciplinar. Use
  quando o usuário pedir HC para militar ou civil preso por crime militar,
  detenção no IPM, excesso de prazo na instrução militar, trancamento de ação
  penal militar ou HC contra prisão disciplinar por vício de legalidade.
metadata:
  area: militar
  tipo_peca: inicial
  verificado_em: 2026-11-25
---
# Habeas corpus na Justiça Militar

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: prisão em flagrante, preventiva ou detenção do art. 18 do CPPM ilegal; excesso de prazo; processo por fato que não é crime militar; punibilidade extinta; nulidade evidente; incompetência; prisão disciplinar com vício de legalidade (competência, forma, previsão legal).
- Não usar: discutir o mérito da punição disciplinar (CF art. 142, § 2º; CPPM art. 466, parágrafo único) — use `mil-recurso-disciplinar` ou `mil-mandado-de-seguranca`; exclusão, perda de patente ou de função (Súmula 694/STF) — `mil-reintegracao-e-reforma`; pena privativa já extinta (Súmula 695/STF); crime comum (`penal-habeas-corpus`).
- Pedido de liberdade ainda não feito ao juiz natural: comece por `mil-liberdade-provisoria` para evitar supressão de instância.

## Entradas mínimas (perguntar o que faltar; nunca supor fatos)
1. Ato coator integral, data e autoridade (comandante, encarregado do IPM, juiz federal da JM, Conselho de Justiça, juiz de direito do juízo militar, tribunal).
2. Onde e desde quando o paciente está preso; se é militar da ativa, inativo ou civil; posto ou graduação (oficial-general muda a competência).
3. Cópia do auto de prisão, do decreto de prisão, da denúncia e do andamento (prova pré-constituída).
4. Pedidos anteriores sobre o mesmo tema e onde tramitam.
5. Se punição disciplinar: regulamento aplicado, portaria, publicação em boletim, autoridade, defesa oferecida.

## Prazo e contagem
- Sem prazo: cabe enquanto durar a coação ou a ameaça.
- Marcos para excesso de prazo: detenção no IPM até 30 dias, prorrogáveis por mais 20 (CPPM art. 18); denúncia em 5 dias com indiciado preso (art. 79); instrução em 50 dias com acusado preso (art. 390).
- Recurso contra a denegação: RHC ao STJ quando denegado por TJ ou TJM (CF art. 105, II, a); recurso ordinário ao STF quando denegado em única instância pelo STM (CF art. 102, II, a). Prazos: `prazos-processuais`.

## Estrutura da peça
Endereçamento pela autoridade coatora → partes → cabimento (e por que não incide o art. 142, § 2º) → fatos → constrangimento ilegal por alínea do art. 467 do CPPM → liminar → pedidos. Roteiro em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Competência na JMU (Lei 8.457/1992): juiz federal da JM julga HC contra autoridade militar por fato ligado a crime militar, salvo oficial-general (art. 30, I-C); o STM julga HC contra juiz federal da JM, Conselho de Justiça e oficial-general (art. 6º, I, c).
- JME: juízo militar estadual e, acima dele, TJ ou TJM (CF art. 125, §§ 3º a 5º). Conferir a organização judiciária local.
- Comandante da Marinha, do Exército ou da Aeronáutica como coator: STJ (CF art. 105, I, c). Tribunal Superior como coator: STF (CF art. 102, I, i).
- Punição disciplinar: a vedação do art. 142, § 2º (estendida aos militares estaduais pelo art. 42, § 1º) atinge o mérito; o exame de legalidade formal é admitido por tribunais (TRF5, RSE 0011096-40.2015.4.05.8300). Posição atual do STF não conferida [VERIFICAR]. Juízo competente para HC disciplinar: conferir caso a caso [VERIFICAR].
- Sem risco à locomoção não cabe HC (STJ, AgInt no HC 750.533): para trancar processo disciplinar, use mandado de segurança.
- Após condenação, o HC ainda cabe nas hipóteses do art. 468 do CPPM.

## Fundamentos verificados
- CF arts. 5º, LXV e LXVIII, 42, § 1º, 102, I, i e II, a, 105, I, c e II, a, 125 e 142, § 2º; CPPM arts. 18, 79, 390, 466 a 470; Lei 8.457/1992, arts. 6º, I, c, e 30, I-C.
- Súmulas 694 e 695 do STF.
- STJ, AgInt no RHC 157.152 (Súmula 695 em punição de PM); TJCE, HC 0000133-92.2026.8.06.0000 (deserção: excesso de prazo sem denúncia).
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Liminar: soltura, suspensão do ato ou salvo-conduto, com indicação objetiva do perigo.
- Mérito: concessão da ordem para relaxar a prisão, revogar a preventiva, trancar o IPM ou a ação penal ou anular a punição por vício formal.
- Requisição de informações à autoridade coatora e vista ao MP.
- Pedido subsidiário de menagem ou liberdade provisória, quando cabíveis (CPPM arts. 263 e 270).

## Checklist pré-protocolo
- [ ] Autoridade coatora e juízo competente definidos (oficial-general? Comandante de Força?)
- [ ] Prova pré-constituída juntada (o HC não admite instrução)
- [ ] Hipótese do art. 467 ou 468 do CPPM indicada expressamente
- [ ] Se disciplinar: tese restrita à legalidade, sem discutir conveniência ou dosimetria
- [ ] Sem supressão de instância nem reiteração de pedido idêntico
- [ ] Liminar com fumus e periculum concretos

## Erros a evitar
- Impetrar no juízo comum contra ato ligado a crime militar (ou o inverso).
- Pedir revisão do mérito da punição disciplinar em HC.
- Usar HC contra exclusão do serviço ou perda de posto (Súmula 694/STF).
- Ignorar que o paciente oficial-general desloca a competência para o STM.

## Integração com o núcleo
`prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

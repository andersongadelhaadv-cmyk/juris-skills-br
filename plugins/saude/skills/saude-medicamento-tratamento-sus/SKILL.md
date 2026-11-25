---
name: saude-medicamento-tratamento-sus
description: >
  Redige ação de obrigação de fazer com tutela de urgência (ou mandado de
  segurança) contra o poder público para fornecimento de medicamento,
  tratamento, cirurgia ou insumo pelo SUS, inclusive de alto custo, observando
  os Temas 6, 793 e 1.234 do STF e as Súmulas Vinculantes 60 e 61. Use quando o
  usuário pedir remédio pelo SUS, medicamento de alto custo contra Estado,
  Município ou União, liminar para tratamento negado pela Secretaria de Saúde,
  cirurgia na fila do SUS, mandado de segurança para medicamento ou tutela
  antecedente para tratamento urgente.
metadata:
  area: saude
  tipo_peca: inicial
  verificado_em: 2026-11-25
---
# Medicamento e tratamento pelo SUS (inclusive alto custo, com tutela de urgência)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: medicamento (incorporado ou não às listas do SUS, com registro na Anvisa), procedimento, cirurgia, exame, insumo ou internação negado ou não fornecido pelo SUS; inclui o pedido de tutela de urgência, incidental ou antecedente, para tratamento de alto custo.
- Medicamento **sem registro** na Anvisa: `saude-medicamento-sem-registro-anvisa` (Tema 500/STF; ação contra a União).
- Contra **plano de saúde**: `consumidor-plano-de-saude`. Indenização por demora ou erro no atendimento público: `adm-responsabilidade-civil-do-estado`.
- Regras gerais de tutela provisória: `civel-tutela-provisoria`; mandado de segurança em geral: `adm-mandado-de-seguranca`.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Relatório médico fundamentado: diagnóstico (CID), tratamentos já feitos e por que falharam, fármaco/procedimento indicado, dose, duração, urgência e risco da demora.
2. Registro na Anvisa e indicação em bula (uso *off label*?); está nas listas do SUS (RENAME, componente especializado, PCDT)? Para qual doença?
3. Houve pedido de incorporação à Conitec? Foi negado, está em análise ou nunca foi feito?
4. **Pedido administrativo e negativa** (ou omissão) do ente — protocolo, resposta, data.
5. Estudos que sustentam a eficácia (ensaios clínicos randomizados, revisão sistemática, meta-análise) — o autor terá esse ônus.
6. Custo anual pelo PMVG da CMED (define competência no Tema 1.234) e três orçamentos.
7. Renda e despesas do paciente (incapacidade financeira); laudo do NATJUS, se já existir.

## Prazo e contagem
- Mandado de segurança: 120 dias da ciência do ato impugnado (Lei 12.016/2009, art. 23). Contra recusa antiga, prefira novo requerimento administrativo ou a ação ordinária [VERIFICAR: termo inicial do prazo em omissão continuada].
- Ação de obrigação de fazer: sem prazo decadencial próprio; a urgência decorre do quadro clínico.
- Incorporação pela Conitec: prazo legal de 180 dias, prorrogável por 90 (Lei 8.080/1990, art. 19-R) — mora relevante para o Tema 6.
- Prazos processuais e de cumprimento: `prazos-processuais`.

## Estrutura da peça
Tutela de urgência em destaque → competência e polo passivo (Tema 1.234; Tema 793) → fatos clínicos → direito à saúde (CF 196 e 198, II; Lei 8.080) → enquadramento: incorporado x não incorporado → requisitos do Tema 6 item a item → urgência → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Incorporado ao SUS**: basta demonstrar indicação, prescrição e falha no fornecimento; o fluxo e o ente responsável seguem os acordos homologados no Tema 1.234 (Súmula Vinculante 60).
- **Não incorporado, com registro na Anvisa**: regra é a negativa; excepcionalmente concede-se com prova cumulativa, pelo autor, de (a) negativa administrativa; (b) ilegalidade da não incorporação pela Conitec, ausência de pedido ou mora; (c) impossibilidade de substituição por item das listas e PCDTs; (d) eficácia e segurança por evidência de alto nível (ensaios randomizados, revisão sistemática ou meta-análise); (e) imprescindibilidade clínica em laudo fundamentado, com tratamentos já feitos; (f) incapacidade financeira (Tema 6/STF; Súmula Vinculante 61). O juiz deve consultar o NATJUS e não pode decidir só com o laudo do autor.
- **Competência (Tema 1.234)**: não incorporado com registro tramita na Justiça Federal quando o tratamento anual (PMVG/CMED) for igual ou superior a 210 salários mínimos (CF art. 109, I); abaixo disso, Justiça Estadual. Oncológicos incorporados seguem o grupo do componente especializado. Instrua a inicial com o cálculo.
- **Polo passivo**: os entes são solidários, cabendo ao juiz direcionar o cumprimento conforme a repartição de competências (Tema 793/STF); o Tema 1.234 permite incluir outro ente para viabilizar o cumprimento.
- **Mandado de segurança**: exige prova pré-constituída de **todos** os requisitos. Em não incorporado, o STJ tem negado o MS por falta de prova pré-constituída e necessidade de dilação (RMS 75.325, 2ª Turma, 2026 — *off label*; RMS 30.746, 2ª Turma, 2026 — laudo particular insuficiente diante do Tema 6). Prefira a ação ordinária quando a eficácia depender de perícia ou NATJUS.
- **Tema 106/STJ** (REsp 1.657.156): ainda citado pelo STJ junto com os Temas 6 e 1.234 (AgInt no RMS 76.899, 1ª Turma, 2026). Os requisitos vinculantes atuais são os do Tema 6 [VERIFICAR: situação atual do Tema 106 após o Tema 6].
- **Irreversibilidade**: a tutela antecipada não se concede com perigo de irreversibilidade (CPC art. 300, § 3º) — em saúde, ponderar o risco à vida; fundamente expressamente.

## Fundamentos verificados
- CF arts. 196, 198, II, 109, I. Lei 8.080/1990 arts. 6º, I, "d", 19-M, 19-P, 19-Q, 19-R, 19-T. CPC arts. 300, 303, 497, 536, 537. Lei 12.016/2009 arts. 1º, 7º, III, 23.
- STF: Temas 6, 793, 1.234; Súmulas Vinculantes 60 e 61. STJ: AgInt no RMS 74.840 e AgInt no RMS 76.899 (MS sem prova pré-constituída); RMS 75.325; RMS 30.746.
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Tutela de urgência (CPC 300) — ou tutela antecipada antecedente (CPC 303), se a urgência for contemporânea — para fornecimento em prazo curto, com multa (CPC 537) e medidas de efetivação (CPC 536).
- Consulta ao NATJUS em caráter de urgência (dever do juiz pelo Tema 6) — antecipe o parecer se possível.
- Procedência: obrigação de fazer (CPC 497) de fornecer o tratamento enquanto houver prescrição, com relatórios periódicos (item 5.4 do Tema 1.234).
- No MS: liminar (Lei 12.016, art. 7º, III) e concessão da segurança.
- Ofício à Conitec para avaliar a incorporação (Tema 6, item 3, "c").
- Gratuidade e prioridade de tramitação, quando cabíveis (ver `civel-peticao-inicial`).

## Checklist pré-protocolo
- [ ] Negativa administrativa (ou omissão) documentada
- [ ] Incorporado ou não? Registro Anvisa? Uso conforme bula?
- [ ] Requisitos (a) a (f) do Tema 6 provados, um a um
- [ ] Evidência científica de alto nível juntada (não só o laudo)
- [ ] Custo anual pelo PMVG/CMED calculado — competência (Tema 1.234)
- [ ] Ente(s) no polo passivo coerente(s) com o fluxo do Tema 1.234 e o Tema 793
- [ ] MS só com prova pré-constituída completa; prazo de 120 dias
- [ ] Irreversibilidade enfrentada no pedido de tutela
- [ ] Multa e prazo de cumprimento propostos

## Erros a evitar
- Pedir medicamento não incorporado só com receita e laudo genérico: o Tema 6 exige prova científica de alto nível e a análise do ato da Conitec.
- Ajuizar na Justiça Estadual tratamento que ultrapassa 210 salários mínimos/ano (ou o inverso).
- Escolher MS quando a eficácia ainda depende de perícia.
- Omitir o pedido administrativo prévio.
- Usar esta skill para medicamento sem registro na Anvisa ou contra plano de saúde.

## Integração com o núcleo
`prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`; tutela em geral: `civel-tutela-provisoria`. Valores a ressarcir ou cobrar: `juros-e-correcao`.

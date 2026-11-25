---
name: saude-medicamento-sem-registro-anvisa
description: >
  Redige ação contra a União (Justiça Federal) para fornecimento de medicamento
  sem registro na Anvisa nas hipóteses excepcionais do Tema 500/STF (mora
  irrazoável da agência, registro no exterior, ausência de substituto) e do
  Tema 1.161/STF (importação autorizada pela Anvisa), além de ação ou mandado
  de segurança contra a Anvisa pela mora na análise do registro. Use quando o
  usuário pedir remédio importado sem registro no Brasil, medicamento órfão
  para doença rara, ação contra a União por medicamento não registrado, ou
  ação contra a Anvisa por demora no registro.
metadata:
  area: saude
  tipo_peca: inicial
  verificado_em: 2026-11-25
---
# Medicamento sem registro na Anvisa / ação contra a Anvisa

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: (a) paciente que precisa de medicamento **sem registro** na Anvisa; (b) medicamento sem registro, mas com **importação autorizada** pela Anvisa; (c) empresa requerente do registro diante da **mora** da Anvisa em decidir.
- Medicamento **com** registro, incorporado ou não ao SUS: `saude-medicamento-tratamento-sus` (Temas 6 e 1.234).
- Medicamento **experimental** (em pesquisa clínica): o Estado não pode ser obrigado a fornecer (Tema 500, item 1) — não ajuizar com base nesta skill.
- Contra plano de saúde: `consumidor-plano-de-saude`.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Medicamento, princípio ativo, fabricante; relatório médico com diagnóstico (CID), tratamentos anteriores e imprescindibilidade.
2. Situação regulatória no Brasil: há pedido de registro protocolado? Em que data? Categoria prioritária ou ordinária? Há decisão? Há autorização de importação excepcional?
3. Registro em agências estrangeiras de referência (quais, desde quando) — documentos oficiais.
4. Existe substituto terapêutico registrado no Brasil? Por que não serve?
5. Doença rara ou ultrarrara (medicamento órfão)?
6. Custo, forma de importação e capacidade financeira do paciente.
7. Para a empresa: número do processo na Anvisa, datas de protocolo, exigências e respostas.

## Prazo e contagem
- Prazos legais da Anvisa para decidir o registro de medicamento: 120 dias na categoria prioritária e 365 dias na ordinária, contados do protocolo (Lei 6.360/1976, art. 17-A, § 2º, incluído pela Lei 13.411/2016). A mora além desses prazos é o pressuposto do Tema 500.
- Mandado de segurança contra a Anvisa: 120 dias da ciência do ato (Lei 12.016/2009, art. 23); em omissão, fundamente o termo inicial [VERIFICAR: termo inicial em omissão continuada].
- Prazos processuais: `prazos-processuais`.

## Estrutura da peça
Tutela de urgência → competência federal e União no polo passivo → fatos clínicos → situação regulatória (pedido, prazos, mora) → requisitos do Tema 500 (ou do Tema 1.161) item a item → urgência → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Regra**: sem registro sanitário não há fornecimento judicial (Tema 500, item 2; Lei 6.360, art. 12; Lei 8.080, art. 19-T).
- **Exceção do Tema 500** (item 3): mora irrazoável da Anvisa (prazo superior ao da Lei 13.411/2016) e, cumulativamente: (i) pedido de registro no Brasil — dispensado para medicamento órfão de doença rara ou ultrarrara; (ii) registro em renomadas agências de regulação no exterior; (iii) inexistência de substituto terapêutico registrado no Brasil.
- **Exceção do Tema 1.161**: medicamento sem registro, mas com importação autorizada pela Anvisa, desde que comprovadas incapacidade econômica, imprescindibilidade clínica e impossibilidade de substituição por item das listas e protocolos do SUS.
- **Polo passivo e competência**: a ação deve ser proposta contra a União (Tema 500, item 4), na Justiça Federal (CF art. 109, I); o Tema 1.234 (item 2.1.1) mantém essa competência. Estado ou Município sozinhos no polo é erro.
- **Ação contra a Anvisa**: quem a move é, em regra, a empresa requerente — para impor decisão no prazo legal (Lei 6.360, art. 17-A), não para obter o registro por decisão judicial. Autarquia federal: Justiça Federal (CF art. 109, I).
- **Irreversibilidade** da tutela: enfrentar o CPC art. 300, § 3º, ponderando o risco à vida.

## Fundamentos verificados
- CF art. 109, I. Lei 6.360/1976 arts. 12 e 17-A (Lei 13.411/2016). Lei 8.080/1990 art. 19-T. CPC arts. 300, 497, 536, 537. Lei 12.016/2009 arts. 1º, 7º, III, 23.
- STF: Tema 500 (RE 657.718); Tema 1.161 (RE 1.165.959); Tema 1.234, item 2.1.1 (RE 1.366.243).
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Tutela de urgência (CPC 300) para fornecimento pela União em prazo curto, com multa (CPC 537) e medidas de efetivação (CPC 536), inclusive importação pela via autorizada.
- Procedência: obrigação de fazer (CPC 497) de fornecer enquanto houver prescrição, com relatórios médicos periódicos.
- Perícia ou consulta técnica (NATJUS) sobre substituto terapêutico e evidências.
- Ação da empresa contra a Anvisa: ordem para decidir o pedido de registro em prazo fixado; no MS, liminar (Lei 12.016, art. 7º, III).

## Checklist pré-protocolo
- [ ] Medicamento não é experimental
- [ ] Data do protocolo de registro no Brasil e categoria (prioritária/ordinária) — mora calculada
- [ ] Ou: medicamento órfão de doença rara/ultrarrara (dispensa o pedido de registro)
- [ ] Ou: importação autorizada pela Anvisa (Tema 1.161)
- [ ] Registros estrangeiros documentados
- [ ] Inexistência de substituto registrado no Brasil demonstrada
- [ ] União no polo passivo; Justiça Federal
- [ ] Incapacidade financeira e imprescindibilidade clínica provadas
- [ ] Irreversibilidade enfrentada

## Erros a evitar
- Ajuizar contra Estado ou Município: o Tema 500 exige a União.
- Pedir medicamento ainda em fase de pesquisa (vedado pelo item 1 do Tema 500).
- Alegar mora sem conferir data de protocolo e prazo legal da categoria.
- Pedir que o juiz "conceda o registro": o Judiciário pode impor a decisão no prazo, não substituir a Anvisa.
- Confundir medicamento sem registro com medicamento registrado e não incorporado (Tema 6).

## Integração com o núcleo
`prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`; tutela em geral: `civel-tutela-provisoria`; MS em geral: `adm-mandado-de-seguranca`.

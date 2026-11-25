---
name: adm-anulacao-de-ato-por-autotutela
description: >
  Redige requerimento administrativo de anulação (ou revisão) de ato ilegal pela
  própria Administração, com base no dever de autotutela (Súmulas 346 e 473 do
  STF; Lei 9.784/1999, arts. 53 a 55, 63, § 2º, e 65), observando a decadência de
  5 anos do art. 54 e o contraditório exigido pelo Tema 138 do STF. Use quando o
  usuário pedir anular ato administrativo na via administrativa, pedido de
  revisão de ofício, prazo de recurso perdido, requerimento de autotutela,
  revisão de sanção por fato novo, ou defesa de quem será prejudicado por
  anulação de ato que o beneficia (decadência e direito adquirido).
metadata:
  area: administrativo-licitacoes
  tipo_peca: requerimento
  verificado_em: 2026-11-25
---
# Anulação de ato pela via administrativa (autotutela)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar em dois sentidos:
  - **Ativo** — o cliente quer que a Administração anule ato ilegal que o prejudica (prazo de recurso perdido, ato já definitivo, nulidade evidente) ou que reveja sanção por fato novo.
  - **Defensivo** — a Administração abriu processo para anular ato que beneficia o cliente: arguir decadência, boa-fé, convalidação e exigir contraditório.
- Não usar:
  - ainda no prazo de recurso: `adm-recurso-contra-auto-de-infracao` (sanção de polícia), `adm-recurso-em-licitacao` (licitação), `adm-defesa-em-pad` (servidor);
  - via judicial: `adm-acao-anulatoria-de-ato-administrativo` ou `adm-mandado-de-seguranca`;
  - revogação por conveniência que o cliente quer impedir em licitação: `adm-recurso-em-licitacao`;
  - informação para instruir o pedido: `adm-acesso-a-informacao-lai`.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. O ato: autoridade, data de edição, publicação, conteúdo e quem ele beneficia ou prejudica.
2. O vício alegado (competência, forma, motivo, objeto, finalidade) e a prova documental.
3. Se o ato gera efeitos patrimoniais contínuos e a data do primeiro pagamento (art. 54, § 1º).
4. No defensivo: data da instauração do processo de anulação ou da primeira medida que impugnou o ato (art. 54, § 2º); indícios de má-fé alegados pela Administração.
5. Recursos já interpostos e decisões; se houve não conhecimento por intempestividade.
6. Ente e lei de processo administrativo aplicável (federal, estadual, municipal).

## Prazo e contagem
- Não há prazo para o requerimento ativo, mas a Administração só pode anular ato favorável ao destinatário em 5 anos da prática, salvo má-fé comprovada (Lei 9.784/1999, art. 54); com efeitos patrimoniais contínuos, conta-se do primeiro pagamento (§ 1º); qualquer medida de autoridade que impugne a validade do ato conta como exercício do direito de anular (§ 2º).
- Estados e Municípios sem lei própria: aplica-se subsidiariamente o prazo da Lei 9.784/1999 (Súmula 633/STJ).
- Revisão de processo sancionador: a qualquer tempo, por fato novo ou circunstância relevante, sem agravamento (art. 65).
- Prescrição para a via judicial continua correndo: requerimento pendente suspende a prescrição contra a Fazenda (Decreto 20.910/1932, art. 4º). Conferir com `prazos-processuais`.

## Estrutura da peça (resumo; detalhe em [estrutura](references/estrutura.md))
Ativo: endereçamento → legitimidade → ato e vício → dever de anular (art. 53; Súmula 473) → não conhecimento de recurso não impede revisão de ofício (art. 63, § 2º) → consequências práticas (LINDB) → pedido. Defensivo: decadência → boa-fé → convalidação → contraditório → orientações da época → pedido de arquivamento.

## Requisitos e preliminares
- Direito de petição (CF, art. 5º, XXXIV, "a").
- Anular é dever diante de ilegalidade; revogar é juízo de conveniência e respeita direitos adquiridos (art. 53; Súmula 473/STF).
- Ato com defeito sanável pode ser convalidado se não lesar o interesse público nem terceiros (art. 55) — no defensivo, pedir convalidação em vez de anulação.
- Ato que já produziu efeitos concretos só se desfaz após processo com contraditório (Tema 138/STF).
- Decisão que anula, revoga, suspende ou convalida deve ser motivada (art. 50, VIII) e indicar as consequências (LINDB, art. 21).
- Vedada invalidação de situação plenamente constituída por mudança posterior de orientação geral (LINDB, art. 24).

## Fundamentos verificados (resumo; detalhe em [fundamentos](references/fundamentos.md))
- CF, art. 5º, XXXIV, "a", e LV; art. 37, caput.
- Lei 9.784/1999: arts. 2º, 50, 53, 54, 55, 63, § 2º, 64, parágrafo único, 65.
- LINDB, arts. 20, 21 e 24.
- Súmulas 346 e 473/STF; Tema 138/STF; Súmula 633/STJ.
- Decreto 20.910/1932, art. 4º.

## Pedidos e requerimentos
- Ativo: anulação do ato e dos atos dele dependentes; restabelecimento da situação anterior; restituição de valores, com atualização pelo núcleo `juros-e-correcao`; subsidiariamente, revisão da sanção (art. 65).
- Defensivo: reconhecimento da decadência e arquivamento; subsidiariamente, convalidação (art. 55), modulação dos efeitos e regime de transição (LINDB, arts. 21 e 24); vista integral e prazo para defesa antes de qualquer decisão (Tema 138).
- Em ambos: decisão motivada (art. 50, VIII) e intimação pessoal do resultado.

## Checklist pré-protocolo
- [ ] Ato identificado com data de edição e de primeiro pagamento (se houver)
- [ ] Cálculo da decadência do art. 54 com as datas
- [ ] Vício demonstrado com documento
- [ ] Lei local de processo administrativo conferida (Súmula 633)
- [ ] Consequências práticas da anulação expostas
- [ ] No defensivo: má-fé alegada enfrentada e convalidação pedida
- [ ] Protocolo guardado (suspende a prescrição judicial — Decreto 20.910/1932, art. 4º)

## Erros a evitar
- Tratar o requerimento como "recurso intempestivo": o fundamento é o dever de anular e o art. 63, § 2º.
- Pedir revogação (mérito) quando o caso é de ilegalidade, ou o inverso.
- No defensivo, discutir só o mérito e esquecer a decadência do art. 54 e o termo inicial do § 1º.
- Esperar a decisão administrativa sem controlar a prescrição da ação judicial.
- Aceitar agravamento em revisão de sanção (vedado pelo art. 65, parágrafo único).

## Integração com o núcleo
`prazos-processuais`, `juros-e-correcao`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

---
name: civel-habilitacao-de-credito-recuperacao-falencia
description: >
  Redige habilitação de crédito, divergência administrativa, impugnação à
  relação de credores, habilitação retardatária, pedido de reserva e ação de
  retificação ou exclusão de crédito em recuperação judicial e falência (Lei
  11.101/2005, arts. 7º a 20), e a contestação do credor impugnado. Use quando
  o usuário pedir para habilitar crédito na recuperação judicial ou na falência,
  divergir do valor ou da classe na lista do administrador judicial, impugnar
  crédito de outro credor, habilitar fora do prazo, pedir reserva de valor ou
  discutir se o crédito é concursal ou extraconcursal.
metadata:
  area: processo-civil
  tipo_peca: requerimento
  verificado_em: 2026-11-25
---
# Habilitação e impugnação de crédito na recuperação judicial e na falência

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar, conforme o momento:
  - **fase administrativa** — habilitação ou divergência dirigida ao administrador judicial (art. 7º, § 1º);
  - **fase judicial** — impugnação contra a relação publicada pelo administrador (art. 8º) ou contestação do credor impugnado (art. 11);
  - **fora do prazo** — habilitação retardatária e reserva de valor (art. 10);
  - **depois do quadro-geral** — retificação do quadro (art. 10, § 6º) ou ação de exclusão, reclassificação ou retificação por falsidade, dolo, simulação, fraude, erro essencial ou documento ignorado (art. 19).
- Não usar: pedido de recuperação, plano, objeção ao plano ou assembleia (fora desta skill); crédito fiscal na falência — incidente próprio do art. 7º-A (`trib-*` / `fazenda-*`); crédito trabalhista ainda ilíquido — apurar antes na Justiça do Trabalho (`trabalhista-*`).
- Cobrança individual contra a recuperanda de crédito concursal: não prossegue (Tema 1051 — ver Fundamentos); habilite.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Tipo de processo (RJ ou falência), juízo, número, data do pedido de recuperação ou da decretação da falência.
2. Datas de publicação: edital do art. 52, § 1º (RJ) ou do art. 99, parágrafo único (falência); relação do administrador (art. 7º, § 2º); quadro-geral homologado?
3. O crédito consta da lista do devedor ou da relação do administrador? Com que valor e classe?
4. Origem do crédito e **data do fato gerador** (contrato, prestação de serviço, sentença que fixou honorários, ato ilícito).
5. Documentos: título, notas, contratos, sentença, planilha; garantias e instrumento; bem da garantia em poder do credor.
6. Para impugnar crédito alheio: qual crédito, por que é indevido, inflado ou mal classificado, e as provas.

## Prazo e contagem
- Habilitação ou divergência ao administrador: **15 dias** do edital (art. 7º, § 1º).
- Impugnação judicial à relação do administrador: **10 dias** da publicação da relação (art. 8º).
- Contestação do credor impugnado: **5 dias** (art. 11); manifestação do devedor e do comitê e parecer do administrador: **5 dias** cada (art. 12).
- Habilitação retardatária ou reserva na falência: até **3 anos** da publicação da sentença de falência, sob pena de decadência (art. 10, § 10).
- Ação do art. 19: até o encerramento da recuperação ou da falência.
- Dias corridos ou úteis na Lei 11.101: conferir em `prazos-processuais` [VERIFICAR: art. 189, § 1º, não conferido nesta skill].

## Estrutura da peça
Habilitação/divergência: destinatário (administrador ou juízo) → credor e endereço para comunicações → crédito (valor atualizado até a data do pedido/falência, origem, classe) → documentos → garantias → pedido. Impugnação: legitimidade → tempestividade → crédito impugnado → razões (existência, valor, classe, concursalidade) → provas → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Conteúdo obrigatório da habilitação (art. 9º): nome e endereço do credor e endereço para comunicações; valor atualizado até a data do pedido de RJ ou da falência, origem e classificação; documentos e provas a produzir; garantia e instrumento; especificação do bem em poder do credor. Originais ou cópias autenticadas se estiverem em outro processo (parágrafo único).
- Legitimados para impugnar (art. 8º): comitê, qualquer credor, devedor ou seus sócios e Ministério Público.
- A impugnação corre em autos apartados; impugnações sobre o mesmo crédito ficam numa só autuação (arts. 8º, parágrafo único, e 13).
- Retardatário na RJ não vota na assembleia, salvo crédito trabalhista (art. 10, § 1º); na falência perde rateios já feitos e paga custas (art. 10, § 3º).
- Concursalidade: a existência do crédito se mede pela data do **fato gerador**, não do trânsito em julgado ou do vencimento (Tema 1051).
- Cotas condominiais: tratadas como extraconcursais pela 2ª Seção do STJ (Tema 1391) — ver Fundamentos.

## Fundamentos verificados
- Lei 11.101/2005, arts. 7º a 20 (com a redação da Lei 14.112/2020).
- Tema 1051/STJ, aplicado em REsp 2.027.349 (3ª Turma, rel. Min. Ricardo Villas Bôas Cueva, julg. 23/06/2025): existência do crédito determinada pela data do fato gerador. [VERIFICAR: o acórdão-paradigma do Tema 1051 não está na base consultada; a tese foi conferida pela transcrição em acórdãos confirmados.]
- Tema 1391/STJ (REsp 2.206.633, 2ª Seção, rel. Min. Ricardo Villas Bôas Cueva, julg. 13/05/2026): cotas condominiais com natureza extraconcursal na RJ.
- Honorários em impugnação de crédito litigiosa: cabimento reconhecido pela 3ª Turma (AgInt no REsp 2.119.427, julg. 13/05/2024); a questão foi afetada como Tema 1250 [VERIFICAR: julgamento do Tema 1250 não localizado na base].
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Habilitação/divergência: inclusão (ou alteração) do crédito na relação, com valor, classe e garantia indicados.
- Impugnação: exclusão, redução, majoração ou reclassificação; produção de provas (art. 15); honorários de sucumbência se houver litigiosidade.
- Retardatária: recebimento como impugnação se antes da homologação do quadro (art. 10, § 5º); **reserva de valor** (art. 10, § 4º).
- Recurso contra a decisão da impugnação: agravo (art. 17), com pedido ao relator de efeito suspensivo ou de inscrição provisória para voto — `civel-agravo-de-instrumento`.
- Atualização do crédito até a data do pedido/falência: cálculo pelo núcleo `juros-e-correcao`.

## Checklist pré-protocolo
- [ ] Fase correta (administrativa, judicial, retardatária, art. 19) e destinatário correto
- [ ] Prazo contado da publicação certa (edital x relação do administrador)
- [ ] Data do fato gerador comprovada (concursal x extraconcursal)
- [ ] Valor atualizado só até a data do pedido de RJ ou da falência
- [ ] Classe fundamentada e garantias com instrumento
- [ ] Todos os requisitos do art. 9º preenchidos
- [ ] Pedido de reserva, se retardatário
- [ ] Prazos e contagem conferidos no núcleo

## Erros a evitar
- Protocolar a habilitação no processo judicial durante a fase administrativa (ela vai ao administrador).
- Atualizar o crédito até hoje, e não até a data do pedido ou da falência.
- Tratar honorários fixados em sentença anterior ao pedido como extraconcursais só porque o trânsito foi posterior (o fato gerador é a sentença — Tema 1051).
- Habilitar fora do prazo sem pedir reserva e sem enfrentar a perda de voto/rateio.
- Impugnar sem impugnação específica e sem prova: o juiz homologa o crédito não impugnado.
- Perder o prazo decadencial de 3 anos na falência (art. 10, § 10).

## Integração com o núcleo
`prazos-processuais`, `juros-e-correcao`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`. Execução individual suspensa contra o devedor: `civel-execucao-titulo-extrajudicial` e `civel-cumprimento-de-sentenca`.

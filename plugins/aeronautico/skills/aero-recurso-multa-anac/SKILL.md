---
name: aero-recurso-multa-anac
description: >
  Redige defesa contra auto de infração e recurso administrativo contra multa ou
  providência aplicada pela ANAC (empresa aérea, táxi aéreo, escola, oficina,
  operador de aeródromo, piloto ou proprietário de aeronave), com base no CBA
  (arts. 288, 289, 292 e 319), na Lei 11.182/2005, na Lei 9.784/1999, na Lei
  9.873/1999 e na Resolução ANAC 472/2018. Use quando o usuário pedir defesa de
  auto de infração da ANAC, recurso contra multa da ANAC, prescrição de multa
  aeronáutica, suspensão ou cassação de licença ou certificado, ou recurso à
  Diretoria da ANAC.
metadata:
  area: aeronautico
  tipo_peca: recurso
  verificado_em: 2026-11-25
---
# Defesa e recurso contra multa da ANAC

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: defesa em primeira instância contra auto de infração; recurso à segunda instância; recurso à Diretoria nos casos de cassação, suspensão ou multa elevada; pedido de reconhecimento de prescrição no processo sancionador; impugnação de providência administrativa (suspensão, cassação, detenção ou apreensão de aeronave).
- Não usar: ação judicial anulatória ou mandado de segurança depois da decisão final (`adm-mandado-de-seguranca`; ação comum em `civel-peticao-inicial`); defesa em execução fiscal da multa já inscrita (`trib-embargos-a-execucao-fiscal` ou `trib-excecao-pre-executividade-fiscal`); processo sancionador de licitação (`adm-defesa-em-processo-sancionador-licitacao`); infração que também é crime ou contravenção (`aero-infracao-aeronautica-jecrim`).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Auto de infração completo: número, data do fato, data da lavratura, descrição da conduta, dispositivo apontado, enquadramento e valor proposto.
2. Data da **ciência** de cada ato (intimação do auto, decisão de primeira instância, decisão de segunda instância) e meio usado.
3. Todos os atos do processo com datas (para medir paralisação e prescrição).
4. Histórico de sanções definitivas do autuado nos 12 meses anteriores (atenuante) e de reincidência (agravante).
5. Provas da versão do autuado: diário de bordo, registros de manutenção, escala de tripulação, comunicações com a ANAC, prova de correção voluntária.
6. Se já pediu arbitramento sumário ou pagou com desconto (implica renúncia ao litígio administrativo).

## Prazo e contagem
- **Defesa**: 20 dias da ciência da intimação do auto (Resolução ANAC 472/2018, art. 25), contados em dias úteis (art. 21, parágrafo único). Conferir se o texto vigente mantém esses prazos [VERIFICAR alterações posteriores a 2021 no portal da ANAC].
- **Recurso**: 10 dias da ciência da decisão (Res. 472, art. 38; mesmo prazo na Lei 9.784/1999, art. 59). Recurso à Diretoria: 10 dias, nas hipóteses do art. 46.
- **Prescrição** — duas teses a medir caso a caso:
  - CBA art. 319: as providências administrativas do Código prescrevem em 2 anos do ato ou fato que as autorizar.
  - Lei 9.873/1999: 5 anos da prática do ato para a ação punitiva federal (art. 1º), 3 anos de paralisação no processo pendente de julgamento ou despacho (art. 1º, § 1º), prazo penal se o fato também for crime (§ 2º); interrupções no art. 2º. O STJ aplica a intercorrente do art. 1º, § 1º, aos processos de infração administrativa não tributária (Tema 1.293).
  - Qual prazo prevalece para infração aeronáutica não foi conferido em jurisprudência [VERIFICAR]: alegue o art. 319 do CBA como lei especial e, subsidiariamente, a Lei 9.873.
- Prazos judiciais posteriores: `prazos-processuais`.

## Estrutura da peça
Tempestividade → efeito suspensivo → preliminares (prescrição, nulidade do auto, cerceamento de defesa) → mérito (fato, autoria, tipicidade, excludentes) → dosimetria (atenuantes, agravantes, infração continuada) → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Efeito suspensivo**: a Res. 472 (art. 38, § 1º) nega efeito suspensivo ao recurso, ressalvado o art. 61 da Lei 9.784; o CBA (art. 292, § 2º) diz que o procedimento será sumário, **com efeito suspensivo**. Peça o efeito com base na lei e, subsidiariamente, no justo receio de prejuízo (Lei 9.784, art. 61, parágrafo único).
- **Ampla defesa e recurso** são assegurados pelo próprio CBA (art. 292) e pela Lei 9.784 (arts. 2º e 38). Prova recusada sem decisão fundamentada é nulidade.
- **Tipicidade**: a ANAC tipifica infrações e sanções por regulamento (CBA art. 288; Lei 11.182, art. 8º, LIII). Confronte a conduta com o tipo da tabela vigente **na data do fato**.
- **Motivação**: decisão que impõe ou agrava sanção ou decide recurso deve indicar fatos e fundamentos (Lei 9.784, art. 50).
- **Reformatio in pejus**: se o recurso puder agravar a situação, o recorrente deve ser cientificado para alegar antes (Lei 9.784, art. 64, parágrafo único).
- **Arbitramento sumário**: pagar 50% do valor médio importa reconhecer a infração e renunciar ao litígio administrativo (Res. 472, art. 28 e § 1º). Avalie antes de recomendar.

## Fundamentos verificados
- CBA arts. 288, 289, 292, 295, 319; Lei 11.182/2005, art. 8º, XXXV, LI e LIII.
- Lei 9.784/1999 arts. 2º, 38, 50, 56, 57, 59, 61, 64; Lei 9.873/1999 arts. 1º, 1º-A, 2º, 5º.
- Resolução ANAC 472/2018 arts. 21, 25, 28, 36, 37-A, 37-B, 38, 46.
- STJ: Tema 1.293 (intercorrente da Lei 9.873); AgInt no AREsp 2.314.672 (fato também crime: prazo penal).
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Recebimento com efeito suspensivo.
- Reconhecimento da prescrição (punitiva ou intercorrente) e arquivamento.
- Nulidade do auto ou da decisão (vício de descrição, tipificação, motivação, cerceamento).
- No mérito, insubsistência do auto.
- Subsidiariamente, redução da multa pelas atenuantes do art. 36, § 1º, da Res. 472, afastamento de agravante sem prova e reconhecimento de infração continuada (arts. 37-A e 37-B), quando cabível.
- Produção de provas especificadas (documentos, diligência, oitiva).

## Checklist pré-protocolo
- [ ] Data de ciência comprovada e prazo contado em dias úteis
- [ ] Linha do tempo do processo para medir 2, 3 e 5 anos
- [ ] Tipo infracional da data do fato conferido
- [ ] Efeito suspensivo pedido (CBA 292 § 2º)
- [ ] Atenuantes documentadas; agravantes impugnadas
- [ ] Nenhum pedido de arbitramento sumário anterior (ou consequência avaliada)
- [ ] Procuração e atos constitutivos juntados

## Erros a evitar
- Contar o prazo em dias corridos.
- Discutir só o mérito e esquecer a prescrição intercorrente.
- Aceitar a regra regulamentar de ausência de efeito suspensivo sem invocar o CBA art. 292, § 2º.
- Recomendar o pagamento com desconto sem explicar a renúncia ao litígio administrativo.
- Impugnar a multa com base em tabela posterior ao fato.

## Integração com o núcleo
`prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`; correção da multa paga indevidamente: `juros-e-correcao`.

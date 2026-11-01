---
name: adm-pedido-de-reequilibrio-economico-financeiro
description: >
  Redige pedido administrativo (ou fundamenta ação) de restabelecimento do
  equilíbrio econômico-financeiro, revisão, reajuste ou repactuação de contrato
  administrativo (CF art. 37, XXI; Lei 14.133/2021, arts. 103, 124, II, "d", 130,
  131, 134 a 136). Use quando o usuário pedir reequilíbrio, revisão contratual,
  recomposição de preços, álea extraordinária, fato do príncipe, aumento de
  insumos, reajuste não pago, repactuação de mão de obra ou termo indenizatório.
metadata:
  area: administrativo-licitacoes
  tipo_peca: requerimento
  verificado_em: 2026-11-01
---
# Pedido de reequilíbrio econômico-financeiro

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
Escolher o instrumento certo antes de redigir:
- Revisão / reequilíbrio (art. 124, II, "d"): força maior, caso fortuito, fato do príncipe, fatos imprevisíveis ou previsíveis de consequências incalculáveis que inviabilizem a execução como pactuada, respeitada a matriz de riscos.
- Reequilíbrio por alteração unilateral (art. 130): no mesmo termo aditivo que alterou os encargos.
- Revisão por tributo ou encargo legal (art. 134): criação, alteração ou extinção após a proposta, com repercussão comprovada.
- Reajuste em sentido estrito: índice contratual, anualidade (art. 92, § 3º e § 4º, I) — formalizado por apostila (art. 136, I).
- Repactuação (art. 135): serviços contínuos com dedicação exclusiva ou predominância de mão de obra; planilha analítica; interregno de 1 ano.
- Não usar reequilíbrio para variações de mercado ordinárias, riscos alocados ao contratado na matriz (art. 103, § 5º) ou erro de proposta.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Contrato, edital, proposta com planilha de custos, matriz de riscos e aditivos.
2. Data-base da proposta e do orçamento; índice de reajuste previsto.
3. Evento invocado, data de ocorrência e prova (norma, ato do poder público, série de preços oficial, nota fiscal).
4. Memória de cálculo do impacto por item da planilha.
5. Vigência do contrato, prorrogações previstas e se já houve aditivo posterior ao evento (com ou sem ressalva).
6. Cláusula com prazo de resposta ao pedido (art. 92, X e XI).

## Prazo e contagem
- O pedido deve ser formulado durante a vigência do contrato e antes de eventual prorrogação (art. 131, parágrafo único). Após a extinção, o reconhecimento se faz por termo indenizatório (art. 131, caput), desde que o pedido tenha sido tempestivo.
- Repactuação: interregno mínimo de 1 ano da proposta ou da última repactuação (art. 135, § 3º); resposta preferencialmente em 1 mês da documentação (art. 92, § 6º).
- Aditivo assinado sem ressalva após o evento tende a afastar o pleito (ver fundamentos). Registrar ressalva expressa em todo aditivo e apostila.
- Ação judicial contra a Fazenda: prescrição quinquenal (Decreto 20.910/1932) — conferir termo inicial com `prazos-processuais`.

## Estrutura da peça (resumo; detalhe em [estrutura](references/estrutura.md))
Endereçamento ao gestor/autoridade → contrato e equação original → evento → enquadramento legal → matriz de riscos → nexo e quantificação → pedidos → anexos técnicos.

## Requisitos e preliminares
- Tempestividade (art. 131, parágrafo único).
- Demonstrar que o risco não foi alocado ao contratado (art. 103, §§ 4º e 5º) ou que se enquadra nas exceções do § 5º (alteração unilateral; tributos diretamente pagos).
- Demonstração analítica; sem planilha não há reequilíbrio.
- Obras atrasadas por desapropriação, desocupação, servidão ou licenciamento ambiental alheios ao contratado: aplica-se a alínea "d" (art. 124, § 2º).

## Fundamentos verificados (resumo; detalhe em [fundamentos](references/fundamentos.md))
CF art. 37, XXI; Lei 14.133/2021, arts. 92, 103, 124, 130, 131, 134, 135, 136, 137, § 3º, II; STJ, AgInt no AREsp 2.013.011 e AgInt nos EDcl no AREsp 2.491.214 (aditivo sem ressalva e ônus da prova).

## Pedidos e requerimentos
- Restabelecimento do equilíbrio por termo aditivo (ou termo indenizatório, se extinto), com o novo preço por item.
- Pagamento das diferenças desde o evento, atualizadas — índices e juros exclusivamente pela skill `juros-e-correcao` (Fazenda: regra da EC 113/2021).
- Prazo de resposta conforme cláusula contratual (art. 92, XI).
- Manifestação do assessoramento jurídico e da área técnica.
- Se cabível, suspensão da execução enquanto perdurar a situação do art. 137, § 2º, II a IV (art. 137, § 3º, II).

## Checklist pré-protocolo
- [ ] Contrato vigente e sem prorrogação formalizada depois do evento.
- [ ] Instrumento correto (revisão, reajuste, repactuação, art. 134).
- [ ] Matriz de riscos analisada cláusula a cláusula.
- [ ] Evento datado e posterior à proposta.
- [ ] Planilha analítica comparando custo original e atual, item a item.
- [ ] Prova documental de cada variação (índices oficiais, notas, normas).
- [ ] Ressalvas registradas em aditivos e apostilas posteriores.

## Erros a evitar
- Pedir reequilíbrio depois do fim da vigência sem pedido anterior.
- Assinar aditivo de prorrogação sem ressalva expressa do pleito pendente.
- Confundir reajuste (índice, apostila) com revisão (evento extraordinário, aditivo).
- Alegar inflação ordinária como álea extraordinária.
- Escrever taxa de juros ou índice próprio em vez de remeter a `juros-e-correcao`.
- Citar o art. 65 da Lei 8.666/1993 em contrato regido pela Lei 14.133/2021 (só para contratos anteriores, art. 190).

## Integração com o núcleo
- `juros-e-correcao`: atualização das diferenças.
- `prazos-processuais`: vigência, prorrogação e prescrição contra a Fazenda.
- `verificacao-de-citacoes`: precedentes adicionais.
- `fidelidade-factual`: números da planilha e datas.
- `estilo-forense`: revisão final.

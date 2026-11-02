---
name: prev-recurso-crps
description: >
  Redige recurso ordinário às Juntas de Recursos e recurso especial às Câmaras
  de Julgamento do Conselho de Recursos da Previdência Social contra decisão do
  INSS (Lei 8.213/1991, art. 126; Decreto 3.048/1999, art. 305). Use quando o
  usuário pedir recurso ao CRPS, recurso administrativo do INSS, recurso à Junta
  de Recursos, recurso especial à Câmara de Julgamento ou contrarrazões no CRPS.
metadata:
  area: previdenciario
  tipo_peca: recurso-administrativo
  verificado_em: 2026-11-01
---
# Recurso ao CRPS (Juntas e Câmaras)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: indeferimento, cessação, suspensão ou concessão em valor/espécie inferior ao devido; decisão sobre CNIS ou atividade rural de segurado especial (art. 126, I e III); resultado de reavaliação de benefício por incapacidade (art. 60, §11).
- Recurso ordinário: da decisão do INSS para a Junta de Recursos. Recurso especial: do acórdão da Junta para a Câmara de Julgamento, nas hipóteses do Regimento Interno do CRPS vigente, aprovado pela Portaria MPS 125/2026 (alterada pelas Portarias MPS 235/2026 e 462/2026); as hipóteses de cabimento e a alçada não foram conferidas em fonte oficial [VERIFICAR no texto compilado publicado pelo MPS].
- Não usar quando já houver ação judicial com o mesmo pedido: a propositura importa renúncia ao recurso e desistência do já interposto (art. 126, §3º). Avaliar com o cliente a via mais rápida antes de recorrer.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Número do benefício/requerimento, espécie e DER.
2. Íntegra da decisão recorrida e data da ciência (carta, Meu INSS, e-mail).
3. Motivo do indeferimento, ponto a ponto.
4. Documentos já juntados e documentos novos disponíveis.
5. Se há ação judicial em curso ou planejada.

## Prazo e contagem
- 30 dias, contados da ciência da decisão, para o recurso ordinário e para o recurso especial; mesmo prazo para contrarrazões (Decreto 3.048/1999, art. 305, §1º). Redação atual do art. 305 não conferida em fonte oficial [VERIFICAR no texto compilado do Decreto 3.048 e no regimento do CRPS].
- Para reavaliação de benefício por incapacidade, a Lei 8.213, art. 60, §11, fixa expressamente prazo máximo de 30 dias para recurso ao CRPS.
- Recurso pode ser interposto diretamente ao CRPS nos casos dos incisos I e III do art. 126, com notificação ao INSS para reanálise em até 30 dias (art. 126, §4º).
- Use `prazos-processuais` para o controle; o prazo administrativo segue as regras do regulamento, não o CPC.

## Estrutura da peça   (detalhe em [estrutura](references/estrutura.md))
1. Endereçamento à Junta de Recursos (ou Câmara de Julgamento) do CRPS.
2. Identificação do recorrente, benefício e decisão recorrida.
3. Tempestividade.
4. Síntese da decisão e dos fundamentos do indeferimento.
5. Razões, um tópico por fundamento do INSS.
6. Documentos novos e pedido de diligência (perícia, justificação administrativa, pesquisa externa).
7. Pedidos.

## Requisitos e preliminares
- Atacar cada fundamento da decisão; o recurso genérico costuma ser mantido.
- Pedir diligências específicas: nova perícia com perito diverso (art. 60, §11), justificação administrativa para prova testemunhal de tempo rural ou união estável, emissão de exigência para documento faltante.
- Juntar os documentos novos com a peça; a instrução no CRPS é a última oportunidade administrativa de levar fatos ao INSS (útil também para o Tema 350 STF).

## Fundamentos verificados   (detalhe em [fundamentos](references/fundamentos.md))
- Lei 8.213, art. 126 (competência do CRPS; §3º renúncia; §4º interposição direta).
- Lei 8.213, art. 60, §11 (30 dias para recurso da reavaliação).
- Lei 9.784/1999, art. 56 (recurso por legalidade e mérito, sem caução, salvo lei).
- Matéria de fundo: usar as skills do benefício correspondente.

## Pedidos e requerimentos
- Conhecimento e provimento para conceder/restabelecer o benefício desde a DER (ou desde a cessação).
- Subsidiariamente, conversão em diligência para perícia, justificação administrativa ou exigência documental.
- Reconhecimento dos períodos controvertidos e acerto do CNIS.

## Checklist pré-protocolo
- [ ] Data da ciência documentada e prazo de 30 dias conferido.
- [ ] Verificado que não há ação judicial com pedido idêntico.
- [ ] Cada fundamento do indeferimento respondido em tópico próprio.
- [ ] Documentos novos numerados e citados no texto.
- [ ] Pedido subsidiário de diligência incluído.
- [ ] Procuração com poderes para recorrer.
- [ ] Comprovante de protocolo salvo.

## Erros a evitar
- Ajuizar ação e manter o recurso: o recurso é tido por desistido (art. 126, §3º).
- Contar o prazo pelo CPC (dias úteis) sem conferir a regra administrativa.
- Recorrer sem juntar o documento que motivou o indeferimento.
- Repetir a inicial judicial: o CRPS julga o processo administrativo; foco no que o INSS decidiu.

## Integração com o núcleo
- `prazos-processuais` para o controle do prazo de 30 dias.
- `verificacao-de-citacoes` para enunciados do CRPS ou precedentes acrescentados.
- `fidelidade-factual` para conferir datas e períodos contra o processo administrativo.
- `estilo-forense` para a redação.
- `juros-e-correcao` só na eventual ação de cobrança de atrasados.

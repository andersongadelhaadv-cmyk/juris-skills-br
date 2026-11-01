---
name: familia-revisional-e-exoneracao-de-alimentos
description: >
  Redige ação revisional (majoração ou redução) e ação de exoneração de alimentos, com
  base na mudança da situação financeira das partes (CC art. 1.699; Lei 5.478 arts. 13 e 15)
  e na Súmula 358 do STJ para filho que atingiu a maioridade. Use quando o usuário pedir
  revisão de pensão, redução de pensão, aumento de pensão, majoração de alimentos,
  exoneração de alimentos, fim da pensão por maioridade, cancelamento de pensão.
metadata:
  area: familia-sucessoes
  tipo_peca: inicial
  verificado_em: 2026-11-01
---
# Revisional e exoneração de alimentos

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: alimentos já fixados (sentença, acordo homologado, escritura) e mudança posterior na necessidade de quem recebe ou na capacidade de quem paga; exoneração por maioridade, conclusão de curso, casamento ou união estável do credor (CC 1.708), procedimento indigno.
- Não usar: primeira fixação (use `familia-acao-de-alimentos`); cobrança (use `familia-execucao-de-alimentos`); mera insatisfação com o valor original sem fato novo.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Título atual (cópia), data e valor fixado; condições da época (renda, despesas).
2. Fato novo e data: desemprego, nova família/filho, doença, aumento de renda do devedor, novas despesas do credor, maioridade, emprego do credor, término de faculdade.
3. Documentos que comprovem a situação antiga e a atual.
4. Idade, estudo e trabalho do alimentando maior.
5. Valor ou percentual pretendido.

## Prazo e contagem
- Sem prazo para propor; a sentença retroage à citação, sem compensação nem devolução do que já foi pago (Súmula 621 STJ; Lei 5.478 art. 13 §2º).
- Enquanto não houver decisão, a obrigação continua: orientar o cliente a seguir pagando (o inadimplemento alimenta execução e prisão).
- Contestação e audiência: ver despacho inicial; contagem com `prazos-processuais`.

## Estrutura da peça
Endereçamento → qualificação → título revisando → situação na fixação × situação atual → direito → tutela provisória (redução/majoração liminar ou exoneração antecipada) → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Competência: foro do domicílio do alimentando (CPC 53, II), mesmo quando o autor é o devedor.
- Tramitação independente: a decisão de alimentos pode ser revista a qualquer tempo (Lei 5.478 art. 15); provisórios revistos em apartado (art. 13 §1º).
- Maioridade não extingue automaticamente: exige decisão judicial com contraditório, ainda que nos próprios autos (Súmula 358 STJ).
- Interesse de incapaz: intervenção do MP (CPC 698).

## Fundamentos verificados
CC 1.694 §1º, 1.699, 1.708; Lei 5.478 arts. 13 e 15; Súmulas 358 e 621 STJ. Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- [ ] Tutela provisória para reduzir/majorar desde logo, ou suspender a obrigação em caso de exoneração, com prova robusta do fato novo.
- [ ] Citação; intimação do MP se houver incapaz.
- [ ] Procedência para fixar o novo valor/percentual (com base de cálculo explícita) ou declarar a exoneração, com efeitos desde a citação.
- [ ] Ofício ao empregador para ajustar ou cessar o desconto em folha após a decisão.
- [ ] Gratuidade, se cabível; honorários.

## Checklist pré-protocolo
- [ ] Fato novo descrito com data e documento, posterior ao título.
- [ ] Comparativo "antes × depois" em tabela (renda e despesas).
- [ ] Na redução, prova de que o devedor não criou a própria incapacidade (pedido de demissão, renúncia a renda).
- [ ] Na exoneração por maioridade, informação sobre estudo/trabalho do filho e possibilidade de autossustento.
- [ ] Cliente orientado a continuar pagando até decisão.

## Erros a evitar
- Parar de pagar porque o filho completou 18 anos (contraria a Súmula 358 STJ).
- Pedir devolução de valores pagos a maior: a Súmula 621 veda repetição e compensação.
- Fundar a redução apenas em nova família sem demonstrar impacto real na capacidade.
- Revisional sem documentos da época da fixação (o juiz precisa comparar).
- Ajuizar no foro do autor-devedor por conveniência.

## Integração com o núcleo
`prazos-processuais`, `juros-e-correcao` (diferenças a pagar após majoração), `verificacao-de-citacoes`, `fidelidade-factual` (datas do fato novo), `estilo-forense`.

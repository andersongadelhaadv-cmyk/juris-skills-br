---
name: contratos-sla-nivel-de-servico
description: >
  Redige acordo de nível de serviço (SLA) como anexo de contrato de prestação
  de serviços — métricas objetivas, janela de medição, exclusões, créditos de
  serviço, teto, gatilho de resolução por falha reiterada — e qualifica os
  créditos à luz da cláusula penal (CC arts. 408 a 416). Use quando o usuário
  pedir SLA, acordo de nível de serviço, anexo de disponibilidade, tempo de
  resposta e solução por severidade, créditos por indisponibilidade,
  penalidade por atraso no atendimento ou revisão do SLA de um fornecedor.
metadata:
  area: contratos
  tipo_peca: contrato
  verificado_em: 2026-11-25
---
# Acordo de nível de serviço (SLA)

Ferramenta de apoio; o advogado responsável revisa todo documento antes de assinar ou enviar.

## Quando usar / quando não usar
- Usar: serviços contínuos com desempenho mensurável — software como serviço, hospedagem, suporte técnico, manutenção, facilities, logística, call center, outsourcing.
- Usar para revisar SLA do fornecedor (lado contratante) ou calibrar o próprio (lado prestador).
- Não usar: obrigação de resultado único (entrega de obra, projeto) — tratar marcos e multa no contrato principal; disputa centrada no valor da multa (`contratos-clausula-penal`); alteração de SLA em contrato vigente sem redesenho (formalizar por `contratos-aditivo-contratual`).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Contrato principal (ou minuta): objeto, preço, prazo, cláusula penal, limitação de responsabilidade, resolução.
2. Lado do cliente: contratante ou prestador.
3. Serviço e o que é "funcionar" para o negócio do contratante (quais funções são críticas).
4. Métricas desejadas e valores-alvo; histórico real de desempenho, se houver.
5. Quem mede, com qual ferramenta, onde ficam os registros, quem tem acesso.
6. Janelas de manutenção, horário de cobertura (24x7 ou horário comercial), fuso.
7. Dependências do contratante (acessos, informações, infraestrutura própria).
8. Valor mensal faturado (base dos créditos) e tolerância a teto de créditos.
9. Há dados pessoais no serviço? Quem é controlador e quem é operador?
10. Relação de consumo ou contrato empresarial paritário?

## Prazos relevantes
- Período de medição (em regra mensal) e prazo para o prestador entregar o relatório.
- Prazo para o contratante contestar a medição e para o prestador responder.
- Prazo para pleitear o crédito; consequência do silêncio (decadência convencional precisa estar escrita).
- Prazos de resposta e solução por severidade, com relógio claro (início no registro do chamado; pausa só nas hipóteses listadas).
- Gatilho de resolução: número de violações em janela móvel (ex.: 3 meses em 6).

## Estrutura do documento
Definições → serviços cobertos → métricas e metas → método de medição e fonte de dados → exclusões → relatórios e contestação → créditos de serviço e teto → falha reiterada e resolução → plano de ação corretiva → relação com cláusula penal e indenização → revisão periódica. Roteiro em [estrutura](references/estrutura.md).

Cláusulas essenciais:
- **Fórmula escrita**, com exemplo numérico. Disponibilidade = (minutos do período − minutos de indisponibilidade não excluída) ÷ minutos do período × 100. Conferir a conta por aritmética, não por estimativa.
- **Definição de indisponibilidade** (o que conta: indisponibilidade total, degradação acima de X, função crítica fora).
- **Exclusões fechadas** (lista taxativa): manutenção programada avisada com antecedência, caso fortuito ou força maior (CC art. 393), causa atribuível ao contratante.
- **Créditos**: tabela de faixas, base de cálculo (mensalidade do serviço afetado), forma (desconto na fatura seguinte) e teto.
- **Relação com outras sanções**: dizer se o crédito é a única consequência da falha de desempenho ou se convive com multa e indenização.

## Riscos e cláusulas sensíveis
- **Natureza do crédito.** Se funciona como sanção pelo atraso ou pela falha, tende a ser lido como cláusula penal moratória: não excede a obrigação principal (CC art. 412), pode ser reduzido se excessivo ou com cumprimento parcial (art. 413) e é devido sem prova de prejuízo (art. 416). A redução do art. 413 é tratada pelo STJ como norma de ordem pública, aplicável mesmo contra quem redigiu a cláusula (AREsp 2.642.072).
- **Indenização suplementar.** Prejuízo acima do crédito só é cobrável se o contrato o convencionar; nesse caso a pena vale como mínimo (art. 416, parágrafo único). Decidir de propósito e escrever.
- **Crédito como remédio exclusivo.** Bom para o prestador; para o contratante, exigir ao menos o direito de resolver por falha reiterada (gatilho objetivo, cláusula resolutiva expressa — art. 474) e a exclusão da limitação em caso de dolo ou culpa grave.
- **Medição unilateral.** Métrica medida só pelo prestador, sem acesso aos registros, esvazia o SLA. Prever acesso, auditoria e regra de desempate.
- **Exclusões abertas** ("eventos fora do controle razoável") transformam meta em promessa.
- **Paritário x consumo.** Entre empresas paritárias, a alocação de riscos é respeitada (art. 421-A). Com consumidor, é nula a cláusula que exonere ou atenue a responsabilidade do fornecedor (CDC arts. 25 e 51, I).
- **Dados pessoais e segurança.** Serviço que trata dados pessoais exige medidas de segurança e comunicação de incidente (LGPD arts. 46 e 48). Definir no SLA prazo de aviso de incidente ao contratante, distinto da disponibilidade.
- **Juros e valores.** O SLA não define juros nem correção; encargos sobre créditos não compensados vão para o núcleo `juros-e-correcao`.

## Fundamentos verificados
- CC arts. 393, 408, 409, 411, 412, 413, 416 e parágrafo único, 421-A, 474, 475.
- CDC arts. 25 e 51, I; LGPD arts. 46 e 48; Lei 13.874/2019, art. 3º, VIII.
- STJ, AREsp 2.642.072 (art. 413 como norma de ordem pública).
Detalhe em [fundamentos](references/fundamentos.md).

## Checklist antes de assinar/enviar
- [ ] Cada métrica com fórmula, unidade, período e exemplo numérico conferido
- [ ] Indisponibilidade definida; exclusões em lista fechada
- [ ] Fonte de medição, acesso aos registros e regra de contestação
- [ ] Tabela de créditos com base de cálculo e teto
- [ ] Teto dos créditos não excede o valor da obrigação principal do período (art. 412)
- [ ] Indenização suplementar: convencionada ou expressamente afastada
- [ ] Gatilho objetivo de resolução por falha reiterada
- [ ] Coerência com a limitação de responsabilidade e a cláusula penal do contrato principal
- [ ] Aviso de incidente de segurança, se houver dados pessoais
- [ ] Revisão periódica das metas prevista

## Erros a evitar
- Meta sem fórmula ("alta disponibilidade", "atendimento ágil").
- Disponibilidade de 99,9% sem dizer o período — a mesma meta tolera indisponibilidades muito diferentes por mês ou por ano.
- Relógio de solução que pausa "aguardando cliente" sem critério.
- Duas sanções para o mesmo fato (crédito e multa) sem regra de compensação.
- Copiar SLA de outro serviço com métricas que não se medem neste.

## Integração com o núcleo
`juros-e-correcao`, `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual` (números do SLA batem com o contrato principal), `estilo-forense`. Cláusula penal em profundidade: `contratos-clausula-penal`.

---
name: trabalhista-acordo-na-execucao
description: >
  Redige a petição conjunta de acordo na fase de liquidação ou execução
  trabalhista (CLT arts. 764 §3º, 831, 832 §§3º a 6º e 846 §§1º-2º), com
  discriminação da natureza das parcelas proporcional ao título (OJ 376 da
  SBDI-1), contribuição previdenciária e fiscal, custas, liberação de penhoras e
  depósitos e cláusula penal. Use quando o usuário pedir acordo na execução
  trabalhista, acordo após o trânsito em julgado, acordo depois dos cálculos
  homologados, parcelamento da dívida trabalhista em execução ou minuta de
  conciliação para encerrar a execução.
metadata:
  area: trabalhista
  tipo_peca: requerimento
  verificado_em: 2026-11-25
---
# Acordo na fase de execução trabalhista

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: processo com sentença transitada em julgado, em liquidação (cálculos apresentados ou homologados) ou em execução (citação, penhora, BacenJud/Sisbajud), em que as partes querem encerrar ou parcelar a dívida.
- Também: acordo entre exequente e responsável subsidiário ou sócio incluído na execução.
- Não usar: acordo antes da sentença ou na audiência inicial (petição de acordo comum; sem a regra do art. 832 §6º); acordo sem processo (use `trabalhista-acordo-extrajudicial`); impugnar a conta (use `trabalhista-impugnacao-de-calculos`); defesa após garantia (use `trabalhista-embargos-a-execucao`); acordo cível ou consumerista (use `consumidor-acordo-judicial`).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Título executivo (sentença, acórdãos) e certidão de trânsito; fase atual (liquidação, cálculos homologados, execução, penhora).
2. Conta de liquidação mais recente, com a separação entre parcelas salariais e indenizatórias, INSS e IR apurados, honorários e custas.
3. Valor bruto do acordo, forma (à vista, parcelas), datas, conta de destino e quem paga.
4. Depósitos recursais, depósitos judiciais, valores bloqueados e bens penhorados: o que será levantado, por quem e como abate.
5. Polo passivo na execução (devedor principal, subsidiário, sócios) e quem assina.
6. Honorários de sucumbência fixados no título e honorários periciais pendentes.
7. Obrigações de fazer ainda pendentes (anotação na CTPS, entrega de guias, PPP, retificação de eSocial).

## Prazo e contagem
- Não há prazo para conciliar: o acordo é lícito mesmo depois de encerrado o juízo conciliatório (CLT art. 764 §3º).
- Parcelas e vencimentos: escrever datas de calendário, não "30 dias após a homologação", salvo se o juízo exigir; prazos processuais em dias úteis pelo núcleo `prazos-processuais`.
- Atualização do débito até a data do acordo e encargos de parcela em atraso: sempre pelo núcleo `juros-e-correcao`; a petição não fixa índice próprio.

## Estrutura da peça
Endereçamento → identificação do processo e da fase → valor e forma de pagamento → discriminação das parcelas (natureza e proporção do título) → contribuições previdenciárias e IR (quem recolhe, base, prazo) → custas e honorários → depósitos, penhoras e bloqueios → obrigações de fazer → cláusula penal e vencimento antecipado → quitação e extinção da execução → requerimentos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Petição conjunta**, assinada pelos advogados de ambas as partes com poderes para transigir e dar quitação (conferir procurações).
- **Homologação não é direito da parte**: é faculdade do juiz (Súmula 418 do TST). Acordo com valor irrisório perto da conta homologada ou com discriminação artificial tende a ser recusado ou ajustado; justificar o deságio (risco de insolvência, prazo, garantia).
- **Discriminação da natureza** é obrigatória na homologação (CLT art. 832 §3º). Depois do trânsito, a proporção entre parcelas salariais e indenizatórias deve seguir a da condenação (OJ 376 da SBDI-1).
- **Créditos da União**: acordo após o trânsito ou após a elaboração dos cálculos não prejudica os créditos da União (art. 832 §6º); a União é intimada da homologação de acordo com parcela indenizatória (art. 832 §4º).
- **Execução de ofício das contribuições** sobre os acordos homologados (art. 876, parágrafo único).

## Fundamentos verificados
- CLT arts. 764 §3º, 831 parágrafo único, 832 §§3º, 3º-A, 3º-B, 4º e 6º, 835, 846 §§1º e 2º, 876 parágrafo único, 789 §3º.
- Lei 8.212/1991, art. 43, §§1º, 3º e 5º (acordo após decisão de mérito: contribuição calculada com base no valor do acordo; recolhimento nas mesmas datas das parcelas).
- TST: OJ 376 da SBDI-1 (proporcionalidade), Súmula 368 (recolhimento, cálculo mês a mês, IR de rendimentos acumulados), Súmula 259 (termo de conciliação só impugnável por ação rescisória), Súmula 418 (homologação como faculdade do juiz).
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Homologação do acordo nos termos da petição, com extinção da execução após o cumprimento integral.
- Liberação ao exequente dos depósitos recursais e judiciais indicados, com abatimento do valor do acordo, e devolução do saldo ao executado, se houver.
- Desbloqueio de valores e levantamento de penhoras, com ofícios, após o pagamento (ou na assinatura, se assim pactuado).
- Suspensão dos atos executórios durante o cumprimento, mantidas as constrições até a quitação, se essa for a garantia escolhida.
- Recolhimento das contribuições previdenciárias e do IR conforme a discriminação, com prazo e comprovação nos autos.
- Rateio das custas como pactuado (na falta, em partes iguais — art. 789 §3º).
- Intimação da União, se cabível.

## Checklist pré-protocolo
- [ ] Fase processual e trânsito em julgado conferidos (define a regra da proporcionalidade)
- [ ] Discriminação de parcelas respeita a proporção salarial/indenizatória do título (OJ 376)
- [ ] Base mínima das parcelas remuneratórias conferida (art. 832 §§3º-A e 3º-B)
- [ ] Responsável e prazo pelo recolhimento de INSS e IR definidos
- [ ] Depósitos, bloqueios e penhoras listados um a um, com destino
- [ ] Honorários de sucumbência e periciais tratados expressamente
- [ ] Cláusula penal e vencimento antecipado redigidos (art. 846 §2º)
- [ ] Obrigações de fazer com prazo e consequência
- [ ] Procurações com poderes para transigir, receber e dar quitação
- [ ] Atualização da conta remetida ao núcleo `juros-e-correcao`

## Erros a evitar
- Rotular todo o acordo como indenizatório depois do trânsito, contrariando a condenação: a União impugna e a homologação pode ser negada (arts. 832 §§4º e 6º; OJ 376).
- Esquecer a parcela previdenciária patronal e o IR: o juiz executa de ofício e o devedor paga duas vezes.
- Dar "quitação do extinto contrato de trabalho" sem que isso tenha sido negociado e sem que o título trate do tema; descrever a quitação com o alcance real (o objeto da execução).
- Levantar depósito recursal sem abater do acordo, ou abater sem prever quem levanta.
- Deixar sem regra o atraso de parcela (multa, vencimento antecipado, prosseguimento da execução pelo saldo).
- Ignorar os honorários de sucumbência do título: o advogado credor pode não anuir e o acordo emperra.

## Integração com o núcleo
`juros-e-correcao` (atualização até a data do acordo e encargos de atraso), `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

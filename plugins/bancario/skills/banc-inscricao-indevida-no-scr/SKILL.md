---
name: banc-inscricao-indevida-no-scr
description: >
  Redige ação de exclusão ou correção de registro no Sistema de Informações de
  Crédito do Banco Central (SCR/Sisbacen, "prejuízo", "vencido", "risco")
  cumulada com indenização, com a Res. CMN 5.037/2022 (comunicação prévia pela
  instituição credora e responsabilidade da remetente) e a jurisprudência do
  STJ que dá ao SCR caráter restritivo. Use quando o usuário pedir para tirar o
  nome do SCR, contestar "prejuízo" no Registrato, registro no Banco Central
  sem aviso, dívida já paga ou inexistente aparecendo no SCR ou crédito negado
  por causa do SCR.
metadata:
  area: bancario
  tipo_peca: inicial
  verificado_em: 2026-11-25
---
# Inscrição indevida no SCR do Banco Central

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: operação registrada no SCR com informação desabonadora (vencido, prejuízo, risco) que é inexistente, já paga, está sub judice sem a anotação devida, ou foi enviada sem comunicação prévia ao cliente.
- Não usar:
  - Negativação em Serasa, SPC ou Boa Vista: `consumidor-negativacao-indevida` (lá vale a Súmula 359; aqui não).
  - A operação nasceu de conta aberta por fraudador: combine com `banc-conta-aberta-indevidamente`.
  - Só se discute o valor da dívida ou os encargos: `consumidor-contratos-bancarios-revisional`.
  - Pedido administrativo de correção antes da ação: `banc-reclamacao-bacen-e-ouvidoria`.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Relatório do Registrato (BC) atualizado: instituição, modalidade, data-base, classificação (a vencer, vencido, prejuízo), valores.
2. Para cada registro: a dívida existe? Foi paga (data)? Está em discussão judicial (processo)?
3. Recebeu comunicação prévia por escrito da instituição sobre o registro no SCR? Quando, como, em qual endereço?
4. Pediu correção à instituição ou à ouvidoria? Protocolo e resposta.
5. Existem outras restrições legítimas (bureaus ou SCR) anteriores? (a defesa usará o raciocínio da Súmula 385).
6. Prejuízos concretos: crédito negado, limite cortado, financiamento recusado, com documentos.

## Prazo e contagem
- Prescrição: a mesma lógica da negativação. Débito inexistente com consumidor por equiparação: 5 anos do art. 27 do CDC. Débito existente e vício só na comunicação: prazo não conferido [VERIFICAR via `verificacao-de-citacoes`]. Registre datas de inclusão, de ciência e de exclusão.
- A Res. CMN 5.037/2022 obriga a instituição a guardar a comunicação prévia por cinco anos (art. 13, § 3º) — peça a exibição.
- Prazos processuais: `prazos-processuais`.

## Estrutura da peça
Fatos (Registrato) → natureza restritiva do SCR e incidência do CDC → ilicitude (débito inexistente/pago/sub judice; ou falta de comunicação prévia) → responsabilidade da instituição remetente → dano moral → tutela de urgência → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Polo passivo: a instituição que remeteu os dados (originadora ou adquirente). Não é o Banco Central: as informações são de exclusiva responsabilidade das remetentes (Res. CMN 5.037/2022, art. 15).
- Separar as duas teses, porque o STJ trata de modo diferente:
  - Débito inexistente: dano moral presumido mais estável.
  - Débito existente, só sem comunicação prévia: há julgados que indenizam (REsp 2.242.278; AREsp 3.126.949) e julgado que nega (AREsp 3.079.630). Avise o cliente do risco.

## Fundamentos verificados
- CDC arts. 6º VIII, 14, 17, 27, 43 §§ 2º e 3º.
- Res. CMN 5.037/2022: art. 13 (comunicação prévia ao cliente, antes da remessa, guardada por 5 anos), art. 15 (responsabilidade exclusiva da remetente por inclusão, correção, exclusão, identificação de operação sub judice e registro de discordância), art. 16 (orientação sobre correção e discordância).
- REsp 2.242.278 (3ª Turma, 2026): notificação prévia ao SCR cabe à credora; Súmula 359 não se aplica; anuência genérica no contrato não supre; dano in re ipsa.
- AREsp 3.126.949 (4ª Turma, 2026): falta de notificação no SCR, sem inscrição legítima anterior, gera dano in re ipsa.
- AREsp 2.970.756 (3ª Turma, 2026) e AREsp 2.898.289 (3ª Turma, 2025): SCR com natureza restritiva; inscrição indevida gera dano moral.
- Contraponto: AREsp 3.079.630 (3ª Turma, 2026): existindo o débito, a falta de notificação não autoriza dano moral.
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Tutela de urgência: ordem à instituição remetente para excluir ou corrigir o registro (ou anotar "sub judice"/discordância) no SCR, com prazo e multa.
- Declaração de inexistência ou inexigibilidade do débito, quando for o caso.
- Exclusão definitiva ou correção do registro.
- Dano moral; juros e correção pelo núcleo `juros-e-correcao`.
- Exibição da comunicação prévia (art. 13, § 3º) e do histórico de remessas; inversão do ônus.

## Checklist pré-protocolo
- [ ] Registrato recente juntado, com cada registro classificado
- [ ] Tese escolhida (débito inexistente x falta de comunicação) e risco explicado
- [ ] Réu é a remetente, não o BC
- [ ] Outras restrições levantadas e enfrentadas
- [ ] Pedido de exibição da comunicação prévia
- [ ] Prescrição conferida
- [ ] Juros e correção remetidos ao núcleo

## Erros a evitar
- Citar a Súmula 359 (mantenedor notifica) para o SCR: o STJ atribui o dever à credora.
- Processar o Banco Central.
- Pedir indenização por falta de notificação sem avisar que há julgado contrário quando a dívida existe.
- Confundir registro "a vencer" (cadastro positivo) com registro desabonador.

## Integração com o núcleo
`juros-e-correcao`, `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

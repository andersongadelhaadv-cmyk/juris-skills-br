---
name: banc-reclamacao-bacen-e-ouvidoria
description: >
  Redige a reclamação formal à ouvidoria da instituição financeira (Res. CMN
  4.860/2020: protocolo e resposta em até 10 dias úteis) e a reclamação ao
  Banco Central contra banco, financeira ou instituição de pagamento, com
  narrativa, pedidos e provas organizados para servir também de prova em ação
  futura. Use quando o usuário pedir para reclamar do banco no Banco Central,
  escrever para a ouvidoria, escalar um problema que o SAC não resolveu,
  registrar discordância de dado no SCR ou documentar a recusa do banco antes
  de processar.
metadata:
  area: bancario
  tipo_peca: requerimento
  verificado_em: 2026-11-25
---
# Reclamação à ouvidoria e ao Banco Central

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: o atendimento primário (agência, aplicativo, SAC, correspondente) não resolveu e é preciso (a) escalar à ouvidoria da instituição e/ou (b) registrar reclamação no Banco Central; também para pedir correção ou registro de discordância de dado no SCR.
- Não usar:
  - Pedido urgente de devolução de Pix: `banc-med-pix-devolucao` (a ouvidoria entra em paralelo, não antes).
  - Ação judicial: `banc-fraude-pix-e-transferencia-nao-autorizada`, `banc-conta-aberta-indevidamente`, `banc-inscricao-indevida-no-scr`, `banc-repeticao-de-indebito-bancario`.
  - Notificação extrajudicial com efeitos contratuais (constituição em mora, resolução): `contratos-notificacao-de-descumprimento`.
  - Seguros, previdência privada, investimentos em valores mobiliários: órgão regulador diverso [VERIFICAR: canal do regulador competente].

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Instituição exata (razão social, CNPJ se possível) e produto (conta, cartão, empréstimo, Pix, consignado).
2. O problema em uma frase e a linha do tempo com datas.
3. Protocolos do atendimento primário (SAC, chat, agência) e o que responderam.
4. Documentos: extratos, contratos, comprovantes, prints, BO.
5. O que o cliente quer exatamente (estorno de R$ X, cancelamento, exclusão de registro, cópia de contrato, explicação).
6. Já houve reclamação na ouvidoria? Número e data; venceu o prazo de resposta?

## Prazo e contagem
- Ouvidoria: resposta conclusiva em até 10 dias úteis, prorrogável uma única vez, excepcionalmente e com justificativa (Res. CMN 4.860/2020, art. 6º, § 2º). Conte a partir do protocolo; anote o vencimento.
- Reclamação ao BC não suspende nem interrompe prescrição [VERIFICAR antes de afirmar ao cliente qualquer efeito sobre prazos]; o prazo da ação corre em paralelo (ver a skill da ação e `prazos-processuais`).

## Estrutura da peça
Identificação → instituição e produto → protocolos anteriores → fatos em ordem cronológica → o que está errado (norma ou contrato, sem excesso) → pedido objetivo e mensurável → documentos → pedido de resposta por escrito. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Ordem: atendimento primário → ouvidoria (última instância interna, art. 3º, I) → Banco Central. A ouvidoria pode receber, excepcionalmente, demanda que não passou pelo primário (art. 6º, § 1º, III, "a") — mas registre o primário sempre que possível.
- A ouvidoria deve fornecer número de protocolo (art. 6º, § 1º, I) e o acesso é gratuito (art. 7º, III).
- Reclamação ao BC: feita pelos canais oficiais do Banco Central [VERIFICAR: caminho atual do serviço no site do BC]; o BC encaminha à instituição, que a ouvidoria também atende (art. 6º, § 1º, III, "b"). O BC não decide o caso individual nem condena a pagar.
- Escrever para leitor que não conhece o caso: curto, datado, com valores e anexos numerados.

## Fundamentos verificados
- Res. CMN 4.860/2020: art. 3º (finalidade da ouvidoria: última instância e mediação), art. 6º (atribuições; protocolo; demandas encaminhadas pelo BC; prazo de 10 dias úteis), art. 7º, III (acesso gratuito).
- Res. CMN 4.949/2021: art. 3º (tratamento justo e equitativo, considerando vulnerabilidades) e art. 4º (segurança, legitimidade das operações, informação clara).
- SCR: Res. CMN 5.037/2022, art. 15, II e V (correção, exclusão e registro de discordância são responsabilidade da remetente) e art. 16, III.
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos (modelo)
- Providência concreta e mensurável (estornar R$ X em até N dias; excluir o registro Y do SCR; encerrar a conta Z; fornecer cópia do contrato W).
- Resposta conclusiva por escrito, no prazo regulamentar, com fundamento.
- Cópia das gravações e registros do atendimento.
- Indicação expressa de que a resposta será usada como prova.

## Checklist pré-envio
- [ ] Protocolos do atendimento primário listados
- [ ] Pedido único, claro e com valor
- [ ] Anexos numerados e citados no texto
- [ ] Data de vencimento da resposta anotada (10 dias úteis)
- [ ] Prazo prescricional da ação conferido e não dependente da reclamação
- [ ] Sem dados sensíveis desnecessários (senhas, fotos de documento além do exigido)

## Erros a evitar
- Texto longo e emotivo sem pedido objetivo: a resposta vem genérica.
- Pular o protocolo do SAC e perder a prova da tentativa prévia.
- Prometer ao cliente que o BC fará o banco pagar.
- Esperar a ouvidoria enquanto o dinheiro sai da conta de destino (Pix): acione o MED já.

## Integração com o núcleo
`prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

---
name: banc-med-pix-devolucao
description: >
  Prepara o requerimento ao banco para acionar o Mecanismo Especial de
  Devolução (MED) do Pix e o bloqueio de valores na conta de destino, com base
  no Regulamento anexo à Resolução BCB 1/2020 (arts. 39-B, 41-B a 41-F),
  mais a notificação que documenta o pedido para uma ação futura. Use quando o
  usuário caiu em golpe ou teve Pix não autorizado e quer pedir a devolução
  pelo banco, saber o que é o MED, cobrar a resposta do banco que não acionou
  o mecanismo ou provar que pediu o bloqueio a tempo.
metadata:
  area: bancario
  tipo_peca: requerimento
  verificado_em: 2026-11-25
---
# MED do Pix: requerimento de devolução e bloqueio

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: logo após Pix fraudulento (golpe, conta invadida, Pix não reconhecido) ou falha operacional, para pedir ao banco do pagador que acione o MED e registrar o pedido por escrito.
- Não usar:
  - Ação judicial de restituição e indenização: `banc-fraude-pix-e-transferencia-nao-autorizada` (use este requerimento como prova).
  - Arrependimento de compra ou briga com o vendedor sobre o produto: o MED exclui controvérsia do negócio subjacente; ver `consumidor-vicio-do-produto-ou-servico`.
  - Reclamação regulatória contra o banco que não respondeu: `banc-reclamacao-bacen-e-ouvidoria`.
  - Notícia-crime contra o golpista: `digital-crime-cibernetico`.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Comprovante de cada Pix: data, hora, valor, identificador da transação (ID/E2E), nome e instituição do recebedor, chave usada.
2. O que aconteceu (golpe com transferência feita pelo cliente; Pix feito por terceiro com acesso indevido; erro operacional do banco).
3. Quando o cliente percebeu e se já contestou pelo aplicativo ou SAC (protocolos, prints).
4. Boletim de ocorrência.
5. Resposta do banco, se houve (recusa, "sem saldo", devolução parcial).

## Prazo e contagem
- Urgência real: o MED só recupera o que ainda houver na conta de destino; cada hora conta.
- Os prazos de contestação pelo usuário, de manutenção do bloqueio e de concretização da devolução não estão no corpo do regulamento: o art. 41-E remete ao Manual Operacional do DICT [VERIFICAR: prazos vigentes na data do fato, no site do Banco Central].
- O regulamento tem alterações frequentes (inclusive Res. BCB 603/2026, com efeitos a partir de 1º/7/2027) [VERIFICAR: redação vigente na data do Pix].
- Prazos processuais da ação posterior: `prazos-processuais`.

## Estrutura da peça
Identificação do cliente e da conta → descrição de cada Pix (tabela) → fato (fraude/falha) e data da ciência → pedido expresso de acionamento do MED e de notificação de infração → pedido de informação sobre o resultado e o saldo bloqueado → protocolo, prazo de resposta e reserva de direitos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Destinatário: o banco do pagador (quem solicita a devolução pelo DICT, art. 41-C, II); cópia ao banco recebedor quando identificado.
- Hipóteses do MED (art. 41-B): fundada suspeita de fraude; falha operacional; casos do Pix Automático. Excluídos: controvérsia do negócio subjacente e recursos em conta de terceiro de boa-fé (art. 41-B, § 1º).
- A devolução depende de notificação de infração aceita pelo banco recebedor e alcança o valor ou o saldo disponível (art. 41-D). MED não garante ressarcimento.

## Fundamentos verificados
- Regulamento anexo à Res. BCB 1/2020: art. 39-B (bloqueio cautelar por suspeita de fraude, simultâneo ao crédito, até 72 horas), art. 39-C (critérios mínimos de avaliação de fraude definidos pelo BC), art. 41-B, 41-C, 41-D, 41-E e 41-F.
- Res. CMN 4.860/2020, art. 6º, §§ 1º e 2º (protocolo e resposta da ouvidoria em até 10 dias úteis), se o SAC falhar.
- Exemplos estaduais (não vinculantes): TJBA reconheceu falha do banco por inércia no MED após comunicação tempestiva; TJDFT mandou o banco de destino restituir valor retido via MED; TJTO afirmou que o MED não garante ressarcimento automático.
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Acionamento imediato do MED para cada transação, com abertura de notificação de infração.
- Informação por escrito: data e hora do acionamento, resposta do banco recebedor, valor bloqueado, valor devolvido.
- Bloqueio cautelar e devoluções parciais até o valor total, nos limites do regulamento.
- Cópia dos registros do atendimento e número de protocolo.
- Reserva de direitos (restituição e indenização em juízo).

## Checklist pré-protocolo
- [ ] ID/E2E de cada Pix e dados do recebedor
- [ ] Data e hora da ciência e do primeiro aviso, com provas
- [ ] BO anexado
- [ ] Enviado por canal que gere protocolo (app, SAC, e-mail com confirmação, ouvidoria)
- [ ] Prazos do Manual do DICT conferidos na data do fato
- [ ] Cliente informado de que o MED depende de saldo e não é garantia

## Erros a evitar
- Esperar a resposta do banco para registrar o BO ou a ouvidoria: faça em paralelo.
- Pedir MED para disputa comercial com vendedor real (excluída pelo art. 41-B, § 1º, I).
- Afirmar prazo de dias "do MED" de memória: está no Manual do DICT e muda.
- Tratar a negativa do MED como fim do caminho: ela abre a discussão de falha na ação própria.

## Integração com o núcleo
`prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

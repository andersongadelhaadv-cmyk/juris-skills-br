---
name: saude-notificacao-extrajudicial-plano-de-saude
description: >
  Redige notificação extrajudicial do beneficiário à operadora de plano de
  saúde para exigir autorização de procedimento, resposta escrita e
  fundamentada à negativa, reembolso de despesas, indicação de prestador da
  rede ou reversão de cancelamento, constituindo prova do requerimento antes da
  ação, com base na Lei 9.656/1998 e nas regras de atendimento da ANS (RN
  623/2024). Use quando o usuário pedir notificação ao plano de saúde, carta ao
  convênio, pedido formal de cobertura, pedido de negativa por escrito,
  cobrança de reembolso atrasado, contestação de cancelamento ou reclamação na
  ouvidoria da operadora antes de processar.
metadata:
  area: saude
  tipo_peca: notificacao
  verificado_em: 2026-11-25
---
# Notificação extrajudicial à operadora de plano de saúde

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: antes da ação, para (a) pedir formalmente cobertura e fixar a data do requerimento; (b) exigir a negativa por escrito e fundamentada; (c) cobrar reembolso não pago ou pago a menor; (d) pedir indicação de prestador apto na rede; (e) contestar cancelamento ou suspensão e oferecer o pagamento; (f) pedir cópia do contrato, da tabela de reembolso e da lista de credenciados.
- Não usar: **urgência ou emergência com risco atual** — não espere resposta; vá direto à tutela (`consumidor-plano-de-saude`; `saude-rescisao-unilateral-plano-de-saude` se o plano foi cancelado). Notificação entre empresas por descumprimento contratual comum: `contratos-notificacao-de-descumprimento`. Notificação por incidente de dados pessoais: `digital-notificacao-de-incidente-lgpd`.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Beneficiário e titular (nome, carteirinha, CPF só no original enviado, nunca em exemplo), tipo de contrato, operadora e administradora, se houver.
2. Objetivo único da notificação (uma notificação por objetivo principal).
3. Prescrição e relatório médico; orçamento; data em que o tratamento é necessário.
4. Histórico com a operadora: protocolos, datas, nomes de atendentes, respostas.
5. Para reembolso: notas, comprovantes, data da entrega dos documentos.
6. Para cancelamento: carta de cancelamento, extrato de pagamentos, oferta de pagamento.
7. Canal disponível: canal virtual da operadora com protocolo, e-mail cadastrado, endereço da sede para carta com AR, cartório.

## Prazo e contagem
- Prazos de resposta da operadora segundo a cartilha oficial da ANS sobre a RN 623/2024 (set/2025): urgência/emergência, resposta imediata; procedimentos de alta complexidade e internação eletiva, até 10 dias úteis; demais consultas, exames e internações, até 5 dias úteis; demandas não assistenciais (boleto, reajuste, cadastro), até 7 dias úteis; ouvidoria, até 7 dias úteis do requerimento [VERIFICAR: conferir os artigos no texto da RN 623/2024 antes de citá-los]. Esses prazos são de **resposta**, não de realização do procedimento.
- Reembolso: a lei fixa pagamento em até 30 dias da entrega da documentação adequada (Lei 9.656/1998, art. 12, VI).
- Cancelamento por inadimplência de plano individual: a operadora precisa ter notificado até o 50º dia de atraso (art. 13, p.ú., II) — a contranotificação deve apontar a data.
- Prazo fixado na notificação: razoável e compatível com o quadro clínico; não invente prazo "legal" diferente dos acima. Contagem processual posterior: `prazos-processuais`.

## Estrutura da peça
Qualificação → contrato → fatos e protocolos anteriores → pedido certo → fundamento resumido → prazo → advertência (ouvidoria, ANS, ação judicial) → anexos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Prova de entrega é o objetivo.** Use o canal que gera protocolo e guarde o número; em paralelo, e-mail com confirmação ou carta com AR. Notificação sem prova de recebimento não serve como prova do requerimento.
- **Peça a negativa por escrito.** Pela cartilha da ANS, a recusa deve vir por escrito, fundamentada, em formato que permita impressão ou download, indicando o contato da ouvidoria. A negativa escrita é o documento-chave da futura tutela.
- **Um pedido claro e executável:** autorizar o procedimento X no prestador Y até a data Z; pagar R$ X de reembolso; restabelecer o contrato e emitir boleto.
- **Tom técnico, sem ameaça desproporcional.** Mencionar ouvidoria, reclamação à ANS (com o protocolo da operadora) e medida judicial é legítimo; multa ou indenização "prefixada" na notificação não é.
- Dados de saúde: envie só o necessário ao pedido; relatório médico completo vai como anexo para a área técnica, não no corpo.

## Fundamentos verificados
- Lei 9.656/1998: art. 12, V, "c" (24 horas de carência em urgência/emergência) e VI (reembolso em 30 dias); art. 13, p.ú., II e III (cancelamento de plano individual); art. 35-C (cobertura obrigatória de emergência e urgência).
- CDC: art. 6º, III (informação adequada e clara) e art. 47.
- RN ANS 623/2024 — regras de atendimento e prazos de resposta, conferidos na cartilha oficial da ANS [VERIFICAR: artigos].
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos (conteúdo mínimo da notificação)
- Identificação do contrato, do beneficiário e dos protocolos anteriores.
- O pedido, com prazo de cumprimento e forma (autorização escrita, guia, depósito em conta indicada).
- Em caso de recusa: resposta escrita, fundamentada, com a cláusula contratual ou o dispositivo legal invocado.
- Exibição de documentos: contrato, tabela de reembolso, lista de credenciados aptos na especialidade e no município.
- Ressalva de direitos e indicação dos próximos passos (ouvidoria, ANS, ação com tutela).

## Checklist pré-envio
- [ ] Objetivo único e pedido executável
- [ ] Protocolos anteriores listados com data
- [ ] Prazo coerente com o quadro clínico e com os prazos de resposta da ANS
- [ ] Pedido expresso de negativa por escrito e fundamentada
- [ ] Anexos: prescrição, relatório, orçamento, comprovantes
- [ ] Canal com prova de entrega definido (protocolo + AR ou e-mail)
- [ ] Caso urgente redirecionado para tutela, sem esperar resposta

## Erros a evitar
- Notificar em vez de ajuizar quando há risco atual à vida ou à saúde.
- Enviar só por telefone ou WhatsApp sem protocolo nem registro.
- Misturar vários pedidos sem prioridade e sem prazo.
- Citar artigo de resolução da ANS sem conferir o texto vigente.
- Expor diagnóstico além do necessário no corpo da carta.

## Integração com o núcleo
`prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`. Depois da resposta: `consumidor-plano-de-saude`, `saude-reembolso-plano-de-saude` ou `saude-rescisao-unilateral-plano-de-saude`.

---
name: consumidor-notificacao-extrajudicial
description: >
  Redige notificação extrajudicial do consumidor ao fornecedor (reclamação
  formal, pedido de cancelamento, contestação de cobrança, exigência de
  cumprimento de oferta), com efeito de obstar a decadência do art. 26, § 2º,
  I, do CDC, e com base nos arts. 30, 35, 42 e 84 do CDC e nos arts. 20 e 21
  do Decreto 13.135/2026 (SAC). Use quando o usuário pedir notificação ao
  fornecedor, carta de reclamação formal, pedido de cancelamento que a empresa
  não processa, contestação de cobrança indevida, exigir a oferta anunciada ou
  constituir prova antes de ajuizar ação de consumo.
metadata:
  area: consumidor
  tipo_peca: notificacao
  verificado_em: 2026-11-25
---
# Notificação extrajudicial consumerista

Ferramenta de apoio; o advogado responsável revisa toda peça antes do envio.

## Quando usar / quando não usar
- Usar, do lado do consumidor: (a) reclamação formal de vício, para obstar a decadência; (b) pedido de cancelamento de serviço não processado; (c) contestação de cobrança indevida ou de serviço não solicitado; (d) exigência de cumprimento de oferta ou publicidade; (e) pedido de documentos (contrato, gravação, faturas) e de solução antes da ação.
- Não usar:
  - Desistência em 7 dias de compra fora do estabelecimento: `consumidor-direito-de-arrependimento` (tem notificação própria).
  - Vício de produto já com ação em vista: a reclamação prévia está também em `consumidor-vicio-do-produto-ou-servico`; use esta skill quando só a carta for pedida.
  - Notificação de mora entre empresas ou em contrato civil: `contratos-notificacao-de-descumprimento`.
  - Locação ou condomínio: `imob-notificacao-extrajudicial-imobiliaria`.
  - Incidente de dados pessoais: `digital-notificacao-de-incidente-lgpd`.
  - Resposta do fornecedor a notificação recebida: tratar como estratégia de defesa (`consumidor-defesa-do-fornecedor`).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Notificante e notificado: razão social e CNPJ do fornecedor; endereço da sede ou canal oficial (SAC, e-mail de ouvidoria).
2. Produto ou serviço, número do contrato/pedido/protocolo, data da compra ou da entrega.
3. O problema, em ordem cronológica, com protocolos de atendimento já abertos e respostas recebidas.
4. O que o cliente quer: conserto, troca, abatimento, restituição, cancelamento, cumprimento da oferta, estorno.
5. Valores envolvidos e prova de pagamento.
6. Prova da oferta (anúncio, print, folheto) quando for o caso.
7. Meio de envio disponível e preferido (carta com AR, cartório de títulos e documentos, e-mail com confirmação, canal do SAC).

## Prazo e contagem
- Vício aparente: decadência de 30 dias (serviço e produto não duráveis) ou 90 dias (duráveis), da entrega ou do fim do serviço; vício oculto, de quando ficar evidenciado (art. 26, I, II, §§ 1º e 3º).
- A reclamação comprovada obsta a decadência até a resposta negativa inequívoca (art. 26, § 2º, I): por isso a notificação deve sair dentro do prazo e ter prova de recebimento.
- SAC: resposta em até 7 dias corridos; cobrança indevida ou serviço não solicitado exige suspensão em até 48 horas (Decreto 13.135/2026, art. 21, caput e § 3º).
- Prazo dado ao fornecedor na carta: razoável e compatível com a lei (não inferior aos prazos legais do fornecedor). Prazos processuais: `prazos-processuais`.

## Estrutura da peça
Qualificação → fatos com datas e protocolos → fundamento legal enxuto → pedido certo e prazo → consequências (ação judicial, Procon, consumidor.gov.br, inversão do ônus, repetição em dobro) → meio de resposta → local, data, assinatura. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Destinatário certo: sede ou canal oficial do fornecedor; em cadeia de fornecimento, notificar todos os que serão réus (comerciante e fabricante).
- Prova do envio e do recebimento é o objetivo principal: AR, cartório, ou protocolo do SAC com número e comprovante eletrônico.
- Tom técnico e sem ameaça desproporcional: a carta tende a ser juntada pelos dois lados no processo.
- Não confessar fatos desfavoráveis nem renunciar a direitos (ex.: "aceito o conserto em qualquer prazo").

## Fundamentos verificados
- CDC art. 26, I, II, §§ 1º, 2º, I, e 3º (decadência e obstação pela reclamação).
- CDC arts. 30 e 35 (oferta vincula; cumprimento forçado, equivalente ou rescisão com restituição).
- CDC art. 42, parágrafo único (repetição em dobro, salvo engano justificável); art. 39, V (vantagem manifestamente excessiva).
- CDC art. 6º, III (informação) e VIII (inversão do ônus).
- Decreto 13.135/2026 (SAC), art. 20, § 1º (cancelamento pelos mesmos canais da contratação, efeitos imediatos, comprovante eletrônico) e art. 21 (7 dias; 48 horas para cobrança indevida).
- Decreto 7.962/2013, art. 4º, V (atendimento eletrônico para reclamação e cancelamento no comércio eletrônico).
- CC art. 397, parágrafo único (sem termo, mora por interpelação).
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos (conteúdo da notificação)
- Providência específica e mensurável (ex.: "cancelar o contrato n. X com efeitos a partir do pedido de DD/MM, cessar as cobranças e estornar R$ Y").
- Prazo para cumprimento e para resposta por escrito.
- Envio de documentos: contrato, gravações, faturas, laudo técnico.
- Advertência de que, sem solução, serão adotadas as medidas judiciais e administrativas cabíveis, inclusive repetição em dobro (art. 42) e indenização.

## Checklist pré-envio
- [ ] Dados do fornecedor conferidos (CNPJ, endereço ou canal oficial)
- [ ] Cronologia com datas e protocolos
- [ ] Prazo decadencial calculado e notificação dentro dele
- [ ] Pedido certo, com valor e prazo
- [ ] Meio de envio com prova de recebimento definido
- [ ] Sem confissão nem renúncia indevida
- [ ] Cópia guardada com o comprovante de envio

## Erros a evitar
- Enviar só por WhatsApp ou chat sem protocolo: difícil provar o recebimento e o conteúdo.
- Notificar depois de vencido o prazo decadencial, achando que a carta "reabre" o prazo.
- Pedir genericamente "providências": sem pedido certo, não há recusa clara a provar.
- Usar a notificação de arrependimento (art. 49) para compra feita na loja física.
- Ameaçar com "danos morais de R$ X": compromete a estratégia e o valor da causa.

## Integração com o núcleo
`prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`. Valores a restituir: `juros-e-correcao`.

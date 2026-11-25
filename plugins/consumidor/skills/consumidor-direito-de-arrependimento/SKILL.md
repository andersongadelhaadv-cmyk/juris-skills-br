---
name: consumidor-direito-de-arrependimento
description: >
  Redige a notificação de arrependimento e a ação de restituição quando o
  fornecedor recusa a desistência em compra feita fora do estabelecimento
  comercial (internet, telefone, aplicativo, domicílio, estande de vendas), com
  base no art. 49 do CDC, nos arts. 4º e 5º do Decreto 7.962/2013 e, em
  multipropriedade e imóvel em estande, no art. 67-A, §§ 10 e 11, da Lei
  4.591/1964. Use quando o usuário pedir devolução de compra online em 7 dias,
  cancelamento de compra pela internet, estorno no cartão, desistência de
  contrato assinado em estande, hotel ou evento, ou loja que recusa a devolução.
metadata:
  area: consumidor
  tipo_peca: inicial
  verificado_em: 2026-11-25
---
# Direito de arrependimento (CDC, art. 49)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: contrato celebrado fora do estabelecimento comercial (comércio eletrônico, telefone, domicílio, abordagem em hotel/evento, estande de vendas) e desistência manifestada em 7 dias da assinatura ou do recebimento do produto/serviço.
- Usar a notificação extrajudicial como primeira peça; a inicial quando houver recusa, retenção de valores ou cobrança mantida no cartão.
- Não usar: compra presencial na loja sem defeito (não há direito legal de troca por arrependimento); produto com defeito (`consumidor-vicio-do-produto-ou-servico`); dano causado pelo produto (`consumidor-acao-indenizatoria`).
- Distrato de imóvel fora do prazo de 7 dias: `imob-distrato-imobiliario`.
- Cobrança mantida e paga após o arrependimento: cumular com `consumidor-repeticao-em-dobro`; negativação decorrente: `consumidor-negativacao-indevida`.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Canal da contratação (site, app, telefone, porta a porta, estande, evento) e prova disso.
2. Data da contratação e data do recebimento do produto ou do início do serviço.
3. Data e meio da manifestação de arrependimento (protocolo, e-mail, chat, carta com AR) e resposta do fornecedor.
4. Valores pagos (sinal, parcelas, frete, taxas, comissão de corretagem) e forma de pagamento (cartão, Pix, boleto, financiamento).
5. Situação do produto: devolvido? Coletado? Recusado pelo fornecedor? Por qual motivo?
6. Há contrato acessório (financiamento, seguro, garantia estendida)?

## Prazo e contagem
- Arrependimento: 7 dias contados da assinatura ou do ato de recebimento do produto ou serviço (CDC art. 49). Registrar as duas datas e usar a mais favorável quando o texto permitir.
- Estande de vendas / fora da sede do incorporador: 7 dias, improrrogáveis; prova por carta registrada com AR, valendo a data da postagem (Lei 4.591/1964, art. 67-A, §§ 10 e 11).
- Prazo de direito material, contado em dias corridos [VERIFICAR: forma de contagem do prazo do art. 49 não conferida em fonte oficial]. Prazos processuais: `prazos-processuais`.

## Estrutura da peça
Notificação → (se recusada) inicial: fatos → contratação fora do estabelecimento → exercício tempestivo → restituição imediata e corrigida → extinção dos acessórios e estorno → (eventual) dano moral → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- O arrependimento é potestativo: não exige motivo nem defeito.
- O fornecedor deve oferecer meio eficaz, inclusive pela mesma ferramenta da contratação, e confirmar imediatamente o recebimento (Decreto 7.962/2013, art. 5º, caput, §§ 1º e 4º).
- O arrependimento rescinde os contratos acessórios sem ônus (art. 5º, § 2º) e obriga o fornecedor a comunicar a administradora do cartão para não lançar ou estornar (art. 5º, § 3º): incluir a administradora no polo passivo só se ela manteve a cobrança após ciência.
- Juizado Especial: verificar valor e complexidade (`civel-juizado-especial`).

## Fundamentos verificados
- CDC art. 49 e parágrafo único (restituição imediata, monetariamente atualizada, dos valores pagos no prazo de reflexão); arts. 6º, III e VIII.
- Decreto 7.962/2013, arts. 4º e 5º.
- Lei 4.591/1964, art. 67-A, §§ 10 e 11 (estande de vendas; devolução integral, inclusive corretagem).
- Julgados estaduais ilustrativos (não vinculantes): TJTO, Ap. 0015021-34.2024.8.27.2722; TJBA, AI 8062810-83.2025.8.05.0000; TJBA, RI 0086529-09.2020.8.05.0001.
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Declaração da resolução do contrato pelo exercício do arrependimento.
- Restituição integral e imediata dos valores pagos (incluir frete e taxas, se pagos), com correção e juros pelo núcleo `juros-e-correcao`.
- Ordem de cancelamento/estorno no cartão e extinção dos contratos acessórios.
- Tutela de urgência para suspender cobranças futuras, se houver parcelas a vencer.
- Recolhimento do produto às custas do fornecedor, se ainda não coletado.
- Dano moral só com fato concreto além da recusa (ver Erros a evitar).
- Inversão do ônus (art. 6º, VIII).

## Checklist pré-protocolo
- [ ] Contratação fora do estabelecimento provada (pedido, e-mail, contrato, local)
- [ ] Datas de contratação, recebimento e arrependimento comprovadas
- [ ] Prova do meio usado para desistir e da resposta (ou silêncio)
- [ ] Planilha de valores pagos (inclusive frete/corretagem)
- [ ] Contratos acessórios identificados
- [ ] Notificação prévia enviada (ou motivo de não ter sido)
- [ ] Juros/correção remetidos ao núcleo

## Erros a evitar
- Invocar o art. 49 em compra feita dentro da loja física.
- Perder o prazo por contar só a partir da assinatura quando o recebimento foi posterior (ou vice-versa).
- Aceitar condição do fornecedor (embalagem original, produto lacrado, multa) como requisito legal sem examinar o caso: o art. 49 não prevê essas condições, mas o uso indevido do produto pode ser discutido pela defesa.
- Pedir dano moral pela simples recusa: há julgado negando-o nessa situação (TJBA, RI 0086529-09.2020.8.05.0001).
- Em multipropriedade/estande, aplicar o regime do distrato (retenção) a desistência feita dentro dos 7 dias.

## Integração com o núcleo
`juros-e-correcao`, `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

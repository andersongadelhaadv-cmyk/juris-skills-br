---
name: imob-notificacao-extrajudicial-imobiliaria
description: >
  Redige notificações extrajudiciais imobiliárias: denúncia de locação
  residencial ou não residencial (Lei 8.245/1991), denúncia pelo adquirente do
  imóvel locado, oferta do direito de preferência, interpelação do promitente
  comprador para constituição em mora (Decreto-Lei 745/1969 e art. 32 da Lei
  6.766/1979) e notificação de condômino infrator (arts. 1.336 e 1.337 do CC).
  Use quando o usuário pedir notificação para desocupar imóvel, aviso de
  retomada, notificação de venda ao inquilino, interpelação de comprador em
  atraso no compromisso de compra e venda ou advertência formal a condômino.
metadata:
  area: imobiliario
  tipo_peca: notificacao
  verificado_em: 2026-11-25
---
# Notificação extrajudicial imobiliária

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: (a) denúncia de locação (vazia ou cheia) pelo locador ou pelo locatário; (b) denúncia pelo adquirente do imóvel locado; (c) comunicação do direito de preferência ao locatário; (d) interpelação do promitente comprador inadimplente, como condição da resolução; (e) advertência a condômino por infração ou comportamento antissocial.
- Não usar: notificação de descumprimento de contrato empresarial genérico (`contratos-notificacao-de-descumprimento`); redação ou revisão do contrato de locação comercial (`contratos-locacao-comercial`); distrato de compra de imóvel (`imob-distrato-imobiliario`); ação de despejo (`imob-acao-de-despejo`); cobrança de cotas condominiais (`imob-cobranca-de-taxas-condominiais`); ação de resolução já proposta (`civel-peticao-inicial`); adquirente de lote em loteamento irregular (`imob-loteamento-irregular-defesa-do-adquirente`); unidade em incorporação imobiliária (`imob-incorporacao-imobiliaria`); alienação fiduciária de imóvel (fora do escopo desta skill).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Tipo de relação: locação (residencial / não residencial), promessa de compra e venda (imóvel loteado ou não), condomínio edilício.
2. Contrato ou convenção: data, prazo, cláusulas de vigência, resolutiva expressa, multa; se está registrado/averbado na matrícula.
3. Partes completas e **endereço onde o notificado será efetivamente encontrado** (contratual, do imóvel, atual).
4. Locação: data de início, prazo original, se houve prorrogação, tempo total ininterrupto, motivo da retomada (se houver).
5. Promessa: parcelas vencidas (datas e valores nominais), se o imóvel integra loteamento registrado.
6. Condomínio: fato concreto, data, dispositivo da convenção/regimento violado, advertências anteriores, ata de assembleia (se multa do art. 1.337).
7. Meio de envio pretendido: Registro de Títulos e Documentos, Registro de Imóveis (loteamento), via judicial, carta com AR.

## Prazo e contagem
- Os prazos abaixo são de direito material e constam da lei; confira sempre o termo inicial (recebimento da notificação, registro da venda, termo do contrato).
- Locação residencial com prazo ≥ 30 meses prorrogada: denúncia a qualquer tempo, com 30 dias para desocupar (Lei 8.245, art. 46, § 2º).
- Locação residencial com prazo < 30 meses prorrogada: retomada só nas hipóteses do art. 47 (inclusive vigência ininterrupta superior a cinco anos, inciso V).
- Não residencial por prazo indeterminado: 30 dias para desocupar (art. 57). Para liminar no despejo (art. 59, § 1º, VIII), a ação deve vir em até 30 dias do termo do contrato ou do cumprimento da notificação.
- Adquirente do imóvel locado: denunciar em 90 dias do registro da venda ou do compromisso, concedendo 90 dias para desocupar (art. 8º, caput e § 2º).
- Direito de preferência: o locatário tem 30 dias para aceitar integralmente a proposta (arts. 27 e 28).
- Denúncia pelo locatário (prazo indeterminado): aviso com 30 dias de antecedência (art. 6º).
- Promitente comprador de imóvel não loteado: 15 dias, contados do recebimento da interpelação, para purgar a mora (DL 745/1969, art. 1º).
- Promitente comprador de lote: 30 dias depois de constituído em mora, com intimação pelo Oficial do Registro de Imóveis (Lei 6.766, art. 32, caput e § 1º).
- Prazos processuais da ação subsequente: `prazos-processuais`.

## Estrutura da peça
Cabeçalho (notificante, notificado, meio de entrega) → relação jurídica e documento de origem → fato que motiva a notificação → fundamento legal específico → providência exigida e prazo certo → consequência do não atendimento → ressalva de direitos → local, data, assinatura. Modelos por modalidade em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Promessa de compra e venda**: a interpelação é indispensável mesmo sem registro do compromisso (Súmula 76/STJ) e mesmo com cláusula resolutiva expressa; nessa hipótese a resolução opera de pleno direito só depois de vencido o prazo sem purgação (DL 745, art. 1º, parágrafo único; CC, art. 474).
- **Meio**: no DL 745, interpelação judicial ou pelo Registro de Títulos e Documentos; na Lei 6.766, intimação pelo Oficial do Registro de Imóveis, pessoal ou pelo RTD, com edital se o destinatário se furtar (art. 49).
- **Locação**: a denúncia precisa ser escrita; identifique a hipótese legal exata, porque denúncia vazia em contrato que só admite retomada motivada é ineficaz.
- **Alienação do imóvel locado**: verifique se há cláusula de vigência averbada na matrícula (art. 8º, caput) — se houver, o adquirente não pode denunciar.
- **Condomínio**: a multa do art. 1.337 exige deliberação de três quartos dos condôminos restantes; a do art. 1.336, § 2º, depende de previsão na convenção ou no ato constitutivo.

## Fundamentos verificados
- Lei 8.245/1991: arts. 4º, 6º, 8º, 27, 28, 46, 47, 56, 57, 59, § 1º, VIII.
- Decreto-Lei 745/1969, art. 1º (redação da Lei 13.097/2015); CC, arts. 397, 473 e 474.
- Lei 6.766/1979, arts. 32 e 49.
- CC, arts. 1.336, 1.337 e 1.348, VII.
- Súmula 76/STJ.
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos (conteúdo da notificação)
- Locação: desocupação no prazo legal, com entrega das chaves e vistoria; ressalva de despejo e de cobrança de aluguéis e encargos.
- Preferência: proposta completa (preço, forma de pagamento, condições, local e horário para exame de documentos), para aceitação em 30 dias.
- Promessa: pagamento das parcelas vencidas, discriminadas, no prazo legal, com local e forma de pagamento; advertência de resolução. Encargos moratórios: só os pactuados, calculados pelo núcleo `juros-e-correcao`.
- Condomínio: cessação da conduta, prazo razoável, indicação da multa aplicável e da regra violada.

## Checklist pré-protocolo
- [ ] Modalidade identificada e dispositivo legal exato citado
- [ ] Prazo legal correto para a modalidade, com termo inicial explícito
- [ ] Endereço atualizado do notificado; meio de envio com prova de recebimento
- [ ] Promessa: parcelas discriminadas; imóvel loteado (Lei 6.766) ou não (DL 745) definido
- [ ] Cláusula de vigência / averbação conferida na matrícula (art. 8º)
- [ ] Condomínio: convenção e ata anexadas ou referidas
- [ ] Cópia do contrato e da matrícula guardadas para a ação seguinte
- [ ] Encargos remetidos ao núcleo `juros-e-correcao`

## Erros a evitar
- Usar o prazo de 15 dias do DL 745 para lote em loteamento (o regime é o do art. 32 da Lei 6.766, de 30 dias) ou o contrário.
- Considerar o contrato resolvido pela cláusula resolutiva expressa sem interpelar o promitente comprador.
- Denúncia vazia em locação residencial inferior a 30 meses sem hipótese do art. 47.
- Adquirente que deixa passar os 90 dias do registro: presume-se a concordância com a locação (art. 8º, § 2º).
- Notificação de preferência sem todas as condições do negócio (o prazo de 30 dias corre sobre proposta integral).
- Fixar multa condominial acima dos tetos legais ou sem o quórum exigido.
- Inserir taxa de juros ou índice "de cabeça" no valor cobrado.

## Integração com o núcleo
`juros-e-correcao`, `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

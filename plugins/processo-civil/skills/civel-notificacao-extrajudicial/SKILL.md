---
name: civel-notificacao-extrajudicial
description: >
  Redige notificação extrajudicial cível de uso geral — constituição do
  devedor em mora quando a obrigação não tem termo (art. 397, parágrafo único,
  do Código Civil), comunicação formal de vontade, pedido de cumprimento,
  interpelação prévia à ação — e orienta quando ela NÃO basta e é preciso
  notificação, interpelação ou protesto judicial (CPC arts. 726 a 729; CC
  arts. 202, II, e 474). Use quando o usuário pedir notificação extrajudicial,
  carta de constituição em mora, interpelação do devedor, notificação antes
  de ajuizar, comunicação formal com prova de recebimento, ou perguntar se
  a notificação interrompe a prescrição.
metadata:
  area: processo-civil
  tipo_peca: notificacao
  verificado_em: 2026-11-25
---
# Notificação extrajudicial cível

Ferramenta de apoio; o advogado responsável revisa toda peça antes do envio.

## Quando usar / quando não usar
- Usar: (a) constituir em mora o devedor de obrigação sem termo (art. 397, p.u., do CC); (b) exigir cumprimento de obrigação civil fora de contrato típico (dever de indenizar, devolução de bem, prestação de contas informal); (c) comunicar formalmente uma vontade juridicamente relevante (desistência, oposição, ciência de cessão, recusa); (d) documentar tentativa de solução antes de ajuizar.
- Não usar:
  - Descumprimento de contrato empresarial ou de prestação de serviço: `contratos-notificacao-de-descumprimento`.
  - Locação, condomínio, compra e venda de imóvel: `imob-notificacao-extrajudicial-imobiliaria`.
  - Consumidor contra fornecedor: `consumidor-notificacao-extrajudicial`; plano de saúde: `saude-notificacao-extrajudicial-plano-de-saude`.
  - Incidente de dados pessoais: `digital-notificacao-de-incidente-lgpd`.
  - Quando a lei exige a via judicial (ver abaixo): faça a petição de notificação/interpelação/protesto judicial com `civel-peticao-inicial` como base de forma.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Notificante e notificado: qualificação e **endereço atual verificado** (físico e eletrônico, se houver).
2. Relação jurídica e documento de origem (contrato, título, ato ilícito, sentença).
3. Obrigação exigida: o quê, quanto, até quando, onde e como cumprir.
4. A obrigação tem termo (data de vencimento)? Se tem, a mora já existe de pleno direito (art. 397, caput) e a notificação é só prova e oportunidade de acordo.
5. Finalidade jurídica pretendida: mora, resolução, prova, prevenir prescrição, comunicação de vontade.
6. Datas: vencimento, últimos contatos, prazo prescricional estimado (para avaliar se a via extrajudicial é segura).
7. Consequência que se quer anunciar (ação, resolução, cobrança) — e se o cliente de fato está disposto a executá-la.

## Prazo e contagem
- Prazo para o notificado cumprir: fixe em dias corridos e com data-limite expressa; não há prazo legal geral para notificação cível. Se o contrato ou a lei fixar prazo próprio, use-o.
- **Notificação extrajudicial não interrompe a prescrição** (STJ, AgInt no AREsp 2.568.641 e AgInt no AREsp 2.579.602). Se a prescrição está perto, use o protesto judicial (art. 202, II, do CC; art. 726, § 2º, do CPC) ou ajuíze a ação.
- Interrupção por ato do devedor: qualquer ato inequívoco de reconhecimento do direito, ainda que extrajudicial (art. 202, VI) — guarde a resposta do notificado que reconheça a dívida.
- A citação válida também constitui em mora (art. 240 do CPC); a notificação não é condição da ação, salvo exigência legal ou contratual específica.
- Contagem processual (se houver prazo judicial depois): `prazos-processuais`.

## Estrutura da peça
Cabeçalho (notificante, notificado, meio de envio) → fatos e documento de origem → obrigação e fundamento → prazo e forma de cumprimento → consequências do silêncio → reserva de direitos → canal de resposta → data, local e assinatura. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Prova do recebimento** é o que dá valor à notificação: Registro de Títulos e Documentos, carta com aviso de recebimento e conteúdo declarado, ou meio eletrônico com comprovação. Escolha o meio que o contrato prevê, se houver cláusula de notificação.
- **Endereço correto**: o do contrato ou o último conhecido e comprovado.
- **Quando a via extrajudicial NÃO basta**:
  - Cláusula resolutiva **tácita**: depende de interpelação judicial (art. 474 do CC). A expressa opera de pleno direito.
  - Prevenir prescrição: protesto judicial (art. 202, II, do CC; art. 726, § 2º, do CPC).
  - Ciência geral por edital ou averbação em registro público: notificação judicial (art. 726, § 1º; art. 728).
- **Tom**: firme e sem ameaça ilícita. Não exponha o notificado a terceiros; não envie a familiares ou empregador.
- **Representação**: o advogado assina com procuração (art. 5º da Lei 8.906/1994), indicada na carta.

## Fundamentos verificados
- CC arts. 202, II e VI; 397, caput e parágrafo único; 422; 474.
- CPC arts. 240; 726 a 729 (notificação, interpelação e protesto judicial).
- STJ: simples envio de notificação extrajudicial não interrompe a prescrição (AgInt no AREsp 2.568.641; AgInt no AREsp 2.579.602).
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos (conteúdo da notificação)
- Cumprimento da obrigação certa, com valor ou ato, data-limite e forma (conta, local, entrega).
- Declaração expressa de que o notificado fica constituído em mora a partir do recebimento (obrigação sem termo).
- Indicação do que acontecerá sem resposta (ação de cobrança, execução, resolução expressa, perdas e danos), sem multa ou sanção não prevista em lei ou contrato.
- Valores atualizados: cálculo pelo núcleo `juros-e-correcao`, com memória anexa.
- Pedido de resposta escrita por canal identificado.
- Reserva de todos os direitos não mencionados.

## Checklist pré-envio
- [ ] Endereço do notificado conferido em documento recente.
- [ ] Meio de envio com prova de conteúdo e de recebimento.
- [ ] Prescrição calculada: se próxima, protesto judicial ou ação, não carta.
- [ ] Cláusula resolutiva: expressa (carta basta) ou tácita (interpelação judicial).
- [ ] Obrigação, valor e prazo certos; data-limite por extenso.
- [ ] Nenhuma ameaça que o cliente não pretenda cumprir; nenhuma exposição a terceiros.
- [ ] Procuração do advogado signatário.
- [ ] Cópia e comprovantes arquivados para instruir a futura ação.

## Erros a evitar
- Contar com a notificação extrajudicial para interromper prescrição.
- Notificar para "resolver o contrato" com base em cláusula resolutiva tácita sem interpelação judicial (art. 474).
- Enviar para endereço antigo ou por meio sem prova de conteúdo.
- Prazo vago ("prazo razoável", "brevidade") que impede provar o termo da mora.
- Valores calculados sem memória ou com índice escolhido de cabeça.
- Linguagem intimidatória ou divulgação da dívida a terceiros.

## Integração com o núcleo
`juros-e-correcao` (valor atualizado), `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`. Fracassada a notificação: `civel-peticao-inicial`, `civel-acao-monitoria` ou `civel-execucao-titulo-extrajudicial`.

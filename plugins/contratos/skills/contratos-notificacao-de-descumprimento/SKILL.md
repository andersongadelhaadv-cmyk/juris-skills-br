---
name: contratos-notificacao-de-descumprimento
description: >
  Redige notificação extrajudicial de descumprimento contratual para
  constituir o devedor em mora, conceder prazo de purgação e preparar a
  resolução, a cobrança da cláusula penal ou a execução (CC arts. 389 a 401,
  397 parágrafo único, 474 e 476). Use quando o usuário pedir notificação
  extrajudicial, interpelação, carta de cobrança formal, aviso de
  inadimplemento, constituição em mora, "dar prazo para cumprir sob pena de
  rescisão" ou notificação prévia exigida por cláusula resolutiva.
metadata:
  area: contratos
  tipo_peca: notificacao
  verificado_em: 2026-11-25
---
# Notificação de descumprimento contratual

Ferramenta de apoio; o advogado responsável revisa todo documento antes de assinar ou enviar.

## Quando usar / quando não usar
- Usar: (a) obrigação sem termo certo — a mora só nasce com a interpelação (CC art. 397, parágrafo único); (b) contrato com cláusula resolutiva expressa que exige aviso ou em que a jurisprudência exige interpelação antes da resolução; (c) obrigação com termo, para registrar a mora, dar prazo de purgação e documentar a boa-fé; (d) preparar cobrança de multa ou perdas e danos.
- Não usar: quando o objetivo já é comunicar a extinção (`contratos-distrato-e-rescisao`); quando o prazo prescricional está próximo — notificação extrajudicial não interrompe prescrição (CC art. 202, V, exige ato judicial); quando se quer ato com fé pública processual — notificação judicial (CPC arts. 726 e 727); cobrança de consumidor com ameaça ou exposição (CDC art. 42).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Contrato, aditivos e a cláusula exata descumprida (número e texto).
2. O que foi descumprido, desde quando, com que prova (fatura, relatório, e-mail, laudo, fotos).
3. A obrigação tem termo certo (data de vencimento) ou não?
4. Cláusula de comunicações: endereço, e-mail, meio obrigatório, prazo para considerar recebido.
5. Cláusula resolutiva expressa? Prazo de cura previsto no contrato?
6. O cliente está em dia com as obrigações dele? (CC art. 476)
7. Valor histórico do débito e datas — **sem** calcular encargos aqui.
8. O que o cliente quer: cumprimento, pagamento, resolução, multa, ou só registro.
9. A outra parte é consumidora? Há fiador ou garantidor a notificar também?

## Prazos relevantes
- Prazo de purgação: o do contrato; se omisso, prazo razoável e certo (data-limite expressa, evitando "imediatamente").
- Contagem: dizer se são dias corridos ou úteis e a partir de quê (recebimento, não envio).
- Mora ex re: obrigação positiva e líquida com termo constitui em mora de pleno direito (art. 397, caput); a notificação, aqui, é prova e oportunidade de purga, não requisito.
- Prescrição corre durante a notificação. Se o prazo estiver perto, ajuizar ou obter reconhecimento do devedor.
- Prazos processuais posteriores: `prazos-processuais`.

## Estrutura do documento
Cabeçalho (notificante, notificado, meio) → referência ao contrato → obrigação e cláusula → fatos com datas e prova → constituição em mora → prazo de purgação e forma de cumprir → consequências previstas no contrato → ressalvas → canal de resposta → assinatura. Roteiro em [estrutura](references/estrutura.md).

Cláusulas essenciais:
- **Identificação precisa** da cláusula violada e do contrato.
- **Fato, não adjetivo**: datas, documentos, quantidades.
- **Prazo certo** e **forma** de purgar (conta, local, entrega).
- **Consequências** exatamente como previstas no contrato (resolução, multa, vencimento antecipado) — não inventar sanção.
- **Ressalva** de direitos não mencionados e de que a tolerância não importa renúncia.

## Riscos e cláusulas sensíveis
- **Sem cláusula resolutiva expressa**, a resolução depende de interpelação **judicial** (art. 474). A notificação extrajudicial constitui em mora, mas não resolve sozinha o contrato.
- **Com cláusula expressa**, a interpelação desatendida viabiliza a resolução de pleno direito (REsp 2.139.100); a jurisprudência exige oportunizar a purga (AgInt nos EDcl no AREsp 2.113.760). Em leasing, notificação prévia é obrigatória mesmo com cláusula expressa (Súmula 369/STJ); em compromisso de compra e venda de imóvel, o não registro não dispensa a interpelação (Súmula 76/STJ).
- **Notificante inadimplente.** Se o cliente também deve, a notificação abre caminho para a exceção do contrato não cumprido (art. 476). Apurar antes.
- **Meio e prova.** Usar o meio que o contrato prevê; sem previsão, meio com prova de conteúdo e de recebimento (Registro de Títulos e Documentos, carta com AR e cópia autenticada, notificação judicial). E-mail ou mensageiro só se o contrato admitir, guardando a prova de entrega.
- **Valores.** Informar o principal e as datas; encargos de mora (CC arts. 389 e 395) pelo núcleo `juros-e-correcao`. Multa: só a prevista, sem exceder a obrigação principal (art. 412).
- **Tom.** Ameaça desproporcional, menção a terceiros ou exposição pública do devedor gera responsabilidade; com consumidor, vedado constrangimento ou ameaça na cobrança (CDC art. 42).
- **Dados pessoais.** Enviar só ao endereço contratual; não copiar terceiros sem necessidade (LGPD art. 7º).

## Fundamentos verificados
- CC arts. 389, 394, 395, 397 e parágrafo único, 401, 202 V, 412, 474, 476.
- CPC arts. 726 e 727 (notificação e interpelação judiciais).
- CDC art. 42; LGPD art. 7º.
- Súmulas 76 e 369/STJ; REsp 2.139.100; AgInt nos EDcl no AREsp 2.113.760.
Detalhe em [fundamentos](references/fundamentos.md).

## Checklist antes de assinar/enviar
- [ ] Cláusula descumprida citada com número e texto conferido
- [ ] Fatos datados e prova listada
- [ ] Cliente adimplente (ou risco do art. 476 registrado ao cliente)
- [ ] Prazo de purgação certo, com regra de contagem
- [ ] Consequências idênticas às do contrato
- [ ] Meio de envio conforme a cláusula de comunicações; prova de recebimento planejada
- [ ] Fiador/garantidor notificado, se for o caso
- [ ] Prescrição conferida — se próxima, notificação não basta
- [ ] Valores históricos corretos; encargos remetidos ao núcleo
- [ ] Tom profissional, sem ameaça e sem terceiros

## Erros a evitar
- Notificar e já declarar o contrato "rescindido" sem prazo de purga quando o contrato ou a jurisprudência o exigem.
- Mandar para endereço diferente do contratual.
- Exigir multa não prevista ou acima do principal.
- Confundir notificação com interrupção da prescrição.
- Calcular juros "de memória" no corpo da carta.

## Integração com o núcleo
`juros-e-correcao`, `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual` (cada fato tem prova), `estilo-forense`.

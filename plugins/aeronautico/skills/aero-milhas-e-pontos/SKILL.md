---
name: aero-milhas-e-pontos
description: >
  Redige ação de obrigação de fazer cumulada com indenização contra programa de
  fidelidade de companhia aérea (ou de banco parceiro) por cancelamento,
  expiração, bloqueio ou estorno indevido de milhas e pontos, com base no CDC
  (arts. 6º, 14, 39 V e 51) e no dever de informação. Use quando o usuário pedir
  ação por milhas expiradas sem aviso, saldo zerado, conta de fidelidade
  bloqueada ou suspensa, pontos estornados, passagem emitida com milhas e
  cancelada sem devolução, ou recusa de resgate de pontos.
metadata:
  area: aeronautico
  tipo_peca: inicial
  verificado_em: 2026-11-25
---
# Milhas e pontos: cancelamento, expiração e bloqueio indevidos

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: (a) milhas canceladas ou expiradas antes do prazo informado, ou sem aviso; (b) conta bloqueada/suspensa por suposta fraude sem prova nem contraditório; (c) pontos transferidos do cartão que não chegaram ou foram estornados; (d) passagem emitida com milhas cancelada pela empresa sem devolução dos pontos e das taxas; (e) alteração unilateral da tabela de resgate aplicada a saldo já acumulado.
- Não usar: atraso, cancelamento de voo ou bagagem em viagem comprada com milhas (`consumidor-transporte-aereo` — o regime é o mesmo do bilhete pago); reembolso de passagem paga em dinheiro (`aero-reembolso-de-passagem`); cobrança de anuidade ou tarifa do cartão de crédito (`consumidor-contratos-bancarios-revisional`); dados pessoais da conta (`aero-habeas-data-dados-de-passageiro`).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Nome do programa e da empresa que o opera (muitas vezes pessoa jurídica distinta da companhia aérea) e, se houver, do banco/emissor de onde vieram os pontos.
2. Extrato da conta com datas de crédito, validade informada e data do cancelamento/expiração/estorno (print com data e hora).
3. Regulamento do programa **vigente na data do acúmulo** e na data do cancelamento; avisos recebidos (e-mail, app) sobre vencimento.
4. Como as milhas foram obtidas: voo, compra de pontos, transferência de cartão, bônus promocional (o regime da oferta muda conforme a origem).
5. Protocolos de atendimento, reclamação no consumidor.gov.br ou Procon, e a resposta da empresa.
6. Se bloqueio por fraude: o que a empresa alegou e se houve oportunidade de defesa.
7. Prejuízo concreto: viagem perdida, passagem comprada em dinheiro para substituir o resgate (com comprovante).

## Prazo e contagem
- Pretensão por falha do serviço (fato do serviço): 5 anos do art. 27 do CDC, contados do conhecimento do dano e de sua autoria. Para pedido fundado só em descumprimento contratual (restabelecimento de saldo), o enquadramento do prazo não foi conferido em fonte oficial [VERIFICAR via `verificacao-de-citacoes`]; na dúvida, ajuíze cedo.
- Prazos processuais: `prazos-processuais`.

## Estrutura da peça
Fatos com linha do tempo do saldo → relação de consumo e legitimidade passiva → abusividade da cláusula ou da conduta (expiração sem informação, alteração unilateral, bloqueio sem prova) → falha do serviço → restabelecimento do saldo (ou conversão em perdas e danos) → danos materiais e, se houver repercussão concreta, morais → tutela de urgência quando há viagem marcada. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Polo passivo**: a operadora do programa; a companhia aérea se o resgate ou o voo foi dela; o banco emissor se a falha está na transferência. Fundamente a solidariedade da cadeia (CDC art. 7º, parágrafo único).
- **Regulamento como contrato de adesão**: cláusula de validade curta, de perda total por inatividade ou de alteração unilateral se discute pelo art. 51 (IV, X, XI e § 1º) do CDC. Não alegue nulidade "genérica" de toda validade: ataque a cláusula concreta, a falta de informação ou a aplicação retroativa.
- **Bloqueio por fraude**: o ônus de provar a irregularidade é da empresa (art. 6º, VIII; art. 14, § 3º). Peça exibição dos registros que fundamentaram o bloqueio.
- **Milhas não são dinheiro**: o pedido principal é restabelecer o saldo; a conversão em pecúnia é subsidiária, pelo valor de mercado da passagem que o resgate cobriria. Há decisão de turma recursal negando a conversão direta e determinando a restituição das milhas (TJBA, RI 0016946-63.2022.8.05.0001).

## Fundamentos verificados
- CDC arts. 6º (VI e VIII), 7º p.ú., 14 (caput e § 3º), 27, 39 V, 51 (IV, X, XI e § 1º).
- Dano moral não é automático: turma recursal do TJDFT reconheceu o crédito das milhas da campanha descumprida e negou dano moral (RI 0708548-85.2025.8.07.0014, julg. 18/05/2026). Precedentes de turma recursal, sem força vinculante.
- Jurisprudência do STJ específica sobre expiração de milhas: não localizada na base consultada [VERIFICAR antes de afirmar entendimento do STJ].
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Tutela de urgência (CPC art. 300) para restabelecer o saldo ou desbloquear a conta, com multa diária, quando houver viagem próxima ou risco de nova expiração.
- Declaração de nulidade da cláusula aplicada (ou de sua ineficácia ao saldo anterior).
- Restabelecimento integral das milhas, com a validade original restaurada a partir do trânsito ou da efetiva recomposição.
- Subsidiariamente, perdas e danos pelo valor da passagem equivalente (cotação documentada).
- Danos materiais comprovados (passagem comprada em dinheiro, taxas pagas e não devolvidas); repetição em dobro só se houve **pagamento** indevido (`consumidor-repeticao-em-dobro`).
- Dano moral apenas com fato concreto (viagem frustrada, bloqueio com imputação de fraude); juros e correção pelo `juros-e-correcao`.
- Inversão do ônus e exibição do extrato completo, do regulamento por versão e dos registros do bloqueio.

## Checklist pré-protocolo
- [ ] Operadora do programa identificada (CNPJ) e cadeia de fornecedores no polo passivo
- [ ] Extrato com datas de crédito, validade e baixa
- [ ] Regulamento da época do acúmulo juntado (não só o atual)
- [ ] Prova de ausência de aviso ou de aviso tardio
- [ ] Cotação da passagem equivalente para o pedido subsidiário
- [ ] Reclamação administrativa e resposta juntadas
- [ ] Fato concreto para o dano moral (ou pedido de dano moral retirado)

## Erros a evitar
- Pedir direto o "valor em reais" das milhas, sem o pedido principal de restabelecimento.
- Processar só a companhia aérea quando o programa é operado por outra pessoa jurídica.
- Juntar apenas o regulamento atual e perder a discussão sobre alteração unilateral.
- Tratar milhas promocionais e milhas compradas como se tivessem a mesma oferta.
- Pedir dano moral presumido.

## Integração com o núcleo
`juros-e-correcao`, `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

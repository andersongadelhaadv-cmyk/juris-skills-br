---
name: prev-mandado-de-seguranca-demora-inss
description: >
  Redige mandado de segurança contra omissão do INSS na análise de requerimento
  de benefício, de recurso administrativo ou no cumprimento de decisão do CRPS
  (Lei 12.016/2009; Lei 9.784/1999, arts. 48 e 49; CF, art. 5º, LXXVIII), com
  base no acordo homologado pelo STF no RE 1.171.152/SC sobre prazos de análise.
  Use quando o usuário pedir mandado de segurança contra o INSS, MS por demora
  na análise do benefício, requerimento parado há meses, INSS não cumpre acórdão
  da Junta de Recursos, benefício "em análise" sem resposta ou ordem para o INSS decidir.
metadata:
  area: previdenciario
  tipo_peca: inicial
  verificado_em: 2026-11-25
---
# Mandado de segurança contra demora do INSS

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: requerimento de benefício, revisão ou recurso administrativo sem decisão além do prazo; acórdão da Junta ou Câmara do CRPS favorável e não cumprido; benefício concedido e não implantado. O pedido é que o INSS **decida** (ou cumpra), não que conceda o benefício.
- Não usar quando o objetivo é o próprio benefício e há prova a produzir (perícia, testemunhas): a via é a ação de concessão (`prev-inicial-aposentadoria`, `prev-beneficio-por-incapacidade`, `prev-bpc-loas`). Sobre demora e interesse de agir na ação ordinária, ver `prev-requerimento-administrativo`.
- Não cabe no JEF: mandado de segurança está excluído da competência do Juizado (Lei 10.259, art. 3º, § 1º, I).
- MS contra ato de outra autoridade administrativa: `adm-mandado-de-seguranca`. Recurso administrativo em si: `prev-recurso-crps`.

## Entradas mínimas (perguntar o que faltar; nunca supor fatos)
1. Protocolo do requerimento ou do recurso (número, data, espécie do benefício) e prints do andamento no Meu INSS.
2. Se houve carta de exigência: data, conteúdo e data do cumprimento (o prazo conta da instrução concluída).
3. Agência ou Central de Análise responsável e o cargo da autoridade (para indicar o coator).
4. Para descumprimento de acórdão do CRPS: cópia do acórdão e da ciência ao INSS.
5. Situação de urgência do segurado (renda, doença, idade) para a liminar.

## Prazo e contagem
- Decadência de 120 dias contados da ciência do ato (Lei 12.016, art. 23). Em omissão continuada, os tribunais afastam a decadência enquanto a inércia persiste (ex.: TRF6, Apelação/Remessa 6001780-58.2025.4.06.3825).
- Lei 9.784, art. 49: concluída a instrução, a Administração tem até 30 dias para decidir, prorrogáveis por igual período motivadamente.
- Prazos de análise por espécie fixados no acordo do RE 1.171.152/SC: [VERIFICAR: tabela de prazos e termos do acordo no portal do STF antes de citar números].
- Prazos processuais: `prazos-processuais`.

## Estrutura da peça
Endereçamento à vara federal → impetrante e autoridade coatora (art. 6º, § 3º) com indicação do INSS como pessoa jurídica (art. 7º, II) → fatos com cronologia do protocolo → cabimento e tempestividade → direito líquido e certo (dever de decidir, prazo legal, razoável duração, acordo do RE 1.171.152) → liminar (art. 7º, III) → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Prova pré-constituída: tudo documentado na inicial (protocolo, andamento, exigências cumpridas). MS não admite dilação probatória.
- Autoridade coatora: quem tem poder de praticar o ato omitido (art. 6º, § 3º). Na prática, os tribunais aceitam o Gerente Executivo do INSS (ex.: TRF5, Remessa 0014711-80.2025.4.05.8302); conferir a estrutura atual (agência, Central de Análise, CEAB) [VERIFICAR no caso].
- Liminar exige fundamento relevante e risco de ineficácia da medida (art. 7º, III). O § 2º do art. 7º veda liminar para "pagamento de qualquer natureza": por isso o pedido é de análise/decisão em prazo, não de pagamento.
- Sem honorários no MS (art. 25). Sentença concessiva sujeita a reexame necessário (art. 14, § 1º).

## Fundamentos verificados
- CF, art. 5º, LXIX (mandado de segurança) e LXXVIII (razoável duração do processo, inclusive administrativo); Lei 9.784, arts. 48 e 49; Lei 12.016, arts. 1º, 6º, § 3º, 7º, 14, 23 e 25; Lei 10.259, art. 3º, § 1º, I.
- Acordo homologado pelo STF no RE 1.171.152/SC, aplicado pelos TRFs em MS por demora do INSS (ex.: TRF1, Remessa 1000954-48.2025.4.01.3602, que o identifica como Tema 1.066/STF [VERIFICAR a numeração no portal do STF]).
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Liminar para que a autoridade analise e conclua o requerimento (ou cumpra o acórdão do CRPS) em prazo fixado pelo juízo, sob multa diária.
- Notificação da autoridade para informações em 10 dias e ciência ao INSS (art. 7º, I e II).
- Intimação do Ministério Público.
- Concessão da segurança, confirmando a liminar.
- Sem pedido de honorários (art. 25).

## Checklist pré-protocolo
- [ ] Protocolo e andamento documentados, com data de cada exigência e cumprimento
- [ ] Prazo legal ou do acordo comprovadamente ultrapassado
- [ ] Autoridade coatora identificada pelo cargo, com endereço
- [ ] Pedido limitado a analisar/decidir/cumprir (não a pagar)
- [ ] Vara federal (não JEF)
- [ ] Prazos do acordo do RE 1.171.152 conferidos no STF, se citados

## Erros a evitar
- Pedir a concessão do benefício no MS quando há fato controvertido: a segurança será negada por falta de direito líquido e certo.
- Impetrar com exigência pendente de cumprimento pelo próprio segurado.
- Citar números de prazo do acordo "de memória".
- Indicar a autarquia como autoridade coatora em vez do agente com poder de decidir.

## Integração com o núcleo
`prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`. Juros e correção não se aplicam ao MS de análise; se houver atrasados depois, `juros-e-correcao` na ação própria.

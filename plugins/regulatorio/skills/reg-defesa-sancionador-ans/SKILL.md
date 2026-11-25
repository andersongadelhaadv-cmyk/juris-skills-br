---
name: reg-defesa-sancionador-ans
description: >
  Redige defesa de operadora de plano de saúde (e de seus administradores) em
  processo administrativo sancionador da Agência Nacional de Saúde
  Suplementar, com base na Lei 9.961/2000, nos arts. 25, 27 e 29 da Lei
  9.656/1998, na Lei 9.784/1999 e na Lei 9.873/1999. Use quando o usuário pedir
  defesa contra auto de infração da ANS, resposta a processo sancionador
  aberto após reclamação de beneficiário, termo de compromisso de ajuste de
  conduta (TCAC) com a ANS, prescrição de multa da ANS ou redução de multa
  aplicada a operadora.
metadata:
  area: regulatorio
  tipo_peca: contestacao
  verificado_em: 2026-11-25
---
# Defesa no processo sancionador da ANS

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: operadora, administradora de benefícios ou seus administradores e conselheiros autuados pela ANS (negativa de cobertura, reajuste, rede, prazos de atendimento, informações periódicas, contratos), antes da decisão de primeira instância.
- Não usar:
  - Decisão da ANS já proferida: `reg-recurso-multa-agencia` (o recurso vai à Diretoria Colegiada).
  - Beneficiário contra a operadora em juízo: `consumidor-plano-de-saude`.
  - Defesa da operadora em ação do consumidor: `consumidor-defesa-do-fornecedor`.
  - Ressarcimento ao SUS: não é sanção; trate como cobrança de crédito da autarquia [VERIFICAR rito próprio].
  - Outra agência: `reg-defesa-processo-sancionador-agencia`.

## Entradas mínimas (perguntar o que faltar; nunca supor fatos)
1. Auto de infração ou ato de instauração, com data da ciência e meio de intimação.
2. Origem: reclamação de beneficiário (protocolo e fase de intermediação prévia, se houve), fiscalização de ofício, representação ou denúncia.
3. Dispositivo imputado (lei, resolução normativa, contrato) e a conduta descrita.
4. Prontuário do caso: pedido do beneficiário, resposta da operadora, datas, autorização ou reembolso efetivados, contrato e aditivos.
5. Prova de correção da conduta antes da lavratura (autorização, reembolso, contato com o beneficiário).
6. Porte da operadora (número de beneficiários) e histórico de sanções — afetam a multa.
7. Interesse em TCAC ou em pagamento com desconto previsto na norma da ANS.

## Prazo e contagem
- Prazo de defesa, desconto por pagamento e efeitos do reconhecimento: fixados na resolução normativa da ANS que rege o processo sancionador [VERIFICAR: número e versão vigente no portal da ANS antes de citar].
- Na falta de regra específica, contagem da Lei 9.784/1999 (art. 66: dias contínuos, exclui o início, inclui o vencimento).
- Prescrição punitiva de 5 anos e intercorrente de 3 anos (Lei 9.873/1999, art. 1º); suspensa durante a vigência do TCAC (Lei 9.656/1998, art. 29, § 6º).
- Conferência de contagem: `prazos-processuais`.

## Estrutura da peça
Endereçamento → tempestividade → síntese → preliminares (prescrição, intimação, tipicidade, legitimidade do autuado) → mérito (cobertura devida ou não, correção da conduta, prova) → dosimetria subsidiária (porte e gravidade) → provas → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Base legal da competência**: a ANS fiscaliza e aplica as penalidades da Lei 9.656/1998 (Lei 9.961/2000, art. 4º, XXIII e XXX).
- **Rito**: processo com base em auto de infração, representação ou denúncia positiva; a ANS regulamenta instauração, recursos e prazos (Lei 9.656/1998, art. 29, caput).
- **Legitimidade passiva administrativa**: o art. 25 alcança a operadora, seus administradores e conselheiros; confira quem foi autuado e por qual conduta.
- **Tipicidade**: a conduta deve se encaixar no tipo da norma da ANS invocada, na redação vigente na data do fato.
- **Prescrição**: tabela de atos (Lei 9.873/1999, arts. 1º e 2º); ato meramente ordinatório não interrompe a intercorrente (ver `reg-defesa-processo-sancionador-agencia`).

## Fundamentos verificados
- Lei 9.961/2000: art. 3º (finalidade), art. 4º, XXIII, XXX e XXXIX (fiscalizar, punir, celebrar termos de compromisso), art. 10, VI e §§ 2º e 3º (recurso à Diretoria Colegiada, efeito suspensivo salvo risco à saúde).
- Lei 9.656/1998: art. 25 (penalidades), art. 27 (multa de R$ 5.000,00 a R$ 1.000.000,00 conforme porte e gravidade), art. 29 (rito e TCAC; § 3º: o TCAC não importa confissão).
- Lei 9.784/1999 e LINDB art. 22, § 2º (dosimetria).
- STJ: reparação voluntária e matéria infralegal da ANS não são revistas em recurso especial (AgInt no AREsp 2.410.565) — a prova tem de ser feita na esfera administrativa.
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Prescrição e arquivamento.
- Nulidade (intimação sem fatos e fundamentos; atipicidade; autuado ilegítimo).
- Improcedência: cobertura não devida pelo contrato e pela norma, ou conduta corrigida antes da autuação, com prova.
- Subsidiariamente: advertência em vez de multa; multa no mínimo compatível com o porte e a gravidade (art. 27); atenuantes previstos na norma da ANS.
- Alternativa negociada: proposta de TCAC à Diretoria Colegiada (art. 29, §§ 1º a 3º), avaliando o impedimento do § 7º.
- Provas documentais, técnicas (parecer médico/atuarial) e vista integral.

## Checklist pré-protocolo
- [ ] Resolução da ANS sobre o processo sancionador conferida na versão vigente
- [ ] Prazo contado da ciência
- [ ] Prontuário completo do atendimento ao beneficiário juntado
- [ ] Prova de autorização, reembolso ou correção com data anterior à autuação
- [ ] Porte da operadora comprovado (base da multa)
- [ ] Avaliada a conveniência de TCAC ou pagamento com desconto, com o cliente
- [ ] Prescrição punitiva e intercorrente calculadas

## Erros a evitar
- Citar número de resolução normativa da ANS de memória: a norma do processo sancionador já foi substituída mais de uma vez; confira.
- Discutir só o direito do beneficiário e esquecer a tipicidade administrativa e a dosimetria.
- Deixar a prova técnica para a ação judicial: o STJ não revê resolução nem prova.
- Assinar TCAC sem medir o § 7º (impedimento de novo termo após descumprimento) e a multa do § 2º.
- Supor efeito suspensivo em tudo: cede quando há risco à saúde do consumidor (Lei 9.961/2000, art. 10, § 3º).

## Integração com o núcleo
`prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`, `juros-e-correcao` (encargos sobre a multa).

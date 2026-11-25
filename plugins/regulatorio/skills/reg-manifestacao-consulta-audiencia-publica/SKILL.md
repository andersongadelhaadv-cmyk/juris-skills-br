---
name: reg-manifestacao-consulta-audiencia-publica
description: >
  Redige contribuição escrita em consulta pública e roteiro de manifestação
  oral em audiência pública de agência reguladora sobre minuta de ato
  normativo, com base nos arts. 6º e 9º a 12 da Lei 13.848/2019, no art. 5º da
  Lei 13.874/2019, no art. 29 da LINDB e nos arts. 31 a 34 da Lei 9.784/1999.
  Use quando o usuário pedir contribuição para consulta pública da ANEEL,
  ANATEL, ANP, ANVISA, ANS ou outra agência, manifestação em audiência
  pública regulatória, crítica à análise de impacto regulatório (AIR) ou
  pedido de prorrogação de consulta pública.
metadata:
  area: regulatorio
  tipo_peca: outro
  verificado_em: 2026-11-25
---
# Manifestação em consulta e audiência pública regulatória

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: contribuição escrita em consulta pública sobre minuta de resolução, alteração normativa ou agenda regulatória; manifestação oral em audiência pública; pedido de prorrogação da consulta ou de acesso aos estudos; acompanhamento do relatório de contribuições.
- Não usar:
  - Ato normativo já editado e impugnação judicial: `adm-mandado-de-seguranca` (efeitos concretos) ou ação própria.
  - Processo individual sancionador: `reg-defesa-processo-sancionador-agencia`.
  - Pedido individual de outorga: `reg-pedido-outorga-licenca-agencia`.
  - Diagnóstico interno de aderência à nova norma: `reg-programa-integridade-compliance` (parecer de compliance regulatório).

## Entradas mínimas (perguntar o que faltar; nunca supor fatos)
1. Aviso de consulta ou audiência: número, agência, prazo, forma de envio (formulário eletrônico, e-mail, sistema), regras de formatação.
2. Minuta, nota técnica e relatório de AIR disponibilizados.
3. Quem contribui (empresa, associação, consumidor) e o interesse defendido — a contribuição é pública.
4. Impacto concreto da minuta no cliente: custo, prazo de adaptação, investimento, efeito sobre contratos e consumidores, com números quando houver.
5. Propostas alternativas de redação e de transição.
6. Informações que o cliente não quer tornar públicas.

## Prazo e contagem
- Consulta pública de agência federal: mínimo de 45 dias, salvo urgência e relevância motivadas (Lei 13.848/2019, art. 9º, § 2º); o prazo concreto é o do aviso.
- Audiência pública: convocação publicada e documentos disponíveis com pelo menos 5 dias úteis de antecedência (art. 10, §§ 2º e 3º).
- Relatório da audiência ou de outros meios de participação: até 30 dias úteis após o encerramento, prorrogáveis uma vez (art. 12).
- Contribuição fora do prazo pode não ser considerada. Conferência: `prazos-processuais`.

## Estrutura da peça
Identificação do contribuinte e do interesse → síntese das posições → comentários gerais (competência, AIR, alternativas, impacto) → comentários por dispositivo (redação atual → proposta → justificativa) → transição → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **AIR**: atos normativos de interesse geral passam por análise de impacto regulatório, nos termos de regulamento (Lei 13.848/2019, art. 6º; Lei 13.874/2019, art. 5º). O relatório de AIR e os estudos devem estar disponíveis no início da consulta, ressalvado o sigiloso (Lei 13.848/2019, art. 9º, § 3º). Ausência ou deficiência é ponto central da contribuição.
- **Dever de resposta**: a agência divulga as contribuições e o seu posicionamento sobre elas (art. 9º, §§ 4º e 5º); a consulta será considerada na decisão (LINDB, art. 29). Formule propostas objetivas, que exijam resposta motivada.
- **Competência e legalidade**: a minuta não pode inovar além da lei setorial; aponte o dispositivo legal que limita a agência [VERIFICAR lei setorial do caso].
- **Transição**: nova interpretação ou novo dever sobre norma indeterminada exige regime de transição quando indispensável (LINDB, art. 23).
- **Motivação e proporcionalidade**: Lei 13.848/2019, arts. 4º e 5º; LINDB, art. 20 (consequências práticas e alternativas).

## Fundamentos verificados
- Lei 13.848/2019, arts. 4º, 5º, 6º, 9º, 10, 11 e 12.
- Lei 13.874/2019, art. 5º.
- LINDB, arts. 20, 23 e 29.
- Lei 9.784/1999, arts. 31, 32 e 34 (órgãos não regidos pela Lei 13.848).
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Acolhimento das propostas de redação, dispositivo a dispositivo.
- Complementação ou revisão da AIR, com as alternativas indicadas.
- Regime de transição e prazo de adaptação proporcionais.
- Prorrogação do prazo da consulta, se os estudos não foram disponibilizados a tempo.
- Realização de audiência pública ou reunião técnica (art. 10 e art. 11).
- Resposta motivada a cada contribuição no relatório.

## Checklist pré-protocolo
- [ ] Formato exigido no aviso (formulário, campos, limite de caracteres) respeitado
- [ ] Cada proposta ligada a um dispositivo da minuta
- [ ] Impacto quantificado e fonte dos números indicada
- [ ] Informação sensível retirada ou enviada pelo canal sigiloso previsto
- [ ] Autorização do cliente para a contribuição pública e para a identificação
- [ ] Protocolo comprovado (recibo eletrônico)

## Erros a evitar
- Texto genérico, sem redação alternativa: a agência responde "não acolhida" sem esforço.
- Expor dado comercial sensível em contribuição que será publicada.
- Ignorar a AIR: é a base técnica que a agência precisa defender.
- Perder o prazo porque a consulta foi aberta em formulário eletrônico com horário de corte.
- Prometer ao cliente que a contribuição vincula a agência: vincula o dever de considerar e responder, não o resultado.

## Integração com o núcleo
`prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

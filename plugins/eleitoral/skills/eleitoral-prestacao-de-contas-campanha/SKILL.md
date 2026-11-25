---
name: eleitoral-prestacao-de-contas-campanha
description: >
  Orienta e redige a prestação de contas de campanha de candidato e partido
  e as manifestações no processo (resposta a diligências, defesa contra
  parecer técnico pela desaprovação), com base nos arts. 22 a 32 da Lei
  9.504/1997. Use quando o usuário pedir para preparar ou revisar prestação
  de contas eleitoral, responder relatório de diligências ou parecer
  conclusivo, evitar desaprovação ou contas julgadas não prestadas, tratar
  sobras, dívidas de campanha ou recursos de fonte vedada.
metadata:
  area: eleitoral
  tipo_peca: outro
  verificado_em: 2026-11-25
---
# Prestação de contas de campanha

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: (a) montar e revisar a prestação de contas final de candidato ou comitê; (b) responder a diligências (Lei 9.504/1997, art. 30, § 4º); (c) manifestação contra parecer pela desaprovação; (d) tratar sobras, dívidas e recursos de origem não identificada ou vedada.
- Não usar: recurso da sentença ou acórdão de contas — `eleitoral-recurso-eleitoral`; representação por arrecadação ou gasto ilícito (art. 30-A) — propor em `eleitoral-aije`, defender em `eleitoral-defesa-abuso-de-poder`; contas anuais de partido (Lei 9.096/1995) — fora do escopo; contas de gestor no Tribunal de Contas — `adm-*`; crime de falsidade na prestação — `penal-*`.

## Entradas mínimas (perguntar o que faltar; nunca supor fatos)
1. Cargo, eleição, se houve segundo turno; candidato eleito ou não (prazo de julgamento antes da diplomação).
2. Extratos da conta bancária específica de toda a campanha (art. 22) e de eventuais contas de fundos públicos.
3. Recibos de doação, notas fiscais, contratos, comprovantes de pagamento, cessões estimáveis em dinheiro.
4. Relatório de diligências ou parecer técnico, se já houver, com a data da intimação.
5. Dívidas não quitadas e decisão do órgão nacional do partido de assumi-las (art. 29, §§ 3º e 4º).
6. Sobras de campanha e destino (art. 31).

## Prazo e contagem
- Entrega das contas: até o 30º dia após a eleição; havendo segundo turno, contas dos dois turnos até o 20º dia após ele (art. 29, III e IV).
- Atraso impede a diplomação dos eleitos enquanto perdurar (art. 29, § 2º).
- Decisão das contas dos eleitos publicada em sessão até 3 dias antes da diplomação (art. 30, § 1º).
- Recurso da decisão: 3 dias da publicação no Diário Oficial (art. 30, § 5º).
- Documentos guardados até 180 dias após a diplomação, ou até decisão final se houver processo (art. 32).
- Prazos de resposta a diligências e calendário: resolução do TSE do pleito [VERIFICAR: resolução de prestação de contas e calendário eleitoral, no site do TSE]. Contagem: `prazos-processuais`.

## Estrutura da peça
Prestação: peças e demonstrativos exigidos pela resolução, conciliação bancária, nota explicativa. Manifestação: tempestividade → irregularidade por irregularidade (natureza, valor, percentual, documento que sana) → irrelevância no conjunto (art. 30, §§ 2º e 2º-A) → pedido de aprovação (ou com ressalvas). Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Conta bancária específica para toda a movimentação (art. 22); gasto pago com recurso fora dela leva à desaprovação e, com abuso econômico, à cassação (art. 22, § 3º).
- Fontes vedadas (art. 24): órgãos públicos, concessionárias, entidades de classe, sindicais, religiosas, esportivas, governos estrangeiros, entre outras.
- Partido que descumpre normas de arrecadação perde a quota do Fundo Partidário do ano seguinte (art. 25).
- Resultados possíveis: aprovadas, aprovadas com ressalvas, desaprovadas, não prestadas (art. 30, caput).
- Erros formais ou materiais corrigidos não autorizam a rejeição (§ 2º); erros irrelevantes no conjunto também não (§ 2º-A).
- Contas julgadas não prestadas e quitação eleitoral: [VERIFICAR: Súmula 42 do TSE — JuriBase sem cobertura do TSE].

## Fundamentos verificados
- Lei 9.504/1997: arts. 22, 24, 25, 28 (§§ 1º a 4º), 29 (III, IV, §§ 2º a 4º), 30 (caput, §§ 1º a 7º), 30-A, 31 e 32.
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Juntada da documentação complementar e retificação das peças (art. 30, § 4º).
- Aprovação das contas; subsidiariamente, aprovação com ressalvas por irrelevância das falhas (art. 30, §§ 2º e 2º-A).
- Afastamento de devolução ou recolhimento quando a origem do recurso for demonstrada [VERIFICAR: hipóteses de recolhimento ao Tesouro na resolução do pleito].
- Reconhecimento da assunção de dívida pelo partido (art. 29, § 3º), que não justifica rejeição (§ 4º).

## Checklist pré-protocolo
- [ ] Extratos de toda a campanha conciliados com receitas e despesas
- [ ] Toda receita com recibo e CPF/CNPJ do doador; nenhuma fonte vedada
- [ ] Todo gasto pago pela conta específica, com documento fiscal
- [ ] Sobras declaradas e transferidas ao partido (art. 31)
- [ ] Dívidas com decisão do órgão nacional (art. 29, § 3º)
- [ ] Prazo de entrega (30º ou 20º dia) cumprido
- [ ] Prazo de resposta a diligência conferido na resolução

## Erros a evitar
- Pagar despesa em espécie ou por conta pessoal (art. 22, § 3º).
- Deixar de declarar cessão estimável (veículo, imóvel, serviço) recebida.
- Responder diligência sem documento, só com explicação.
- Confundir contas de campanha (Lei 9.504/1997) com contas anuais do partido.
- Não dimensionar o percentual da falha sobre o total: é o argumento do § 2º-A.

## Integração com o núcleo
`prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`. Valores a recolher com atualização: `juros-e-correcao`.

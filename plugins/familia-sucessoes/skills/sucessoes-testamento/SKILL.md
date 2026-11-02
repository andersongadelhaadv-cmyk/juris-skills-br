---
name: sucessoes-testamento
description: >
  Elabora minuta de testamento (público, cerrado ou particular) e codicilo respeitando a
  legítima, e redige os pedidos de abertura, registro e cumprimento ou confirmação de
  testamento (CC arts. 1.857 a 1.990; CPC arts. 735 a 737). Use quando o usuário pedir
  testamento, minuta de testamento, testamento público, testamento particular, codicilo,
  cláusula de inalienabilidade, deserdação, abertura de testamento, cumprimento de
  testamento, confirmação de testamento particular, anulação de testamento.
metadata:
  area: familia-sucessoes
  tipo_peca: outro
  verificado_em: 2026-11-01
---
# Testamento: elaboração e cumprimento

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: planejar disposições de última vontade; escolher a forma; redigir cláusulas (legados, restrições com justa causa, deserdação, testamenteiro, reconhecimento de filho, disposições não patrimoniais); após o óbito, requerer abertura/registro/cumprimento (CPC 735 a 737).
- Não usar: doações em vida e estruturação patrimonial (use `sucessoes-planejamento-e-partilha-em-vida`); inventário (skills de inventário).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Testador: idade (16 anos ou mais), discernimento, capacidade de ler/assinar, deficiência visual ou auditiva.
2. Família: cônjuge/companheiro e regime; descendentes; ascendentes (herdeiros necessários).
3. Patrimônio estimado e bens que se quer destinar.
4. Beneficiários pretendidos e eventuais impedimentos (CC 1.801).
5. Restrições desejadas e a justa causa (se sobre a legítima).
6. Forma preferida e disponibilidade de testemunhas.
7. Após o óbito: tipo de testamento, quem o detém, certidão de óbito.

## Prazo e contagem
- Impugnar a validade do testamento: 5 anos do registro (CC 1.859).
- Anular disposição por erro, dolo ou coação: 4 anos do conhecimento do vício (CC 1.909 p.ú.).
- Provar causa de deserdação: 4 anos da abertura do testamento (CC 1.965 p.ú.).
- Testamenteiro cumpre e presta contas em 180 dias da aceitação, salvo prazo maior (CC 1.983).
- Prazos processuais via `prazos-processuais`.

## Estrutura da peça
Minuta: qualificação e capacidade → revogação de anteriores → herdeiros necessários e legítima → disposições sobre a parte disponível → legados → cláusulas restritivas → disposições não patrimoniais → testamenteiro → fecho conforme a forma. Pós-óbito: requerimento de abertura/registro/cumprimento ou de publicação e confirmação do particular. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Havendo herdeiros necessários (descendentes, ascendentes e cônjuge — CC 1.845; a 4ª Turma do STJ inclui o companheiro, por força da equiparação dos Temas 809 e 498 do STF — AgInt nos EDcl no REsp 1.982.343), só se dispõe da metade (CC 1.789, 1.845, 1.846); legítima não entra no testamento (CC 1.857 §1º).
- Testamento conjuntivo é proibido (CC 1.863).
- Formas ordinárias (CC 1.862): público (tabelião, 2 testemunhas, leitura e assinatura — CC 1.864); cerrado (aprovação pelo tabelião com 2 testemunhas — CC 1.868; vedado a quem não sabe ler, CC 1.872); particular (3 testemunhas — CC 1.876; sem testemunhas só em circunstâncias excepcionais declaradas, CC 1.879).
- Cego só pelo testamento público (CC 1.867).
- Cláusulas de inalienabilidade, impenhorabilidade e incomunicabilidade sobre a legítima exigem justa causa declarada (CC 1.848).
- Testamento e inventário: com testamento, inventário judicial ou extrajudicial com autorização do juízo do cumprimento (CPC 610; Res. CNJ 35, art. 12-B).

## Fundamentos verificados
CC 1.789, 1.801, 1.845 a 1.850, 1.857 a 1.879, 1.881, 1.900, 1.909, 1.911, 1.961 a 1.969, 1.973 a 1.975, 1.976 a 1.990; CPC 735 a 737. Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
Pós-óbito:
- [ ] Abertura e registro (cerrado: CPC 735) ou cumprimento (público: CPC 736) ou publicação e confirmação (particular: CPC 737).
- [ ] Intimação dos herdeiros não requerentes e do MP.
- [ ] Nomeação/termo do testamenteiro (ou dativo, CPC 735 §4º).
- [ ] Autorização para inventário extrajudicial, se todos forem capazes e concordes (Res. CNJ 35, art. 12-B).

## Checklist pré-protocolo
- [ ] Legítima calculada e respeitada (simular o monte com e sem colação).
- [ ] Beneficiários sem impedimento do CC 1.801/1.802.
- [ ] Justa causa redigida de forma concreta para cada cláusula restritiva sobre a legítima.
- [ ] Forma escolhida com número correto de testemunhas e sem testemunha beneficiária.
- [ ] Revogação expressa de testamentos anteriores, se desejada (CC 1.969).
- [ ] Orientação sobre registro em Central notarial e guarda do original (cerrado/particular).

## Erros a evitar
- Dispor de mais que a metade havendo herdeiros necessários (as disposições serão reduzidas, CC 1.967).
- Gravar a legítima sem justa causa ou com fórmula genérica.
- Usar testemunha que é herdeira, legatária ou parente próximo destes (CC 1.801, II).
- Deserdar sem indicar causa legal (CC 1.814, 1.962, 1.963) — e sem alertar que o beneficiado precisa prová-la (CC 1.965).
- Esquecer o rompimento do testamento pelo surgimento de descendente (CC 1.973).
- Testamento particular digitado com rasuras ou espaços em branco (CC 1.876 §2º).

## Integração com o núcleo
`prazos-processuais`, `verificacao-de-citacoes` (jurisprudência sobre flexibilização de formalidades), `fidelidade-factual`, `estilo-forense`; `juros-e-correcao` se houver legado em dinheiro com atualização.

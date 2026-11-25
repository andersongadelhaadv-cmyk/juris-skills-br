---
name: trabalhista-replica
description: >
  Redige a réplica trabalhista (manifestação do reclamante sobre a defesa e os
  documentos juntados pela reclamada), enfrentando fatos impeditivos,
  modificativos e extintivos, preliminares e prova documental, com distribuição
  do ônus da prova pelo art. 818 da CLT e Súmulas 212 e 338 do TST. Use quando o
  usuário pedir réplica trabalhista, impugnação à contestação na Justiça do
  Trabalho, manifestação sobre defesa e documentos, impugnar cartões de ponto,
  contracheques ou recibos juntados pela empresa.
metadata:
  area: trabalhista
  tipo_peca: outro
  verificado_em: 2026-11-25
---
# Réplica trabalhista (manifestação sobre defesa e documentos)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: reclamante intimado (em audiência ou por despacho) a se manifestar sobre a contestação e os documentos da reclamada.
- Usar também para manifestação sobre documentos novos juntados depois da defesa.
- Não usar: réplica em processo cível (`civel-replica`); defesa da empresa (`trabalhista-contestacao`); impugnação à conta de liquidação (`trabalhista-impugnacao-de-calculos`); razões finais (memoriais) — peça própria, depois da instrução.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Petição inicial e contestação completas, com a lista de documentos (ID do PJe).
2. Ata da audiência ou despacho que abriu o prazo, com a data da intimação.
3. Versão do cliente sobre cada fato novo trazido na defesa (justa causa, pagamento, compensação, jornada, função).
4. Para cada documento: o cliente reconhece a assinatura? O conteúdo é verdadeiro? Há marcações "britânicas" (horários sempre iguais)?
5. Provas que o reclamante ainda pretende produzir (testemunhas, perícia, exibição).
6. Número de empregados da reclamada (relevante para o controle de jornada).

## Prazo e contagem
- A CLT não fixa prazo próprio para réplica: vale o prazo assinado pelo juízo em audiência ou despacho. No silêncio, discute-se a aplicação subsidiária dos 15 dias dos arts. 350, 351 e 437, § 1º, do CPC (CLT art. 769; CPC art. 15).
- Contagem e dias úteis: `prazos-processuais`. Perder o prazo arrisca preclusão sobre documentos não impugnados.

## Estrutura da peça
Tempestividade → preliminares da defesa (rebater uma a uma) → prejudiciais (prescrição, decadência) → fatos impeditivos/modificativos/extintivos → impugnação dos documentos (por ID) → ônus da prova → provas a produzir → requerimentos. Roteiro em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Impugnação específica**: documento a documento, com ID e motivo (admissibilidade, autenticidade, falsidade ou conteúdo — CPC art. 436). Impugnação genérica ("impugnam-se todos os documentos") tende a não produzir efeito.
- **Fato novo na defesa** (justa causa, pagamento, pedido de demissão, compensação): rebater e indicar a prova contrária.
- **Ônus da prova**: CLT art. 818, I e II; possibilidade de distribuição diversa por decisão fundamentada antes da instrução (§§ 1º e 2º) — requerer na réplica se for o caso.
- **Jornada**: controles com horários uniformes são inválidos como prova (Súmula 338, III). Atenção: a Súmula 338, I, menciona empregador com mais de 10 empregados, mas o art. 74, § 2º, da CLT, na redação vigente, exige registro para estabelecimentos com mais de 20 trabalhadores — usar o critério legal e verificar o número de empregados.
- **Término do contrato negado**: ônus do empregador (Súmula 212).
- **Falsidade**: se a assinatura não é do reclamante, suscitar a falsidade (CPC art. 436, III) e requerer perícia.

## Fundamentos verificados
CLT arts. 769, 818, 847, parágrafo único, e 74, § 2º; CPC arts. 15, 350, 351, 436 e 437; Súmulas 212 e 338 do TST. Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Rejeição das preliminares e prejudiciais.
- Desconsideração dos documentos impugnados, ou perícia (grafotécnica, contábil) quando houver falsidade ou divergência de valores.
- Aplicação da Súmula 338 (presunção da jornada da inicial) quando cabível.
- Distribuição diversa do ônus da prova (art. 818, § 1º), com pedido de decisão antes da instrução.
- Exibição de documentos em poder da reclamada não juntados.
- Reiteração dos pedidos da inicial e protesto pelas provas.

## Checklist pré-protocolo
- [ ] Prazo conferido (ata/despacho) e contagem pelo núcleo `prazos-processuais`
- [ ] Cada preliminar e prejudicial respondida
- [ ] Tabela de documentos: ID, descrição, posição (reconhece/impugna) e motivo
- [ ] Cartões de ponto analisados (uniformidade, assinatura, períodos faltantes)
- [ ] Recibos e contracheques confrontados com extratos bancários
- [ ] Número de empregados conferido para o art. 74, § 2º
- [ ] Provas especificadas (testemunhas, perícia, exibição)
- [ ] Nada de taxa de juros ou índice: `juros-e-correcao`

## Erros a evitar
- Impugnação genérica de todos os documentos, sem ID nem motivo.
- Silenciar sobre fato extintivo novo (pagamento, quitação) e permitir que fique incontroverso.
- Confessar fato na réplica por excesso de narrativa.
- Usar o número de 10 empregados da Súmula 338 sem conferir a redação atual do art. 74, § 2º.
- Inovar o pedido na réplica (alterar causa de pedir depois da defesa exige concordância e controle do juízo) [VERIFICAR: limites de aditamento após a defesa no processo do trabalho, CPC art. 329 c/c CLT art. 769].

## Integração com o núcleo
`prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`, `juros-e-correcao`.

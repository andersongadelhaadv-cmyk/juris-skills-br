---
name: trabalhista-parecer-juridico
description: >
  Redige parecer jurídico trabalhista (consulta de empresa, sindicato ou
  trabalhador) com ementa, quesitos, fatos, análise da lei, da norma coletiva e
  da jurisprudência, riscos graduados e conclusão objetiva; trata do negociado
  sobre o legislado (CLT arts. 611-A e 611-B, Tema 1046 do STF) e da prescrição
  (art. 11). Use quando o usuário pedir parecer trabalhista, opinião legal sobre
  risco de passivo, validade de cláusula de acordo ou convenção coletiva,
  enquadramento de verba ou consulta sobre prática de RH.
metadata:
  area: trabalhista
  tipo_peca: parecer
  verificado_em: 2026-11-25
---
# Parecer jurídico trabalhista

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: consulta pontual que pede opinião técnica fundamentada e escrita (ex.: "a cláusula X da convenção é válida?", "esse prestador PJ gera vínculo?", "qual o risco de passivo desta prática?").
- Não usar: programa amplo de conformidade com diagnóstico e plano de ação (`trabalhista-compliance`); parecer sobre contrato civil ou empresarial (`contratos-parecer-sobre-contrato`); parecer societário (`soc-parecer-societario`); peça processual (`trabalhista-reclamacao`, `trabalhista-contestacao`).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Consulente e sua posição (empregador, empregado, sindicato, terceiro).
2. Quesitos, formulados pelo consulente ou reconstruídos e confirmados com ele.
3. Documentos: contratos, normas coletivas vigentes no período (com vigência e base territorial), regulamentos internos, holerites, controles, correspondências.
4. Período dos fatos (lei aplicável no tempo — antes ou depois da Lei 13.467/2017) e situação atual dos contratos.
5. Número de empregados e estabelecimentos envolvidos, se o tema for coletivo.
6. Uso pretendido do parecer (decisão interna, negociação, juntada em processo).

## Prazo e contagem
- Parecer não tem prazo processual, mas deve analisar a prescrição da pretensão do trabalhador: cinco anos, até dois anos após a extinção do contrato (CLT art. 11, caput); interrupção só por ajuizamento de reclamação (§ 3º).
- Se o parecer orienta prática contínua, registrar a data-base da análise e o gatilho de revisão (lei nova, tese nova, nova norma coletiva).
- Prazos de processos em curso: `prazos-processuais`.

## Estrutura da peça
Ementa → consulta e quesitos → fatos e documentos examinados → análise (lei, norma coletiva, jurisprudência) → riscos → respostas aos quesitos → conclusão e ressalvas. Roteiro em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Delimitação**: o parecer responde aos quesitos com base nos documentos recebidos; listar o que foi e o que não foi examinado.
- **Fontes e hierarquia**: na falta de disposição legal ou contratual, a Justiça do Trabalho decide pela jurisprudência, analogia, equidade, princípios, usos e costumes e direito comparado (CLT art. 8º, caput); súmulas não podem restringir direitos nem criar obrigações sem lei (§ 2º).
- **Norma coletiva**: exame limitado aos elementos essenciais do negócio jurídico, com intervenção mínima (art. 8º, § 3º; art. 611-A, § 1º). Prevalência sobre a lei nas matérias do art. 611-A; objeto ilícito nas do art. 611-B (ex.: normas de saúde, higiene e segurança, XVII — sendo que duração do trabalho e intervalos não se consideram normas de saúde para esse fim, parágrafo único).
- **Tema 1046 do STF**: constitucionalidade de normas coletivas que limitam ou afastam direitos, sem exigir contrapartida explícita, respeitados os direitos absolutamente indisponíveis — o núcleo do parecer é identificar se o direito tocado é indisponível.
- **Risco graduado**: provável, possível ou remoto, com o motivo em uma linha. Sem número de probabilidade inventado.
- **Valores**: estimativa de passivo só com memória de cálculo; juros e correção pelo núcleo `juros-e-correcao`.

## Fundamentos verificados
CLT arts. 8º (caput, §§ 2º e 3º), 11 (caput e § 3º), 611-A (caput e § 1º) e 611-B (caput, XVII e parágrafo único); Tema 1046 do STF. Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
Não há pedido: o parecer termina com **respostas numeradas aos quesitos** e **recomendações práticas** (o que manter, o que ajustar, o que documentar, quando revisar).

## Checklist pré-protocolo
- [ ] Quesitos confirmados com o consulente
- [ ] Lista de documentos examinados e não examinados
- [ ] Lei aplicável no tempo identificada
- [ ] Norma coletiva com vigência e base territorial conferidas
- [ ] Toda súmula, OJ e tema citados passaram por `verificacao-de-citacoes`
- [ ] Riscos graduados e justificados
- [ ] Prescrição analisada
- [ ] Conclusão responde a todos os quesitos, sem ambiguidade
- [ ] Ressalvas: data-base e gatilhos de revisão

## Erros a evitar
- Responder pergunta diferente da formulada.
- Citar súmula sem conferir vigência (súmulas do TST são revistas e canceladas com frequência).
- Tratar o Tema 1046 como autorização ampla: ele ressalva os direitos absolutamente indisponíveis.
- Confundir norma de saúde e segurança com regra de jornada e intervalo (art. 611-B, parágrafo único).
- Conclusão em "depende" sem dizer de quê.
- Prometer resultado judicial.

## Integração com o núcleo
`verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`, `juros-e-correcao`, `prazos-processuais`.

---
name: trabalhista-recurso-de-revista
description: >
  Redige recurso de revista ao TST contra acórdão de TRT em recurso ordinário
  (CLT art. 896), cumprindo os ônus do §1º-A (trecho do prequestionamento,
  indicação explícita da violação, impugnação analítica), demonstrando
  transcendência (art. 896-A) e evitando os óbices das Súmulas 126, 297 e 333 do
  TST. Use quando o usuário pedir recurso de revista, RR, recorrer ao TST,
  demonstrar transcendência, cotejo analítico, divergência jurisprudencial
  trabalhista ou contrarrazões ao recurso de revista.
metadata:
  area: trabalhista
  tipo_peca: recurso-revista
  verificado_em: 2026-11-01
---
# Recurso de revista

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: acórdão de TRT em RO, em dissídio individual, por divergência (art. 896 "a" e "b") ou violação literal de lei federal/afronta direta à CF ("c").
- Execução e agravo de petição: só por ofensa direta e literal à CF (art. 896 §2º; Súmula 266 do TST), salvo execução fiscal e CNDT (§10).
- Sumaríssimo: só contrariedade a súmula do TST, súmula vinculante do STF ou violação direta da CF (§9º).
- Não usar: acórdão de TRT em agravo de instrumento (Súmula 218 do TST); reexame de prova (Súmula 126 do TST).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
- Acórdão regional integral e acórdão de ED, com datas de publicação.
- Teses que se quer levar e o trecho exato do acórdão em que cada uma foi decidida.
- Dispositivos, súmulas, OJs e arestos que se pretende confrontar (com fonte e data).
- Valor da condenação, preparo já feito e situação de depósito recursal.

## Prazo e contagem
- 8 dias úteis (Lei 5.584/1970 art. 6º; CLT art. 775). Interposição perante a Presidência do TRT (art. 896 §1º).
- Se o acórdão foi omisso, opor ED antes (Súmula 297 II; Súmula 184 do TST), sob pena de preclusão.

## Estrutura da peça
Interposição ao Presidente do TRT; razões: transcendência; pressupostos extrínsecos; para cada tema — trecho do prequestionamento, dispositivo violado ou divergência, cotejo analítico, pedido. Roteiro em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Art. 896 §1º-A** (sob pena de não conhecimento): I) transcrever o trecho do acórdão que consubstancia o prequestionamento; II) indicar de forma explícita a violação ou contrariedade; III) impugnar todos os fundamentos, com demonstração analítica; IV) na preliminar de negativa de prestação jurisdicional, transcrever o trecho dos ED e o trecho da decisão que os rejeitou.
- **Prequestionamento**: tese explícita no acórdão (Súmula 297 I); se omisso, ED (II); persistindo a omissão após ED, a questão jurídica se considera prequestionada (III).
- **Transcendência** (art. 896-A): econômica, política, social ou jurídica (§1º). O TRT não examina transcendência (§6º); o relator no TST pode denegar monocraticamente (§2º).
- **Negativa de prestação jurisdicional**: indicar violação dos arts. 832 da CLT, 489 do CPC ou 93 IX da CF (Súmula 459 do TST).
- **Divergência**: atual (§7º), com prova da fonte e cotejo (§8º; Súmula 337 do TST); arestos de Turma do TST não servem para a alínea "a" (que exige outro TRT ou SDI).
- **Óbices**: reexame de fatos (Súmula 126), decisão conforme jurisprudência atual do TST (Súmula 333; art. 896 §7º), fundamento não impugnado (Súmula 422 I).
- **Preparo**: novo depósito até o valor da condenação (Súmula 128 I).

## Fundamentos verificados
CLT arts. 896, 896-A, 896-C, 897-A; Súmulas 126, 128, 184, 218, 266, 297, 333, 337, 422, 459 do TST. Detalhes em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Reconhecimento da transcendência; conhecimento por violação ou divergência (indicar a alínea); provimento com a reforma específica.
- Se a matéria for juros e correção, a tese a sustentar vem da skill `juros-e-correcao` (não escrever taxa aqui).

## Checklist pré-protocolo
- [ ] Para cada tema: trecho do acórdão transcrito entre aspas, com indicação de página/ID.
- [ ] Dispositivo, súmula ou OJ indicado explicitamente por tema.
- [ ] Cotejo analítico feito (tese do acórdão x tese do paradigma ou texto da norma).
- [ ] Todos os fundamentos autônomos do acórdão impugnados.
- [ ] Tópico de transcendência por tema, com o indicador do §1º.
- [ ] ED opostos quando havia omissão.
- [ ] Nenhum tema depende de rever prova.
- [ ] Depósito e custas comprovados.

## Erros a evitar
- Transcrever o acórdão inteiro sem destacar o trecho do prequestionamento.
- Pedir revisão do valor da prova ("a testemunha não merece crédito").
- Citar aresto de Turma do TST como paradigma da alínea "a".
- Esquecer o rol restrito do sumaríssimo e da execução.
- Citar súmula ou OJ sem conferir se foi cancelada ou alterada.

## Integração com o núcleo
`verificacao-de-citacoes` (todo aresto e súmula), `prazos-processuais`, `juros-e-correcao`, `fidelidade-factual`, `estilo-forense`.

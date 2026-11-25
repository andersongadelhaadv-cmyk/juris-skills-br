# Changelog

## v0.3.0 — 2026-11

Novo plugin `imobiliario`, com 22 skills (152 no total). Texto próprio; normas conferidas no Planalto e súmulas/precedentes no JuriBase (63 LEI, 96 CONFIRMADO, 32 VERIFICAR).

- imobiliario: despejo, renovatória, revisional de aluguel, locação residencial; cobrança e prestação de contas de condomínio; possessórias, imissão na posse, embargos de terceiro; usucapião judicial e extrajudicial; adjudicação compulsória; compra e venda, distrato na planta, revisão de financiamento SFH/SFI e FGTS; análise de matrícula, parecer, notificação; retificação de área, Reurb, loteamento irregular e incorporação.
- Temas do STJ ainda pendentes de julgamento (1.349, 1.420, 1.464, 1.465, 1.466) aparecem como risco, nunca como tese.
- nucleo: roteador e catálogo passam a encaminhar pedidos imobiliários.

## v0.2.0 — 2026-11

Novo plugin `contratos`, com 22 skills (130 no total). Texto próprio; normas conferidas no Planalto e súmulas/precedentes no JuriBase, registrados no `fontes.yaml` de cada skill (91 LEI, 78 CONFIRMADO, 21 VERIFICAR).

- contratos: elaboração, análise e revisão, parecer; prestação de serviços e prestação por PJ (mitigação de vínculo); compra e venda empresarial; locação comercial; franquia e COF; licença de software e SaaS; NDA; agência e distribuição; representação comercial; parceria e joint venture; comodato; cessão de direitos; cláusula penal; memorando de entendimentos; aditivo; distrato e rescisão; notificação de descumprimento; SLA; termo de responsabilidade.
- nucleo: roteador e catálogo passam a encaminhar pedidos de contrato.
- Itens não conferidos em fonte oficial ficam marcados com [VERIFICAR].

## v0.1.3 — 2026-11

Correções e conferências em fonte oficial nos plugins familia-sucessoes, consumidor e administrativo-licitacoes (PRs #21, #22 e #23). Com esta versão, os nove plugins passaram por conferência em fonte oficial.

- familia-sucessoes: **correções** — ITCMD não incide sobre previdência complementar, seguro e pecúlio (LC 227/2026, art. 150, III); avaliação de quotas pelo art. 154; regime de bens em contrato de união estável só vale para frente (STJ); sem prisão civil por alimentos indenizatórios; companheiro como herdeiro necessário (4ª Turma do STJ). Res. CNJ 35, art. 12-B, conferido.
- consumidor: **correções** — consignado entra no mínimo existencial (STF, ADPFs 1.005, 1.006 e 1.097); hipóteses de força maior no transporte aéreo (CBA art. 256, §§3º e 4º); tese literal do Tema 27/STJ; repetição em dobro contratual com prazo decenal. Inclui o Tema 1082/STJ (planos coletivos).
- administrativo-licitacoes: **correções** — oitiva prévia no MS coletivo e vedações à liminar declaradas inconstitucionais (ADI 4.296); improbidade conforme ADIs 7.156/7.236 e 7.042/7.043; juros compensatórios na desapropriação após a Lei 14.620/2023; decadência do MS em concurso conta do fim da validade (STJ, REsp 2.178.391).
- Itens não conferidos em fonte oficial continuam marcados com [VERIFICAR].

## v0.1.2 — 2026-11

Correções e conferências em fonte oficial nos plugins previdenciario, trabalhista e processo-civil (PRs #18, #19 e #20).

- previdenciario: **correções** — pensão por morte decorrente de acidente do trabalho é da Justiça Federal (STJ, CC 197.182); duração da pensão para cônjuge com duas tabelas pela data do óbito (texto da Lei 13.135/2015 até 2020; Portaria ME 424/2020 desde 01/01/2021); art. 77, §2º-A, alcança acidente de qualquer natureza; regimento do CRPS pela Portaria MPS 125/2026. Inclui o Tema 995/STJ (reafirmação da DER).
- trabalhista: **correções** — Tema 21 de IRR do TST trata de justiça gratuita (o de valor dos pedidos é o Tema 35); alcance da ADI 5766; faixas do art. 223-G orientativas; Tema 1389/STF (pejotização) com a situação da suspensão. Inclui IN 41/2018 e CLT art. 899, §§9º a 11.
- processo-civil: **correções** — CPC art. 337, §6º, trata só da arbitragem (incompetência relativa: art. 65); transição da relevância no REsp pela redação literal do art. 4º da Lei 15.484/2026. Confere Tema 988/STJ, ADI 5.941 e Súmula 115/STJ.
- Itens não conferidos em fonte oficial continuam marcados com [VERIFICAR].

## v0.1.1 — 2026-11

Correções e conferências em fonte oficial nos plugins nucleo, penal e tributario-fazenda.

- nucleo: intimações pelo DJEN e pelo Domicílio Judicial Eletrônico (Res. CNJ 455/2022 com a Res. 569/2024; CPC 224 e 231), com exemplo de contagem; taxa legal de juros descrita pela metodologia da Res. CMN 5.171/2024.
- penal: inovação de tese na tréplica do júri é vedada (STJ); Tema 1260/STJ trata da pronúncia; Tema 1084/STJ e argumento do Tema 1169/STF sob a Lei 15.358/2026; habeas corpus contra ato de turma recursal.
- tributario-fazenda: **correção** — o recurso voluntário ao CARF é de 20 dias úteis (art. 33 do Decreto 70.235, alterado pelo art. 173 da LC 227/2026), com a transição do ADI RFB 2/2026; recurso especial à CSRF e CTN art. 211-B; ADI 4.296.
- Itens não conferidos em fonte oficial continuam marcados com [VERIFICAR].

## v0.1.0 — 2026-11

Primeira versão pública.

- Plugins: nucleo, processo-civil, trabalhista, previdenciario, penal, tributario-fazenda, familia-sucessoes, consumidor, administrativo-licitacoes.
- Juros e correção atualizados pela Lei 14.905/2024, ADC 58 e EC 113/2021, centralizados no núcleo.
- Recurso especial com tópico de relevância (CPC, art. 1.035-A, Lei 15.484/2026).
- Normas conferidas nos dados abertos do Senado Federal; precedentes conferidos no JuriBase.
- Juros contra a Fazenda alinhados à EC 136/2025 em todas as skills; honorários em RPV não impugnada conforme o Tema 1190 do STJ.
- Prazo do recurso voluntário no CARF marcado para conferência (art. 33 do Decreto 70.235 não alterado pela LC 227/2026); art. 174, §1º, do CTN com a ressalva do veto ao novo caput.

---
name: eleitoral-aije
description: >
  Redige ação de investigação judicial eleitoral (AIJE) pelo rito do art. 22
  da LC 64/1990, por abuso de poder econômico ou político, uso indevido dos
  meios de comunicação, captação ilícita de sufrágio (art. 41-A), conduta
  vedada (art. 73) ou arrecadação e gastos ilícitos (art. 30-A da Lei
  9.504/1997). Use quando o usuário pedir AIJE, investigação judicial
  eleitoral, cassação de registro ou diploma por abuso, compra de votos,
  uso da máquina pública ou caixa dois na campanha.
metadata:
  area: eleitoral
  tipo_peca: inicial
  verificado_em: 2026-11-25
---
# Ação de investigação judicial eleitoral (AIJE)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: (a) abuso de poder econômico ou de autoridade e uso indevido de veículos ou meios de comunicação em benefício de candidato ou partido (LC 64/1990, art. 22); (b) captação ilícita de sufrágio (Lei 9.504/1997, art. 41-A); (c) conduta vedada a agente público (art. 73); (d) captação ou gasto ilícito de recursos (art. 30-A) — todas pelo rito do art. 22.
- Não usar: depois de 15 dias da diplomação, por abuso econômico, corrupção ou fraude — `eleitoral-aime`; defender o investigado — `eleitoral-defesa-abuso-de-poder`; propaganda irregular sem gravidade — `eleitoral-representacao-propaganda-irregular`; inelegibilidade preexistente ao registro — `eleitoral-impugnacao-registro-candidatura`; recurso — `eleitoral-recurso-eleitoral`; improbidade pelo mesmo fato — `adm-acao-popular` / `adm-defesa-em-improbidade`.

## Entradas mínimas (perguntar o que faltar; nunca supor fatos)
1. Eleição, cargo, circunscrição; candidatos titular e vice (chapa majoritária).
2. Fatos: quem praticou, quem se beneficiou, quando (antes ou depois do registro, da eleição, da diplomação), onde, alcance.
3. Prova disponível: documentos, mídias, ata notarial, até 6 testemunhas por parte; documentos em poder de terceiros ou bancos a requisitar.
4. Data da diplomação (limite dos arts. 30-A, 41-A, 73) e se já houve ação sobre o mesmo fato.
5. Qual hipótese legal se pretende (abuso, 41-A, 73, 30-A) — mudam legitimidade, prazo e sanção.

## Prazo e contagem
- Art. 30-A: até 15 dias da diplomação, por partido ou coligação (Lei 9.504/1997, art. 30-A, caput).
- Art. 41-A: até a data da diplomação (§ 3º). Art. 73: até a diplomação (§ 12).
- Abuso do art. 22: a lei não fixa termo; a procedência vale "ainda que após a proclamação dos eleitos" (art. 22, XIV). Termos inicial e final fixados pela jurisprudência do TSE [VERIFICAR: marco inicial e final da AIJE na jurisprudência do TSE — JuriBase sem cobertura do TSE].
- Rito: defesa em 5 dias; testemunhas em 5 dias; diligências em 3; alegações em 2; relatório em 3 (art. 22, I, V, VI, X, XII). Contagem: `prazos-processuais`.

## Estrutura da peça
Endereçamento → legitimidade → fatos → gravidade (art. 22, XVI) → prova e requisições → tutela de suspensão do ato (art. 22, I, "b") → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Legitimidade (art. 22, caput): partido, coligação, candidato ou MP Eleitoral. No art. 30-A, só partido ou coligação (caput).
- Competência: Corregedor-Geral (TSE) ou Regional (TRE); nas eleições municipais, o juiz eleitoral (LC 64/1990, art. 24).
- Polo passivo: beneficiário e quem contribuiu para o ato (a inelegibilidade alcança ambos — art. 22, XIV). Chapa majoritária: [VERIFICAR: Súmula 38 do TSE sobre litisconsórcio entre titular e vice — JuriBase sem cobertura do TSE].
- Gravidade, não potencialidade: não se exige demonstrar que o ato alterou o resultado, mas a gravidade das circunstâncias (art. 22, XVI).
- Ações sobre o mesmo fato: reunião (Lei 9.504/1997, art. 96-B).

## Fundamentos verificados
- LC 64/1990, arts. 19, 22 (I a XIV e XVI), 23 e 24; CF, art. 14, § 9º.
- Lei 9.504/1997, arts. 30-A, 41-A e 73, §§ 4º, 5º e 12.
- STF, Tema 986 (RE 1.096.029): novas eleições automáticas quando o eleito em pleito majoritário é cassado (CE, art. 224, § 3º).
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Notificação para defesa em 5 dias; suspensão liminar do ato, se relevante o fundamento e houver risco de ineficácia (art. 22, I, "b").
- Oitiva de até 6 testemunhas; requisição de documentos a terceiros e instituições de crédito (art. 22, VIII).
- Procedência: cassação do registro ou diploma do beneficiado e inelegibilidade por 8 anos do representado e de quem contribuiu (art. 22, XIV); no 41-A, também multa; no 73, multa e cassação (§§ 4º e 5º); no 30-A, negativa ou cassação do diploma (§ 2º).
- Remessa ao MP Eleitoral para as providências cabíveis (art. 22, XIV).

## Checklist pré-protocolo
- [ ] Hipótese legal definida (abuso / 41-A / 73 / 30-A) e prazo conferido
- [ ] Legitimidade conforme a hipótese (30-A só partido/coligação)
- [ ] Beneficiário e responsáveis no polo passivo; vice incluído na chapa majoritária
- [ ] Gravidade demonstrada com dados (alcance, valores, eleitorado)
- [ ] Rol de testemunhas (até 6) na inicial
- [ ] Ação anterior sobre o mesmo fato pesquisada (art. 96-B)

## Erros a evitar
- Usar o argumento de potencialidade em vez de gravidade (art. 22, XVI).
- Ajuizar o art. 30-A em nome de candidato (legitimidade é de partido ou coligação).
- Deixar passar a diplomação nos casos dos arts. 41-A e 73.
- Prova só testemunhal frágil para pedir cassação: junte documento e mídia.
- Omitir quem contribuiu para o ato e perder a inelegibilidade dele.

## Integração com o núcleo
`prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

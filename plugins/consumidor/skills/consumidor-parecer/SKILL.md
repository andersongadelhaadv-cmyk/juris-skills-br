---
name: consumidor-parecer
description: >
  Redige parecer jurídico de direito do consumidor (consulta escrita), para
  consumidor, fornecedor ou associação: incidência do CDC (arts. 2º, 3º, 17 e
  29; teoria finalista mitigada; Súmulas 297, 563 e 602 do STJ), regime de
  responsabilidade, validade de cláusulas e práticas (arts. 39 e 51),
  decadência e prescrição (arts. 26 e 27; Tema 1280 do STJ), riscos e
  recomendação. Use quando o usuário pedir parecer, opinião legal, consulta
  escrita ou análise de risco sobre relação de consumo, se o CDC se aplica a
  um contrato, se uma prática comercial ou política de vendas é abusiva, ou
  qual a chance de êxito antes de ajuizar ou de se defender.
metadata:
  area: consumidor
  tipo_peca: parecer
  verificado_em: 2026-11-25
---
# Parecer de direito do consumidor

Ferramenta de apoio; o advogado responsável revisa toda peça antes da entrega ao cliente.

## Quando usar / quando não usar
- Usar: consulta escrita que exige opinião fundamentada sobre relação de consumo — aplicabilidade do CDC, regularidade de prática comercial, oferta e publicidade, cláusulas de contrato-padrão, responsabilidade em incidente, prazos, risco de litígio individual ou coletivo.
- Serve aos dois lados: consumidor (chance de êxito) e fornecedor (conformidade e risco).
- Não usar:
  - Contrato civil ou empresarial sem relação de consumo: `contratos-parecer-sobre-contrato`.
  - Revisão de minuta com marcas de alteração: `contratos-analise-e-revisao-de-contrato` (aplicando o CDC se for o caso).
  - Peça processual pronta: a skill da ação (`consumidor-*`) ou da defesa (`consumidor-defesa-do-fornecedor`).
  - Proteção de dados pessoais (LGPD): skills `digital-*`.
  - Plano de saúde, imóvel, banco: usar o parecer geral, mas puxar fundamentos de `consumidor-plano-de-saude`, `imob-parecer-juridico-imobiliario`, `consumidor-contratos-bancarios-revisional`.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Quem consulta e qual a pergunta exata (uma ou mais questões, numeradas).
2. Fatos com datas e documentos: contrato, termos de uso, anúncios, política comercial, reclamações, notificações, autos de infração do Procon.
3. Perfil das partes: pessoa física ou jurídica; destinação do produto ou serviço; vulnerabilidade.
4. Setor regulado? (banco, seguro, saúde suplementar, telecom, energia, aviação, previdência complementar).
5. Há processo, inquérito civil ou procedimento administrativo em curso?
6. Finalidade do parecer: decidir se ajuíza, defender-se, ajustar prática, instruir negociação.
7. Prazo de entrega e destinatário (cliente leigo, diretoria, uso em juízo).

## Prazo e contagem
- Identificar e calcular no parecer: decadência por vício (art. 26: 30 ou 90 dias; obstação pela reclamação, § 2º, I) e prescrição por fato do produto ou serviço (art. 27: 5 anos do conhecimento do dano e da autoria).
- Pretensões fora dos arts. 26 e 27 (inadimplemento contratual, restituição): prazo não conferido em fonte oficial nesta skill [VERIFICAR via `verificacao-de-citacoes`].
- Prazos processuais eventualmente em curso: `prazos-processuais`.

## Estrutura da peça
Ementa → consulta e quesitos → fatos e documentos examinados → análise por quesito (norma, jurisprudência confirmada, aplicação ao caso, contra-argumento) → riscos (alto, médio, baixo) → conclusões respondendo cada quesito → recomendações práticas → ressalvas. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Delimitar o escopo: o parecer responde aos quesitos com base nos documentos recebidos; fatos não informados são ressalva, não suposição.
- Enfrentar a melhor tese contrária: parecer que só concorda não serve para decidir.
- Separar o que é lei, o que é jurisprudência dominante confirmada e o que é opinião do parecerista.
- Linguagem: ementa e conclusões compreensíveis ao leigo; fundamentação técnica no corpo.

## Fundamentos verificados
- CDC arts. 2º, 3º, 17 e 29 (conceitos e equiparações); art. 4º, III (harmonização e boa-fé); art. 6º (direitos básicos).
- CDC arts. 14 (responsabilidade objetiva), 25 (vedação de exoneração), 26 e 27 (decadência e prescrição), 30 e 35 (oferta), 39 (práticas abusivas), 46, 47 e 51 a 54 (contratos), 84 (tutela específica), 101, I (foro).
- Súmulas 297 (CDC e instituições financeiras), 563 (previdência complementar aberta, não fechada) e 602 (cooperativas habitacionais) do STJ.
- Teoria finalista mitigada: AgInt no AREsp 2.498.507.
- Tema 1280/STJ (REsp 2.124.717): vítima do evento é consumidora por equiparação (art. 17) e a prescrição é a do art. 27.
- Inversão do ônus não automática (REsp 1.971.102) — relevante para avaliar o risco probatório.
Detalhe em [fundamentos](references/fundamentos.md).

## Conteúdo essencial do parecer
- Resposta direta a cada quesito (sim, não, depende — e de quê).
- Classificação do risco com justificativa, sem percentual de êxito inventado.
- Medidas recomendadas e ordem (ex.: notificar, ajustar cláusula, provisionar, propor acordo, ajuizar).
- Documentos e provas que faltam e como obtê-los.
- Ressalvas: data-base do parecer, documentos examinados, pontos em [VERIFICAR].

## Checklist pré-entrega
- [ ] Quesitos transcritos e todos respondidos nas conclusões
- [ ] Documentos examinados listados
- [ ] Incidência do CDC decidida antes do mérito (e da regra setorial)
- [ ] Prazos de decadência e prescrição calculados
- [ ] Tese contrária enfrentada
- [ ] Toda súmula e precedente confirmados no JuriBase, com dados completos
- [ ] Valores e encargos remetidos ao núcleo `juros-e-correcao`
- [ ] Linguagem das conclusões acessível ao destinatário

## Erros a evitar
- Presumir que todo contrato com empresa é de consumo: PJ e insumo exigem análise de vulnerabilidade.
- Aplicar o CDC a previdência complementar fechada (Súmula 563 o afasta).
- Confundir decadência do vício (art. 26) com prescrição do fato do serviço (art. 27).
- Dar percentual de êxito sem base ou omitir o risco de sucumbência.
- Citar precedente sem número, órgão e data confirmados.

## Integração com o núcleo
`verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`, `juros-e-correcao`, `prazos-processuais`.

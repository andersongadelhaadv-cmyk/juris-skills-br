---
name: civel-parecer-juridico
description: >
  Redige parecer jurídico cível e processual civil (consulta escrita do
  cliente ou de colega): viabilidade de ação, defesa ou recurso, prescrição e
  decadência, cabimento e estratégia processual, risco de um processo em
  curso, efeitos de decisão ou de acordo, com relatório da consulta,
  premissas, fundamentação verificada, respostas aos quesitos e conclusão
  com grau de risco. Atividade privativa de advocacia (Lei 8.906/1994, art.
  1º, II), que independe de mandato (art. 5º, § 4º). Use quando o usuário
  pedir parecer, opinião legal, consulta escrita, análise de risco ou de
  viabilidade em matéria cível ou processual, due diligence de contencioso
  ou "vale a pena entrar com a ação / recorrer?".
metadata:
  area: processo-civil
  tipo_peca: parecer
  verificado_em: 2026-11-25
---
# Parecer jurídico cível e processual

Ferramenta de apoio; o advogado responsável revisa toda peça antes da entrega ao cliente.

## Quando usar / quando não usar
- Usar: consulta escrita que pede opinião fundamentada sobre direito civil geral ou processo civil — chance de êxito, prescrição, cabimento de medida ou recurso, risco de condenação, provisionamento de contingência, efeitos de sentença, de acordo ou de decisão interlocutória, estratégia entre caminhos alternativos.
- Serve a qualquer lado (autor, réu, terceiro) e a colega que pede segunda opinião.
- Não usar (há parecer especializado):
  - Contrato (validade, cláusulas, riscos): `contratos-parecer-sobre-contrato`; revisão de minuta: `contratos-analise-e-revisao-de-contrato`.
  - Relação de consumo: `consumidor-parecer`.
  - Imóvel, matrícula, locação: `imob-parecer-juridico-imobiliario`.
  - Sociedades: `soc-parecer-societario`; due diligence societária: `soc-due-diligence-societaria`.
  - Proteção de dados e direito digital: `digital-*`.
  - Quando o pedido é a peça processual em si, use a skill da peça (`civel-peticao-inicial`, `civel-contestacao`, `civel-apelacao` etc.).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Consulente e sua posição (quem pergunta, interesse, se há processo).
2. Perguntas exatas (quesitos). Se vierem vagas, reformule e peça confirmação antes de escrever.
3. Documentos: contrato, correspondências, petições, decisões, certidões, cálculos. Parecer sem documento é parecer sobre narrativa — dizer isso no texto.
4. Datas relevantes (fato, ciência, vencimento, citação, intimação) — essenciais para prescrição e prazos.
5. Processo em curso: número, fase, últimas decisões, prazos abertos.
6. Finalidade do parecer (decisão interna, provisionamento, juntada em processo, negociação) e destinatário.
7. Prazo para entrega e se há urgência processual (prazo correndo).

## Prazo e contagem
- Se houver prazo processual em curso, informe-o no início do parecer, com contagem pelo núcleo `prazos-processuais`; o parecer não pode fazer o cliente perder o prazo.
- Prescrição e decadência: identificar o termo inicial, as causas de interrupção e suspensão e a data provável de consumação; cada prazo citado vai ao `fontes.yaml` ou recebe `[VERIFICAR]`.
- Data-base do parecer: a análise vale para a lei e a jurisprudência da data de emissão — declarar.

## Estrutura da peça
Ementa → consulta e quesitos → documentos examinados e premissas → síntese dos fatos → fundamentação por questão → respostas objetivas aos quesitos → conclusão com grau de risco e recomendação → ressalvas → data e assinatura. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Privatividade**: consultoria e assessoria jurídicas são atividades privativas de advogado (Lei 8.906/1994, art. 1º, II); podem ser verbais ou escritas e independem de mandato ou contrato de honorários (art. 5º, § 4º).
- **Responsabilidade**: o advogado responde pelos atos profissionais praticados com dolo ou culpa (art. 32) — por isso premissas, ressalvas e fontes verificadas não são enfeite.
- **Fidelidade**: todo fato vem de documento indicado ou do relato do consulente, identificado como tal. Nada de presumir datas ou valores.
- **Citações**: só norma conferida e precedente confirmado (`verificacao-de-citacoes`). Jurisprudência divergente deve ser mostrada, não escondida.
- **Isenção**: o parecer opina; não promete resultado. Use escala de risco qualitativa (remoto, possível, provável) e explique o critério.
- **Sigilo**: parecer é documento do cliente; não identificar terceiros além do necessário.

## Fundamentos verificados
- Lei 8.906/1994, arts. 1º, II; 5º, § 4º; 32.
- Fundamentos de mérito: variam com a consulta — cada norma e precedente usado entra no `fontes.yaml` do trabalho e passa pelo núcleo `verificacao-de-citacoes`.
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos (conteúdo da conclusão)
- Resposta direta a cada quesito, numerada, em uma a três frases, antes de qualquer ressalva.
- Grau de risco por cenário, com o fator que mais pesa em cada um.
- Recomendação de conduta (ajuizar, defender, recorrer, negociar, aguardar, produzir prova), com prazo para agir.
- Providências imediatas (documentos a obter, notificação, preservação de prova, medida urgente).
- Valores em discussão: só com memória de cálculo do núcleo `juros-e-correcao`; sem índice de cabeça.

## Checklist pré-entrega
- [ ] Quesitos confirmados com o consulente.
- [ ] Lista de documentos examinados e de premissas assumidas.
- [ ] Prazos processuais e prescricionais calculados e destacados no início.
- [ ] Cada citação no `fontes.yaml`; nada de memória.
- [ ] Posições contrárias e jurisprudência desfavorável enfrentadas.
- [ ] Respostas objetivas antes das ressalvas.
- [ ] Grau de risco com critério explicado; nenhuma promessa de êxito.
- [ ] Data-base, local e assinatura com OAB.

## Erros a evitar
- Responder à pergunta que o advogado acha melhor, e não à que o cliente fez.
- Esconder a jurisprudência contrária ou apresentar tese minoritária como pacífica.
- Percentual de êxito sem base ("80% de chance") — prefira escala qualitativa justificada.
- Parecer longo sem conclusão clara na primeira página.
- Ignorar prazo correndo enquanto se analisa o mérito.
- Tratar relato do cliente como fato provado.

## Integração com o núcleo
`verificacao-de-citacoes`, `fidelidade-factual`, `prazos-processuais`, `juros-e-correcao`, `estilo-forense`. Se a conclusão for agir: `roteador-de-pecas` indica a peça.

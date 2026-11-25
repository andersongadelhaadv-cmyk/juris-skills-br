---
name: trib-parecer-tributario
description: >
  Redige parecer tributário consultivo geral (incidência, interpretação de
  norma, alcance de benefício, efeito de decisão judicial ou administrativa,
  risco de uma prática), com método de interpretação do CTN (arts. 107 a 112),
  proteção de quem segue norma complementar (art. 100), mudança de critério
  (art. 146) e precedentes vinculantes (art. 194-A). Use quando o usuário pedir
  parecer tributário, opinião legal sobre tributo, consulta sobre incidência,
  memorando de risco fiscal, análise de tese tributária ou resposta formal a
  dúvida de cliente sobre imposto ou contribuição.
metadata:
  area: tributario-fazenda
  tipo_peca: parecer
  verificado_em: 2026-11-25
---
# Parecer tributário consultivo

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo e todo parecer antes da entrega ao cliente.

Peça consultiva: responde uma pergunta delimitada, com fundamento conferido e grau de risco. Afirma apenas o que está na norma lida no dia ou em precedente confirmado; o resto vai marcado. Alíquota, base, percentual e valor: só de norma conferida ou do cálculo do cliente.

## Quando usar / quando não usar
- Usar: (a) incide ou não incide; (b) como interpretar dispositivo, isenção ou obrigação acessória; (c) qual o efeito, para o cliente, de decisão do STF/STJ, do CARF ou de solução de consulta; (d) risco de uma prática já adotada; (e) viabilidade de tese antes de ajuizar.
- Não usar:
  - Desenho de estrutura ou reorganização: `trib-planejamento-tributario`.
  - Revisão de rotinas e programa de conformidade: `trib-compliance-tributario`.
  - Reforma do consumo (IBS, CBS, IS): `trib-reforma-tributaria-ibs-cbs`.
  - Parecer sobre contrato em geral: `contratos-parecer-sobre-contrato`; societário: `soc-parecer-societario`.
  - Ação já decidida pelo cliente: skill da peça (`trib-mandado-de-seguranca`, `trib-repeticao-de-indebito`, `trib-acao-anulatoria`, `trib-declaratoria-inexistencia-relacao-tributaria`).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. A pergunta exata do cliente e para que ele usará a resposta.
2. Fatos: atividade, operação, partes, local, datas, valores informados.
3. Tributo(s) e ente(s) envolvidos; regime de apuração.
4. Documentos: contratos, notas, declarações, autuações, decisões recebidas.
5. Se já há consulta formal, processo administrativo ou judicial sobre o tema.
6. Data-base desejada da análise (a legislação muda; o parecer fala de uma data).

## Prazo e contagem
- Sem prazo processual próprio. Se o parecer recomendar medida com prazo (impugnação, recurso, ação, repetição), indicar a skill da peça e calcular em `prazos-processuais`.
- Para fatos passados, informar decadência (CTN, art. 150, § 4º; art. 173, I) e prescrição (art. 174).

## Estrutura da peça
Ementa → consulta → fatos e premissas → legislação aplicável na data-base → interpretação → jurisprudência e posição administrativa → riscos → conclusão objetiva (respostas numeradas às perguntas) → ressalvas. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Delimitar a pergunta: parecer que responde tudo não responde nada.
- Fixar a data-base da legislação e listar as normas lidas.
- Distinguir: texto da lei → posição administrativa (soluções de consulta, atos normativos) → jurisprudência (vinculante x persuasiva).
- Interpretação literal obrigatória para suspensão ou exclusão do crédito, isenção e dispensa de obrigação acessória (CTN, art. 111).
- Dúvida em matéria de infração ou penalidade favorece o acusado (CTN, art. 112).
- Analogia não cria tributo (CTN, art. 108, § 1º).

## Fundamentos verificados
- CTN, art. 100, parágrafo único: seguir norma complementar exclui penalidades, juros de mora e atualização da base — base para recomendar que o cliente documente a orientação seguida.
- CTN, art. 107, §§ 1º a 3º (LC 236/2026): consulta e pareceres jurídicos da administração; vinculação limitada ao órgão; solução vale só para o consulente.
- CTN, arts. 108, § 1º, 111 e 112.
- CTN, art. 146 (redação da LC 236/2026): mudança de critério jurídico só alcança fatos geradores posteriores, para o mesmo sujeito passivo.
- CTN, art. 194-A (LC 236/2026): decisão definitiva vinculante do STF ou STJ vincula a administração tributária.
- Lei 9.430/1996, art. 48: consulta federal em instância única, sem recurso; nova orientação só para fatos posteriores à ciência ou publicação (§ 12).
- Precedente específico do tema: confirmar cada um com `verificacao-de-citacoes` antes de citar; o que não for confirmado vai como `[VERIFICAR]`.
Detalhe em [fundamentos](references/fundamentos.md).

## Conclusão do parecer
- Responder cada pergunta em uma ou duas frases, na ordem da consulta.
- Graduar o risco (provável / possível / remoto) e dizer de onde vem a graduação.
- Indicar a medida recomendada: manter, corrigir, autorregularizar (`trib-compliance-tributario`), formular consulta, ajuizar (skill da peça).
- Encargos e atualização de valores: núcleo `juros-e-correcao`.

## Checklist pré-entrega
- [ ] Pergunta delimitada e reproduzida
- [ ] Data-base da legislação declarada
- [ ] Cada norma citada conferida no texto oficial
- [ ] Cada precedente confirmado (ou marcado `[VERIFICAR]`) e classificado como vinculante ou persuasivo
- [ ] Posição administrativa identificada (ou declarado que não foi localizada)
- [ ] Conclusão responde à pergunta, com grau de risco
- [ ] Nenhuma alíquota, percentual ou valor de memória
- [ ] Ressalvas de mudança legislativa e de lei estadual/municipal

## Erros a evitar
- Responder com doutrina genérica sem enfrentar o texto da norma aplicável.
- Citar ementa ou número de processo sem confirmação.
- Tratar acórdão isolado como "jurisprudência pacífica".
- Omitir a posição da administração, que é o que o cliente enfrentará primeiro.
- Esquecer que solução de consulta de terceiro não vincula a administração em favor do cliente da mesma forma que a dele.
- Concluir com "depende" sem dizer de quê.

## Integração com o núcleo
`verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`, `juros-e-correcao`, `prazos-processuais`.

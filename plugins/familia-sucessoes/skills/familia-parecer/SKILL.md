---
name: familia-parecer
description: >
  Redige parecer jurídico de direito de família (consulta escrita): regime de bens e o que
  se partilha, efeitos do pacto, alimentos (cabimento, valor, renúncia), guarda e
  convivência, via judicial ou extrajudicial, riscos e estratégia (CC arts. 1.583, 1.584,
  1.639 a 1.688, 1.694, 1.707, 1.725; CPC arts. 693, 694, 698, 731 e 733; STF Tema 1236).
  Use quando o usuário pedir parecer, opinião legal, consulta escrita, análise de risco ou
  "qual a chance" em divórcio, união estável, partilha, pensão alimentícia, guarda, regime
  de bens ou pacto antenupcial, antes de ajuizar, negociar ou assinar.
metadata:
  area: familia-sucessoes
  tipo_peca: parecer
  verificado_em: 2026-11-25
---
# Parecer de direito de família

Ferramenta de apoio; o advogado responsável revisa toda peça antes da entrega ao cliente.

## Quando usar / quando não usar
- Usar: consulta que pede opinião fundamentada sobre conflito ou planejamento familiar — o que entra na partilha, se o pacto protege um bem, se cabe ou quanto pedir de alimentos, chance de guarda unilateral, cartório ou juiz, risco de um acordo.
- Serve a qualquer polo; registre para quem é o parecer (conflito de interesses impede atender os dois cônjuges em litígio).
- Não usar:
  - peça pronta: `familia-divorcio`, `familia-uniao-estavel`, `familia-acao-de-alimentos`, `familia-revisional-e-exoneracao-de-alimentos`, `familia-execucao-de-alimentos`, `familia-guarda-e-convivencia`, `familia-investigacao-de-paternidade`, `familia-partilha-posterior-e-sobrepartilha`, `familia-acordo-extrajudicial-homologacao`;
  - minuta de pacto: `familia-pacto-antenupcial`;
  - herança, testamento, planejamento sucessório: `sucessoes-*`, `soc-holding-familiar`;
  - medida protetiva da Lei Maria da Penha: `penal-maria-da-penha-medidas-protetivas`;
  - quotas, empresa e acordo de sócios na partilha: puxar `soc-parecer-societario`.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Quem consulta, para quê (ajuizar, defender-se, negociar, assinar) e os quesitos numerados.
2. Estado civil e documentos: certidão de casamento, pacto, escritura ou sentença de união estável, decisões anteriores.
3. Datas-chave: casamento ou início da união, separação de fato, nascimento dos filhos, aquisição de cada bem.
4. Patrimônio com origem (anterior, herança, doação, sub-rogação, onerosa na constância) e dívidas.
5. Renda e despesas de cada parte; necessidades dos filhos; plano de saúde e escola.
6. Rotina dos filhos, histórico de convivência, mudança de cidade pretendida.
7. Violência doméstica, medidas protetivas ou processos criminais (pergunta obrigatória).
8. Processos em curso e prazos correndo.

## Prazo e contagem
- Identificar no parecer os prazos que importam ao caso e calculá-los com `prazos-processuais` (prazos processuais) e com a fonte oficial (prescrição e decadência).
- Partilha: o STJ tem tratado a pretensão de partilha como imprescritível (AgInt nos EDcl no AREsp 2.726.027, 3ª Turma, 2025); sobrepartilha tem julgados com prazo decenal — ver `familia-partilha-posterior-e-sobrepartilha`.
- Prescrição de prestações alimentares vencidas: confirmar o prazo e o termo inicial na fonte oficial antes de afirmar [VERIFICAR via `verificacao-de-citacoes`].

## Estrutura da peça
Ementa → consulta e quesitos → documentos examinados e fatos tomados como premissa → análise por quesito (norma, jurisprudência confirmada, aplicação, melhor tese contrária) → matriz de riscos → conclusões por quesito → recomendações (judicial x extrajudicial, provas a reunir, ordem das providências) → ressalvas. Roteiro em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Escopo delimitado: fatos não informados viram ressalva, não suposição.
- Separar lei, jurisprudência confirmada e opinião do parecerista; toda citação passa por `verificacao-de-citacoes`.
- Regime de bens primeiro: sem pacto, comunhão parcial (CC 1.640); maior de 70 sem pacto — separação obrigatória (CC 1.641, II), afastável por escritura (STF Tema 1236), com Súmula 377 STF e Súmula 655 STJ na conta.
- Via extrajudicial: só sem nascituro ou filho incapaz (CPC 733), salvo questões dos filhos já resolvidas em juízo — ver `familia-divorcio`; acordos sobre filhos exigem homologação com oitiva do MP (Lei 13.140, art. 3º § 2º).
- Guarda compartilhada é a regra, salvo recusa de um genitor ou probabilidade de risco de violência doméstica ou familiar (CC 1.584 § 2º).
- Alimentos: proporção entre necessidade e possibilidade (CC 1.694 § 1º); irrenunciáveis pelo credor (CC 1.707).

## Fundamentos verificados
CC 1.583, 1.584, 1.639 a 1.641, 1.658 a 1.660, 1.668, 1.672, 1.687, 1.694, 1.707, 1.725, 1.829, I, 1.845; CPC 53, I, 189, II, 693, 694, 698, 731, 733; Lei 13.140/2015, art. 3º; STF Tema 1236; Súmula 377 STF; Súmulas 197 e 655 STJ; STJ AgInt nos EDcl no AREsp 2.726.027. Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos (conclusões e recomendações)
- [ ] Resposta direta a cada quesito ("sim", "não", "depende de X"), antes da fundamentação.
- [ ] Grau de risco por tese (alto, médio, baixo), com o motivo.
- [ ] Recomendação de via: acordo extrajudicial, escritura, mediação ou ação, e por quê.
- [ ] Lista de documentos e provas a obter antes de agir.
- [ ] Providências urgentes (averbação, indisponibilidade, prova de violência, preservação de mensagens).
- [ ] Efeitos colaterais: tributários (ITCMD em partilha desigual, lei estadual), sucessórios (regime e herança), previdenciários.

## Checklist pré-entrega
- [ ] Quesitos copiados exatamente como formulados e todos respondidos.
- [ ] Regime de bens confirmado em documento, não em relato.
- [ ] Bens classificados como comuns ou particulares com a prova da origem.
- [ ] Pergunta sobre violência doméstica feita e registrada.
- [ ] Toda súmula, tema ou acórdão conferido; o que não foi conferido está marcado [VERIFICAR].
- [ ] Ressalvas de premissa fática e de data do parecer.

## Erros a evitar
- Prometer resultado em guarda ou alimentos (decisão depende de prova e de estudo psicossocial).
- Esquecer que o regime repercute na herança (CC 1.829, I) ao opinar sobre separação convencional.
- Tratar a união estável como casamento sem checar contrato escrito (CC 1.725) e prova do início da convivência.
- Opinar sobre partilha de quotas sem o contrato social e o balanço.
- Afirmar prazo prescricional de memória.

## Integração com o núcleo
`verificacao-de-citacoes`, `fidelidade-factual`, `prazos-processuais`, `juros-e-correcao` (alimentos atrasados, reposições — nunca fixar índice aqui), `estilo-forense`, `roteador-de-pecas` (para indicar a peça seguinte).

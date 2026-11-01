---
name: verificacao-de-citacoes
description: >
  Protocolo obrigatório para conferir, antes de qualquer uso, súmulas, temas,
  teses, acórdãos e dispositivos de lei citados em peças: consulta à base de
  jurisprudência (verificar_citacao e buscar_jurisprudencia) e à API de dados
  abertos do Senado para normas, com o tratamento de cada resultado e o padrão
  de citação (CPC arts. 489, §1º, V e VI, 926 e 927). Use quando o usuário
  pedir para conferir, checar ou validar jurisprudência, súmula, tema
  repetitivo, número de processo, artigo de lei, "isso existe?", "achar
  precedente", "fundamentar com julgado" ou revisar citações de uma peça.
metadata:
  area: nucleo
  tipo_peca: outro
  verificado_em: 2026-11-01
---
# Verificação de citações

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

Regra única: nada é citado de memória. Número de processo, relator, data,
órgão julgador, ementa, texto de súmula e redação de artigo só entram na peça
depois de conferidos na fonte, e com o link da fonte.

## Quando usar / quando não usar
- Usar: toda vez que o usuário, a skill de área ou o próprio modelo quiser incluir
  precedente, súmula, tema, OJ, enunciado ou dispositivo de lei; na revisão de peça
  pronta (inclusive da parte contrária, para apontar citação inexistente ou deturpada).
- Não usar para doutrina: livro e artigo não estão na base; exija do usuário a obra,
  edição e página, ou não cite.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
- O texto da citação como está (número, tribunal, classe, relator, data, trecho).
- A finalidade: tese que o precedente deve sustentar.
- Tribunais relevantes (vinculantes para o caso, tribunal local).

## Prazo e contagem
Não se aplica.

## Estrutura da peça
Para cada citação: verificar → classificar o estado → agir conforme a tabela →
registrar no fontes.yaml (skills) ou na lista de conferência (peças). Fluxo
completo e formato de citação em [estrutura](references/estrutura.md).

## Requisitos e preliminares
**Ferramentas** (carregar antes do uso): `verificar_citacao` (confere uma citação
concreta) e `buscar_jurisprudencia` (procura julgados por tema; aceita filtro de
tribunais, por exemplo ["STF","STJ","TST","TNU"]).

**Estados de `verificar_citacao` e o que fazer**
| Estado | Significado | Ação |
|---|---|---|
| CONFIRMADO | existe na base, com dados reais | use os dados devolvidos (não os informados), com o link `fonteUrl`; para súmula ou tema, confira vigência na página do tribunal |
| DIVERGENCIA | existe, mas algum dado difere | corrija pela versão real e avise o usuário do que mudou |
| NAO_ENCONTRADO | não está no escopo coberto | não afirme que não existe; retire o número, mantenha a tese em termos gerais com [VERIFICAR: conferir número e fonte] e peça a fonte ao usuário; não ofereça outro processo como se fosse o mesmo |
| INDISPONIVEL | a base não respondeu | tente uma vez mais; persistindo, marque [VERIFICAR] e nada conclua sobre a existência |

**Estados de `buscar_jurisprudencia`**
| Estado | Ação |
|---|---|
| ENCONTRADO | leia a ementa; use só o que for pertinente; cite com tribunal, classe, número, relator, data e link |
| SEM_RESULTADO | reformule a consulta (sinônimos, dispositivo legal, menos filtros) uma ou duas vezes |
| SEM_COBERTURA | a base não cobre; não preencha a lacuna com memória; diga isso ao usuário |

Um resultado ENCONTRADO prova a existência do julgado, não que ele decide o caso:
a pertinência é juízo profissional (CPC 489, §1º, V e VI).

**Sem acesso à base**: se as ferramentas não estiverem conectadas, diga isso ao
usuário, mantenha cada citação com [VERIFICAR: conferir no site oficial do
tribunal] e liste os links oficiais para a conferência manual. Não apresente a
peça como verificada.

## Fundamentos verificados
- Normas: API do Senado – `https://legis.senado.leg.br/dadosabertos/legislacao/lista?tipo=LEI&numero=<n>&ano=<aaaa>`
  (LCP para lei complementar, EMC para emenda, DEL para decreto-lei) devolve o
  identificador; a página `https://legis.senado.leg.br/norma/<id>` mostra alterações,
  vigência e o texto publicado. Dispositivo alterado recentemente ou que será
  transcrito: confira o texto, não só a ementa.
- CPC 926 e 927 (deveres de coerência e observância dos precedentes, inclusive o
  inciso III-A, incluído pela Lei 15.484/2026); CPC 489, §1º, V e VI (identificar
  fundamentos determinantes e distinguir); CPC 1.029, §1º (prova da divergência).
- Deveres de veracidade: CPC 77, I e II; CPC 80, II; EOAB art. 34, XIV.
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
Não se aplica diretamente. Na peça, a citação verificada sustenta o pedido; a
inexistente nunca.

## Checklist pré-protocolo
- [ ] Cada súmula, tema e acórdão passou por `verificar_citacao`.
- [ ] Dados usados são os devolvidos pela base, não os digitados pelo usuário.
- [ ] Toda citação traz tribunal, classe, número, relator (quando houver), data e link.
- [ ] Súmulas e temas: vigência conferida na página oficial (não cancelada, não superada).
- [ ] Ementa lida e relação com o caso explicada em uma ou duas frases.
- [ ] Nenhum NAO_ENCONTRADO foi mantido com número; todos viraram [VERIFICAR].
- [ ] Artigos de lei transcritos conferidos no texto vigente.

## Erros a evitar
- Citar "Tema X" sem dizer o tribunal: números de tema se repetem entre cortes.
- Transformar NAO_ENCONTRADO em "não existe" ou, ao contrário, em citação "confirmada".
- Trocar o precedente pedido por outro parecido sem avisar.
- Copiar ementa longa: transcreva só o trecho decisivo, entre aspas, com o link.
- Citar súmula já cancelada ou revisada.

## Integração com o núcleo
- `fidelidade-factual`: a mesma regra de não inventar vale para fatos do caso.
- `juros-e-correcao` e `prazos-processuais`: os precedentes delas já estão conferidos; novos acréscimos passam por aqui.
- `estilo-forense`: formato de citação e transcrição mínima.

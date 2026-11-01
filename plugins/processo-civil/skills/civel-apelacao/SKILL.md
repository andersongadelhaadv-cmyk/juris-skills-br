---
name: civel-apelacao
description: >
  Redige apelação cível e contrarrazões (CPC arts. 1.009 a 1.014), com preparo
  (art. 1.007), preliminares de interlocutórias não agraváveis (art. 1.009, §1º),
  efeito suspensivo (art. 1.012) e julgamento imediato do mérito pela causa
  madura (art. 1.013, §3º). Use quando o usuário pedir apelação, recurso contra
  sentença, razões de apelação, contrarrazões de apelação ou apelação adesiva.
metadata:
  area: processo-civil
  tipo_peca: apelacao
  verificado_em: 2026-11-01
---
# Apelação cível

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: contra sentença (art. 1.009), inclusive capítulo que decide tutela provisória (art. 1.013, §5º) ou matéria do art. 1.015 (art. 1.009, §3º).
- Usar para contrarrazões e para apelação adesiva (art. 997, §§1º e 2º).
- Não usar: decisão parcial de mérito (art. 356, §5º — agravo de instrumento); sentença de juizado (recurso inominado, `civel-juizado-especial`); sentença homologatória de conciliação no juizado.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
- Sentença integral, data da intimação e eventuais ED (e sua decisão).
- Capítulos que serão impugnados e capítulos aceitos.
- Interlocutórias não agraváveis que causaram prejuízo (para preliminar).
- Valor do preparo conforme tabela do tribunal; se há gratuidade ou isenção.
- Se há urgência em suspender os efeitos (sentenças do art. 1.012, §1º).

## Prazo e contagem
- 15 dias úteis (art. 1.003, §5º, c/c art. 219); dobra para Fazenda, MP, Defensoria.
- ED interrompem o prazo (art. 1.026).
- Feriado local: comprovar no ato; se não, o tribunal manda corrigir ou desconsidera se já constar do processo eletrônico (art. 1.003, §6º, Lei 14.939/2024).
- Preparo no ato; sem comprovação, recolhimento em dobro após intimação (art. 1.007, §4º). Use `prazos-processuais`.

## Estrutura da peça
Petição de interposição ao juízo de primeiro grau → razões ao tribunal: tempestividade, preparo, cabimento → síntese → preliminares (nulidade da sentença e interlocutórias do art. 1.009, §1º) → mérito por capítulo → pedido de efeito suspensivo (se for o caso) → causa madura → prequestionamento → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Art. 1.010: qualificação, fato e direito, razões de reforma ou nulidade, pedido de nova decisão.
- Dialeticidade: impugnar os fundamentos da sentença; o relator não conhece recurso que não os ataca (art. 932, III).
- Efeito suspensivo é a regra (art. 1.012); exceções no §1º (alimentos, tutela provisória, embargos do executado improcedentes etc.), com pedido ao tribunal ou ao relator (§§3º e 4º).
- Fato novo só por força maior (art. 1.014).
- Não há juízo de admissibilidade em primeiro grau (art. 1.010, §3º).

## Fundamentos verificados
CPC arts. 85, §11, 932, 997, 1.003, 1.007, 1.009 a 1.014; Súmula 484 do STJ. Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Conhecimento e provimento para reformar (error in iudicando) ou anular (error in procedendo) a sentença, capítulo por capítulo.
- Julgamento imediato do mérito, se presente hipótese do art. 1.013, §§3º e 4º.
- Efeito suspensivo, nas hipóteses do art. 1.012, §1º.
- Inversão da sucumbência; majoração ou não dos honorários recursais (art. 85, §11).
- Juros e correção, se impugnados, conforme `juros-e-correcao`.

## Checklist pré-protocolo
- [ ] Prazo de 15 dias úteis, com interrupção por ED considerada.
- [ ] Guia de preparo e porte (autos físicos) pagas e juntadas; ou gratuidade/isenção indicada.
- [ ] Feriado local comprovado, se influir na tempestividade.
- [ ] Cada fundamento da sentença atacado.
- [ ] Interlocutórias não agraváveis suscitadas em preliminar.
- [ ] Pedido de nova decisão claro (reforma, anulação, julgamento imediato).
- [ ] Prequestionamento dos dispositivos que irão a REsp/RE.

## Erros a evitar
- Copiar a inicial ou a contestação sem enfrentar a sentença.
- Esquecer interlocutória não agravável na preliminar: preclusão.
- Pedir só anulação quando o processo está maduro: peça também o julgamento imediato.
- Preparo insuficiente não complementado em 5 dias (art. 1.007, §2º); no recolhimento em dobro não há nova complementação (§5º).
- Juntar documento novo sem justificar (art. 435).

## Integração com o núcleo
- `prazos-processuais` para prazo, interrupção e preparo.
- `juros-e-correcao` para discutir índices e termos iniciais da condenação.
- `verificacao-de-citacoes` para todo precedente.
- `fidelidade-factual` para citações da sentença e da prova.
- `estilo-forense` na revisão.

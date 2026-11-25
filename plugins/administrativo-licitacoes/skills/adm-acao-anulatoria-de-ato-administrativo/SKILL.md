---
name: adm-acao-anulatoria-de-ato-administrativo
description: >
  Redige petição inicial de ação anulatória de ato administrativo pelo
  procedimento comum (CPC arts. 319 e 300), com controle de legalidade,
  motivação e proporcionalidade do ato (Lei 9.784/1999, arts. 2º, 50 e 53; LINDB
  arts. 20 a 22) e prescrição quinquenal do Decreto 20.910/1932. Use quando o
  usuário pedir anular ato administrativo na justiça, ação anulatória contra
  multa, sanção, indeferimento, cassação de licença, demissão, exclusão de
  programa, ato sem motivação ou desproporcional, com tutela de urgência para
  suspender os efeitos do ato.
metadata:
  area: administrativo-licitacoes
  tipo_peca: inicial
  verificado_em: 2026-11-25
---
# Ação anulatória de ato administrativo

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: ato administrativo concreto (sanção, multa não tributária, indeferimento, cassação, anulação ou revogação de benefício, exclusão de cadastro) que precisa ser desconstituído em juízo, com ou sem pedido de restituição ou indenização acessória; casos que exigem prova a produzir (perícia, testemunhas).
- Não usar:
  - prova toda pré-constituída e ato recente: avaliar `adm-mandado-de-seguranca`;
  - crédito tributário: `trib-acao-anulatoria`;
  - ainda há prazo de recurso administrativo e convém usá-lo: `adm-recurso-contra-auto-de-infracao` ou `adm-anulacao-de-ato-por-autotutela`;
  - sanção de licitação ainda na fase administrativa: `adm-defesa-em-processo-sancionador-licitacao`;
  - ato lesivo ao patrimônio público atacado por cidadão: `adm-acao-popular`;
  - pedido só de indenização: `adm-responsabilidade-civil-do-estado`;
  - concurso público: `adm-concurso-publico`; servidor punido em PAD, fase administrativa: `adm-defesa-em-pad`;
  - defesa da Fazenda: `fazenda-contestacao-fazendaria`.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Cópia integral do processo administrativo (pedir vista antes de redigir).
2. O ato atacado: autoridade, data, publicação ou ciência pessoal, conteúdo e motivação declarada.
3. Ente e entidade que praticaram o ato (União, Estado, Município, autarquia, fundação) — define réu e juízo.
4. Vícios que o cliente aponta: competência, forma, motivo, finalidade, objeto, contraditório, proporcionalidade.
5. Recursos administrativos interpostos, decisões e datas; se o processo ainda tramita.
6. Efeitos concretos atuais (multa em cobrança, inscrição em dívida ativa, atividade paralisada, perda de renda) e prova do perigo.
7. Valores pagos ou a restituir, se houver.
8. Normas específicas do setor (lei de trânsito, ambiental, sanitária, regulatória, estatuto local).

## Prazo e contagem
- Prescrição: em regra, 5 anos contados do ato ou fato (Decreto 20.910/1932, art. 1º); a prescrição não corre enquanto a Administração estuda requerimento do titular (art. 4º); interrompida, recomeça pela metade (art. 9º). Conferir se lei específica do setor fixa prazo próprio [VERIFICAR: conforme a matéria].
- Termo inicial: ciência da decisão final, ou do ato quando não houve recurso — registrar as duas datas.
- Prazos processuais e prerrogativas da Fazenda em juízo: `prazos-processuais`.

## Estrutura da peça (resumo; detalhe em [estrutura](references/estrutura.md))
Endereçamento e competência → partes (pessoa jurídica de direito público, não a autoridade) → síntese → fatos e trâmite administrativo → cabimento e prescrição → vícios do ato, um por tópico → consequências práticas (LINDB) → tutela de urgência → pedidos → provas → valor da causa.

## Requisitos e preliminares
- Réu: a pessoa jurídica que praticou o ato ou a que pertence o órgão; autoridade não é parte na ação comum.
- Requisitos da inicial do CPC, art. 319; juntar o processo administrativo.
- Não se exige esgotamento da via administrativa (CF, art. 5º, XXXV); se houver recurso pendente com efeito suspensivo, avaliar interesse e risco de decisões conflitantes.
- Competência: conforme o ente réu e a organização judiciária local [VERIFICAR: Justiça Federal, Fazenda Pública estadual ou Juizado da Fazenda conforme valor e matéria].
- Ato com efeitos já produzidos desfeito sem processo prévio: invocar o Tema 138 do STF.

## Fundamentos verificados (resumo; detalhe em [fundamentos](references/fundamentos.md))
- CF, art. 5º, XXXV, LIV e LV; art. 37, caput.
- Lei 9.784/1999: art. 2º (princípios e garantias, inc. X), art. 38 (provas consideradas na decisão), art. 50 (motivação obrigatória), art. 53 (dever de anular), art. 69 (aplicação subsidiária). Súmula 633/STJ para Estados e Municípios sem lei própria.
- LINDB, arts. 20, 21, 22 e 24.
- Súmula 473/STF ("ressalvada, em todos os casos, a apreciação judicial").
- Tema 138/STF (desfazimento com efeitos concretos exige processo administrativo).
- Decreto 20.910/1932, arts. 1º, 4º e 9º. CPC, arts. 300 e 319.

## Pedidos e requerimentos
- Tutela de urgência (CPC, art. 300) para suspender os efeitos do ato (exigibilidade da multa, inscrição, interdição), com prazo de cumprimento.
- Declaração de nulidade e desconstituição do ato e dos que dele dependam.
- Restituição do que foi pago por força do ato; juros e correção pelo núcleo `juros-e-correcao`.
- Subsidiariamente, redução da sanção por desproporcionalidade, quando a lei der margem.
- Exibição integral do processo administrativo, se negada a vista.
- Provas: documental, pericial e testemunhal especificadas.

## Checklist pré-protocolo
- [ ] Processo administrativo integral juntado
- [ ] Ato identificado com data de ciência; prescrição calculada
- [ ] Réu é a pessoa jurídica correta
- [ ] Cada vício em tópico próprio, ligado a documento
- [ ] Motivação do ato confrontada com a prova dos autos administrativos
- [ ] Consequências práticas da invalidação expostas (LINDB, arts. 20 e 21)
- [ ] Tutela com probabilidade e perigo concretos
- [ ] Lei específica do setor conferida
- [ ] Juros e correção remetidos ao núcleo

## Erros a evitar
- Pedir ao juiz que substitua o juízo de conveniência da Administração; o ataque é à legalidade, à motivação e à proporcionalidade.
- Alegar vício sem mostrar onde ele está no processo administrativo.
- Propor contra a autoridade (como no MS) em vez da pessoa jurídica.
- Ignorar o regime de transição e as orientações da época (LINDB, art. 24) quando o ato revisou situação consolidada.
- Esquecer a suspensão da prescrição durante requerimento administrativo pendente (Decreto 20.910/1932, art. 4º).

## Integração com o núcleo
`prazos-processuais`, `juros-e-correcao`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

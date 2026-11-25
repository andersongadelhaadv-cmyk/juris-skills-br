---
name: mil-indenizacao-acidente-em-servico
description: >
  Redige ação de indenização por danos morais, materiais e estéticos de militar
  (ou de seus dependentes, em caso de morte) vítima de acidente ou doença em
  serviço, contra a União ou o Estado (CF art. 37, § 6º), cumulável com reforma
  ou pensão, e, se houver defeito de equipamento, contra o fabricante. Use
  quando o usuário pedir indenização por acidente em serviço militar, lesão em
  treinamento ou instrução, morte de militar em serviço, dano moral do militar
  ferido ou pensão indenizatória por incapacidade decorrente do serviço.
metadata:
  area: militar
  tipo_peca: inicial
  verificado_em: 2026-11-25
---
# Indenização por acidente em serviço militar

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: lesão, doença ou morte de militar em serviço, treinamento, instrução, operação ou trajeto, com dano indenizável.
- Não usar: pedido só de reforma, reintegração ou adido — `mil-reintegracao-e-reforma` (pode ser cumulado); dano a civil causado por militar — `adm-responsabilidade-civil-do-estado`; acidente de trabalho de empregado celetista — `trabalhista-acidente-e-doenca-ocupacional`; benefício do INSS — `prev-acidentario`.

## Entradas mínimas (perguntar o que faltar; nunca supor fatos)
1. Data, local e dinâmica do acidente; atividade em curso; ordens recebidas; equipamentos de proteção.
2. Atestado de origem ou inquérito sanitário de origem; laudos, prontuários, inspeções de saúde.
3. Sequelas: incapacidade (grau, temporária ou permanente), dano estético, tratamentos futuros.
4. Situação funcional após o fato (reformado, licenciado, em atividade) e remuneração.
5. Despesas comprovadas; perda de renda; dependentes (em caso de morte).
6. Inquérito, sindicância ou IPM sobre o fato; equipamento defeituoso (fabricante identificado?).

## Prazo e contagem
- Contra a União ou o Estado: cinco anos do fato (Decreto 20.910/1932, art. 1º). Termo inicial quando a incapacidade só se consolida depois do acidente: conferir caso a caso [VERIFICAR].
- Contra o fabricante de arma ou equipamento defeituoso: o STJ aplicou o prazo quinquenal do CDC ao policial militar consumidor por equiparação (REsp 1.948.463).
- Contagem processual: `prazos-processuais`.

## Estrutura da peça
Competência → fatos → responsabilidade do Estado (nexo e dever de segurança) → danos → cumulação com reforma ou pensão → pedidos. Roteiro em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Competência: ação contra a União na Justiça Federal (CF art. 109, I); contra Estado, no juízo da Fazenda Pública estadual. Ação contra ato disciplinar não é o caso aqui (CF art. 125, § 4º).
- Responsabilidade do Estado pelos danos causados por seus agentes (CF art. 37, § 6º). O STJ reconhece a responsabilidade do Estado por dano moral decorrente de acidente nas atividades castrenses, mesmo sem previsão no Estatuto dos Militares (precedente transcrito no AgInt no REsp 1.818.950). Nesse mesmo julgado, faltou ato ilícito reconhecido na origem e o pedido não prosperou: descreva a falha concreta (ordem imprudente, falta de equipamento, treinamento sem segurança, demora no socorro). Debate sobre responsabilidade objetiva ou subjetiva nesse caso [VERIFICAR a linha atual].
- Cumulação: a reforma e a pensão têm natureza diversa da indenização civil; o STJ admite cumular indenização com pensão em caso de morte de militar em serviço (AgInt no REsp 1.826.414) e de servidor morto em serviço (REsp 1.511.942).
- Desligamento indevido de militar adoecido no serviço também gera dano moral (STJ, AgInt no AREsp 2.673.204) — cumular com `mil-reintegracao-e-reforma`.
- Prova: perícia médica (incapacidade, nexo, dano estético) e prova do fato (testemunhas da tropa, IPM, sindicância).

## Fundamentos verificados
- CF arts. 37, § 6º, 109, I; Lei 6.880/1980, arts. 108 e 110 (efeitos funcionais); Decreto 20.910/1932, art. 1º.
- STJ: AgInt no REsp 1.818.950, AgInt no REsp 1.826.414, REsp 1.511.942, AgInt no AREsp 2.673.204, REsp 1.948.463.
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Dano moral, com valor fundamentado (gravidade, sequela, idade, carreira interrompida).
- Dano estético, se houver, autônomo ao moral.
- Danos materiais: despesas comprovadas, tratamento futuro e pensão indenizatória pela perda ou redução da capacidade.
- Em caso de morte: dano moral dos familiares e pensão aos dependentes, sem compensar com a pensão militar.
- Juros e correção pelo núcleo `juros-e-correcao` (não definir taxa na peça).
- Perícia médica e produção de prova testemunhal; requisição do IPM ou sindicância.

## Checklist pré-protocolo
- [ ] Prescrição quinquenal conferida a partir do fato ou da consolidação
- [ ] Falha concreta do serviço descrita (não só "acidente em serviço")
- [ ] Atestado de origem ou ISO juntado
- [ ] Danos separados (moral, estético, material, pensão)
- [ ] Cumulação com reforma ou pensão explicada
- [ ] Fabricante incluído se houve defeito de equipamento

## Erros a evitar
- Pedir indenização apoiada só no fato de o acidente ser "em serviço", sem descrever a falha.
- Deduzir da indenização o valor da reforma ou da pensão militar.
- Fixar juros e correção no texto da peça em vez de remeter ao núcleo.
- Propor contra a pessoa jurídica errada (União x Estado) ou no juízo militar.

## Integração com o núcleo
`juros-e-correcao`, `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

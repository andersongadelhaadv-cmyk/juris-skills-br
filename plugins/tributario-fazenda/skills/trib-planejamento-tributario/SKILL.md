---
name: trib-planejamento-tributario
description: >
  Elabora parecer de planejamento tributário sobre estruturação de operações,
  reorganizações e escolhas de modelo de negócio, com teste de licitude
  (elisão x evasão x simulação), risco de desconsideração pelo art. 116,
  parágrafo único, do CTN (constitucionalidade mantida na ADI 2.446/STF),
  qualificação de multa (Lei 9.430/1996, art. 44, § 1º, e Lei 4.502/1964,
  arts. 71 a 73) e matriz de riscos. Use quando o usuário pedir planejamento
  tributário, parecer de estruturação, reorganização societária com efeito
  fiscal, análise de economia tributária lícita, teste de propósito negocial
  ou avaliação do risco de autuação de uma estrutura.
metadata:
  area: tributario-fazenda
  tipo_peca: parecer
  verificado_em: 2026-11-25
---
# Planejamento tributário — parecer de estruturação

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo e todo parecer antes da entrega ao cliente.

Esta skill produz PARECER sobre uma estrutura proposta ou já adotada. Não promete economia: compara cenários, aponta o fundamento legal de cada efeito e gradua o risco. Alíquota, base de cálculo, percentual de multa e valor só entram se vierem de norma conferida no dia ou de cálculo do próprio cliente; nunca de memória.

## Quando usar / quando não usar
- Usar: (a) escolha de regime ou de forma de organizar a atividade antes de operar; (b) reorganização (incorporação, cisão, segregação de atividades, nova sociedade) com efeito tributário; (c) revisão de estrutura já implantada para medir risco de autuação; (d) parecer para conselho, investidor ou auditoria sobre a defensabilidade de uma estrutura.
- Não usar:
  - Atos societários da holding familiar (contrato social, doação de quotas): `soc-holding-familiar`; decisão sucessória: `sucessoes-planejamento-e-partilha-em-vida`.
  - Impactos da reforma do consumo (IBS, CBS, IS): `trib-reforma-tributaria-ibs-cbs`.
  - Consulta pontual sobre interpretação de norma, sem desenho de estrutura: `trib-parecer-tributario`.
  - Rotinas de conformidade e revisão de obrigações: `trib-compliance-tributario`.
  - Autuação já lavrada: `trib-defesa-administrativa-e-carf`; débito inscrito: `trib-embargos-a-execucao-fiscal`.
  - Pedido de regime especial à administração: `trib-enquadramento-regime-especial`.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Objetivo do cliente em linguagem de negócio (não "pagar menos"): expandir, separar riscos, receber investidor, suceder, profissionalizar.
2. Situação atual: atividades, faturamento por linha, regime de apuração em cada tributo, estados e municípios envolvidos.
3. Estrutura proposta, passo a passo, com datas e ordem dos atos.
4. Substância de cada entidade: empregados, sede, ativos, contratos, decisões, riscos assumidos.
5. Cálculos de cenário do cliente ou da contabilidade (o parecer não inventa números).
6. Histórico fiscal: autuações, consultas formuladas, parcelamentos, ações judiciais.
7. Prazo desejado e quem será o destinatário do parecer.

## Prazo e contagem
- Não há prazo processual; há janelas de lei (opção de regime no início do período, prazo de alteração contratual, etc.). Cada janela citada no parecer precisa de norma conferida no dia [VERIFICAR a norma de cada janela].
- Revisão de estrutura antiga: mapear decadência (CTN, art. 150, § 4º, e art. 173, I) e lembrar que dolo, fraude ou simulação deslocam a contagem do lançamento por homologação para o art. 173, I. Cálculo de prazos: `prazos-processuais`.

## Estrutura da peça
Ementa → consulta e premissas → fatos e documentos recebidos → cenários comparados → licitude de cada passo (elisão x evasão x simulação) → risco do art. 116, parágrafo único → risco penal e de multa qualificada → matriz de riscos → recomendações e condições → ressalvas. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Delimite as premissas: o parecer vale para os fatos descritos e se torna inaplicável se a execução divergir.
- Separe três planos: (1) a norma permite o efeito? (2) os atos são reais e coerentes entre si? (3) a fiscalização tem instrumento legal para requalificar?
- Simulação é vício do negócio (CC, art. 167): ato aparente que não corresponde ao querido. Se houver, não é planejamento; recomende não executar.
- Sonegação, fraude e conluio (Lei 4.502/1964, arts. 71 a 73) levam à multa qualificada (Lei 9.430/1996, art. 44, § 1º) e podem configurar crime (Lei 8.137/1990, arts. 1º e 2º).
- Teto e gradação de multas têm regra geral nova no CTN, art. 113-A (LC 236/2026); os entes têm prazo de adaptação. Percentuais: só da norma conferida no dia.

## Fundamentos verificados
- CTN, art. 116, parágrafo único (LC 104/2001): a autoridade pode desconsiderar atos ou negócios praticados com a finalidade de dissimular o fato gerador ou a natureza dos elementos da obrigação, "observados os procedimentos a serem estabelecidos em lei ordinária".
- ADI 2.446/STF (rel. Min. Cármen Lúcia): pedido julgado improcedente por maioria em sessão virtual de 1º a 8/4/2022; acórdão publicado no DJe de 27/4/2022. O dispositivo segue válido. O alcance dos fundamentos (se a norma alcança só a dissimulação ou também o abuso de forma) deve ser lido no inteiro teor antes de citado [VERIFICAR: teor da ementa não conferido].
- Lei ordinária federal de procedimento do art. 116, parágrafo único: não conferida [VERIFICAR antes de afirmar que existe ou que falta].
- CTN, art. 149, VII, e art. 150, § 4º, parte final (dolo, fraude ou simulação).
- CTN, art. 108, § 1º: a analogia não pode resultar em tributo não previsto em lei.
- CTN, art. 146 (redação da LC 236/2026): mudança de critério jurídico só vale para fatos geradores posteriores, para o mesmo sujeito passivo.
- Consulta formal como redutor de risco: CTN, art. 107, §§ 1º a 3º (LC 236/2026), e Lei 9.430/1996, art. 48.
Detalhe em [fundamentos](references/fundamentos.md).

## Recomendações típicas do parecer
- Executar na ordem e nas datas indicadas, com atas, contratos e fluxos financeiros coerentes.
- Dar substância a cada entidade e documentar a razão de negócio de cada passo.
- Avaliar consulta formal antes da execução quando a tese for nova ou houver divergência administrativa.
- Reavaliar após mudança de lei, de critério da administração ou precedente vinculante (CTN, art. 194-A, LC 236/2026).
- Guardar a documentação até a prescrição (CTN, art. 195, parágrafo único).
- Atualização de valores e encargos: núcleo `juros-e-correcao`.

## Checklist pré-entrega
- [ ] Premissas fáticas listadas e validadas pelo cliente por escrito
- [ ] Cada cenário com fundamento legal conferido e número fornecido pelo cliente
- [ ] Teste de simulação (CC, art. 167) feito passo a passo
- [ ] Risco do art. 116, parágrafo único, enfrentado, com a ADI 2.446 citada sem extrapolar o que foi conferido
- [ ] Risco de multa qualificada e risco penal expostos sem percentual de memória
- [ ] Matriz de riscos (provável / possível / remoto) com justificativa
- [ ] Ressalvas de mudança legislativa e de lei estadual/municipal
- [ ] Nenhum `[VERIFICAR]` pendente no texto final

## Erros a evitar
- Vender "economia garantida" ou "risco zero"; o parecer gradua risco.
- Citar percentual, alíquota ou teto de multa de memória.
- Tratar a ADI 2.446 como aval a qualquer estrutura: ela manteve a norma de desconsideração.
- Ignorar a ordem e a cronologia dos atos: passos colados no tempo e sem função própria são o primeiro alvo da fiscalização.
- Planejar só o tributo federal e esquecer ITBI, ITCMD, ISS ou ICMS do caso.
- Dar parecer sem documentos, só com a narrativa do cliente.

## Integração com o núcleo
`verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`, `juros-e-correcao`, `prazos-processuais`.

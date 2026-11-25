---
name: trabalhista-compliance
description: >
  Estrutura diagnóstico e programa de compliance trabalhista para empresas:
  mapeamento de riscos (jornada e registro de ponto, igualdade salarial e
  relatório de transparência, saúde e segurança, assédio e canal de denúncias,
  terceirização e PJ), relatório de achados com plano de ação e políticas
  internas, com base na CLT, na Lei 14.457/2022 e na Lei 14.611/2023. Use quando
  o usuário pedir compliance trabalhista, auditoria trabalhista preventiva,
  diagnóstico de passivo, política antiassédio, canal de denúncias ou adequação
  à igualdade salarial.
metadata:
  area: trabalhista
  tipo_peca: outro
  verificado_em: 2026-11-25
---
# Compliance trabalhista

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: auditoria preventiva, diagnóstico de passivo antes de M&A ou de mudança de gestão, implantação ou revisão de políticas de RH, resposta a fiscalização ou a denúncia interna.
- Não usar: consulta pontual com quesitos (`trabalhista-parecer-juridico`); programa de integridade anticorrupção (`reg-programa-integridade-compliance`); adequação à LGPD dos dados de empregados (`digital-politica-de-privacidade-e-termos-de-uso`, `digital-contrato-dpa-operador`); due diligence societária ampla (`soc-due-diligence-societaria`); defesa em ação já ajuizada (`trabalhista-contestacao`).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Porte: número de empregados por estabelecimento, atividade e CNAE, unidades e estados.
2. Se tem CIPA, SESMT e qual a norma coletiva aplicável a cada categoria.
3. Amostra documental: contratos, controles de ponto, folhas, recibos de férias, ASOs, PGR/PCMSO, ordens de serviço de segurança, contratos de terceirização e de PJ.
4. Histórico: ações trabalhistas (quantidade e temas), autos de infração, TACs, denúncias internas.
5. Políticas existentes: código de conduta, política antiassédio, canal de denúncias, plano de cargos e salários.
6. Escopo combinado: todas as frentes ou só algumas; prazo e entregáveis.

## Prazo e contagem
- Passivo potencial: reclamações alcançam cinco anos, até dois anos após a extinção (CLT art. 11, caput). Delimitar a janela de auditoria por esse critério.
- Obrigações periódicas: capacitação antiassédio pelo menos a cada 12 meses (Lei 14.457/2022, art. 23, IV); relatório de transparência salarial semestral para empresas com 100 ou mais empregados (Lei 14.611/2023, art. 5º).
- Prazos de defesa administrativa ou judicial: `prazos-processuais`.

## Estrutura da peça
Escopo e método → mapa de riscos por frente → achados (fato, norma, risco, evidência) → plano de ação priorizado → políticas e minutas → cronograma de monitoramento. Roteiro em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Jornada**: estabelecimentos com mais de 20 trabalhadores devem anotar entrada e saída (CLT art. 74, § 2º). Conferir marcações uniformes, horas extras habituais e intervalos.
- **Saúde e segurança**: a empresa deve cumprir e fazer cumprir as normas de segurança e medicina do trabalho e instruir os empregados por ordens de serviço (CLT art. 157, I e II). Norma de saúde e segurança não pode ser reduzida por negociação coletiva (art. 611-B, XVII), mas duração do trabalho e intervalos não entram nessa categoria (parágrafo único).
- **Igualdade salarial**: mesma função e trabalho de igual valor, ao mesmo empregador e no mesmo estabelecimento, sem distinção de sexo, etnia, nacionalidade ou idade (CLT art. 461, caput). Empresas com 100 ou mais empregados: relatório semestral, plano de ação se houver desigualdade e multa administrativa de até 3% da folha, limitada a 100 salários mínimos (Lei 14.611/2023, art. 5º, §§ 2º e 3º).
- **Assédio e violência**: empresas com CIPA devem ter regras de conduta divulgadas, procedimento de denúncia com anonimato e apuração, inclusão do tema na CIPA e capacitação anual (Lei 14.457/2022, art. 23, I a IV). A ofensa à esfera moral ou existencial gera dano extrapatrimonial (CLT art. 223-B).
- **Terceirização e PJ**: avaliar subordinação, pessoalidade e habitualidade nos contratos de PJ e de terceiros — remeter a análise de cada caso a `trabalhista-vinculo-de-emprego` [VERIFICAR: base legal da terceirização (Lei 6.019/1974) e teses do STF antes de citar].
- **Sigilo e dados**: apurações internas tratam dados pessoais e, por vezes, sensíveis; acesso restrito e registro de quem acessou.

## Fundamentos verificados
CLT arts. 11, 74, § 2º, 157, I e II, 223-B, 461 e 611-B, XVII e parágrafo único; Lei 14.457/2022, art. 23; Lei 14.611/2023, art. 5º. Detalhe em [fundamentos](references/fundamentos.md).

## Cláusulas essenciais (políticas e plano de ação)
- Política antiassédio: definições, condutas vedadas, canal, anonimato, vedação de retaliação, rito de apuração, sanções, capacitação anual.
- Política de jornada: registro, horas extras com autorização, banco de horas conforme norma coletiva, intervalos.
- Política de remuneração: critérios objetivos de cargos e salários, revisão periódica de equidade.
- Plano de ação: achado, medida, responsável, prazo, evidência de conclusão.

## Checklist pré-protocolo
- [ ] Escopo e amostra documentados (o que foi e o que não foi auditado)
- [ ] Número de empregados por estabelecimento conferido (limiares de 20 e 100)
- [ ] Cada achado com norma, evidência e grau de risco
- [ ] Normas coletivas vigentes conferidas por categoria e base territorial
- [ ] Plano de ação com responsável e prazo
- [ ] Estimativa de passivo, se houver, com memória de cálculo e `juros-e-correcao`
- [ ] Citações de jurisprudência passadas por `verificacao-de-citacoes`
- [ ] Dados pessoais minimizados no relatório

## Erros a evitar
- Relatório genérico, sem evidência ou sem norma por achado.
- Usar o limiar de 10 empregados da Súmula 338 do TST no lugar dos 20 do art. 74, § 2º vigente.
- Implantar canal de denúncias sem rito de apuração e sem proteção contra retaliação.
- Tratar o relatório de transparência como só formalidade: desigualdade exige plano de ação.
- Afirmar regularidade de PJ ou terceirização sem examinar a prática real.

## Integração com o núcleo
`juros-e-correcao`, `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

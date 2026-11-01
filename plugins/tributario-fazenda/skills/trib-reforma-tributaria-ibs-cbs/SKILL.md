---
name: trib-reforma-tributaria-ibs-cbs
description: >
  Elabora parecer consultivo sobre a reforma tributária do consumo (EC 132/2023,
  LC 214/2025 e alterações da LC 227/2026): IBS, CBS, Imposto Seletivo, ano-teste
  de 2026, cronograma de transição 2027-2033, créditos, split payment e impactos
  no contrato e na formação de preço. Use quando o usuário pedir parecer, análise
  de impacto, consulta, memorando ou planejamento sobre IBS, CBS, Imposto
  Seletivo, reforma tributária, fim do PIS/Cofins, ICMS e ISS, transição ou
  regimes diferenciados.
metadata:
  area: tributario-fazenda
  tipo_peca: parecer
  verificado_em: 2026-11-01
---
# Parecer sobre a reforma tributária do consumo (IBS, CBS e IS)

Ferramenta de apoio; o advogado responsável revisa todo parecer antes de entregá-lo ao cliente.

Esta skill produz PARECER (peça consultiva), não petição. Afirme apenas o que está no texto normativo conferido; marque como [VERIFICAR] regulamentos, atos do Comitê Gestor e normas posteriores não confirmadas.

## Quando usar / quando não usar
- Usar: consulta sobre enquadramento de operações, alíquotas de transição, créditos, regimes diferenciados e específicos, split payment, obrigações acessórias do ano-teste, cláusulas contratuais de reequilíbrio, comparação de cenários.
- Não usar: litígio já instaurado (use a skill da peça cabível, p.ex. `trib-mandado-de-seguranca`, `trib-defesa-administrativa-e-carf`); cálculo de atualização de débitos (use `juros-e-correcao`).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
- Atividade, CNAE, NCM/NBS dos principais bens e serviços; regime de apuração atual (lucro real, presumido, Simples Nacional).
- Estados e Municípios de origem e destino das operações; perfil dos clientes (contribuintes ou consumidores finais).
- Estrutura de custos e de insumos (para estimar créditos); contratos de longo prazo vigentes.
- Pergunta exata do cliente e horizonte temporal (2026, 2027-2028, 2029-2032, 2033).

## Prazo e contagem
Não há prazo processual. Datas-chave do cronograma (texto conferido):
- **2026 (ano-teste)**: IBS estadual de 0,1% e CBS de 0,9% (ADCT art. 125; LC 214 arts. 343 e 346); valores compensáveis com PIS/Cofins ou ressarcíveis (LC 214 art. 348); dispensa de recolhimento para quem cumpre as obrigações acessórias (art. 348, §1º); não se aplicam ao Simples Nacional (art. 348, III, c). Autuação por descumprimento de acessória em 2026: prazo de 60 dias para sanar, com extinção da penalidade (art. 348, §§3º e 4º, LC 227/2026).
- **2027**: cobrança da CBS e do Imposto Seletivo; extinção de PIS e Cofins; IPI a zero, salvo Zona Franca de Manaus (ADCT art. 126).
- **2027-2028**: IBS de 0,05% estadual + 0,05% municipal; CBS reduzida em 0,1 ponto (ADCT art. 127; LC 214 arts. 344 e 347).
- **2029-2032**: ICMS e ISS reduzidos a 9/10, 8/10, 7/10 e 6/10 das alíquotas (ADCT art. 128).
- **2033**: extinção do ICMS e do ISS (ADCT art. 129).
- Confira a vigência de cada dispositivo da LC 214 no art. 544 (efeitos escalonados).

## Estrutura do parecer
Ementa → consulta → documentos analisados → síntese normativa → análise por tema → riscos e pontos em aberto → conclusões numeradas → recomendações práticas. Roteiro em [estrutura](references/estrutura.md).

## Requisitos e cautelas
- Base legal mínima: CF arts. 156-A e 195, V; ADCT arts. 125 a 133; LC 214/2025 com redação da LC 227/2026.
- Normas posteriores (Senado): LC 235/2026, art. 6º (art. 82, §11, I da LC 214: exigência de receita de exportação superior a 30% da receita bruta nos três anos anteriores; art. 174, §12: alíquotas de fevereiro de 2026 como referência da carga dos combustíveis com alíquota reduzida entre março e junho de 2026). Decreto 12.955/2026 regulamenta a CBS; Decreto 13.133/2026 delega ao Ministro da Fazenda a divulgação das alíquotas da CBS sobre certos combustíveis. Leia o texto do decreto antes de aplicar ao caso.
- ADIs 7.779 e 7.790 (acórdãos de 03/08/2026), segundo a ficha da LC 214 no Senado: inconstitucionalidade de parte do texto do art. 149, II, b e c, e do art. 150, §1º (alíquota zero na compra de automóveis por pessoas com deficiência e com TEA); declarados constitucionais o art. 149, §1º, o art. 150, IV e §1º (ADI 7.779) e o art. 152, II (ADI 7.790). Qual parte do texto caiu: ler os acórdãos no STF antes de opinar [VERIFICAR].
- Não afirme alíquotas de referência definitivas: dependem de resolução do Senado (ADCT art. 130) e do cálculo da LC 214 (arts. 353 e seguintes).
- Separe com clareza o que é texto legal, o que é interpretação e o que depende de regulamento.
- Contencioso administrativo do IBS e prazos da CBS: LC 227/2026 (Comitê Gestor e processo administrativo do IBS; Decreto 70.235 art. 37, §5º para CBS).

## Fundamentos verificados
EC 132/2023; LC 214/2025 arts. 1º, 2º, 10, 12, 14, 26, 27, 31 a 33, 39, 47, 343 a 348, 353, 544; LC 227/2026; ADCT arts. 125 a 133. Detalhe em [fundamentos](references/fundamentos.md).

## Conclusões e recomendações (modelo)
- Conclusões numeradas, cada uma com o dispositivo que a sustenta e o grau de segurança (texto expresso / interpretação / depende de regulamento).
- Recomendações: ajustes de cadastro e documento fiscal, revisão de cláusulas de preço e reequilíbrio, mapeamento de créditos, simulação por ano da transição, monitoramento normativo.

## Checklist pré-entrega
- [ ] Cada afirmação normativa com artigo e versão conferida (LC 214 com LC 227/2026).
- [ ] Datas do cronograma conferidas no ADCT e na LC 214, art. 544.
- [ ] Regulamentos e atos do Comitê Gestor marcados [VERIFICAR] se não lidos.
- [ ] Cenários numéricos rotulados como estimativa, com premissas explícitas.
- [ ] Nenhuma alíquota de referência apresentada como definitiva.
- [ ] Ressalva sobre alterações normativas posteriores à data do parecer.

## Erros a evitar
- Tratar o ano de 2026 como de cobrança efetiva sem mencionar compensação e dispensa (LC 214 art. 348).
- Aplicar as alíquotas do ano-teste ao Simples Nacional.
- Afirmar a extinção de ICMS/ISS antes de 2033.
- Citar regulamento, resolução do Comitê Gestor ou norma de 2026 sem conferir no Senado ou no DOU.
- Transformar parecer em promessa de economia fiscal.

## Integração com o núcleo
- `fidelidade-factual`: conferência de dados do cliente (NCM, operações, contratos).
- `verificacao-de-citacoes`: qualquer precedente ou decisão de ADI citada.
- `prazos-processuais`: só se houver prazo administrativo envolvido (ex.: 60 dias do art. 348, §3º).
- `juros-e-correcao`: atualização de valores em simulações de passivo.
- `estilo-forense`: revisão final do texto.

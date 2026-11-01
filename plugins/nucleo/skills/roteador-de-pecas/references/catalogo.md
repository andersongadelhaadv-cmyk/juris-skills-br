# Catálogo de skills por área

Lista gerada a partir das pastas `plugins/*/skills/` em 01/11/2026. Outras áreas podem
ter sido acrescentadas depois; se o usuário pedir uma peça que não aparece aqui, confira
as pastas antes de dizer que não existe. A descrição completa e os gatilhos de cada
skill estão no respectivo SKILL.md.

Toda skill de área usa as do núcleo: `fidelidade-factual`, `verificacao-de-citacoes`,
`estilo-forense`, `prazos-processuais` e, nos pedidos em dinheiro, `juros-e-correcao`.

## Núcleo (transversal) (plugin `nucleo`)

| Skill | Para quê |
|---|---|
| `estilo-forense` | Guia de redação e formatação de peças processuais: clareza, parágrafos curtos, tópicos numerados, pedidos em alíneas, transcrição mínima,... |
| `fidelidade-factual` | Camada anti-alucinação de toda peça: impede inventar fatos do caso, datas, valores, documentos, dispositivos, precedentes ou doutrina; separa fato... |
| `juros-e-correcao` | Define o regime de correção monetária e juros de mora de qualquer crédito judicial conforme a natureza da dívida e o período, redige o pedido e... |
| `prazos-processuais` | Calcula e confere prazos processuais no cível, trabalhista, penal, juizados e contra a Fazenda, com termo inicial por modo de intimação, prazo em... |
| `roteador-de-pecas` | Hub de entrada do repositório: a partir do pedido do usuário, identifica área, fase processual, polo e tipo de peça e indica a skill certa, com... |
| `verificacao-de-citacoes` | Protocolo obrigatório para conferir, antes de qualquer uso, súmulas, temas, teses, acórdãos e dispositivos de lei citados em peças: consulta à... |

## Processo civil (plugin `processo-civil`)

| Skill | Para quê |
|---|---|
| `civel-acao-monitoria` | Redige ação monitória, fundada em prova escrita sem eficácia de título executivo, e também embargos monitórios do réu. |
| `civel-agravo-de-instrumento` | Redige agravo de instrumento cível contra decisão interlocutória do rol do art. 1.015 ou, excepcionalmente, fora dele pela taxatividade mitigada,... |
| `civel-agravo-interno` | Redige agravo interno contra decisão monocrática de relator ou outra decisão unipessoal em tribunal, com impugnação específica dos fundamentos e... |
| `civel-alegacoes-finais` | Redige alegações finais cíveis — debates orais ou razões finais escritas — ao fim da instrução, com análise da prova produzida por ponto... |
| `civel-apelacao` | Redige apelação cível e contrarrazões, com preparo, preliminares de interlocutórias não agraváveis, efeito suspensivo e julgamento imediato do... |
| `civel-contestacao` | Redige contestação no procedimento comum cível, com preliminares do art. 337, impugnação específica dos fatos e concentração de toda a defesa. |
| `civel-cumprimento-de-sentenca` | Redige requerimento de cumprimento de sentença cível: pagar quantia, provisório, obrigação de fazer/não fazer e entregar coisa e contra a Fazenda... |
| `civel-embargos-a-execucao` | Redige embargos à execução de título extrajudicial, com as matérias do art. 917, excesso de execução com valor e demonstrativo, pedido de efeito... |
| `civel-embargos-de-declaracao` | Redige embargos de declaração cíveis contra omissão, contradição, obscuridade ou erro material, inclusive para prequestionamento e com pedido de... |
| `civel-excecao-de-pre-executividade` | Redige exceção de pré-executividade em execução ou cumprimento de sentença, restrita a matérias conhecíveis de ofício que dispensam dilação... |
| `civel-execucao-titulo-extrajudicial` | Redige petição inicial de execução de título extrajudicial por quantia certa, com demonstrativo do débito, indicação de bens, averbação e pedido... |
| `civel-impugnacao-ao-cumprimento` | Redige impugnação ao cumprimento de sentença com as matérias do §1º, excesso de execução com valor e demonstrativo e pedido de efeito suspensivo. |
| `civel-juizado-especial` | Redige peças do Juizado Especial Cível: pedido inicial, contestação com pedido contraposto e recurso inominado, com limites de valor, prazos em... |
| `civel-peticao-inicial` | Redige petição inicial de procedimento comum cível conforme os arts. 319 e 320 do CPC, com cálculo do valor da causa, pedido de tutela provisória... |
| `civel-reconvencao` | Redige reconvenção, dentro da contestação ou isolada, com conexão, valor da causa próprio e requisitos de petição inicial. |
| `civel-recurso-especial` | Redige recurso especial cível ao STJ, com tópico obrigatório de relevância da questão federal, prequestionamento e prevenção dos óbices das... |
| `civel-recurso-extraordinario` | Redige recurso extraordinário cível ao STF, com preliminar formal e fundamentada de repercussão geral e prequestionamento da questão constitucional. |
| `civel-replica` | Redige réplica nos termos dos arts. 350, 351 e 437 do CPC, rebatendo preliminares, fatos impeditivos, modificativos ou extintivos e documentos novos. |
| `civel-tutela-provisoria` | Redige pedido de tutela provisória cível: urgência antecipada ou cautelar, em caráter antecedente ou incidental, e tutela da evidência. |

## Trabalhista (plugin `trabalhista`)

| Skill | Para quê |
|---|---|
| `trabalhista-acidente-e-doenca-ocupacional` | Estrutura pedidos decorrentes de acidente do trabalho e doença ocupacional: estabilidade de 12 meses, reintegração ou indenização substitutiva,... |
| `trabalhista-acordo-extrajudicial` | Redige a petição conjunta de homologação de acordo extrajudicial na Justiça do Trabalho, com advogados distintos para cada parte, discriminação... |
| `trabalhista-agravo-de-instrumento` | Redige agravo de instrumento trabalhista contra decisão que denega seguimento a recurso, em especial ao recurso de revista e ao recurso ordinário,... |
| `trabalhista-agravo-de-peticao` | Redige agravo de petição contra decisões do juiz na execução trabalhista, com a delimitação justificada das matérias e dos valores impugnados... |
| `trabalhista-contestacao` | Redige contestação trabalhista apresentada até a audiência, com preliminares, prescrição bienal e quinquenal, impugnação específica de cada pedido... |
| `trabalhista-embargos-a-execucao` | Redige embargos à execução trabalhista após a garantia do juízo ou a penhora, com as matérias do §1º, a impugnação da sentença de liquidação e a... |
| `trabalhista-embargos-de-declaracao` | Redige embargos de declaração no processo do trabalho contra sentença ou acórdão, em 5 dias, para sanar omissão, contradição, obscuridade, erro... |
| `trabalhista-impugnacao-de-calculos` | Redige impugnação fundamentada aos cálculos de liquidação trabalhista no prazo comum de 8 dias, com indicação de itens e valores sob pena de... |
| `trabalhista-insalubridade-periculosidade` | Estrutura pedido ou defesa sobre adicional de insalubridade e de periculosidade, com perícia obrigatória, base de cálculo, não cumulação, EPI e... |
| `trabalhista-mandado-de-seguranca` | Redige mandado de segurança na Justiça do Trabalho contra ato judicial sem recurso próprio com efeito suspensivo, em especial tutela provisória... |
| `trabalhista-reclamacao` | Redige petição inicial trabalhista com pedidos certos, determinados e com valor, escolha de rito ordinário ou sumaríssimo, gratuidade e honorários... |
| `trabalhista-recurso-de-revista` | Redige recurso de revista ao TST contra acórdão de TRT em recurso ordinário, cumprindo os ônus do §1º-A, demonstrando transcendência e evitando os... |
| `trabalhista-recurso-ordinario` | Redige recurso ordinário trabalhista contra sentença de Vara do Trabalho ou acórdão de TRT em competência originária, com preparo completo:... |
| `trabalhista-rescisao-indireta` | Estrutura o pedido de rescisão indireta do contrato de trabalho por falta grave do empregador, com enquadramento na alínea correta, prova da... |
| `trabalhista-vinculo-de-emprego` | Estrutura o pedido de reconhecimento de vínculo de emprego pelos requisitos do art. 3º da CLT — pessoa física, pessoalidade, não eventualidade,... |

## Penal (plugin `penal`)

| Skill | Para quê |
|---|---|
| `penal-agravo-em-execucao` | Redige agravo em execução penal e contrarrazões, processado pelo rito do recurso em sentido estrito, contra decisões do juiz da execução sobre... |
| `penal-alegacoes-finais` | Redige alegações finais da defesa por memoriais e roteiro para debates orais, com preliminares, mérito absolutório, teses subsidiárias de... |
| `penal-anpp` | Prepara requerimento de acordo de não persecução penal, pedido de remessa ao órgão superior do Ministério Público após recusa e impugnação de... |
| `penal-apelacao-criminal` | Redige a petição de interposição e as razões de apelação criminal da defesa, inclusive contra decisões do Tribunal do Júri, com efeitos, prazos de... |
| `penal-dosimetria` | Analisa e impugna a dosimetria da pena pelo critério trifásico, com regime inicial, substituição, sursis, detração e súmulas do STJ e do STF sobre... |
| `penal-habeas-corpus` | Redige habeas corpus liberatório ou preventivo, com definição da autoridade coatora e do tribunal competente, pedido liminar e enquadramento nas... |
| `penal-liberdade-provisoria-e-relaxamento` | Redige pedidos de relaxamento de prisão ilegal, liberdade provisória com ou sem fiança, revogação ou substituição de preventiva por cautelares e... |
| `penal-livramento-condicional` | Redige pedido de livramento condicional e defesa contra sua revogação, com cálculo das frações, requisitos subjetivos e vedações legais do art.... |
| `penal-maria-da-penha-medidas-protetivas` | Redige pedido de medidas protetivas de urgência em favor da ofendida e, do lado do requerido, manifestação, pedido de revogação ou modulação e... |
| `penal-plenario-do-juri` | Prepara a atuação da defesa no plenário do Tribunal do Júri: rol do art. 422, recusas, roteiro de debates, réplica e tréplica, apartes, quesitação... |
| `penal-progressao-de-regime` | Redige pedido de progressão de regime, com cálculo da fração pela data do fato, data-base, requisito subjetivo e exame criminológico. |
| `penal-recurso-em-sentido-estrito` | Redige recurso em sentido estrito e contrarrazões, com enquadramento no rol do art. 581, juízo de retratação e pedido de efeito suspensivo ou ativo. |
| `penal-resposta-a-acusacao` | Redige a resposta à acusação do procedimento comum e do júri e a defesa prévia da Lei de Drogas, com preliminares, pedido de absolvição sumária e... |
| `penal-revisao-criminal` | Redige revisão criminal contra condenação transitada em julgado, nas hipóteses de contrariedade à lei ou à evidência dos autos, prova falsa e... |

## Previdenciário (plugin `previdenciario`)

| Skill | Para quê |
|---|---|
| `prev-acidentario` | Prepara a ação acidentária contra o INSS na Justiça Estadual, com demonstração de nexo causal ou epidemiológico e pedido de auxílio-acidente,... |
| `prev-aposentadoria-especial` | Estrutura a ação de aposentadoria especial ou de reconhecimento e conversão de tempo especial no RGPS, com análise de PPP/LTCAT e dos limites de... |
| `prev-beneficio-por-incapacidade` | Prepara ação de concessão ou restabelecimento de auxílio por incapacidade temporária e de aposentadoria por incapacidade permanente, com foco em... |
| `prev-bpc-loas` | Estrutura o pedido judicial de benefício de prestação continuada à pessoa com deficiência ou idosa de 65 anos ou mais, incluindo renda per capita... |
| `prev-inicial-aposentadoria` | Monta a petição inicial de concessão de aposentadoria do RGPS contra o INSS, enquadrando o segurado na regra permanente ou nas transições da EC... |
| `prev-pedido-de-uniformizacao-tnu` | Redige pedido de uniformização de interpretação de lei federal no Juizado Especial Federal, dirigido à Turma Regional ou à Turma Nacional de... |
| `prev-pensao-por-morte` | Monta o pedido de pensão por morte no RGPS, com dependência, qualidade de segurado do falecido, termo inicial, cotas e duração por idade do... |
| `prev-recurso-crps` | Redige recurso ordinário às Juntas de Recursos e recurso especial às Câmaras de Julgamento do Conselho de Recursos da Previdência Social contra... |
| `prev-requerimento-administrativo` | Prepara o requerimento administrativo de benefício ao INSS pelo Meu INSS, com conferência do CNIS, rol de documentos e cuidado com o interesse de... |
| `prev-revisao-de-beneficio` | Avalia e redige ação de revisão de benefício do RGPS, começando pelo controle da decadência de 10 anos e da prescrição quinquenal, e filtra teses... |
| `prev-rpps-servidor` | Orienta pedido administrativo ou ação de aposentadoria e abono de permanência de servidor público federal no RPPS da União após a EC 103/2019, com... |
| `prev-tempo-rural-e-segurado-especial` | Estrutura o reconhecimento de tempo rural e da condição de segurado especial para aposentadoria por idade rural, híbrida ou averbação, com início... |

## Família e sucessões (plugin `familia-sucessoes`)

| Skill | Para quê |
|---|---|
| `familia-acao-de-alimentos` | Redige petição inicial de ação de alimentos, inclusive alimentos gravídicos e alimentos avoengos, com pedido de provisórios. |
| `familia-divorcio` | Redige divórcio litigioso ou consensual, com partilha, guarda, convivência, alimentos e nome, a partir da EC 66/2010, CPC arts. 693 a 699-A e 731... |
| `familia-execucao-de-alimentos` | Redige o requerimento de cumprimento de sentença ou execução de alimentos pelo rito da prisão ou da expropriação, com protesto, desconto em folha... |
| `familia-guarda-e-convivencia` | Redige ação de guarda e de regulamentação de convivência, modificação de guarda e incidente de alienação parental. |
| `familia-investigacao-de-paternidade` | Redige ação de investigação de paternidade, cumulada ou não com alimentos e petição de herança, com pedido de exame de DNA. |
| `familia-revisional-e-exoneracao-de-alimentos` | Redige ação revisional e ação de exoneração de alimentos, com base na mudança da situação financeira das partes e na Súmula 358 do STJ para filho... |
| `familia-uniao-estavel` | Redige ação de reconhecimento e dissolução de união estável, com partilha, alimentos e efeitos sucessórios. |
| `sucessoes-inventario-extrajudicial` | Prepara inventário e partilha por escritura pública, inclusive com herdeiro menor ou incapaz e com testamento nas hipóteses admitidas. |
| `sucessoes-inventario-judicial` | Redige a abertura de inventário judicial e suas peças pelo CPC arts. 610 a 673, com orientação sobre ITCMD. |
| `sucessoes-planejamento-e-partilha-em-vida` | Elabora parecer consultivo de planejamento sucessório e minutas de doação com reserva de usufruto, partilha em vida e estrutura societária,... |
| `sucessoes-testamento` | Elabora minuta de testamento e codicilo respeitando a legítima, e redige os pedidos de abertura, registro e cumprimento ou confirmação de testamento. |

## Consumidor (plugin `consumidor`)

| Skill | Para quê |
|---|---|
| `consumidor-acao-indenizatoria` | Redige petição inicial de ação indenizatória em relação de consumo, com responsabilidade objetiva dos arts. 12 a 14 do CDC, inversão do ônus da... |
| `consumidor-contratos-bancarios-revisional` | Redige ação revisional de contrato bancário de consumo, com aplicação do CDC às instituições financeiras, controle de juros remuneratórios,... |
| `consumidor-defesa-do-fornecedor` | Redige contestação do fornecedor em ação de consumo, com as excludentes dos arts. 12, § 3º, e 14, § 3º, do CDC, ausência de dano, culpa exclusiva... |
| `consumidor-negativacao-indevida` | Redige ação declaratória de inexistência de débito cumulada com cancelamento de inscrição em cadastro de inadimplentes e indenização por dano... |
| `consumidor-plano-de-saude` | Redige ação de obrigação de fazer com tutela de urgência contra operadora de plano de saúde por negativa de cobertura, com base na Lei 9.656/1998,... |
| `consumidor-repeticao-em-dobro` | Estrutura o pedido de repetição do indébito em dobro do art. 42, parágrafo único, do CDC, com a tese da Corte Especial do STJ, sua modulação... |
| `consumidor-superendividamento` | Redige o pedido de repactuação de dívidas do consumidor superendividado, com plano de pagamento em até 5 anos e preservação do mínimo existencial. |
| `consumidor-transporte-aereo` | Redige ação indenizatória contra companhia aérea por atraso, cancelamento, overbooking ou extravio/avaria de bagagem, definindo o regime... |
| `consumidor-vicio-do-produto-ou-servico` | Redige inicial por vício de qualidade ou quantidade de produto ou serviço, com as alternativas dos arts. 18 a 20 do CDC e controle da decadência... |

## Tributário e Fazenda Pública (plugin `tributario-fazenda`)

| Skill | Para quê |
|---|---|
| `fazenda-contestacao-fazendaria` | Redige contestação em nome da Fazenda Pública, com prazo em dobro e intimação pessoal, indisponibilidade do interesse público e atenção à remessa... |
| `fazenda-cumprimento-contra-a-fazenda` | Redige requerimento de cumprimento de sentença contra a Fazenda Pública para pagamento de quantia, com demonstrativo discriminado, expedição de... |
| `fazenda-execucao-fiscal-inicial` | Redige petição inicial de execução fiscal pela Fazenda Pública, com CDA conforme LEF art. 2º, §5º e CTN art. 202, providências prévias exigidas... |
| `trib-acao-anulatoria` | Redige ação anulatória de débito fiscal, com pedido de tutela ou depósito integral para suspender a exigibilidade. |
| `trib-defesa-administrativa-e-carf` | Redige impugnação administrativa a auto de infração e recurso voluntário ao CARF no processo administrativo fiscal federal, observando as normas... |
| `trib-embargos-a-execucao-fiscal` | Redige embargos à execução fiscal, com garantia prévia do juízo, prazo de 30 dias e concentração de toda a defesa. |
| `trib-excecao-pre-executividade-fiscal` | Redige exceção de pré-executividade em execução fiscal, sem garantia do juízo, restrita a matérias conhecíveis de ofício que não exijam dilação... |
| `trib-mandado-de-seguranca` | Redige mandado de segurança tributário, repressivo ou preventivo, com base na Lei 12.016/2009, inclusive para declarar o direito à compensação. |
| `trib-prescricao-intercorrente` | Analisa e redige petição de reconhecimento de prescrição intercorrente, prescrição originária e decadência tributária em execução fiscal. |
| `trib-reforma-tributaria-ibs-cbs` | Elabora parecer consultivo sobre a reforma tributária do consumo: IBS, CBS, Imposto Seletivo, ano-teste de 2026, cronograma de transição... |
| `trib-repeticao-de-indebito` | Redige ação de repetição de indébito tributário, com prazo de 5 anos, prova do encargo nos tributos indiretos e opção entre precatório e compensação. |

## Administrativo e licitações (plugin `administrativo-licitacoes`)

| Skill | Para quê |
|---|---|
| `adm-acao-popular` | Redige petição inicial de ação popular para anular ato lesivo ao patrimônio público, à moralidade administrativa, ao meio ambiente ou ao... |
| `adm-concurso-publico` | Redige mandado de segurança ou ação de procedimento comum em concurso público: direito à nomeação, preterição, eliminação ilegal, exigências do... |
| `adm-defesa-em-improbidade` | Redige contestação, manifestação e peças de defesa em ação de improbidade administrativa: dolo específico, tipicidade estrita, prescrição do art.... |
| `adm-defesa-em-pad` | Redige defesa escrita, requerimentos, recurso e pedido de revisão em sindicância ou processo administrativo disciplinar de servidor público federal. |
| `adm-defesa-em-processo-sancionador-licitacao` | Redige defesa prévia, alegações finais, recurso ou pedido de reconsideração de licitante ou contratado em processo de responsabilização da Lei... |
| `adm-desapropriacao-defesa` | Redige contestação do expropriado e manifestações em ação de desapropriação por utilidade pública: impugnação do preço, imissão provisória,... |
| `adm-impugnacao-ao-edital` | Redige impugnação a edital de licitação ou pedido de esclarecimento com base na Lei 14.133/2021, art. 164. |
| `adm-mandado-de-seguranca` | Redige petição inicial de mandado de segurança individual ou coletivo contra ato de autoridade pública, com pedido de liminar. |
| `adm-pedido-de-reequilibrio-economico-financeiro` | Redige pedido administrativo de restabelecimento do equilíbrio econômico-financeiro, revisão, reajuste ou repactuação de contrato administrativo. |
| `adm-recurso-em-licitacao` | Redige recurso administrativo, contrarrazões ou pedido de reconsideração em licitação regida pela Lei 14.133/2021: julgamento de propostas,... |
| `adm-responsabilidade-civil-do-estado` | Redige petição inicial de ação indenizatória contra o Estado ou prestadora de serviço público com base na responsabilidade objetiva da CF art. 37,... |

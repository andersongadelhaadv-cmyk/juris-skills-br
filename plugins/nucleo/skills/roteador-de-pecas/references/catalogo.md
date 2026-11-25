# Catálogo de skills por área

Lista gerada a partir das pastas `plugins/*/skills/` em 01/11/2026. Outras áreas podem
ter sido acrescentadas depois; se o usuário pedir uma peça que não aparece aqui, confira
as pastas antes de dizer que não existe. A descrição completa e os gatilhos de cada
skill estão no respectivo SKILL.md.

Toda skill de área usa as do núcleo: `fidelidade-factual`, `verificacao-de-citacoes`,
`estilo-forense`, `prazos-processuais` e, nos pedidos em dinheiro, `juros-e-correcao`.

## Núcleo (plugin `nucleo`)

| Skill | Para quê |
|---|---|
| `estilo-forense` | Guia de redação e formatação de peças processuais: clareza, parágrafos curtos, tópicos numerados, pedidos em alíneas, transcrição mínima, linguagem... |
| `fidelidade-factual` | Camada anti-alucinação de toda peça: impede inventar fatos do caso, datas, valores, documentos, dispositivos, precedentes ou doutrina; separa fato... |
| `juros-e-correcao` | Define o regime de correção monetária e juros de mora de qualquer crédito judicial conforme a natureza da dívida e o período (CC arts. 389 e 406 com... |
| `prazos-processuais` | Calcula e confere prazos processuais no cível (CPC arts. 219 a 232, dias úteis), trabalhista (CLT art. 775), penal (CPP art. 798, dias corridos),... |
| `roteador-de-pecas` | Hub de entrada do repositório: a partir do pedido do usuário, identifica área, fase processual, polo e tipo de peça e indica a skill certa (e as do... |
| `verificacao-de-citacoes` | Protocolo obrigatório para conferir, antes de qualquer uso, súmulas, temas, teses, acórdãos e dispositivos de lei citados em peças: consulta à base... |

## Processo civil (plugin `processo-civil`)

| Skill | Para quê |
|---|---|
| `civel-acao-de-cobranca` | Redige petição inicial de ação de cobrança pelo procedimento comum, depois de escolher a via certa entre execução de título extrajudicial, monitória... |
| `civel-acao-de-exigir-contas` | Redige a ação de exigir contas (CPC, arts. 550 a 553) nas duas fases — a primeira, sobre o dever de prestar, e a segunda, de julgamento das contas e... |
| `civel-acao-declaratoria` | Redige petição inicial de ação declaratória cível (CPC, arts. 19 e 20) para obter certeza sobre a existência, a inexistência ou o modo de ser de uma... |
| `civel-acao-indenizatoria` | Redige petição inicial de ação indenizatória cível fora da relação de consumo, com base no ato ilícito e no abuso de direito (CC, arts. 186, 187 e... |
| `civel-acao-monitoria` | Redige ação monitória (CPC arts. 700 a 702), fundada em prova escrita sem eficácia de título executivo, e também embargos monitórios do réu. |
| `civel-acao-rescisoria` | Redige petição inicial de ação rescisória cível (CPC, arts. 966 a 975) contra decisão de mérito transitada em julgado — ou terminativa que impeça... |
| `civel-acordo-judicial-e-extrajudicial` | Redige minuta de acordo cível (transação dos arts. 840 a 850 do Código Civil), judicial ou extrajudicial, e a petição de homologação: em processo em... |
| `civel-agravo-de-instrumento` | Redige agravo de instrumento cível (CPC arts. 1.015 a 1.020) contra decisão interlocutória do rol do art. 1.015 ou, excepcionalmente, fora dele pela... |
| `civel-agravo-interno` | Redige agravo interno contra decisão monocrática de relator ou outra decisão unipessoal em tribunal (CPC art. 1.021), com impugnação específica dos... |
| `civel-alegacoes-finais` | Redige alegações finais cíveis — debates orais ou razões finais escritas (memoriais) — ao fim da instrução (CPC art. 364), com análise da prova... |
| `civel-apelacao` | Redige apelação cível e contrarrazões (CPC arts. 1.009 a 1.014), com preparo (art. 1.007), preliminares de interlocutórias não agraváveis (art.... |
| `civel-consignacao-em-pagamento` | Redige a consignação em pagamento de obrigação civil comum — depósito bancário extrajudicial com notificação ao credor ou ação consignatória (CPC,... |
| `civel-contestacao` | Redige contestação no procedimento comum cível (CPC arts. 335 a 342), com preliminares do art. 337, impugnação específica dos fatos (art. 341) e... |
| `civel-cumprimento-de-sentenca` | Redige requerimento de cumprimento de sentença cível (CPC arts. 513 a 538): pagar quantia (art. 523, com multa de 10% e honorários de 10% do §1º),... |
| `civel-embargos-a-execucao` | Redige embargos à execução de título extrajudicial (CPC arts. 914 a 920), com as matérias do art. 917, excesso de execução com valor e demonstrativo,... |
| `civel-embargos-de-declaracao` | Redige embargos de declaração cíveis (CPC arts. 1.022 a 1.026) contra omissão, contradição, obscuridade ou erro material, inclusive para... |
| `civel-excecao-de-pre-executividade` | Redige exceção (ou objeção) de pré-executividade em execução ou cumprimento de sentença, restrita a matérias conhecíveis de ofício que dispensam... |
| `civel-execucao-titulo-extrajudicial` | Redige petição inicial de execução de título extrajudicial por quantia certa (CPC arts. 784, 798, 829 e seguintes), com demonstrativo do débito,... |
| `civel-habilitacao-de-credito-recuperacao-falencia` | Redige habilitação de crédito, divergência administrativa, impugnação à relação de credores, habilitação retardatária, pedido de reserva e ação de... |
| `civel-impugnacao-ao-cumprimento` | Redige impugnação ao cumprimento de sentença (CPC art. 525; Fazenda, art. 535) com as matérias do §1º, excesso de execução com valor e demonstrativo... |
| `civel-incidente-de-desconsideracao` | Redige o pedido de instauração do incidente de desconsideração da personalidade jurídica (CPC, arts. 133 a 137) em relação civil ou empresarial... |
| `civel-juizado-especial` | Redige peças do Juizado Especial Cível (Lei 9.099/1995): pedido inicial, contestação com pedido contraposto e recurso inominado (arts. 41 a 43), com... |
| `civel-notificacao-extrajudicial` | Redige notificação extrajudicial cível de uso geral — constituição do devedor em mora quando a obrigação não tem termo (art. 397, parágrafo único, do... |
| `civel-obrigacao-de-fazer-ou-nao-fazer` | Redige petição inicial de ação de obrigação de fazer ou de não fazer com pedido de tutela específica ou de resultado prático equivalente (CPC, arts.... |
| `civel-oposicao` | Redige a petição inicial de oposição (CPC, arts. 682 a 686), ação do terceiro que pretende, no todo ou em parte, a coisa ou o direito disputado entre... |
| `civel-parecer-juridico` | Redige parecer jurídico cível e processual civil (consulta escrita do cliente ou de colega): viabilidade de ação, defesa ou recurso, prescrição e... |
| `civel-peticao-inicial` | Redige petição inicial de procedimento comum cível conforme os arts. 319 e 320 do CPC, com cálculo do valor da causa (art. 292), pedido de tutela... |
| `civel-procuracao-e-substabelecimento` | Redige procuração judicial (ad judicia et extra) e substabelecimento, com ou sem reserva de poderes, e as petições de revogação, renúncia e... |
| `civel-producao-antecipada-de-provas` | Redige a ação de produção antecipada de provas (CPC, arts. 381 a 383) — perícia, inspeção, testemunha, exibição de documentos —, com ou sem urgência... |
| `civel-reconvencao` | Redige reconvenção (pretensão própria do réu contra o autor, CPC art. 343), dentro da contestação ou isolada, com conexão, valor da causa próprio e... |
| `civel-recurso-especial` | Redige recurso especial cível ao STJ (CF art. 105, III; CPC art. 1.029), com tópico obrigatório de relevância da questão federal (CPC art. 1.035-A,... |
| `civel-recurso-extraordinario` | Redige recurso extraordinário cível ao STF (CF art. 102, III; CPC arts. 1.029 e 1.035), com preliminar formal e fundamentada de repercussão geral e... |
| `civel-replica` | Redige réplica (manifestação do autor sobre a contestação) nos termos dos arts. 350, 351 e 437 do CPC, rebatendo preliminares, fatos impeditivos,... |
| `civel-tutela-provisoria` | Redige pedido de tutela provisória cível (CPC arts. 294 a 311): urgência antecipada ou cautelar, em caráter antecedente ou incidental, e tutela da... |

## Trabalhista (plugin `trabalhista`)

| Skill | Para quê |
|---|---|
| `trabalhista-acao-anulatoria-clausula-coletiva` | Redige ação anulatória de cláusula de convenção coletiva ou de acordo coletivo de trabalho, com controle limitado aos elementos essenciais do negócio... |
| `trabalhista-acao-rescisoria` | Redige ação rescisória na Justiça do Trabalho (CLT art. 836, com o regime dos arts. 966 a 975 do CPC), com depósito prévio de 20%, prazo decadencial... |
| `trabalhista-acidente-e-doenca-ocupacional` | Estrutura pedidos (ou defesa) decorrentes de acidente do trabalho e doença ocupacional: estabilidade de 12 meses (Lei 8.213/1991 art. 118; Súmula 378... |
| `trabalhista-acordo-extrajudicial` | Redige a petição conjunta de homologação de acordo extrajudicial na Justiça do Trabalho (CLT arts. 855-B a 855-E), com advogados distintos para cada... |
| `trabalhista-acordo-na-execucao` | Redige a petição conjunta de acordo na fase de liquidação ou execução trabalhista (CLT arts. 764 §3º, 831, 832 §§3º a 6º e 846 §§1º-2º), com... |
| `trabalhista-agravo-de-instrumento` | Redige agravo de instrumento trabalhista contra decisão que denega seguimento a recurso (CLT art. 897 "b"), em especial ao recurso de revista e ao... |
| `trabalhista-agravo-de-peticao` | Redige agravo de petição contra decisões do juiz na execução trabalhista (CLT art. 897 "a"), com a delimitação justificada das matérias e dos valores... |
| `trabalhista-assedio-moral-e-sexual` | Estrutura o pedido (ou a defesa) de indenização por assédio moral e por assédio sexual no trabalho, com base nos arts. 223-A a 223-G da CLT... |
| `trabalhista-auditoria-de-peticao-inicial` | Audita petição inicial trabalhista contra os requisitos do art. 840 §1º da CLT (juízo, qualificação, breve exposição dos fatos, pedido certo,... |
| `trabalhista-compliance` | Estrutura diagnóstico e programa de compliance trabalhista para empresas: mapeamento de riscos (jornada e registro de ponto, igualdade salarial e... |
| `trabalhista-contestacao` | Redige contestação trabalhista apresentada até a audiência (CLT art. 847), com preliminares, prescrição bienal e quinquenal (CF art. 7º XXIX; CLT... |
| `trabalhista-contrato-de-trabalho` | Elabora contrato individual de trabalho regido pela CLT, escolhendo a modalidade (prazo indeterminado, determinado, experiência, intermitente, tempo... |
| `trabalhista-dano-existencial` | Estrutura o pedido (ou a defesa) de indenização por dano existencial decorrente de jornada exaustiva, com base no art. 223-B da CLT (ofensa à esfera... |
| `trabalhista-dissidio-coletivo` | Redige representação de dissídio coletivo de natureza econômica, jurídica ou de greve (CLT arts. 856 a 875; CF art. 114, §§2º e 3º), com o... |
| `trabalhista-embargos-a-execucao` | Redige embargos à execução trabalhista após a garantia do juízo ou a penhora (CLT art. 884), com as matérias do §1º, a impugnação da sentença de... |
| `trabalhista-embargos-de-declaracao` | Redige embargos de declaração no processo do trabalho contra sentença ou acórdão (CLT art. 897-A), em 5 dias, para sanar omissão, contradição,... |
| `trabalhista-embargos-sdi1` | Redige recurso de embargos à Subseção I Especializada em Dissídios Individuais (SDI-1) do TST contra acórdão de Turma (CLT art. 894, II), com... |
| `trabalhista-excecao-pre-executividade` | Redige exceção (objeção) de pré-executividade na execução trabalhista, sem garantia do juízo, restrita a matérias de ordem pública provadas de plano... |
| `trabalhista-impugnacao-de-calculos` | Redige impugnação fundamentada aos cálculos de liquidação trabalhista no prazo comum de 8 dias (CLT art. 879 §2º), com indicação de itens e valores... |
| `trabalhista-insalubridade-periculosidade` | Estrutura pedido ou defesa sobre adicional de insalubridade (CLT arts. 189-192) e de periculosidade (art. 193), com perícia obrigatória (art. 195),... |
| `trabalhista-justa-causa` | Orienta a aplicação da dispensa por justa causa pelo empregador (CLT art. 482: enquadramento na alínea, apuração, imediatidade, proporcionalidade,... |
| `trabalhista-mandado-de-seguranca` | Redige mandado de segurança na Justiça do Trabalho contra ato judicial sem recurso próprio com efeito suspensivo (Lei 12.016/2009, arts. 1º e 5º), em... |
| `trabalhista-notificacao-extrajudicial` | Redige notificação extrajudicial em relação de emprego, de qualquer dos lados: convocação para retorno ao trabalho (abandono, Súmula 32 do TST),... |
| `trabalhista-parecer-juridico` | Redige parecer jurídico trabalhista (consulta de empresa, sindicato ou trabalhador) com ementa, quesitos, fatos, análise da lei, da norma coletiva e... |
| `trabalhista-reclamacao` | Redige petição inicial trabalhista (reclamação) com pedidos certos, determinados e com valor (CLT art. 840 §1º), escolha de rito ordinário ou... |
| `trabalhista-recurso-adesivo` | Redige recurso adesivo no processo do trabalho (CPC art. 997, aplicado por força da CLT art. 769 e da Súmula 283 do TST), cabível em recurso... |
| `trabalhista-recurso-de-revista` | Redige recurso de revista ao TST contra acórdão de TRT em recurso ordinário (CLT art. 896), cumprindo os ônus do §1º-A (trecho do prequestionamento,... |
| `trabalhista-recurso-ordinario` | Redige recurso ordinário trabalhista contra sentença de Vara do Trabalho ou acórdão de TRT em competência originária (CLT art. 895), com preparo... |
| `trabalhista-replica` | Redige a réplica trabalhista (manifestação do reclamante sobre a defesa e os documentos juntados pela reclamada), enfrentando fatos impeditivos,... |
| `trabalhista-rescisao-indireta` | Estrutura o pedido de rescisão indireta do contrato de trabalho por falta grave do empregador (CLT art. 483), com enquadramento na alínea correta,... |
| `trabalhista-revisao-de-contrato-de-trabalho` | Analisa e revisa contrato individual de trabalho já assinado ou minuta recebida, cláusula por cláusula, apontando nulidades (CLT arts. 9º, 444 e... |
| `trabalhista-teletrabalho` | Orienta a contratação, a alteração e o litígio do teletrabalho e do home office pelos arts. 75-A a 75-F e 62, III, da CLT (redação da Lei... |
| `trabalhista-terceirizacao` | Estrutura o pedido (ou a defesa) de responsabilidade do tomador na terceirização e no trabalho temporário pela Lei 6.019/1974 (arts. 4º-A a 5º-D, 10... |
| `trabalhista-trabalho-intermitente` | Orienta a contratação e o litígio do contrato de trabalho intermitente (CLT arts. 443, §3º, e 452-A): contrato escrito com valor-hora não inferior ao... |
| `trabalhista-triagem-de-reclamatoria` | Faz a triagem de reclamação trabalhista recebida pela empresa antes da defesa: conferência da notificação e da audiência (CLT arts. 841, 843 e 844),... |
| `trabalhista-tutela-de-urgencia` | Redige pedido de tutela provisória de urgência na Justiça do Trabalho (CPC arts. 294, 300 e 303 c/c CLT art. 769 e CPC art. 15), antecedente ou... |
| `trabalhista-verbas-rescisorias` | Roteiro de cálculo e conferência das verbas rescisórias por modalidade de extinção (sem justa causa, justa causa, pedido de demissão, acordo do art.... |
| `trabalhista-vinculo-de-emprego` | Estrutura o pedido (ou a defesa) de reconhecimento de vínculo de emprego pelos requisitos do art. 3º da CLT — pessoa física, pessoalidade, não... |

## Previdenciário (plugin `previdenciario`)

| Skill | Para quê |
|---|---|
| `prev-acidentario` | Prepara a ação acidentária contra o INSS na Justiça Estadual (CF, art. 109, I; Lei 8.213/1991, arts. 19 a 22, 86 e 129), com demonstração de nexo... |
| `prev-agravo-de-instrumento-previdenciario` | Redige agravo de instrumento em ação previdenciária contra o INSS (CPC, arts. 1.015 a 1.019), sobretudo contra decisão que nega, concede ou revoga... |
| `prev-apelacao-previdenciaria` | Redige apelação e contrarrazões em ação previdenciária contra o INSS na Justiça Federal ou na competência delegada estadual (CF, art. 109, §§ 3º e... |
| `prev-aposentadoria-especial` | Estrutura a ação de aposentadoria especial ou de reconhecimento e conversão de tempo especial no RGPS (Lei 8.213/1991, arts. 57 e 58; EC 103/2019,... |
| `prev-aposentadoria-por-idade-urbana` | Monta a petição inicial de aposentadoria por idade urbana contra o INSS, pela transição do art. 18 ou pela regra permanente do art. 19 da EC... |
| `prev-auxilio-acidente-previdenciario` | Prepara a ação de auxílio-acidente previdenciário (acidente de qualquer natureza, sem relação com o trabalho) contra o INSS na Justiça Federal (Lei... |
| `prev-averbacao-tempo-de-contribuicao` | Estrutura a ação declaratória de reconhecimento e averbação de tempo de contribuição no RGPS (STJ Súmula 242; Lei 8.213/1991, arts. 55, 94 e 96) para... |
| `prev-beneficio-por-incapacidade` | Prepara ação de concessão ou restabelecimento de auxílio por incapacidade temporária e de aposentadoria por incapacidade permanente (Lei 8.213/1991,... |
| `prev-bpc-loas` | Estrutura o pedido judicial de benefício de prestação continuada à pessoa com deficiência ou idosa de 65 anos ou mais (CF, art. 203, V; Lei... |
| `prev-certidao-de-tempo-de-contribuicao` | Prepara requerimento ao INSS e, se negado, ação para expedição ou retificação de Certidão de Tempo de Contribuição (CTC) para contagem recíproca em... |
| `prev-embargos-de-declaracao-previdenciarios` | Redige embargos de declaração contra sentença ou acórdão em causa previdenciária, no procedimento comum (CPC, arts. 1.022 a 1.026) ou no JEF (Lei... |
| `prev-impugnacao-laudo-pericial` | Redige a manifestação de impugnação ao laudo da perícia médica judicial em ação de benefício por incapacidade, auxílio-acidente ou BPC, com pedido de... |
| `prev-inicial-aposentadoria` | Monta a petição inicial de concessão de aposentadoria do RGPS contra o INSS, enquadrando o segurado na regra permanente ou nas transições da EC... |
| `prev-mandado-de-seguranca-demora-inss` | Redige mandado de segurança contra omissão do INSS na análise de requerimento de benefício, de recurso administrativo ou no cumprimento de decisão do... |
| `prev-pedido-de-uniformizacao-tnu` | Redige pedido de uniformização de interpretação de lei federal no Juizado Especial Federal, dirigido à Turma Regional ou à Turma Nacional de... |
| `prev-pensao-por-morte` | Monta o pedido de pensão por morte no RGPS (Lei 8.213/1991, arts. 16 e 74 a 77; EC 103/2019, art. 23), com dependência, qualidade de segurado do... |
| `prev-planejamento-previdenciario` | Monta parecer de planejamento previdenciário no RGPS: diagnóstico do CNIS, qualidade de segurado e carência (Lei 8.213, arts. 15, 25 e 27-A),... |
| `prev-recurso-crps` | Redige recurso ordinário às Juntas de Recursos e recurso especial às Câmaras de Julgamento do Conselho de Recursos da Previdência Social contra... |
| `prev-requerimento-administrativo` | Prepara o requerimento administrativo de benefício ao INSS pelo Meu INSS, com conferência do CNIS, rol de documentos e cuidado com o interesse de... |
| `prev-revisao-da-vida-toda-acoes-pendentes` | Orienta o advogado sobre a revisão da vida toda depois do STF (Tema 1.102; ADIs 2.110 e 2.111): tese superada, parecer de inviabilidade para cliente... |
| `prev-revisao-de-beneficio` | Avalia e redige ação de revisão de benefício do RGPS, começando pelo controle da decadência de 10 anos e da prescrição quinquenal (Lei 8.213/1991,... |
| `prev-rpps-servidor` | Orienta pedido administrativo ou ação de aposentadoria e abono de permanência de servidor público federal no RPPS da União após a EC 103/2019 (arts.... |
| `prev-salario-maternidade` | Prepara a ação de concessão de salário-maternidade contra o INSS (Lei 8.213/1991, arts. 25, III, 26, VI, 39, p.ú., e 71 a 73), por parto, adoção ou... |
| `prev-tempo-rural-e-segurado-especial` | Estrutura o reconhecimento de tempo rural e da condição de segurado especial para aposentadoria por idade rural, híbrida ou averbação (Lei... |
| `prev-tutela-de-urgencia-previdenciaria` | Redige o pedido de tutela de urgência ou da evidência para implantar ou restabelecer benefício previdenciário ou assistencial contra o INSS (CPC,... |

## Penal (plugin `penal`)

| Skill | Para quê |
|---|---|
| `penal-acesso-aos-autos-do-inquerito` | Redige o pedido de acesso da defesa aos autos de inquérito ou outra investigação criminal e a escalada quando ele é negado: requerimento à... |
| `penal-agravo-em-execucao` | Redige agravo em execução penal e contrarrazões (Lei 7.210/1984, art. 197), processado pelo rito do recurso em sentido estrito, contra decisões do... |
| `penal-alegacoes-finais` | Redige alegações finais da defesa por memoriais (CPP art. 403 §3º e art. 404 p.ú.) e roteiro para debates orais, com preliminares, mérito absolutório... |
| `penal-anpp` | Prepara requerimento de acordo de não persecução penal, pedido de remessa ao órgão superior do Ministério Público após recusa e impugnação de... |
| `penal-apelacao-criminal` | Redige a petição de interposição e as razões de apelação criminal da defesa (CPP arts. 593 a 603), inclusive contra decisões do Tribunal do Júri... |
| `penal-arguicao-de-nulidades` | Redige petição de arguição de nulidade processual penal (CPP arts. 563 a 573), com enquadramento no art. 564, demonstração de prejuízo, momento de... |
| `penal-defesa-em-pic` | Organiza a defesa no procedimento investigatório criminal (PIC) conduzido pelo Ministério Público e redige as peças dessa fase: manifestação e... |
| `penal-defesa-falta-grave` | Redige a defesa técnica do condenado no procedimento disciplinar por falta grave (LEP arts. 50 a 59) e a manifestação na audiência de justificação... |
| `penal-defesa-no-inquerito-policial` | Organiza a atuação da defesa no inquérito policial e redige as peças da fase investigativa: requerimento de diligências ao delegado (CPP art. 14),... |
| `penal-dosimetria` | Analisa e impugna a dosimetria da pena pelo critério trifásico (CP arts. 59 e 68), com regime inicial (art. 33 e STF Tema 972), substituição (art.... |
| `penal-embargos-de-declaracao` | Redige embargos de declaração em matéria criminal contra sentença (CPP art. 382) e contra acórdão (CPP arts. 619 e 620), no prazo de 2 dias corridos,... |
| `penal-embargos-infringentes-e-de-nulidade` | Redige embargos infringentes e de nulidade da defesa contra acórdão criminal não unânime desfavorável ao réu (CPP art. 609, parágrafo único), no... |
| `penal-excecao-de-suspeicao-e-impedimento` | Redige exceção de suspeição e arguição de impedimento ou incompatibilidade do juiz no processo penal (CPP arts. 95 a 112 e 252 a 256), com procuração... |
| `penal-habeas-corpus` | Redige habeas corpus liberatório ou preventivo (CF art. 5º, LXVIII; CPP arts. 647 a 667), com definição da autoridade coatora e do tribunal... |
| `penal-impronuncia-absolvicao-sumaria-desclassificacao` | Redige as alegações da defesa ao fim da primeira fase do júri (judicium accusationis) pedindo impronúncia (CPP art. 414), absolvição sumária (art.... |
| `penal-indulto-e-comutacao` | Redige pedido de indulto (extinção da pena) e de comutação (redução da pena) ao juiz da execução com base no decreto presidencial do ano (CF art. 84,... |
| `penal-liberdade-provisoria-e-relaxamento` | Redige pedidos de relaxamento de prisão ilegal, liberdade provisória com ou sem fiança, revogação ou substituição de preventiva por cautelares e... |
| `penal-livramento-condicional` | Redige pedido de livramento condicional e defesa contra sua revogação (CP arts. 83 a 90; LEP arts. 131 a 146), com cálculo das frações, requisitos... |
| `penal-mandado-de-seguranca-criminal` | Redige mandado de segurança em matéria penal (CF art. 5º, LXIX; Lei 12.016/2009) contra ato de juiz criminal, delegado ou membro do MP que viole... |
| `penal-maria-da-penha-medidas-protetivas` | Redige pedido de medidas protetivas de urgência em favor da ofendida e, do lado do requerido, manifestação, pedido de revogação ou modulação e defesa... |
| `penal-parecer-criminal` | Elabora parecer jurídico criminal consultivo (atividade privativa da advocacia, EOAB art. 1º, II): enquadramento típico de conduta passada ou... |
| `penal-plenario-do-juri` | Prepara a atuação da defesa no plenário do Tribunal do Júri (CPP arts. 422 a 497): rol do art. 422, recusas, roteiro de debates, réplica e tréplica,... |
| `penal-progressao-de-regime` | Redige pedido de progressão de regime (Lei 7.210/1984, art. 112, com a redação das Leis 13.964/2019, 14.843/2024, 15.358/2026 e 15.402/2026), com... |
| `penal-queixa-crime` | Redige queixa-crime em ação penal privada (CPP arts. 30, 41 e 44; CP art. 100) — calúnia, difamação, injúria, dano simples e outros crimes de ação... |
| `penal-recurso-em-sentido-estrito` | Redige recurso em sentido estrito e contrarrazões (CPP arts. 581 a 592), com enquadramento no rol do art. 581, juízo de retratação (art. 589) e... |
| `penal-recurso-especial-criminal` | Redige recurso especial em matéria criminal ao STJ (CF art. 105, III, a e c; CPP art. 638; CPC arts. 1.029 e seguintes), com prequestionamento,... |
| `penal-recurso-extraordinario-criminal` | Redige recurso extraordinário em matéria criminal ao STF (CF art. 102, III e § 3º; CPP art. 638; CPC arts. 1.029 e 1.035), com preliminar formal e... |
| `penal-remicao-de-pena` | Redige pedido de reconhecimento e declaração de remição de pena por trabalho, estudo, leitura e aprovação em ENEM/ENCCEJA perante o juiz da execução... |
| `penal-resposta-a-acusacao` | Redige a resposta à acusação do procedimento comum e do júri (CPP arts. 396, 396-A, 397 e 406) e a defesa prévia da Lei de Drogas (Lei 11.343/2006,... |
| `penal-revisao-criminal` | Redige revisão criminal contra condenação transitada em julgado (CPP arts. 621 a 631), nas hipóteses de contrariedade à lei ou à evidência dos autos,... |
| `penal-revogacao-de-cautelares-diversas` | Redige pedido de revogação, substituição ou flexibilização de medidas cautelares diversas da prisão já impostas a investigado ou réu solto (CPP arts.... |

## Tributário e Fazenda Pública (plugin `tributario-fazenda`)

| Skill | Para quê |
|---|---|
| `fazenda-contestacao-fazendaria` | Redige contestação em nome da Fazenda Pública (União, Estados, DF, Municípios, autarquias e fundações de direito público), com prazo em dobro e... |
| `fazenda-cumprimento-contra-a-fazenda` | Redige requerimento de cumprimento de sentença contra a Fazenda Pública para pagamento de quantia (CPC arts. 534 e 535), com demonstrativo... |
| `fazenda-execucao-fiscal-inicial` | Redige petição inicial de execução fiscal pela Fazenda Pública (LEF arts. 1º, 2º, 6º e 8º), com CDA conforme LEF art. 2º, §5º e CTN art. 202,... |
| `trib-acao-anulatoria` | Redige ação anulatória de débito fiscal (LEF art. 38 e CTN arts. 151 e 204), com pedido de tutela ou depósito integral para suspender a exigibilidade... |
| `trib-acao-regressiva-corresponsaveis` | Redige ação regressiva (de reembolso) de quem pagou crédito tributário como responsável ou devedor solidário contra o contribuinte ou os demais... |
| `trib-acao-rescisoria` | Redige ação rescisória em matéria tributária (CPC arts. 966 a 975), pelo contribuinte ou pela Fazenda, com foco na violação manifesta de norma... |
| `trib-agravo-de-instrumento` | Redige agravo de instrumento em matéria tributária (CPC arts. 1.015 a 1.019; Lei 12.016/2009, art. 7º, §1º) contra decisões em execução fiscal, em... |
| `trib-amicus-curiae` | Redige pedido de ingresso e manifestação como amicus curiae em causa tributária (CPC art. 138; arts. 983, 1.035, §4º, e 1.038, I; Lei 9.868/1999,... |
| `trib-cancelamento-de-cda` | Redige requerimento administrativo de revisão e cancelamento de inscrição em dívida ativa e de sua CDA perante a procuradoria (União, Estado ou... |
| `trib-certidao-negativa-cpen` | Redige requerimento administrativo de certidão negativa de débitos (CND) ou de certidão positiva com efeito de negativa (CPEN) e, se negada ou não... |
| `trib-compensacao-per-dcomp` | Orienta e redige o pedido de restituição e a declaração de compensação de tributos federais (PER/DCOMP) com base no art. 74 da Lei 9.430/1996 e nos... |
| `trib-compliance-tributario` | Estrutura programa de compliance tributário e redige relatório de revisão de rotinas fiscais (obrigações principais e acessórias, guarda de... |
| `trib-consignacao-em-pagamento` | Redige ação de consignação em pagamento de crédito tributário (CTN arts. 156, VIII, e 164; CPC arts. 539 a 549) nas três hipóteses legais: recusa ou... |
| `trib-consulta-tributaria-formal` | Redige consulta formal à Receita Federal sobre interpretação da legislação tributária aplicável a fato determinado, com os requisitos de eficácia do... |
| `trib-declaratoria-inexistencia-relacao-tributaria` | Redige ação declaratória de inexistência de relação jurídico-tributária (CPC arts. 19, I, e 20), preventiva ou cumulada com repetição, com tutela ou... |
| `trib-defesa-administrativa-e-carf` | Redige impugnação administrativa a auto de infração e recurso voluntário ao CARF no processo administrativo fiscal federal (Decreto 70.235/1972, com... |
| `trib-defesa-cautelar-fiscal` | Redige a contestação em medida cautelar fiscal (Lei 8.397/1992, art. 8º: 15 dias), o agravo contra a liminar de indisponibilidade (art. 7º) e o... |
| `trib-defesa-redirecionamento-socio` | Monta a defesa do sócio, administrador ou ex-sócio contra o redirecionamento da execução fiscal (CTN art. 135, III; Súmulas 430 e 435/STJ; Temas 981,... |
| `trib-embargos-a-execucao-fiscal` | Redige embargos à execução fiscal (LEF arts. 16 a 20), com garantia prévia do juízo (art. 16, §1º), prazo de 30 dias e concentração de toda a defesa... |
| `trib-embargos-de-terceiro-execucao-fiscal` | Redige embargos de terceiro contra penhora, arresto ou indisponibilidade em execução fiscal (CPC arts. 674 a 681, aplicados pela LEF art. 1º),... |
| `trib-enquadramento-regime-especial` | Redige requerimento administrativo de enquadramento, habilitação ou concessão de regime especial de tributação ou de benefício de caráter individual... |
| `trib-excecao-pre-executividade-fiscal` | Redige exceção de pré-executividade em execução fiscal, sem garantia do juízo, restrita a matérias conhecíveis de ofício que não exijam dilação... |
| `trib-garantia-antecipada-certidao` | Redige ação de tutela cautelar antecedente de caução (garantia antecipada da futura execução fiscal) com seguro garantia, fiança bancária, depósito... |
| `trib-habilitacao-de-credito-judicial` | Orienta o aproveitamento de indébito tributário reconhecido em decisão judicial transitada em julgado: escolha entre precatório/RPV e compensação... |
| `trib-mandado-de-seguranca` | Redige mandado de segurança tributário, repressivo ou preventivo, com base na Lei 12.016/2009 (prazo decadencial de 120 dias do art. 23), inclusive... |
| `trib-memorial-e-sustentacao-oral-carf` | Prepara memorial escrito e roteiro de sustentação oral para julgamento no CARF e na Câmara Superior de Recursos Fiscais, em reunião síncrona... |
| `trib-parcelamento-e-regularizacao` | Orienta o pedido de parcelamento de débito tributário e a adesão a programa de regularização fiscal, com base no CTN (arts. 151, VI, 155-A e 174) e,... |
| `trib-parecer-tributario` | Redige parecer tributário consultivo geral (incidência, interpretação de norma, alcance de benefício, efeito de decisão judicial ou administrativa,... |
| `trib-planejamento-tributario` | Elabora parecer de planejamento tributário sobre estruturação de operações, reorganizações e escolhas de modelo de negócio, com teste de licitude... |
| `trib-prescricao-intercorrente` | Analisa e redige petição de reconhecimento de prescrição intercorrente, prescrição originária e decadência tributária em execução fiscal (LEF art.... |
| `trib-recurso-administrativo-estadual` | Redige recurso no processo administrativo tributário estadual (ICMS, IPVA, ITCMD e taxas), contra decisão de primeira instância que manteve auto de... |
| `trib-recurso-especial-csrf` | Redige recurso especial de divergência do contribuinte à Câmara Superior de Recursos Fiscais (CSRF) contra acórdão de turma do CARF, com cotejo... |
| `trib-recurso-especial-tributario` | Complementa a skill civel-recurso-especial com o recorte tributário do recurso especial ao STJ (CF art. 105, III): separar a questão de lei federal... |
| `trib-reforma-tributaria-ibs-cbs` | Elabora parecer consultivo sobre a reforma tributária do consumo (EC 132/2023, LC 214/2025 e alterações da LC 227/2026): IBS, CBS, Imposto Seletivo,... |
| `trib-repeticao-de-indebito` | Redige ação de repetição de indébito tributário (CTN arts. 165 a 169), com prazo de 5 anos (art. 168 e LC 118/2005, Tema 4 STF), prova do encargo nos... |
| `trib-revisao-de-lancamento-de-oficio` | Orienta e redige pedido de revisão de lançamento tributário fora do rito da impugnação (CTN arts. 145 e 149) e a defesa contra revisão feita pelo... |
| `trib-transacao-tributaria` | Orienta e redige pedido de transação tributária federal (Lei 13.988/2020 e CTN art. 171) — por adesão a edital, proposta individual do devedor ou... |

## Família e sucessões (plugin `familia-sucessoes`)

| Skill | Para quê |
|---|---|
| `familia-acao-de-alimentos` | Redige petição inicial de ação de alimentos (Lei 5.478/1968; CC arts. 1.694 a 1.710), inclusive alimentos gravídicos (Lei 11.804/2008) e alimentos... |
| `familia-acordo-extrajudicial-homologacao` | Redige o termo de acordo extrajudicial de família (alimentos, guarda, convivência, partilha) e a petição conjunta de homologação em jurisdição... |
| `familia-adocao` | Redige pedido de adoção de criança ou adolescente (ECA arts. 39 a 52-D e 165 a 170) — unilateral, conjunta, por parente, de quem já tem a guarda... |
| `familia-alvara-judicial` | Redige pedido de alvará judicial em jurisdição voluntária (CPC arts. 719 a 725) — levantamento de valores deixados pelo falecido sem inventário (Lei... |
| `familia-busca-e-apreensao-de-menor` | Redige pedido de busca e apreensão de criança ou adolescente — incidental ao cumprimento de decisão de guarda ou convivência (CPC art. 536, §§ 1º e... |
| `familia-destituicao-do-poder-familiar` | Redige ação de perda (destituição) ou suspensão do poder familiar pelo rito do ECA (arts. 155 a 163), com fundamento nos arts. 1.637 e 1.638 do CC e... |
| `familia-divorcio` | Redige divórcio litigioso ou consensual (judicial ou por escritura), com partilha, guarda, convivência, alimentos e nome, a partir da EC 66/2010 (CF... |
| `familia-emancipacao` | Orienta e redige a emancipação de menor com 16 anos completos — voluntária, por escritura pública dos pais, ou judicial, por sentença em jurisdição... |
| `familia-execucao-de-alimentos` | Redige o requerimento de cumprimento de sentença ou execução de alimentos pelo rito da prisão ou da expropriação (CPC arts. 528 a 533 e 911 a 913),... |
| `familia-filiacao-socioafetiva` | Redige ação declaratória de paternidade ou maternidade socioafetiva (em vida ou post mortem), com ou sem multiparentalidade e petição de herança, e... |
| `familia-guarda-e-convivencia` | Redige ação de guarda e de regulamentação de convivência (visitas), modificação de guarda e incidente de alienação parental (CC arts. 1.583 a 1.590;... |
| `familia-interdicao-e-curatela` | Redige ação de curatela (interdição) de maior, com curador provisório, e os pedidos conexos — levantamento total ou parcial, remoção de curador,... |
| `familia-investigacao-de-paternidade` | Redige ação de investigação de paternidade (ou maternidade), cumulada ou não com alimentos e petição de herança, com pedido de exame de DNA (Lei... |
| `familia-negatoria-de-paternidade` | Redige ação negatória de paternidade cumulada com anulação (retificação) do registro de nascimento, proposta pelo pai registral, com base nos arts.... |
| `familia-pacto-antenupcial` | Elabora minuta de pacto antenupcial para escritura pública — escolha do regime (separação convencional, comunhão universal, participação final nos... |
| `familia-parecer` | Redige parecer jurídico de direito de família (consulta escrita): regime de bens e o que se partilha, efeitos do pacto, alimentos (cabimento, valor,... |
| `familia-partilha-posterior-e-sobrepartilha` | Redige ação de partilha de bens posterior ao divórcio ou à dissolução de união estável e ação de sobrepartilha de bem omitido, sonegado ou descoberto... |
| `familia-revisional-e-exoneracao-de-alimentos` | Redige ação revisional (majoração ou redução) e ação de exoneração de alimentos, com base na mudança da situação financeira das partes (CC art.... |
| `familia-tutela-de-menor` | Redige pedido de nomeação de tutor para criança ou adolescente (órfão, filho de pais ausentes ou destituídos), controle judicial de tutor... |
| `familia-uniao-estavel` | Redige ação de reconhecimento e dissolução de união estável (inclusive post mortem), com partilha, alimentos e efeitos sucessórios (CC arts. 1.723 a... |
| `sucessoes-inventario-extrajudicial` | Prepara inventário e partilha por escritura pública (CPC art. 610 §§1º e 2º; Res. CNJ 35/2007 com as alterações das Res. 571/2024 e 695/2026),... |
| `sucessoes-inventario-judicial` | Redige a abertura de inventário judicial e suas peças (primeiras declarações, arrolamento sumário e comum, colação, habilitação de crédito, plano de... |
| `sucessoes-planejamento-e-partilha-em-vida` | Elabora parecer consultivo de planejamento sucessório e minutas de doação com reserva de usufruto, partilha em vida e estrutura societária (holding... |
| `sucessoes-testamento` | Elabora minuta de testamento (público, cerrado ou particular) e codicilo respeitando a legítima, e redige os pedidos de abertura, registro e... |

## Consumidor (plugin `consumidor`)

| Skill | Para quê |
|---|---|
| `consumidor-acao-coletiva` | Redige ação coletiva de consumo (ação civil pública consumerista) para tutela de direitos difusos, coletivos e individuais homogêneos, com base nos... |
| `consumidor-acao-indenizatoria` | Redige petição inicial de ação indenizatória em relação de consumo (fato do produto ou do serviço), com responsabilidade objetiva dos arts. 12 a 14... |
| `consumidor-acordo-judicial` | Redige minuta de acordo (transação) em ação de consumo e a petição de homologação, no Juizado Especial ou na Justiça comum, com base nos arts. 840 a... |
| `consumidor-clausulas-abusivas` | Redige ação declaratória de nulidade (ou de revisão) de cláusula contratual abusiva em contrato de consumo, com base nos arts. 6º, IV e V, 46, 47, 51... |
| `consumidor-contratos-bancarios-revisional` | Redige ação revisional de contrato bancário de consumo (empréstimo, financiamento, cartão, cheque especial), com aplicação do CDC às instituições... |
| `consumidor-defesa-do-fornecedor` | Redige contestação do fornecedor (empresa, banco, operadora, companhia aérea, varejista) em ação de consumo, com as excludentes dos arts. 12, § 3º, e... |
| `consumidor-defesa-procon` | Redige a defesa (impugnação) e o recurso do fornecedor em processo administrativo sancionador do Procon ou de outro órgão do SNDC, com base no... |
| `consumidor-desconsideracao-personalidade-juridica` | Redige o pedido (incidente ou requerimento na inicial) de desconsideração da personalidade jurídica do fornecedor em relação de consumo, pela teoria... |
| `consumidor-direito-de-arrependimento` | Redige a notificação de arrependimento e a ação de restituição quando o fornecedor recusa a desistência em compra feita fora do estabelecimento... |
| `consumidor-negativacao-indevida` | Redige ação declaratória de inexistência de débito cumulada com cancelamento de inscrição em cadastro de inadimplentes e indenização por dano moral,... |
| `consumidor-notificacao-extrajudicial` | Redige notificação extrajudicial do consumidor ao fornecedor (reclamação formal, pedido de cancelamento, contestação de cobrança, exigência de... |
| `consumidor-parecer` | Redige parecer jurídico de direito do consumidor (consulta escrita), para consumidor, fornecedor ou associação: incidência do CDC (arts. 2º, 3º, 17 e... |
| `consumidor-plano-de-saude` | Redige ação de obrigação de fazer com tutela de urgência contra operadora de plano de saúde por negativa de cobertura, com base na Lei 9.656/1998... |
| `consumidor-publicidade-enganosa` | Redige ação contra publicidade enganosa ou abusiva (CDC arts. 36 a 38), com vinculação da oferta e cumprimento forçado (arts. 30 e 35), inversão... |
| `consumidor-recall` | Redige notificação e ação de obrigação de fazer (com indenização, se houver dano) ligadas a recall: produto que o fornecedor sabe ou deveria saber... |
| `consumidor-recurso-consumerista` | Monta as teses de mérito consumeristas de recurso inominado (Lei 9.099/1995, arts. 41 a 46) ou de apelação (CPC, arts. 1.009 a 1.013) em ação de... |
| `consumidor-repeticao-em-dobro` | Estrutura o pedido de repetição do indébito em dobro do art. 42, parágrafo único, do CDC (como ação autônoma ou capítulo de outra peça), com a tese... |
| `consumidor-superendividamento` | Redige o pedido de repactuação de dívidas do consumidor superendividado (CDC arts. 54-A e 104-A a 104-C, incluídos pela Lei 14.181/2021), com plano... |
| `consumidor-transporte-aereo` | Redige ação indenizatória contra companhia aérea por atraso, cancelamento, overbooking ou extravio/avaria de bagagem, definindo o regime aplicável:... |
| `consumidor-vicio-do-produto-ou-servico` | Redige inicial (e a reclamação prévia) por vício de qualidade ou quantidade de produto ou serviço, com as alternativas dos arts. 18 a 20 do CDC e... |

## Administrativo e licitações (plugin `administrativo-licitacoes`)

| Skill | Para quê |
|---|---|
| `adm-acao-anulatoria-de-ato-administrativo` | Redige petição inicial de ação anulatória de ato administrativo pelo procedimento comum (CPC arts. 319 e 300), com controle de legalidade, motivação... |
| `adm-acao-de-improbidade` | Redige petição inicial de ação de improbidade administrativa pelo autor — Ministério Público ou pessoa jurídica lesada (legitimidade concorrente... |
| `adm-acao-popular` | Redige petição inicial de ação popular para anular ato lesivo ao patrimônio público, à moralidade administrativa, ao meio ambiente ou ao patrimônio... |
| `adm-acesso-a-informacao-lai` | Redige pedido de acesso à informação, recurso contra negativa, reclamação por omissão e recursos às instâncias seguintes com base na Lei de Acesso à... |
| `adm-anulacao-de-ato-por-autotutela` | Redige requerimento administrativo de anulação (ou revisão) de ato ilegal pela própria Administração, com base no dever de autotutela (Súmulas 346 e... |
| `adm-concurso-publico` | Redige mandado de segurança ou ação de procedimento comum em concurso público: direito à nomeação (Temas 161 e 784 do STF), preterição, eliminação... |
| `adm-defesa-em-improbidade` | Redige contestação, manifestação e peças de defesa em ação de improbidade administrativa (Lei 8.429/1992 com a redação da Lei 14.230/2021): dolo... |
| `adm-defesa-em-pad` | Redige defesa escrita, requerimentos, recurso e pedido de revisão em sindicância ou processo administrativo disciplinar de servidor público federal... |
| `adm-defesa-em-processo-sancionador-licitacao` | Redige defesa prévia, alegações finais, recurso ou pedido de reconsideração de licitante ou contratado em processo de responsabilização da Lei... |
| `adm-desapropriacao-defesa` | Redige contestação do expropriado e manifestações em ação de desapropriação por utilidade pública (Decreto-Lei 3.365/1941): impugnação do preço,... |
| `adm-impugnacao-ao-edital` | Redige impugnação a edital de licitação ou pedido de esclarecimento com base na Lei 14.133/2021, art. 164 (prazo de até 3 dias úteis antes da... |
| `adm-mandado-de-seguranca` | Redige petição inicial de mandado de segurança individual ou coletivo contra ato de autoridade pública (CF art. 5º, LXIX e LXX; Lei 12.016/2009), com... |
| `adm-pedido-de-reequilibrio-economico-financeiro` | Redige pedido administrativo (ou fundamenta ação) de restabelecimento do equilíbrio econômico-financeiro, revisão, reajuste ou repactuação de... |
| `adm-recurso-contra-auto-de-infracao` | Redige defesa e recurso administrativo contra auto de infração e multa aplicados no exercício do poder de polícia (vigilância sanitária, fiscalização... |
| `adm-recurso-em-licitacao` | Redige recurso administrativo, contrarrazões ou pedido de reconsideração em licitação regida pela Lei 14.133/2021 (arts. 165 a 168): julgamento de... |
| `adm-responsabilidade-civil-do-estado` | Redige petição inicial (ou contestação) de ação indenizatória contra o Estado ou prestadora de serviço público com base na responsabilidade objetiva... |

## Contratos (plugin `contratos`)

| Skill | Para quê |
|---|---|
| `contratos-aditivo-contratual` | Redige termo aditivo a contrato civil ou empresarial (alteração de prazo, preço, reajuste, escopo, garantias ou partes) preservando o contrato... |
| `contratos-agencia-e-distribuicao` | Redige e revisa contrato de agência e de distribuição regido pelos arts. 710 a 721 do Código Civil, com zona, exclusividade recíproca, remuneração... |
| `contratos-analise-e-revisao-de-contrato` | Revisa e audita contrato recebido da outra parte: lê cláusula a cláusula, monta mapa de riscos (alto, médio, baixo), aponta cláusulas leoninas ou... |
| `contratos-cessao-de-direitos` | Redige instrumento de cessão de crédito, de posição contratual e de direitos (inclusive direitos patrimoniais de autor), com base nos arts. 286 a 298... |
| `contratos-clausula-penal` | Redige e revisa cláusula penal compensatória e moratória em contratos civis e empresariais, com base nos arts. 408 a 416 do Código Civil, no dever de... |
| `contratos-comodato` | Redige contrato de comodato (empréstimo gratuito de coisa infungível) de imóvel, veículo, equipamento ou maquinário, e a notificação de retomada, com... |
| `contratos-compra-e-venda-empresarial` | Redige contrato de compra e venda mercantil entre empresas (fornecimento, venda de mercadorias, equipamentos ou safra), com base nos arts. 481 a 532... |
| `contratos-distrato-e-rescisao` | Escolhe a via correta de extinção do contrato (distrato, resilição unilateral por denúncia, resolução por inadimplemento, cláusula resolutiva... |
| `contratos-elaboracao-de-contrato` | Roteiro geral para redigir contrato civil ou empresarial sob medida, do levantamento do negócio à minuta pronta para assinatura: partes, objeto,... |
| `contratos-franquia-e-cof` | Redige e revisa contrato de franquia empresarial e a Circular de Oferta de Franquia (COF) conforme a Lei 13.966/2019, com prazo de entrega de 10... |
| `contratos-licenca-de-software-e-saas` | Redige e revisa contrato de licença de uso de software (on-premise) e contrato de software como serviço (SaaS), com base na Lei 9.609/1998, no Código... |
| `contratos-locacao-comercial` | Redige e revisa contrato de locação não residencial (comercial) com base na Lei 8.245/1991, arts. 51 a 57, tratando a ação renovatória como cláusula... |
| `contratos-memorando-de-entendimentos` | Redige memorando de entendimentos (MOU), carta de intenções ou term sheet, separando com precisão o que vincula (sigilo, exclusividade, custos, foro)... |
| `contratos-nda-confidencialidade` | Redige e revisa acordo de confidencialidade (NDA), unilateral ou mútuo, para negociações, due diligence, parcerias, prestação de serviços e projetos... |
| `contratos-notificacao-de-descumprimento` | Redige notificação extrajudicial de descumprimento contratual para constituir o devedor em mora, conceder prazo de purgação e preparar a resolução, a... |
| `contratos-parceria-e-joint-venture` | Estrutura e redige contrato de parceria empresarial, consórcio entre sociedades (Lei 6.404/1976, arts. 278 e 279), sociedade em conta de participação... |
| `contratos-parecer-sobre-contrato` | Redige parecer jurídico sobre contrato já celebrado: validade (nulidade, anulabilidade), interpretação de cláusula controvertida, execução,... |
| `contratos-prestacao-de-servicos` | Redige contrato de prestação de serviços civil ou empresarial, regido pelos arts. 593 a 609 do Código Civil e pela teoria geral dos contratos:... |
| `contratos-prestacao-de-servicos-pj` | Redige contrato de prestação de serviços por pessoa jurídica com foco em mitigar o risco de reconhecimento de vínculo empregatício (CLT, arts. 2º,... |
| `contratos-representacao-comercial` | Redige e revisa contrato de representação comercial autônoma regido pela Lei 4.886/1965, com os elementos obrigatórios do art. 27, a indenização... |
| `contratos-sla-nivel-de-servico` | Redige acordo de nível de serviço (SLA) como anexo de contrato de prestação de serviços — métricas objetivas, janela de medição, exclusões, créditos... |
| `contratos-termo-de-responsabilidade` | Redige termo de responsabilidade — uso de equipamento (empregado, prestador, comodato), guarda de bens (depósito), participação em evento ou... |

## Imobiliário (plugin `imobiliario`)

| Skill | Para quê |
|---|---|
| `imob-acao-de-despejo` | Redige ação de despejo da Lei 8.245/1991 — por falta de pagamento (com ou sem cobrança cumulada), por denúncia vazia, por denúncia cheia e por... |
| `imob-acao-renovatoria` | Redige ação renovatória de locação não residencial (Lei 8.245/1991, arts. 51 a 57 e 71 a 75): requisitos do art. 51, janela decadencial do § 5º,... |
| `imob-acao-revisional-de-aluguel` | Redige ação revisional de aluguel da Lei 8.245/1991 (arts. 19 e 68 a 70), proposta pelo locador para elevar ou pelo locatário para reduzir o aluguel... |
| `imob-adjudicacao-compulsoria` | Redige ação de adjudicação compulsória (CC arts. 1.417 e 1.418) ou monta o pedido extrajudicial no Registro de Imóveis (Lei 6.015/1973, art. 216-B)... |
| `imob-analise-de-matricula-e-due-diligence` | Analisa a matrícula do imóvel ato por ato e conduz a due diligence imobiliária (vendedor, imóvel e riscos de fraude), com base na Lei 6.015/1973... |
| `imob-cobranca-de-taxas-condominiais` | Redige execução de título extrajudicial de cotas condominiais (CPC, art. 784, X) ou ação de cobrança pelo procedimento comum, com parcelas vincendas,... |
| `imob-compra-e-venda-de-imovel` | Redige e revisa promessa (compromisso) de compra e venda e contrato de compra e venda de imóvel, com due diligence de certidões, forma exigida... |
| `imob-distrato-imobiliario` | Redige ação de resolução de promessa de compra e venda de imóvel na planta (ou instrumento de distrato) com restituição das parcelas pagas, aplicando... |
| `imob-embargos-de-terceiro` | Redige embargos de terceiro contra penhora, arresto, indisponibilidade ou outra constrição judicial sobre imóvel de quem não é parte no processo (CPC... |
| `imob-imissao-na-posse` | Redige ação de imissão na posse do adquirente (proprietário que nunca teve a posse) contra o alienante ou terceiro que ocupa o imóvel, ação petitória... |
| `imob-incorporacao-imobiliaria` | Elabora parecer e checklist de registro e compliance de incorporação imobiliária: memorial de incorporação e documentos do art. 32 da Lei 4.591/1964,... |
| `imob-locacao-residencial` | Elabora ou revisa contrato de locação residencial urbana (Lei 8.245/1991): prazo e efeitos dos 30 meses, aluguel e reajuste, encargos ordinários e... |
| `imob-loteamento-irregular-defesa-do-adquirente` | Redige a defesa do adquirente de lote em loteamento irregular ou clandestino: notificação ao loteador e depósito das prestações (art. 38 da Lei... |
| `imob-notificacao-extrajudicial-imobiliaria` | Redige notificações extrajudiciais imobiliárias: denúncia de locação residencial ou não residencial (Lei 8.245/1991), denúncia pelo adquirente do... |
| `imob-parecer-juridico-imobiliario` | Redige parecer jurídico sobre negócio ou situação imobiliária (aquisição, promessa, garantia fiduciária, regularidade registral, desfazimento de... |
| `imob-prestacao-de-contas-de-condominio` | Redige ação de exigir contas do condomínio contra síndico, ex-síndico ou administradora (CC, art. 1.348, VIII; CPC, arts. 550 a 553), nas duas fases... |
| `imob-regularizacao-fundiaria-reurb` | Estrutura requerimento de instauração de Regularização Fundiária Urbana (Reurb-S ou Reurb-E) ao Município, acompanhamento do procedimento até a... |
| `imob-reintegracao-de-posse` | Redige ações possessórias de imóvel — reintegração de posse (esbulho), manutenção de posse (turbação) e interdito proibitório (ameaça) — pelos arts.... |
| `imob-retificacao-de-area` | Prepara requerimento de retificação de registro imobiliário e de área, pela via administrativa no Registro de Imóveis (art. 213 da Lei 6.015/1973) ou... |
| `imob-revisao-de-financiamento-sfh` | Redige ação revisional de contrato de financiamento habitacional (SFH ou SFI), com ou sem alienação fiduciária (Lei 9.514/1997), e orienta o uso do... |
| `imob-usucapiao-extrajudicial` | Prepara o requerimento de reconhecimento extrajudicial de usucapião no Registro de Imóveis (Lei 6.015/1973, art. 216-A), com ata notarial, planta e... |
| `imob-usucapiao-judicial` | Redige ação de usucapião de imóvel — extraordinária, ordinária, especial urbana e rural (CF arts. 183 e 191), familiar por abandono do lar (CC art.... |

## Digital e LGPD (plugin `digital`)

| Skill | Para quê |
|---|---|
| `digital-contrato-de-influenciador` | Elabora e revisa contrato de influenciador digital (publicidade em redes sociais, publi, embaixador de marca, UGC, permuta), com cláusulas de... |
| `digital-contrato-dpa-operador` | Elabora ou revisa acordo de tratamento de dados pessoais (DPA) entre controlador e operador — instruções, segurança, suboperadores, incidentes, apoio... |
| `digital-crime-cibernetico` | Redige notitia criminis, representação da vítima e requerimentos de preservação e fornecimento de registros em crimes cibernéticos: invasão de... |
| `digital-deepfake-e-uso-de-imagem` | Redige ação de obrigação de fazer e indenização por uso não autorizado de imagem ou voz, montagem e deepfake (conteúdo sintético gerado ou alterado... |
| `digital-defesa-em-processo-sancionador-anpd` | Redige defesa, alegações finais e recurso em processo administrativo sancionador da ANPD por infração à LGPD, inclusive impugnação do auto de... |
| `digital-direitos-autorais-online` | Redige notificação extrajudicial e ação inibitória e indenizatória por violação de direitos autorais na internet (texto, foto, vídeo, música, curso,... |
| `digital-indenizacao-por-vazamento-de-dados` | Redige ação do titular contra controlador e/ou operador por vazamento ou exposição indevida de dados pessoais — obrigação de fazer (informação,... |
| `digital-notificacao-de-incidente-lgpd` | Conduz a resposta jurídica a incidente de segurança com dados pessoais: avaliação de risco ou dano relevante, comunicação à ANPD, comunicação aos... |
| `digital-ofensas-em-redes-sociais` | Redige ação indenizatória por dano moral (com obrigação de fazer) contra quem publicou calúnia, difamação ou injúria em rede social, e o pedido... |
| `digital-perfil-falso-e-impersonation` | Redige ação de obrigação de fazer com tutela de urgência para suspender perfil falso ou conta que usa indevidamente o nome, a foto ou a identidade do... |
| `digital-politica-de-privacidade-e-termos-de-uso` | Elabora ou revisa política de privacidade e termos de uso de site, aplicativo ou plataforma, com base nos arts. 6º, 7º, 9º, 11, 14 e 18 da LGPD, no... |
| `digital-remocao-de-conteudo` | Redige notificação extrajudicial ao provedor e ação de obrigação de fazer para remoção de conteúdo ilícito ou ofensivo da internet, com base nos... |
| `digital-remocao-indevida-de-conteudo` | Redige ação de obrigação de fazer com tutela de urgência, cumulada com indenização, contra plataforma digital que removeu conteúdo, suspendeu,... |
| `digital-resposta-a-titular-de-dados` | Redige a resposta do controlador a requisição de titular de dados pessoais (confirmação, acesso, correção, eliminação, portabilidade, informação... |
| `digital-restauracao-de-conta` | Redige ação de obrigação de fazer contra a plataforma (rede social, e-mail, mensageiro, loja de aplicativos) para restabelecer conta bloqueada,... |

## Bancário (plugin `bancario`)

| Skill | Para quê |
|---|---|
| `banc-busca-e-apreensao-contestacao` | Redige a contestação (resposta) do devedor fiduciante na ação de busca e apreensão de veículo ou outro bem móvel alienado fiduciariamente... |
| `banc-consignacao-e-purgacao-da-mora` | Redige a consignação em pagamento (extrajudicial em banco ou ação consignatória) de parcelas de contrato bancário — financiamento de veículo, cédula... |
| `banc-conta-aberta-indevidamente` | Redige ação declaratória de inexistência de relação jurídica cumulada com encerramento de conta, cancelamento de produtos vinculados e indenização,... |
| `banc-defesa-execucao-alienacao-fiduciaria` | Organiza a defesa do devedor em execução de crédito garantido por alienação fiduciária de bem móvel: conversão da busca e apreensão em execução (DL... |
| `banc-fraude-pix-e-transferencia-nao-autorizada` | Redige ação declaratória de inexigibilidade cumulada com restituição e indenização contra instituição financeira por Pix, TED, empréstimo ou... |
| `banc-inscricao-indevida-no-scr` | Redige ação de exclusão ou correção de registro no Sistema de Informações de Crédito do Banco Central (SCR/Sisbacen, "prejuízo", "vencido", "risco")... |
| `banc-med-pix-devolucao` | Prepara o requerimento ao banco para acionar o Mecanismo Especial de Devolução (MED) do Pix e o bloqueio de valores na conta de destino, com base no... |
| `banc-reclamacao-bacen-e-ouvidoria` | Redige a reclamação formal à ouvidoria da instituição financeira (Res. CMN 4.860/2020: protocolo e resposta em até 10 dias úteis) e a reclamação ao... |
| `banc-renegociacao-extrajudicial-de-divida` | Prepara a proposta de renegociação extrajudicial de dívida bancária e revisa ou redige o termo de acordo (transação, novação ou confissão de dívida... |
| `banc-repeticao-de-indebito-bancario` | Redige ação de repetição de indébito contra banco por lançamentos debitados na conta sem causa válida (tarifas e cestas sem pactuação expressa,... |

## Saúde (plugin `saude`)

| Skill | Para quê |
|---|---|
| `saude-defesa-do-medico` | Redige contestação do médico (e, se for o caso, da clínica) em ação indenizatória por erro médico: ilegitimidade em atendimento público (Tema... |
| `saude-defesa-etica-medica-crm` | Redige a defesa do médico em sindicância e processo ético-profissional (PEP) no Conselho Regional de Medicina — manifestação preliminar, defesa... |
| `saude-indenizacao-erro-medico` | Redige petição inicial de ação indenizatória por erro médico contra o médico (e, quando couber, a clínica ou o hospital), com a distinção entre... |
| `saude-medicamento-sem-registro-anvisa` | Redige ação contra a União (Justiça Federal) para fornecimento de medicamento sem registro na Anvisa nas hipóteses excepcionais do Tema 500/STF (mora... |
| `saude-medicamento-tratamento-sus` | Redige ação de obrigação de fazer com tutela de urgência (ou mandado de segurança) contra o poder público para fornecimento de medicamento,... |
| `saude-notificacao-extrajudicial-plano-de-saude` | Redige notificação extrajudicial do beneficiário à operadora de plano de saúde para exigir autorização de procedimento, resposta escrita e... |
| `saude-reembolso-plano-de-saude` | Redige ação de cobrança de reembolso de despesas médico-hospitalares contra operadora de plano de saúde, com base no art. 12, VI, da Lei 9.656/1998,... |
| `saude-rescisao-unilateral-plano-de-saude` | Redige ação de restabelecimento de plano de saúde cancelado unilateralmente pela operadora, com tutela de urgência, com base no art. 13, parágrafo... |
| `saude-responsabilidade-civil-hospitalar` | Redige petição inicial de ação indenizatória contra hospital, clínica ou estabelecimento de saúde privado por falha do serviço hospitalar (infecção... |

## Societário (plugin `societario`)

| Skill | Para quê |
|---|---|
| `soc-acordo-de-socios` | Elabora acordo de acionistas (Lei 6.404/1976, art. 118) e acordo de quotistas em sociedade limitada, com cláusulas de voto e bloco de controle,... |
| `soc-ata-de-reuniao-de-socios` | Redige edital de convocação, ata de reunião ou assembleia de sócios de sociedade limitada e deliberação escrita unânime, conferindo matéria, forma,... |
| `soc-contrato-social-ltda` | Elabora contrato social de sociedade limitada (pluripessoal ou unipessoal) e suas alterações, com as cláusulas obrigatórias do art. 997 e o regime... |
| `soc-dissolucao-parcial-e-exclusao-de-socio` | Redige ação de dissolução parcial de sociedade com apuração de haveres (retirada, recesso, morte ou exclusão de sócio), a exclusão extrajudicial por... |
| `soc-due-diligence-societaria` | Conduz e redige relatório de due diligence jurídica (auditoria legal) de sociedade-alvo em aquisição, investimento ou reorganização: lista de... |
| `soc-holding-familiar` | Estrutura e redige os atos de constituição de holding familiar ou patrimonial (contrato social de LTDA, integralização de bens, doação de quotas com... |
| `soc-ma-compra-de-quotas-e-acoes` | Redige ou revisa contrato de compra e venda de quotas ou ações (SPA/QPA) e estrutura operações de M&A — aquisição de controle, incorporação, fusão e... |
| `soc-parecer-societario` | Redige parecer jurídico societário (opinião legal) sobre questão concreta de sociedade limitada ou anônima fechada: validade de deliberação e quórum,... |

## Ambiental (plugin `ambiental`)

| Skill | Para quê |
|---|---|
| `amb-acao-civil-publica` | Redige ação civil pública ambiental para reparação de dano coletivo ao meio ambiente (Lei 7.347/1985; Lei 6.938/1981, art. 14, § 1º; CF, art. 225, §... |
| `amb-auditoria-compliance` | Conduz auditoria jurídica ambiental (due diligence) e estrutura programa de compliance ambiental, com parecer de riscos nas três esferas (civil... |
| `amb-defesa-acao-civil-publica` | Redige contestação do réu em ação civil pública ambiental (Lei 7.347/1985), enfrentando legitimidade, nexo causal, existência e extensão do dano,... |
| `amb-defesa-auto-de-infracao` | Redige a defesa administrativa contra auto de infração ambiental lavrado pelo IBAMA, ICMBio ou por órgão estadual ou municipal do SISNAMA, com base... |
| `amb-defesa-crime-ambiental` | Organiza a defesa em crime ambiental da Lei 9.605/1998 (pessoa física, dirigente ou pessoa jurídica): tipicidade dos delitos mais frequentes (arts.... |
| `amb-indenizacao-dano-ambiental-individual` | Redige ação indenizatória de vítima individual de dano ambiental (dano reflexo ou por ricochete) e ação de vizinhança contra interferência poluidora,... |
| `amb-licenca-de-operacao-corretiva` | Redige o requerimento de licenciamento corretivo — Licença de Operação Corretiva (LOC) — para regularizar atividade ou empreendimento que já opera... |
| `amb-mandado-de-seguranca-licenciamento` | Redige petição inicial de mandado de segurança contra ato ou omissão no licenciamento ambiental — indeferimento sem motivação, condicionante ilegal,... |
| `amb-recurso-auto-de-infracao` | Redige o recurso administrativo contra a decisão de primeira instância que homologou auto de infração ambiental do IBAMA, do ICMBio ou de órgão... |
| `amb-recurso-no-licenciamento` | Redige impugnação e recurso administrativo no licenciamento ambiental: pedido de revisão de condicionantes, recurso contra alteração de... |
| `amb-reserva-legal-e-car` | Orienta e redige requerimentos de regularização de reserva legal e do Cadastro Ambiental Rural (CAR) pela Lei 12.651/2012: inscrição e retificação do... |
| `amb-termo-ajustamento-conduta` | Elabora, revisa e negocia termo de ajustamento de conduta (TAC) ambiental com o Ministério Público ou órgão público legitimado (Lei 7.347/1985, art.... |

## Aeronáutico (plugin `aeronautico`)

| Skill | Para quê |
|---|---|
| `aero-acidente-aereo-indenizacao` | Redige ação indenizatória por acidente aéreo com morte ou lesão de passageiro, tripulante ou terceiro na superfície, proposta pela vítima ou pelos... |
| `aero-habeas-data-dados-de-passageiro` | Redige habeas data (CF art. 5º, LXXII; Lei 9.507/1997) ou, quando o banco não tiver caráter público, requerimento e ação de obrigação de fazer com... |
| `aero-infracao-aeronautica-jecrim` | Orienta a defesa no Juizado Especial Criminal (estadual ou federal) de infração de menor potencial ofensivo ligada à aviação: contravenção de abuso... |
| `aero-milhas-e-pontos` | Redige ação de obrigação de fazer cumulada com indenização contra programa de fidelidade de companhia aérea (ou de banco parceiro) por cancelamento,... |
| `aero-recurso-multa-anac` | Redige defesa contra auto de infração e recurso administrativo contra multa ou providência aplicada pela ANAC (empresa aérea, táxi aéreo, escola,... |
| `aero-reembolso-de-passagem` | Redige ação de restituição de valor de passagem aérea recusado ou retido pela companhia ou pela agência, seja por cancelamento do voo pela empresa... |

## Desportivo (plugin `desportivo`)

| Skill | Para quê |
|---|---|
| `desp-cobranca-luvas-premios-arena` | Redige ação de cobrança de luvas, prêmios por performance ou resultado, direito de imagem contratual e repasse do direito de arena devidos ao atleta... |
| `desp-contrato-de-agenciamento` | Elabora, revisa ou analisa a validade do contrato de agenciamento, intermediação e representação esportiva entre atleta (ou clube) e agente, com... |
| `desp-contrato-especial-de-trabalho-esportivo` | Elabora ou revisa o contrato especial de trabalho esportivo do atleta profissional (CETE), com prazo de 3 meses a 5 anos, cláusula indenizatória e... |
| `desp-defesa-antidoping` | Prepara a defesa de atleta ou pessoal de apoio acusado de violação de regra antidopagem — resposta à notificação da ABCD, audiência de suspensão... |
| `desp-defesa-disciplinar` | Prepara a defesa de atleta, treinador, dirigente, árbitro ou clube denunciado pela Procuradoria perante a Comissão Disciplinar ou o Tribunal de... |
| `desp-indenizacao-lesao-esportiva` | Redige reclamação trabalhista de atleta profissional lesionado em treino, jogo ou a serviço do clube, cobrando a indenização do seguro obrigatório de... |
| `desp-mandado-seguranca-suspensao-atleta` | Redige a impugnação urgente de suspensão de atleta: mandado de garantia perante o STJD/TJD (CBJD, arts. 88 a 94) ou o TJD-AD (Código Brasileiro... |
| `desp-nulidade-transferencia-internacional` | Estrutura a ação (ou a reclamação perante o órgão desportivo competente) de nulidade ou anulação de transferência internacional de atleta — cessão a... |
| `desp-patrocinio-e-cessao-de-imagem` | Elabora ou revisa contrato de patrocínio de atleta e contrato de cessão de direito de uso de imagem, nome e voz do atleta (com clube, marca ou... |
| `desp-recurso-stjd` | Redige recurso voluntário contra decisão de Comissão Disciplinar ou de Tribunal de Justiça Desportiva, dirigido ao TJD Pleno ou ao Superior Tribunal... |
| `desp-recurso-tas-cas` | Organiza a apelação (statement of appeal e appeal brief) à Corte Arbitral do Esporte (TAS/CAS), em Lausanne, contra decisão de federação... |
| `desp-rescisao-contrato-desportivo` | Redige reclamação trabalhista de atleta profissional para rescisão do contrato especial de trabalho esportivo (mora salarial ou de imagem, rescisão... |

## Militar (plugin `militar`)

| Skill | Para quê |
|---|---|
| `mil-defesa-criminal-militar` | Estrutura a defesa técnica no processo penal militar (CPM, Decreto-Lei 1.001/1969; CPPM, Decreto-Lei 1.002/1969): competência da Justiça Militar,... |
| `mil-habeas-corpus` | Redige habeas corpus na Justiça Militar (CF art. 5º, LXVIII; CPPM arts. 466 a 470), com escolha do juízo pela autoridade coatora (juiz federal da JM,... |
| `mil-indenizacao-acidente-em-servico` | Redige ação de indenização por danos morais, materiais e estéticos de militar (ou de seus dependentes, em caso de morte) vítima de acidente ou doença... |
| `mil-liberdade-provisoria` | Redige pedido de liberdade na Justiça Militar ao juiz da causa: relaxamento de flagrante ilegal, revogação da prisão preventiva (CPPM arts. 254 a... |
| `mil-mandado-de-seguranca` | Redige mandado de segurança contra ato de autoridade militar (CF art. 5º, LXIX; Lei 12.016/2009) — punição disciplinar, Conselho de Disciplina ou de... |
| `mil-recurso-disciplinar` | Redige defesa e recursos no processo disciplinar militar: pedido de reconsideração, recurso disciplinar hierárquico e cancelamento de registro de... |
| `mil-recurso-em-sentido-estrito` | Redige recurso em sentido estrito no processo penal militar (CPPM arts. 516 a 525): cabimento pelas alíneas do art. 516, prazo de três dias para... |
| `mil-reintegracao-e-reforma` | Redige ação para anular exclusão ilegal do serviço militar (licenciamento, desincorporação, exclusão a bem da disciplina) com reintegração, agregação... |
| `mil-revisao-criminal` | Redige revisão criminal de condenação transitada em julgado na Justiça Militar (CPPM arts. 550 a 562), com as hipóteses do art. 551 (sentença... |

## Eleitoral (plugin `eleitoral`)

| Skill | Para quê |
|---|---|
| `eleitoral-aije` | Redige ação de investigação judicial eleitoral (AIJE) pelo rito do art. 22 da LC 64/1990, por abuso de poder econômico ou político, uso indevido dos... |
| `eleitoral-aime` | Redige ação de impugnação de mandato eletivo (AIME) com base no art. 14, §§ 10 e 11, da Constituição, ajuizada em até 15 dias da diplomação, em... |
| `eleitoral-defesa-abuso-de-poder` | Redige a defesa de candidato, agente público ou terceiro em ação por abuso de poder e ilícitos de campanha — AIJE (art. 22 da LC 64/1990), AIME (art.... |
| `eleitoral-impugnacao-registro-candidatura` | Redige ação de impugnação de registro de candidatura (AIRC) e a contestação do candidato impugnado, pelo rito dos arts. 3º a 17 da LC 64/1990, com... |
| `eleitoral-prestacao-de-contas-campanha` | Orienta e redige a prestação de contas de campanha de candidato e partido e as manifestações no processo (resposta a diligências, defesa contra... |
| `eleitoral-recurso-eleitoral` | Redige recursos na Justiça Eleitoral pelo Código Eleitoral (Lei 4.737/1965) e pela CF, art. 121: recurso ao TRE contra decisão de juiz eleitoral,... |
| `eleitoral-representacao-propaganda-irregular` | Redige representação por propaganda eleitoral irregular pelo rito sumário do art. 96 da Lei 9.504/1997 (defesa em 48 horas, recurso em 24 horas), e a... |

## Internacional (plugin `internacional`)

| Skill | Para quê |
|---|---|
| `intl-apostilamento-legalizacao` | Orienta o apostilamento (Convenção da Apostila de Haia, Decreto 8.660/2016) e, quando o país não é parte, a legalização consular de documentos... |
| `intl-carta-rogatoria-exequatur` | Orienta a carta rogatória nas duas direções: a ativa (juiz brasileiro pede ato a autoridade estrangeira — citação, prova, intimação) e a passiva... |
| `intl-contrato-internacional` | Elabora ou revisa contrato internacional (compra e venda de mercadorias, fornecimento, distribuição, prestação de serviços transfronteiriça) com... |
| `intl-cooperacao-auxilio-direto` | Orienta pedido de cooperação jurídica internacional por auxílio direto (ativo ou passivo) e a defesa de quem é alvo de medida pedida por Estado... |
| `intl-defesa-extradicao` | Redige a defesa do extraditando no processo de extradição passiva perante o STF (Lei 13.445/2017, arts. 81 a 99; CF, art. 5º, LI e LII, e art. 102,... |
| `intl-homologacao-sentenca-estrangeira` | Redige pedido de homologação de decisão estrangeira (judicial ou arbitral) no STJ, ou a contestação a esse pedido, com base no art. 105, I, i, da CF,... |

## Agrário (plugin `agrario`)

| Skill | Para quê |
|---|---|
| `agrario-arrendamento-e-parceria-rural` | Redige e revisa contrato de arrendamento rural e de parceria rural (agrícola, pecuária, agroindustrial, extrativa) pelo Estatuto da Terra (Lei... |
| `agrario-desapropriacao-reforma-agraria` | Redige a contestação do expropriado na ação de desapropriação por interesse social para reforma agrária (CF arts. 184 a 186; LC 76/1993; Lei... |
| `agrario-imovel-rural-no-inventario` | Prepara o dossiê e o plano de partilha do imóvel rural no inventário judicial ou extrajudicial — CCIR (Lei 4.947/1966, art. 22, § 2º), ITR dos... |
| `agrario-regularizacao-fundiaria-rural` | Estrutura o requerimento de regularização fundiária de ocupação rural em terras da União (Lei 11.952/2009 — Amazônia Legal e, pelo art. 40-A, áreas... |

## Regulatório (plugin `regulatorio`)

| Skill | Para quê |
|---|---|
| `reg-defesa-processo-sancionador-agencia` | Redige defesa administrativa contra auto de infração ou notificação de processo sancionador instaurado por agência reguladora federal (ANEEL, ANATEL,... |
| `reg-defesa-sancionador-ans` | Redige defesa de operadora de plano de saúde (e de seus administradores) em processo administrativo sancionador da Agência Nacional de Saúde... |
| `reg-manifestacao-consulta-audiencia-publica` | Redige contribuição escrita em consulta pública e roteiro de manifestação oral em audiência pública de agência reguladora sobre minuta de ato... |
| `reg-pedido-outorga-licenca-agencia` | Redige requerimento administrativo de habilitação, registro, autorização, licença ou outorga perante agência reguladora (e pedidos correlatos de... |
| `reg-programa-integridade-compliance` | Estrutura programa de integridade anticorrupção e redige parecer de compliance regulatório (diagnóstico de aderência da empresa a normas setoriais e... |
| `reg-recurso-multa-agencia` | Redige recurso administrativo contra decisão de agência reguladora que aplicou multa ou outra sanção, com pedido de reconsideração, efeito suspensivo... |

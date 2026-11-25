# juris-skills-br

Skills jurídicas brasileiras para o Claude: estrutura de peças, requisitos, prazos e fundamentos verificados, organizados por área do direito.

**379 skills em 23 plugins**, com conteúdo conferido até 25/11/2026. Normas foram conferidas em fonte oficial (Planalto, Senado, Câmara e órgãos emissores) e precedentes foram conferidos no JuriBase; o que não foi confirmado vem marcado com [VERIFICAR].

> Ferramenta de apoio. O advogado responsável revisa toda peça antes do protocolo.

## Instalação no Claude Code

Adicione o marketplace uma vez:

```
/plugin marketplace add andersongadelhaadv-cmyk/juris-skills-br
```

Depois instale o núcleo e as áreas que você pratica:

```
/plugin install nucleo@juris-skills-br
/plugin install processo-civil@juris-skills-br
/plugin install trabalhista@juris-skills-br
```

O plugin `nucleo` é a base dos demais: concentra juros e correção, prazos, verificação de citações e estilo. Instale-o sempre.

## Plugins

| Plugin | Skills | Conteúdo |
| --- | --- | --- |
| `nucleo` | 6 | Camada comum: juros e correção, prazos processuais, verificação de citações, fidelidade factual, estilo forense e roteador de peças. |
| `processo-civil` | 34 | Peças do processo civil: inicial, contestação, réplica, reconvenção, tutelas, recursos (inclusive REsp com relevância), execução e juizado especial. |
| `trabalhista` | 38 | Peças trabalhistas: reclamação, contestação, recursos (RO, RR, agravos), execução, cálculos e temas recorrentes. |
| `previdenciario` | 25 | RGPS e RPPS: requerimento e recurso administrativo, aposentadorias da EC 103, incapacidade, BPC/LOAS, pensão, revisão, TNU. |
| `penal` | 31 | Defesa penal: resposta à acusação, habeas corpus, prisão e cautelares, recursos, execução penal, ANPP, júri, Maria da Penha, dosimetria. |
| `tributario-fazenda` | 37 | Tributário e Fazenda Pública: mandado de segurança, anulatória, repetição de indébito, execução fiscal, CARF, reforma tributária, cumprimento contra a Fazenda. |
| `familia-sucessoes` | 24 | Família e sucessões: alimentos, execução de alimentos, divórcio, guarda, união estável, paternidade, inventário, testamento e planejamento. |
| `consumidor` | 20 | Consumidor: indenizatória, vício, negativação, plano de saúde, revisional bancária, superendividamento, transporte aéreo e defesa do fornecedor. |
| `administrativo-licitacoes` | 16 | Administrativo e licitações (Lei 14.133): mandado de segurança, impugnação e recurso, sanções, reequilíbrio, improbidade, PAD, concurso, responsabilidade do Estado. |
| `contratos` | 22 | Contratos: elaboração, revisão e parecer; prestação de serviços, compra e venda, locação comercial, franquia, software/SaaS, NDA, distribuição e representação; aditivo, distrato e notificação de descumprimento. |
| `imobiliario` | 22 | Imobiliário: despejo, renovatória e revisional de aluguel; posse (reintegração, imissão, embargos de terceiro); usucapião judicial e extrajudicial; adjudicação compulsória; compra e venda, distrato e financiamento SFH; condomínio; matrícula, retificação, REURB, loteamento e incorporação. |
| `digital` | 15 | Direito digital e LGPD: remoção de conteúdo e perfil falso, ofensas e deepfake, conta bloqueada, crimes cibernéticos, direitos autorais online; LGPD (incidente, titular, DPA, política de privacidade, ANPD, vazamento); contrato de influenciador. |
| `bancario` | 10 | Bancário: fraude e transferência não autorizada, conta fantasma, SCR, revisional, repetição de indébito, busca e apreensão, alienação fiduciária e renegociação. |
| `saude` | 9 | Saúde: erro médico, responsabilidade hospitalar, plano de saúde (cobertura, reembolso, cancelamento), medicamento pelo SUS, ANVISA e defesa ética no CRM/CFM. |
| `societario` | 8 | Societário: contrato social, acordo de sócios, atas, holding familiar, M&A, due diligence, dissolução e parecer. |
| `ambiental` | 12 | Ambiental: ação civil pública, dano ambiental, defesa em auto de infração e crime ambiental, licenciamento, CAR/reserva legal, TAC e compliance. |
| `aeronautico` | 6 | Aeronáutico: reembolso de passagem, milhas e pontos, acidente aéreo, multas da ANAC, dados de passageiro e infração aeronáutica (atraso, cancelamento e bagagem ficam em consumidor-transporte-aereo). |
| `desportivo` | 12 | Desportivo: contrato de atleta, agenciamento, patrocínio e imagem, rescisão, luvas e premiações, STJD, TAS/CAS e antidoping. |
| `militar` | 9 | Militar: defesa criminal militar, habeas corpus e recursos na Justiça Militar (CPPM), PAD militar, reintegração e acidente em serviço. |
| `eleitoral` | 7 | Eleitoral: registro de candidatura, propaganda irregular, AIJE, AIME, abuso de poder, prestação de contas e recurso eleitoral. |
| `internacional` | 6 | Internacional: contrato internacional, homologação de sentença estrangeira, carta rogatória, cooperação jurídica, apostilamento e extradição. |
| `agrario` | 4 | Agrário: arrendamento e parceria rural, usucapião rural, posse rural, regularização fundiária rural, desapropriação e inventário de imóvel rural. |
| `regulatorio` | 6 | Regulatório: processo sancionador e multas de agências reguladoras (inclusive ANS), habilitação e licenças, audiência pública, compliance e programa de integridade. |


## Como as skills funcionam

- **Estrutura, não minuta pronta.** Cada skill traz entradas mínimas, prazo, estrutura da peça, requisitos, fundamentos, pedidos, checklist pré-protocolo e erros a evitar. O texto do caso é redigido na hora, a partir dos fatos que você informa.
- **Juros e correção centralizados.** Nenhuma skill de área define taxa própria; todas aplicam `nucleo/juros-e-correcao` (Lei 14.905/2024, ADC 58, EC 113/2021 e EC 136/2025).
- **Registro de verificação.** Cada skill tem um `fontes.yaml` com a norma ou precedente, o status, o link oficial e a data da consulta. Nesta versão: 636 citações de jurisprudência confirmadas, 415 registros de normas e 43 itens marcados para conferência.
- **Marcação `[VERIFICAR]`.** O que não pôde ser confirmado em fonte oficial aparece marcado no texto. Confira antes de usar.
- **Detalhe sob demanda.** O `SKILL.md` é curto; o roteiro completo da peça e os fundamentos ficam em `references/`.

## Skills por área

<details>
<summary><b>Núcleo</b> — 6 skills</summary>

| Skill | Conteúdo |
| --- | --- |
| `estilo-forense` | Estilo forense |
| `fidelidade-factual` | Fidelidade factual |
| `juros-e-correcao` | Juros e correção monetária |
| `prazos-processuais` | Prazos processuais |
| `roteador-de-pecas` | Roteador de peças |
| `verificacao-de-citacoes` | Verificação de citações |

</details>

<details>
<summary><b>Processo civil</b> — 34 skills</summary>

| Skill | Conteúdo |
| --- | --- |
| `civel-acao-de-cobranca` | Ação de cobrança (procedimento comum) |
| `civel-acao-de-exigir-contas` | Ação de exigir contas (CPC, arts. 550 a 553) |
| `civel-acao-declaratoria` | Ação declaratória cível |
| `civel-acao-indenizatoria` | Ação indenizatória cível (responsabilidade civil comum) |
| `civel-acao-monitoria` | Ação monitória (e embargos monitórios) |
| `civel-acao-rescisoria` | Ação rescisória cível |
| `civel-acordo-judicial-e-extrajudicial` | Acordo cível judicial e extrajudicial (transação e homologação) |
| `civel-agravo-de-instrumento` | Agravo de instrumento |
| `civel-agravo-interno` | Agravo interno |
| `civel-alegacoes-finais` | Alegações finais cíveis (debates ou memoriais) |
| `civel-apelacao` | Apelação cível |
| `civel-consignacao-em-pagamento` | Consignação em pagamento (obrigação civil) |
| `civel-contestacao` | Contestação cível |
| `civel-cumprimento-de-sentenca` | Cumprimento de sentença (cível) |
| `civel-embargos-a-execucao` | Embargos à execução (título extrajudicial) |
| `civel-embargos-de-declaracao` | Embargos de declaração (cível) |
| `civel-excecao-de-pre-executividade` | Exceção de pré-executividade |
| `civel-execucao-titulo-extrajudicial` | Execução de título extrajudicial |
| `civel-habilitacao-de-credito-recuperacao-falencia` | Habilitação e impugnação de crédito na recuperação judicial e na falência |
| `civel-impugnacao-ao-cumprimento` | Impugnação ao cumprimento de sentença |
| `civel-incidente-de-desconsideracao` | Incidente de desconsideração da personalidade jurídica (CPC 133-137; CC 50) |
| `civel-juizado-especial` | Juizado Especial Cível (inicial, contestação, recurso inominado) |
| `civel-notificacao-extrajudicial` | Notificação extrajudicial cível |
| `civel-obrigacao-de-fazer-ou-nao-fazer` | Ação de obrigação de fazer ou de não fazer |
| `civel-oposicao` | Oposição (CPC, arts. 682 a 686) |
| `civel-parecer-juridico` | Parecer jurídico cível e processual |
| `civel-peticao-inicial` | Petição inicial cível (procedimento comum) |
| `civel-procuracao-e-substabelecimento` | Procuração judicial e substabelecimento |
| `civel-producao-antecipada-de-provas` | Produção antecipada de provas (CPC, arts. 381 a 383) |
| `civel-reconvencao` | Reconvenção |
| `civel-recurso-especial` | Recurso especial (cível) |
| `civel-recurso-extraordinario` | Recurso extraordinário (cível) |
| `civel-replica` | Réplica (manifestação sobre a contestação) |
| `civel-tutela-provisoria` | Tutela provisória (urgência e evidência) |

</details>

<details>
<summary><b>Trabalhista</b> — 38 skills</summary>

| Skill | Conteúdo |
| --- | --- |
| `trabalhista-acao-anulatoria-clausula-coletiva` | Ação anulatória de cláusula de norma coletiva |
| `trabalhista-acao-rescisoria` | Ação rescisória trabalhista |
| `trabalhista-acidente-e-doenca-ocupacional` | Acidente do trabalho e doença ocupacional |
| `trabalhista-acordo-extrajudicial` | Homologação de acordo extrajudicial |
| `trabalhista-acordo-na-execucao` | Acordo na fase de execução trabalhista |
| `trabalhista-agravo-de-instrumento` | Agravo de instrumento trabalhista |
| `trabalhista-agravo-de-peticao` | Agravo de petição |
| `trabalhista-assedio-moral-e-sexual` | Assédio moral e sexual no trabalho (indenização) |
| `trabalhista-auditoria-de-peticao-inicial` | Auditoria de petição inicial trabalhista (art. 840 §1º) |
| `trabalhista-compliance` | Compliance trabalhista |
| `trabalhista-contestacao` | Contestação trabalhista |
| `trabalhista-contrato-de-trabalho` | Elaboração de contrato de trabalho (CLT) |
| `trabalhista-dano-existencial` | Dano existencial (jornada exaustiva) |
| `trabalhista-dissidio-coletivo` | Dissídio coletivo |
| `trabalhista-embargos-a-execucao` | Embargos à execução trabalhista |
| `trabalhista-embargos-de-declaracao` | Embargos de declaração trabalhistas |
| `trabalhista-embargos-sdi1` | Embargos à SDI-1 do TST |
| `trabalhista-excecao-pre-executividade` | Exceção de pré-executividade trabalhista |
| `trabalhista-impugnacao-de-calculos` | Impugnação aos cálculos de liquidação |
| `trabalhista-insalubridade-periculosidade` | Adicionais de insalubridade e periculosidade |
| `trabalhista-justa-causa` | Justa causa — aplicação e defesa (CLT art. 482) |
| `trabalhista-mandado-de-seguranca` | Mandado de segurança trabalhista |
| `trabalhista-notificacao-extrajudicial` | Notificação extrajudicial trabalhista |
| `trabalhista-parecer-juridico` | Parecer jurídico trabalhista |
| `trabalhista-reclamacao` | Reclamação trabalhista (petição inicial) |
| `trabalhista-recurso-adesivo` | Recurso adesivo trabalhista |
| `trabalhista-recurso-de-revista` | Recurso de revista |
| `trabalhista-recurso-ordinario` | Recurso ordinário trabalhista |
| `trabalhista-replica` | Réplica trabalhista (manifestação sobre defesa e documentos) |
| `trabalhista-rescisao-indireta` | Rescisão indireta |
| `trabalhista-revisao-de-contrato-de-trabalho` | Análise e revisão de contrato de trabalho |
| `trabalhista-teletrabalho` | Teletrabalho e home office (CLT arts. 75-A a 75-F) |
| `trabalhista-terceirizacao` | Terceirização e responsabilidade do tomador (Lei 6.019/1974) |
| `trabalhista-trabalho-intermitente` | Trabalho intermitente (CLT arts. 443, § 3º, e 452-A) |
| `trabalhista-triagem-de-reclamatoria` | Triagem de reclamatória recebida (risco antes da defesa) |
| `trabalhista-tutela-de-urgencia` | Tutela de urgência trabalhista |
| `trabalhista-verbas-rescisorias` | Cálculo e conferência de verbas rescisórias |
| `trabalhista-vinculo-de-emprego` | Reconhecimento de vínculo de emprego |

</details>

<details>
<summary><b>Previdenciário</b> — 25 skills</summary>

| Skill | Conteúdo |
| --- | --- |
| `prev-acidentario` | Ação acidentária e auxílio-acidente |
| `prev-agravo-de-instrumento-previdenciario` | Agravo de instrumento previdenciário |
| `prev-apelacao-previdenciaria` | Apelação previdenciária |
| `prev-aposentadoria-especial` | Aposentadoria especial e conversão de tempo especial |
| `prev-aposentadoria-por-idade-urbana` | Aposentadoria por idade urbana (EC 103/2019, arts. 18 e 19) |
| `prev-auxilio-acidente-previdenciario` | Auxílio-acidente previdenciário (acidente de qualquer natureza) |
| `prev-averbacao-tempo-de-contribuicao` | Averbação de tempo de contribuição (urbano, militar, aluno-aprendiz) |
| `prev-beneficio-por-incapacidade` | Benefícios por incapacidade (temporária e permanente) |
| `prev-bpc-loas` | BPC/LOAS (pessoa com deficiência e pessoa idosa) |
| `prev-certidao-de-tempo-de-contribuicao` | Certidão de Tempo de Contribuição (CTC) para regime próprio |
| `prev-embargos-de-declaracao-previdenciarios` | Embargos de declaração previdenciários |
| `prev-impugnacao-laudo-pericial` | Impugnação ao laudo da perícia médica judicial |
| `prev-inicial-aposentadoria` | Petição inicial de aposentadoria (RGPS) |
| `prev-mandado-de-seguranca-demora-inss` | Mandado de segurança contra demora do INSS |
| `prev-pedido-de-uniformizacao-tnu` | Pedido de uniformização (TRU/TNU) |
| `prev-pensao-por-morte` | Pensão por morte (RGPS) |
| `prev-planejamento-previdenciario` | Planejamento previdenciário (parecer) |
| `prev-recurso-crps` | Recurso ao CRPS (Juntas e Câmaras) |
| `prev-requerimento-administrativo` | Requerimento administrativo ao INSS |
| `prev-revisao-da-vida-toda-acoes-pendentes` | Revisão da vida toda: tese superada e ações pendentes |
| `prev-revisao-de-beneficio` | Revisão de benefício previdenciário |
| `prev-rpps-servidor` | RPPS da União: aposentadoria e abono de permanência |
| `prev-salario-maternidade` | Salário-maternidade |
| `prev-tempo-rural-e-segurado-especial` | Tempo rural e segurado especial |
| `prev-tutela-de-urgencia-previdenciaria` | Tutela de urgência previdenciária |

</details>

<details>
<summary><b>Penal</b> — 31 skills</summary>

| Skill | Conteúdo |
| --- | --- |
| `penal-acesso-aos-autos-do-inquerito` | Acesso da defesa aos autos do inquérito |
| `penal-agravo-em-execucao` | Agravo em execução penal |
| `penal-alegacoes-finais` | Alegações finais (memoriais) da defesa |
| `penal-anpp` | Acordo de não persecução penal (ANPP) |
| `penal-apelacao-criminal` | Apelação criminal |
| `penal-arguicao-de-nulidades` | Arguição de nulidades processuais penais |
| `penal-defesa-em-pic` | Defesa em procedimento investigatório criminal (PIC) do Ministério Público |
| `penal-defesa-falta-grave` | Defesa em procedimento de falta grave |
| `penal-defesa-no-inquerito-policial` | Defesa no inquérito policial |
| `penal-dosimetria` | Dosimetria da pena |
| `penal-embargos-de-declaracao` | Embargos de declaração penais |
| `penal-embargos-infringentes-e-de-nulidade` | Embargos infringentes e de nulidade |
| `penal-excecao-de-suspeicao-e-impedimento` | Exceção de suspeição e arguição de impedimento |
| `penal-habeas-corpus` | Habeas corpus |
| `penal-impronuncia-absolvicao-sumaria-desclassificacao` | Impronúncia, absolvição sumária e desclassificação no júri |
| `penal-indulto-e-comutacao` | Indulto e comutação de pena |
| `penal-liberdade-provisoria-e-relaxamento` | Liberdade provisória, relaxamento e revogação da preventiva |
| `penal-livramento-condicional` | Livramento condicional |
| `penal-mandado-de-seguranca-criminal` | Mandado de segurança em matéria penal |
| `penal-maria-da-penha-medidas-protetivas` | Medidas protetivas da Lei Maria da Penha (ofendida e requerido) |
| `penal-parecer-criminal` | Parecer criminal (consultivo) |
| `penal-plenario-do-juri` | Plenário do Tribunal do Júri — defesa |
| `penal-progressao-de-regime` | Progressão de regime |
| `penal-queixa-crime` | Queixa-crime |
| `penal-recurso-em-sentido-estrito` | Recurso em sentido estrito (RESE) |
| `penal-recurso-especial-criminal` | Recurso especial criminal |
| `penal-recurso-extraordinario-criminal` | Recurso extraordinário criminal |
| `penal-remicao-de-pena` | Remição de pena por trabalho e estudo |
| `penal-resposta-a-acusacao` | Resposta à acusação e defesa prévia |
| `penal-revisao-criminal` | Revisão criminal |
| `penal-revogacao-de-cautelares-diversas` | Revogação, substituição e flexibilização de cautelares diversas da prisão |

</details>

<details>
<summary><b>Tributário e Fazenda Pública</b> — 37 skills</summary>

| Skill | Conteúdo |
| --- | --- |
| `fazenda-contestacao-fazendaria` | Contestação da Fazenda Pública |
| `fazenda-cumprimento-contra-a-fazenda` | Cumprimento de sentença contra a Fazenda Pública |
| `fazenda-execucao-fiscal-inicial` | Petição inicial de execução fiscal (lado da Fazenda) |
| `trib-acao-anulatoria` | Ação anulatória de débito fiscal |
| `trib-acao-regressiva-corresponsaveis` | Ação regressiva contra corresponsáveis tributários |
| `trib-acao-rescisoria` | Ação rescisória tributária |
| `trib-agravo-de-instrumento` | Agravo de instrumento em matéria tributária |
| `trib-amicus-curiae` | Manifestação como amicus curiae em matéria tributária |
| `trib-cancelamento-de-cda` | Cancelamento e nulidade de CDA |
| `trib-certidao-negativa-cpen` | Certidão negativa e positiva com efeito de negativa |
| `trib-compensacao-per-dcomp` | Compensação tributária federal (PER/DCOMP) |
| `trib-compliance-tributario` | Compliance tributário — programa e revisão de rotinas |
| `trib-consignacao-em-pagamento` | Consignação em pagamento tributária |
| `trib-consulta-tributaria-formal` | Consulta tributária formal (federal) |
| `trib-declaratoria-inexistencia-relacao-tributaria` | Ação declaratória de inexistência de relação jurídico-tributária |
| `trib-defesa-administrativa-e-carf` | Defesa administrativa tributária e recurso ao CARF |
| `trib-defesa-cautelar-fiscal` | Defesa em medida cautelar fiscal |
| `trib-defesa-redirecionamento-socio` | Defesa contra o redirecionamento da execução fiscal ao sócio |
| `trib-embargos-a-execucao-fiscal` | Embargos à execução fiscal |
| `trib-embargos-de-terceiro-execucao-fiscal` | Embargos de terceiro em execução fiscal |
| `trib-enquadramento-regime-especial` | Requerimento de enquadramento em regime especial de tributação |
| `trib-excecao-pre-executividade-fiscal` | Exceção de pré-executividade em execução fiscal |
| `trib-garantia-antecipada-certidao` | Garantia antecipada para obter certidão |
| `trib-habilitacao-de-credito-judicial` | Habilitação de crédito tributário reconhecido judicialmente |
| `trib-mandado-de-seguranca` | Mandado de segurança tributário |
| `trib-memorial-e-sustentacao-oral-carf` | Memorial e sustentação oral no CARF |
| `trib-parcelamento-e-regularizacao` | Parcelamento e programas de regularização fiscal |
| `trib-parecer-tributario` | Parecer tributário consultivo |
| `trib-planejamento-tributario` | Planejamento tributário — parecer de estruturação |
| `trib-prescricao-intercorrente` | Prescrição intercorrente, prescrição e decadência tributária |
| `trib-recurso-administrativo-estadual` | Recurso no processo administrativo tributário estadual |
| `trib-recurso-especial-csrf` | Recurso especial à Câmara Superior de Recursos Fiscais |
| `trib-recurso-especial-tributario` | Recurso especial tributário (recorte) |
| `trib-reforma-tributaria-ibs-cbs` | Parecer sobre a reforma tributária do consumo (IBS, CBS e IS) |
| `trib-repeticao-de-indebito` | Ação de repetição de indébito tributário |
| `trib-revisao-de-lancamento-de-oficio` | Revisão de lançamento de ofício |
| `trib-transacao-tributaria` | Transação tributária (Lei 13.988/2020) |

</details>

<details>
<summary><b>Família e sucessões</b> — 24 skills</summary>

| Skill | Conteúdo |
| --- | --- |
| `familia-acao-de-alimentos` | Ação de alimentos (inicial) |
| `familia-acordo-extrajudicial-homologacao` | Acordo extrajudicial de família e pedido de homologação |
| `familia-adocao` | Adoção |
| `familia-alvara-judicial` | Alvará judicial (jurisdição voluntária) |
| `familia-busca-e-apreensao-de-menor` | Busca e apreensão de menor |
| `familia-destituicao-do-poder-familiar` | Destituição e suspensão do poder familiar |
| `familia-divorcio` | Divórcio (litigioso, consensual judicial e extrajudicial) |
| `familia-emancipacao` | Emancipação |
| `familia-execucao-de-alimentos` | Execução / cumprimento de sentença de alimentos |
| `familia-filiacao-socioafetiva` | Filiação socioafetiva e multiparentalidade |
| `familia-guarda-e-convivencia` | Guarda e convivência |
| `familia-interdicao-e-curatela` | Curatela (interdição) e tomada de decisão apoiada |
| `familia-investigacao-de-paternidade` | Investigação de paternidade |
| `familia-negatoria-de-paternidade` | Negatória de paternidade |
| `familia-pacto-antenupcial` | Pacto antenupcial |
| `familia-parecer` | Parecer de direito de família |
| `familia-partilha-posterior-e-sobrepartilha` | Partilha posterior ao divórcio e sobrepartilha |
| `familia-revisional-e-exoneracao-de-alimentos` | Revisional e exoneração de alimentos |
| `familia-tutela-de-menor` | Tutela de menor |
| `familia-uniao-estavel` | União estável: reconhecimento e dissolução |
| `sucessoes-inventario-extrajudicial` | Inventário extrajudicial (escritura pública) |
| `sucessoes-inventario-judicial` | Inventário judicial |
| `sucessoes-planejamento-e-partilha-em-vida` | Planejamento sucessório e partilha em vida (consultivo) |
| `sucessoes-testamento` | Testamento: elaboração e cumprimento |

</details>

<details>
<summary><b>Consumidor</b> — 20 skills</summary>

| Skill | Conteúdo |
| --- | --- |
| `consumidor-acao-coletiva` | Ação coletiva de consumo (CDC, arts. 81 a 104) |
| `consumidor-acao-indenizatoria` | Ação indenizatória de consumo (fato do produto ou do serviço) |
| `consumidor-acordo-judicial` | Acordo em ação de consumo (transação e homologação) |
| `consumidor-clausulas-abusivas` | Cláusulas abusivas em contrato de consumo (CDC, arts. 51 a 53) |
| `consumidor-contratos-bancarios-revisional` | Revisional de contrato bancário (consumo) |
| `consumidor-defesa-do-fornecedor` | Contestação do fornecedor em ação de consumo |
| `consumidor-defesa-procon` | Defesa em processo administrativo do Procon (Decreto 2.181/1997) |
| `consumidor-desconsideracao-personalidade-juridica` | Desconsideração da personalidade jurídica no CDC (art. 28) |
| `consumidor-direito-de-arrependimento` | Direito de arrependimento (CDC, art. 49) |
| `consumidor-negativacao-indevida` | Negativação indevida |
| `consumidor-notificacao-extrajudicial` | Notificação extrajudicial consumerista |
| `consumidor-parecer` | Parecer de direito do consumidor |
| `consumidor-plano-de-saude` | Plano de saúde — negativa de cobertura com tutela de urgência |
| `consumidor-publicidade-enganosa` | Publicidade enganosa ou abusiva (CDC, arts. 36 a 38 e 67) |
| `consumidor-recall` | Recall e fato do produto (CDC, arts. 10, 12 e 13) |
| `consumidor-recurso-consumerista` | Recurso em ação de consumo (enfoque consumerista) |
| `consumidor-repeticao-em-dobro` | Repetição do indébito em dobro (CDC art. 42, p.ú.) |
| `consumidor-superendividamento` | Superendividamento — repactuação de dívidas |
| `consumidor-transporte-aereo` | Transporte aéreo de passageiros |
| `consumidor-vicio-do-produto-ou-servico` | Vício do produto ou do serviço |

</details>

<details>
<summary><b>Administrativo e licitações</b> — 16 skills</summary>

| Skill | Conteúdo |
| --- | --- |
| `adm-acao-anulatoria-de-ato-administrativo` | Ação anulatória de ato administrativo |
| `adm-acao-de-improbidade` | Ação de improbidade administrativa (autor) |
| `adm-acao-popular` | Ação popular (Lei 4.717/1965) |
| `adm-acesso-a-informacao-lai` | Pedido de acesso à informação (LAI) e recursos |
| `adm-anulacao-de-ato-por-autotutela` | Anulação de ato pela via administrativa (autotutela) |
| `adm-concurso-publico` | Concurso público — nomeação e controle de atos da banca |
| `adm-defesa-em-improbidade` | Defesa em ação de improbidade administrativa |
| `adm-defesa-em-pad` | Defesa em processo administrativo disciplinar (Lei 8.112/1990) |
| `adm-defesa-em-processo-sancionador-licitacao` | Defesa em processo sancionador de licitações e contratos |
| `adm-desapropriacao-defesa` | Defesa do expropriado (Decreto-Lei 3.365/1941) |
| `adm-impugnacao-ao-edital` | Impugnação ao edital (Lei 14.133/2021, art. 164) |
| `adm-mandado-de-seguranca` | Mandado de segurança (Lei 12.016/2009) |
| `adm-pedido-de-reequilibrio-economico-financeiro` | Pedido de reequilíbrio econômico-financeiro |
| `adm-recurso-contra-auto-de-infracao` | Defesa e recurso contra auto de infração administrativo |
| `adm-recurso-em-licitacao` | Recurso em licitação (Lei 14.133/2021, arts. 165 a 168) |
| `adm-responsabilidade-civil-do-estado` | Responsabilidade civil do Estado (CF art. 37, § 6º) |

</details>

<details>
<summary><b>Contratos</b> — 22 skills</summary>

| Skill | Conteúdo |
| --- | --- |
| `contratos-aditivo-contratual` | Termo aditivo contratual |
| `contratos-agencia-e-distribuicao` | Agência e distribuição |
| `contratos-analise-e-revisao-de-contrato` | Análise e revisão de contrato |
| `contratos-cessao-de-direitos` | Cessão de crédito, de posição contratual e de direitos |
| `contratos-clausula-penal` | Cláusula penal |
| `contratos-comodato` | Comodato |
| `contratos-compra-e-venda-empresarial` | Compra e venda empresarial |
| `contratos-distrato-e-rescisao` | Distrato e rescisão de contrato |
| `contratos-elaboracao-de-contrato` | Elaboração de contrato (roteiro geral) |
| `contratos-franquia-e-cof` | Franquia e Circular de Oferta de Franquia |
| `contratos-licenca-de-software-e-saas` | Licença de software e SaaS |
| `contratos-locacao-comercial` | Locação comercial (não residencial) |
| `contratos-memorando-de-entendimentos` | Memorando de entendimentos / carta de intenções |
| `contratos-nda-confidencialidade` | Acordo de confidencialidade (NDA) |
| `contratos-notificacao-de-descumprimento` | Notificação de descumprimento contratual |
| `contratos-parceria-e-joint-venture` | Parceria empresarial, consórcio e joint venture |
| `contratos-parecer-sobre-contrato` | Parecer sobre contrato |
| `contratos-prestacao-de-servicos` | Contrato de prestação de serviços |
| `contratos-prestacao-de-servicos-pj` | Prestação de serviços por pessoa jurídica (mitigação de vínculo) |
| `contratos-representacao-comercial` | Representação comercial autônoma |
| `contratos-sla-nivel-de-servico` | Acordo de nível de serviço (SLA) |
| `contratos-termo-de-responsabilidade` | Termo de responsabilidade |

</details>

<details>
<summary><b>Imobiliário</b> — 22 skills</summary>

| Skill | Conteúdo |
| --- | --- |
| `imob-acao-de-despejo` | Ação de despejo |
| `imob-acao-renovatoria` | Ação renovatória |
| `imob-acao-revisional-de-aluguel` | Ação revisional de aluguel |
| `imob-adjudicacao-compulsoria` | Adjudicação compulsória (judicial e extrajudicial) |
| `imob-analise-de-matricula-e-due-diligence` | Análise de matrícula e due diligence imobiliária |
| `imob-cobranca-de-taxas-condominiais` | Cobrança de taxas condominiais |
| `imob-compra-e-venda-de-imovel` | Compra e venda de imóvel (promessa e contrato definitivo) |
| `imob-distrato-imobiliario` | Distrato e resolução de promessa de compra e venda na planta |
| `imob-embargos-de-terceiro` | Embargos de terceiro (imóvel) |
| `imob-imissao-na-posse` | Imissão na posse |
| `imob-incorporacao-imobiliaria` | Incorporação imobiliária — registro e compliance |
| `imob-locacao-residencial` | Contrato de locação residencial |
| `imob-loteamento-irregular-defesa-do-adquirente` | Loteamento irregular — defesa do adquirente |
| `imob-notificacao-extrajudicial-imobiliaria` | Notificação extrajudicial imobiliária |
| `imob-parecer-juridico-imobiliario` | Parecer jurídico imobiliário |
| `imob-prestacao-de-contas-de-condominio` | Prestação de contas de condomínio |
| `imob-regularizacao-fundiaria-reurb` | Regularização Fundiária Urbana (Reurb-S e Reurb-E) |
| `imob-reintegracao-de-posse` | Ações possessórias — reintegração, manutenção e interdito proibitório |
| `imob-retificacao-de-area` | Retificação de registro e de área |
| `imob-revisao-de-financiamento-sfh` | Revisão de financiamento habitacional (SFH/SFI) e uso do FGTS |
| `imob-usucapiao-extrajudicial` | Usucapião extrajudicial (art. 216-A da Lei 6.015/1973) |
| `imob-usucapiao-judicial` | Usucapião judicial de imóvel |

</details>

<details>
<summary><b>Digital e LGPD</b> — 15 skills</summary>

| Skill | Conteúdo |
| --- | --- |
| `digital-contrato-de-influenciador` | Contrato de influenciador digital |
| `digital-contrato-dpa-operador` | Acordo de tratamento de dados (DPA) — controlador e operador |
| `digital-crime-cibernetico` | Crime cibernético — atuação pela vítima |
| `digital-deepfake-e-uso-de-imagem` | Deepfake, montagem e uso indevido de imagem ou voz |
| `digital-defesa-em-processo-sancionador-anpd` | Defesa em processo sancionador da ANPD |
| `digital-direitos-autorais-online` | Direitos autorais na internet |
| `digital-indenizacao-por-vazamento-de-dados` | Indenização por vazamento de dados pessoais |
| `digital-notificacao-de-incidente-lgpd` | Notificação de incidente de segurança (LGPD) |
| `digital-ofensas-em-redes-sociais` | Ofensas em redes sociais: indenização e direito de resposta |
| `digital-perfil-falso-e-impersonation` | Perfil falso e uso indevido de identidade |
| `digital-politica-de-privacidade-e-termos-de-uso` | Política de privacidade e termos de uso |
| `digital-remocao-de-conteudo` | Remoção de conteúdo da internet |
| `digital-remocao-indevida-de-conteudo` | Remoção indevida de conteúdo ou suspensão de conta |
| `digital-resposta-a-titular-de-dados` | Resposta a requisição de titular de dados |
| `digital-restauracao-de-conta` | Restauração de conta em plataforma digital |

</details>

<details>
<summary><b>Bancário</b> — 10 skills</summary>

| Skill | Conteúdo |
| --- | --- |
| `banc-busca-e-apreensao-contestacao` | Contestação em busca e apreensão (DL 911/1969) |
| `banc-consignacao-e-purgacao-da-mora` | Consignação em pagamento e purgação da mora (contrato bancário) |
| `banc-conta-aberta-indevidamente` | Conta aberta indevidamente (conta fantasma) |
| `banc-defesa-execucao-alienacao-fiduciaria` | Defesa em execução com alienação fiduciária |
| `banc-fraude-pix-e-transferencia-nao-autorizada` | Fraude em conta: Pix e transferências não autorizadas |
| `banc-inscricao-indevida-no-scr` | Inscrição indevida no SCR do Banco Central |
| `banc-med-pix-devolucao` | MED do Pix: requerimento de devolução e bloqueio |
| `banc-reclamacao-bacen-e-ouvidoria` | Reclamação à ouvidoria e ao Banco Central |
| `banc-renegociacao-extrajudicial-de-divida` | Renegociação extrajudicial de dívida bancária (proposta e acordo) |
| `banc-repeticao-de-indebito-bancario` | Repetição de indébito bancário (débitos em conta) |

</details>

<details>
<summary><b>Saúde</b> — 9 skills</summary>

| Skill | Conteúdo |
| --- | --- |
| `saude-defesa-do-medico` | Defesa do médico em ação de erro médico |
| `saude-defesa-etica-medica-crm` | Defesa ético-disciplinar do médico no CRM e recurso ao CFM |
| `saude-indenizacao-erro-medico` | Indenização por erro médico |
| `saude-medicamento-sem-registro-anvisa` | Medicamento sem registro na Anvisa / ação contra a Anvisa |
| `saude-medicamento-tratamento-sus` | Medicamento e tratamento pelo SUS (inclusive alto custo, com tutela de urgência) |
| `saude-notificacao-extrajudicial-plano-de-saude` | Notificação extrajudicial à operadora de plano de saúde |
| `saude-reembolso-plano-de-saude` | Reembolso de despesas médicas pelo plano de saúde |
| `saude-rescisao-unilateral-plano-de-saude` | Cancelamento unilateral do plano de saúde — ação de restabelecimento |
| `saude-responsabilidade-civil-hospitalar` | Responsabilidade civil hospitalar (inclusive infecção hospitalar) |

</details>

<details>
<summary><b>Societário</b> — 8 skills</summary>

| Skill | Conteúdo |
| --- | --- |
| `soc-acordo-de-socios` | Acordo de sócios (acionistas e quotistas) |
| `soc-ata-de-reuniao-de-socios` | Ata de reunião ou assembleia de sócios (LTDA) |
| `soc-contrato-social-ltda` | Contrato social de sociedade limitada |
| `soc-dissolucao-parcial-e-exclusao-de-socio` | Dissolução parcial, apuração de haveres e exclusão de sócio |
| `soc-due-diligence-societaria` | Due diligence jurídica societária |
| `soc-holding-familiar` | Holding familiar — estruturação e contrato social |
| `soc-ma-compra-de-quotas-e-acoes` | M&A — compra e venda de quotas ou ações |
| `soc-parecer-societario` | Parecer societário |

</details>

<details>
<summary><b>Ambiental</b> — 12 skills</summary>

| Skill | Conteúdo |
| --- | --- |
| `amb-acao-civil-publica` | Ação civil pública ambiental |
| `amb-auditoria-compliance` | Auditoria e compliance ambiental |
| `amb-defesa-acao-civil-publica` | Defesa em ação civil pública ambiental |
| `amb-defesa-auto-de-infracao` | Defesa em auto de infração ambiental |
| `amb-defesa-crime-ambiental` | Defesa em crime ambiental |
| `amb-indenizacao-dano-ambiental-individual` | Indenização por dano ambiental individual e vizinhança |
| `amb-licenca-de-operacao-corretiva` | Licença de Operação Corretiva (licenciamento corretivo) |
| `amb-mandado-de-seguranca-licenciamento` | Mandado de segurança contra ato de licenciamento ambiental |
| `amb-recurso-auto-de-infracao` | Recurso administrativo contra decisão em auto de infração ambiental |
| `amb-recurso-no-licenciamento` | Impugnação e recurso no licenciamento ambiental |
| `amb-reserva-legal-e-car` | Regularização de reserva legal e CAR |
| `amb-termo-ajustamento-conduta` | Termo de ajustamento de conduta ambiental |

</details>

<details>
<summary><b>Aeronáutico</b> — 6 skills</summary>

| Skill | Conteúdo |
| --- | --- |
| `aero-acidente-aereo-indenizacao` | Indenização por acidente aéreo (vítimas e familiares) |
| `aero-habeas-data-dados-de-passageiro` | Habeas data e acesso a dados de passageiro |
| `aero-infracao-aeronautica-jecrim` | Infração aeronáutica no Juizado Especial Criminal |
| `aero-milhas-e-pontos` | Milhas e pontos: cancelamento, expiração e bloqueio indevidos |
| `aero-recurso-multa-anac` | Defesa e recurso contra multa da ANAC |
| `aero-reembolso-de-passagem` | Reembolso de passagem aérea recusado |

</details>

<details>
<summary><b>Desportivo</b> — 12 skills</summary>

| Skill | Conteúdo |
| --- | --- |
| `desp-cobranca-luvas-premios-arena` | Cobrança de luvas, prêmios e direito de arena |
| `desp-contrato-de-agenciamento` | Contrato de agenciamento esportivo |
| `desp-contrato-especial-de-trabalho-esportivo` | Contrato especial de trabalho esportivo |
| `desp-defesa-antidoping` | Defesa em processo antidopagem |
| `desp-defesa-disciplinar` | Defesa disciplinar na Justiça Desportiva |
| `desp-indenizacao-lesao-esportiva` | Indenização por lesão esportiva |
| `desp-mandado-seguranca-suspensao-atleta` | Mandado de segurança (e de garantia) contra suspensão de atleta |
| `desp-nulidade-transferencia-internacional` | Nulidade de transferência internacional de atleta |
| `desp-patrocinio-e-cessao-de-imagem` | Patrocínio e cessão de imagem de atleta |
| `desp-recurso-stjd` | Recurso voluntário ao STJD |
| `desp-recurso-tas-cas` | Recurso ao TAS/CAS |
| `desp-rescisao-contrato-desportivo` | Rescisão do contrato desportivo (cláusulas indenizatória e compensatória) |

</details>

<details>
<summary><b>Militar</b> — 9 skills</summary>

| Skill | Conteúdo |
| --- | --- |
| `mil-defesa-criminal-militar` | Defesa criminal militar |
| `mil-habeas-corpus` | Habeas corpus na Justiça Militar |
| `mil-indenizacao-acidente-em-servico` | Indenização por acidente em serviço militar |
| `mil-liberdade-provisoria` | Liberdade provisória, revogação de preventiva e menagem (CPPM) |
| `mil-mandado-de-seguranca` | Mandado de segurança contra ato de autoridade militar |
| `mil-recurso-disciplinar` | Recurso em processo disciplinar militar |
| `mil-recurso-em-sentido-estrito` | Recurso em sentido estrito no CPPM |
| `mil-reintegracao-e-reforma` | Reintegração ao serviço militar e reforma |
| `mil-revisao-criminal` | Revisão criminal militar |

</details>

<details>
<summary><b>Eleitoral</b> — 7 skills</summary>

| Skill | Conteúdo |
| --- | --- |
| `eleitoral-aije` | Ação de investigação judicial eleitoral (AIJE) |
| `eleitoral-aime` | Ação de impugnação de mandato eletivo (AIME) |
| `eleitoral-defesa-abuso-de-poder` | Defesa em ação por abuso de poder |
| `eleitoral-impugnacao-registro-candidatura` | Registro de candidatura e AIRC |
| `eleitoral-prestacao-de-contas-campanha` | Prestação de contas de campanha |
| `eleitoral-recurso-eleitoral` | Recurso eleitoral |
| `eleitoral-representacao-propaganda-irregular` | Representação por propaganda irregular (art. 96) |

</details>

<details>
<summary><b>Internacional</b> — 6 skills</summary>

| Skill | Conteúdo |
| --- | --- |
| `intl-apostilamento-legalizacao` | Apostilamento e legalização de documentos |
| `intl-carta-rogatoria-exequatur` | Carta rogatória e exequatur |
| `intl-contrato-internacional` | Contrato internacional |
| `intl-cooperacao-auxilio-direto` | Cooperação jurídica internacional — auxílio direto |
| `intl-defesa-extradicao` | Defesa em processo de extradição (STF) |
| `intl-homologacao-sentenca-estrangeira` | Homologação de decisão estrangeira (STJ) |

</details>

<details>
<summary><b>Agrário</b> — 4 skills</summary>

| Skill | Conteúdo |
| --- | --- |
| `agrario-arrendamento-e-parceria-rural` | Arrendamento e parceria rural |
| `agrario-desapropriacao-reforma-agraria` | Desapropriação para reforma agrária — defesa do expropriado |
| `agrario-imovel-rural-no-inventario` | Imóvel rural no inventário |
| `agrario-regularizacao-fundiaria-rural` | Regularização fundiária rural e georreferenciamento |

</details>

<details>
<summary><b>Regulatório</b> — 6 skills</summary>

| Skill | Conteúdo |
| --- | --- |
| `reg-defesa-processo-sancionador-agencia` | Defesa em processo sancionador de agência reguladora |
| `reg-defesa-sancionador-ans` | Defesa no processo sancionador da ANS |
| `reg-manifestacao-consulta-audiencia-publica` | Manifestação em consulta e audiência pública regulatória |
| `reg-pedido-outorga-licenca-agencia` | Pedido de habilitação, licença ou outorga perante agência |
| `reg-programa-integridade-compliance` | Programa de integridade e parecer de compliance regulatório |
| `reg-recurso-multa-agencia` | Recurso contra multa de agência reguladora |

</details>

## Uso com o JuriBase

As skills orientam a conferir toda súmula, tema ou precedente antes de citá-lo. Com o conector JuriBase ativo no Claude, a skill `verificacao-de-citacoes` faz essa conferência automaticamente. Sem o conector, confira na fonte oficial do tribunal.

## Contribuir

Veja [CONTRIBUTING.md](CONTRIBUTING.md). Antes de abrir um pull request, rode:

```
python3 scripts/validar.py
```

## Licença

[MIT](LICENSE) © 2026 PreviusIA Serviço Digital Ltda.

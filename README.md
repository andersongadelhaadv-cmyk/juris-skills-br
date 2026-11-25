# juris-skills-br

Skills jurídicas brasileiras para o Claude: estrutura de peças, requisitos, prazos e fundamentos verificados, organizados por área do direito.

**152 skills em 11 plugins**, com conteúdo conferido até 25/11/2026. Normas foram conferidas nos dados abertos do Senado Federal e precedentes foram conferidos no JuriBase.

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
| `processo-civil` | 19 | Peças do processo civil: inicial, contestação, réplica, reconvenção, tutelas, recursos (inclusive REsp com relevância), execução e juizado especial. |
| `trabalhista` | 15 | Peças trabalhistas: reclamação, contestação, recursos (RO, RR, agravos), execução, cálculos e temas recorrentes. |
| `previdenciario` | 12 | RGPS e RPPS: requerimento e recurso administrativo, aposentadorias da EC 103, incapacidade, BPC/LOAS, pensão, revisão, TNU. |
| `penal` | 14 | Defesa penal: resposta à acusação, habeas corpus, prisão e cautelares, recursos, execução penal, ANPP, júri, Maria da Penha, dosimetria. |
| `tributario-fazenda` | 11 | Tributário e Fazenda Pública: mandado de segurança, anulatória, repetição de indébito, execução fiscal, CARF, reforma tributária, cumprimento contra a Fazenda. |
| `familia-sucessoes` | 11 | Família e sucessões: alimentos, execução de alimentos, divórcio, guarda, união estável, paternidade, inventário, testamento e planejamento. |
| `consumidor` | 9 | Consumidor: indenizatória, vício, negativação, plano de saúde, revisional bancária, superendividamento, transporte aéreo e defesa do fornecedor. |
| `administrativo-licitacoes` | 11 | Administrativo e licitações (Lei 14.133): mandado de segurança, impugnação e recurso, sanções, reequilíbrio, improbidade, PAD, concurso, responsabilidade do Estado. |
| `contratos` | 22 | Contratos: elaboração, revisão e parecer; prestação de serviços (inclusive PJ), compra e venda, locação comercial, franquia, software/SaaS, NDA, distribuição e representação; aditivo, distrato e notificação de descumprimento. |
| `imobiliario` | 22 | Imobiliário: despejo, renovatória e revisional; posse, imissão e embargos de terceiro; usucapião judicial e extrajudicial; adjudicação compulsória; compra e venda, distrato e SFH; condomínio; matrícula, retificação, REURB, loteamento e incorporação. |


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
<summary><b>Processo civil</b> — 19 skills</summary>

| Skill | Conteúdo |
| --- | --- |
| `civel-acao-monitoria` | Ação monitória (e embargos monitórios) |
| `civel-agravo-de-instrumento` | Agravo de instrumento |
| `civel-agravo-interno` | Agravo interno |
| `civel-alegacoes-finais` | Alegações finais cíveis (debates ou memoriais) |
| `civel-apelacao` | Apelação cível |
| `civel-contestacao` | Contestação cível |
| `civel-cumprimento-de-sentenca` | Cumprimento de sentença (cível) |
| `civel-embargos-a-execucao` | Embargos à execução (título extrajudicial) |
| `civel-embargos-de-declaracao` | Embargos de declaração (cível) |
| `civel-excecao-de-pre-executividade` | Exceção de pré-executividade |
| `civel-execucao-titulo-extrajudicial` | Execução de título extrajudicial |
| `civel-impugnacao-ao-cumprimento` | Impugnação ao cumprimento de sentença |
| `civel-juizado-especial` | Juizado Especial Cível (inicial, contestação, recurso inominado) |
| `civel-peticao-inicial` | Petição inicial cível (procedimento comum) |
| `civel-reconvencao` | Reconvenção |
| `civel-recurso-especial` | Recurso especial (cível) |
| `civel-recurso-extraordinario` | Recurso extraordinário (cível) |
| `civel-replica` | Réplica (manifestação sobre a contestação) |
| `civel-tutela-provisoria` | Tutela provisória (urgência e evidência) |

</details>

<details>
<summary><b>Trabalhista</b> — 15 skills</summary>

| Skill | Conteúdo |
| --- | --- |
| `trabalhista-acidente-e-doenca-ocupacional` | Acidente do trabalho e doença ocupacional |
| `trabalhista-acordo-extrajudicial` | Homologação de acordo extrajudicial |
| `trabalhista-agravo-de-instrumento` | Agravo de instrumento trabalhista |
| `trabalhista-agravo-de-peticao` | Agravo de petição |
| `trabalhista-contestacao` | Contestação trabalhista |
| `trabalhista-embargos-a-execucao` | Embargos à execução trabalhista |
| `trabalhista-embargos-de-declaracao` | Embargos de declaração trabalhistas |
| `trabalhista-impugnacao-de-calculos` | Impugnação aos cálculos de liquidação |
| `trabalhista-insalubridade-periculosidade` | Adicionais de insalubridade e periculosidade |
| `trabalhista-mandado-de-seguranca` | Mandado de segurança trabalhista |
| `trabalhista-reclamacao` | Reclamação trabalhista (petição inicial) |
| `trabalhista-recurso-de-revista` | Recurso de revista |
| `trabalhista-recurso-ordinario` | Recurso ordinário trabalhista |
| `trabalhista-rescisao-indireta` | Rescisão indireta |
| `trabalhista-vinculo-de-emprego` | Reconhecimento de vínculo de emprego |

</details>

<details>
<summary><b>Previdenciário</b> — 12 skills</summary>

| Skill | Conteúdo |
| --- | --- |
| `prev-acidentario` | Ação acidentária e auxílio-acidente |
| `prev-aposentadoria-especial` | Aposentadoria especial e conversão de tempo especial |
| `prev-beneficio-por-incapacidade` | Benefícios por incapacidade (temporária e permanente) |
| `prev-bpc-loas` | BPC/LOAS (pessoa com deficiência e pessoa idosa) |
| `prev-inicial-aposentadoria` | Petição inicial de aposentadoria (RGPS) |
| `prev-pedido-de-uniformizacao-tnu` | Pedido de uniformização (TRU/TNU) |
| `prev-pensao-por-morte` | Pensão por morte (RGPS) |
| `prev-recurso-crps` | Recurso ao CRPS (Juntas e Câmaras) |
| `prev-requerimento-administrativo` | Requerimento administrativo ao INSS |
| `prev-revisao-de-beneficio` | Revisão de benefício previdenciário |
| `prev-rpps-servidor` | RPPS da União: aposentadoria e abono de permanência |
| `prev-tempo-rural-e-segurado-especial` | Tempo rural e segurado especial |

</details>

<details>
<summary><b>Penal</b> — 14 skills</summary>

| Skill | Conteúdo |
| --- | --- |
| `penal-agravo-em-execucao` | Agravo em execução penal |
| `penal-alegacoes-finais` | Alegações finais (memoriais) da defesa |
| `penal-anpp` | Acordo de não persecução penal (ANPP) |
| `penal-apelacao-criminal` | Apelação criminal |
| `penal-dosimetria` | Dosimetria da pena |
| `penal-habeas-corpus` | Habeas corpus |
| `penal-liberdade-provisoria-e-relaxamento` | Liberdade provisória, relaxamento e revogação da preventiva |
| `penal-livramento-condicional` | Livramento condicional |
| `penal-maria-da-penha-medidas-protetivas` | Medidas protetivas da Lei Maria da Penha (ofendida e requerido) |
| `penal-plenario-do-juri` | Plenário do Tribunal do Júri — defesa |
| `penal-progressao-de-regime` | Progressão de regime |
| `penal-recurso-em-sentido-estrito` | Recurso em sentido estrito (RESE) |
| `penal-resposta-a-acusacao` | Resposta à acusação e defesa prévia |
| `penal-revisao-criminal` | Revisão criminal |

</details>

<details>
<summary><b>Tributário e Fazenda Pública</b> — 11 skills</summary>

| Skill | Conteúdo |
| --- | --- |
| `fazenda-contestacao-fazendaria` | Contestação da Fazenda Pública |
| `fazenda-cumprimento-contra-a-fazenda` | Cumprimento de sentença contra a Fazenda Pública |
| `fazenda-execucao-fiscal-inicial` | Petição inicial de execução fiscal (lado da Fazenda) |
| `trib-acao-anulatoria` | Ação anulatória de débito fiscal |
| `trib-defesa-administrativa-e-carf` | Defesa administrativa tributária e recurso ao CARF |
| `trib-embargos-a-execucao-fiscal` | Embargos à execução fiscal |
| `trib-excecao-pre-executividade-fiscal` | Exceção de pré-executividade em execução fiscal |
| `trib-mandado-de-seguranca` | Mandado de segurança tributário |
| `trib-prescricao-intercorrente` | Prescrição intercorrente, prescrição e decadência tributária |
| `trib-reforma-tributaria-ibs-cbs` | Parecer sobre a reforma tributária do consumo (IBS, CBS e IS) |
| `trib-repeticao-de-indebito` | Ação de repetição de indébito tributário |

</details>

<details>
<summary><b>Família e sucessões</b> — 11 skills</summary>

| Skill | Conteúdo |
| --- | --- |
| `familia-acao-de-alimentos` | Ação de alimentos (inicial) |
| `familia-divorcio` | Divórcio (litigioso, consensual judicial e extrajudicial) |
| `familia-execucao-de-alimentos` | Execução / cumprimento de sentença de alimentos |
| `familia-guarda-e-convivencia` | Guarda e convivência |
| `familia-investigacao-de-paternidade` | Investigação de paternidade |
| `familia-revisional-e-exoneracao-de-alimentos` | Revisional e exoneração de alimentos |
| `familia-uniao-estavel` | União estável: reconhecimento e dissolução |
| `sucessoes-inventario-extrajudicial` | Inventário extrajudicial (escritura pública) |
| `sucessoes-inventario-judicial` | Inventário judicial |
| `sucessoes-planejamento-e-partilha-em-vida` | Planejamento sucessório e partilha em vida (consultivo) |
| `sucessoes-testamento` | Testamento: elaboração e cumprimento |

</details>

<details>
<summary><b>Consumidor</b> — 9 skills</summary>

| Skill | Conteúdo |
| --- | --- |
| `consumidor-acao-indenizatoria` | Ação indenizatória de consumo (fato do produto ou do serviço) |
| `consumidor-contratos-bancarios-revisional` | Revisional de contrato bancário (consumo) |
| `consumidor-defesa-do-fornecedor` | Contestação do fornecedor em ação de consumo |
| `consumidor-negativacao-indevida` | Negativação indevida |
| `consumidor-plano-de-saude` | Plano de saúde — negativa de cobertura com tutela de urgência |
| `consumidor-repeticao-em-dobro` | Repetição do indébito em dobro (CDC art. 42, p.ú.) |
| `consumidor-superendividamento` | Superendividamento — repactuação de dívidas |
| `consumidor-transporte-aereo` | Transporte aéreo de passageiros |
| `consumidor-vicio-do-produto-ou-servico` | Vício do produto ou do serviço |

</details>

<details>
<summary><b>Administrativo e licitações</b> — 11 skills</summary>

| Skill | Conteúdo |
| --- | --- |
| `adm-acao-popular` | Ação popular (Lei 4.717/1965) |
| `adm-concurso-publico` | Concurso público — nomeação e controle de atos da banca |
| `adm-defesa-em-improbidade` | Defesa em ação de improbidade administrativa |
| `adm-defesa-em-pad` | Defesa em processo administrativo disciplinar (Lei 8.112/1990) |
| `adm-defesa-em-processo-sancionador-licitacao` | Defesa em processo sancionador de licitações e contratos |
| `adm-desapropriacao-defesa` | Defesa do expropriado (Decreto-Lei 3.365/1941) |
| `adm-impugnacao-ao-edital` | Impugnação ao edital (Lei 14.133/2021, art. 164) |
| `adm-mandado-de-seguranca` | Mandado de segurança (Lei 12.016/2009) |
| `adm-pedido-de-reequilibrio-economico-financeiro` | Pedido de reequilíbrio econômico-financeiro |
| `adm-recurso-em-licitacao` | Recurso em licitação (Lei 14.133/2021, arts. 165 a 168) |
| `adm-responsabilidade-civil-do-estado` | Responsabilidade civil do Estado (CF art. 37, § 6º) |

</details>

<details>
<summary><b>Contratos</b> — 22 skills</summary>

| Skill | Conteúdo |
| --- | --- |
| `contratos-elaboracao-de-contrato` | Elaboração de contrato (roteiro geral) |
| `contratos-analise-e-revisao-de-contrato` | Análise e revisão de contrato |
| `contratos-parecer-sobre-contrato` | Parecer sobre contrato |
| `contratos-prestacao-de-servicos` | Contrato de prestação de serviços |
| `contratos-prestacao-de-servicos-pj` | Prestação de serviços por pessoa jurídica (mitigação de vínculo) |
| `contratos-compra-e-venda-empresarial` | Compra e venda empresarial |
| `contratos-locacao-comercial` | Locação comercial (não residencial) |
| `contratos-franquia-e-cof` | Franquia e Circular de Oferta de Franquia |
| `contratos-licenca-de-software-e-saas` | Licença de software e SaaS |
| `contratos-nda-confidencialidade` | Acordo de confidencialidade (NDA) |
| `contratos-agencia-e-distribuicao` | Agência e distribuição |
| `contratos-representacao-comercial` | Representação comercial autônoma |
| `contratos-parceria-e-joint-venture` | Parceria empresarial, consórcio e joint venture |
| `contratos-comodato` | Comodato |
| `contratos-cessao-de-direitos` | Cessão de crédito, de posição contratual e de direitos |
| `contratos-clausula-penal` | Cláusula penal |
| `contratos-memorando-de-entendimentos` | Memorando de entendimentos / carta de intenções |
| `contratos-aditivo-contratual` | Termo aditivo contratual |
| `contratos-distrato-e-rescisao` | Distrato e rescisão de contrato |
| `contratos-notificacao-de-descumprimento` | Notificação de descumprimento contratual |
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
| `imob-locacao-residencial` | Contrato de locação residencial |
| `imob-cobranca-de-taxas-condominiais` | Cobrança de taxas condominiais |
| `imob-prestacao-de-contas-de-condominio` | Prestação de contas de condomínio |
| `imob-reintegracao-de-posse` | Possessórias — reintegração, manutenção e interdito proibitório |
| `imob-imissao-na-posse` | Imissão na posse |
| `imob-embargos-de-terceiro` | Embargos de terceiro (imóvel) |
| `imob-usucapiao-judicial` | Usucapião judicial de imóvel |
| `imob-usucapiao-extrajudicial` | Usucapião extrajudicial (art. 216-A da Lei 6.015/1973) |
| `imob-adjudicacao-compulsoria` | Adjudicação compulsória (judicial e extrajudicial) |
| `imob-compra-e-venda-de-imovel` | Compra e venda de imóvel |
| `imob-distrato-imobiliario` | Distrato de promessa de compra e venda na planta |
| `imob-revisao-de-financiamento-sfh` | Revisão de financiamento habitacional (SFH/SFI) e FGTS |
| `imob-analise-de-matricula-e-due-diligence` | Análise de matrícula e due diligence |
| `imob-parecer-juridico-imobiliario` | Parecer jurídico imobiliário |
| `imob-notificacao-extrajudicial-imobiliaria` | Notificação extrajudicial imobiliária |
| `imob-retificacao-de-area` | Retificação de registro e de área |
| `imob-regularizacao-fundiaria-reurb` | Regularização fundiária (Reurb-S e Reurb-E) |
| `imob-loteamento-irregular-defesa-do-adquirente` | Loteamento irregular — defesa do adquirente |
| `imob-incorporacao-imobiliaria` | Incorporação imobiliária — registro e compliance |

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

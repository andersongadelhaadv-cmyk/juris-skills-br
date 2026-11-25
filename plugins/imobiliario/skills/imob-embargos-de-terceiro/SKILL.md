---
name: imob-embargos-de-terceiro
description: >
  Redige embargos de terceiro contra penhora, arresto, indisponibilidade ou
  outra constrição judicial sobre imóvel de quem não é parte no processo (CPC
  arts. 674 a 681), inclusive do promitente comprador sem registro (Súmula
  84/STJ) e do cônjuge na defesa da meação (Súmula 134/STJ). Use quando o
  usuário pedir para livrar imóvel penhorado em execução alheia, defender
  comprador de boa-fé acusado de fraude à execução, contar o prazo dos
  embargos de terceiro ou atribuir os honorários a quem deu causa à constrição.
metadata:
  area: imobiliario
  tipo_peca: inicial
  verificado_em: 2026-11-25
---
# Embargos de terceiro (imóvel)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: quem **não é parte** no processo sofre ou está ameaçado de constrição sobre imóvel que possui ou sobre o qual tem direito incompatível com o ato (art. 674 do CPC): proprietário, inclusive fiduciário, ou possuidor (§ 1º); cônjuge/companheiro (§ 2º, I); adquirente atingido por fraude à execução (§ 2º, II); atingido por desconsideração da personalidade sem ter sido parte no incidente (§ 2º, III); credor com garantia real não intimado (§ 2º, IV).
- Não usar:
  - o próprio **executado** se defende por embargos à execução ou impugnação: `civel-embargos-a-execucao`, `civel-impugnacao-ao-cumprimento`; matéria de ordem pública sem dilação: `civel-excecao-de-pre-executividade`;
  - execução fiscal contra o devedor: `trib-embargos-a-execucao-fiscal` (o terceiro continua usando embargos de terceiro);
  - esbulho sem ordem judicial: `imob-reintegracao-de-posse`;
  - promitente comprador que quer a escritura: `imob-adjudicacao-compulsoria`.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Número do processo de origem, juízo, partes e o ato constritivo (penhora, arresto, indisponibilidade), com a data.
2. Matrícula atualizada (penhora averbada? quando?).
3. Título do embargante: escritura, promessa (registrada ou não), cessão, partilha, posse sem título — com datas.
4. Prova da posse: contas, IPTU, condomínio, fotos, testemunhas, contrato de financiamento.
5. Quando o embargante **soube** da constrição e como (intimação pessoal, edital, oficial no imóvel, carta de arrematação).
6. Fase do processo de origem: conhecimento, execução, já houve adjudicação/alienação/arrematação? A carta foi assinada?
7. Na alegação de fraude à execução: data da aquisição x data da citação/averbação da penhora; certidões obtidas na compra.
8. Cônjuge: regime de bens e se a dívida reverteu em benefício da família.

## Prazo e contagem
- Fase de conhecimento: a qualquer tempo enquanto não transitada em julgado a sentença (art. 675).
- Execução/cumprimento: até **5 dias depois** da adjudicação, alienação por iniciativa particular ou arrematação, **sempre antes da assinatura da carta** (art. 675).
- Terceiro **sem ciência** da execução: o prazo corre da efetiva turbação ou esbulho; a ciência que deflagra o prazo deve ser inequívoca, direta e pessoal — editais e atos genéricos de publicidade não bastam (STJ, REsp 2.167.032). A data da intimação da penhora não serve de termo inicial (STJ, REsp 2.075.570).
- Adquirente intimado na forma do art. 792, § 4º: o decurso dos 15 dias ali previstos não impede os embargos de terceiro repressivos, respeitado o art. 675 (STJ, AREsp 2.163.176) [VERIFICAR: texto do art. 792, § 4º, conferido só pela ementa].
- Contagem em dias úteis e demais prazos: `prazos-processuais`.

## Estrutura da peça
Distribuição por dependência ao juízo da constrição (art. 676) → qualidade de terceiro → posse/domínio → ilegitimidade da constrição → liminar (art. 678) → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Petição com **prova sumária** da posse ou do domínio e da qualidade de terceiro, documentos e rol de testemunhas (art. 677); a posse pode ser provada em audiência preliminar (§ 1º).
- **Polo passivo**: quem se beneficia da constrição; e também o adversário dele no processo principal, se foi quem indicou o bem (art. 677, § 4º). Citação pessoal se o embargado não tiver procurador nos autos (§ 3º).
- Promitente comprador **sem registro** é legitimado se tiver posse (Súmula 84/STJ).
- Fraude à execução: sem averbação da penhora, cabe ao credor provar a má-fé do adquirente (Súmula 375/STJ).
- Cônjuge intimado da penhora ainda pode embargar para defender a meação (Súmula 134/STJ), ressalvado o art. 843.
- Contra credor com garantia real, o embargado só alega as matérias do art. 680.

## Fundamentos verificados
- CPC arts. 674 a 681.
- Súmulas 84, 134, 303 e 375 do STJ.
- STJ: REsp 2.167.032; REsp 2.075.570; AREsp 2.163.176.
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Liminar (art. 678): suspensão das medidas constritivas sobre o imóvel e, se pedido, manutenção ou reintegração provisória da posse; caução pode ser exigida, salvo hipossuficiência (parágrafo único).
- Audiência preliminar para prova da posse, se a documental for insuficiente (art. 677, § 1º).
- Procedência: cancelamento da constrição e reconhecimento do domínio, da manutenção ou da reintegração definitiva (art. 681); ofício ao registro para cancelar a averbação.
- Honorários contra quem deu causa à constrição indevida (Súmula 303/STJ) — se o embargante não registrou o título, avalie o risco de arcar com eles.
- Juros e correção sobre eventuais verbas: `juros-e-correcao`.

## Checklist pré-protocolo
- [ ] Tempestividade demonstrada com a data e o modo da ciência
- [ ] Carta de arrematação/adjudicação ainda não assinada (ou tese da ciência inequívoca)
- [ ] Distribuição por dependência ao juízo que ordenou a constrição
- [ ] Prova sumária de posse/domínio e de não ser parte
- [ ] Polo passivo conforme art. 677, § 4º
- [ ] Súmula 375 e certidões da compra (fraude à execução)
- [ ] Pedido liminar do art. 678 e ofício ao registro
- [ ] Honorários: quem deu causa (Súmula 303)

## Erros a evitar
- Contar o prazo da intimação da penhora ou do edital de leilão para quem nunca teve ciência pessoal.
- Distribuir livremente, fora do juízo da constrição.
- Deixar de incluir o executado quando foi ele quem indicou o bem.
- Embargar como terceiro sendo parte (executado, ou sócio já citado no incidente de desconsideração).
- Esquecer que, sem registro do título, o credor pode alegar que o embargante deu causa à penhora (Súmula 303).

## Integração com o núcleo
`prazos-processuais`, `juros-e-correcao`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`, `civel-tutela-provisoria`.

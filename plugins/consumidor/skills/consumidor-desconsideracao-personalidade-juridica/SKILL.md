---
name: consumidor-desconsideracao-personalidade-juridica
description: >
  Redige o pedido (incidente ou requerimento na inicial) de desconsideração da
  personalidade jurídica do fornecedor em relação de consumo, pela teoria menor
  do art. 28, § 5º, do CDC (insolvência e obstáculo ao ressarcimento), com as
  hipóteses do caput, a responsabilidade de grupos e consorciadas (§§ 2º a 4º) e
  o rito dos arts. 133 a 137 do CPC — e a defesa do sócio. Use quando o usuário
  pedir para atingir bens dos sócios de empresa que não paga condenação de
  consumo, incidente de desconsideração em cumprimento de sentença, incluir
  empresa do grupo, ou defender sócio/administrador incluído no polo passivo.
metadata:
  area: consumidor
  tipo_peca: requerimento
  verificado_em: 2026-11-25
---
# Desconsideração da personalidade jurídica no CDC (art. 28)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: crédito de consumidor (indenização, restituição, multa) contra pessoa jurídica fornecedora sem patrimônio suficiente, em conhecimento, cumprimento de sentença ou execução.
- Usar também do lado do sócio/administrador citado no incidente (manifestação do art. 135 do CPC).
- Não usar: relação civil ou empresarial sem consumo — aplica-se o art. 50 do CC (teoria maior; STJ, Tema 1210): ver `civel-cumprimento-de-sentenca` e `civel-embargos-a-execucao`.
- Execução fiscal ou crédito tributário: `trib-*`. Crédito trabalhista: `trabalhista-agravo-de-peticao`.
- Fraude de bens já alienados: tratar também a fraude à execução (CPC art. 137) com a skill de cumprimento.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Título (sentença, acordo, contrato) e natureza consumerista da relação.
2. Diligências patrimoniais frustradas contra a PJ (bloqueios, pesquisa de bens, certidões) e situação cadastral (ativa, inapta, baixada, em recuperação ou falência).
3. Quadro societário atual e histórico (ficha da Junta), com indicação de quem exerce gestão.
4. Indícios de abuso, se houver (confusão patrimonial, encerramento irregular, sucessão empresarial, transferência de bens) — reforçam, mas não são exigidos pela teoria menor.
5. Empresas do mesmo grupo, controladas, consorciadas ou coligadas, com prova do vínculo.
6. Fase processual e se a desconsideração será pedida na inicial ou em incidente.

## Prazo e contagem
- Não há prazo próprio para pedir a desconsideração; atenção à prescrição da pretensão executória e à intercorrente [VERIFICAR: prazo aplicável no caso via `verificacao-de-citacoes`].
- Sócio citado no incidente: 15 dias para manifestação e provas (CPC art. 135).
- Instauração suspende o processo, salvo pedido na inicial (CPC art. 134, § 3º).
- Prazos processuais: `prazos-processuais`.

## Estrutura da peça
Cabimento (relação de consumo) → fundamento legal (art. 28 caput e/ou § 5º) → requisitos concretos (insolvência + obstáculo; ou hipótese do caput) → delimitação subjetiva (quem geriu; grupo) → pedido de instauração, citação e tutela cautelar → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Teoria menor (art. 28, § 5º): basta demonstrar a insolvência do fornecedor e que a personalidade jurídica é obstáculo ao ressarcimento (REsp 1.900.843); dispensa prova de fraude, abuso ou confusão patrimonial.
- Limite subjetivo: sócio sem poder de gestão não é atingido, salvo prova de que contribuiu ao menos culposamente para o ilícito (AgInt no AREsp 2.783.789; REsp 1.900.843).
- Sociedade anônima: a teoria menor pode alcançar o acionista controlador (REsp 2.034.442).
- Grupo e controladas respondem subsidiariamente; consorciadas, solidariamente; coligadas, só por culpa (art. 28, §§ 2º a 4º).
- Rito obrigatório: incidente (CPC arts. 133 a 137) ou pedido na inicial com citação do sócio (art. 134, § 2º); o requerimento deve demonstrar os pressupostos legais (art. 134, § 4º).
- Recuperação judicial da devedora não impede, por si, atos contra os sócios desconsiderados (REsp 2.034.442).

## Fundamentos verificados
- CDC art. 28, caput e §§ 2º a 5º; art. 6º, VIII.
- CPC arts. 133 a 137. CC art. 50 (contraste — teoria maior).
- STJ, Tema 1210 (REsp 1.873.187): teoria maior nas relações civis e empresariais — delimita, por contraste, o campo do CDC.
- STJ: REsp 1.900.843; AgInt no AREsp 2.783.789; REsp 2.034.442.
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Instauração do incidente, comunicação ao distribuidor (art. 134, § 1º) e citação dos sócios/empresas para manifestação em 15 dias.
- Tutela cautelar de indisponibilidade de bens dos requeridos, demonstrados os requisitos de urgência.
- Acolhimento para incluir os requeridos no polo passivo, com responsabilidade patrimonial pelo débito (indicar solidária ou subsidiária, conforme o § aplicado).
- Declaração de ineficácia de alienações em fraude à execução, se houver (art. 137).
- Juros e correção do débito pelo núcleo `juros-e-correcao`.

## Checklist pré-protocolo
- [ ] Relação de consumo demonstrada (senão, art. 50 do CC e Tema 1210)
- [ ] Prova da insolvência/obstáculo: diligências frustradas documentadas
- [ ] Ficha da Junta com gestão de cada sócio indicado
- [ ] Vínculo de grupo/consórcio provado, se incluir outras empresas
- [ ] Rito escolhido (incidente x inicial) e pedido de citação
- [ ] Recurso contra a decisão do incidente mapeado (`civel-agravo-de-instrumento`; agravo interno se do relator — art. 136, p.u.)
- [ ] Juros/correção remetidos ao núcleo

## Erros a evitar
- Citar o Tema 1210 como se valesse para consumo: ele restringe às relações civis e empresariais.
- Incluir todos os sócios indistintamente: sócio minoritário sem gestão tende a ser excluído.
- Pedir desconsideração sem esgotar minimamente a busca de bens da PJ (fragiliza o "obstáculo").
- Pular o incidente e pedir penhora direta em bens do sócio.
- Do lado da defesa: discutir só ausência de fraude, quando a teoria menor dispensa fraude — atacar a relação de consumo, a solvência e a ausência de gestão.

## Integração com o núcleo
`juros-e-correcao`, `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

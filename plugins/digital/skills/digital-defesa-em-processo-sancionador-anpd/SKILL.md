---
name: digital-defesa-em-processo-sancionador-anpd
description: >
  Redige defesa, alegações finais e recurso em processo administrativo
  sancionador da ANPD por infração à LGPD, inclusive impugnação do auto de
  infração, com base nos arts. 52 a 54 e 55-J da Lei 13.709/2018, no
  Regulamento do Processo de Fiscalização e do Processo Administrativo
  Sancionador (Resolução CD/ANPD nº 1/2021) e no Regulamento de Dosimetria
  (Resolução CD/ANPD nº 4/2023). Use quando o usuário pedir defesa contra auto
  de infração da ANPD, recurso ao Conselho Diretor, redução de multa da LGPD,
  discussão de dosimetria, atenuantes, proposta de TAC ou nulidade do processo
  sancionador de proteção de dados.
metadata:
  area: digital
  tipo_peca: contestacao
  verificado_em: 2026-11-25
---
# Defesa em processo sancionador da ANPD

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: (a) defesa após intimação do auto de infração; (b) alegações finais quando houver prova nova; (c) recurso contra decisão de primeira instância; (d) proposta de termo de ajustamento de conduta (TAC); (e) pedido de reconsideração/efeito suspensivo.
- Não usar: diagnóstico de adequação de um produto à LGPD sem processo instaurado (skill `lgpd-saas-adequacao`, se disponível); ação judicial anulatória da sanção depois de esgotada a via administrativa (`adm-mandado-de-seguranca` ou `civel-peticao-inicial`); ação indenizatória de titular por vazamento (`consumidor-acao-indenizatoria`); defesa em PAD de servidor (`adm-defesa-em-pad`).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Auto de infração completo: conduta imputada, fatos, dispositivo legal ou regulamentar indicado, data da ciência oficial.
2. Histórico anterior: procedimento preparatório, medidas de orientação, preventivas ou corretivas impostas e se foram cumpridas (pesam como agravante se descumpridas).
3. Porte e faturamento do autuado no último exercício, por ramo de atividade; enquadramento como agente de pequeno porte.
4. Volume e natureza dos dados (sensíveis, de crianças/adolescentes/idosos), número de titulares, duração do tratamento.
5. Base legal invocada para o tratamento e documentos que a comprovam (registro das operações, relatório de impacto, contratos com operadores).
6. Medidas adotadas e datas: cessação da conduta, comunicação de incidente, mitigação aos titulares, política de governança, encarregado nomeado.
7. Processos sancionadores anteriores (reincidência específica ou genérica).

## Prazo e contagem
- Prazos do processo sancionador contados em **dias úteis** a partir da ciência oficial, prorrogando-se para o primeiro dia útil se vencerem sem expediente (Res. CD/ANPD nº 1/2021, art. 8º).
- Defesa: 10 dias úteis da intimação do auto (art. 47). Alegações finais: 10 dias úteis, facultadas quando há prova nova após a defesa (art. 53). Recurso: 10 dias úteis da intimação da decisão (art. 58).
- Multa: pagamento em até 20 dias úteis da ciência da decisão, em dobro para agente de pequeno porte (Res. CD/ANPD nº 4/2023, art. 17); renúncia expressa ao recurso com pagamento no prazo dá redução de 25% (art. 18).
- Prescrição da ação punitiva: tese do art. 1º da Lei 9.873/1999 (5 anos; 3 anos de paralisação) — aplicação à ANPD não conferida em precedente [VERIFICAR].
- Confirme o texto vigente dos regulamentos no gov.br/anpd antes do protocolo: a ANPD foi transformada em agência pela Lei 15.352/2026 e a Res. nº 4/2023 está em revisão na agenda regulatória [VERIFICAR: unidade competente e redação atual].
- Prazos processuais judiciais, se o caso for à Justiça: `prazos-processuais`.

## Estrutura da peça
Endereçamento → tempestividade → síntese do auto → preliminares (nulidade do auto, cerceamento, prescrição) → mérito (atipicidade, base legal válida, ausência de dano) → subsidiário: reclassificação da infração e dosimetria → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Auto de infração**: deve identificar o autuado, descrever a conduta e os fatos e indicar o dispositivo violado (Res. nº 1/2021, arts. 46 e 47). Descrição genérica que impede a defesa é nulidade a arguir na primeira oportunidade.
- **Devido processo**: sanção só após procedimento com ampla defesa (LGPD art. 52 § 1º; art. 55-J, IV; Res. nº 4/2023, art. 4º). Lei 9.784/1999 aplica-se subsidiariamente (art. 69), com dever de motivação (art. 50).
- **Ônus da prova**: o autuado prova o que alega (Res. nº 1/2021, art. 50) e também o cumprimento das atenuantes (Res. nº 4/2023, art. 13 § 3º). Junte documentos datados.
- **Gradação legal**: suspensão do banco de dados, suspensão da atividade e proibição de tratamento só após ao menos uma sanção dos incisos II a VI no mesmo caso (LGPD art. 52 § 6º).
- **Efeito suspensivo** do recurso limita-se à matéria contestada, salvo receio de prejuízo de difícil reparação (Res. nº 1/2021, art. 60) — impugne tudo que quiser suspender.

## Fundamentos verificados
- LGPD arts. 52 (sanções e critérios), 53 (metodologia por regulamento), 54 (multa diária fundamentada), 55-A (natureza da ANPD) e 55-J, IV (competência sancionadora com contraditório e recurso).
- Res. CD/ANPD nº 4/2023: classificação leve/média/grave (art. 8º), advertência (art. 9º), multa simples (arts. 10 e 11), agravantes (art. 12), atenuantes (art. 13), piso e teto (art. 15), afastamento da metodologia (art. 27).
- Res. CD/ANPD nº 1/2021: auto de infração, defesa, instrução, decisão, recurso, TAC (arts. 43, 46-47, 50, 53, 58, 60).
- Lei 9.784/1999 arts. 2º, 50 e 69; Lei 9.873/1999 art. 1º.
- Jurisprudência específica sobre sanção da ANPD: sem resultado no JuriBase em 25/11/2026 [VERIFICAR antes de citar qualquer julgado].
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Nulidade do auto (descrição deficiente, capitulação errada, cerceamento) e arquivamento.
- Reconhecimento da prescrição, se for o caso.
- Improcedência por atipicidade ou existência de base legal.
- Subsidiariamente: reclassificação para leve ou média; advertência em vez de multa (art. 9º); aplicação de cada atenuante com prova e percentual; exclusão de agravantes não comprovadas; observância do teto de 2% do faturamento do ramo e de R$ 50 milhões por infração.
- Produção de provas (documental, pericial, testemunhal), com justificativa de pertinência.
- No recurso: efeito suspensivo; reconsideração pela primeira instância.
- Encargos de mora e atualização de multa paga e restituída: pelo núcleo `juros-e-correcao`.

## Checklist pré-protocolo
- [ ] Data da ciência oficial e prazo em dias úteis conferidos
- [ ] Texto vigente dos regulamentos conferido no gov.br/anpd
- [ ] Cada fato do auto rebatido ou admitido com estratégia
- [ ] Faturamento por ramo documentado (evita arbitramento pela ANPD)
- [ ] Atenuantes provadas com documento e data anterior ao marco processual correspondente
- [ ] Classificação leve/média/grave enfrentada critério a critério
- [ ] Avaliado: TAC, renúncia ao recurso com 25% de redução, ou recurso
- [ ] Procuração e atos constitutivos juntados

## Erros a evitar
- Cessar a conduta só depois da decisão: a atenuante de cessação cai de 75% para 30% conforme o momento, e não conta se decorre de mero cumprimento de ordem (Res. nº 4/2023, art. 13, I e § 1º).
- Deixar o faturamento sem prova idônea: a ANPD pode defini-lo, inclusive pelo faturamento total do grupo (LGPD art. 52 § 4º; Res. nº 4/2023, art. 11 § 3º).
- Recorrer genericamente: o efeito suspensivo alcança só a matéria impugnada.
- Tratar obstrução à fiscalização como questão menor: por si só torna a infração grave (Res. nº 4/2023, art. 8º § 3º, II).
- Citar decisões da ANPD ou julgados sem conferir a fonte.

## Integração com o núcleo
`prazos-processuais`, `juros-e-correcao`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

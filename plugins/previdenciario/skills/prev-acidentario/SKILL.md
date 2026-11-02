---
name: prev-acidentario
description: >
  Prepara a ação acidentária contra o INSS na Justiça Estadual (CF, art. 109, I;
  Lei 8.213/1991, arts. 19 a 22, 86 e 129), com demonstração de nexo causal ou
  epidemiológico e pedido de auxílio-acidente, auxílio por incapacidade ou
  aposentadoria acidentários. Use quando o usuário pedir ação acidentária,
  auxílio-acidente, benefício B91/B94, doença ocupacional, CAT, NTEP, sequela de
  acidente de trabalho ou acidente de trajeto.
metadata:
  area: previdenciario
  tipo_peca: inicial
  verificado_em: 2026-11-01
---
# Ação acidentária e auxílio-acidente

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: benefício decorrente de acidente do trabalho, doença profissional ou do trabalho (inclusive equiparados do art. 21); conversão de benefício comum (B31) em acidentário (B91); auxílio-acidente por sequela que reduza a capacidade.
- Auxílio-acidente por acidente de qualquer natureza (sem relação com o trabalho): benefício previdenciário comum, de competência federal, pois a exceção do CF, art. 109, I, alcança só as causas de acidente de trabalho. Definir pelos fatos (CAT, nexo, NTEP) se o caso é acidentário antes de escolher a Justiça.
- Pensão por morte de segurado vítima de acidente do trabalho: competência da Justiça Federal (STJ, CC 197.182); ver `prev-pensao-por-morte`.
- Indenização contra o empregador: Justiça do Trabalho (outra área).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Descrição do acidente ou da doença, data, local, atividade no momento.
2. CAT emitida (por quem e quando) ou recusa do empregador.
3. Documentos médicos, afastamentos, benefícios recebidos (espécie, DIB, DCB).
4. Atividade habitual e sequelas atuais.
5. CNAE do empregador e CID (para NTEP, art. 21-A).
6. Requerimento/decisão do INSS.

## Prazo e contagem
- Sem decadência para a concessão; prescrição quinquenal das parcelas.
- Auxílio-acidente é devido a partir do dia seguinte à cessação do auxílio por incapacidade (art. 86, §2º).
- Prazos processuais em dias úteis (CPC, art. 219); o INSS tem prazo em dobro na Justiça Estadual (CPC, art. 183).

## Estrutura da peça   (detalhe em [estrutura](references/estrutura.md))
1. Competência da Justiça Estadual.
2. Qualidade de segurado (empregado, doméstico, avulso, segurado especial — art. 19).
3. Fato acidentário e nexo (causal, concausal ou NTEP).
4. Incapacidade ou redução da capacidade.
5. Benefício cabível e DIB.
6. Perícia e quesitos.
7. Pedidos; isenção de custas (art. 129, p.ú.).

## Requisitos e preliminares
- Competência: Justiça Estadual (CF, art. 109, I, exclui acidentes de trabalho da Justiça Federal; STJ Súmula 15; STF Súmula 501). Juntar prova de notificação do evento ao INSS (CAT) (art. 129, II).
- Segurados cobertos: empregado, doméstico, avulso e segurado especial (art. 19); só eles recebem auxílio-acidente (art. 18, §1º: incisos I, II, VI e VII do art. 11). Contribuinte individual e facultativo não têm direito ao auxílio-acidente.
- Nexo: doença profissional ou do trabalho (art. 20), concausa e equiparações (art. 21), NTEP (art. 21-A). Não são doença do trabalho: degenerativa, inerente ao grupo etário, sem incapacidade e endêmica (art. 20, §1º), salvo prova de relação com o trabalho.
- Auxílio-acidente (art. 86): sequela consolidada que reduza a capacidade para o trabalho habitual; 50% do salário de benefício; não acumula com aposentadoria (§2º; STJ Súmula 507 para benefícios anteriores a 11/11/1997). Perda auditiva exige nexo e redução da capacidade (§4º); grau mínimo regulamentar não exclui o benefício (STJ Súmula 44). STJ Tema 416: basta lesão que implique redução da capacidade para o labor habitual.
- Sem carência (art. 26, I e II).

## Fundamentos verificados   (detalhe em [fundamentos](references/fundamentos.md))
- CF, art. 109, I; Lei 8.213, arts. 19, 20, 21, 21-A, 22, 26, 86, 129.
- STJ Súmulas 15, 44 e 507; STF Súmula 501; STJ Tema 416.

## Pedidos e requerimentos
- Reconhecimento da natureza acidentária e conversão do benefício (B31 em B91), com os efeitos próprios.
- Concessão de auxílio-acidente desde o dia seguinte à cessação do auxílio por incapacidade.
- Subsidiariamente, auxílio por incapacidade temporária ou aposentadoria por incapacidade permanente acidentários (100% da média, EC 103, art. 26, §3º, II).
- Perícia médica com especialista e vistoria do local, se útil.
- Atrasados conforme `juros-e-correcao`.

## Checklist pré-protocolo
- [ ] CAT (ou prova da comunicação substitutiva, art. 22, §2º) anexada.
- [ ] Categoria do segurado coberta pelo benefício acidentário.
- [ ] Nexo descrito (mecânica do acidente ou exposição ocupacional) e NTEP verificado.
- [ ] Sequela consolidada e atividade habitual descritas.
- [ ] Ação proposta na Justiça Estadual.
- [ ] Juros e correção remetidos ao núcleo.

## Erros a evitar
- Propor na Justiça Federal ação de benefício acidentário.
- Pedir auxílio-acidente cumulado com aposentadoria concedida após 11/11/1997.
- Confundir incapacidade (auxílio por incapacidade) com redução da capacidade (auxílio-acidente).
- Ignorar o pedido de conversão B31→B91 (efeitos na estabilidade e no FGTS são trabalhistas; aqui, foco no benefício).

## Integração com o núcleo
- `juros-e-correcao`; `prazos-processuais`; `verificacao-de-citacoes`; `fidelidade-factual`; `estilo-forense`.

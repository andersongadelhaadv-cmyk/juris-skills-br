---
name: prev-auxilio-acidente-previdenciario
description: >
  Prepara a ação de auxílio-acidente previdenciário (acidente de qualquer
  natureza, sem relação com o trabalho) contra o INSS na Justiça Federal (Lei
  8.213/1991, arts. 18, §1º, 26, I, e 86), com foco na sequela consolidada que
  reduz a capacidade para o trabalho habitual, na DIB após a cessação do
  auxílio-doença e na vedação de cumular com aposentadoria. Use quando o usuário
  pedir auxílio-acidente por acidente de trânsito, queda, fratura ou lesão
  doméstica ou esportiva, sequela após alta do INSS, B36 negado ou auxílio-acidente
  de empregado, doméstico, avulso ou segurado especial fora do trabalho.
metadata:
  area: previdenciario
  tipo_peca: inicial
  verificado_em: 2026-11-25
---
# Auxílio-acidente previdenciário (acidente de qualquer natureza)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: sequela de acidente sem relação com o trabalho (trânsito fora do trajeto, queda em casa, esporte, agressão) que reduz a capacidade para a atividade habitual, em segurado empregado, doméstico, avulso ou segurado especial.
- Acidente do trabalho, doença ocupacional, acidente de trajeto, perda auditiva ligada ao trabalho ou conversão B31→B91: `prev-acidentario` (Justiça Estadual, CF, art. 109, I).
- Incapacidade total, temporária ou permanente (não só redução): `prev-beneficio-por-incapacidade`.
- Indenização contra o causador do acidente: `civel-*` (responsabilidade civil); o auxílio-acidente não a exclui.
- Contribuinte individual (inclusive MEI) e facultativo: não têm direito ao auxílio-acidente (art. 18, §1º). Não ajuizar.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Descrição do acidente, data, local e por que não tem relação com o trabalho (boletim de ocorrência, prontuário de atendimento).
2. Categoria de segurado na data do acidente (CNIS/CTPS) — precisa ser empregado, doméstico, avulso ou segurado especial.
3. Benefícios recebidos: auxílio por incapacidade (NB, DIB, DCB) e se houve pedido de prorrogação.
4. Atividade habitual na data do acidente, com tarefas concretas.
5. Sequela atual: laudos, exames de imagem, relatório do médico assistente sobre consolidação e limitação.
6. Requerimento/decisão do INSS sobre o auxílio-acidente (ou cessação do auxílio-doença sem análise do B36).
7. Se já recebe aposentadoria ou tem data prevista para se aposentar.

## Prazo e contagem
- Sem decadência para concessão (STF Tema 313); prescrição das parcelas vencidas há mais de 5 anos do ajuizamento (art. 103, p.ú.). Se o auxílio-doença cessou há mais de 5 anos, as parcelas anteriores ao quinquênio estão perdidas, mas o benefício segue devido para frente.
- DIB: dia seguinte à cessação do auxílio-doença (art. 86, §2º). Sem benefício prévio, pedir desde a DER; sem DER, a jurisprudência do STJ tem fixado na citação (REsp 2.242.398, caso acidentário).
- Prazos processuais: `prazos-processuais`.

## Estrutura da peça   (detalhe em [estrutura](references/estrutura.md))
1. Competência da Justiça Federal (acidente sem nexo com o trabalho) e interesse de agir.
2. Qualidade de segurado e categoria contemplada (art. 18, §1º).
3. O acidente e a consolidação das lesões.
4. A sequela e a redução da capacidade para o trabalho habitual.
5. DIB, valor (50% do salário de benefício) e não cumulação com aposentadoria.
6. Perícia e quesitos.
7. Pedidos.

## Requisitos e preliminares
- Competência: a exceção do CF, art. 109, I, cobre só acidentes de trabalho; o auxílio-acidente de qualquer natureza é causa federal. A competência se define pelo pedido e pela causa de pedir (STJ, CC 187.898). Se os fatos sugerem nexo com o trabalho, decidir antes de ajuizar e, na dúvida, usar `prev-acidentario`.
- Sem carência (art. 26, I). Basta a qualidade de segurado na data do acidente.
- Segurados contemplados: incisos I, II, VI e VII do art. 11 — empregado, doméstico (desde a LC 150/2015), avulso e segurado especial (art. 18, §1º).
- Requisitos materiais (art. 86, caput): acidente de qualquer natureza; lesões consolidadas; sequela que implique redução da capacidade para o trabalho que habitualmente exercia. A redução precisa ser efetiva e permanente (STJ, AgInt nos EDcl no AREsp 1.757.537, remetendo ao repetitivo REsp 1.108.298/SC — Tema 416); sequela que nem reduz a capacidade nem exige maior esforço não dá direito (TNU Súmula 89). Argumento útil: maior esforço para a mesma tarefa é redução.
- Valor: 50% do salário de benefício, devido até a véspera de qualquer aposentadoria ou até o óbito (art. 86, §1º). Recebimento de salário ou de outro benefício, exceto aposentadoria, não prejudica o auxílio-acidente (§3º).
- Não cumula com aposentadoria (art. 86, §2º); a cumulação só se admite se lesão e aposentadoria forem anteriores a 11/11/1997 (STJ Súmula 507). Avaliar com o cliente o momento de se aposentar.
- Perícia: quesitos devem mirar consolidação, sequela, atividade habitual concreta e comparação antes x depois — não "incapacidade".

## Fundamentos verificados   (detalhe em [fundamentos](references/fundamentos.md))
- CF, art. 109, I; Lei 8.213/1991, arts. 18, §1º; 26, I; 86, caput e §§1º a 3º; 103, p.ú.
- STF Temas 313 e 350; STJ Súmula 507; STJ, AgInt nos EDcl no AREsp 1.757.537; STJ, AgInt no REsp 1.999.361; STJ, REsp 2.242.398; STJ, CC 187.898; TNU Súmula 89.

## Pedidos e requerimentos
- Concessão do auxílio-acidente desde o dia seguinte à cessação do auxílio-doença NB __ (ou desde a DER), em 50% do salário de benefício.
- Perícia médica na especialidade da sequela, com quesitos anexos.
- Parcelas vencidas com correção e juros pelo núcleo `juros-e-correcao`.
- Subsidiariamente, se a perícia apontar incapacidade, concessão do benefício por incapacidade cabível (fungibilidade).
- Justiça gratuita.

## Checklist pré-protocolo
- [ ] Acidente sem nexo com o trabalho demonstrado (ou competência estadual escolhida).
- [ ] Categoria de segurado contemplada pelo art. 18, §1º na data do acidente.
- [ ] Data de cessação do auxílio-doença e prescrição conferidas.
- [ ] Laudo de consolidação e descrição da atividade habitual concreta.
- [ ] Quesitos de redução da capacidade (não de incapacidade).
- [ ] Situação de aposentadoria verificada (vedação de cumular).
- [ ] Juros e correção remetidos ao núcleo.

## Erros a evitar
- Ajuizar para contribuinte individual, MEI ou facultativo.
- Levar à Justiça Estadual um acidente doméstico, ou à Federal um acidente de trajeto.
- Formular quesitos de incapacidade total e receber laudo "apto" sem análise da redução.
- Pedir DIB na data do acidente, ignorando o art. 86, §2º.
- Esquecer que a aposentadoria futura encerra o auxílio-acidente.

## Integração com o núcleo
- `juros-e-correcao`; `prazos-processuais`; `verificacao-de-citacoes`; `fidelidade-factual` (datas de DIB/DCB e do acidente); `estilo-forense`.

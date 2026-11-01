---
name: consumidor-plano-de-saude
description: >
  Redige ação de obrigação de fazer com tutela de urgência contra operadora de
  plano de saúde por negativa de cobertura, com base na Lei 9.656/1998 (art. 10,
  §§ 12 e 13, incluídos pela Lei 14.454/2022, na interpretação dada pelo STF),
  no CDC e nas Súmulas 302, 597, 608 e 609 do STJ. Use quando o usuário pedir
  liminar contra plano de saúde, negativa de cirurgia, exame, medicamento ou
  terapia, tratamento fora do rol da ANS, carência em urgência, recusa por doença
  preexistente, limite de internação ou cancelamento do plano durante tratamento.
metadata:
  area: consumidor
  tipo_peca: tutela
  verificado_em: 2026-11-01
---
# Plano de saúde — negativa de cobertura com tutela de urgência

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: negativa (expressa, tácita ou por demora) de procedimento, exame, internação, medicamento ou terapia; carência em urgência/emergência; recusa por doença preexistente; rescisão unilateral indevida.
- Não usar sozinha: reajuste por faixa etária ou sinistralidade (revisão contratual com cálculo atuarial) — adaptar com cuidado; plano de autogestão — o CDC não se aplica (Súmula 608), a fundamentação passa a ser Lei 9.656 e Código Civil.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Contrato: tipo (individual, coletivo empresarial/adesão, autogestão), data de adesão, segmentação (ambulatorial, hospitalar, obstétrica), carências.
2. Prescrição e relatório do médico assistente: diagnóstico (CID), tratamento, urgência, risco da demora, alternativas tentadas.
3. **Prova do requerimento à operadora e da negativa** (ou da demora irrazoável/omissão): protocolo, e-mail, carta, gravação.
4. O procedimento está no rol da ANS? Se não: existe alternativa no rol? Há registro na Anvisa? Há evidência científica de alto nível ou avaliação de tecnologia (Conitec ou agência internacional)? Há negativa expressa da ANS ou proposta de atualização pendente?
5. Orçamento do tratamento/medicamento e prazo em que é necessário.
6. Hospital/profissional: credenciado ou não? Há rede apta?

## Prazo e contagem
- Urgência: a peça é de tutela (CPC 300); pedir apreciação imediata e intimação por meio célere.
- Carência máxima em urgência/emergência: 24 horas (Lei 9.656, art. 12, V, "c"; Súmula 597).
- Indenização: prescrição [VERIFICAR: confirmar prazo aplicável ao caso — contratual (art. 205 CC) ou outro — via `verificacao-de-citacoes`].
- Prazos processuais: `prazos-processuais`.

## Estrutura da peça
Tutela de urgência em destaque → fatos → relação de consumo (Súmula 608) → dever de cobertura (rol, ou §13 + requisitos do STF) → abusividade da negativa → urgência → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Fora do rol: demonstrar **cumulativamente** os requisitos fixados pelo STF ao interpretar o art. 10 § 13 (ver fundamentos), com prova do requerimento prévio e da negativa. Sem isso, a liminar tende a ser negada.
- Pedir que o juízo consulte o NATJUS, quando houver — a decisão não pode se apoiar só no laudo da parte (tese do STF transcrita no REsp 2.253.522); juntar parecer técnico/literatura antecipa essa etapa.
- Medicamento de uso domiciliar: há exclusão legal (art. 10, VI) com exceções; verificar antes de pedir (o STJ reconheceu licitude da negativa em hipótese de uso domiciliar fora das exceções).
- Autogestão: retirar fundamentos de CDC.

## Fundamentos verificados
- Lei 9.656/1998: art. 10 §§ 4º, 12 e 13; art. 12, V, "c"; art. 13, p.ú., II e III; art. 35-C.
- STF, ADI 7.265 (interpretação conforme do § 13, requisitos cumulativos) — teses transcritas no REsp 2.253.522/STJ.
- Súmulas STJ 302 (limite de internação), 597 (carência em urgência), 608 (CDC, salvo autogestão), 609 (doença preexistente).
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Tutela de urgência: autorização e custeio do tratamento em prazo curto (horas/dias), sob multa diária, com alternativa de bloqueio de valores; expedição de ofício/mandado com urgência.
- Confirmação em sentença da obrigação de fazer.
- Reembolso de despesas já pagas (se houver) e dano moral quando a recusa agravou o quadro (fatos concretos).
- Inversão do ônus (exceto autogestão). Juros/correção: `juros-e-correcao`.

## Checklist pré-protocolo
- [ ] Tipo de contrato identificado (autogestão afasta o CDC)
- [ ] Prova do requerimento e da negativa/omissão juntada
- [ ] Relatório médico com urgência, CID e justificativa da escolha terapêutica
- [ ] Se fora do rol: cada requisito cumulativo demonstrado com documento
- [ ] Registro na Anvisa conferido
- [ ] Orçamento e prazo de necessidade
- [ ] Multa e prazo de cumprimento propostos
- [ ] Dano moral com fatos (não automático)

## Erros a evitar
- Tratar o rol como "meramente exemplificativo" sem demonstrar os requisitos legais e os do STF.
- Ajuizar sem prova do pedido administrativo à operadora.
- Basear-se só no laudo do médico assistente, sem evidência científica.
- Invocar CDC contra operadora de autogestão.
- Pedir medicamento sem registro na Anvisa como se fosse coberto.

## Integração com o núcleo
`juros-e-correcao` (reembolso e indenização), `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

---
name: amb-reserva-legal-e-car
description: >
  Orienta e redige requerimentos de regularização de reserva legal e do
  Cadastro Ambiental Rural (CAR) pela Lei 12.651/2012: inscrição e retificação
  do CAR, proposta de localização da reserva, cômputo de APP, adesão ao PRA e
  termo de compromisso, recomposição, regeneração ou compensação (art. 66),
  regime dos imóveis até 4 módulos fiscais (art. 67) e dispensa pelo art. 68.
  Use quando o usuário pedir regularizar fazenda, responder notificação do
  órgão estadual sobre o CAR, compensar reserva legal, aderir ao PRA ou provar
  que o desmatamento antigo respeitou a lei da época.
metadata:
  area: ambiental
  tipo_peca: requerimento
  verificado_em: 2026-11-25
---
# Regularização de reserva legal e CAR

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: requerimentos e manifestações ao órgão estadual (ou municipal conveniado) sobre CAR, reserva legal, PRA e compensação; parecer de enquadramento do imóvel.
- Não usar:
  - auto de infração já lavrado: `amb-defesa-auto-de-infracao` / `amb-recurso-auto-de-infracao`;
  - ACP do MP sobre a reserva: `amb-defesa-acao-civil-publica`; acordo com o MP: `amb-termo-ajustamento-conduta`;
  - titulação e regularização fundiária da posse: `agrario-regularizacao-fundiaria-rural`;
  - imóvel rural em inventário: `agrario-imovel-rural-no-inventario`.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Matrícula(s), área total, módulos fiscais do município e situação em 22/07/2008.
2. Bioma e localização (Amazônia Legal: floresta, cerrado, campos gerais; demais regiões).
3. Recibo e situação do CAR (ativo, pendente, cancelado), notificações recebidas.
4. Vegetação nativa existente, APPs, áreas consolidadas — com imagens datadas.
5. Histórico de supressão: quando, com qual autorização, e qual percentual exigia a lei da época.
6. Autos de infração, embargos, termos de compromisso ou TAC sobre o imóvel.
7. Plano do cliente: recompor, regenerar ou compensar? Há área excedente própria ou de terceiro?

## Prazo e contagem
- Inscrição no CAR obrigatória e por prazo indeterminado (art. 29, § 3º).
- Adesão ao PRA: requerer no prazo de 1 ano após notificação do órgão competente (art. 59, § 2º) — controlar a data da notificação.
- Recomposição de reserva desmatada irregularmente após 22/07/2008: iniciada nos prazos legais e concluída nos prazos do PRA (art. 17, § 4º); atividades na área ficam suspensas (art. 17, § 3º).
- Prazos de recurso administrativo dependem da norma estadual [VERIFICAR na legislação do Estado]; prazos judiciais: `prazos-processuais`.

## Estrutura do requerimento
Qualificação e imóvel → situação do CAR → diagnóstico (percentual exigido × existente) → enquadramento (art. 12, 15, 66, 67 ou 68) → proposta (localização, recomposição, regeneração, compensação, PRA) → documentos → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Percentuais (art. 12): Amazônia Legal — 80% em floresta, 35% em cerrado, 20% em campos gerais; demais regiões — 20%.
- Cômputo de APP na reserva (art. 15): sem conversão de novas áreas, área conservada ou em recuperação e requerimento no CAR.
- Localização aprovada pelo órgão estadual após inclusão no CAR; protocolada a documentação, não cabe sanção pela não formalização da reserva (art. 14, §§ 1º e 2º).
- Registro no CAR dispensa averbação na matrícula (art. 18, § 4º); o CAR não é título de posse ou propriedade (art. 29, § 2º).
- Obrigações têm natureza real e passam ao sucessor (art. 2º, § 2º; art. 7º, § 2º; Súmula 623/STJ).

## Fundamentos verificados
- Lei 12.651/2012: arts. 2º, § 2º; 3º, III; 12; 14; 15; 17; 18; 29; 59; 60; 66; 67; 68.
- Súmula 623/STJ (*propter rem*); Súmula 613/STJ (sem fato consumado).
- TAC anterior a 2012 não é revisto pelo novo Código: AgInt no AREsp 2.123.237 (STJ, 1ª T., 2024).
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Inscrição/retificação do CAR com a delimitação correta de APP, reserva legal e áreas consolidadas.
- Aprovação da localização da reserva legal (art. 14), com cômputo de APP quando cabível (art. 15).
- Adesão ao PRA e assinatura do termo de compromisso (art. 59), com suspensão das sanções por infrações anteriores a 22/07/2008 (§§ 4º e 5º).
- Reconhecimento da reserva pelo remanescente de 22/07/2008 (art. 67) ou dispensa de recompor (art. 68), com prova documental (art. 68, § 1º).
- Compensação (art. 66, § 5º): CRA, arrendamento de servidão/reserva, doação de área em UC pendente de regularização ou cadastramento de área equivalente no mesmo bioma (§ 6º).

## Checklist pré-protocolo
- [ ] Módulos fiscais e situação em 22/07/2008 comprovados
- [ ] Bioma e percentual aplicável corretos
- [ ] Imagens datadas e histórico de autorizações juntados
- [ ] Prazo de adesão ao PRA controlado a partir da notificação
- [ ] Área de compensação equivalente, no mesmo bioma, com CAR prévio
- [ ] Autos de infração/TAC existentes cruzados com o requerimento
- [ ] Norma estadual do PRA consultada

## Erros a evitar
- Tratar o CAR como prova de posse ou propriedade (art. 29, § 2º).
- Invocar o art. 67 para imóvel que só passou a ter até 4 módulos depois de 22/07/2008 (desmembramento posterior).
- Pedir dispensa pelo art. 68 sem documento que prove o percentual da época.
- Compensar em outro bioma ou com área sem equivalência de extensão (art. 66, § 6º).
- Usar a regularização administrativa para rever TAC firmado antes de 2012 (AgInt no AREsp 2.123.237).

## Integração com o núcleo
`prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

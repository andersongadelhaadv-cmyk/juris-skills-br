---
name: eleitoral-defesa-abuso-de-poder
description: >
  Redige a defesa de candidato, agente público ou terceiro em ação por abuso
  de poder e ilícitos de campanha — AIJE (art. 22 da LC 64/1990), AIME (art.
  14, § 10, da CF) e representações dos arts. 30-A, 41-A e 73 da Lei
  9.504/1997 — atacando prazo, legitimidade, polo passivo, prova e gravidade.
  Use quando o usuário pedir defesa ou contestação em AIJE ou AIME, defender
  prefeito ou vereador acusado de compra de votos, uso da máquina, caixa dois
  ou abuso econômico, ou evitar cassação e inelegibilidade.
metadata:
  area: eleitoral
  tipo_peca: contestacao
  verificado_em: 2026-11-25
---
# Defesa em ação por abuso de poder

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: defesa (contestação) e alegações finais do representado/impugnado em AIJE, AIME, art. 30-A, art. 41-A ou art. 73.
- Não usar: propor a ação — `eleitoral-aije` ou `eleitoral-aime`; defesa em representação por propaganda (art. 96) — `eleitoral-representacao-propaganda-irregular`; contestação de AIRC — `eleitoral-impugnacao-registro-candidatura`; recurso contra a cassação — `eleitoral-recurso-eleitoral`; improbidade ou crime pelo mesmo fato — `adm-defesa-em-improbidade` / `penal-resposta-a-acusacao`.

## Entradas mínimas (perguntar o que faltar; nunca supor fatos)
1. Cópia integral da inicial, documentos e decisão de notificação/citação, com a data da ciência.
2. Tipo da ação e fundamento legal invocado (muda prazo, legitimidade e sanção).
3. Datas: registro, eleição, diplomação, ajuizamento.
4. Versão do cliente para cada fato, com documentos (contratos, notas, extratos, prestação de contas, agenda, atos administrativos).
5. Testemunhas disponíveis (até 6 na AIJE/AIRC) e provas em poder de terceiros.
6. Outras ações sobre o mesmo fato (AIJE, AIME, representação, inquérito) e sua fase.

## Prazo e contagem
- AIJE e ritos do art. 22 (30-A, 41-A, 73): defesa em 5 dias da notificação (LC 64/1990, art. 22, I, "a").
- AIME: se aplicado o rito dos arts. 3º e seguintes da LC 64/1990, contestação em 7 dias (art. 4º) [VERIFICAR: rito da AIME na jurisprudência do TSE].
- Alegações: 2 dias na AIJE (art. 22, X); 5 dias no rito ordinário (art. 6º).
- Contagem e períodos de prazo contínuo: `prazos-processuais`.

## Estrutura da peça
Tempestividade → preliminares (decadência, ilegitimidade, inépcia, polo passivo, litispendência) → mérito fato por fato → ausência de gravidade → ausência de responsabilidade pessoal / prévio conhecimento → provas → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Decadência/intempestividade:** 30-A após 15 dias da diplomação (Lei 9.504/1997, art. 30-A); 41-A e 73 após a diplomação (art. 41-A, § 3º; art. 73, § 12); AIME após 15 dias da diplomação (CF, art. 14, § 10).
- **Ilegitimidade ativa:** 30-A só partido ou coligação; AIJE: partido, coligação, candidato ou MP (LC 64/1990, art. 22, caput).
- **Inépcia/indeferimento liminar:** falta de requisito ou de caso de representação (art. 22, I, "c"); AIME sem prova pré-constituída (CF, art. 14, § 10).
- **Polo passivo:** ausência de litisconsorte necessário (vice na majoritária) [VERIFICAR: Súmula 38 do TSE — JuriBase sem cobertura do TSE].
- **Reunião ou coisa julgada:** mesmo fato já julgado — art. 96-B, § 3º, da Lei 9.504/1997.

## Fundamentos verificados
- LC 64/1990, art. 22 (I, V, X, XIV, XVI), art. 23 (livre apreciação com motivação), arts. 3º a 7º.
- Lei 9.504/1997, arts. 30-A, 41-A (§ 1º dolo específico), 73 (§§ 4º, 5º, 12), 96-B.
- CF, art. 14, §§ 10 e 11 (temeridade e má-fé do autor).
- CE, art. 257, § 2º (efeito suspensivo do recurso contra cassação).
- STF, Tema 986 (consequência de cassação na majoritária).
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Acolhimento das preliminares e extinção.
- No mérito, improcedência; subsidiariamente, afastar a inelegibilidade de quem não praticou nem contribuiu para o ato (art. 22, XIV) e reduzir a multa ao mínimo.
- Produção de prova testemunhal (até 6), documental e requisições a terceiros (art. 22, VIII).
- Na AIME, condenação do autor por ação temerária ou de má-fé, se houver base (CF, art. 14, § 11).

## Checklist pré-protocolo
- [ ] Data da ciência e prazo de 5 (ou 7) dias conferidos
- [ ] Todas as preliminares de prazo e legitimidade testadas contra a data da diplomação
- [ ] Cada fato da inicial respondido (sem negativa genérica)
- [ ] Gravidade enfrentada com números (alcance, valores, eleitorado)
- [ ] Responsabilidade pessoal e prévio conhecimento discutidos
- [ ] Rol de testemunhas e documentos juntados com a defesa

## Erros a evitar
- Defender com "não alterou o resultado": o critério legal é a gravidade, não a potencialidade (art. 22, XVI).
- Negativa genérica: o art. 23 permite ao tribunal decidir por indícios e fatos notórios.
- Deixar de arrolar testemunhas na defesa (o rito concentra a prova).
- Esquecer que o vice e terceiros podem ter defesas próprias (ausência de participação).
- Ignorar ação conexa e perder a reunião (art. 96-B).

## Integração com o núcleo
`prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

---
name: amb-defesa-crime-ambiental
description: >
  Organiza a defesa em crime ambiental da Lei 9.605/1998 (pessoa física,
  dirigente ou pessoa jurídica): tipicidade dos delitos mais frequentes (arts.
  38, 48, 50, 54, 60, 69-A), responsabilidade penal da empresa (arts. 3º, 21 e
  22), composição do dano para transação (art. 27), suspensão condicional com
  laudo de reparação (art. 28) e suspensão da punibilidade pelo PRA (Lei
  12.651/2012, art. 60). Use quando o usuário pedir defesa em inquérito,
  denúncia, termo circunstanciado ou ação penal por desmatamento, poluição,
  operação sem licença ou laudo ambiental falso.
metadata:
  area: ambiental
  tipo_peca: contestacao
  verificado_em: 2026-11-25
---
# Defesa em crime ambiental

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: o núcleo ambiental da defesa — tipicidade, prova técnica, responsabilidade da pessoa jurídica e dos dirigentes, institutos despenalizadores próprios da Lei 9.605 e reflexos das esferas cível e administrativa.
- A peça processual em si segue a skill penal correspondente:
  - resposta à acusação: `penal-resposta-a-acusacao`;
  - ANPP: `penal-anpp`; habeas corpus/trancamento: `penal-habeas-corpus`;
  - alegações finais e apelação: `penal-alegacoes-finais`, `penal-apelacao-criminal`; pena: `penal-dosimetria`.
- Não usar: auto de infração (`amb-defesa-auto-de-infracao`); ACP sobre o mesmo fato (`amb-defesa-acao-civil-publica`).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Peça acusatória (ou termo circunstanciado/portaria do inquérito) e tipo penal imputado.
2. Quem é acusado: pessoa física, dirigente, pessoa jurídica — e qual decisão interna ligou a empresa ao fato.
3. Laudos: há perícia de constatação? Quem fez, quando, com que método?
4. Licenças, autorizações, CAR, PRA, termo de compromisso, TAC.
5. Já houve reparação ou composição do dano? Há laudo de reparação?
6. Data do fato (prescrição; marco de 22/07/2008 para o PRA) e antecedentes ambientais.
7. Reorganização societária (incorporação, extinção) após o fato.

## Prazo e contagem
- Prazos penais seguem a contagem própria do processo penal, diferente da do CPC: use `prazos-processuais`.
- Prescrição penal pela pena máxima do tipo; o termo de compromisso do PRA interrompe a prescrição durante a suspensão (Lei 12.651, art. 60, § 1º).

## Estrutura da defesa
Pressupostos (justa causa, inépcia) → tipicidade objetiva e subjetiva do tipo ambiental → prova técnica → autoria (dirigente/empresa) → institutos despenalizadores → pena. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Pessoa jurídica responde penalmente quando a infração decorre de decisão do representante legal/contratual ou órgão colegiado, no interesse ou benefício dela (art. 3º); isso não exclui a das pessoas físicas (parágrafo único). Ataque a ausência de descrição dessa decisão na denúncia.
- Dirigente: o art. 2º exige que soubesse da conduta e pudesse evitá-la; cargo, por si, não basta.
- Incorporação da empresa acusada: extinção da punibilidade pela intranscendência da pena, sem migrar para a incorporadora (REsp 1.977.172).
- Perícia: art. 19 (constatação do dano para fiança e multa); no art. 54, *caput*, primeira parte, o STJ fixou natureza formal e desnecessidade de perícia (Tema 1.377) — a defesa deve discutir a potencialidade concreta, não exigir laudo de dano.

## Fundamentos verificados
- CF, art. 225, § 3º (independência das esferas penal, administrativa e civil).
- Lei 9.605/1998: arts. 2º, 3º, 6º, 7º, 14, 19, 20, 21, 22, 27, 28, 38, 48, 50, 54, 60 e 69-A.
- Lei 12.651/2012, art. 60 (suspensão da punibilidade dos arts. 38, 39 e 48 pelo termo do PRA; extinção com a regularização).
- Tema 1.377/STJ; REsp 1.977.172 (STJ, 3ª Seção, 2022).
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Rejeição da denúncia/absolvição sumária por atipicidade, inépcia (falta de descrição da decisão societária ou da conduta do dirigente) ou falta de justa causa.
- Extinção da punibilidade (incorporação; regularização pelo PRA; prescrição).
- Transação penal condicionada à composição do dano, ou demonstração da impossibilidade (art. 27).
- Suspensão condicional do processo com cronograma de reparação e laudo (art. 28).
- Perícia e assistente técnico; quesitos sobre extensão, causalidade e reversibilidade.
- Subsidiariamente: atenuantes do art. 14 (reparação espontânea, comunicação do perigo, colaboração), penas restritivas (art. 7º) e, para a empresa, penas do art. 21 proporcionais à situação econômica (art. 6º, III).

## Checklist pré-protocolo
- [ ] Tipo penal conferido no texto vigente (atenção às alterações da Lei 15.190/2025 no art. 60 e no art. 67)
- [ ] Denúncia descreve decisão societária (PJ) e ciência/poder de evitar (dirigente)?
- [ ] Laudo e cadeia de custódia examinados
- [ ] Composição do dano tentada e documentada (transação)
- [ ] PRA/termo de compromisso verificado para arts. 38, 39 e 48
- [ ] Reflexos na ACP e no auto de infração mapeados (o que se admite numa esfera vale como prova na outra)

## Erros a evitar
- Tratar a reparação como confissão e recusar compor o dano: sem composição não há transação (art. 27).
- Pedir a extinção da punibilidade pelo PRA para crime fora dos arts. 38, 39 e 48.
- Exigir perícia de dano no art. 54, *caput*, primeira parte, contra o Tema 1.377.
- Esquecer que a pena do art. 60 foi alterada pela Lei 15.190/2025, com vigência a conferir [VERIFICAR].
- Defender a empresa e o dirigente com teses conflitantes sem avaliar conflito de interesses.

## Integração com o núcleo
`prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`; peças penais: `penal-*` (ver acima).

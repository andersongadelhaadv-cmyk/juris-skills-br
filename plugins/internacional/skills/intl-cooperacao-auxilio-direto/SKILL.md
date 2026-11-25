---
name: intl-cooperacao-auxilio-direto
description: >
  Orienta pedido de cooperação jurídica internacional por auxílio direto
  (ativo ou passivo) e a defesa de quem é alvo de medida pedida por Estado
  estrangeiro, com base nos arts. 26 a 34 e 37 a 41 do CPC: autoridade
  central, papel da AGU e do MPF, competência do juiz federal e limites de
  ordem pública. Use quando o usuário precisar obter prova, informação ou
  documento no exterior sem carta rogatória, responder a pedido estrangeiro
  de quebra de sigilo ou bloqueio cumprido por juiz federal, ou decidir
  entre auxílio direto e carta rogatória.
metadata:
  area: internacional
  tipo_peca: requerimento
  verificado_em: 2026-11-25
---
# Cooperação jurídica internacional — auxílio direto

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: a medida **não decorre** de decisão judicial estrangeira a delibar no Brasil (CPC, art. 28) — informação sobre o direito ou sobre processos, colheita de prova, outra medida não proibida (art. 30); pedido ativo de autoridade brasileira; defesa do atingido por medida de auxílio direto passivo deferida por juiz federal.
- Não usar: há decisão judicial estrangeira a cumprir (carta rogatória — `intl-carta-rogatoria-exequatur`; sentença definitiva — `intl-homologacao-sentenca-estrangeira`); entrega de pessoa (`intl-defesa-extradicao`); legalização de documento para uso particular (`intl-apostilamento-legalizacao`).

## Entradas mínimas (perguntar o que faltar; nunca supor fatos)
1. Direção: ativo (Brasil pede) ou passivo (Estado estrangeiro pede ao Brasil).
2. Matéria: civil, comercial, família, penal — define o tratado e a autoridade central designada.
3. Tratado aplicável (bilateral ou multilateral) ou ausência dele (reciprocidade por via diplomática — art. 26, § 1º).
4. Medida pretendida e sua base: há decisão judicial estrangeira por trás? (Se sim, é rogatória.)
5. No passivo: quem requereu em juízo (AGU ou MPF), qual juízo federal deferiu, data da ciência, o que foi colhido ou bloqueado.
6. Há sigilo legal no Brasil ou no Estado requerente (art. 26, III)?

## Prazo e contagem
- Não há prazo legal único para o pedido. Na defesa do atingido, os prazos são os do meio de impugnação escolhido perante o juízo federal ou o tribunal (agravo, mandado de segurança, habeas corpus no penal) — conte com `prazos-processuais`.

## Estrutura da peça
Ativo: requerimento ao juízo (ou à autoridade central, se não exigir jurisdição) com objeto, base convencional, fatos e quesitos, traduções. Passivo (defesa): petição ao juízo federal ou recurso ao tribunal, demonstrando que a medida exigia rogatória, ofende ordem pública ou normas fundamentais, ou excede o pedido. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Princípios (art. 26):** devido processo no Estado requerente; igualdade de tratamento e assistência judiciária; publicidade, salvo sigilo; autoridade central; espontaneidade na troca de informações. Vedados atos que contrariem normas fundamentais do Estado brasileiro (§ 3º).
- **Autoridade central:** a designada no tratado; na falta, o Ministério da Justiça (art. 26, § 4º). Ela se comunica diretamente com as congêneres (art. 31).
- **Passivo sem atividade jurisdicional:** a própria autoridade central providencia (art. 32).
- **Passivo com atividade jurisdicional:** a autoridade central encaminha à AGU, que requer em juízo; o MPF requer quando for a autoridade central (art. 33). Competente o juízo federal do lugar da execução (art. 34).
- **Ativo:** pedido vai à autoridade central com tradução para a língua do Estado requerido (arts. 37 e 38).
- **Documentos:** o que chega por autoridade central ou via diplomática é autêntico, sem legalização (art. 41).
- **Limite de prova:** não cabe colheita de prova para processo estrangeiro em matéria de competência exclusiva brasileira (art. 30, II).
- **Linha do STJ:** auxílio direto e rogatória têm natureza distinta; havendo decisão judicial estrangeira, o exequatur é imprescindível (AgInt na CR 21.916, 2025). No auxílio direto, não se exige exequatur (AgRg no RHC 186.237, 5ª Turma, 2025).

## Fundamentos verificados
- CPC arts. 26 a 34 e 37 a 41; art. 40 (execução de decisão estrangeira só por rogatória ou homologação).
- STJ: AgInt na CR 21.916 (Corte Especial, 2025); AgRg no RHC 186.237 (5ª Turma, 2025).
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Ativo: expedição do pedido de cooperação pela autoridade central, com objeto delimitado, quesitos e traduções; preservação de sigilo, se cabível.
- Defesa no passivo: declaração de que a medida dependia de exequatur (se havia decisão judicial estrangeira); limitação da medida ao objeto do pedido; preservação de sigilo e de dados de terceiros; restituição ou não transmissão do material colhido, conforme o caso [VERIFICAR: viabilidade concreta de retenção ou devolução de prova já enviada não conferida em precedente].

## Checklist pré-protocolo
- [ ] Verificado se há decisão judicial estrangeira por trás (rogatória x auxílio direto)
- [ ] Tratado e autoridade central identificados
- [ ] No passivo: quem requereu (AGU/MPF) e qual juízo federal decidiu
- [ ] Objeto delimitado e proporcional
- [ ] Traduções para a língua do Estado requerido (ativo)
- [ ] Sigilo legal avaliado nos dois Estados

## Erros a evitar
- Tratar como rogatória (e mandar ao STJ) pedido que é auxílio direto — e vice-versa.
- Impugnar auxílio direto apenas por "falta de exequatur" quando não há decisão judicial estrangeira a delibar.
- Ignorar o art. 26, § 3º: o argumento forte é a incompatibilidade com normas fundamentais, não o mérito da investigação estrangeira.
- Pedir prova para processo estrangeiro sobre matéria de competência exclusiva brasileira.

## Integração com o núcleo
`prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`. Vizinhas: `intl-carta-rogatoria-exequatur`, `intl-homologacao-sentenca-estrangeira`, `penal-habeas-corpus`, `adm-mandado-de-seguranca`.

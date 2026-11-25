---
name: prev-impugnacao-laudo-pericial
description: >
  Redige a manifestação de impugnação ao laudo da perícia médica judicial em
  ação de benefício por incapacidade, auxílio-acidente ou BPC, com pedido de
  esclarecimentos, quesitos complementares, nova perícia ou substituição do
  perito (CPC, arts. 465, 468, 469, 473, 477, 479 e 480; Lei 10.259/2001,
  art. 12). Use quando o usuário pedir para impugnar laudo pericial, contestar
  perícia médica judicial, manifestar sobre laudo desfavorável, pedir nova
  perícia ou perito especialista, apontar laudo omisso ou contraditório, ou
  discutir a DII fixada pelo perito.
metadata:
  area: previdenciario
  tipo_peca: outro
  verificado_em: 2026-11-25
---
# Impugnação ao laudo da perícia médica judicial

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: laudo judicial desfavorável, omisso, contraditório ou sem método em ação de auxílio por incapacidade temporária, aposentadoria por incapacidade permanente, auxílio-acidente ou BPC à pessoa com deficiência; DII ou DCB fixadas sem base; quesitos não respondidos.
- Não usar: petição inicial e quesitos iniciais → `prev-beneficio-por-incapacidade`, `prev-acidentario` ou `prev-bpc-loas`. Restabelecimento após alta programada → `prev-beneficio-por-incapacidade`. Sentença já proferida → recurso (`civel-apelacao`, recurso inominado em `civel-juizado-especial`, `prev-pedido-de-uniformizacao-tnu`). Perícia técnica de tempo especial → `prev-aposentadoria-especial`.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Laudo completo e data da intimação.
2. Quesitos apresentados pelas partes e pelo juízo; quais ficaram sem resposta.
3. Documentos médicos do cliente (com datas, CID, exames, tratamentos, afastamentos), em ordem cronológica.
4. Atividade habitual detalhada, idade, escolaridade.
5. Parecer de assistente técnico, se houver.
6. Especialidade do perito e da doença; houve exame físico? Quanto tempo durou?
7. Rito: JEF ou procedimento comum (muda a fase e a forma).

## Prazo e contagem
- Procedimento comum: 15 dias da intimação do laudo para manifestação das partes e parecer do assistente técnico (CPC, art. 477, § 1º).
- JEF: seguir o prazo fixado pelo juízo; contagem e regras especiais em `prazos-processuais`.
- Arguição de impedimento ou suspeição do perito: 15 dias da intimação da nomeação (CPC, art. 465, § 1º); fato posterior se alega na primeira oportunidade [VERIFICAR: prazo para fato superveniente].
- Prazo perdido = preclusão do ponto; impugnar tudo de uma vez.

## Estrutura da peça   (detalhe em [estrutura](references/estrutura.md))
1. Tempestividade.
2. Síntese do laudo (conclusão, DID, DII, prognóstico).
3. Vícios formais (art. 473): objeto, análise técnica, método, respostas conclusivas.
4. Vícios de conteúdo: omissões, contradições internas, divergência com a prova documental, atividade habitual mal compreendida.
5. Pedido principal (esclarecimentos / quesitos complementares) e subsidiário (nova perícia, substituição do perito).
6. Pedido para que o juiz aprecie o laudo com os demais elementos (art. 479) e, se for o caso, as condições pessoais.

## Requisitos e preliminares
- **O juiz não fica preso ao laudo:** aprecia a prova pericial pelo art. 371 e indica os motivos para acolher ou afastar suas conclusões (CPC, art. 479). Por isso a impugnação aponta elementos concretos dos autos, não só discordância.
- **Esclarecimentos:** o perito deve esclarecer, em 15 dias, os pontos divergentes apresentados pelas partes (art. 477, § 2º); pode ser intimado para a audiência (art. 477, § 3º).
- **Quesitos suplementares** podem ser apresentados durante a diligência (art. 469).
- **Nova perícia** quando a matéria não estiver suficientemente esclarecida; não substitui a primeira, o juiz avalia ambas (art. 480, caput e § 3º).
- **Substituição do perito** por falta de conhecimento técnico ou por descumprimento injustificado do prazo (art. 468).
- **Perito especialista:** o CPC manda nomear "perito especializado no objeto da perícia" (art. 465), mas o STJ entende que a especialidade médica, em regra, não é pressuposto de validade da perícia (AgInt no AREsp 2.416.506). Pedir especialista com fundamento concreto (doença complexa, laudo que ignora exames da área), não por regra.
- **Condições pessoais:** reconhecida incapacidade parcial, o juiz deve analisar as condições pessoais e sociais para a aposentadoria por incapacidade permanente (TNU Súmula 47); se não reconhecer incapacidade para a atividade habitual, não é obrigado a analisá-las (TNU Súmula 77). Logo, ataque primeiro a conclusão sobre a atividade habitual.
- **DII:** ponto decisivo para qualidade de segurado e preexistência (TNU Súmula 53). Laudo que fixa DII sem justificativa ou contra documentos datados deve ser impugnado especificamente.

## Fundamentos verificados   (detalhe em [fundamentos](references/fundamentos.md))
- CPC, arts. 465, 467, 468, 469, 473, 477, 479 e 480; Lei 10.259/2001, art. 12, § 2º; Lei 8.213/1991, arts. 60, §§ 8º e 9º, e 101.
- TNU Súmulas 47, 53 e 77; STJ, AgInt no AREsp 2.416.506.

## Pedidos e requerimentos
- Intimação do perito para responder, de forma conclusiva, aos quesitos não respondidos e aos complementares (listar numerados).
- Subsidiariamente, nova perícia com perito de especialidade X, justificando (art. 480).
- Se o caso: substituição do perito (art. 468) ou arguição de impedimento/suspeição (art. 467).
- Apreciação do laudo com os documentos médicos (art. 479) e, reconhecida incapacidade parcial, das condições pessoais (Súmula 47/TNU).
- Fixação de DCB compatível com o prognóstico e com reavaliação pelo INSS (Lei 8.213, art. 60, §§ 8º e 9º; art. 101), quando o laudo for favorável mas a DCB for irreal.

## Checklist pré-protocolo
- [ ] Prazo conferido em `prazos-processuais`.
- [ ] Cada quesito sem resposta identificado pelo número.
- [ ] Contradições citadas com a página/trecho do laudo.
- [ ] Cada documento médico confrontado indicado com data e ID nos autos.
- [ ] Atividade habitual descrita de forma concreta.
- [ ] Pedido principal e subsidiário separados.
- [ ] Parecer do assistente técnico juntado, se houver.

## Erros a evitar
- Impugnação genérica ("o laudo não condiz com a realidade") sem apontar trecho e documento.
- Pedir só "nova perícia com especialista" sem demonstrar a insuficiência do laudo.
- Deixar passar o prazo e tentar discutir o laudo só na apelação.
- Ignorar a DII fixada pelo perito quando ela derruba a qualidade de segurado.
- Juntar documento médico novo sem explicar por que não existia antes.

## Integração com o núcleo
- `prazos-processuais`; `verificacao-de-citacoes`; `fidelidade-factual` (trechos do laudo e datas dos documentos); `estilo-forense`.

---
name: prev-agravo-de-instrumento-previdenciario
description: >
  Redige agravo de instrumento em ação previdenciária contra o INSS (CPC, arts.
  1.015 a 1.019), sobretudo contra decisão que nega, concede ou revoga tutela de
  benefício, com pedido de antecipação da tutela recursal e atenção ao regime do
  JEF, onde só se recorre de medida cautelar (Lei 10.259, arts. 4º e 5º). Use
  quando o usuário pedir agravo contra indeferimento de liminar de benefício,
  restabelecimento negado, cessação de auxílio por incapacidade, gratuidade
  negada, perícia indeferida ou decisão no cumprimento de sentença contra o INSS.
metadata:
  area: previdenciario
  tipo_peca: recurso
  verificado_em: 2026-11-25
---
# Agravo de instrumento previdenciário

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: decisão interlocutória em ação previdenciária no procedimento comum (vara federal ou competência delegada) que verse sobre tutela provisória, gratuidade, exibição de documento (processo administrativo, PPP), ou proferida no cumprimento de sentença contra o INSS (CPC, art. 1.015, I, V, VI e parágrafo único).
- Usar também fora do rol, demonstrando urgência pela inutilidade do exame na apelação (Tema 988/STJ) — ex.: perícia indeferida em caso de incapacidade que se agrava.
- JEF: só há recurso contra decisão que defere ou indefere medida cautelar/antecipatória (Lei 10.259, arts. 4º e 5º); a peça é dirigida à Turma Recursal e o rito segue o regimento local [VERIFICAR: nome e prazo no regimento da Turma Recursal].
- Não usar contra sentença (`prev-apelacao-previdenciaria`) nem para pedir a tutela pela primeira vez (`prev-tutela-de-urgencia-previdenciaria`). Técnica geral do agravo: `civel-agravo-de-instrumento`. Ação acidentária estadual: o agravo vai ao TJ (`prev-acidentario`).

## Entradas mínimas (perguntar o que faltar; nunca supor fatos)
1. Decisão agravada integral e certidão ou registro da intimação.
2. Peças da origem: inicial, contestação (se houver), petição que gerou a decisão, procurações.
3. O que o segurado pediu e por que o juiz negou (ausência de prova, necessidade de perícia, irreversibilidade).
4. Prova da probabilidade: laudos, CNIS, carta de indeferimento ou de cessação, PPP.
5. Prova do perigo: renda atual, doença, idade, dependentes, dívidas de subsistência.
6. Se já existe benefício ativo ou concessão anterior por tutela (risco de devolução — Tema 692/STJ).

## Prazo e contagem
- 15 dias úteis (CPC, art. 1.003, § 5º); o INSS responde em dobro (art. 183), salvo no JEF (Lei 10.259, art. 9º).
- Contagem: `prazos-processuais`.

## Estrutura da peça
Endereçamento ao TRF (ou Turma Recursal, no JEF) → partes e advogados (art. 1.016) → cabimento (inciso do art. 1.015 ou Tema 988) → tempestividade → decisão agravada → razões (probabilidade e perigo, com a prova) → pedido de antecipação da tutela recursal (art. 1.019, I) → pedidos → rol de peças. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Instrução obrigatória (art. 1.017, I): inicial, contestação, petição que ensejou a decisão, decisão agravada, prova da intimação e procurações; ou declaração de inexistência pelo advogado (art. 1.017, II). Em autos eletrônicos, conferir a regra do tribunal [VERIFICAR: dispensa de peças em processo eletrônico no TRF].
- Pedido de efeito ativo: o relator pode deferir a pretensão recursal em antecipação de tutela (art. 1.019, I) — é aqui que se pede a implantação imediata do benefício.
- Tutela antecipada não se concede se houver perigo de irreversibilidade (CPC, art. 300, § 3º); enfrentar o argumento com o caráter alimentar e com a possibilidade de desconto futuro (Lei 8.213, art. 115, II).
- A restrição da ADC 4 não se aplica à tutela em causa previdenciária (Súmula 729/STF).

## Fundamentos verificados
- CPC, arts. 183, 300, 1.003, 1.015, 1.016, 1.017, 1.019; Lei 10.259, arts. 4º, 5º e 9º; Lei 8.213, art. 115, II.
- Tema 988/STJ: taxatividade mitigada do rol do art. 1.015, com urgência pela inutilidade do julgamento na apelação.
- Súmula 729/STF; Tema 692/STJ (devolução e desconto de até 30%).
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Antecipação da tutela recursal para determinar a implantação ou o restabelecimento do benefício X em N dias, com multa diária.
- Ao final, provimento para reformar a decisão.
- Intimação do agravado para resposta (art. 1.019, II).
- Subsidiariamente, determinação de perícia com urgência ou de juntada do processo administrativo.

## Checklist pré-protocolo
- [ ] Cabimento indicado (inciso do art. 1.015 ou urgência do Tema 988)
- [ ] Tribunal certo: TRF (vara federal ou competência delegada) ou Turma Recursal (JEF)
- [ ] Peças obrigatórias anexadas ou declaração do art. 1.017, II
- [ ] Probabilidade com documento, não só alegação
- [ ] Perigo concreto (renda, doença, idade) demonstrado
- [ ] Irreversibilidade e Tema 692 enfrentados
- [ ] Prazo conferido

## Erros a evitar
- Agravar no JEF de decisão que não trata de medida cautelar ou antecipatória (Lei 10.259, art. 5º).
- Usar o agravo para discutir mérito ainda não decidido na origem (supressão de instância).
- Invocar o Tema 988 sem demonstrar por que a apelação chegaria tarde.
- Não informar ao cliente o risco de devolver o que receber se a tutela cair (Tema 692).

## Integração com o núcleo
`prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`; `juros-e-correcao` só se o agravo for no cumprimento de sentença.

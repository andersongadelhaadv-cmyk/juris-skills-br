---
name: desp-recurso-tas-cas
description: >
  Organiza a apelação (statement of appeal e appeal brief) à Corte Arbitral do
  Esporte (TAS/CAS), em Lausanne, contra decisão de federação internacional,
  da FIFA ou de órgão antidopagem, e a posterior homologação da sentença
  arbitral estrangeira no STJ (Lei 9.307/1996, arts. 34 a 39). Use quando o
  usuário pedir recurso ao TAS ou ao CAS, arbitragem esportiva internacional,
  apelação contra decisão da FIFA, de federação internacional ou da Justiça
  Antidopagem em caso internacional, ou homologação de laudo do CAS no Brasil.
metadata:
  area: desportivo
  tipo_peca: recurso
  verificado_em: 2026-11-25
---
# Recurso ao TAS/CAS

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: (a) decisão final de órgão desportivo cujo estatuto ou regulamento prevê apelação ao CAS; (b) decisão antidopagem em procedimento extraordinário ou recorrível por entidade internacional (Código Brasileiro Antidopagem, arts. 318, 320 e 331); (c) homologação, no STJ, de sentença do CAS a ser executada no Brasil.
- Não usar: recurso interno da Justiça Desportiva brasileira (`desp-recurso-stjd`); defesa antidopagem em primeira instância nacional (`desp-defesa-antidoping`); arbitragem comercial comum entre clubes (`contratos-*` ou `civel-*`); disputa de transferência ainda na FIFA ou na CBF (`desp-nulidade-transferencia-internacional`).

## Entradas mínimas (perguntar o que faltar; nunca supor fatos)
1. Decisão recorrida, com data e forma da notificação ao cliente (e-mail, sistema TMS/FIFA, carta).
2. Fundamento da competência do CAS: cláusula estatutária, regulamento da federação, cláusula do contrato ou compromisso arbitral.
3. Regulamento aplicável e prazo de apelação nele previsto (o regulamento da federação pode fixar prazo próprio).
4. Recursos internos esgotados? Quais e quando.
5. Idioma do procedimento, número de árbitros pretendido, indicação de árbitro da lista.
6. Pedido de medida provisória (suspensão da decisão) e sua urgência.
7. Capacidade de pagar a taxa e os adiantamentos de custas; pedido de assistência jurídica, se for o caso.

## Prazo e contagem
- Prazo de apelação: o do estatuto ou regulamento da entidade; na falta, o prazo supletivo do Código do CAS [VERIFICAR: conferir o artigo e o número de dias na versão vigente do Código do CAS antes de afirmar].
- Antidopagem nacional: vinte e um dias corridos do recebimento da decisão para recorrer ao CAS (Código Brasileiro Antidopagem 2021, art. 324); terceiro com direito de recorrer pode pedir cópia dos autos em quinze dias corridos (art. 324, § 1º).
- Prazos do CAS são fatais e contados conforme o próprio Código; registrar a data exata da notificação.
- Homologação no STJ: sem prazo de ajuizamento na Lei 9.307/1996; prazos da defesa e recursos: `prazos-processuais`.

## Estrutura da peça
Declaração de apelação (statement of appeal: partes, decisão, competência, pedidos, árbitro, idioma, medida provisória) → memorial de apelação (appeal brief: fatos, direito aplicável, mérito, provas, pedidos) → eventual pedido de medidas provisórias → depois, homologação no STJ. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Competência do CAS depende de base convencional (estatuto, regulamento, contrato) — demonstrar a cadeia de remissões até a cláusula.
- Esgotamento das vias internas da entidade, quando o regulamento exigir; a AMA pode recorrer direto ao CAS sem esgotar instâncias internas em antidopagem (CBA, art. 316, § 3º).
- No CAS, a matéria recorrida é devolvida por inteiro (CBA, art. 316, § 2º, em antidopagem); revisão de fato e de direito.
- Notificar a AMA e as demais partes com direito a recurso, quando o caso for antidopagem (CBA, art. 331, parágrafo único).
- Sede na Suíça: a impugnação do laudo segue a lei suíça — envolver correspondente local.

## Homologação no STJ
- Sentença arbitral estrangeira é a proferida fora do território nacional (Lei 9.307/1996, art. 34, parágrafo único) e depende só da homologação do STJ (art. 35).
- Defesas do requerido limitadas às hipóteses do art. 38 (incapacidade, convenção inválida, falta de notificação ou de contraditório, excesso, instituição irregular, sentença não obrigatória ou anulada) e do art. 39 (matéria não arbitrável pela lei brasileira; ofensa à ordem pública).
- Citação feita conforme a convenção ou a lei do país da arbitragem, inclusive postal com prova de recebimento e prazo hábil, não ofende a ordem pública (art. 39, parágrafo único).
- Precedentes do STJ sobre homologação de laudos do CAS não foram localizados no JuriBase [VERIFICAR].

## Fundamentos verificados
- Lei 9.307/1996, arts. 34, 35, 38 e 39.
- Código Brasileiro Antidopagem 2021 (compilado com Res. CNE 2/2022 e 68/2022), arts. 316, 318, 320, 324 e 331.
- CBJD (consolidado de 2009), art. 136, § 1º (irrecorribilidade do Pleno do STJD, ressalvada a regulamentação internacional da modalidade).
- Código do CAS: apenas referência; nenhum artigo citado sem conferência [VERIFICAR].
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Admissão da apelação e fixação da competência do CAS.
- Medida provisória para suspender a decisão recorrida até o laudo.
- Anulação ou reforma da decisão (absolvição, redução de sanção, restabelecimento de resultado).
- Condenação da parte contrária em custas e contribuição para honorários, nos termos do Código do CAS.
- Produção de prova: documentos, testemunhas, peritos, audiência.

## Checklist pré-protocolo
- [ ] Data da notificação da decisão comprovada e prazo do regulamento conferido
- [ ] Cadeia de competência documentada (estatuto → regulamento → cláusula)
- [ ] Vias internas esgotadas, ou dispensa demonstrada
- [ ] Taxa de protocolo paga e adiantamento de custas planejado
- [ ] Árbitro indicado e idioma escolhido
- [ ] Partes com direito a recurso notificadas (antidopagem)
- [ ] Versão vigente do Código do CAS conferida

## Erros a evitar
- Perder o prazo por contar da publicação, e não do recebimento da decisão.
- Confundir declaração de apelação com memorial e protocolar o memorial fora do prazo próprio.
- Citar artigo do Código do CAS de memória.
- Ignorar que a decisão desportiva continua produzindo efeitos sem medida provisória.
- Executar laudo do CAS no Brasil sem a homologação do STJ.

## Integração com o núcleo
`prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`, `juros-e-correcao` (se o laudo condenar em dinheiro).

---
name: sucessoes-inventario-extrajudicial
description: >
  Prepara inventário e partilha por escritura pública (CPC art. 610 §§1º e 2º; Res. CNJ
  35/2007 com as alterações das Res. 571/2024 e 695/2026), inclusive com herdeiro menor ou
  incapaz e com testamento nas hipóteses admitidas. Use quando o usuário pedir inventário em
  cartório, inventário extrajudicial, escritura de inventário, adjudicação em cartório,
  inventário com menor em cartório, inventário com testamento em cartório, minuta de
  escritura de partilha.
metadata:
  area: familia-sucessoes
  tipo_peca: outro
  verificado_em: 2026-11-01
---
# Inventário extrajudicial (escritura pública)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: todos os interessados concordes e assistidos por advogado; inclusive com herdeiro menor/incapaz (pagamento em parte ideal de cada bem + manifestação favorável do MP) e com testamento (após autorização do juízo no processo de abertura e cumprimento).
- Não usar: divergência entre herdeiros; testamento que reconheça filho ou contenha declaração irrevogável (vedado pela Res. 35, art. 12-B §1º); partilha desigual para incapaz; impugnação do MP ou de terceiro (vai a juízo). Nesses casos, `sucessoes-inventario-judicial`.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Certidão de óbito; estado civil e regime; certidões dos herdeiros.
2. Busca de testamento (certidão da Central notarial); se houver, decisão judicial que autoriza a via extrajudicial.
3. Herdeiros: capacidade; menores/incapazes e seus representantes.
4. Bens, valores atribuídos e documentos (matrículas, CRLV, extratos, contrato social); dívidas.
5. Inventariante indicado; necessidade de vender bem durante o procedimento.
6. Lei estadual do ITCMD e situação do recolhimento (prévio ou posterior).
7. Companheiro sobrevivente: a união é reconhecida por todos os herdeiros?

## Prazo e contagem
- Mesmo prazo de abertura de 2 meses (CPC 611) para fins de multa estadual (Súmula 542 STF) — confirmar a lei local.
- Desde a Res. CNJ 695/2026, a escritura não depende de prévio recolhimento do ITCMD; o tabelião comunica o fisco em 5 dias (ou no prazo da lei tributária). O imposto continua devido pela alíquota da data do óbito (Súmula 112 STF).
- Prazo para pagar despesas após venda de bem autorizada na escritura: até 1 ano (Res. 35, art. 11-A §1º).

## Estrutura da peça
Minuta de escritura (ou roteiro para o tabelião) → nomeação do inventariante → qualificação → autor da herança → herdeiros e meeiro → bens → dívidas → partilha → declarações tributárias → cláusulas finais. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Todos capazes e concordes, ou incapaz com quinhão em parte ideal em cada bem e parecer favorável do MP (Res. 35, art. 12-A).
- Testamento: autorização expressa do juízo sucessório em ação de abertura e cumprimento; todos capazes e concordes; dúvida → tabelião suscita o juízo (Res. 35, art. 12-B).
- Advogado ou defensor obrigatório, com qualificação e assinatura no ato (CPC 610 §2º).
- Livre escolha do tabelião (Res. 35, art. 1º); escritura dispensa homologação e vale para registro e bancos (CPC 610 §1º).
- Companheiro: herdeiro quando a união é reconhecida pelos demais sucessores (Res. 35, arts. 18 e 19); se houver disputa, via judicial ou ação declaratória antes.

## Fundamentos verificados
CPC 610 §§1º e 2º, 611; Res. CNJ 35/2007 arts. 1º, 3º, 11-A, 12-A, 12-B, 15, 18, 19, 26, 32 (redações 2024/2026); CC 1.829, 2.015; Súmulas 112 e 542 STF; precedente do STJ sobre testamento. Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
Na escritura (ou no requerimento ao tabelião):
- [ ] Nomeação de inventariante (e autorização para alienar bem, com destinação do preço às despesas e garantia, se necessário — art. 11-A).
- [ ] Partilha ou adjudicação (herdeiro único, art. 26).
- [ ] Declaração das partes sobre ITCMD (recolhido, a recolher, isenção ou não incidência) — art. 15 com redação de 2026.
- [ ] Encaminhamento ao MP quando houver incapaz.
- [ ] Registro nos órgãos competentes e levantamento de valores.

## Checklist pré-protocolo
- [ ] Certidão negativa de testamento ou decisão judicial autorizando a escritura.
- [ ] Incapaz: quinhão em fração ideal de todos os bens, sem compensações; parecer do MP.
- [ ] Valores dos bens declarados pelo inventariante (art. 32) e coerentes com a base do fisco estadual.
- [ ] Doações em vida declaradas para colação.
- [ ] Concordância expressa de todos sobre a união estável, se houver companheiro.
- [ ] Orientação escrita ao cliente sobre ITCMD pendente e consequências.

## Erros a evitar
- Atribuir bens inteiros ao incapaz ou compensar quinhões (o art. 12-A exige parte ideal em cada bem).
- Lavrar escritura com testamento sem a autorização judicial prévia.
- Afirmar ao cliente que "não paga mais ITCMD": a Res. 695/2026 só retirou a exigência de pagamento prévio; o imposto continua devido e o fisco é avisado.
- Ignorar exigências do registro de imóveis quanto à prova fiscal [VERIFICAR: posição da corregedoria local após a Res. 695/2026].
- Subavaliar bens (o tabelião pode recusar diante de indícios de fraude, art. 32 §2º).

## Integração com o núcleo
`prazos-processuais` (prazo de abertura e multa estadual), `juros-e-correcao` (ITCMD em atraso, reposições), `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

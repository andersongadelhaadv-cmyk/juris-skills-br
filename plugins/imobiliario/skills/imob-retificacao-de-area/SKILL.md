---
name: imob-retificacao-de-area
description: >
  Prepara requerimento de retificação de registro imobiliário e de área, pela
  via administrativa no Registro de Imóveis (art. 213 da Lei 6.015/1973) ou pela
  via judicial (art. 212), com planta, memorial, anuência ou notificação dos
  confrontantes e tratamento da impugnação. Use quando o usuário pedir para
  corrigir a metragem ou as medidas da matrícula, inserir coordenadas
  georreferenciadas, atualizar confrontações, corrigir erro de transposição do
  título ou dados pessoais na matrícula, ou responder a impugnação de vizinho
  na retificação de área.
metadata:
  area: imobiliario
  tipo_peca: requerimento
  verificado_em: 2026-11-25
---
# Retificação de registro e de área

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: (a) erro de transposição do título, confrontação desatualizada, logradouro renomeado, dados de qualificação (art. 213, I); (b) inserção ou alteração de medida perimetral, com ou sem alteração de área (art. 213, II); (c) retificação judicial quando a via administrativa for inviável ou preferida (art. 212); (d) resposta a impugnação de confrontante.
- Não usar: quando o objetivo real é **adquirir área a mais** do que o título contém — a retificação não serve para isso (AREsp 2.633.317); avalie usucapião (`imob-usucapiao-judicial`, ou extrajudicial, art. 216-A) ou ação própria (`civel-peticao-inicial`); núcleo urbano informal inteiro (`imob-regularizacao-fundiaria-reurb`); disputa de domínio entre vizinhos (reivindicatória/demarcatória, `civel-peticao-inicial`); nulidade do registro por vício do título (art. 214 — ação própria).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Certidão de inteiro teor atualizada da matrícula (e transcrições anteriores, se houver).
2. Título aquisitivo e cadeia dominial que originou a descrição.
3. Qual é o erro: transposição, confrontação, logradouro, medidas, área, coordenadas, qualificação pessoal.
4. Levantamento topográfico: área registrada × área medida, diferença percentual, divisas alcançadas.
5. Imóvel urbano ou rural; se rural, situação do georreferenciamento/certificação.
6. Confrontantes: nomes, matrículas, endereços; quem já assinou a planta.
7. Existência de conflito possessório ou de divisa com algum vizinho.
8. Profissional habilitado responsável (ART/RRT).

## Prazo e contagem
- Confrontante que não assinou a planta é notificado para se manifestar em **15 dias** (art. 213, § 2º); se não encontrado, edital publicado duas vezes, com o mesmo prazo (§ 3º).
- Silêncio no prazo = anuência presumida (§ 4º).
- Impugnação fundamentada: requerente e profissional se manifestam em **5 dias** (§ 5º).
- O art. 1.247 do CC não fixa prazo para pedir a retificação; prazo de pretensões conexas (anulação, indenização) não conferido nesta skill [VERIFICAR via `verificacao-de-citacoes`].
- Prazos processuais da via judicial e do recurso: `prazos-processuais`.

## Estrutura da peça
Requerimento ao Oficial (ou petição ao juízo) → matrícula e título → descrição do erro → enquadramento no inciso do art. 213 → documentos técnicos → confrontantes (anuências e pedidos de notificação) → pedido de averbação. Roteiro em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Via administrativa é a regra** (art. 212, caput), facultada a judicial; a opção administrativa não impede a prestação jurisdicional a pedido do prejudicado (art. 212, parágrafo único).
- **Inciso I** (de ofício ou a requerimento): erros e atualizações que não alteram medidas perimétricas.
- **Inciso II**: exige planta e memorial assinados por profissional habilitado, com ART, **e pelos confrontantes**.
- **Confrontantes relevantes**: só os confinantes das divisas alcançadas pela alteração (§ 16); o § 10 define quem é confrontante (inclusive condomínios e titulares de direitos reais) e exclui credores hipotecários e pignoratícios.
- **Imóvel rural**: em desmembramento, parcelamento, remembramento e em qualquer transferência, a descrição exige memorial georreferenciado com precisão fixada pelo INCRA (art. 176, §§ 3º e 4º).
- **Acréscimo substancial de área**: alto risco de recusa ou extinção sem mérito; documente que a diferença decorre de erro de medição, não de incorporação de área alheia.

## Fundamentos verificados
- Lei 6.015/1973: arts. 176, §§ 3º e 4º; 212; 213 (I, II, §§ 1º a 6º, 10, 16); 214; 216-A.
- CC: arts. 1.245 e 1.247.
- STJ, AREsp 2.633.317 (retificação não serve à ampliação substancial de área).
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Averbação da retificação, com a nova descrição (medidas, área, coordenadas, confrontações).
- Notificação, pelo Oficial, dos confrontantes que não assinaram (pessoal, correio com AR ou RTD); edital para os não encontrados.
- Na via judicial: citação dos confrontantes e interessados, prova pericial se houver controvérsia técnica, expedição de mandado de averbação.
- Se houver impugnação: tentativa de transação; não havendo, remessa ao juiz competente (art. 213, § 6º).

## Checklist pré-protocolo
- [ ] Matrícula de inteiro teor recente e título de origem juntados
- [ ] Erro classificado no inciso I ou II do art. 213
- [ ] Planta e memorial com ART/RRT, assinados pelo profissional
- [ ] Lista completa de confrontantes das divisas alcançadas (§ 16), com anuência ou endereço para notificação
- [ ] Rural: georreferenciamento/certificação verificados
- [ ] Diferença de área explicada tecnicamente (erro de medição, não acréscimo)
- [ ] Sinais de disputa de domínio avaliados antes de escolher a via
- [ ] Emolumentos e custas consultados na tabela local

## Erros a evitar
- Usar a retificação como "usucapião disfarçada" para ganhar área (AREsp 2.633.317).
- Esquecer confrontante titular de direito real ou condomínio (§ 10) — a averbação fica vulnerável.
- Notificar confrontante de divisa não alcançada e deixar de fora quem é afetado (§ 16).
- Insistir na via administrativa quando a impugnação discute propriedade: o juiz remete às vias ordinárias (§ 6º).
- Planta sem ART ou memorial divergente da planta.
- Responsabilidade: descrições falsas responsabilizam requerente e profissional (§ 14).

## Integração com o núcleo
`prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

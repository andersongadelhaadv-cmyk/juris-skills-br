---
name: imob-loteamento-irregular-defesa-do-adquirente
description: >
  Redige a defesa do adquirente de lote em loteamento irregular ou clandestino:
  notificação ao loteador e depósito das prestações (art. 38 da Lei
  6.766/1979), ação de nulidade do compromisso por venda de lote não
  registrado (art. 37) ou de resolução por falta de infraestrutura, com
  restituição integral, e defesa contra cobrança ou rescisão promovida pelo
  loteador (arts. 39 e 46). Use quando o usuário pedir ajuda para quem comprou
  terreno em loteamento sem registro, sem aprovação da prefeitura ou sem
  asfalto, água e luz prometidos, quer parar de pagar com segurança, reaver o
  dinheiro ou se defender de ação do loteador.
metadata:
  area: imobiliario
  tipo_peca: inicial
  verificado_em: 2026-11-25
---
# Loteamento irregular — defesa do adquirente

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: (a) loteamento não registrado no Registro de Imóveis (clandestino); (b) registrado, mas não executado conforme o projeto ou sem notificação/aprovação municipal (irregular); (c) infraestrutura contratada e não entregue; (d) adquirente demandado pelo loteador (cobrança, rescisão, reintegração).
- Não usar: regularização coletiva do núcleo pelo Município ou pela associação (`imob-regularizacao-fundiaria-reurb`); mera interpelação ou constituição em mora (`imob-notificacao-extrajudicial-imobiliaria`); unidade em incorporação de edifício (`imob-incorporacao-imobiliaria`); vício de construção da casa entregue (`consumidor-vicio-do-produto-ou-servico`); contestação genérica (`civel-contestacao`).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Contrato (compromisso, recibo, cessão), datas, preço, parcelas pagas e a vencer (comprovantes).
2. Certidão do Registro de Imóveis: o loteamento está registrado? há matrícula do lote?
3. Certidão ou informação da Prefeitura sobre aprovação do projeto e das obras.
4. O que foi prometido (asfalto, água, energia, esgoto, drenagem) e o que existe; fotos e datas.
5. Quem vendeu: loteador, corretor, empresa do mesmo grupo, particular revendedor.
6. Publicidade e propostas recebidas (afirmações sobre legalidade).
7. Objetivo do cliente: manter o lote e regularizar, ou desfazer e reaver o pagamento.
8. Notificações ou ações já recebidas do loteador; construção feita no lote.

## Prazo e contagem
- Não há prazo legal para o adquirente suspender os pagamentos e notificar o loteador: o art. 38 incide quando constatada a irregularidade.
- Notificação: pessoal ou pelo Registro de Títulos e Documentos; com edital, o prazo começa 10 dias após a última publicação (art. 49).
- Prescrição das pretensões de nulidade, restituição e indenização: não conferida nesta skill [VERIFICAR via `verificacao-de-citacoes`]. Registre data do contrato, de cada pagamento e da ciência da irregularidade.
- Prazos processuais (contestação, recursos): `prazos-processuais`.

## Estrutura da peça
Fatos com tabela de pagamentos → prova da irregularidade (certidões) → enquadramento (clandestino × irregular × inadimplemento de infraestrutura) → caminho escolhido (suspensão/depósito; nulidade; resolução) → responsabilidade do loteador, do grupo e do Município → pedidos. Roteiro em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Foro**: comarca da situação do lote (art. 48).
- **Suspensão e depósito** (art. 38): constatada a falta de registro ou de execução regular, o adquirente suspende o pagamento das prestações restantes e notifica o loteador para suprir a falta; deposita as prestações no Registro de Imóveis, que as recolhe em instituição de crédito, com levantamento só por autorização judicial (§ 1º).
- **Nulidade**: venda ou promessa de lote não registrado é vedada (art. 37); o STJ declara nulo o negócio, mesmo entre particulares e mesmo com ciência do adquirente, com retorno ao estado anterior (REsp 2.166.273).
- **Resolução por inadimplemento do loteador**: falta de infraestrutura contratada autoriza a resolução com restituição integral, ainda que a escritura já esteja registrada (REsp 2.172.231; Súmula 543/STJ).
- **Cláusula de rescisão por inadimplemento do adquirente é nula** se o loteamento não está regularmente inscrito (art. 39).
- **Loteador sem registros não tem ação nem defesa** fundada na Lei 6.766 (art. 46).
- **Grupo econômico**: responde solidariamente quem dele se beneficiou (art. 47).
- **Município**: pode regularizar e usar os depósitos (art. 40); o STJ reconhece seu poder-dever de regularizar (AgInt no AREsp 1.762.074).
- **Crime**: vender lote de parcelamento não registrado é forma qualificada do crime do art. 50 (parágrafo único, I) — avaliar representação, sem usá-la como ameaça na negociação.

## Fundamentos verificados
- Lei 6.766/1979: arts. 32, 37, 38, 39, 40, 46, 47, 48, 49 e 50.
- STJ: REsp 2.166.273; REsp 2.172.231; AgInt no AREsp 1.762.074; Súmula 543.
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Tutela de urgência para autorizar a suspensão dos pagamentos e o depósito (art. 38), e para impedir negativação, cobrança ou reintegração.
- Declaração de nulidade do compromisso (art. 37) **ou** resolução por inadimplemento do loteador.
- Restituição integral dos valores pagos, corrigidos; juros e correção pelo núcleo `juros-e-correcao`.
- Indenização por benfeitorias e prejuízos comprovados; dano moral só se houver fato concreto além do descumprimento.
- Inclusão das pessoas do grupo econômico beneficiárias (art. 47).
- Alternativa, se o cliente quer ficar com o lote: obrigação de fazer (registro e obras), com prazo e multa, e depósito das prestações até a regularização.
- Na defesa: improcedência da cobrança ou rescisão (arts. 39 e 46) e reconvenção (`civel-reconvencao`).

## Checklist pré-protocolo
- [ ] Certidão do Registro de Imóveis e informação da Prefeitura juntadas
- [ ] Enquadramento definido: clandestino, irregular ou inadimplemento de infraestrutura
- [ ] Objetivo do cliente definido (manter × desfazer) e pedidos coerentes
- [ ] Tabela de pagamentos com comprovantes
- [ ] Polo passivo: loteador, vendedor, empresas do grupo (art. 47); Município se for o caso
- [ ] Notificação do art. 38 feita ou requerida
- [ ] Prescrição verificada
- [ ] Juros e correção remetidos ao núcleo

## Erros a evitar
- Simplesmente parar de pagar sem notificar e sem depositar — expõe o cliente à mora.
- Pedir nulidade e, ao mesmo tempo, obrigação de entregar o lote regularizado, sem ordem de subsidiariedade.
- Aceitar a tese do loteador de que o registro da escritura impede a resolução (afastada no REsp 2.172.231).
- Aceitar retenção de valores em favor do loteador inadimplente (Súmula 543: restituição integral se a culpa é do vendedor).
- Deixar de alegar o art. 46 na contestação a ação do loteador sem registros.
- Usar índice ou taxa de juros sem o núcleo `juros-e-correcao`.

## Integração com o núcleo
`juros-e-correcao`, `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

---
name: banc-renegociacao-extrajudicial-de-divida
description: >
  Prepara a proposta de renegociação extrajudicial de dívida bancária e
  revisa ou redige o termo de acordo (transação, novação ou confissão de
  dívida com novo plano), com controle de ressalvas, garantias, fiadores,
  quitação antecipada com redução de juros (CDC, art. 52, § 2º), baixa de
  negativação e da ação em curso. Use quando o usuário pedir para propor
  acordo ao banco, contraproposta de renegociação, carta de proposta de
  pagamento à vista com desconto, revisar o termo de acordo ou confissão de
  dívida que o banco mandou assinar, quitação de financiamento com desconto,
  ou acordo para encerrar busca e apreensão ou execução.
metadata:
  area: bancario
  tipo_peca: contrato
  verificado_em: 2026-11-25
---
# Renegociação extrajudicial de dívida bancária (proposta e acordo)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: (a) carta de proposta ao banco (à vista com desconto, parcelamento, carência, alongamento); (b) contraproposta; (c) revisão do termo de renegociação, confissão de dívida ou "acordo" oferecido pelo banco ou por assessoria de cobrança; (d) minuta de acordo para encerrar ação em curso (busca e apreensão, execução, revisional), com homologação.
- Não usar:
  - Vários credores e comprometimento do mínimo existencial → `consumidor-superendividamento` (repactuação judicial ou no Procon).
  - Discussão judicial de cláusulas → `consumidor-contratos-bancarios-revisional`.
  - Depósito por recusa do banco em receber → `banc-consignacao-e-purgacao-da-mora`.
  - Defesa em processo já ajuizado → `banc-busca-e-apreensao-contestacao` ou `banc-defesa-execucao-alienacao-fiduciaria`.
  - Acordo com empresa não financeira → `contratos-notificacao-de-descumprimento` ou `contratos-aditivo-contratual`.
  - Acordo trabalhista → `trabalhista-acordo-extrajudicial`.

## Entradas mínimas (perguntar o que faltar; nunca supor fatos)
1. Contratos envolvidos (número, modalidade, garantia), saldo informado pelo banco e data da posição.
2. Capacidade real de pagamento: valor à vista disponível ou parcela máxima mensal sem comprometer o sustento.
3. Situação: atraso desde quando, negativação, protesto, ação ajuizada (número do processo, fase).
4. Garantias e garantidores: alienação fiduciária, avalista, fiador, cônjuge que assinou.
5. Há suspeita de encargo abusivo, tarifa, seguro embutido ou venda casada que o cliente quer discutir depois?
6. Proposta já recebida do banco (texto integral, não só o valor).
7. Objetivo: quitar, reduzir parcela, recuperar o bem, limpar o nome, encerrar a ação.

## Prazo e contagem
- Proposta e acordo não têm prazo legal próprio; atenção aos prazos que **correm em paralelo** e não se suspendem pela negociação: 5 dias de pagamento integral e 15 de resposta na busca e apreensão (DL 911, art. 3º), prazos de embargos, purgação no imóvel. Negociar **sem perder prazo**: `prazos-processuais`.
- Fixe no termo: data-limite para aceitar, vencimento das parcelas, prazo para baixa da negativação e para o protocolo do pedido de homologação/extinção.

## Estrutura do documento
Proposta: identificação → contratos e saldo → situação do devedor (sem confissões desnecessárias) → proposta objetiva → condições (baixa, extinção da ação, devolução do bem) → validade → ressalva de direitos. Acordo: partes → objeto → valor e forma → efeitos sobre contratos e garantias → negativação e processos → inadimplemento → ressalvas → foro e assinaturas. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e cuidados
- **Transação** é concessão recíproca para prevenir ou terminar litígio (CC, art. 840), só sobre direitos patrimoniais privados (art. 841), interpretada **restritivamente** (art. 843). Se o direito já está em juízo, a forma é escritura pública ou termo nos autos homologado (art. 842).
- **Fiador:** transação entre credor e devedor desobriga o fiador (CC, art. 844, § 1º). Se o banco quer manter garantidor, ele precisa assinar; se o cliente é o garantidor, isso é argumento.
- **Novação** exige ânimo de novar, expresso ou tácito inequívoco; sem ele, a segunda obrigação só confirma a primeira (CC, arts. 360 e 361). Novação extingue garantias e acessórios, salvo estipulação em contrário (art. 364) — leia a cláusula que "mantém todas as garantias".
- **Ressalva de ilegalidades anteriores:** a renegociação ou confissão de dívida não impede discutir ilegalidades dos contratos anteriores (Súmula 286/STJ). Mesmo assim, recuse cláusula de renúncia ampla e inclua ressalva expressa quando o cliente quiser discutir depois.
- **Quitação antecipada:** consumidor tem direito à liquidação antecipada, total ou parcial, com redução proporcional dos juros e acréscimos (CDC, art. 52, § 2º; art. 54-B, V). Use isso como piso da proposta à vista.
- **Boa-fé** na negociação e na execução do acordo (CC, art. 422).
- Superendividado pessoa natural pode levar a conciliação ao Procon ou outro órgão do SNDC (CDC, art. 104-C), cujo acordo deve prever data de exclusão dos cadastros.

## Fundamentos verificados
- CC, arts. 360, 361, 364, 422, 840, 841, 842, 843 e 844.
- CDC, arts. 52 (§ 2º), 54-B e 104-C.
- Súmula 286/STJ.
Detalhe em [fundamentos](references/fundamentos.md).

## Cláusulas essenciais (acordo)
- Identificação de **todos** os contratos abrangidos e do saldo considerado, com data da posição.
- Valor, número e vencimento das parcelas; meio de pagamento; o que acontece com pagamento em atraso (tolerância, multa) — sem vencimento antecipado por atraso mínimo.
- Natureza: transação/novação ou simples parcelamento; destino das garantias (liberação de gravame após quitação, com prazo).
- Baixa da negativação e do protesto em prazo certo após o pagamento da 1ª parcela ou à vista.
- Processo em curso: pedido conjunto de homologação/extinção, custas e honorários de cada parte, levantamento de constrição, devolução do bem apreendido.
- Ressalva expressa de direitos (Súmula 286) ou, se a quitação for ampla, que seja **recíproca**.
- Quitação plena ao final, com termo de quitação e liberação do gravame.
- Juros e correção de eventual parcelamento: conferir pelo núcleo `juros-e-correcao`; não fixar taxa aqui.

## Checklist antes de enviar ou assinar
- [ ] Prazos processuais paralelos anotados e protegidos
- [ ] Parcela cabe no orçamento declarado pelo cliente
- [ ] Todos os contratos e o saldo identificados
- [ ] Garantias e garantidores tratados (art. 844, § 1º; art. 364)
- [ ] Cláusula de renúncia ampla retirada ou neutralizada por ressalva
- [ ] Baixa de negativação, liberação de gravame e extinção da ação com prazos
- [ ] Consequência do atraso proporcional
- [ ] Assinatura de quem tem poderes pelo banco

## Erros a evitar
- Deixar correr o prazo de 5 dias da busca e apreensão ou de embargos esperando resposta do banco.
- Assinar confissão de dívida com renúncia genérica a "qualquer discussão" sem ressalva.
- Acordo sem prazo de baixa da negativação ou de liberação do gravame.
- Esquecer o processo: acordo extrajudicial sem pedido de homologação deixa a ação andando.
- Confissões factuais na proposta ("reconheço dever R$ X") quando ainda há tese de abusividade.
- Prometer ao cliente desconto certo: a aceitação é do banco.

## Integração com o núcleo
`prazos-processuais`, `juros-e-correcao`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

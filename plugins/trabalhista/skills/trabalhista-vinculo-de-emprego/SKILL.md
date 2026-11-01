---
name: trabalhista-vinculo-de-emprego
description: >
  Estrutura o pedido (ou a defesa) de reconhecimento de vínculo de emprego pelos
  requisitos do art. 3º da CLT — pessoa física, pessoalidade, não eventualidade,
  subordinação e onerosidade — incluindo pejotização, falso autônomo (art. 442-B)
  e terceirização (Tema 725 do STF). Use quando o usuário pedir reconhecimento de
  vínculo, vínculo empregatício, pejotização, contrato de PJ fraudulento, falso
  autônomo, registro em carteira, anotação da CTPS, ou defesa da empresa contra
  pedido de vínculo.
metadata:
  area: trabalhista
  tipo_peca: inicial
  verificado_em: 2026-11-01
---
# Reconhecimento de vínculo de emprego

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: trabalho sem registro, contratação como PJ, MEI, autônomo, cooperado ou estagiário em desvio; terceirização com subordinação direta ao tomador. Serve à inicial (com `trabalhista-reclamacao`) e à contestação (com `trabalhista-contestacao`).
- Não usar sozinha para relações com a Administração Pública: contratação irregular não gera vínculo com ente público (Súmula 331 II do TST; CF art. 37 II).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
- Período, função, local, jornada, forma e valor do pagamento.
- Quem dava ordens, quem controlava horário, metas, punições; possibilidade de se fazer substituir.
- Contrato escrito (PJ, prestação de serviços, parceria), notas fiscais, e-mails, mensagens, crachá, uniforme, e-mail corporativo.
- Se havia exclusividade e se o trabalhador tinha outros clientes.
- Para a defesa: autonomia real (vários clientes, preço próprio, assunção de riscos, estrutura própria).

## Prazo e contagem
- Prescrição: bienal e quinquenal sobre os créditos (CLT art. 11; CF art. 7º XXIX). O pedido declaratório para anotação com fins previdenciários não prescreve (art. 11 §1º).

## Estrutura da peça
Tópico "Do vínculo de emprego": fatos que revelam cada requisito do art. 3º, a fraude ao contrato formal (art. 9º) e o pedido declaratório; depois as verbas do período. Roteiro em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Requisitos** (arts. 2º e 3º): pessoa física, pessoalidade, não eventualidade, subordinação, onerosidade. Demonstrar cada um com fato e prova.
- **Primazia da realidade e nulidade**: atos que desvirtuam a CLT são nulos (art. 9º).
- **Autônomo** (art. 442-B): cumpridas as formalidades, a contratação de autônomo afasta a condição de empregado; o debate é sobre a realidade da autonomia.
- **Terceirização**: lícita em qualquer atividade, com responsabilidade subsidiária da contratante (Tema 725 do STF). Vínculo direto com o tomador só se demonstrada subordinação e pessoalidade diretas. O item I da Súmula 331 foi cancelado; usar os itens vigentes (II a VI) e conferir no site do TST.
- **Pejotização no STF**: há discussão no STF sobre a licitude da contratação por pessoa jurídica e a competência da Justiça do Trabalho, com possível suspensão de processos. O Tema 1389 não foi localizado no JuriBase [VERIFICAR existência, tese e eventual ordem de suspensão no portal do STF antes de ajuizar ou contestar].
- **Ônus**: negada a prestação de serviços, é do reclamante; admitida a prestação e alegada outra natureza, passa ao réu (art. 818 II). Fim do contrato: Súmula 212 do TST.
- **Ente público tomador**: responsabilidade subsidiária depende de prova de conduta negligente, sem inversão automática do ônus (Tema 1118 do STF; Súmula 331 V do TST).

## Fundamentos verificados
CLT arts. 2º, 3º, 9º, 11, 442-B, 818; CF art. 7º XXIX; Súmulas 212 e 331 do TST; Temas 725 e 1118 do STF. Detalhes em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Declaração do vínculo (datas, função, salário) e anotação da CTPS.
- Verbas do período: 13º, férias + 1/3, FGTS, verbas rescisórias, multas dos arts. 467 e 477 §8º, recolhimentos previdenciários.
- Responsabilidade do tomador (subsidiária ou solidária) com fundamento específico.
- Correção e juros conforme `juros-e-correcao`.

## Checklist pré-protocolo
- [ ] Cada requisito do art. 3º com fato concreto e prova.
- [ ] Contrato formal analisado e fraude explicada.
- [ ] Situação do tema de pejotização no STF verificada na data.
- [ ] Ente público no polo: cabimento e ônus revistos à luz do Tema 1118.
- [ ] Pedidos liquidados.

## Erros a evitar
- Narrar "trabalhava como empregado" sem fatos de subordinação.
- Citar o item I da Súmula 331 (cancelado).
- Pedir vínculo direto com ente público.
- Ignorar decisão do STF que suspenda processos sobre pejotização.

## Integração com o núcleo
`verificacao-de-citacoes` (obrigatória para o tema do STF), `juros-e-correcao`, `prazos-processuais`, `fidelidade-factual`, `estilo-forense`.

---
name: familia-guarda-e-convivencia
description: >
  Redige ação de guarda e de regulamentação de convivência (visitas), modificação de guarda
  e incidente de alienação parental (CC arts. 1.583 a 1.590; Lei 12.318/2010 com as
  alterações da Lei 14.340/2022; Lei 14.713/2023 sobre violência doméstica). Use quando o
  usuário pedir guarda compartilhada, guarda unilateral, regulamentação de visitas,
  convivência, modificação de guarda, busca e apreensão de menor, alienação parental,
  mudança de cidade com o filho.
metadata:
  area: familia-sucessoes
  tipo_peca: inicial
  verificado_em: 2026-11-01
---
# Guarda e convivência

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: fixação ou modificação de guarda; plano de convivência; ampliação/restrição de convivência; alienação parental (ação autônoma ou incidental); convivência de avós (CC 1.589 p.ú.).
- Não usar: alimentos isolados (use `familia-acao-de-alimentos`); medidas protetivas da Lei Maria da Penha (via criminal/juizado de violência doméstica); destituição do poder familiar e adoção (ECA, fora do escopo).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Filhos: nomes, idades, escola, rotina, saúde, necessidades especiais.
2. Situação atual: com quem residem, como tem sido a convivência, acordos informais.
3. Proposta concreta: base de moradia, calendário (semanas, fins de semana, férias, feriados, datas comemorativas), logística de entrega.
4. Histórico de violência doméstica ou familiar (boletins, medidas protetivas, processos) — pergunta obrigatória.
5. Atos de alienação parental, se alegados, com provas (mensagens, faltas a visitas, relatórios escolares).
6. Mudança de domicílio pretendida ou ocorrida.

## Prazo e contagem
- Em ações de guarda, antes da audiência de mediação o juiz pergunta às partes e ao MP sobre risco de violência doméstica e dá 5 dias para apresentar prova ou indícios (CPC 699-A). Preparar essa prova antes.
- Perícia de alienação parental: laudo em 90 dias, prorrogável só por decisão justificada (Lei 12.318 art. 5º §3º).
- Demais prazos pelo procedimento das ações de família (CPC 693 e seguintes); contagem via `prazos-processuais`.

## Estrutura da peça
Endereçamento → qualificação → filhos e rotina → situação atual → direito (melhor interesse, guarda compartilhada como regra, exceções) → plano de convivência → tutela provisória → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Competência: foro do domicílio de quem detém a guarda (Súmula 383 STJ).
- Guarda compartilhada é a regra mesmo sem acordo, salvo se um genitor declarar que não a deseja ou houver elementos de probabilidade de risco de violência doméstica ou familiar (CC 1.584 §2º, redação da Lei 14.713/2023).
- Guarda compartilhada não é divisão matemática de tempo: tempo "equilibrado", com cidade-base que melhor atenda aos filhos (CC 1.583 §§2º e 3º).
- Liminar de guarda preferencialmente após ouvir ambas as partes (CC 1.585).
- Depoimento da criança: com especialista (CPC 699) e, em alienação parental, obrigatoriamente pela Lei 13.431/2017, sob pena de nulidade (Lei 12.318 art. 8º-A).
- MP intervém (incapaz).

## Fundamentos verificados
CC 1.583 a 1.590; CPC 699 e 699-A; Lei 12.318 arts. 2º, 4º, 5º, 6º e 8º-A; Lei 14.713/2023; Lei 14.340/2022; Súmula 383 STJ. Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- [ ] Guarda (compartilhada ou, justificadamente, unilateral) com base de moradia definida.
- [ ] Plano de convivência detalhado (anexo).
- [ ] Tutela provisória de guarda/convivência; em alienação parental, medidas provisórias urgentes e convivência assistida mínima (Lei 12.318 art. 4º).
- [ ] Estudo psicossocial ou perícia biopsicossocial (Lei 12.318 art. 5º; CC 1.584 §3º).
- [ ] Medidas do art. 6º da Lei 12.318, conforme a gravidade (advertência, ampliação da convivência, multa, acompanhamento, alteração da guarda, fixação cautelar de domicílio, inversão da obrigação de levar e buscar).
- [ ] Direito de informação perante escolas e serviços de saúde (CC 1.583 §5º e 1.584 §6º).
- [ ] Intimação do MP; segredo de justiça.

## Checklist pré-protocolo
- [ ] Pergunta sobre violência doméstica feita ao cliente e resposta registrada; provas reunidas para os 5 dias do CPC 699-A.
- [ ] Plano de convivência com calendário completo e regras de comunicação.
- [ ] Prova da rotina (escola, saúde, atividades).
- [ ] Alegação de alienação parental apoiada em fatos concretos e datados, não em rótulos.
- [ ] Pedido de escuta especializada, se a oitiva da criança for necessária.

## Erros a evitar
- Pedir guarda unilateral só por desentendimento entre os pais (não é exceção legal).
- Ignorar a regra da Lei 14.713/2023: com indícios de violência, a guarda compartilhada não é aplicada; sem indícios, não use a alegação como estratégia.
- Pedir suspensão da autoridade parental com base na Lei 12.318: o inciso VII do art. 6º foi revogado pela Lei 14.340/2022.
- Pedir oitiva da criança em audiência comum.
- Plano vago ("visitas livres") que gera novos litígios.

## Integração com o núcleo
`prazos-processuais`, `verificacao-de-citacoes` (julgados sobre guarda compartilhada à distância, alienação parental), `fidelidade-factual` (fatos sensíveis e datas), `estilo-forense`; `juros-e-correcao` só se houver multa ou alimentos cumulados.

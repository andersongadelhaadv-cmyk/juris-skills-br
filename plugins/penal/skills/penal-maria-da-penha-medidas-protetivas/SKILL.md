---
name: penal-maria-da-penha-medidas-protetivas
description: >
  Redige pedido de medidas protetivas de urgência em favor da ofendida e, do lado
  do requerido, manifestação, pedido de revogação ou modulação e defesa no crime
  de descumprimento (Lei 11.340/2006, arts. 18 a 24-A, com as Leis 14.550/2023,
  14.994/2024, 15.383/2026 e 15.412/2026). Use quando o usuário pedir medida
  protetiva, MPU, afastamento do lar, proibição de contato, monitoração do
  agressor, revogação de medida protetiva, defesa do requerido ou art. 24-A.
metadata:
  area: penal
  tipo_peca: requerimento
  verificado_em: 2026-11-01
---
# Medidas protetivas da Lei Maria da Penha (ofendida e requerido)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Ofendida: pedido de MPU (arts. 18, 19, 22, 23 e 24), inclusive monitoração eletrônica do agressor (22, VIII), alimentos provisórios, afastamento do lar.
- Requerido: manifestação após a concessão (contraditório diferido), pedido de revogação ou modulação por ausência de risco, ajuste de visitas e alimentos, defesa na ação penal pelo art. 24-A.
- Não usar: divórcio, guarda e partilha (plugin de família); prisão preventiva do agressor (ver `penal-liberdade-provisoria-e-relaxamento`).
- Conflito de interesses: o mesmo advogado não pode atuar para os dois polos.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Relação entre as partes (art. 5º: unidade doméstica, família, relação íntima de afeto — não exige coabitação, Súmula 600 STJ).
2. Fatos de violência (física, psicológica, sexual, patrimonial, moral, vicária — art. 7º), datas, provas (mensagens, laudos, testemunhas).
3. Filhos, dependentes, armas, bens comuns, dependência econômica.
4. Para o requerido: decisão concedida, medidas impostas, data da intimação, fatos posteriores que mostram cessação do risco, contatos iniciados pela ofendida, necessidades de trabalho e convivência com filhos.

## Prazo e contagem
- Juiz decide em 48 h do recebimento do expediente (art. 18).
- MPU vigora enquanto persistir o risco, sem prazo predeterminado (art. 19 §6º; STJ Tema 1249).
- Recursos e prazos penais: contínuos (CPP 798); a suspensão de 20/12 a 20/01 NÃO alcança procedimentos da Lei Maria da Penha (CPP 798-A, II). Use `prazos-processuais`.

## Estrutura da peça
Resumo (detalhe em [estrutura](references/estrutura.md)): (A) ofendida — qualificação, relação, fatos, risco, medidas pedidas e fundamento de cada uma; (B) requerido — síntese da decisão, contraditório, inexistência ou cessação do risco, proporcionalidade, pedidos de revogação ou modulação.

## Requisitos e preliminares
- Concessão em cognição sumária, com base no depoimento à polícia ou em alegações escritas; indeferimento só se avaliada a inexistência de risco (art. 19 §4º).
- Independem de tipificação penal, ação penal, inquérito ou boletim de ocorrência (19 §5º).
- MPU tem natureza de tutela inibitória; revogação exige contraditório com oitiva da vítima e do requerido (STJ Tema 1249, tese IV). Iniciativa de revisão cabe a quem está obrigado (o requerido).
- Monitoração eletrônica (22, VIII; Lei 15.383/2026): prioridade quando houver descumprimento anterior ou risco iminente; a decisão que a negar nesses casos deve fundamentar expressamente (22 §§6º e 9º).
- Medidas cíveis, inclusive alimentos, constituem título executivo judicial, sem ação principal (22 §10, Lei 15.412/2026).
- Descumprimento (24-A): reclusão de 2 a 5 anos e multa (Lei 14.994/2024); aumento de 1/3 até metade se violadas áreas de exclusão monitoradas ou o dispositivo (§4º, Lei 15.383/2026); fiança só pelo juiz (§2º). Independe da competência civil ou criminal de quem deferiu (§1º).
- Na esfera penal: ação pública incondicionada na lesão corporal (Súmula 542 STJ); sem transação ou suspensão do processo (Súmula 536 STJ); sem insignificância (Súmula 589 STJ); sem substituição por restritiva em crime com violência ou grave ameaça (Súmula 588 STJ); ANPP vedado (CPP 28-A §2º, IV).

## Fundamentos verificados
Resumo (detalhe em [fundamentos](references/fundamentos.md)): Lei 11.340, arts. 5º, 7º, 12-C, 18 a 24-A; CPP 313, III; 798-A; Súmulas 536, 542, 588, 589, 600 STJ; STJ Tema 1249; precedentes do STJ sobre oitiva prévia da vítima.

## Pedidos e requerimentos
- Ofendida: medidas do art. 22 (I a VIII) e dos arts. 23 e 24, com indicação de distância mínima, meios de contato proibidos, alimentos, guarda provisória de animais/bens; comunicação à polícia e ao órgão de armas; inclusão em programa de proteção.
- Requerido: revogação por ausência ou cessação do risco; subsidiariamente, modulação (redução de distância, regime de visitas por terceiros, autorização de contato para assuntos dos filhos por meio indicado); designação de audiência com oitiva da ofendida; esclarecimento dos limites das medidas para evitar descumprimento involuntário.

## Checklist pré-protocolo
- [ ] Relação do art. 5º descrita com fatos.
- [ ] Cada medida pedida ligada a um risco concreto.
- [ ] Para o requerido: data da intimação, cumprimento integral das medidas até aqui, provas de cessação do risco.
- [ ] Pedido de oitiva da ofendida antes da revogação (Tema 1249).
- [ ] Ausência de conflito de interesses confirmada.
- [ ] Precedentes adicionais conferidos em `verificacao-de-citacoes`.

## Erros a evitar
- Pedir prazo certo de validade (a lei e o Tema 1249 afastam prazo predeterminado).
- Orientar o requerido a "resolver" contatando a ofendida: o contato pode configurar o art. 24-A. O STJ admite atipicidade quando o consentimento da vítima é incontroverso (6ª Turma, AgRg no REsp 2.216.609), mas também afirma a natureza formal do crime e a irrelevância da reaproximação sem revogação judicial da medida (5ª Turma, AgRg no REsp 2.279.947). O caminho seguro é pedir a revogação ou modulação da medida ao juiz (ver fundamentos).
- Tratar o 24-A como crime de menor potencial ofensivo: a pena é de 2 a 5 anos.
- Esquecer que alimentos fixados na MPU já são título executivo (22 §10).

## Integração com o núcleo
- `prazos-processuais`: 48 h; prazos penais contínuos; exceção do 798-A.
- `juros-e-correcao`: atualização de alimentos provisórios executados — aplicar o núcleo, nunca índice próprio.
- `verificacao-de-citacoes`, `fidelidade-factual` (narrativa sensível, sem exageros), `estilo-forense`.

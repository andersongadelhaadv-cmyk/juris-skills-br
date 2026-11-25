---
name: trabalhista-dano-existencial
description: >
  Estrutura o pedido (ou a defesa) de indenização por dano existencial decorrente
  de jornada exaustiva, com base no art. 223-B da CLT (ofensa à esfera
  existencial), nos limites de jornada (CF art. 7º, XIII; CLT arts. 58, 59 e 71)
  e na exigência do TST de prova concreta do prejuízo à vida pessoal, familiar e
  social. Use quando o usuário pedir indenização por jornada excessiva, horas
  extras habituais em excesso, trabalho sem folga ou sem férias, privação do
  convívio familiar e do lazer, ou defesa da empresa contra pedido de dano
  existencial.
metadata:
  area: trabalhista
  tipo_peca: inicial
  verificado_em: 2026-11-25
---
# Dano existencial (jornada exaustiva)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: jornada habitualmente muito acima dos limites legais (ou supressão sistemática de folgas, intervalos e férias) que comprovadamente impediu o trabalhador de conviver, descansar, estudar ou cuidar da saúde. Entra como tópico de `trabalhista-reclamacao`, junto do pedido de horas extras.
- Defesa da empresa: `trabalhista-contestacao` + o roteiro de defesa em [estrutura](references/estrutura.md).
- Não usar quando: a única base é a quantidade de horas extras, sem fato concreto de prejuízo à vida fora do trabalho (a tese tende a ser rejeitada — ver Fundamentos); o abuso é pessoal e humilhante (`trabalhista-assedio-moral-e-sexual`); houve adoecimento com nexo e pedido de pensão ou estabilidade (`trabalhista-acidente-e-doenca-ocupacional`).
- Trabalho em condição análoga à de escravo (jornada exaustiva como elemento do tipo penal): plugin `penal` e órgãos de fiscalização; aqui só o reflexo indenizatório.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Jornada real: horário de entrada e saída, intervalos, dias trabalhados por semana, período em que isso durou.
2. Prova da jornada: cartões de ponto, registros de sistema, e-mails e mensagens fora do horário, relatórios, rastreamento, testemunhas.
3. Folgas, feriados e férias: gozadas ou não; vendidas por imposição?
4. **Prejuízo concreto fora do trabalho** (decisivo): curso abandonado, ausência em eventos familiares, rompimento afetivo, impossibilidade de tratamento de saúde, filhos sem convívio — e como provar (documentos, testemunhas que não sejam só colegas).
5. Regime de jornada contratado (controle de ponto, banco de horas, cargo de confiança, trabalho externo, teletrabalho).
6. Contrato ativo ou extinto, datas e último salário contratual.

## Prazo e contagem
- Prescrição: cinco anos, até dois anos após a extinção (CF art. 7º, XXIX). O período indenizável fica limitado ao quinquênio não prescrito.
- Limite constitucional semanal: o art. 7º, XIII, da CF passou a fixar 40 horas semanais (EC 141/2026). Para contratos que atravessam a mudança, separar os períodos [VERIFICAR: data de vigência e eventual regra de transição da EC 141/2026].
- Prazos processuais: `prazos-processuais`.

## Estrutura da peça
Jornada e prova → excesso em relação aos limites (diário, semanal, intervalos, folgas) → fatos concretos de privação da vida pessoal → nexo entre a jornada e a privação → dano existencial distinto do dano moral → quantificação. Roteiro em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Base legal do dano**: o art. 223-B da CLT inclui expressamente a ofensa à esfera existencial entre os danos extrapatrimoniais.
- **Excesso de jornada**: duração normal de 8 horas diárias (CLT art. 58) e o limite semanal constitucional (CF art. 7º, XIII); horas extras limitadas a duas por dia (CLT art. 59); intervalo mínimo de 1 hora em jornada acima de 6 horas (CLT art. 71).
- **Prova do prejuízo**: a jurisprudência do TST (inclusive da SBDI-1, segundo os acórdãos de turma consultados) é de que a jornada extenuante, por si só, não gera dano existencial; exige-se demonstração efetiva do prejuízo ao convívio familiar e social. Construir a petição em torno desse ponto.
- **Exceções de jornada**: se a empresa alegar cargo de gestão, trabalho externo ou teletrabalho por produção (CLT art. 62), atacar primeiro o enquadramento — sem ele, a jornada e o excesso ficam fora do debate.
- **Ônus da prova**: jornada pelo controle de ponto e regras próprias (ver `trabalhista-reclamacao`); prejuízo existencial é ônus do autor (CLT art. 818, I).

## Fundamentos verificados
CF art. 7º, XIII (redação da EC 141/2026) e XXIX; CLT arts. 58, 59, 62, 71, 223-B, 223-G, 818 e 840 § 1º; ADIs 6050, 6069 e 6082 (critérios do art. 223-G orientativos), na ementa transcrita pelo TST; acórdãos do TST de 2026 exigindo prova do dano existencial. Detalhes em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Indenização por dano existencial em pedido próprio, com valor fundamentado nos critérios do art. 223-G e sem tratar a faixa do § 1º como teto.
- Horas extras, intervalos, repousos e reflexos em pedidos separados (o dano existencial não substitui a remuneração do trabalho extraordinário).
- Se houver também humilhação ou exposição, dano moral em pedido distinto, com causa de pedir distinta, para evitar alegação de bis in idem.
- Exibição dos controles de jornada e registros eletrônicos.
- Valores liquidados (art. 840 § 1º); correção e juros pelo núcleo `juros-e-correcao`.

## Checklist pré-protocolo
- [ ] Jornada descrita com horários e período, e prova de cada elemento.
- [ ] Pelo menos um fato concreto de privação da vida fora do trabalho, com prova própria.
- [ ] Testemunha que conheça a vida pessoal do autor (não apenas a jornada).
- [ ] Enquadramento em exceção do art. 62 enfrentado, se previsível.
- [ ] Períodos antes e depois da EC 141/2026 separados, se for o caso.
- [ ] Dano existencial e dano moral com causas de pedir distintas.
- [ ] Prescrição conferida; pedidos liquidados; juros e correção remetidos ao núcleo.

## Erros a evitar
- Pedir dano existencial só com base no número de horas extras ("dano in re ipsa"): tende a ser rejeitado.
- Usar apenas colegas de trabalho como testemunhas da vida familiar.
- Misturar dano existencial e dano moral no mesmo pedido, com a mesma causa.
- Na defesa, discutir só o valor e deixar sem impugnação a jornada alegada.

## Integração com o núcleo
`juros-e-correcao`, `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

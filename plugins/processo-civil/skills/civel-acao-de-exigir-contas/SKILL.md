---
name: civel-acao-de-exigir-contas
description: >
  Redige a ação de exigir contas (CPC, arts. 550 a 553) nas duas fases — a
  primeira, sobre o dever de prestar, e a segunda, de julgamento das contas e
  apuração do saldo como título executivo —, além da impugnação específica às
  contas e da defesa do réu. Use quando o usuário pedir prestação de contas de
  mandatário, procurador, sócio administrador, administrador de bens, gestor de
  negócios, banco em conta-corrente, credor fiduciário após leilão, inventariante
  ou outro administrador de bens alheios, ou quiser cobrar o saldo apurado.
metadata:
  area: processo-civil
  tipo_peca: inicial
  verificado_em: 2026-11-25
---
# Ação de exigir contas (CPC, arts. 550 a 553)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: há **administração ou gestão de bens, valores ou interesses alheios** e o autor afirma o direito de exigir que o gestor demonstre receitas, despesas e saldo.
- Hipóteses típicas: mandato e procuração (inclusive advogado que levantou valores do cliente); sócio administrador perante o sócio; administrador de bens em condomínio comum; correntista perante o banco (Súmula 259/STJ); devedor fiduciário quanto ao produto do leilão do imóvel e à evolução do débito.
- Não usar:
  - condomínio edilício contra síndico ou administradora: `imob-prestacao-de-contas-de-condominio`;
  - contas de inventariante, tutor, curador, depositário ou outro administrador nomeado em juízo: prestadas **em apenso** ao processo da nomeação (art. 553) — `sucessoes-inventario-judicial`;
  - contrato de mútuo ou financiamento comum, sem gestão de bens alheios (Tema 528/STJ, ver Fundamentos): `consumidor-contratos-bancarios-revisional`;
  - revisão de cláusulas de contrato bancário (a ação de contas não serve para isso);
  - mera obtenção de documentos, sem apuração de saldo: `civel-producao-antecipada-de-provas`.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Relação jurídica que gera o dever de prestar contas (contrato, procuração, contrato social, conta-corrente) e documento.
2. Período a ser abrangido e bens/valores administrados.
3. **Pedido extrajudicial de contas** feito antes, data, meio e resposta (recusa, silêncio, contas insuficientes) — base do interesse de agir.
4. Lançamentos ou fatos concretos que geram dúvida (extratos, recibos, valores levantados, tarifas).
5. Se já há contas prestadas extrajudicialmente: por que são inadequadas.
6. Estimativa do saldo pretendido, se houver.

## Prazo e contagem
- Réu citado para **prestar as contas ou contestar em 15 dias** (art. 550, caput).
- Prestadas as contas, o autor tem **15 dias** para se manifestar (art. 550, § 2º).
- Procedente a primeira fase, o réu presta contas em **15 dias**, sob pena de não poder impugnar as que o autor apresentar; se não prestar, o autor as apresenta em **15 dias** (art. 550, §§ 5º e 6º).
- Prescrição da pretensão de exigir contas: depende da relação de base [VERIFICAR: prazo aplicável via `verificacao-de-citacoes`]. A decadência do art. 26 do CDC não se aplica às contas sobre tarifas e encargos bancários (Súmula 477/STJ).
- Contagem: `prazos-processuais`.

## Estrutura da peça
Endereçamento → qualificação → relação jurídica e dever de prestar contas → período e objeto → razões detalhadas da exigência, com documentos (art. 550, § 1º) → interesse de agir (pedido prévio não atendido ou contas rejeitadas) → pedidos da primeira fase e, desde logo, da segunda (condenação no saldo) → provas → valor da causa. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- A inicial especifica, **detalhadamente**, as razões pelas quais se exigem as contas, instruída com documentos (art. 550, § 1º).
- Interesse de agir: recusa ou mora em prestar, não aprovação das contas prestadas ou divergência sobre saldo; a recusa pode ser provada por pedido prévio não atendido em prazo razoável (STJ, AgInt no REsp 2.009.271).
- Contas apresentadas devem ser **em forma adequada**: receitas, aplicação das despesas, investimentos (art. 551); as do autor também, com o saldo (art. 551, § 2º).
- Impugnação às contas deve ser fundamentada e específica, referindo o lançamento questionado (art. 550, § 3º); havendo impugnação específica, o juiz fixa prazo para o réu juntar os documentos dos lançamentos (art. 551, § 1º).
- Sem contestação: julgamento antecipado (art. 550, § 4º, remetendo ao art. 355).
- A sentença apura o saldo e é título executivo judicial (art. 552).

## Fundamentos verificados
- CPC arts. 550 a 553; art. 355 (por remissão).
- Súmula 259/STJ (correntista pode propor ação de prestação de contas) e Súmula 477/STJ (decadência do art. 26 do CDC inaplicável às contas sobre tarifas e encargos bancários) — vigência não registrada na base; conferir no portal do STJ.
- STJ, REsp 2.193.129 (3ª Turma, rel. Min. Moura Ribeiro, julg. 24/11/2025): contas exigem gestão de bens alheios, o que não ocorre no mútuo/financiamento comum (Tema 528); distinção para a alienação fiduciária de imóvel com venda extrajudicial.
- STJ, AgInt no REsp 2.014.057 (3ª Turma, rel. Min. Moura Ribeiro, julg. 18/09/2023): a ação de contas não é instrumento adequado à revisão de contratos bancários.
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Citação do réu para prestar as contas ou contestar em 15 dias.
- Procedência da primeira fase, condenando o réu a prestar contas em 15 dias, sob a pena do art. 550, § 5º.
- Na segunda fase: julgamento das contas, apuração do saldo e condenação ao pagamento (art. 552); perícia contábil, se necessária (art. 550, § 6º).
- Exibição dos documentos que justificam os lançamentos impugnados (art. 551, § 1º).
- Juros e correção do saldo: `juros-e-correcao`.
- Custas e honorários (fixados em cada fase conforme a sucumbência) [VERIFICAR: critério de honorários na primeira fase no tribunal local].

## Checklist pré-protocolo
- [ ] Relação de gestão de bens alheios demonstrada (não é mútuo comum)
- [ ] Via correta: não é condomínio edilício nem administrador nomeado em juízo (art. 553)
- [ ] Pedido extrajudicial prévio e a resposta juntados
- [ ] Período e objeto delimitados; razões detalhadas (art. 550, § 1º)
- [ ] Lançamentos duvidosos apontados especificamente
- [ ] Pedido de condenação no saldo já formulado
- [ ] Prescrição verificada

## Erros a evitar
- Pedir contas genéricas "de toda a relação", sem período nem razões concretas.
- Usar a ação de contas para revisar juros e cláusulas de contrato bancário.
- Exigir contas de banco em financiamento comum (Tema 528).
- Impugnar as contas de forma genérica, sem indicar o lançamento (art. 550, § 3º).
- Perder o prazo de 15 dias para apresentar as próprias contas quando o réu não as presta (art. 550, § 6º).

## Integração com o núcleo
`prazos-processuais`, `juros-e-correcao`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`. Execução do saldo: `civel-cumprimento-de-sentenca`. Recurso contra a decisão da primeira fase: conferir natureza (sentença ou interlocutória) no caso — `civel-apelacao` / `civel-agravo-de-instrumento` [VERIFICAR: recurso cabível contra a decisão da 1ª fase].

---
name: imob-reintegracao-de-posse
description: >
  Redige ações possessórias de imóvel — reintegração de posse (esbulho),
  manutenção de posse (turbação) e interdito proibitório (ameaça) — pelos
  arts. 554 a 568 do CPC e 1.196 a 1.224 do CC, separando posse nova (rito
  especial com liminar) de posse velha (procedimento comum). Use quando o
  usuário pedir ação contra invasão de terreno, ocupação de imóvel, comodatário
  que não devolve após notificação, cerca ou obra do vizinho avançando, ameaça
  de invasão, ocupação coletiva ou defesa possessória do réu.
metadata:
  area: imobiliario
  tipo_peca: inicial
  verificado_em: 2026-11-25
---
# Ações possessórias — reintegração, manutenção e interdito proibitório

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: (a) esbulho — perdeu a posse (reintegração); (b) turbação — conserva a posse, mas é perturbado (manutenção); (c) justo receio de esbulho ou turbação iminente (interdito proibitório, art. 567 do CPC); (d) defesa do réu possuidor com pedido possessório na contestação (art. 556).
- Não usar:
  - quem **nunca teve posse** e quer entrar no imóvel com base no título (petitória): `imob-imissao-na-posse`;
  - imóvel **locado** — a retomada se faz por despejo, não por possessória nem imissão (STJ, REsp 1.864.878): `imob-acao-de-despejo`;
  - constrição judicial (penhora, arresto) sobre imóvel de quem não é parte: `imob-embargos-de-terceiro`;
  - quer o domínio pela posse prolongada: `imob-usucapiao-judicial`;
  - redigir ou extinguir o comodato em si: `contratos-comodato`; tutela isolada: `civel-tutela-provisoria`.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Identificação do imóvel: matrícula (se houver), endereço, confrontações, área, croqui ou fotos.
2. Como e desde quando o autor exerce a posse (moradia, cultivo, cerca, contas, IPTU, testemunhas).
3. **Data exata** do esbulho/turbação ou da ameaça — define posse nova ou velha.
4. Quem é o ofensor; se for ocupação coletiva, quantas pessoas e se há como identificá-las.
5. Origem da relação: houve comodato, permissão, tolerância, contrato? Houve notificação para devolver? Quando?
6. Estado civil do autor e do réu e se a posse é exercida em conjunto (art. 73, § 2º, do CPC).
7. Prejuízos (perdas e danos, frutos) e benfeitorias feitas por qualquer das partes.
8. Há ação petitória ou de usucapião em curso sobre o mesmo bem?

## Prazo e contagem
- **Ano e dia** (art. 558 do CPC): ação proposta dentro de ano e dia do esbulho/turbação segue o rito especial, com liminar do art. 562; depois disso, procedimento comum, **sem perder o caráter possessório** (art. 558, parágrafo único).
- Termo inicial em esbulho que o possuidor não presenciou: a posse só se considera perdida quando, ciente, ele se abstém de retomá-la ou é repelido (art. 1.224 do CC) — documente a data da ciência.
- Comodato ou permissão: o esbulho se caracteriza com a recusa após a notificação; guarde a prova da data.
- Concedida ou não a liminar, o autor promove a citação em 5 dias; contestação em 15 dias (art. 564 e parágrafo único).
- Prazos processuais em dias úteis: `prazos-processuais`.

## Estrutura da peça
Endereçamento (foro da situação, competência absoluta — art. 47, § 2º) → qualificação → fatos (posse, ofensa, data) → requisitos do art. 561 um a um → posse nova/velha e liminar → cumulações do art. 555 → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Prova dos quatro requisitos do art. 561: posse; esbulho/turbação pelo réu; data; perda (reintegração) ou continuidade (manutenção) da posse.
- **Fungibilidade** (art. 554): o juiz concede a proteção cabível ainda que se tenha proposto a possessória "errada" — mesmo assim escolha a ação certa.
- **Exceção de domínio vedada**: pendente a possessória, não se propõe ação de domínio entre as partes, e alegar propriedade não obsta a proteção possessória (art. 557 do CPC; art. 1.210, § 2º, do CC). Debate-se posse, não título.
- Detenção não é posse (art. 1.198 do CC); atos de mera permissão ou tolerância não induzem posse (art. 1.208) — argumento central contra ocupante que se diz possuidor.
- Posse injusta = violenta, clandestina ou precária (art. 1.200); comodatário que não devolve após notificação passa a ter posse precária.
- Litígio coletivo: citação pessoal dos encontrados no local e edital para os demais, intimação do MP e da Defensoria (art. 554, §§ 1º a 3º); posse velha coletiva exige audiência de mediação antes da liminar (art. 565).
- Liminar contra pessoa jurídica de direito público só após ouvir seu representante (art. 562, parágrafo único).
- Réu pode pedir caução se o autor não tiver idoneidade financeira (art. 559).

## Fundamentos verificados
- CPC arts. 47, § 2º; 73, § 2º; 554 a 568.
- CC arts. 1.196, 1.198, 1.200, 1.208, 1.210 (e §§ 1º e 2º), 1.214 a 1.222 (frutos e benfeitorias), 1.224.
- Súmula 237/STF (usucapião pode ser arguida em defesa) — o réu pode alegá-la; prepare a réplica.
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Liminar de reintegração/manutenção *inaudita altera parte* (art. 562) ou, se a inicial não bastar, audiência de justificação.
- Posse velha: tutela provisória pelos requisitos gerais (art. 300), demonstrando probabilidade e perigo concretos.
- Interdito: mandado proibitório com pena pecuniária para o caso de transgressão (art. 567).
- Cumulação (art. 555): perdas e danos; indenização dos frutos; medidas para evitar nova ofensa e para cumprir a tutela (multa, remoção, apoio policial).
- Juros e correção sobre perdas e danos: núcleo `juros-e-correcao`.
- Citação dos réus (no litígio coletivo, na forma do art. 554, § 1º); provas (testemunhas, inspeção, perícia de localização).

## Checklist pré-protocolo
- [ ] Data do esbulho/turbação provada e enquadrada em posse nova ou velha
- [ ] Cada requisito do art. 561 com documento ou testemunha indicada
- [ ] Foro da situação do imóvel
- [ ] Cônjuge incluído se houver composse ou ato de ambos (art. 73, § 2º)
- [ ] Notificação prévia juntada (comodato/permissão)
- [ ] Identificação do imóvel suficiente para o oficial cumprir o mandado
- [ ] Ocupação coletiva: MP, Defensoria, divulgação e mediação (arts. 554 e 565)
- [ ] Pedidos cumulados do art. 555 e multa para o descumprimento
- [ ] Juros/correção remetidos ao núcleo

## Erros a evitar
- Fundamentar a inicial só na escritura/matrícula: possessória discute posse; quem nunca possuiu deve usar a imissão.
- Omitir a data da ofensa ou deixá-la vaga — o juiz não tem como aferir o ano e dia.
- Chamar de "esbulho" a mera ameaça (é interdito) ou a perturbação sem perda (é manutenção).
- Pedir a liminar do art. 562 em posse velha sem fundamentar a tutela do art. 300.
- Ignorar a mediação obrigatória do art. 565 em ocupação coletiva antiga.
- Usar possessória contra locatário inadimplente (a via é o despejo).

## Integração com o núcleo
`prazos-processuais`, `juros-e-correcao`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`, `civel-tutela-provisoria`, `civel-contestacao` (defesa do réu).

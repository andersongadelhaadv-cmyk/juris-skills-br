---
name: prev-revisao-da-vida-toda-acoes-pendentes
description: >
  Orienta o advogado sobre a revisão da vida toda depois do STF (Tema 1.102;
  ADIs 2.110 e 2.111): tese superada, parecer de inviabilidade para cliente
  novo e manifestação em ação pendente para aplicar a modulação
  (irrepetibilidade dos valores recebidos até 05/04/2024 e dispensa de
  honorários, custas e perícias contábeis). Use quando o usuário perguntar se
  ainda cabe revisão da vida toda, tiver ação de vida toda em andamento,
  receber cobrança do INSS de valores pagos por liminar ou precisar encerrar
  essas ações sem custo ao cliente.
metadata:
  area: previdenciario
  tipo_peca: outro
  verificado_em: 2026-11-25
---
# Revisão da vida toda: tese superada e ações pendentes

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Situação da tese (conferida em 25/11/2026)
- **A revisão da vida toda está SUPERADA.** O STF declarou constitucional o art. 3º da Lei 9.876/1999 (ADIs 2.110 e 2.111) e, no Tema 1.102 (RE 1.276.977), fixou que o segurado que se enquadra nesse dispositivo **não pode optar** pela regra definitiva do art. 29, I e II, da Lei 8.213/1991, "independentemente de lhe ser mais favorável".
- Modulação (tese do Tema 1.102): (a) irrepetibilidade dos valores recebidos por decisões judiciais, definitivas ou provisórias, proferidas **até 05/04/2024** (publicação da ata do mérito das ADIs); (b) excepcionalmente, não se cobram honorários sucumbenciais, custas e perícias contábeis dos autores de ações **pendentes de conclusão até 05/04/2024**. Ficam mantidas devoluções e pagamentos já feitos.
- As ADIs 2.110 e 2.111 não estão na base do JuriBase; resultado e data da ata foram confirmados pela própria tese do Tema 1.102.
- Esta skill **não redige inicial**. Ajuizar hoje é perder a ação e arcar com sucumbência sem a proteção da modulação.

## Quando usar / quando não usar
- Usar: (a) cliente novo pede a revisão → parecer de inviabilidade; (b) ação de vida toda em curso → manifestação pedindo julgamento com a modulação; (c) INSS cobra (nos autos ou administrativamente) valores pagos por tutela ou sentença → defesa com o item (a) da modulação; (d) execução/cumprimento de título de vida toda.
- Não usar: outras revisões de RMI (inclusão de período, salário omitido, erro de cálculo, melhor benefício) → `prev-revisao-de-beneficio`. Recurso administrativo → `prev-recurso-crps`. Recurso judicial genérico → `civel-apelacao` ou `prev-pedido-de-uniformizacao-tnu`.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Data do ajuizamento (antes ou depois de 05/04/2024) e fase atual do processo.
2. Houve tutela de urgência ou sentença favorável? Datas exatas de cada decisão e de cada pagamento.
3. Há trânsito em julgado favorável? Em que data? Já há cumprimento de sentença ou RPV/precatório?
4. Há cobrança do INSS (ofício, desconto no benefício, pedido nos autos)? Juntar o documento.
5. Houve condenação em honorários, custas ou perícia contábil? Já pagos?
6. Para parecer: carta de concessão (espécie, DIB) e data de filiação ao RGPS.

## Prazo e contagem
- O marco é **05/04/2024** — para decisões que geraram pagamento (item a) e para pendência da ação (item b). Registre as datas em quadro.
- Prazos de manifestação, impugnação e recurso: `prazos-processuais`.
- Título transitado em julgado antes ou depois do julgamento do STF: o CPC trata a inexigibilidade (art. 535, III e § 5º, se a decisão do STF é anterior ao trânsito, § 7º) e a rescisória (§ 8º, se posterior, com prazo contado da decisão do STF). Como os tribunais aplicam isso à vida toda não foi conferido [VERIFICAR: jurisprudência sobre coisa julgada e rescisória em vida toda não encontrada no JuriBase].

## Estrutura da peça   (detalhe em [estrutura](references/estrutura.md))
- **Parecer ao cliente:** pergunta → tese e situação no STF → por que não ajuizar → alternativas reais (outras revisões) → conclusão.
- **Manifestação em ação pendente:** síntese → Tema 1.102 e ADIs → enquadramento na modulação (data do ajuizamento, datas das decisões) → pedidos.
- **Defesa contra cobrança:** origem e data de cada pagamento → item (a) da modulação → pedido de cessação da cobrança e devolução de descontos.

## Requisitos e preliminares
- Separe três grupos de clientes, porque o tratamento muda:
  1. Ação ajuizada **até 05/04/2024**, sem trânsito: proteção do item (b) (sem honorários, custas e perícia contábil); valores recebidos por decisões até essa data são irrepetíveis.
  2. Ação ajuizada **depois de 05/04/2024**: sem a proteção do item (b). Avaliar desistência: após a contestação depende de consentimento do réu (CPC, art. 485, § 4º) e quem desiste paga despesas e honorários (art. 90). Discutir custo com o cliente antes.
  3. **Título transitado em julgado**: risco de impugnação por inexigibilidade ou de rescisória (CPC, art. 535, §§ 5º a 8º) [VERIFICAR: aplicação concreta].
- Pagamento feito por decisão **posterior** a 05/04/2024 não está no texto do item (a): avisar o cliente do risco de devolução.
- Não alegar "direito adquirido à tese" nem pedir sobrestamento à espera de mudança: o Tema 1.102 é vinculante (repercussão geral).

## Fundamentos verificados   (detalhe em [fundamentos](references/fundamentos.md))
- Lei 9.876/1999, art. 3º; Lei 8.213/1991, art. 29, I e II; EC 103/2019, art. 26 (benefícios pela regra da reforma já usam todo o período desde 07/1994).
- STF Tema 1.102 (RE 1.276.977), com a modulação; ADIs 2.110 e 2.111 (via tese do Tema 1.102).
- CPC, arts. 90, 485, VIII e § 4º, e 535, III e §§ 5º a 8º.

## Pedidos e requerimentos
- Ação pendente até 05/04/2024: aplicação do Tema 1.102 **com a modulação**; afastamento expresso de honorários sucumbenciais, custas e perícias contábeis; declaração de irrepetibilidade dos valores recebidos por decisões até 05/04/2024.
- Cobrança do INSS: cessação dos descontos e devolução do que foi descontado indevidamente; correção e juros pelo núcleo `juros-e-correcao`.
- Pedido subsidiário, se houver outra revisão viável no mesmo caso: tratar em ação própria (`prev-revisao-de-beneficio`).

## Checklist pré-protocolo
- [ ] Quadro de datas: ajuizamento, cada decisão favorável, cada pagamento, trânsito.
- [ ] Grupo do cliente identificado (1, 2 ou 3).
- [ ] Tese do Tema 1.102 transcrita da fonte oficial, com os itens (a) e (b).
- [ ] Pedido expresso de afastamento de honorários, custas e perícia contábil (grupo 1).
- [ ] Cliente informado por escrito de que a tese foi superada e dos riscos do seu grupo.
- [ ] Nenhuma taxa de juros ou índice escrito na peça.

## Erros a evitar
- Ajuizar ou "manter por precaução" pedido de revisão da vida toda: a tese está superada.
- Esquecer de pedir a aplicação do item (b) e deixar o juiz condenar em honorários.
- Prometer irrepetibilidade de valor pago por decisão posterior a 05/04/2024.
- Desistir depois da contestação sem calcular o custo do art. 90 do CPC.
- Tratar o título transitado como intocável sem avaliar o art. 535, §§ 5º a 8º, do CPC.

## Integração com o núcleo
- `prazos-processuais`; `juros-e-correcao` (devolução de descontos); `verificacao-de-citacoes` (conferir novidades no Tema 1.102 antes de protocolar); `fidelidade-factual` (datas de decisões e pagamentos); `estilo-forense`.

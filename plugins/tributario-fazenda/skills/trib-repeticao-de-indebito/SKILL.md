---
name: trib-repeticao-de-indebito
description: >
  Redige ação de repetição de indébito tributário (CTN arts. 165 a 169), com
  prazo de 5 anos (art. 168 e LC 118/2005, Tema 4 STF), prova do encargo nos
  tributos indiretos (art. 166) e opção entre precatório e compensação. Use quando
  o usuário pedir restituição de tributo pago a maior ou indevido, ação de
  repetição, devolução de imposto, recuperação de crédito tributário, restituir
  ICMS, ISS, IR retido ou contribuição recolhida indevidamente.
metadata:
  area: tributario-fazenda
  tipo_peca: inicial
  verificado_em: 2026-11-01
---
# Ação de repetição de indébito tributário

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: tributo já pago indevidamente ou a maior (CTN art. 165, I e II) ou pago com base em decisão condenatória depois reformada (art. 165, III); pedido condenatório de devolução em dinheiro e/ou declaração do direito de compensar.
- Não usar: crédito ainda não pago (use `trib-acao-anulatoria` ou `trib-mandado-de-seguranca`); quando só se quer declarar compensação com prova documental pronta e ato recente (MS pode ser mais rápido, Súmula 213 STJ).
- Pedido administrativo negado: a anulatória da decisão denegatória prescreve em 2 anos (CTN art. 169). Use esta skill, ajustando o pedido.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
- Guias, DARFs, DAEs ou comprovantes de retenção, com datas de pagamento e competências.
- Fundamento da indevida cobrança (inconstitucionalidade, erro de cálculo, não incidência, decisão reformada).
- Se o tributo é indireto (ICMS, IPI, ISS em certas hipóteses): quem suportou o encargo e prova disso, ou autorização do terceiro (art. 166; Súmula 546 STF).
- Pedido administrativo anterior (data, número, decisão).
- Ente credor e, em caso de IR retido por Estado/Município de servidor, a legitimidade passiva do ente retentor (Súmula 447 STJ).

## Prazo e contagem
- 5 anos (CTN art. 168), contados da extinção do crédito (pagamento) nos casos do art. 165, I e II. Para tributos sujeitos a homologação, o prazo de 5 anos do pagamento vale para ações ajuizadas a partir de 09/06/2005 (LC 118/2005; Tema 4 STF).
- Art. 165, III: conta da decisão administrativa definitiva ou do trânsito em julgado da decisão que reformou a condenação.
- Pedido administrativo de restituição ou compensação NÃO interrompe a prescrição da ação (Súmula 625 STJ).
- Habilitação do crédito judicial na Receita para compensar: 5 anos contados da certificação do trânsito em julgado (art. 168, §§2º e 3º, LC 236/2026).
- Use `prazos-processuais` para a contagem.

## Estrutura da peça
Endereçamento → partes → fatos e pagamentos → legitimidade (art. 166) → prazo → fundamento do indébito → quantificação → atualização (remissão ao núcleo) → forma de devolução → pedidos. Roteiro em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Prova do pagamento é indispensável; planilha por competência.
- Tributo indireto: sem prova de que o autor assumiu o encargo ou autorização do contribuinte de fato, a ação falha (art. 166; Súmula 546 STF).
- Restituição abrange, proporcionalmente, juros de mora e multas pagos, salvo multas por infração formal não afetadas (art. 167).
- Atualização: o CTN agora manda atualizar os indébitos pelos mesmos índices aplicados aos créditos tributários do ente (art. 165-A, LC 236/2026). Para tributos estaduais, a SELIC só incide se prevista em lei local e não se cumula com outros índices (Súmula 523 STJ). As Súmulas 162 (correção desde o pagamento) e 188 (juros do trânsito em julgado; CTN art. 167, p.ú.) devem ser lidas à luz do índice legal do ente. Calcule SEMPRE com `juros-e-correcao`.
- Forma de recebimento: precatório/RPV (CF art. 100) ou compensação após o trânsito em julgado (CTN art. 170-A; Súmula 461 STJ). Restituição administrativa do indébito judicial não é admitida (Tema 1262 STF).

## Fundamentos verificados
CTN arts. 165, 165-A, 166, 167, 168, 169, 170 e 170-A; LC 118/2005; CF art. 100; Tema 4 e Tema 1262 STF; Súmula 546 STF; Súmulas 162, 188, 447, 461, 523 e 625 STJ. Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Declaração de inexistência da relação jurídica que fundou a cobrança (se o fundamento continuar a incidir, peça também a cessação para o futuro).
- Condenação à restituição dos valores pagos nos 5 anos anteriores ao ajuizamento e durante o processo, atualizados pelo critério legal indicado em `juros-e-correcao`.
- Faculdade de optar, na execução, por precatório/RPV ou compensação (Súmula 461 STJ).
- Honorários pelo CPC art. 85, §3º.

## Checklist pré-protocolo
- [ ] Datas de cada pagamento listadas e prazo de 5 anos conferido por guia.
- [ ] Tributo direto ou indireto definido; prova do encargo (art. 166) anexada se indireto.
- [ ] Planilha de valores sem taxa inventada: gerada pelo `juros-e-correcao`.
- [ ] Legitimidade passiva correta (ente credor ou ente retentor no IR de servidor).
- [ ] Pedido administrativo anterior não tratado como causa interruptiva.
- [ ] Opção precatório/compensação preservada.

## Erros a evitar
- Contar o prazo pela tese dos "5 + 5" em ação ajuizada após 09/06/2005 (Tema 4 STF).
- Afirmar que o pedido administrativo interrompeu a prescrição (Súmula 625 STJ).
- Pedir restituição administrativa do valor reconhecido em juízo (Tema 1262 STF).
- Cumular SELIC com outro índice ou aplicar juros supletivos do CTN art. 161, §1º quando a lei do ente prevê índice próprio (Súmula 523 STJ; use o núcleo).
- Ignorar o art. 166 em ICMS e IPI.

## Integração com o núcleo
- `juros-e-correcao`: atualização do indébito (índice do ente, art. 165-A; Fazenda federal, SELIC). Nunca escrever taxa própria.
- `prazos-processuais`: prescrição do art. 168 e prazos do processo.
- `verificacao-de-citacoes`: todo precedente acrescentado.
- `fidelidade-factual`: conferência de guias e datas.
- `estilo-forense`: revisão final.

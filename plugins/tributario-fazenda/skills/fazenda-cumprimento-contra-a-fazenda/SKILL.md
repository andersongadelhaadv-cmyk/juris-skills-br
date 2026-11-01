---
name: fazenda-cumprimento-contra-a-fazenda
description: >
  Redige requerimento de cumprimento de sentença contra a Fazenda Pública para
  pagamento de quantia (CPC arts. 534 e 535), com demonstrativo discriminado,
  expedição de precatório ou RPV (CF art. 100) e atualização pelo regime da
  EC 113/2021 com a redação da EC 136/2025; também orienta a impugnação da
  Fazenda. Use quando o usuário pedir cumprimento de sentença contra União,
  Estado, Município ou autarquia, execução contra a Fazenda, expedição de
  precatório ou RPV, requisição de pequeno valor, destaque de honorários,
  impugnação ao cumprimento pela Fazenda ou excesso de execução.
metadata:
  area: tributario-fazenda
  tipo_peca: execucao
  verificado_em: 2026-11-01
---
# Cumprimento de sentença contra a Fazenda Pública

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: título judicial que condena a Fazenda a pagar quantia (inclusive repetição de indébito e honorários); impugnação da Fazenda (art. 535); pedidos de expedição de precatório/RPV, destaque de honorários, parcela incontroversa.
- Não usar: execução de título extrajudicial contra a Fazenda (CPC art. 910, embargos em 30 dias; cabível, Súmula 279 STJ); obrigação de fazer; cumprimento entre particulares.
- Indébito reconhecido em MS: devolução em dinheiro pelo regime de precatórios (Tema 1262 STF) ou compensação (Súmula 461 STJ).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
- Sentença, acórdãos, certidão de trânsito em julgado; se ilíquida, decisão de liquidação.
- Dados de cada exequente (nome, CPF/CNPJ) e contrato de honorários se houver destaque.
- Ente devedor e lei local que fixa o teto de RPV (se não houver lei: 40 SM Estados/DF, 30 SM Municípios, ADCT art. 87; União: 60 SM, Lei 10.259/2001 art. 17, §1º).
- Prioridades: idade de 60 anos ou mais, doença grave, deficiência, natureza alimentar (CF art. 100, §§1º e 2º).
- Débitos do credor inscritos em dívida ativa (podem gerar depósito à conta do juízo da cobrança: CF art. 100, §9º, na redação da EC 113/2021) [VERIFICAR efeitos das ADIs indicadas no texto constitucional].

## Prazo e contagem
- Fazenda intimada para impugnar em 30 dias nos próprios autos (art. 535), sem dobra (prazo próprio, art. 183, §2º).
- RPV: pagamento em 2 meses da entrega da requisição (art. 535, §3º, II); na Justiça Federal, 60 dias (Lei 10.259/2001 art. 17).
- Precatório: inclusão no orçamento se apresentado até 1º de fevereiro, pagamento até o fim do exercício seguinte (CF art. 100, §5º, redação EC 136/2025).
- Prescrição da pretensão executória: mesmo prazo da ação (Súmula 150 STF), 5 anos contra a Fazenda. Pedido administrativo não interrompe (Súmula 625 STJ). Use `prazos-processuais`.

## Estrutura da peça
Requerimento: endereçamento → título e trânsito → exequentes → demonstrativo (art. 534) → regime de atualização → enquadramento precatório/RPV → prioridades → destaque de honorários → pedidos. Impugnação da Fazenda: matérias do art. 535 com valor que entende correto. Roteiro em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Demonstrativo discriminado por exequente com índice, juros, termos inicial e final, capitalização e descontos (art. 534, I a VI; §1º).
- Sem multa de 10% do art. 523 (art. 534, §2º). Honorários do cumprimento: não são devidos quando o crédito vai para precatório e não há impugnação (art. 85, §7º); são devidos em execução individual de sentença coletiva, mesmo sem embargos (Súmula 345 STJ).
- Vedado fracionar para enquadrar em RPV (CF art. 100, §8º); parcela incontroversa pode ser requisitada de imediato, considerado o valor total para dimensionar RPV (Tema 28 STF; CPC art. 535, §4º). Renúncia ao excedente para receber por RPV é facultada (ADCT art. 87, p.ú.; Lei 10.259/2001 art. 17, §4º).
- Honorários contratuais/sucumbenciais: natureza alimentar, requisitados em ordem própria (Súmula Vinculante 47).
- Atualização: a partir da expedição, a EC 136/2025 fixou IPCA + juros simples de 2% a.a., limitado à SELIC, para requisitórios federais (EC 113/2021 art. 3º, caput e §1º) e para Estados, DF e Municípios desde 01/08/2025 (ADCT art. 97, §§16 e 16-A); em processos tributários, os critérios do crédito tributário do ente (EC 113 art. 3º, §2º). Não incidem juros no período de graça do art. 100, §5º (EC 113 art. 3º, §3º; Súmula Vinculante 17). Incidem juros entre a data dos cálculos e a requisição (Tema 96 STF). Período anterior à expedição e liquidação: aplique `juros-e-correcao` [VERIFICAR conciliação entre Tema 1419 STF e a EC 136/2025].
- Impugnação: excesso de execução exige indicar de imediato o valor correto, sob pena de não conhecimento (art. 535, §2º).

## Fundamentos verificados
CPC arts. 85, §7º, 183, §2º, 534, 535 e 910; CF art. 100 (redação EC 62/2009, 94/2016, 113/2021 e 136/2025); ADCT arts. 87 e 97, §§16 e 16-A; EC 113/2021 art. 3º (redação EC 136/2025); Lei 10.259/2001 art. 17; Lei 12.153/2009 art. 13; Súmula Vinculante 17 e 47; Súmulas 150 STF; 279, 311, 345, 461 e 625 STJ; Temas 28, 96, 1262 e 1419 STF. Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Intimação da Fazenda na pessoa do representante judicial para impugnar em 30 dias (art. 535).
- Não impugnada ou rejeitada a impugnação: expedição de precatório (art. 535, §3º, I) ou RPV (inciso II), por exequente; parcela incontroversa de imediato (§4º).
- Destaque dos honorários contratuais (juntar contrato) e requisição autônoma dos sucumbenciais.
- Registro das prioridades constitucionais.

## Checklist pré-protocolo
- [ ] Trânsito em julgado certificado; liquidação concluída se a sentença era ilíquida.
- [ ] Demonstrativo por exequente com todos os itens do art. 534, gerado pelo `juros-e-correcao`.
- [ ] Teto de RPV do ente conferido (lei local ou ADCT art. 87); decisão sobre renúncia ao excedente.
- [ ] Nenhum fracionamento indevido; parcela incontroversa identificada.
- [ ] Prioridades e natureza alimentar comprovadas por documento.
- [ ] Contrato de honorários anexado para destaque.
- [ ] Prazo prescricional da execução conferido (Súmula 150 STF).

## Erros a evitar
- Pedir multa do art. 523 contra a Fazenda (art. 534, §2º).
- Apresentar cálculo global sem discriminar cada exequente (art. 534, §1º).
- Fracionar o crédito para caber em RPV (CF art. 100, §8º).
- Aplicar SELIC ou juros de mora próprios após a expedição sem observar a EC 136/2025.
- Na impugnação da Fazenda: alegar excesso sem apresentar o valor correto (art. 535, §2º).
- Escrever taxa de juros na peça: use `juros-e-correcao`.

## Integração com o núcleo
- `juros-e-correcao`: demonstrativo e regime constitucional de atualização (antes e depois da expedição).
- `prazos-processuais`: prazo de impugnação (30 dias, sem dobra) e prescrição executória.
- `verificacao-de-citacoes`: todo precedente acrescentado.
- `fidelidade-factual`: dados dos exequentes e valores.
- `estilo-forense`: revisão final.

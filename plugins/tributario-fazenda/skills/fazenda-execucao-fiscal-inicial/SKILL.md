---
name: fazenda-execucao-fiscal-inicial
description: >
  Redige petição inicial de execução fiscal pela Fazenda Pública (LEF arts. 1º,
  2º, 6º e 8º), com CDA conforme LEF art. 2º, §5º e CTN art. 202, providências
  prévias exigidas pelo Tema 1184 STF e pela Res. CNJ 547/2024 (conciliação e
  protesto), e pedido de redirecionamento a sócio (CTN art. 135, III; Súmula 435
  STJ). Use quando o usuário for procurador ou advogado público e pedir execução
  fiscal, ajuizar CDA, cobrança judicial de dívida ativa, redirecionamento ao
  sócio, inclusão de corresponsável ou pedido de indisponibilidade de bens.
metadata:
  area: tributario-fazenda
  tipo_peca: execucao
  verificado_em: 2026-11-01
---
# Petição inicial de execução fiscal (lado da Fazenda)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: cobrança judicial de dívida ativa tributária ou não tributária da União, Estados, DF, Municípios e autarquias (LEF art. 1º); pedido incidental de redirecionamento; inclusão de créditos de IPTU/correlatos na mesma execução (Res. CNJ 547/2024, art. 4º-A).
- Não usar: defesa do executado (use `trib-embargos-a-execucao-fiscal` ou `trib-excecao-pre-executividade-fiscal`); crédito com exigibilidade suspensa (CTN art. 151) ou em discussão administrativa pendente.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
- CDA(s) e termo de inscrição; número do processo administrativo ou auto de infração.
- Data de constituição definitiva e de inscrição; verificação de prescrição.
- Valor atualizado por CDA e se o total supera o piso de ajuizamento do ente e o patamar de baixo valor da Res. CNJ 547/2024 (R$ 10.000,00 no ajuizamento, para fins de extinção).
- Comprovação das providências prévias: tentativa de conciliação/solução administrativa e protesto (ou motivo de dispensa).
- Para redirecionamento: certidão do oficial de justiça ou documento que demonstre o encerramento irregular; ficha da Junta com os administradores na data da dissolução.

## Prazo e contagem
- Prescrição: 5 anos da constituição definitiva (CTN art. 174); interrompem, entre outros, o despacho citatório e o protesto da CDA (art. 174, §1º, I e II; incisos II a IX na redação da LC 236/2026, cujo novo caput do §1º foi vetado). Inscrição suspende 180 dias apenas para dívida não tributária (LEF art. 2º, §3º).
- Ajuíze com folga: a demora atribuível ao Judiciário não prejudica (Súmula 106 STJ), mas a da Fazenda sim.
- Redirecionamento: controle a prescrição para o redirecionamento conforme o Tema 444 do STJ (termo inicial pela actio nata; a citação da devedora original não inicia o prazo quando a dissolução irregular é posterior). Detalhe em fundamentos.
- Use `prazos-processuais`.

## Estrutura da peça
Endereçamento → exequente → executado(s) e corresponsáveis → pedido de citação pelo correio (LEF art. 8º) → demonstração das providências prévias → valor da causa → requerimentos de penhora/indisponibilidade → (se for o caso) redirecionamento. Roteiro em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Inicial simples: juiz, pedido e requerimento de citação; CDA integra a inicial (LEF art. 6º). Não se exige demonstrativo de cálculo (Súmula 559 STJ) nem indeferimento por falta de CPF/CNPJ (Súmula 558 STJ).
- CDA com todos os requisitos (LEF art. 2º, §5º e §6º; CTN art. 202, redação LC 236/2026): devedor e corresponsáveis, valor originário, termo inicial e forma dos juros e encargos, origem, natureza e fundamento legal, atualização monetária, data e número da inscrição, número do processo administrativo. Emenda/substituição até a decisão de primeira instância, sem trocar o sujeito passivo (LEF art. 2º, §8º; Súmula 392 STJ).
- Interesse de agir (Tema 1184 STF e Res. CNJ 547/2024, arts. 2º e 3º): prévia tentativa de conciliação ou solução administrativa (presumida se prevista em ato normativo do ente) e prévio protesto, salvo dispensa justificada (comunicação a cadastros de crédito, averbação da CDA em registros de bens, indicação de bens penhoráveis na inicial ou inclusão no Cadin).
- Redirecionamento (CTN art. 135, III): exige excesso de poderes ou infração à lei; o mero inadimplemento não basta (Súmula 430 STJ); dissolução irregular presumida autoriza (Súmula 435 STJ); responde quem administrava na data da dissolução, ainda que não fosse gestor no fato gerador (REsp 1.643.944, repetitivo da 1ª Seção, 2022).
- Indisponibilidade (CTN art. 185-A): só após citação, sem pagamento nem bens penhoráveis, limitada ao valor exigível.

## Fundamentos verificados
LEF arts. 1º, 2º, 3º, 6º a 9º, 11, 25, 39 e 40; CTN arts. 134, 135, 174, 185, 185-A, 202 a 204; Lei 9.492/1997 art. 1º, p.ú.; Lei 10.522/2002 art. 20-B; Tema 1184 STF; Res. CNJ 547/2024; Súmulas 106, 392, 430, 435, 452, 515, 558 e 559 STJ; REsp 1.643.944/STJ. Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Citação do executado pelo correio com AR para pagar ou garantir em 5 dias (LEF art. 8º), sucessivamente por oficial e edital.
- Não pago nem garantido: penhora preferencial de dinheiro por meio eletrônico (LEF art. 11, I), arresto se o devedor se ocultar (art. 7º, III), registro e avaliação.
- Após citação infrutífera de bens: indisponibilidade (CTN art. 185-A).
- Redirecionamento aos administradores identificados, com citação para pagar ou garantir.
- Intimações pessoais ao representante da Fazenda (LEF art. 25). Dispensa de custas (art. 39).

## Checklist pré-protocolo
- [ ] Crédito não prescrito e exigível (sem suspensão do art. 151).
- [ ] CDA conferida item a item (LEF art. 2º, §5º; CTN art. 202).
- [ ] Providências prévias documentadas (conciliação e protesto ou motivo de dispensa).
- [ ] Valor acima do piso do ente; ciência do patamar da Res. CNJ 547/2024.
- [ ] Redirecionamento só com prova da dissolução irregular ou de infração, e com os administradores da época.
- [ ] Planilha de atualização gerada pelo `juros-e-correcao` (a CDA indica a forma de cálculo).

## Erros a evitar
- Ajuizar sem prova de conciliação/protesto (risco de extinção por falta de interesse, Tema 1184 STF).
- Incluir sócio na CDA sem processo administrativo de apuração de responsabilidade ou pedir redirecionamento por mero inadimplemento (Súmula 430 STJ).
- Substituir a CDA para trocar o executado (Súmula 392 STJ).
- Pedir indisponibilidade antes da citação e da busca de bens (CTN art. 185-A).
- Escrever taxa de juros na inicial: a CDA define o critério; cálculos pelo núcleo.

## Integração com o núcleo
- `prazos-processuais`: prescrição do crédito e do redirecionamento.
- `juros-e-correcao`: atualização do débito (Fazenda: SELIC conforme lei do ente; nunca taxa própria na peça).
- `verificacao-de-citacoes`: todo precedente acrescentado (inclusive número de repetitivos).
- `fidelidade-factual`: certidões de oficial e registros da Junta.
- `estilo-forense`: revisão final.

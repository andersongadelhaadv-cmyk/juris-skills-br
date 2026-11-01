---
name: trabalhista-rescisao-indireta
description: >
  Estrutura o pedido de rescisão indireta do contrato de trabalho por falta grave
  do empregador (CLT art. 483), com enquadramento na alínea correta, prova da
  gravidade e atualidade, opção de permanecer ou não no serviço (§3º) e verbas
  devidas como na dispensa sem justa causa. Use quando o usuário pedir rescisão
  indireta, justa causa do empregador, despedida indireta, atraso de salários ou
  FGTS não depositado como motivo para sair, assédio do chefe, ou converter pedido
  de demissão em rescisão indireta.
metadata:
  area: trabalhista
  tipo_peca: inicial
  verificado_em: 2026-11-01
---
# Rescisão indireta

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: empregado quer romper o contrato por falta grave do empregador e receber as verbas da dispensa imotivada. A peça é uma reclamação trabalhista: use a estrutura de `trabalhista-reclamacao` e acrescente os tópicos desta skill.
- Não usar: quando o empregado já pediu demissão sem vício (avaliar antes se houve coação ou erro); quando a falta é antiga e tolerada por longo tempo sem qualquer reação (risco de perdão tácito — argumentar caso a caso).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
- Qual falta, desde quando, com que frequência, e a prova (holerites com atraso, extrato do FGTS, mensagens, testemunhas, boletim, atestado).
- Se o empregado continua trabalhando e se quer continuar até a sentença.
- Dados contratuais para liquidar as verbas (salário, admissão, férias, 13º, FGTS).
- Se há estabilidade (gestante, acidentária, CIPA, dirigente) que mude o cálculo.

## Prazo e contagem
- Prescrição bienal conta da extinção do contrato; na rescisão indireta a data da extinção é controvertida — documentar a data do afastamento ou da comunicação (CLT art. 11; CF art. 7º XXIX).
- A imediatidade é exigida com flexibilidade para o empregado; explicar por que a reação ocorreu quando ocorreu.

## Estrutura da peça
Na reclamação: tópico "Da rescisão indireta" antes das verbas — falta, enquadramento, gravidade, prova, data de término pretendida — e depois o rol de verbas rescisórias. Roteiro em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Enquadramento** (art. 483): a) serviços superiores às forças, ilícitos ou alheios ao contrato; b) rigor excessivo; c) perigo manifesto de mal considerável; d) descumprimento das obrigações do contrato; e) ato lesivo da honra e boa fama; f) ofensa física; g) redução do trabalho por peça ou tarefa que afete o salário.
- **Permanência no serviço**: nas alíneas "d" e "g", o empregado pode pleitear a rescisão permanecendo ou não no serviço até a decisão (§3º). Nas demais, em regra deve afastar-se; orientar o cliente sobre o risco de a ausência ser tratada como abandono se a tese não prevalecer.
- **Mora salarial**: o pagamento de salários atrasados em audiência não afasta a mora (Súmula 13 do TST).
- **Aviso prévio** é devido na despedida indireta (art. 487 §4º).
- Ônus da prova da falta é do empregado (art. 818 I).

## Fundamentos verificados
CLT arts. 11, 477, 483, 487 §4º, 818; CF art. 7º XXIX; Súmula 13 do TST. Detalhes em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Declaração da rescisão indireta, com data de término.
- Verbas: aviso prévio indenizado; saldo de salário; 13º e férias proporcionais + 1/3; férias vencidas; FGTS do período e indenização compensatória; liberação de guias para saque e seguro-desemprego (ou indenização substitutiva); baixa na CTPS.
- Pedido sucessivo, se cabível: reconhecimento de dispensa sem justa causa ou conversão do pedido de demissão.
- Dano moral, se a falta também lesionou direito da personalidade (arts. 223-A e ss.; ver `trabalhista-acidente-e-doenca-ocupacional` sobre os parâmetros e as ADIs).
- Correção e juros conforme `juros-e-correcao`.

## Checklist pré-protocolo
- [ ] Alínea do art. 483 indicada para cada falta.
- [ ] Prova da falta e da gravidade anexada ou testemunhas arroladas.
- [ ] Decisão sobre permanecer ou sair registrada (e o cliente orientado sobre o risco).
- [ ] Data de término pretendida definida.
- [ ] Verbas liquidadas (art. 840 §1º).
- [ ] Pedido sucessivo para o caso de não reconhecimento.

## Erros a evitar
- Pedir rescisão indireta por falta leve ou isolada sem demonstrar gravidade.
- Orientar o empregado a parar de trabalhar em alínea que não seja "d" ou "g" sem avaliar o risco.
- Esquecer o aviso prévio e a indenização do FGTS.
- Deixar de liquidar os pedidos.

## Integração com o núcleo
`juros-e-correcao`, `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual` (fatos da falta só como narrados e provados), `estilo-forense`.

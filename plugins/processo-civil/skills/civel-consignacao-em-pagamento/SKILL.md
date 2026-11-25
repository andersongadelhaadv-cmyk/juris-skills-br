---
name: civel-consignacao-em-pagamento
description: >
  Redige a consignação em pagamento de obrigação civil comum — depósito
  bancário extrajudicial com notificação ao credor ou ação consignatória (CPC,
  arts. 539 a 549; CC, arts. 334 a 345) — nas hipóteses de recusa injusta,
  credor que não vem receber, credor desconhecido ou incerto, dúvida sobre quem
  deve receber e litígio sobre o objeto, com alerta do Tema 967/STJ (depósito
  insuficiente leva à improcedência). Use quando o usuário pedir para depositar
  em juízo o que deve, credor que se recusa a receber ou dar quitação, dois
  credores disputando o mesmo pagamento, credor sumido, parcelas de contrato
  civil recusadas ou "quero pagar e me livrar da mora".
metadata:
  area: processo-civil
  tipo_peca: inicial
  verificado_em: 2026-11-25
---
# Consignação em pagamento (obrigação civil)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar nas hipóteses do CC, art. 335: (I) credor não pode ou, sem justa causa, recusa receber ou dar quitação; (II) credor não vai nem manda receber a coisa no lugar, tempo e condição devidos; (III) credor incapaz, desconhecido, ausente ou em lugar incerto ou de acesso perigoso ou difícil; (IV) dúvida sobre quem deve legitimamente receber; (V) litígio pendente sobre o objeto do pagamento.
- O cliente **quer pagar** o valor ou a coisa que entende devidos e obter a quitação, extinguindo a obrigação (CC, art. 334; CPC, art. 546).
- Não usar:
  - Parcelas de financiamento ou contrato bancário → `banc-consignacao-e-purgacao-da-mora`.
  - Tributo → `trib-consignacao-em-pagamento`.
  - Aluguel e encargos da locação: rito próprio do art. 67 da Lei 8.245/1991 (ordenada a citação, o autor é intimado a depositar em 24 horas) → adaptar com `imob-locacao-residencial` ou `contratos-locacao-comercial`.
  - O objetivo é discutir cláusulas e pagar menos → `consumidor-contratos-bancarios-revisional` ou `civel-acao-declaratoria`; a consignatória exige depósito integral.
  - Pagamento já feito em duplicidade → repetição de indébito.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Obrigação: contrato, valor, vencimento, lugar do pagamento (decisivo para foro e depósito).
2. Hipótese do art. 335 e sua prova (recusa por escrito, e-mails, notificação devolvida, cessão não comunicada, disputa entre pretendentes, ação em curso sobre o objeto).
3. Valor integral devido na data do depósito, com encargos de mora já incidentes (Tema 967) — memória de cálculo.
4. Prestações sucessivas? Quais vencem durante o processo?
5. Coisa (não dinheiro): coisa certa ou indeterminada? Quem escolhe? (CPC, art. 543).
6. Já houve depósito bancário extrajudicial? Data, banco, retorno do AR, recusa e data dela.

## Prazo e contagem
- **Via extrajudicial** (só dinheiro): depósito em banco, oficial onde houver, no lugar do pagamento, com carta e AR ao credor; ele tem 10 dias para recusar por escrito ao banco (CPC, art. 539, § 1º). Sem recusa, devedor liberado (§ 2º). Com recusa, a ação deve ser proposta em **1 mês**, com prova do depósito e da recusa (§ 3º); sem ação, o depósito fica sem efeito (§ 4º).
- **Via judicial**: depósito em 5 dias do deferimento, sob pena de extinção sem mérito (art. 542, I e parágrafo único), salvo se já feito na via extrajudicial.
- **Prestações sucessivas**: depositar cada uma em até 5 dias do vencimento, no mesmo processo (art. 541).
- **Complementação**: alegada insuficiência, o autor pode completar em 10 dias, salvo se o inadimplemento da prestação acarretar a rescisão do contrato (art. 545).
- Contagem em dias úteis ou corridos conforme a natureza do prazo: `prazos-processuais`.

## Estrutura da peça
Endereçamento (lugar do pagamento) → qualificação → síntese → obrigação → hipótese do art. 335 → integralidade do valor → pedido de depósito → citação para levantar ou contestar → pedidos → valor da causa. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Foro e lugar**: a consignação é requerida no lugar do pagamento (CPC, art. 540; CC, art. 337).
- **Integralidade**: o depósito deve reunir pessoas, objeto, modo e tempo exigidos para o pagamento válido (CC, art. 336). Depósito insuficiente → improcedência, porque o pagamento parcial não extingue o vínculo (Tema 967/STJ); a sentença ainda fixa o saldo e vale como título para o credor (CPC, art. 545, § 2º).
- **Dúvida sobre o credor**: citar todos os possíveis titulares (art. 547); um só comparece → decisão de plano; mais de um → extingue-se a obrigação e o processo segue entre eles (art. 548). Quem paga a um dos pretendentes sabendo do litígio assume o risco (CC, art. 344).
- **Defesa limitada do réu**: não houve recusa ou mora; recusa justa; depósito fora do prazo ou lugar; depósito não integral — este último só com indicação do valor que entende devido (art. 544).

## Fundamentos verificados
CC arts. 334 a 345, 394; CPC arts. 539 a 549; Lei 8.245/1991, art. 67; Tema 967/STJ (tese transcrita no AREsp 1.635.102); STJ, REsp 2.111.705 (art. 545, § 2º) e AgInt no AREsp 1.987.678 (arts. 547 e 548). Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Autorização para depósito da quantia ou coisa em 5 dias (art. 542, I), ou juntada do depósito extrajudicial e da recusa (art. 539, § 3º).
- Autorização para depositar as prestações que vencerem (art. 541).
- Citação do réu para levantar o depósito ou contestar (art. 542, II); na dúvida, citação de todos os pretendentes (art. 547).
- Procedência para declarar extinta a obrigação, com condenação em custas e honorários (art. 546) e despesas do depósito (CC, art. 343).
- Cessação dos juros e riscos desde o depósito (art. 540; CC, art. 337).

## Checklist pré-protocolo
- [ ] Hipótese do art. 335 identificada e provada
- [ ] Valor integral com encargos até a data do depósito (memória pelo núcleo `juros-e-correcao`)
- [ ] Foro do lugar do pagamento
- [ ] Prazo de 1 mês respeitado, se houve depósito extrajudicial recusado
- [ ] Plano para depositar cada prestação em até 5 dias do vencimento
- [ ] Todos os possíveis credores citados (hipótese de dúvida)
- [ ] Contrato conferido: o inadimplemento acarreta rescisão? (afasta a complementação do art. 545)

## Erros a evitar
- Depositar só o valor "que o cliente acha justo" sem os encargos da mora já incidente: improcedência (Tema 967).
- Usar a consignatória para impor revisão contratual ou desconto.
- Perder o prazo de 1 mês após a recusa extrajudicial e ficar sem o efeito do depósito.
- Esquecer de depositar as parcelas que vencem no curso do processo.
- Pagar a um dos credores em disputa em vez de consignar (CC, art. 344).

## Integração com o núcleo
`juros-e-correcao` (cálculo do valor integral), `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

---
name: banc-conta-aberta-indevidamente
description: >
  Redige ação declaratória de inexistência de relação jurídica cumulada com
  encerramento de conta, cancelamento de produtos vinculados e indenização,
  quando banco ou instituição de pagamento abre conta em nome do cliente sem
  que ele a tenha pedido (conta fantasma, conta laranja aberta com documentos
  falsos, conta usada para receber golpes). Fundamenta no dever de verificar a
  identidade (Res. CMN 4.753/2019), na Súmula 479 do STJ e no CDC. Use quando
  o usuário pedir para encerrar conta que não abriu, contestar conta digital
  aberta por fraudador, afastar cobrança de tarifa ou cartão de conta
  desconhecida ou responsabilizar o banco por conta aberta com seus dados.
metadata:
  area: bancario
  tipo_peca: inicial
  verificado_em: 2026-11-25
---
# Conta aberta indevidamente (conta fantasma)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: existe conta (de depósitos ou de pagamento) em nome do cliente que ele não abriu, com ou sem produtos vinculados (cartão, limite, empréstimo, chave Pix), inclusive usada por terceiros para receber dinheiro de golpes.
- Não usar:
  - O cliente abriu a conta e contesta operações nela: `banc-fraude-pix-e-transferencia-nao-autorizada`.
  - O único efeito foi negativação em bureau privado: `consumidor-negativacao-indevida`; registro no SCR: `banc-inscricao-indevida-no-scr`.
  - Vítima de golpe que pagou para conta laranja e quer acionar o banco de destino: `banc-fraude-pix-e-transferencia-nao-autorizada` (o banco de destino como réu) e, antes, `banc-med-pix-devolucao`.
  - Uso indevido de dados pessoais fora do sistema financeiro: `digital-indenizacao-por-vazamento-de-dados`.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Como descobriu a conta (cobrança, Registrato/consulta ao BC, intimação policial, bloqueio judicial, ligação de vítima de golpe).
2. Instituição, tipo de conta (depósitos ou pagamento), número, data de abertura, canal (agência, aplicativo).
3. Produtos vinculados: cartão, limite, empréstimo, chave Pix, tarifas cobradas; houve negativação ou registro no SCR?
4. A conta recebeu dinheiro de terceiros (golpes)? Há inquérito ou ação em que o cliente figure como suspeito?
5. Documentos do cliente foram perdidos, furtados ou vazados? Boletim de ocorrência.
6. Reclamações já feitas: SAC, ouvidoria, Banco Central; respostas e protocolos.

## Prazo e contagem
- Prescrição da reparação: fato do serviço e consumidor por equiparação atraem os 5 anos do art. 27 do CDC; o STJ aplicou esse prazo a empréstimos não pactuados com descontos e negativação (AREsp 2.481.029). Conte do conhecimento do dano e da autoria.
- A declaração de inexistência da relação jurídica, em si, não se sujeita a prescrição [VERIFICAR: confirmar em precedente antes de afirmar na peça].
- Prazos processuais: `prazos-processuais`.

## Estrutura da peça
Fatos (descoberta, dados da conta, efeitos) → consumidor por equiparação → dever regulatório de verificar identidade → fortuito interno → inexistência da relação e nulidade dos produtos → danos → tutela de urgência (encerramento/bloqueio, exclusão de registros) → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Polo passivo: a instituição que abriu a conta; se houve negativação por outro credor, incluí-lo.
- Prova negativa: o cliente não prova que não abriu; pedir que o banco exiba a ficha de abertura, documentos usados, selfie/biometria, IP, dispositivo e o documento interno de critérios de identificação (Res. CMN 4.753/2019, art. 8º).
- Se a conta foi usada para golpes, juntar o BO do cliente e informar o juízo criminal/delegacia; o pedido cível ajuda a afastar suspeita.

## Fundamentos verificados
- CDC arts. 6º VIII, 14, 17 (vítima do evento equiparada a consumidor), 27.
- Res. CMN 4.753/2019, art. 2º (verificar e validar identidade e autenticidade das informações, inclusive por confronto com bancos de dados) e art. 7º (integridade e autenticidade de documentos eletrônicos).
- Res. CMN 4.949/2021, art. 4º, II (segurança das transações e legitimidade das operações contratadas).
- Súmula 479/STJ; AREsp 2.949.395, que transcreve precedente da Segunda Seção citando a abertura de conta-corrente mediante fraude como fortuito interno.
- AgInt no AREsp 2.896.567 (3ª Turma, 2025): empréstimo com abertura de conta irregular; ilicitude e dano moral mantidos.
- Súmula 532/STJ, se houve envio de cartão não solicitado.
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Tutela de urgência: bloqueio ou encerramento da conta e de chaves Pix, suspensão de cobranças, exclusão de negativação/SCR, multa diária.
- Declaração de inexistência da relação jurídica e nulidade de cada produto vinculado.
- Cancelamento definitivo de débitos; restituição do que tiver sido cobrado (dobro: `consumidor-repeticao-em-dobro`).
- Dano moral com os fatos concretos (uso da conta em golpes, intimação policial, negativação).
- Exibição da documentação de abertura e dos logs; inversão do ônus.
- Juros e correção: núcleo `juros-e-correcao`.

## Checklist pré-protocolo
- [ ] Prova da existência da conta (extrato, Registrato, carta, intimação)
- [ ] BO e prova de perda/vazamento de documentos, se houver
- [ ] Todos os produtos vinculados listados
- [ ] Registros em bureaus e SCR consultados
- [ ] Pedido de exibição especificado (ficha, biometria, IP, dispositivo)
- [ ] Prescrição conferida
- [ ] Juros e correção remetidos ao núcleo

## Erros a evitar
- Pedir só o encerramento e esquecer chaves Pix, cartões, limites e registros no SCR.
- Tratar a conta de pagamento de fintech como se a Res. CMN 4.753/2019 se aplicasse sem ressalva: ela rege conta de depósitos [VERIFICAR: norma específica para conta de pagamento antes de citá-la].
- Deixar de mencionar o inquérito em que o cliente aparece como titular da conta.
- Afirmar dano moral presumido sem fatos.

## Integração com o núcleo
`juros-e-correcao`, `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

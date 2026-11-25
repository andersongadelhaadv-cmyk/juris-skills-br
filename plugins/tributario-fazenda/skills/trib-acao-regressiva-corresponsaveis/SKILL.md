---
name: trib-acao-regressiva-corresponsaveis
description: >
  Redige ação regressiva (de reembolso) de quem pagou crédito tributário como
  responsável ou devedor solidário contra o contribuinte ou os demais
  coobrigados, com base no CTN arts. 123, 124, 125, 128, 134 e 135 e no Código
  Civil arts. 283, 285, 346, III, e 349. Use quando o usuário pedir ação de
  regresso por tributo pago, reembolso de dívida fiscal paga pelo sócio,
  administrador, adquirente ou substituto tributário, cobrança da quota-parte
  de coobrigado, ressarcimento de tributo pago no redirecionamento da execução
  fiscal, ou cobrança de cláusula de indenização tributária entre partes.
metadata:
  area: tributario-fazenda
  tipo_peca: inicial
  verificado_em: 2026-11-25
---
# Ação regressiva contra corresponsáveis tributários

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: o cliente **já pagou** (no todo ou em parte) crédito tributário pelo qual respondia como responsável, solidário ou substituto, e quer recuperar do contribuinte ou dos demais coobrigados. Exemplos: sócio ou ex-sócio que quitou débito após redirecionamento; coproprietário que pagou o IPTU inteiro; adquirente ou vendedor obrigado por cláusula contratual de responsabilidade tributária; responsável por retenção que recolheu sem ter retido.
- É ação **entre particulares**: o fisco não é parte e não é atingido. O CTN art. 123 impede opor convenções particulares à Fazenda, mas não as invalida entre os contratantes.
- Não usar: discutir se o tributo era devido perante o fisco (`trib-repeticao-de-indebito`, `trib-acao-anulatoria`); defender-se do redirecionamento na execução (`trib-excecao-pre-executividade-fiscal`, `trib-embargos-a-execucao-fiscal`); cobrança contratual sem nenhum componente tributário (`civel-peticao-inicial`, `contratos-notificacao-de-descumprimento`).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Comprovante do pagamento (guia, DARE/DARF quitado, termo de parcelamento e parcelas pagas), com datas e valores.
2. Título da responsabilidade: decisão de redirecionamento, CDA com o nome do cliente, lei que atribui a responsabilidade, contrato com cláusula tributária.
3. Quem é o contribuinte e quem são os coobrigados; participação de cada um (quotas, fração ideal, cláusula de rateio).
4. Se o cliente foi responsabilizado por **ato próprio** com excesso de poderes ou infração (CTN art. 135) ou por mera solidariedade/sucessão.
5. Notificação extrajudicial ao devedor e resposta.
6. Situação patrimonial dos réus (para a utilidade da ação).

## Prazo e contagem
- Prescrição da pretensão regressiva: não conferida em fonte oficial [VERIFICAR: discute-se entre os prazos do CC art. 206 e o geral do art. 205, conforme a natureza (sub-rogação, quota-parte, cláusula contratual)]. O termo inicial mais seguro é a data de cada pagamento.
- Remeta a contagem a `prazos-processuais`; na dúvida, ajuíze dentro do prazo mais curto possível.

## Estrutura da peça
Endereçamento (Justiça comum estadual, foro do réu ou do contrato) → partes → síntese do pagamento → origem da responsabilidade do autor → fundamento do regresso (sub-rogação, quota-parte ou contrato) → cálculo por réu → pedidos. Roteiro em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Fundamento do regresso** (escolha e declare):
  - Sub-rogação legal: terceiro interessado que paga dívida pela qual era ou podia ser obrigado (CC art. 346, III) recebe os direitos, ações, privilégios e garantias do credor primitivo (art. 349). Útil quando o responsável pagou dívida que era do contribuinte (CTN arts. 128 e 134).
  - Quota-parte entre solidários: quem paga por inteiro exige de cada codevedor a sua quota (CC art. 283); se a dívida interessa só a um deles, este responde por toda ela (art. 285). Solidariedade tributária nasce do interesse comum no fato gerador ou de lei (CTN art. 124), e o pagamento de um aproveita aos demais (art. 125, I).
  - Contrato: cláusula de indenização ou rateio tributário (válida entre as partes — CTN art. 123).
- **Responsabilidade por ato próprio** (CTN art. 135): se o autor foi responsabilizado por infração que ele mesmo praticou, o regresso integral contra a sociedade ou os sócios é controvertido [VERIFICAR]; avalie antes de prometer resultado ao cliente.
- **Reconhecimento do débito pelo autor**: julgado do TJMG manteve improcedente regressiva de ICMS-ST quando o próprio autor havia reconhecido administrativamente o débito como seu (Apelação 5000780-49.2021.8.13.0172). Confira se o cliente confessou a dívida como contribuinte antes de ajuizar.
- O autor precisa provar o pagamento efetivo, não a mera inclusão na CDA.

## Fundamentos verificados
CTN arts. 123, 124, 125, 128, 134 e 135; CC arts. 283, 285, 346, III, e 349; TJMG, Apelação 5000780-49.2021.8.13.0172. Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Condenação de cada réu ao reembolso (integral, se a dívida era só dele; ou da respectiva quota), com atualização desde cada pagamento pelo núcleo `juros-e-correcao`.
- Subsidiariamente, condenação solidária dos coobrigados na parte que excede a quota do autor.
- Tutela cautelar de arresto ou indisponibilidade, se houver risco concreto de dilapidação (CPC art. 300).
- Exibição de livros, contratos e declarações fiscais em poder dos réus, se necessários ao rateio.
- Custas e honorários.

## Checklist pré-protocolo
- [ ] Todos os pagamentos comprovados, com data (termo inicial do prazo e da atualização)
- [ ] Fundamento do regresso escolhido e declarado (sub-rogação, quota-parte ou contrato)
- [ ] Origem da responsabilidade do autor documentada (CDA, decisão, lei, cláusula)
- [ ] Verificado se o autor respondeu por ato próprio (CTN art. 135) ou confessou o débito
- [ ] Planilha de rateio por réu
- [ ] Prescrição conferida em `prazos-processuais`
- [ ] Juros e correção remetidos ao núcleo

## Erros a evitar
- Incluir o fisco no polo passivo: a ação é privada e não discute o crédito perante a Fazenda.
- Cobrar o valor integral de um coobrigado sem justificar por que a dívida era só dele (CC art. 285).
- Pedir reembolso de tributo apenas inscrito ou parcelado, sem pagamento efetivo das parcelas.
- Ignorar a confissão de dívida feita pelo próprio autor em parcelamento ou denúncia espontânea.
- Fixar taxa de juros na petição: remeta ao núcleo.

## Integração com o núcleo
`juros-e-correcao`, `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

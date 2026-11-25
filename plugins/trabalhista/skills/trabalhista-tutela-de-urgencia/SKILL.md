---
name: trabalhista-tutela-de-urgencia
description: >
  Redige pedido de tutela provisória de urgência na Justiça do Trabalho (CPC
  arts. 294, 300 e 303 c/c CLT art. 769 e CPC art. 15), antecedente ou
  incidental, inclusive as liminares do art. 659, IX e X, da CLT (transferência
  abusiva e reintegração de dirigente sindical), com multa coercitiva (CPC art.
  537). Use quando o usuário pedir liminar trabalhista, tutela de urgência para
  reintegração, restabelecimento de plano de saúde, liberação de guias, sustar
  transferência ou tutela da evidência em reclamação trabalhista.
metadata:
  area: trabalhista
  tipo_peca: requerimento
  verificado_em: 2026-11-25
---
# Tutela de urgência trabalhista

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: pedido de tutela provisória (urgência ou evidência) dentro da reclamação, em tópico próprio, ou em petição incidental ou antecedente.
- Hipóteses típicas: reintegração de empregado com garantia provisória de emprego; restabelecimento de plano de saúde durante afastamento; sustação de transferência abusiva; entrega de guias e documentos rescisórios; cessação de conduta lesiva em curso.
- Não usar: atacar decisão que concedeu ou negou a tutela antes da sentença (`trabalhista-mandado-de-seguranca`); tutela concedida na sentença (impugnável por `trabalhista-recurso-ordinario`); tutela em processo cível (`civel-tutela-provisoria`).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Qual providência concreta se quer (fazer, não fazer, entregar) e em que prazo.
2. Prova documental da probabilidade do direito (TRCT, comunicado de dispensa, atestado, CAT, ata de eleição sindical, carta de transferência, carteira do plano).
3. Fato que demonstra o perigo de dano ou risco ao resultado útil (tratamento interrompido, perda de renda, prazo correndo).
4. Se a medida é reversível e se o cliente tem condição de prestar caução.
5. Se já há ação em curso (incidental) ou se a urgência é contemporânea ao ajuizamento (antecedente).

## Prazo e contagem
- Não há prazo legal para pedir tutela, mas a demora do próprio requerente enfraquece o perigo de dano: registrar datas.
- Tutela antecedente (CPC art. 303): exige aditamento posterior da inicial no prazo legal — conferir em `prazos-processuais` [VERIFICAR: compatibilidade e forma do rito antecedente no processo do trabalho].
- Contra a decisão interlocutória: mandado de segurança antes da sentença (Súmula 414, II); prazo decadencial em `prazos-processuais`.

## Estrutura da peça
Fatos urgentes → probabilidade do direito → perigo de dano → reversibilidade e caução → medida pedida, prazo e multa → pedidos. Roteiro em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Aplicação ao processo do trabalho**: CLT art. 769 e CPC art. 15.
- **Requisitos** (CPC art. 300): elementos que evidenciem a probabilidade do direito e o perigo de dano ou o risco ao resultado útil do processo.
- **Caução** (art. 300, § 1º): o juiz pode exigir; dispensável ao economicamente hipossuficiente — pedir a dispensa expressamente.
- **Liminar ou justificação prévia** (art. 300, § 2º).
- **Irreversibilidade** (art. 300, § 3º): a tutela antecipada não se concede com perigo de irreversibilidade dos efeitos; demonstrar que a reintegração é reversível (o trabalho prestado é remunerado).
- **Liminares da própria CLT** (art. 659): IX — tornar sem efeito transferência disciplinada pelos parágrafos do art. 469; X — reintegrar dirigente sindical afastado, suspenso ou dispensado.
- **Tutela da evidência** (CPC art. 311): sem perigo de dano, em abuso de defesa (I) ou inicial com prova documental suficiente dos fatos constitutivos (IV); liminar sem ouvir a reclamada só nos incisos II e III (parágrafo único).
- **Efetivação** (CPC arts. 297 e 537): multa diária com prazo razoável, desde que suficiente e compatível com a obrigação.

## Fundamentos verificados
CLT arts. 659, IX e X, e 769; CPC arts. 15, 294, 297, 300, 303, 311 e 537; Súmula 414 do TST. Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Concessão liminar, sem oitiva da parte contrária, da providência concreta (descrita com precisão), em prazo certo.
- Multa diária por descumprimento (CPC art. 537), com teto ou revisão a critério do juízo.
- Dispensa de caução, se hipossuficiente.
- Intimação da reclamada por oficial de justiça ou meio mais célere, quando a urgência justificar.
- Confirmação da tutela na sentença.

## Checklist pré-protocolo
- [ ] Providência descrita de forma executável (quem, o quê, em quanto tempo)
- [ ] Documento que prova cada requisito juntado e indicado por ID
- [ ] Perigo de dano atual, com datas (não alegação genérica)
- [ ] Reversibilidade enfrentada
- [ ] Caução: pedido de dispensa ou oferta
- [ ] Multa com prazo razoável
- [ ] Rito correto: incidental, antecedente ou tópico da inicial
- [ ] Valores, juros e correção pelo núcleo `juros-e-correcao`

## Erros a evitar
- Pedir "tutela" sem dizer exatamente o que a reclamada deve fazer.
- Perigo de dano presumido, sem fato concreto e sem datas.
- Ignorar o § 3º do art. 300 em pedido de pagamento de valores (irreversibilidade).
- Usar MS contra tutela concedida na sentença (Súmula 414, I: cabe recurso ordinário, com pedido de efeito suspensivo).
- Pedir tutela da evidência com base nos incisos I ou IV liminarmente (o parágrafo único só autoriza liminar nos incisos II e III).

## Integração com o núcleo
`prazos-processuais`, `juros-e-correcao`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

---
name: reg-pedido-outorga-licenca-agencia
description: >
  Redige requerimento administrativo de habilitação, registro, autorização,
  licença ou outorga perante agência reguladora (e pedidos correlatos de
  transferência, prorrogação e alteração), com base na Lei 13.848/2019, nos
  arts. 48 a 50 da Lei 9.784/1999 e na aprovação tácita do art. 3º, IX, da Lei
  13.874/2019. Use quando o usuário pedir requerimento de autorização ou
  registro em agência, pedido de outorga, habilitação de empresa no setor
  regulado, prorrogação ou transferência de outorga, resposta a exigência da
  agência no pedido, ou cobrança de decisão em pedido parado.
metadata:
  area: regulatorio
  tipo_peca: requerimento
  verificado_em: 2026-11-25
---
# Pedido de habilitação, licença ou outorga perante agência

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: requerimento inicial de autorização, registro, habilitação, licença ou outorga em agência reguladora; pedido de prorrogação, transferência de controle ou alteração do ato; resposta a exigência formulada no processo; petição cobrando decisão em pedido paralisado.
- Não usar:
  - Outorga por licitação (concessão ou permissão precedida de edital): impugnação em `adm-impugnacao-ao-edital`; recurso em `adm-recurso-em-licitacao`.
  - Pedido indeferido e já decidido: recurso administrativo (rito do art. 56 da Lei 9.784/1999; estrutura análoga a `reg-recurso-multa-agencia`).
  - Omissão prolongada que exige ordem judicial: `adm-mandado-de-seguranca`.
  - Licença ambiental: fora desta skill (procure o plugin ambiental).
  - Registro de operadora de plano de saúde na ANS: use esta skill, conferindo a norma própria da ANS [VERIFICAR].

## Entradas mínimas (perguntar o que faltar; nunca supor fatos)
1. Agência, tipo de ato pretendido e a lei setorial e a resolução que o disciplinam (requisitos, documentos, taxa, prazo de análise) — o advogado confere a versão vigente.
2. Dados societários: contrato/estatuto, controle direto e indireto, administradores, grupo econômico.
3. Requisitos de qualificação: técnica, econômico-financeira, jurídica e fiscal (certidões), conforme a norma.
4. Descrição do projeto ou serviço: área, capacidade, cronograma, tecnologia, abrangência geográfica.
5. Taxa ou preço público pago e guia.
6. Histórico com a agência: outorgas anteriores, sanções, pendências.
7. Urgência econômica (contrato condicionado, financiamento, prazo de leilão).

## Prazo e contagem
- Prazo de análise: o fixado pela agência para o ato; a Lei 13.874/2019 garante ao requerente ser informado do prazo máximo, e o silêncio após esse prazo importa aprovação tácita, salvo vedação legal ou as exceções do § 6º do art. 3º (art. 3º, IX, e §§ 6º a 8º). Conferir se o ato pretendido é ato de liberação de atividade econômica e se a agência regulamentou o prazo [VERIFICAR no caso].
- Sem prazo específico: decisão em até 30 dias após concluída a instrução, prorrogáveis por igual período motivadamente (Lei 9.784/1999, art. 49).
- Prazo para cumprir exigências: o fixado no ofício; contagem pela norma da agência ou pelo art. 66 da Lei 9.784/1999. Conferência: `prazos-processuais`.

## Estrutura da peça
Endereçamento → qualificação e representação → objeto (ato pretendido e base normativa) → atendimento dos requisitos, item a item → documentos → pedidos (deferimento, prazo, comunicação). Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Correspondência estrita com a norma**: montar uma matriz requisito → documento → folha. Pedido incompleto gera exigência e reinicia ou suspende a contagem conforme a regra da agência.
- **Dever de decidir**: a Administração tem o dever de emitir decisão expressa (Lei 9.784/1999, art. 48), motivada quando negar ou limitar direitos (art. 50, I).
- **Motivação e proporcionalidade**: exigências devem ter base normativa e ser proporcionais (Lei 13.848/2019, arts. 4º e 5º).
- **Segurança jurídica**: respostas a consultas e súmulas administrativas da agência vinculam o órgão até revisão (LINDB, art. 30, parágrafo único) — use-as a favor do pedido.
- **Aprovação tácita**: nunca dê por certa sem conferir a regulamentação do prazo e as exceções legais.

## Fundamentos verificados
- Lei 13.848/2019, arts. 4º e 5º.
- Lei 9.784/1999, arts. 3º, 48, 49, 50 e 66.
- Lei 13.874/2019, art. 3º, IX, e §§ 6º a 8º.
- LINDB, art. 30.
- Lei setorial e resolução da agência do caso [VERIFICAR — não conferidas nesta skill, variam por setor].
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Deferimento do ato (autorização, registro, outorga, prorrogação, transferência), com o escopo exato pretendido.
- Informação do prazo máximo de análise (Lei 13.874/2019, art. 3º, IX).
- Tramitação prioritária, se a norma admitir e houver fundamento.
- Prazo razoável para eventuais exigências, concentradas em um único ofício.
- Tratamento sigiloso de informações comerciais sensíveis, se a norma permitir, com versão pública.
- Intimações no nome do advogado.

## Checklist pré-protocolo
- [ ] Resolução vigente da agência conferida (requisitos, taxa, formulário, sistema eletrônico)
- [ ] Matriz requisito → documento completa
- [ ] Certidões dentro da validade na data do protocolo
- [ ] Taxa paga e comprovada
- [ ] Organograma societário com controle final
- [ ] Informações sigilosas separadas em anexo próprio
- [ ] Data de protocolo registrada para controle do prazo de análise

## Erros a evitar
- Protocolar sem matriz de requisitos e receber exigência que atrasa meses.
- Tratar aprovação tácita como automática sem conferir a regulamentação e o § 6º.
- Omitir controle indireto ou administradores, que a agência descobre depois e usa para indeferir.
- Deixar certidões vencerem durante as exigências.
- Expor segredo comercial no processo público por não pedir tratamento sigiloso.

## Integração com o núcleo
`prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

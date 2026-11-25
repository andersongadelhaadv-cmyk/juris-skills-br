---
name: trib-enquadramento-regime-especial
description: >
  Redige requerimento administrativo de enquadramento, habilitação ou
  concessão de regime especial de tributação ou de benefício de caráter
  individual (genérico: o regime concreto e seus requisitos vêm da lei e do
  regulamento conferidos no caso), com prova dos requisitos (CTN, art. 179),
  interpretação literal (art. 111), dever de decidir e motivar (Lei 9.784/1999,
  arts. 48 a 50) e proteção do benefício oneroso (CTN, art. 178; Súmula 544/STF).
  Use quando o usuário pedir pedido de regime especial, habilitação em regime
  tributário, reconhecimento de isenção por despacho, termo de acordo de
  regime especial ou renovação de benefício fiscal.
metadata:
  area: tributario-fazenda
  tipo_peca: requerimento
  verificado_em: 2026-11-25
---
# Requerimento de enquadramento em regime especial de tributação

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

Modelo **genérico**. Esta skill não afirma a existência, o nome, os requisitos nem os efeitos de nenhum regime específico: tudo isso sai da lei instituidora e do regulamento lidos no caso, com dispositivo e data de consulta. Sem a norma conferida, o requerimento não sai.

## Quando usar / quando não usar
- Usar: (a) habilitação ou adesão a regime especial previsto em lei federal, estadual ou municipal; (b) reconhecimento de isenção ou benefício não geral por despacho (CTN, art. 179); (c) renovação periódica de benefício; (d) termo de acordo ou regime especial de apuração, recolhimento ou obrigação acessória previsto em norma do ente.
- Não usar:
  - Opção por regime feita só por declaração ou sistema, sem requerimento: siga a norma do ente; dúvida sobre cabimento vai para `trib-parecer-tributario`.
  - Escolha entre regimes ou estrutura para usar o regime: `trib-planejamento-tributario`.
  - Indeferimento já ocorrido: recurso administrativo previsto na norma do ente (`trib-defesa-administrativa-e-carf`, quando couber) ou `trib-mandado-de-seguranca`.
  - Regimes da reforma do consumo (IBS, CBS): `trib-reforma-tributaria-ibs-cbs`.
  - Outorga regulatória de agência: `reg-pedido-outorga-licenca-agencia`.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Nome do regime e **norma instituidora** (lei, decreto, regulamento, ato normativo), com artigos.
2. Ente e órgão competente; forma de protocolo (sistema, processo eletrônico, papel).
3. Lista oficial de requisitos e documentos exigidos pela norma.
4. Dados do requerente: CNPJ, atividades, estabelecimentos, regime atual.
5. Situação fiscal: certidões, débitos, parcelamentos, processos (muitos regimes exigem regularidade — confirmar na norma).
6. Compromissos que o regime impõe (investimento, emprego, prazo, contrapartida) e se o cliente os aceita.
7. Prazo de vigência pretendido e regras de renovação.

## Prazo e contagem
- Prazo para pedir, renovar ou cumprir exigência: o da norma do regime [VERIFICAR no caso].
- Benefício por período certo exige renovação antes do término de cada período; sem ela, os efeitos cessam a partir do primeiro dia do período seguinte (CTN, art. 179, § 1º).
- Prazo para a administração decidir: o da norma específica; no âmbito federal, na falta de regra própria, a Lei 9.784/1999 (art. 49) dá até trinta dias após a instrução, prorrogáveis motivadamente. Para outros entes, conferir a lei local [VERIFICAR].
- Prazo de recurso em caso de indeferimento: o da norma específica; supletivamente, Lei 9.784/1999, art. 59, no âmbito federal. Contagem: `prazos-processuais`.

## Estrutura da peça
Endereçamento → qualificação → objeto → norma instituidora transcrita → requisitos, um a um, com prova → compromissos aceitos → pedido de decisão expressa e motivada → documentos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Competência: dirigir à autoridade que a norma indica; pedido a órgão errado atrasa ou é indeferido.
- Requisitos são de interpretação literal (CTN, art. 111): demonstrar cada um com o documento exigido, sem equivalência "por analogia".
- O despacho não gera direito adquirido e pode ser revisto se as condições deixarem de existir (CTN, art. 179, § 2º, c/c art. 155).
- Benefício concedido por prazo certo e sob condições não é livremente revogável (CTN, art. 178; Súmula 544/STF: isenção sob condição onerosa não pode ser livremente suprimida). Guardar prova do cumprimento das condições.

## Fundamentos verificados
- CTN, art. 179, caput e §§ 1º e 2º: isenção não geral efetivada por despacho, mediante requerimento que prove o preenchimento das condições e requisitos de lei ou contrato; renovação periódica; sem direito adquirido.
- CTN, art. 155: revogação de ofício quando apurado que o beneficiado não satisfazia ou deixou de satisfazer as condições; penalidade só em caso de dolo ou simulação.
- CTN, arts. 111 e 178; Súmula 544/STF.
- Lei 9.784/1999 (processo administrativo federal): art. 2º (motivação, segurança jurídica, razoabilidade), art. 48 (dever de decidir), art. 49 (prazo), art. 50, I (motivar ato que nega direito), arts. 56 e 59 (recurso).
- Norma do regime concreto: `[VERIFICAR]` até ser lida e registrada no `fontes.yaml` do trabalho.
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Deferimento do enquadramento/habilitação no regime, com indicação da norma e da vigência.
- Decisão expressa e motivada, no prazo da norma (ou da Lei 9.784/1999, art. 49, no âmbito federal).
- Intimação por meio indicado (domicílio tributário eletrônico, se adotado).
- Se houver exigência, prazo para cumpri-la antes de qualquer indeferimento.
- Efeitos a partir da data prevista na norma (não pedir retroação que a norma não preveja).

## Checklist pré-protocolo
- [ ] Norma instituidora lida no dia, com artigos transcritos
- [ ] Cada requisito com documento correspondente, na ordem da norma
- [ ] Certidões e situação fiscal conferidas na data do protocolo
- [ ] Autoridade competente e canal de protocolo corretos
- [ ] Compromissos do regime aceitos pelo cliente por escrito
- [ ] Prazo de renovação anotado na agenda do cliente
- [ ] Nenhum requisito, efeito ou alíquota afirmado sem norma conferida

## Erros a evitar
- Afirmar que o regime "reduz a carga" ou "dá direito" a algo que a norma lida não diz.
- Usar requisito de outro regime ou de outro estado como se fosse o do caso.
- Protocolar com certidão vencida ou débito não tratado quando a norma exige regularidade.
- Esquecer a renovação periódica e perder o benefício (CTN, art. 179, § 1º).
- Pedir efeito retroativo sem previsão normativa.

## Integração com o núcleo
`prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`, `juros-e-correcao`.

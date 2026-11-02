---
name: trabalhista-recurso-ordinario
description: >
  Redige recurso ordinário trabalhista contra sentença de Vara do Trabalho ou
  acórdão de TRT em competência originária (CLT art. 895), com preparo completo:
  depósito recursal (art. 899 e §§) e custas (art. 789). Use quando o usuário pedir
  recurso ordinário, RO, recorrer da sentença trabalhista, contrarrazões ao RO,
  recurso ordinário em mandado de segurança ou ação rescisória no TRT, ou calcular
  depósito recursal e custas.
metadata:
  area: trabalhista
  tipo_peca: recurso-ordinario
  verificado_em: 2026-11-02
---
# Recurso ordinário trabalhista

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: sentença definitiva ou terminativa da Vara (art. 895 I); decisão definitiva ou terminativa do TRT em competência originária, como mandado de segurança e ação rescisória (art. 895 II; Súmula 201 do TST para o MS).
- Também para contrarrazões (mesmo prazo, art. 900).
- Não usar: decisão interlocutória (em regra irrecorrível de imediato — art. 893 §1º e Súmula 214 do TST); execução (use `trabalhista-agravo-de-peticao`); causa de alçada de até 2 salários mínimos sem matéria constitucional (Lei 5.584/1970, art. 2º §4º).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
- Sentença integral, data da intimação e eventual decisão de embargos de declaração.
- Valor da condenação e das custas fixados na sentença; rito (ordinário ou sumaríssimo).
- Qual parte recorre; se empregador, porte (ME/EPP, doméstico, entidade sem fins lucrativos), gratuidade, recuperação judicial ou filantropia.
- Capítulos que se quer reformar e a prova dos autos que sustenta cada tese.

## Prazo e contagem
- 8 dias úteis (CLT art. 895; Lei 5.584/1970 art. 6º; CLT art. 775). ED interrompem o prazo (art. 897-A §3º).
- Intimação na sexta-feira: prazo começa na segunda (Súmula 1 do TST).
- Feriado local deve ser comprovado no ato da interposição (Súmula 385 do TST).
- Entes públicos que não exploram atividade econômica: prazo em dobro para recorrer (Decreto-Lei 779/1969, art. 1º III) e dispensa de depósito recursal (art. 1º IV).

## Estrutura da peça
Petição de interposição ao juízo a quo + razões ao TRT: admissibilidade (tempestividade, representação, preparo), preliminares, mérito por capítulo, pedido. Roteiro em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Depósito recursal** (art. 899): exigido do empregador condenado em pecúnia; limitado ao teto vigente fixado pelo TST e ao valor da condenação (§6º); comprovado no prazo do recurso (Súmula 245 do TST). Metade para entidade sem fins lucrativos, empregador doméstico, MEI, ME e EPP (§9º); isenção para beneficiário da gratuidade, entidade filantrópica e empresa em recuperação judicial (§10); pode ser substituído por fiança bancária ou seguro garantia (§11). Recolher integralmente em cada recurso até atingir a condenação (Súmula 128 I). O valor do teto é atualizado periodicamente por ato do TST; número do ato e valor vigente não conferidos em fonte oficial [VERIFICAR na data da interposição].
- **Custas** (art. 789): 2% sobre a condenação ou o valor arbitrado, com mínimo e máximo legais; pagas e comprovadas no prazo do recurso (§1º). Inversão de sucumbência no TRT: Súmula 25 do TST.
- **Representação**: procuração nos autos até a interposição (Súmula 383 do TST).
- **Dialeticidade**: no RO ao TRT a exigência é atenuada, salvo razões totalmente dissociadas da sentença (Súmula 422 III).
- Efeito devolutivo em profundidade: fundamentos da inicial ou da defesa não examinados sobem com o capítulo impugnado (Súmula 393 do TST).

## Fundamentos verificados
CLT arts. 789, 893, 895, 897-A, 899, 900; Lei 5.584/1970 arts. 2º e 6º; Súmulas 1, 25, 128, 201, 214, 245, 383, 385, 393, 422 do TST. Detalhes em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Conhecimento e provimento para reformar cada capítulo indicado; pedidos sucessivos se houver.
- Se a sentença for omissa num pedido e a causa estiver madura, pedir julgamento imediato pelo TRT (Súmula 393 II).
- Critério de juros e correção: se impugnado, fundamentar com `juros-e-correcao`.
- Efeito suspensivo, se necessário, por requerimento próprio ao tribunal (via indicada na Súmula 414 I do TST).

## Checklist pré-protocolo
- [ ] Prazo de 8 dias úteis conferido, com feriados locais comprovados.
- [ ] Guia e comprovante do depósito recursal (ou fundamento da redução/isenção) anexados.
- [ ] Guia e comprovante de custas anexados.
- [ ] Procuração e substabelecimentos regulares.
- [ ] Cada capítulo impugnado ataca o fundamento da sentença.
- [ ] Rito sumaríssimo: ciente de que o RO terá tramitação simplificada (art. 895 §1º).
- [ ] Juros e correção remetidos ao núcleo.

## Erros a evitar
- Recolher depósito em valor de teto desatualizado ou abaixo da condenação.
- Comprovar preparo depois do prazo.
- Recorrer de interlocutória fora das exceções da Súmula 214.
- Repetir a contestação sem enfrentar a sentença.
- Usar RO contra decisão em execução.

## Integração com o núcleo
`prazos-processuais` (8 dias úteis, feriados), `juros-e-correcao`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

---
name: adm-acao-de-improbidade
description: >
  Redige petição inicial de ação de improbidade administrativa pelo autor —
  Ministério Público ou pessoa jurídica lesada (legitimidade concorrente
  restabelecida na ADI 7.042) — sob a Lei 8.429/1992 com a redação da Lei
  14.230/2021: dolo específico, individualização da conduta, tipo único por ato
  (art. 17, § 10-D), indisponibilidade de bens (art. 16) e prescrição (art. 23).
  Use quando o usuário (procurador do Município, Estado, autarquia ou promotor)
  pedir ajuizar ação de improbidade, inicial de improbidade, ressarcimento por
  ato ímprobo doloso, bloqueio de bens de ex-gestor ou acordo de não persecução
  civil pelo autor.
metadata:
  area: administrativo-licitacoes
  tipo_peca: inicial
  verificado_em: 2026-11-25
---
# Ação de improbidade administrativa (autor)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: ente público lesado (por sua advocacia pública) ou Ministério Público que vai propor a ação contra agente público e terceiros que induziram ou concorreram dolosamente (Lei 8.429/1992, art. 3º).
- Não usar:
  - defesa do réu: `adm-defesa-em-improbidade`;
  - cidadão contra ato lesivo: `adm-acao-popular`;
  - só ressarcimento sem tipificação dolosa nos arts. 9º a 11 — avaliar ação civil pública ou ação de ressarcimento (art. 17, § 16, permite conversão);
  - sanção a empresa por ato contra a Administração em licitação na via administrativa: `adm-defesa-em-processo-sancionador-licitacao` (lado da defesa) e Lei 12.846/2013 [VERIFICAR: rito anticorrupção não coberto aqui].

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Quem propõe (MP ou pessoa jurídica interessada) e qual a pessoa jurídica lesada.
2. Réus: agentes públicos (cargo, período) e terceiros beneficiados ou partícipes.
3. Conduta de cada réu, com data, documento e o resultado ilícito visado.
4. Prova do dolo — vontade livre e consciente de alcançar o resultado ilícito (art. 1º, § 2º); mero exercício da função não basta (art. 1º, § 3º).
5. Dano: valor apurado, laudo, relatório de auditoria, tomada de contas; ou enriquecimento ilícito e seu valor.
6. Data do fato ou da cessação da conduta permanente (prescrição) e se foi antes ou depois da publicação da Lei 14.230/2021 (Tema 1199).
7. Bens conhecidos dos réus e indício concreto de dilapidação (para a indisponibilidade).
8. Procedimento prévio: inquérito civil, sindicância, processo de contas, representação do art. 7º.

## Prazo e contagem
- Prescrição: 8 anos do fato ou, na infração permanente, do dia em que cessou (art. 23, caput); interrupções do art. 23, § 4º. A recontagem do § 5º foi objeto das ADIs 7.156 e 7.236 [VERIFICAR: conferir o resultado na fonte oficial; ver `adm-defesa-em-improbidade`].
- Novo regime prescricional é irretroativo: aplica-se a partir da publicação da Lei 14.230/2021 (Tema 1199/STF).
- Ressarcimento por ato doloso tipificado na LIA é imprescritível (Tema 897/STF) — pedido de ressarcimento sobrevive à prescrição das sanções.
- Prazos processuais: `prazos-processuais`.

## Estrutura da peça (resumo; detalhe em [estrutura](references/estrutura.md))
Competência e legitimidade → réus individualizados → fatos por réu → tipificação (um tipo por ato) → dolo de cada réu → dano ou enriquecimento → sanções do art. 12 pretendidas → indisponibilidade → pedidos → provas.

## Requisitos e preliminares
- Legitimidade: MP (art. 17, caput) e pessoa jurídica interessada, de forma concorrente e disjuntiva (ADI 7.042, interpretação conforme do art. 17 e do art. 17-B). Se o autor for o MP, requerer a intimação da pessoa jurídica lesada [VERIFICAR: forma de intervenção no caso concreto].
- Foro: local do dano ou da pessoa jurídica prejudicada (art. 17, § 4º-A).
- Inicial deve individualizar a conduta de cada réu com elementos mínimos de autoria e trazer documentos ou justificação que indiquem os fatos e o dolo (art. 17, § 6º), sob pena de rejeição (art. 17, § 6º-B).
- Cada ato vinculado a um só tipo dos arts. 9º, 10 ou 11 (art. 17, § 10-D).
- Art. 10 exige perda patrimonial efetiva e comprovada; art. 11 exige conduta enquadrada nos incisos.
- Não se aplicam à ação de improbidade a presunção de veracidade na revelia nem a inversão do ônus contra o réu (art. 17, § 19).

## Fundamentos verificados (resumo; detalhe em [fundamentos](references/fundamentos.md))
- CF, art. 37, §§ 4º e 5º.
- Lei 8.429/1992: arts. 1º, §§ 1º a 4º; 2º; 3º; 7º; 9º, 10 e 11 (caput); 12; 16; 17 (§§ 4º-A, 6º, 6º-A, 6º-B, 7º, 10-C, 10-D, 16, 19); 17-B; 17-C; 21; 23.
- ADI 7.042 (legitimidade concorrente). Tema 1199/STF. Tema 897/STF.

## Pedidos e requerimentos
- Indisponibilidade de bens (art. 16), demonstrando perigo concreto (§ 3º); sem oitiva prévia só se o contraditório frustrar a medida (§ 4º); limitada ao ressarcimento integral do dano ou ao acréscimo ilícito, sem a multa (§ 10).
- Recebimento da inicial e citação para contestar em 30 dias (art. 17, § 7º).
- Condenação de cada réu às sanções do art. 12 correspondentes ao tipo, com dosimetria proposta.
- Ressarcimento integral do dano e perda dos bens acrescidos ilicitamente; atualização pelo núcleo `juros-e-correcao`.
- Provas: documental, pericial contábil, testemunhal.
- Abertura para acordo de não persecução civil (art. 17-B), indicando o mínimo exigido: ressarcimento integral e reversão da vantagem indevida.

## Checklist pré-protocolo
- [ ] Legitimidade e pessoa jurídica lesada identificadas
- [ ] Conduta e dolo descritos réu por réu, com documento
- [ ] Um único tipo por ato (§ 10-D)
- [ ] Dano efetivo quantificado (art. 10) ou vantagem indevida (art. 9º)
- [ ] Data do fato e regime prescricional (antes/depois da publicação da Lei 14.230/2021)
- [ ] Pedido de indisponibilidade com perigo concreto e limite de valor
- [ ] Sanções do art. 12 compatíveis com o tipo
- [ ] Foro do § 4º-A

## Erros a evitar
- Narrar fatos em bloco, sem separar a conduta de cada réu (rejeição pelo § 6º-B).
- Tipificar o mesmo ato em dois artigos "subsidiariamente" (§ 10-D).
- Imputar improbidade por culpa ou por mera irregularidade formal (art. 1º, §§ 1º a 3º; Tema 1199).
- Pedir indisponibilidade com urgência presumida ou incluindo a multa (art. 16, §§ 3º, 4º e 10).
- Deixar de pedir o ressarcimento quando as sanções estão prescritas (Tema 897).

## Integração com o núcleo
`prazos-processuais`, `juros-e-correcao`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

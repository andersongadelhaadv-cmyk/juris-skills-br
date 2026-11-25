---
name: contratos-nda-confidencialidade
description: >
  Redige e revisa acordo de confidencialidade (NDA), unilateral ou mútuo, para
  negociações, due diligence, parcerias, prestação de serviços e projetos de
  tecnologia, com cláusula penal calibrada, LGPD para dados pessoais e, quando
  cabível, a proteção penal e civil do art. 195, XI e XII, da Lei 9.279/1996
  (concorrência desleal). Use quando o usuário pedir um NDA, termo de sigilo,
  acordo de não divulgação, cláusula de confidencialidade em outro contrato,
  revisão de NDA recebido da outra parte ou notificação por quebra de sigilo.
metadata:
  area: contratos
  tipo_peca: contrato
  verificado_em: 2026-11-25
---
# Acordo de confidencialidade (NDA)

Ferramenta de apoio; o advogado responsável revisa todo documento antes de assinar ou enviar.

## Quando usar / quando não usar
- Usar: fase de negociação (M&A, investimento, parceria), due diligence, fornecedor que acessará informação estratégica, projeto de software, termo individual de sigilo de prestador PJ.
- Não usar: sigilo de empregado celetista (cláusula do contrato de trabalho e regras trabalhistas — fora desta skill); sigilo profissional legal (advogado, médico); proteção de invenção que deveria ser patenteada (o NDA não substitui o depósito).
- Contrato principal já em negociação: a cláusula de confidencialidade pode ir dentro dele (`contratos-licenca-de-software-e-saas`, `contratos-franquia-e-cof`, `contratos-representacao-comercial`).

## Entradas mínimas (perguntar o que faltar; nunca supor fatos)
1. Quem revela e quem recebe; se o fluxo é de mão única (unilateral) ou de mão dupla (mútuo).
2. Finalidade exata para a qual a informação pode ser usada.
3. Tipos de informação (técnica, comercial, financeira, dados pessoais, código-fonte).
4. Quem do lado receptor pode acessar (empregados, assessores, financiadores, grupo econômico).
5. Prazo da negociação e por quanto tempo o sigilo deve durar depois.
6. Se haverá dados pessoais e de que categoria.
7. Sanção desejada (multa fixa, perdas e danos, ambos) e foro ou arbitragem.
8. Se há elemento estrangeiro (lei, idioma, foro).

## Prazos relevantes
- Prazo do acordo e prazo de sobrevivência do sigilo após o término: defina os dois separadamente; para segredo de negócio, o sigilo pode durar enquanto a informação mantiver esse caráter.
- Devolução ou destruição: prazo em dias contados do pedido ou do término, com declaração escrita.
- Prescrição da pretensão indenizatória por quebra: não conferida para o caso típico [VERIFICAR: prazo aplicável à responsabilidade contratual].
- Prazos judiciais: `prazos-processuais`.

## Estrutura do documento
Partes → considerandos e finalidade → definição de informação confidencial → exceções → obrigações do receptor → pessoas autorizadas → divulgação exigida por lei ou ordem judicial → dados pessoais → propriedade e ausência de licença → devolução e destruição → prazo e sobrevivência → sanções → disposições gerais e foro. Roteiro em [estrutura](references/estrutura.md).

## Riscos e cláusulas sensíveis
- **Definição.** "Toda informação trocada" é ampla demais e difícil de provar; prefira categorias + marcação + confirmação escrita de informação oral em prazo curto, sem perder a cláusula de informação "que pela natureza se presume confidencial".
- **Exceções clássicas.** Informação já pública, já conhecida do receptor, recebida legitimamente de terceiro ou desenvolvida de forma independente; o ônus de provar a exceção deve ficar com o receptor.
- **Finalidade vinculada.** Proíba o uso fora da finalidade, não só a divulgação; é o uso que gera a vantagem concorrencial.
- **Cláusula penal.** Não pode exceder a obrigação principal (CC, art. 412) e pode ser reduzida se manifestamente excessiva (art. 413). Indenização suplementar só se pactuada; nesse caso a multa vale como mínimo (art. 416, parágrafo único). Para o lado que revela, pactue a suplementar.
- **Concorrência desleal.** Divulgar ou explorar informação confidencial obtida por relação contratual, mesmo após o término, é crime (Lei 9.279/1996, art. 195, XI), assim como obtê-la por meio ilícito ou fraude (XII); a ação civil é independente (art. 207), e o dano se mede pelos benefícios que o prejudicado teria auferido (art. 208). Informação pública ou evidente para um técnico no assunto fica fora do tipo — por isso a definição contratual deve ser mais ampla que o tipo penal.
- **Não concorrência e não aliciamento.** São obrigações diferentes do sigilo e exigem limites de prazo, território e objeto [VERIFICAR: nenhum precedente sobre parâmetros encontrado no JuriBase em 2026-11-25]. Não as esconda dentro do NDA sem negociação expressa.
- **Dados pessoais.** Compartilhamento de dados de clientes ou empregados na due diligence exige base legal (LGPD, art. 7º), segurança (art. 46) e definição de papéis (art. 5º, VI e VII). Prefira dados anonimizados ou agregados.
- **Paridade.** Entre empresas, presume-se contrato paritário e respeita-se a alocação de riscos (CC, art. 421-A; Lei 13.874/2019, art. 3º, VIII).

## Fundamentos verificados
- CC: arts. 412, 413, 416, 421, 421-A e 422.
- Lei 9.279/1996: arts. 195, XI e XII, e § 1º; 207, 208 e 209.
- LGPD: arts. 5º (VI e VII), 7º e 46. Lei 13.874/2019, art. 3º, VIII.
- Nenhum precedente sobre NDA ou art. 195, XI, foi encontrado no JuriBase em 2026-11-25.
Detalhe em [fundamentos](references/fundamentos.md).

## Checklist antes de assinar/enviar
- [ ] Unilateral ou mútuo conforme o fluxo real de informação
- [ ] Finalidade descrita de forma específica
- [ ] Definição por categorias, com regra para informação oral
- [ ] Exceções com ônus da prova no receptor
- [ ] Pessoas autorizadas e responsabilidade do receptor por elas
- [ ] Rito para ordem judicial (aviso prévio à parte que revelou)
- [ ] Cláusula penal dentro do limite do art. 412 e indenização suplementar decidida
- [ ] Prazo do acordo e de sobrevivência separados
- [ ] Dados pessoais tratados ou excluídos
- [ ] Encargos de mora remetidos ao núcleo `juros-e-correcao`

## Erros a evitar
- Usar NDA mútuo quando só uma parte revela (enfraquece a posição de quem revela).
- Multa genérica de valor desproporcional, convidando a redução judicial.
- Esquecer o uso indevido e proibir apenas a divulgação.
- Prazo de sigilo que se encerra junto com o acordo, deixando o segredo exposto.
- Incluir não concorrência sem prazo, área e objeto.

## Integração com o núcleo
`verificacao-de-citacoes`, `fidelidade-factual` (descrição da finalidade e das partes), `estilo-forense`, `juros-e-correcao` (multa e mora), `prazos-processuais` (se houver medida judicial).

---
name: desp-contrato-de-agenciamento
description: >
  Elabora, revisa ou analisa a validade do contrato de agenciamento,
  intermediação e representação esportiva entre atleta (ou clube) e agente,
  com remuneração, exclusividade, prazo e nulidades do art. 27-C da Lei
  9.615/1998 e do art. 95 da Lei 14.597/2023. Use quando o usuário pedir
  contrato com empresário ou agente de jogador, procuração para intermediar
  transferência, cobrança de comissão de agente, rompimento com agente,
  gerenciamento de carreira de atleta menor ou parecer sobre cláusula abusiva
  em contrato de agência esportiva.
metadata:
  area: desportivo
  tipo_peca: contrato
  verificado_em: 2026-11-25
---
# Contrato de agenciamento esportivo

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: minuta ou revisão do contrato entre atleta e agente (intermediação de contratos e gerenciamento de carreira), ou entre clube e intermediário; parecer sobre validade de cláusulas; notificação de rompimento; roteiro de cobrança de comissão.
- Não usar:
  - representação comercial de produtos ou agência empresarial comum: `contratos-representacao-comercial` ou `contratos-agencia-e-distribuicao`;
  - contrato de imagem ou patrocínio do atleta: `desp-patrocinio-e-cessao-de-imagem`;
  - contrato de trabalho com o clube: `desp-contrato-especial-de-trabalho-esportivo`;
  - ação de cobrança já pronta para ajuizar: use esta skill para a tese e `civel-peticao-inicial` ou `civel-acao-monitoria` para a peça.

## Entradas mínimas (perguntar o que faltar; nunca supor fatos)
1. Quem contrata quem: atleta x agente; clube x agente; ou ambos (risco de conflito de interesses).
2. Idade do atleta (menor de 18 anos muda tudo — art. 27-C, VI, da Lei Pelé).
3. Agente é pessoa natural ou jurídica? Tem licença ou registro na entidade da modalidade ou na federação internacional? É parente de 1º grau, cônjuge ou advogado do atleta (art. 95, § 1º, da LGE)?
4. Modalidade e regulamento de agentes aplicável (entidade nacional e federação internacional).
5. Objeto: só intermediação de um negócio, ou gerenciamento de carreira? Abrange imagem e patrocínios?
6. Remuneração: percentual, base de cálculo (salário, luvas, transferência), quem paga, quando.
7. Prazo, exclusividade, renovação, multa e foro pretendidos.
8. Para cobrança: contrato, negócio concluído, valores recebidos pelo atleta ou clube, data do vencimento.

## Prazo e contagem
- Prazo do contrato: a Lei Pelé e a LGE vigentes não fixam prazo máximo para o agenciamento. O antigo § 7º do art. 28 da Lei Pelé (procuração de no máximo um ano) aparece riscado no texto compilado; não o cite como vigente. Conferir prazo máximo no regulamento da modalidade [VERIFICAR: regulamento de agentes vigente da entidade/federação].
- Prescrição da cobrança de comissão fixada em instrumento particular: 5 anos para dívida líquida (CC, art. 206, § 5º, I); sem liquidez, avaliar outros prazos do art. 206 ou o geral do art. 205 [VERIFICAR conforme o caso].
- Prazos processuais: `prazos-processuais`.

## Estrutura do contrato
Qualificação e licença → objeto (intermediação e/ou gerenciamento) → poderes e limites → deveres do agente (diligência, informação, prestação de contas, ausência de conflito) → remuneração e base de cálculo → prazo e exclusividade → confidencialidade e dados → extinção e efeitos (negócios em curso) → conformidade com regulamentos → solução de conflitos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares (nulidades)
São nulos os contratos do atleta com agente e as cláusulas ou procurações que (Lei Pelé, art. 27-C):
- resultem vínculo desportivo;
- impliquem vinculação ou exigência de receita da entidade decorrente de transferência;
- restrinjam a liberdade de trabalho desportivo;
- estabeleçam obrigações abusivas ou desproporcionais;
- violem a boa-fé objetiva ou o fim social do contrato;
- versem sobre gerenciamento de carreira de atleta em formação menor de 18 anos.
Também são nulas cláusulas de terceiros que possam intervir nas transferências ou interferir no desempenho do atleta ou do clube, salvo norma coletiva (art. 27-B).
- Agente: pessoa natural ou jurídica que intermedeia contratos esportivos e agencia carreiras (LGE, art. 95, caput); a atuação segue os regulamentos da organização de administração e da federação internacional (§ 2º), que fiscaliza o exercício e informa à Receita os valores das transferências (§ 3º).
- Parentes de 1º grau, cônjuge e advogado do atleta podem representá-lo sem registro ou licença, se outorgados expressamente (§ 1º).

## Fundamentos verificados
- Lei Pelé, arts. 27-B e 27-C; LGE, art. 95.
- CC, arts. 653 (mandato), 710 (agência), 722 (corretagem) — qualificar o contrato conforme o objeto; arts. 205 e 206, § 5º, I (prescrição).
- TJRS, 16ª Câmara Cível, 5014293-56.2022.8.21.0001 (embargos de declaração em apelação; comissão sobre transferência de atleta) e TJSP, Conflito de Competência 0037627-04.2024.8.26.0000 (cobrança de comissão de agenciamento de atleta): exemplos de cobranças processadas na Justiça comum.
Detalhe em [fundamentos](references/fundamentos.md).

## Cláusulas essenciais
- Objeto delimitado (quais negócios; se inclui imagem e patrocínio) e poderes expressos.
- Remuneração com base de cálculo clara e momento do fato gerador (negócio concluído); vedado receber do atleta e do clube no mesmo negócio sem consentimento informado.
- Prestação de contas e repasse dos valores recebidos em nome do atleta, com prazo.
- Exclusividade razoável, com saída por justa causa; multa proporcional (risco de nulidade por desproporção — art. 27-C, IV).
- Nenhuma cláusula que dê ao agente participação em transferência ou direitos econômicos do atleta (art. 27-C, I e II).
- Atleta menor: não contratar gerenciamento de carreira; se houver apenas intermediação pontual, assistência dos responsáveis e checagem do regulamento [VERIFICAR].
- Proteção de dados pessoais e de saúde do atleta.
- Foro ou arbitragem; lei aplicável e regulamento de agentes incorporado por referência.

## Checklist pré-assinatura
- [ ] Idade do atleta conferida (menor de 18: sem gerenciamento de carreira)
- [ ] Licença/registro do agente ou enquadramento no art. 95, § 1º, da LGE
- [ ] Nenhuma cláusula sobre vínculo desportivo ou receita de transferência
- [ ] Remuneração, base de cálculo e fato gerador definidos
- [ ] Multa e exclusividade proporcionais
- [ ] Dupla representação vedada ou consentida por escrito
- [ ] Regulamento de agentes da modalidade conferido na versão vigente
- [ ] Juros e correção da cobrança remetidos ao núcleo

## Erros a evitar
- Tratar o agenciamento como relação de emprego ou levá-lo à Justiça do Trabalho sem examinar a natureza do pedido.
- Prever percentual sobre "qualquer transferência futura" do atleta: atinge receita de transferência e esbarra no art. 27-C, II.
- Assinar gerenciamento de carreira com atleta de 16 ou 17 anos.
- Citar o antigo prazo de um ano para procuração (dispositivo substituído).
- Esquecer de regular os negócios em curso na data da extinção (comissão de "cauda").

## Integração com o núcleo
`juros-e-correcao`, `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

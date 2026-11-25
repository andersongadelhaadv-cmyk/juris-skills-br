---
name: imob-incorporacao-imobiliaria
description: >
  Elabora parecer e checklist de registro e compliance de incorporação
  imobiliária: memorial de incorporação e documentos do art. 32 da Lei
  4.591/1964, validade do registro, prazo de carência, quadro-resumo, regime do
  patrimônio de afetação (arts. 31-A a 31-F), prazo de tolerância de entrega e
  regras de desfazimento (art. 67-A). Use quando o usuário pedir para preparar
  ou revisar o registro de incorporação, auditar se a incorporadora pode
  vender unidades na planta, instituir patrimônio de afetação, revisar
  contrato de unidade em construção ou avaliar risco de atraso e distrato.
metadata:
  area: imobiliario
  tipo_peca: parecer
  verificado_em: 2026-11-25
---
# Incorporação imobiliária — registro e compliance

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: (a) montagem ou auditoria do memorial de incorporação; (b) parecer sobre a possibilidade de comercializar unidades; (c) instituição e gestão do patrimônio de afetação; (d) revisão do contrato-padrão e do quadro-resumo; (e) análise de risco de atraso, desistência e distrato, pelo lado da incorporadora ou do adquirente.
- Não usar: loteamento de terrenos (`imob-loteamento-irregular-defesa-do-adquirente`); ação do consumidor por atraso ou vício já ajuizada (`consumidor-acao-indenizatoria`, `consumidor-vicio-do-produto-ou-servico`); revisão geral de contrato não imobiliário (`contratos-analise-e-revisao-de-contrato`); distrato ou resolução já em negociação ou litígio (`imob-distrato-imobiliario`); tributos da incorporação (`trib-*`).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Quem é o cliente: incorporadora, construtora, proprietário do terreno, adquirente, comissão de representantes, financiador.
2. Título do terreno (matrícula atualizada) e situação do incorporador perante o art. 31 (proprietário, promitente comprador, mandatário).
3. Projeto aprovado, alvará, cálculo de áreas, memorial descritivo, orçamento.
4. Se há registro do memorial: data e número; se já houve venda, financiamento ou início de obra.
5. Se há prazo de carência declarado e quando termina.
6. Se o patrimônio de afetação foi ou será constituído (termo averbado?).
7. Contrato-padrão e quadro-resumo; prazo de entrega e cláusula de tolerância.
8. Para conflito: cronograma real, parcelas pagas, causa do atraso ou da inadimplência.

## Prazo e contagem
- Validade do registro da incorporação: **180 dias**; não concretizada (venda/oneração de unidade, financiamento ou início das obras), o incorporador só negocia após averbar certidões e documentos atualizados, a cada 180 dias (art. 33).
- Carência para desistência: fixada na declaração do art. 32, "n"; não ultrapassa a validade do registro; **improrrogável**; desistência comunicada por escrito ao Registro e a cada adquirente (art. 34).
- Exame pelo Oficial: **10 dias úteis** para exigências e mais 10 para a certidão (art. 32, § 6º).
- Contratos definitivos: prazo do art. 35 contado do fim da carência [VERIFICAR: a página oficial indica 45 dias no texto e nota de ampliação para 60 dias pela Lei 4.864/1965].
- Tolerância de entrega: até **180 dias corridos**, se pactuada de forma clara e destacada (art. 43-A).
- Restituição no desfazimento com afetação: até 30 dias após o habite-se; sem afetação: parcela única após 180 dias do desfazimento (art. 67-A, §§ 5º e 6º).
- Prazos processuais: `prazos-processuais`.

## Estrutura da peça
Parecer: consulta → documentos examinados → diagnóstico do registro (art. 32) → validade e carência → patrimônio de afetação → contrato e quadro-resumo → riscos (atraso, distrato, hipoteca, crimes) → conclusão com pendências. Roteiro e checklist em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Venda só após o registro do memorial** com os documentos do art. 32 (título, certidões, histórico vintenário, projeto aprovado, cálculo de áreas, memorial descritivo, orçamento, instrumento de divisão em frações ideais, minuta de convenção, declaração de carência, vagas de garagem etc.).
- **Publicidade**: número do registro e cartório em anúncios, contratos e propostas, salvo classificados (art. 32, § 3º).
- **Ônus fiscais ou reais** não impedem o registro, desde que constem dos extratos (art. 32, § 5º).
- **Patrimônio de afetação** (arts. 31-A a 31-F): opcional; constituído por termo averbado; separa terreno e acessões, que só respondem pelas dívidas da própria incorporação; não se sujeita à falência do incorporador; exige conta própria, demonstrativos trimestrais e acesso da comissão e do fiscal.
- **Quadro-resumo obrigatório** no início dos contratos (art. 35-A).
- **Hipoteca do financiamento da obra** não tem eficácia perante adquirentes (Súmula 308/STJ).
- **Infrações**: negociar frações sem cumprir a Lei é contravenção (art. 66, I); afirmação falsa sobre a construção ou a alienação é crime (art. 65).

## Fundamentos verificados
- Lei 4.591/1964: arts. 28, parágrafo único; 29; 31; 31-A a 31-F; 32; 33; 34; 35, §§ 4º e 5º; 35-A; 43; 43-A; 65; 66, I; 67-A.
- STJ: Súmulas 308 e 543; Tema 1.466 (afetado — retenção de até 50% sob afetação).
Detalhe em [fundamentos](references/fundamentos.md).

## Cláusulas e providências essenciais
- Termo de afetação averbado, se adotado, e rotina de conta segregada e relatórios trimestrais.
- Declaração de carência com condições objetivas de desistência.
- Quadro-resumo completo: preço, entrada, corretagem, índices, consequências do desfazimento, prazo de entrega e do habite-se, ônus e dados do registro.
- Cláusula de tolerância clara e destacada (art. 43-A); indenização de 1% ao mês sobre o valor pago se excedida e não houver resolução (§ 2º).
- Cláusula de desfazimento dentro dos tetos do art. 67-A (corretagem integral + pena até 25%, ou até 50% sob afetação), sem índices fora do pactuado; cálculo pelo núcleo `juros-e-correcao`.

## Checklist pré-protocolo
- [ ] Matrícula do terreno e legitimidade do incorporador (art. 31)
- [ ] Todos os documentos do art. 32 presentes e atualizados
- [ ] Validade de 180 dias e revalidações controladas (art. 33)
- [ ] Carência declarada, dentro da validade, sem prorrogação (art. 34)
- [ ] Afetação: termo averbado e rotinas do art. 31-D implementadas
- [ ] Quadro-resumo conforme art. 35-A
- [ ] Publicidade com número do registro (art. 32, § 3º)
- [ ] Hipotecas e ônus mapeados; Súmula 308 considerada
- [ ] Tema 1.466 conferido antes de opinar sobre retenção

## Erros a evitar
- Lançar vendas antes do registro do memorial (contravenção do art. 66, I).
- Deixar o registro caducar após 180 dias sem revalidação e continuar vendendo.
- Prorrogar a carência ou desistir sem comunicar cada adquirente (art. 34, §§ 4º e 6º).
- Afirmar que o adquirente sempre perde 50%: o teto majorado vale só sob afetação e está em discussão no Tema 1.466 [VERIFICAR mérito].
- Cobrar pena ou reter valores quando a culpa é da incorporadora (Súmula 543: restituição integral).
- Opinar com índice ou taxa sem o núcleo `juros-e-correcao`.

## Integração com o núcleo
`juros-e-correcao`, `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

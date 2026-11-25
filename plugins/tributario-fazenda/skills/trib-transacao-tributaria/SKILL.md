---
name: trib-transacao-tributaria
description: >
  Orienta e redige pedido de transação tributária federal (Lei 13.988/2020 e CTN
  art. 171) — por adesão a edital, proposta individual do devedor ou transação
  no contencioso —, com análise de capacidade de pagamento, limites de desconto
  e prazo, compromissos e rescisão. Use quando o usuário pedir transação
  tributária, acordo com a PGFN ou com a Receita, desconto em multa e juros de
  dívida ativa, uso de prejuízo fiscal ou precatório para quitar débito, edital
  de transação ou defesa contra rescisão de transação.
metadata:
  area: tributario-fazenda
  tipo_peca: requerimento
  verificado_em: 2026-11-25
---
# Transação tributária (Lei 13.988/2020)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: (a) débito inscrito em dívida ativa da União, de autarquias e fundações federais; (b) crédito em contencioso administrativo fiscal federal (transação proposta pela Receita, art. 10-A); (c) edital de contencioso de relevante e disseminada controvérsia (art. 16); (d) contencioso de pequeno valor (arts. 23 a 25); (e) impugnação à rescisão (art. 4º, § 1º).
- Estados e Municípios: só se houver lei local de transação (CTN art. 171 exige lei); use esta skill como roteiro e aplique a lei do ente.
- Não usar: quando o débito é indevido e a tese é forte — a transação exige confissão irrevogável e renúncia às alegações de direito (art. 3º); avalie `trib-defesa-administrativa-e-carf`, `trib-acao-anulatoria` ou `trib-embargos-a-execucao-fiscal`. Só parcelar, sem desconto: `trib-parcelamento-e-regularizacao`.

## Entradas mínimas (perguntar o que faltar; nunca supor fatos)
1. Extrato dos débitos por órgão (Receita, PGFN, PGF), situação, valor principal e acessórios, garantias e execuções.
2. Porte do devedor (pessoa física, ME/EPP, demais), recuperação judicial ou falência.
3. Edital aberto conferido no dia (número, prazo de adesão, débitos elegíveis) — ou opção por proposta individual.
4. Dados de capacidade de pagamento (faturamento, endividamento, ativos) — base da classificação de recuperabilidade.
5. Prejuízo fiscal e base negativa de CSLL disponíveis; precatórios ou créditos transitados em julgado.
6. Ações e defesas em curso sobre os débitos (serão desistidas).

## Prazo e contagem
- Adesão: dentro do prazo do edital (conferir no dia; não presumir prorrogação).
- Impugnação à rescisão: 30 dias (art. 4º, § 1º).
- Após rescisão: vedada nova transação por 2 anos (art. 4º, § 4º).
- A proposta, por si, não suspende a exigibilidade nem a execução (art. 12); a suspensão vem da proposta **aceita** (CTN art. 151, VIII, LC 236/2026).
- Prazos processuais: `prazos-processuais`.

## Estrutura da peça
Proposta individual: qualificação → débitos → situação econômica e recuperabilidade → proposta (descontos, prazo, entrada, garantias, uso de prejuízo fiscal/precatório) → compromissos → pedidos. Adesão: checagem de elegibilidade → simulação → termo. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Compromissos mínimos (art. 3º): não usar a transação para prejudicar a concorrência, não ocultar bens por interposta pessoa, desistir de impugnações e recursos administrativos, renunciar às alegações de direito nas ações judiciais. A proposta deferida é confissão irrevogável (art. 3º, § 1º); a extinção dos créditos só ocorre com o cumprimento integral (§ 3º).
- Limites (art. 11, § 2º): vedada redução do principal; redução máxima de 65% do total; prazo máximo de 120 meses. Pessoa natural, ME e EPP: até 70% e 145 meses (§ 3º). Prejuízo fiscal e base negativa de CSLL: até 70% do saldo remanescente após descontos (art. 11, IV).
- Vedações (art. 5º): multas de natureza penal; Simples Nacional sem lei complementar autorizativa; FGTS sem autorização do Conselho Curador; devedor contumaz conforme lei específica.
- Não há restituição nem compensação de valores já pagos (art. 7º) e a proposta aceita não implica novação (art. 12, § 3º).
- Rescisão (art. 4º): descumprimento, esvaziamento patrimonial, falência, fraude etc.; restabelece a cobrança integral, deduzidos os pagamentos (§ 3º).

## Fundamentos verificados
- CTN arts. 151, VIII; 171.
- Lei 13.988/2020, arts. 1º a 5º, 7º, 10, 10-A, 11, 12, 16 a 20, 23 a 25 (redações das Leis 14.375/2022 e 14.689/2023).
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Deferimento da transação nos termos propostos (ou adesão ao edital nº ...).
- Subsidiariamente, contraproposta com indicação objetiva dos pontos negociáveis.
- Suspensão da execução fiscal por convenção das partes, após o aceite (art. 12, §§ 1º e 2º).
- Uso de prejuízo fiscal/base negativa e de precatórios, com documentação.
- Valores e encargos: núcleo `juros-e-correcao` (não calcular desconto sem o demonstrativo oficial).

## Checklist pré-protocolo
- [ ] Edital ou ato de proposta individual conferido na fonte oficial, no dia
- [ ] Cliente ciente da confissão irrevogável e das desistências/renúncias
- [ ] Teses fortes avaliadas antes de renunciar
- [ ] Limites de desconto e prazo conferidos com o porte do devedor
- [ ] Garantias e execuções mapeadas
- [ ] Fluxo de caixa compatível com as parcelas (rescisão bloqueia nova transação por 2 anos)

## Erros a evitar
- Tratar a proposta como suspensiva antes do aceite.
- Prometer redução do principal (vedada).
- Aderir sem avisar o cliente de que as ações em curso serão extintas com resolução de mérito.
- Afirmar que um edital está aberto sem conferir a data.
- Aplicar a lei federal a débito estadual ou municipal.

## Integração com o núcleo
`juros-e-correcao`, `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`. Vizinhas: `trib-parcelamento-e-regularizacao`, `trib-habilitacao-de-credito-judicial` (precatório como moeda), `trib-embargos-a-execucao-fiscal`.

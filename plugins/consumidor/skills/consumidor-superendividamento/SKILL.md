---
name: consumidor-superendividamento
description: >
  Redige o pedido de repactuação de dívidas do consumidor superendividado
  (CDC arts. 54-A e 104-A a 104-C, incluídos pela Lei 14.181/2021), com plano de
  pagamento em até 5 anos e preservação do mínimo existencial (Decreto 11.150/2022,
  alterado pelo Decreto 11.567/2023). Use quando o usuário pedir ação de
  superendividamento, repactuação ou renegociação judicial de dívidas, plano de
  pagamento com todos os credores, audiência global de conciliação, "lei do
  superendividamento" ou proteção do mínimo existencial contra descontos.
metadata:
  area: consumidor
  tipo_peca: inicial
  verificado_em: 2026-11-02
---
# Superendividamento — repactuação de dívidas

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: consumidor **pessoa natural, de boa-fé**, impossibilitado de pagar o conjunto de dívidas de consumo exigíveis e vincendas sem comprometer o mínimo existencial (art. 54-A § 1º).
- Não usar: dívidas contraídas com fraude/má-fé, dolo de não pagar ou aquisição de produtos/serviços de luxo de alto valor (art. 54-A § 3º). Também ficam fora da repactuação: crédito com garantia real, financiamento imobiliário e crédito rural (art. 104-A § 1º) — listar, mas não incluir no plano.
- Discussão de uma única cláusula abusiva: `consumidor-contratos-bancarios-revisional`.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Renda mensal líquida comprovada (holerites, extratos de benefício) e composição familiar.
2. Despesas básicas mensais (moradia, alimentação, saúde, educação, transporte) com comprovantes.
3. Lista de **todos** os credores: natureza da dívida, contrato, saldo, parcela, garantias, descontos em folha/conta.
4. Origem do endividamento (boa-fé: desemprego, doença, redução de renda etc.).
5. Ações e negativações em curso.
6. Proposta de plano: valor mensal disponível, prazo (máx. 5 anos), ordem e proporção entre credores.
7. Se já houve repactuação homologada: data da liquidação (repetição só após 2 anos — art. 104-A § 5º).

## Prazo e contagem
- Plano consensual: prazo máximo de 5 anos (art. 104-A caput).
- Plano judicial compulsório: primeira parcela em até 180 dias da homologação; liquidação total em até 5 anos após a quitação do plano consensual; credores recebem ao menos o principal corrigido (art. 104-B § 4º).
- Credores citados na fase compulsória: 15 dias para documentos e razões (art. 104-B § 2º); administrador: até 30 dias para o plano (§ 3º).
- Mínimo existencial: **R$ 600,00** mensais (Decreto 11.150/2022, art. 3º, na redação do Decreto 11.567/2023). O STF (ADPFs 1.005, 1.006 e 1.097, julg. 23/04/2026) deu interpretação conforme ao § 3º do art. 3º, determinou estudos anuais do CMN sobre a atualização do valor e declarou inconstitucional a exclusão do consignado do cômputo (art. 4º, p.ú., I, "h"). **Confirmar na data do protocolo se houve novo decreto ou atualização.**

## Estrutura da peça
Fatos e boa-fé → enquadramento (art. 54-A) → quadro de dívidas (incluídas e excluídas) → orçamento e mínimo existencial → plano de pagamento → pedido de audiência global (art. 104-A) → pedido subsidiário de processo compulsório (art. 104-B) → tutelas. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Procedimento **bifásico**: primeiro a audiência conciliatória com todos os credores (art. 104-A); só depois, frustrada a conciliação, o processo de revisão e repactuação compulsória (art. 104-B), a pedido do consumidor.
- O plano precisa ser **viável** e mostrar quitação integral em até 5 anos, preservado o mínimo existencial e com proporcionalidade entre credores — proposta que só limita descontos é insuficiente (REsp 2.231.246).
- Fase conciliatória pode ocorrer no Procon/órgãos do SNDC (art. 104-C).

## Fundamentos verificados
- CDC arts. 4º IX e X; 6º XI e XII; 54-A a 54-G; 104-A a 104-C.
- Decreto 11.150/2022, art. 3º (redação do Decreto 11.567/2023): mínimo existencial de R$ 600,00; art. 4º: dívidas fora do cômputo — sem a alínea "h" do inciso I do parágrafo único (consignado), declarada inconstitucional nas ADPFs 1.005, 1.006 e 1.097.
- STJ: sanções do art. 104-A § 2º só para ausência injustificada ou procurador sem poderes; não há obrigação legal de o credor aderir ou contrapropor (REsp 2.188.689).
- STJ: exigência de plano viável com quitação em 5 anos (REsp 2.231.246).
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Instauração do processo de repactuação e designação de audiência global com todos os credores do art. 54-A, com advertência do art. 104-A § 2º.
- Homologação do plano (sentença com eficácia de título executivo — art. 104-A § 3º), com os itens do § 4º (dilação, redução de encargos, suspensão/extinção de ações, data de exclusão dos cadastros).
- Subsidiariamente: instauração do processo por superendividamento (art. 104-B), citação dos credores remanescentes, nomeação de administrador.
- Tutela de urgência para limitar descontos que invadem o mínimo existencial e suspender negativações, demonstrando o risco concreto.
- Gratuidade de justiça, se cabível.
- Correção dos valores do plano: `juros-e-correcao` apenas se houver condenação; o plano compulsório usa correção por índices oficiais (art. 104-B § 4º).

## Checklist pré-protocolo
- [ ] Todos os credores listados (omitir credor fragiliza o plano)
- [ ] Dívidas excluídas (garantia real, imobiliário, rural, dolosas, luxo) separadas
- [ ] Renda e despesas comprovadas por documentos
- [ ] Plano mostra quitação integral em até 60 meses (planilha)
- [ ] Mínimo existencial conferido na regulamentação vigente na data
- [ ] Narrativa de boa-fé com prova da causa do endividamento
- [ ] Pedido bifásico (104-A, subsidiariamente 104-B)
- [ ] Verificado se há repactuação anterior (art. 104-A § 5º)

## Erros a evitar
- Propor plano que não quita a dívida em 5 anos ou que apenas limita descontos a um percentual da renda.
- Pedir direto o plano compulsório sem passar pela conciliação.
- Pedir sanção do § 2º contra credor que compareceu com poderes e só recusou o plano.
- Incluir financiamento imobiliário ou dívida com garantia real no plano.
- Tratar o mínimo existencial como valor fixo eterno sem conferir a regulamentação vigente.
- Deixar as parcelas de consignado fora do cálculo do mínimo existencial com base no art. 4º, p.ú., I, "h", do Decreto 11.150 (dispositivo declarado inconstitucional pelo STF).

## Integração com o núcleo
`juros-e-correcao`, `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

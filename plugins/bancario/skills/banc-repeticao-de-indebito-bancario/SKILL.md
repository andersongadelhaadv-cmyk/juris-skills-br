---
name: banc-repeticao-de-indebito-bancario
description: >
  Redige ação de repetição de indébito contra banco por lançamentos debitados
  na conta sem causa válida (tarifas e cestas sem pactuação expressa, seguros e
  títulos não contratados, débitos automáticos não autorizados), inclusive
  para correntista pessoa jurídica fora do CDC (CC arts. 876 e 877; Súmula 322
  do STJ), com a cumulação obrigatória de tudo na mesma ação (Tema 1.268 do
  STJ). Use quando o usuário pedir devolução de tarifas cobradas na conta,
  estorno de seguro ou capitalização que não contratou, restituição de débitos
  em conta da empresa ou recuperação de juros cobrados sobre tarifas ilegais.
metadata:
  area: bancario
  tipo_peca: inicial
  verificado_em: 2026-11-25
---
# Repetição de indébito bancário (débitos em conta)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: o banco debitou na conta valores sem contrato ou sem pactuação expressa e o cliente quer de volta o que pagou, com os reflexos (juros e encargos incidentes sobre esses débitos).
- Não usar:
  - Fundamento e cálculo da devolução em dobro (CDC art. 42, p.ú., modulação, Tema 929): `consumidor-repeticao-em-dobro` — use aquela skill para o capítulo da dobra.
  - Revisão de juros, capitalização e encargos do contrato de crédito: `consumidor-contratos-bancarios-revisional`.
  - Débitos decorrentes de fraude de terceiro (Pix, empréstimo do golpista): `banc-fraude-pix-e-transferencia-nao-autorizada`.
  - Conta inteira que o cliente não abriu: `banc-conta-aberta-indevidamente`.
  - Indébito tributário: `trib-repeticao-de-indebito`.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Extratos de todo o período, com cada lançamento contestado: data, histórico, valor.
2. Contrato de abertura de conta, termo de adesão a pacote de serviços, propostas de seguro ou capitalização — existem? Estão assinados? Pedir exibição se o cliente não tem.
3. Titular: pessoa física ou jurídica; a empresa usa a conta como destinatária final ou como insumo? (decide CDC x Código Civil).
4. Os débitos geraram saldo negativo e cobrança de juros de cheque especial sobre eles?
5. Houve ação anterior sobre tarifas ou encargos da mesma conta/contrato? (Tema 1.268 — coisa julgada).
6. Reclamações prévias e respostas.

## Prazo e contagem
- Repetição de indébito em relação contratual bancária: prazo decenal do art. 205 do CC, por se tratar de pretensão pessoal (REsp 2.230.380, em revisional com repetição). Conte cada débito da sua data; liste os que ficariam fora dos 10 anos.
- Se a defesa sustentar o prazo trienal do enriquecimento sem causa (CC art. 206, § 3º, IV), enfrente com a natureza contratual da relação.
- Correção e juros sobre cada débito: núcleo `juros-e-correcao`, nunca taxa própria nem a taxa do banco.
- Prazos processuais: `prazos-processuais`.

## Estrutura da peça
Lançamentos (planilha) → relação jurídica (CDC ou CC) → ausência de causa de cada débito → dispensa da prova do erro → pedidos cumulados (débito principal + encargos incidentes) → forma da restituição (simples ou dobro) → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Cumular tudo agora.** A eficácia preclusiva da coisa julgada impede nova ação para pedir juros remuneratórios incidentes sobre tarifas já declaradas ilegais em ação anterior (Tema 1.268/STJ). Peça, na mesma ação, as tarifas e os juros e encargos que incidiram sobre elas.
- **Prova do erro.** Fora do CDC, quem paga voluntariamente o indevido prova o erro (CC art. 877), mas a Súmula 322/STJ dispensa essa prova nos contratos de abertura de crédito em conta-corrente; e débito lançado pelo próprio banco não é pagamento voluntário — argumente isso.
- **Pactuação expressa.** O STJ exige pactuação expressa para cobrar tarifas de serviços bancários não isentos (AgInt no REsp 2.007.902): sem contrato, o ônus de exibir é do banco.

## Fundamentos verificados
- CC arts. 876, 877, 884, 885 e 205; CDC arts. 6º VIII e 42 p.ú. (para a dobra, ver skill vizinha).
- Súmula 297/STJ (CDC a bancos) e Súmula 322/STJ (sem prova do erro na abertura de crédito em conta-corrente).
- Tema 1.268/STJ (REsp 2.148.794, Segunda Seção, 2025): coisa julgada impede nova ação para juros sobre tarifas já declaradas ilegais.
- AgInt no REsp 2.007.902 (3ª Turma, 2025): pactuação expressa para tarifas.
- AgInt nos EDcl no REsp 1.852.329 (3ª Turma, 2023): repetição de débitos em conta não segue os critérios usados pelo banco; juros legais e índices oficiais (cálculo pelo núcleo).
- REsp 2.081.643 (3ª Turma, 2025): restituição restrita aos valores efetivamente descontados da conta.
- REsp 2.230.380 (3ª Turma, 2026): prazo decenal.
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Declaração de inexigibilidade de cada rubrica e abstenção de novos débitos (tutela, se em curso).
- Restituição dos valores debitados e dos encargos incidentes sobre eles (juros de saldo devedor, IOF, tarifas de excesso), simples ou em dobro conforme `consumidor-repeticao-em-dobro`.
- Exibição do contrato de conta, termo de pacote e propostas, sob pena do art. 400 do CPC; perícia contábil se necessário.
- Correção e juros: `juros-e-correcao`.

## Checklist pré-protocolo
- [ ] Planilha com todos os débitos e seus reflexos (Tema 1.268)
- [ ] Ação anterior sobre a mesma conta pesquisada
- [ ] Débitos fora de 10 anos separados
- [ ] Regime (CDC ou CC) justificado
- [ ] Pedido de exibição do contrato e do termo de pacote
- [ ] Capítulo da dobra montado pela skill vizinha
- [ ] Juros e correção remetidos ao núcleo

## Erros a evitar
- Pedir só as tarifas e deixar os juros incidentes para depois: perde-se pela coisa julgada.
- Calcular a devolução pela taxa do cheque especial do banco.
- Aplicar o CDC sem justificar quando o titular é empresa que usa a conta como insumo.
- Pedir dobro de valor apenas lançado e estornado.

## Integração com o núcleo
`juros-e-correcao`, `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

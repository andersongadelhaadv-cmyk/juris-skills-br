---
name: civel-acao-indenizatoria
description: >
  Redige petição inicial de ação indenizatória cível fora da relação de consumo,
  com base no ato ilícito e no abuso de direito (CC, arts. 186, 187 e 927),
  responsabilidade objetiva por lei ou por atividade de risco (art. 927,
  parágrafo único), extensão do dano (art. 944), danos materiais, morais e
  estéticos cumulados (Súmulas 37 e 387/STJ) e prescrição trienal ou decenal
  conforme a natureza da responsabilidade. Use quando o usuário pedir ação de
  danos morais e materiais entre particulares, acidente de trânsito, ofensa à
  honra fora da internet, dano causado por vizinho, quebra de contrato com
  prejuízo, lucros cessantes, pensão por morte ou lesão, ou "processar por
  danos" sem fornecedor envolvido.
metadata:
  area: processo-civil
  tipo_peca: inicial
  verificado_em: 2026-11-25
---
# Ação indenizatória cível (responsabilidade civil comum)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: dano causado por particular, empresa fora de relação de consumo ou contratante, por ato ilícito (CC, art. 186), abuso de direito (art. 187), atividade de risco ou hipótese legal de responsabilidade objetiva (art. 927, parágrafo único), ou inadimplemento contratual com prejuízo (arts. 389 e 402).
- Não usar (skill mais específica):
  - Fornecedor x consumidor → `consumidor-acao-indenizatoria`.
  - Ofensa em redes sociais, vazamento de dados, deepfake → `digital-ofensas-em-redes-sociais`, `digital-indenizacao-por-vazamento-de-dados`, `digital-deepfake-e-uso-de-imagem`.
  - Erro médico ou hospital → `saude-indenizacao-erro-medico`, `saude-responsabilidade-civil-hospitalar`.
  - Estado como réu → `adm-responsabilidade-civil-do-estado`.
  - Acidente de trabalho contra o empregador → `trabalhista-acidente-e-doenca-ocupacional`.
  - Dano ambiental individual → `amb-indenizacao-dano-ambiental-individual`; acidente aéreo → `aero-acidente-aereo-indenizacao`.
  - Valor e causa compatíveis com o juizado → `civel-juizado-especial`.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. O fato danoso: data, local, dinâmica, quem agiu (e por conta de quem: empregador, dono do veículo, pais).
2. Fundamento da responsabilidade: culpa (qual conduta), risco da atividade, lei específica ou contrato descumprido.
3. Danos materiais com prova: despesas, orçamentos, notas, lucros cessantes (renda anterior provada).
4. Dano moral e estético: repercussão concreta (afastamento, internação, sequela, exposição); fotos e laudos.
5. Houve inquérito ou processo criminal sobre o fato? (art. 200 e art. 935 do CC).
6. Culpa da vítima ou de terceiro alegável pelo réu (art. 945); seguro do réu (possível denunciação da lide).
7. Em morte ou incapacidade: dependentes, renda da vítima, idade (arts. 948 a 950).

## Prazo e contagem
- Responsabilidade **extracontratual**: 3 anos (CC, art. 206, § 3º, V).
- Responsabilidade **contratual**: 10 anos (art. 205), segundo a 2ª Seção do STJ (AgInt nos EREsp 1.685.808, 2024), que reserva o trienal à extracontratual.
- Fato apurado no juízo criminal: a prescrição não corre antes da sentença definitiva (art. 200).
- Termo inicial (ciência do dano e da autoria): confirmar caso a caso [VERIFICAR: não há precedente sobre actio nata conferido nesta skill]. Prazos processuais: `prazos-processuais`.

## Estrutura da peça
Endereçamento → qualificação → síntese → fatos → responsabilidade (conduta, nexo, dano; ou risco/lei) → excludentes previsíveis → danos por espécie → quantificação → tutela provisória → pedidos → provas → valor da causa → audiência. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Foro**: lugar do ato ou fato na reparação de dano (CPC, art. 53, IV, "a"); domicílio do autor ou local do fato se o dano decorre de delito ou acidente de veículos (art. 53, V).
- **Polo passivo**: autor do dano e responsáveis solidários (CC, art. 942); em acidente de trânsito, condutor e proprietário, que responde objetiva e solidariamente pelo ato culposo de quem conduz (STJ, REsp 2.212.856, 3ª Turma, 2025).
- **Valor**: o art. 292, V, exige o valor pretendido, inclusive do dano moral; pedido genérico só se não for possível determinar as consequências do fato (art. 324, § 1º, II).
- **Independência das instâncias**: decididas no crime a existência do fato ou a autoria, não se discutem mais no cível (art. 935).

## Fundamentos verificados
CC arts. 186, 187, 188, 200, 205, 206 § 3º V, 389, 402, 403, 927, 935, 942, 944, 945, 948, 949, 950; CPC arts. 53, 292, 300, 324; Súmulas 37, 227 e 387/STJ; STJ sobre prazo contratual decenal, método bifásico e responsabilidade do proprietário do veículo. Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Danos emergentes (valor provado) e lucros cessantes (art. 402), um a um.
- Pensão mensal em morte (art. 948, II) ou incapacidade (art. 950), com pedido de pagamento único se preferido (art. 950, parágrafo único).
- Dano moral e dano estético, cumulados e com valor certo para cada um (Súmulas 37 e 387).
- Correção monetária e juros, com índice, taxa e termo inicial definidos pelo núcleo `juros-e-correcao` (não escrever taxa nem termo de memória).
- Tutela de urgência (art. 300) para custeio de tratamento ou pensão provisória, se houver prova robusta e urgência.
- Citação; custas e honorários; provas.

## Checklist pré-protocolo
- [ ] Natureza da responsabilidade definida (contratual x extracontratual) e prazo anotado
- [ ] Cada dano com prova própria e valor separado
- [ ] Dano moral com valor certo e critérios de fixação expostos
- [ ] Excludentes do réu antecipadas (culpa da vítima, fato de terceiro, caso fortuito)
- [ ] Responsáveis solidários no polo passivo
- [ ] Situação do processo criminal verificada (arts. 200 e 935)
- [ ] Juros e correção remetidos ao núcleo

## Erros a evitar
- Usar o prazo de 3 anos para inadimplemento contratual (ou o de 10 para ilícito extracontratual).
- Pedir dano moral "a arbitrar" sem valor: viola o art. 292, V.
- Lucros cessantes sem prova da renda anterior: viram dano hipotético (art. 403).
- Ignorar a culpa concorrente da vítima, que reduz a indenização (art. 945), e ser surpreendido.
- Pedir indenização punitiva sem base: a indenização mede-se pela extensão do dano (art. 944).

## Integração com o núcleo
`juros-e-correcao` (obrigatório), `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

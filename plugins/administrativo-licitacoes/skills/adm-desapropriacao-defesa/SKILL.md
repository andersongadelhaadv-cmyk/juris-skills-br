---
name: adm-desapropriacao-defesa
description: >
  Redige contestação do expropriado e manifestações em ação de desapropriação por
  utilidade pública (Decreto-Lei 3.365/1941): impugnação do preço, imissão
  provisória, levantamento do depósito, juros compensatórios (art. 15-A e ADI
  2.332) e honorários. Use quando o usuário pedir defesa em desapropriação,
  contestação do expropriado, discordar do valor da indenização, laudo de
  avaliação, imissão na posse, levantamento de 80% do depósito ou desapropriação
  indireta.
metadata:
  area: administrativo-licitacoes
  tipo_peca: contestacao
  verificado_em: 2026-11-01
---
# Defesa do expropriado (Decreto-Lei 3.365/1941)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: contestação na ação de desapropriação direta; manifestação sobre imissão provisória e depósito; pedido de levantamento; quesitos e impugnação ao laudo; resposta à notificação com oferta (art. 10-A) ou opção por mediação/arbitragem (art. 10-B).
- Desapropriação indireta (apossamento administrativo): a peça é inicial de indenização; reaproveitar os tópicos de valor e juros (art. 15-A, § 2º).
- Não usar para discutir, na contestação, se há utilidade pública: o juiz não decide isso no processo expropriatório (art. 9º) e a contestação só versa sobre vício do processo ou preço (art. 20). Desvio de finalidade e nulidade do decreto vão por ação direta.
- Reforma agrária (LC 76/1993) e desapropriação urbanística sancionatória têm regras próprias — não usar esta skill sem adaptação.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Decreto de utilidade pública (data de expedição: caducidade de 5 anos — art. 10).
2. Notificação extrajudicial e oferta (art. 10-A) e resposta do proprietário.
3. Inicial, oferta, depósito, laudo prévio e decisão sobre imissão provisória (data da imissão).
4. Matrícula, ônus reais, dívidas fiscais (art. 32, §§ 1º a 3º; art. 34).
5. Dados do imóvel para avaliação: área, benfeitorias, uso econômico, renda, área remanescente.
6. Prova de lucros cessantes, se houver pedido de juros compensatórios (art. 15-A, § 1º).

## Prazo e contagem
- Contestação: feita a citação, a causa segue o rito ordinário (art. 19) e o CPC se aplica no que o decreto-lei for omisso (art. 42) — 15 dias úteis (CPC arts. 219 e 335). Termo inicial: a audiência de conciliação, se designada (CPC art. 335, I e II); nos demais casos, a data do CPC art. 231 conforme o modo da citação — mandado ou hora certa (inciso II e § 4º), precatória (inciso VI), edital (inciso IV); ver DL arts. 16 a 18. Conferir com `prazos-processuais`.
- Notificação extrajudicial: 15 dias para aceitar ou rejeitar a oferta; silêncio = rejeição (art. 10-A, § 1º, IV).
- Urgência: o expropriante deve requerer a imissão em 120 dias da alegação de urgência, sem renovação (art. 15, §§ 2º e 3º).
- Caducidade do decreto: 5 anos sem acordo ou ajuizamento (art. 10).
- Ação de indenização por restrições do poder público: 5 anos (art. 10, parágrafo único).

## Estrutura da peça (resumo; detalhe em [estrutura](references/estrutura.md))
Tempestividade → preliminares processuais (caducidade, falta de notificação, vícios da inicial, urgência fora do prazo) → impugnação do preço com contraproposta e assistente técnico → juros compensatórios e moratórios → honorários → levantamento → pedidos e quesitos.

## Requisitos e preliminares
- Inicial deve conter a oferta e o decreto ou sua publicação, e a planta/descrição do bem (art. 13).
- Imissão provisória exige alegação de urgência e depósito nos critérios do art. 15, § 1º; registro no cartório (§ 4º).
- Se não houver oposição expressa à validade do decreto na contestação, a propriedade é transferida desde logo e o processo segue só quanto ao litigioso (art. 34-A, § 4º) — decidir com o cliente antes de contestar.

## Fundamentos verificados (resumo; detalhe em [fundamentos](references/fundamentos.md))
CF art. 5º, XXIV (justa e prévia indenização em dinheiro); DL 3.365/1941, arts. 9º, 10, 10-A, 10-B, 13, 15, 15-A, 15-B, 20, 26, 27, 32 a 34-A, 42. STF, ADI 2.332. STJ: Súmulas 69, 114, 131; AgInt no REsp 2.096.836 (base dos juros após a Lei 14.620/2023).

## Pedidos e requerimentos
- Indenização justa, contemporânea da avaliação (art. 26), incluindo benfeitorias (art. 26, § 1º) e desvalorização da área remanescente (art. 27).
- Correção do valor se passado mais de 1 ano da avaliação (art. 26, § 2º) — índice e cálculo pela skill `juros-e-correcao`.
- Juros compensatórios sobre a diferença, desde a imissão (art. 15-A; Súmula 69 do STJ), e juros moratórios do art. 15-B — percentuais, base e interação com a EC 113/2021 calculados exclusivamente pela skill `juros-e-correcao`. Base: para os juros incidentes na vigência da Lei 14.620/2023, a diferença entre o preço ofertado e o valor fixado na sentença, pois os juros compensatórios seguem a lei vigente quando incidem (STJ, AgInt no REsp 2.096.836); para períodos anteriores, a redação então vigente, com a interpretação da ADI 2.332 (diferença entre 80% da oferta e o valor fixado).
- Honorários entre 0,5% e 5% da diferença (art. 27, § 1º), sem o teto em reais declarado inconstitucional na ADI 2.332, incluindo juros na base (Súmula 131 do STJ).
- Levantamento de até 80% do depósito (art. 33, § 2º), ou 100% em caso de concordância com a imissão (art. 34-A, § 2º), observado o art. 34.
- Perícia com assistente técnico e quesitos.

## Checklist pré-protocolo
- [ ] Data do decreto e do ajuizamento (caducidade).
- [ ] Notificação do art. 10-A recebida e respondida.
- [ ] Contestação restrita a vício processual e preço (art. 20).
- [ ] Decisão consciente sobre opor-se ou não ao decreto (art. 34-A, § 4º).
- [ ] Laudo do assistente técnico e contraproposta de valor.
- [ ] Prova de lucros cessantes para juros compensatórios.
- [ ] Certidões para levantamento (propriedade, quitação fiscal, editais — art. 34).
- [ ] Nenhum percentual de juros ou índice escrito sem passar por `juros-e-correcao`.

## Erros a evitar
- Contestar a utilidade pública ou o mérito do decreto na própria ação (arts. 9º e 20).
- Aplicar a Súmula 618 do STF (12% ao ano) como regra vigente: superada pela legislação posterior e pela ADI 2.332.
- Pedir juros compensatórios sobre a totalidade do valor, e não sobre a diferença.
- Esquecer de requerer o levantamento dos 80% logo após a imissão.
- Aceitar o teto de honorários em reais do art. 27, § 1º.

## Integração com o núcleo
- `juros-e-correcao`: correção, juros compensatórios e moratórios (obrigatório).
- `prazos-processuais`: contestação, caducidade e prescrição.
- `verificacao-de-citacoes`: precedentes adicionais.
- `fidelidade-factual`: dados do imóvel e do depósito.
- `estilo-forense`: revisão final.

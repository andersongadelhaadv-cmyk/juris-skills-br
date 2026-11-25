---
name: imob-locacao-residencial
description: >
  Elabora ou revisa contrato de locação residencial urbana (Lei 8.245/1991):
  prazo e efeitos dos 30 meses, aluguel e reajuste, encargos ordinários e
  extraordinários, garantia única do art. 37 (caução, fiança, seguro-fiança,
  cessão fiduciária de cotas), vistoria, multa por devolução antecipada,
  benfeitorias e cláusula de vigência. Use quando o usuário pedir contrato de
  aluguel de casa ou apartamento, revisão de minuta de locação residencial,
  cláusula de fiança, caução de três meses ou checagem de cláusulas nulas.
metadata:
  area: imobiliario
  tipo_peca: contrato
  verificado_em: 2026-11-25
---
# Contrato de locação residencial

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: locação de imóvel urbano para moradia, regida pela Lei 8.245/1991, seja para redigir a minuta (do lado do locador ou do locatário), seja para revisar uma minuta pronta.
- Não usar: locação comercial, loja, sala ou galpão (`contratos-locacao-comercial`); locação por temporada como modalidade própria — tratar à parte, conferindo os artigos específicos [VERIFICAR: arts. 48 a 50 da Lei 8.245/1991 não conferidos nesta skill]; imóvel rural (Estatuto da Terra); conflito já instalado (`imob-acao-de-despejo`, `imob-acao-revisional-de-aluguel`); análise genérica de contrato (`contratos-analise-e-revisao-de-contrato`).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Partes completas; regime de bens e cônjuge do locador (relevante se prazo de 10 anos ou mais — art. 3º) e do fiador.
2. Imóvel: endereço, matrícula, vaga, mobília, condomínio (convenção e regimento a entregar).
3. Prazo pretendido e se o locador quer poder retomar sem motivo ao final (decide entre 30 meses ou mais e prazo menor).
4. Aluguel, vencimento, forma de pagamento, índice de reajuste.
5. Garantia escolhida (apenas uma) e seus dados; seguro contra incêndio.
6. Quem paga IPTU, condomínio ordinário, consumo; taxa de administração/intermediação.
7. Estado do imóvel (laudo de vistoria com fotos) e regras sobre obras, benfeitorias, animais e sublocação.
8. Há promessa de venda ou risco de alienação? (cláusula de vigência e averbação — art. 8º).

## Prazo e contagem
- Prazo de 30 meses ou mais: termina no vencimento sem notificação; prorrogado por indeterminado, o locador denuncia com 30 dias (art. 46).
- Prazo inferior a 30 meses (ou verbal): prorroga-se e a retomada fica restrita às hipóteses do art. 47 — escolha que deve ser explicada ao cliente.
- Prazo de 10 anos ou mais exige vênia conjugal (art. 3º).
- Locatário em contrato por prazo indeterminado denuncia com 30 dias de aviso escrito (art. 6º).

## Estrutura do contrato
Qualificação → objeto e destinação → prazo → aluguel e reajuste → encargos → garantia → vistoria e conservação → obras e benfeitorias → cessão/sublocação → devolução antecipada → alienação e cláusula de vigência → rescisão → foro e citação por AR. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Aluguel livre, vedados moeda estrangeira, variação cambial e salário mínimo como indexador; reajuste conforme legislação específica (art. 17).
- Uma só garantia por contrato, sob pena de nulidade (art. 37). Caução em dinheiro até três meses de aluguel, depositada em poupança (art. 38).
- Sem garantia, o locador pode exigir o aluguel antecipado até o sexto dia útil do mês vincendo (art. 42).
- Nulas as cláusulas que frustrem os objetivos da lei, especialmente as que afastem a prorrogação do art. 47 (art. 45).

## Fundamentos verificados
- Lei 8.245/1991: arts. 3º, 4º, 6º, 8º, 13, 17, 22, 23, 37 a 42, 45, 46, 47, 58, IV.
- Fiador não responde por aditamento ao qual não anuiu (Súmula 214/STJ); garantias se estendem até a devolução do imóvel, salvo cláusula em contrário (art. 39); exoneração do fiador em prorrogação por indeterminado: responde por 120 dias após notificar (art. 40, X).
- Bem de família do fiador é penhorável (Súmula 549/STJ; Lei 8.009/1990, art. 3º, VII), constitucionalidade afirmada pelo STF para locação residencial e comercial (Tema 1127).
- Cláusula de renúncia à indenização por benfeitorias e ao direito de retenção é válida (Súmula 335/STJ).
Detalhe em [fundamentos](references/fundamentos.md).

## Cláusulas essenciais
- Prazo e regime de retomada (30 meses ou menos), com a consequência explicada.
- Aluguel, vencimento (na falta, sexto dia útil do mês seguinte — art. 23, I), índice e periodicidade.
- Divisão de encargos: despesas ordinárias ao locatário (art. 23, XII), extraordinárias ao locador (art. 22, X); taxa de administração e intermediação ao locador (art. 22, VII).
- Garantia única, com a cláusula de extensão até a entrega das chaves (art. 39) e o procedimento de substituição (art. 40, parágrafo único: 30 dias para nova garantia).
- Laudo de vistoria de entrada anexo; devolução no mesmo estado, salvo desgaste natural (art. 23, III).
- Obras só com consentimento escrito (art. 23, VI); regime de benfeitorias (Súmula 335/STJ).
- Cessão, sublocação e empréstimo dependem de consentimento prévio e escrito (art. 13).
- Multa por devolução antecipada proporcional ao prazo restante; dispensa se o locatário for transferido pelo empregador e avisar com 30 dias (art. 4º).
- Cláusula de vigência em caso de alienação, com averbação na matrícula, se o locatário quiser proteção (art. 8º).
- Autorização de citação por correspondência com AR (art. 58, IV); foro do imóvel ou de eleição.
- Multa moratória, correção e juros: taxas pelo núcleo `juros-e-correcao`.

## Checklist pré-assinatura
- [ ] Apenas uma garantia (nenhuma caução "adicional" escondida)
- [ ] Caução em dinheiro limitada a três meses e destinada a poupança
- [ ] Prazo escolhido conscientemente (30 meses x art. 47)
- [ ] Vênia conjugal se prazo de 10 anos ou mais
- [ ] Fiador com cônjuge anuente e ciente da penhorabilidade do bem de família
- [ ] Laudo de vistoria com fotos anexado e assinado
- [ ] Encargos divididos conforme arts. 22 e 23
- [ ] Nenhuma cláusula que afaste direitos irrenunciáveis (art. 45)

## Erros a evitar
- Exigir fiança e caução ao mesmo tempo (nulidade — art. 37).
- Indexar o aluguel ao salário mínimo ou ao dólar (art. 17).
- Cobrar do locatário fundo de reserva ou obras estruturais (despesas extraordinárias — art. 22, X e parágrafo único).
- Aditar valor ou prazo sem a assinatura do fiador (Súmula 214/STJ).
- Fixar multa rescisória integral, sem proporcionalidade (art. 4º).
- Prometer ao locador retomada livre em contrato de 12 meses.

## Integração com o núcleo
`juros-e-correcao` (multa, correção, juros), `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`; minutas gerais: `contratos-elaboracao-de-contrato`.

---
name: trib-prescricao-intercorrente
description: >
  Analisa e redige petição de reconhecimento de prescrição intercorrente,
  prescrição originária e decadência tributária em execução fiscal (LEF art. 40;
  CTN arts. 150, 173 e 174, com as causas interruptivas da LC 236/2026). Use
  quando o usuário pedir prescrição intercorrente, extinção de execução fiscal
  parada, processo arquivado há mais de 5 anos, art. 40 da LEF, contagem de
  prescrição ou decadência de crédito tributário, ou cálculo da linha do tempo
  da execução.
metadata:
  area: tributario-fazenda
  tipo_peca: requerimento
  verificado_em: 2026-11-01
---
# Prescrição intercorrente, prescrição e decadência tributária

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: execução fiscal sem localização do devedor ou de bens por longo período; dúvida sobre prazos de decadência (constituição) ou de prescrição (cobrança); montar a linha do tempo antes de escolher a peça.
- A peça pode ser simples petição nos autos, exceção de pré-executividade (`trib-excecao-pre-executividade-fiscal`) ou tópico dos embargos (`trib-embargos-a-execucao-fiscal`).
- Não usar para execuções comuns (CPC art. 921 tem regra própria; aplique só subsidiariamente).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
- Fato gerador, data da declaração ou do lançamento, data da notificação do auto e da decisão administrativa definitiva.
- Data do ajuizamento e do despacho que ordenou a citação; data da citação efetiva.
- Data da primeira tentativa frustrada de localizar devedor ou bens e da ciência da Fazenda.
- Todas as petições da Fazenda e o resultado (houve penhora efetiva? citação efetiva?).
- Parcelamentos, protestos, pedidos de revisão, falência ou recuperação.

## Prazo e contagem
1. **Decadência** (prazo para lançar, 5 anos): CTN art. 173, I (primeiro dia do exercício seguinte); art. 150, §4º (do fato gerador, com pagamento); §5º (dolo, fraude ou simulação: regra do art. 173, I); §6º (pagamento parcial: do fato gerador), estes dois incluídos pela LC 236/2026. Sem declaração nem pagamento: Súmula 555 STJ. A notificação do auto encerra a decadência (Súmula 622 STJ).
2. **Prescrição originária** (5 anos): da constituição definitiva (CTN art. 174) até o despacho citatório (art. 174, §1º, I), que retroage ao ajuizamento se a demora for do Judiciário (Súmula 106 STJ). A inscrição suspende por 180 dias só para dívida não tributária (LEF art. 2º, §3º) [confirme a natureza do crédito].
3. **Prescrição intercorrente** (LEF art. 40): ciência da Fazenda sobre a não localização do devedor ou de bens → 1 ano de suspensão automática → 5 anos de prescrição → oitiva da Fazenda → decretação (inclusive de ofício). Súmula 314 STJ. A sistemática fixada pela 1ª Seção do STJ em repetitivo (contagem automática a partir da ciência da Fazenda; só efetiva citação ou constrição interrompem, não o mero peticionamento) é aplicada em julgados verificados, como o AgInt no AREsp 3.049.264 (2026) [VERIFICAR: número do tema e do REsp paradigma diretamente no site do STJ antes de citar].
- LC 236/2026 (inciso sancionado; só o novo caput do §1º foi vetado): nova causa interruptiva no art. 174, §1º, VII (sentença de extinção da execução por não localização, desde que a intercorrente não tenha começado). Considere-a ao montar a linha do tempo.
- Use `prazos-processuais` para cada marco.

## Estrutura da peça
Endereçamento → síntese → linha do tempo documentada → marco inicial (ciência da Fazenda) → suspensão anual → quinquênio → ausência de causa interruptiva eficaz → pedido. Roteiro em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- A Fazenda deve ser ouvida antes da decretação de ofício (LEF art. 40, §4º), salvo valores abaixo do mínimo fixado (§5º). Na petição do executado, peça a intimação.
- Nulidade por falta de intimação só se demonstrado prejuízo (diretriz aplicada pelos julgados verificados).
- Honorários: incabíveis na exceção acolhida por prescrição intercorrente (Tema 1229 STJ).
- Execuções de baixo valor paradas: confira também Res. CNJ 547/2024 (extinção por falta de interesse, art. 1º, §1º) e Tema 1184 STF.

## Fundamentos verificados
LEF arts. 2º, §3º, 8º, §2º e 40; CTN arts. 150, 173 e 174; CPC art. 921 (subsidiário); Súmulas 106, 314, 409, 436, 555 e 622 STJ; Tema 1229 STJ; Tema 1184 STF; Res. CNJ 547/2024. Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Intimação da Fazenda (art. 40, §4º).
- Reconhecimento da prescrição intercorrente (ou originária) e extinção da execução com resolução de mérito (CPC art. 487, II; CTN art. 156, V).
- Levantamento de penhoras, bloqueios e restrições; baixa da inscrição.
- Honorários somente quando não incidir o Tema 1229 STJ (ex.: prescrição originária).

## Checklist pré-protocolo
- [ ] Linha do tempo com folha/ID de cada ato.
- [ ] Marco da ciência da Fazenda sobre a primeira diligência negativa identificado.
- [ ] Cada petição da Fazenda conferida: houve citação ou constrição EFETIVA?
- [ ] Causas da LC 236/2026 (protesto, extinção por não localização, falência) verificadas.
- [ ] Natureza do crédito (tributário ou não) definida para aplicar ou não o art. 2º, §3º da LEF.
- [ ] Pedido de honorários ajustado ao Tema 1229 STJ.

## Erros a evitar
- Contar a intercorrente do despacho de arquivamento em vez da ciência da Fazenda.
- Considerar interruptiva a simples petição da Fazenda sem resultado útil.
- Confundir decadência (constituição) com prescrição (cobrança).
- Citar número de tema ou REsp sem conferir no site do tribunal.
- Pedir honorários na extinção por intercorrente.

## Integração com o núcleo
- `prazos-processuais`: cálculo de cada prazo e conferência de datas.
- `verificacao-de-citacoes`: confirmar número do repetitivo paradigma e qualquer julgado acrescentado.
- `fidelidade-factual`: datas dos autos.
- `juros-e-correcao`: não se aplica ao mérito; use apenas se houver pedido condenatório acessório.
- `estilo-forense`: revisão final.

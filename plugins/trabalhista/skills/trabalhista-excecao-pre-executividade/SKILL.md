---
name: trabalhista-excecao-pre-executividade
description: >
  Redige exceção (objeção) de pré-executividade na execução trabalhista, sem
  garantia do juízo, restrita a matérias de ordem pública provadas de plano —
  nulidade de citação, ilegitimidade manifesta, inexigibilidade do título (CLT
  art. 884, §5º), prescrição intercorrente (CLT art. 11-A), pagamento
  documentado —, com o alerta de que a rejeição é interlocutória (Súmula
  214/TST). Use quando o usuário pedir exceção de pré-executividade trabalhista,
  defesa do executado ou do sócio sem garantir o juízo, ou objeção contra
  bloqueio na execução trabalhista.
metadata:
  area: trabalhista
  tipo_peca: outro
  verificado_em: 2026-11-25
---
# Exceção de pré-executividade trabalhista

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: o executado (empresa, sócio incluído, tomador responsabilizado) não garantiu a execução e tem tese de ordem pública demonstrável só com documentos, sem perícia nem testemunha.
- Matérias típicas: falta ou nulidade de citação; ilegitimidade evidente (executado estranho ao título, sem decisão que o inclua); título inexigível (CLT art. 884, §5º); prescrição intercorrente (CLT art. 11-A); pagamento ou acordo quitado comprovado por documento; incompetência absoluta.
- Não usar: excesso de execução ou erro de cálculo que dependa de conferência contábil (`trabalhista-impugnacao-de-calculos` antes da homologação; `trabalhista-embargos-a-execucao` depois de garantir o juízo); terceiro com bem penhorado (embargos de terceiro, `imob-embargos-de-terceiro` como referência de estrutura); execução cível (`civel-excecao-de-pre-executividade`) ou fiscal (`trib-excecao-pre-executividade-fiscal`); entidade filantrópica, que pode embargar sem garantia (CLT art. 884, §6º).

## Entradas mínimas (perguntar o que faltar; nunca supor fatos)
1. Título executivo e certidão de trânsito; decisão de homologação dos cálculos.
2. Atos de citação/intimação do executado e a decisão que o incluiu no polo (se sócio ou responsável).
3. Atos de constrição já praticados (bloqueio via sistema, penhora) e datas.
4. Documento que prova a tese de plano (comprovante, decisão do STF, certidão de inércia do exequente etc.).
5. Para prescrição intercorrente: a determinação judicial descumprida pelo exequente e a data (art. 11-A, §1º).

## Prazo e contagem
- Não há prazo legal próprio: a construção jurisprudencial admite a objeção enquanto durar a execução, mas a demora pode custar a constrição de bens. Protocole antes de expirar o prazo de embargos se houver garantia em curso.
- Embargos à execução, se garantido o juízo: 5 dias (CLT art. 884). Agravo de petição contra decisão terminativa: `prazos-processuais`.

## Estrutura da peça
Endereçamento ao juízo da execução → cabimento (ordem pública + prova pré-constituída + dispensa de garantia) → tese, com documentos → pedido de suspensão de atos de constrição → pedidos. Roteiro em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Base normativa:** a regra trabalhista exige garantia para embargos (CLT art. 884, caput); a objeção de pré-executividade é admitida para nulidades que o juiz conhece de ofício, com apoio subsidiário no CPC (arts. 518 e 803, parágrafo único), via CLT arts. 769 e 889 [VERIFICAR: CLT art. 889 manda aplicar antes a Lei de Execução Fiscal; confirme a compatibilidade no caso].
- **Prova pré-constituída:** se a tese precisar de instrução, a objeção será rejeitada e a matéria terá de ir para embargos.
- **Recorribilidade:** a decisão que rejeita a objeção e manda prosseguir a execução é interlocutória e, em regra, não admite recurso imediato (CLT art. 893, §1º; Súmula 214/TST); há acórdão do TST nesse sentido, com não conhecimento de agravo de petição contra decisão em exceção sem garantia do juízo (EDCiv-Ag-EDCiv-Ag-AIRR 973-04.2015.5.09.0664). Acolhida a objeção com extinção da execução (ou exclusão do executado), cabe agravo de petição (CLT art. 897, a; `trabalhista-agravo-de-peticao`).
- **Revista na execução:** só por violação direta e literal da Constituição (Súmula 266/TST).

## Fundamentos verificados
- CLT arts. 11-A, 769, 884 (caput, §§1º, 5º e 6º), 889, 893 §1º, 897 a.
- CPC arts. 518 e 803, parágrafo único.
- Súmulas 214 e 266 do TST; acórdão TST 973-04.2015.5.09.0664 (rejeição como interlocutória).
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Efeito suspensivo prático: suspensão dos atos de constrição até a decisão da objeção, demonstrando o risco concreto.
- Acolhimento da objeção para declarar a nulidade, a inexigibilidade, a prescrição intercorrente, a extinção pelo pagamento ou a exclusão do executado.
- Liberação de valores bloqueados.
- Juros e correção sobre valores a restituir: `juros-e-correcao`.

## Checklist pré-protocolo
- [ ] Tese é de ordem pública e cognoscível de ofício
- [ ] Prova inteiramente documental, já juntada
- [ ] Nenhum ponto depende de cálculo controvertido
- [ ] Prazo de embargos não está correndo (ou peça protocolada antes dele)
- [ ] Cliente informado de que a rejeição, em regra, não é recorrível de imediato
- [ ] Prescrição intercorrente: ordem judicial descumprida identificada e prazo de 2 anos contado

## Erros a evitar
- Usar a objeção para discutir cálculo ou prova (vira embargos sem garantia, rejeitados).
- Interpor agravo de petição contra a simples rejeição sem enfrentar a Súmula 214.
- Alegar prescrição intercorrente sem apontar a determinação judicial descumprida (art. 11-A, §1º).
- Confundir a inexigibilidade do §5º do art. 884 com mera divergência jurisprudencial: exige declaração de inconstitucionalidade ou interpretação tida por incompatível com a CF pelo STF.

## Integração com o núcleo
`prazos-processuais`, `juros-e-correcao`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

---
name: amb-mandado-de-seguranca-licenciamento
description: >
  Redige petição inicial de mandado de segurança contra ato ou omissão no
  licenciamento ambiental — indeferimento sem motivação, condicionante ilegal,
  suspensão ou cancelamento de licença sem contraditório, exigência de licença
  por ente incompetente, demora além dos prazos legais — com base na Lei
  12.016/2009, na Lei 15.190/2025, na LC 140/2011 e na Lei 9.784/1999. Use
  quando o empreendedor tiver prova documental pronta e precisar de liminar
  para suspender ato do órgão licenciador (IBAMA, órgão estadual ou municipal),
  obrigar a análise do pedido de licença em atraso, afastar dupla exigência de
  licenciamento ou embargo ligado à licença, dentro de 120 dias da ciência.
metadata:
  area: ambiental
  tipo_peca: inicial
  verificado_em: 2026-11-25
---
# Mandado de segurança contra ato de licenciamento ambiental

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: ato concreto (ou omissão) da autoridade licenciadora que viole direito líquido e certo do empreendedor, demonstrável só com documentos: decisão sem motivação, condicionante sem base legal, suspensão/cancelamento sem contraditório, licenciamento exigido por segundo ente, inércia além do art. 47 da Lei 15.190/2025.
- Não usar:
  - a tese depende de perícia (se a condicionante é tecnicamente desnecessária, se houve dano) → ação de procedimento comum com tutela de urgência (`civel-peticao-inicial`, `civel-tutela-provisoria`);
  - ainda cabe pedido administrativo eficaz e barato → `amb-recurso-no-licenciamento`;
  - impugnação de multa ambiental já constituída → `amb-recurso-auto-de-infracao` ou `trib-acao-anulatoria`;
  - MS em tema não ambiental → `adm-mandado-de-seguranca` (roteiro geral do writ, que esta skill complementa).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Ato coator na íntegra (licença com condicionante, ofício de indeferimento, suspensão, cancelamento, exigência) e data da ciência; para omissão, protocolo e data de entrega dos estudos completos.
2. Autoridade que praticou o ato ou da qual partiu a ordem (cargo exato) e pessoa jurídica (IBAMA, autarquia estadual, município).
3. Processo de licenciamento completo: estudos, pareceres, exigências de complementação, respostas.
4. Recurso administrativo interposto? Com efeito suspensivo? (Lei 12.016/2009, art. 5º, I).
5. Prova do periculum: contratos, cronograma, financiamento, empregados, safra.
6. Regime do processo (anterior ou posterior à vigência da Lei 15.190/2025) e lei estadual/municipal de licenciamento.

## Prazo e contagem
- 120 dias da ciência do ato (Lei 12.016/2009, art. 23). Para omissão continuada, o prazo é discutido — documente a data de cada pedido e da última cobrança.
- Prazos processuais do writ: `prazos-processuais`.

## Estrutura da peça
Endereçamento → partes e autoridade coatora → cabimento e tempestividade → competência → fatos do licenciamento → direito líquido e certo por tese → liminar → pedidos. Roteiro detalhado em [estrutura](references/estrutura.md); forma geral do writ em `adm-mandado-de-seguranca`.

## Requisitos e preliminares
- **Prova pré-constituída:** todo o processo de licenciamento juntado; tese que exige laudo técnico contraditório não cabe no MS.
- **Autoridade coatora:** quem praticou o ato ou ordenou sua prática (Lei 12.016/2009, art. 6º, § 3º) — em regra o dirigente que assinou a licença ou a decisão, não o técnico que deu parecer.
- **Juízo:** Justiça Federal se a autoridade for federal (IBAMA, ICMBio); estadual se a autoridade for estadual ou municipal. Confira a regra de competência e o regimento local.
- **Recurso com efeito suspensivo:** não cabe MS contra ato sujeito a recurso administrativo com efeito suspensivo independente de caução (art. 5º, I). No licenciamento, o efeito suspensivo dos arts. 14, § 7º, e 16, § 3º, da Lei 15.190/2025 é facultativo — se não foi concedido, o writ é cabível; diga isso na peça.
- **Liminar:** fundamento relevante e risco de ineficácia da medida final (art. 7º, III); o juiz pode exigir caução. Antecipe a objeção da proteção ambiental: peça medida que não autorize dano (ex.: suspender a condicionante X, não a licença inteira; determinar a análise em prazo, não "emitir a licença").
- **Omissão:** o decurso dos prazos não gera licença tácita (Lei 15.190/2025, art. 47, § 3º; LC 140/2011, art. 14, § 3º). O pedido viável é ordem para decidir em prazo, ou declaração de competência supletiva, não a emissão da licença pelo juiz.
- **Sem honorários** no MS (art. 25); sentença concessiva sujeita a reexame necessário (art. 14, § 1º); MP opina em 10 dias (art. 12).

## Fundamentos verificados
- CF, art. 5º, LV e LXIX; Lei 12.016/2009, arts. 1º, 5º, 6º, 7º, 12, 14, 23 e 25.
- Lei 15.190/2025, arts. 14, §§ 6º e 7º, 16, 47 e 60; LC 140/2011, arts. 13, 14 e 17.
- Lei 9.784/1999, arts. 2º, 50 e 64; Resolução CONAMA 237/1997, art. 19 (processos sob o regime anterior).
- STJ: licenciar ≠ fiscalizar (REsp 1.971.073); competência do licenciador pelo reflexo do impacto (RMS 69.666); Súmula 613 (sem fato consumado).
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Liminar para suspender o ato coator (ou a condicionante específica) ou para determinar à autoridade que decida em prazo certo.
- Notificação da autoridade coatora e ciência à pessoa jurídica (Lei 12.016/2009, art. 7º — forma em `adm-mandado-de-seguranca`).
- Oitiva do Ministério Público.
- Concessão da segurança: anular o ato (indeferimento, condicionante, suspensão, cancelamento, exigência do ente incompetente) ou determinar a análise/decisão em prazo.
- Sem pedido de valores pretéritos (não cabe no MS).

## Checklist pré-protocolo
- [ ] Ciência do ato comprovada e 120 dias conferidos
- [ ] Autoridade coatora e pessoa jurídica corretas; juízo competente
- [ ] Processo de licenciamento integral juntado (sem depender de perícia)
- [ ] Recurso administrativo: inexistente, ou sem efeito suspensivo — dito expressamente
- [ ] Liminar desenhada para não autorizar dano ambiental
- [ ] Regime aplicável (Lei 15.190/2025 x anterior) explicado
- [ ] Situação de ações de controle de constitucionalidade contra a Lei 15.190/2025 conferida [VERIFICAR]

## Erros a evitar
- Pedir ao juiz que emita a licença: o pedido é anular o ato ou mandar decidir.
- Alegar licença tácita pelo decurso do prazo.
- Levar ao MS discussão técnica sobre a necessidade da condicionante sem prova documental inequívoca.
- Indicar como coator o técnico parecerista ou o ente errado.
- Sustentar que a licença estadual impede autuação do IBAMA: o STJ distingue licenciar de fiscalizar (REsp 1.971.073).
- Invocar o tempo de operação como direito adquirido (Súmula 613/STJ).

## Integração com o núcleo
`prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

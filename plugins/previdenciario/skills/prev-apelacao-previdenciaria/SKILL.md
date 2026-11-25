---
name: prev-apelacao-previdenciaria
description: >
  Redige apelação e contrarrazões em ação previdenciária contra o INSS na
  Justiça Federal ou na competência delegada estadual (CF, art. 109, §§ 3º e 4º;
  CPC, arts. 496, 1.009 a 1.013), com remessa necessária, tutela na sentença,
  reafirmação da DER (Tema 995/STJ), termo inicial (Tema 1124/STJ) e honorários
  pela Súmula 111/STJ. Use quando o usuário pedir apelação previdenciária,
  recurso contra sentença em ação contra o INSS, contrarrazões do segurado,
  reforma de sentença que negou aposentadoria, DIB errada ou honorários sobre
  parcelas vencidas.
metadata:
  area: previdenciario
  tipo_peca: recurso
  verificado_em: 2026-11-25
---
# Apelação previdenciária

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: sentença do procedimento comum em ação de concessão, restabelecimento ou revisão de benefício, proferida por vara federal ou por juiz estadual na competência delegada (recurso ao TRF — CF, art. 109, § 4º); contrarrazões do segurado à apelação do INSS.
- Não usar no Juizado Especial Federal: lá o recurso de sentença é o recurso inominado à Turma Recursal (Lei 9.099, arts. 41 e 42, aplicada pela Lei 10.259, art. 1º); para divergência entre turmas, `prev-pedido-de-uniformizacao-tnu`.
- Ação acidentária na Justiça Estadual: ver `prev-acidentario` (o recurso vai ao Tribunal de Justiça).
- Técnica recursal genérica (preparo, adesivo, causa madura em detalhe): `civel-apelacao`. Embargos antes da apelação: `prev-embargos-de-declaracao-previdenciarios`.

## Entradas mínimas (perguntar o que faltar; nunca supor fatos)
1. Sentença integral, data da intimação e juízo (vara federal, JEF ou estadual delegada).
2. Petição inicial, contestação, laudos (médico, social, PPP/LTCAT) e o processo administrativo (NB, DER, motivo do indeferimento).
3. O que foi concedido e o que foi negado, capítulo a capítulo: benefício, períodos, DIB, tutela, honorários.
4. CNIS atualizado, para checar se houve contribuição após a DER (reafirmação).
5. Se houve tutela na sentença e se o benefício já foi implantado.
6. Valor estimado da condenação (para a remessa necessária).

## Prazo e contagem
- 15 dias úteis para apelar e para contrarrazoar (CPC, art. 1.003, § 5º); o INSS tem prazo em dobro (CPC, art. 183) fora do JEF.
- Embargos de declaração interrompem o prazo (CPC, art. 1.026).
- Contagem e feriados: `prazos-processuais`.

## Estrutura da peça
Interposição ao juízo de origem → razões ao TRF → tempestividade e cabimento → síntese da sentença → preliminares (nulidade por cerceamento de prova, questões não agraváveis — art. 1.009, § 1º) → mérito por capítulo → DIB/DER/reafirmação → honorários → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Petição com nomes, fatos e direito, razões de reforma ou nulidade e pedido de nova decisão (CPC, art. 1.010).
- Remessa necessária: a sentença contra autarquia federal só fica dispensada do reexame se a condenação ou o proveito for inferior a 1.000 salários mínimos (CPC, art. 496, § 3º, I) ou nas hipóteses do § 4º (súmula, repetitivo, IRDR). No JEF não há reexame necessário (Lei 10.259, art. 13). Não conte com a remessa para corrigir capítulo que o segurado perdeu: recorra.
- Tutela concedida, confirmada ou revogada na sentença produz efeitos imediatos (CPC, art. 1.012, § 1º, V); para suspender ou restabelecer, pedido ao relator (art. 1.012, §§ 3º e 4º).
- Cerceamento de defesa (perícia indeferida, testemunhas rurais não ouvidas) vem em preliminar, com pedido de anulação e retorno; se o processo estiver maduro, pedir julgamento imediato (art. 1.013, § 3º).
- Custas e preparo: conferir o regime do tribunal e a gratuidade deferida [VERIFICAR: tabela e isenções do TRF ou do TJ na competência delegada].

## Fundamentos verificados
- CPC, arts. 183, 493, 496, 1.003, 1.009, 1.010, 1.012, 1.013, 1.026; CF, art. 109, §§ 3º e 4º; Lei 10.259, arts. 1º e 13.
- Tema 995/STJ: reafirmação da DER para o momento em que implementados os requisitos, inclusive entre o ajuizamento e o julgamento nas instâncias ordinárias (CPC, arts. 493 e 933), observada a causa de pedir.
- Tema 1124/STJ (julg. 08/10/2025): critérios do termo inicial dos efeitos financeiros (DER ou citação) quando a prova não foi submetida ao INSS — ler a tese no inteiro teor antes de citar.
- Súmula 111/STJ e Tema 1105/STJ: honorários não incidem sobre prestações vencidas após a sentença (ou após o primeiro julgamento de procedência).
- STF Tema 334: direito ao cálculo pelo quadro mais favorável.
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Conhecimento e provimento para reformar a sentença no capítulo X (conceder o benefício Y, reconhecer os períodos Z, fixar a DIB na DER).
- Subsidiariamente: reafirmação da DER (Tema 995) para a data em que os requisitos foram implementados.
- Anulação por cerceamento, com retorno para produção da prova, ou julgamento imediato (art. 1.013, § 3º).
- Implantação imediata do benefício (tutela recursal), demonstrando probabilidade e perigo — ver `prev-tutela-de-urgencia-previdenciaria`.
- Honorários recursais e base de cálculo conforme Súmula 111; juros e correção pelo núcleo `juros-e-correcao`.
- Prequestionamento expresso dos dispositivos federais e constitucionais.

## Checklist pré-protocolo
- [ ] Tempestividade conferida (data da intimação, dias úteis, embargos anteriores)
- [ ] Juízo de origem correto e recurso dirigido ao TRF (inclusive na competência delegada)
- [ ] Cada capítulo desfavorável impugnado especificamente
- [ ] CNIS atualizado conferido para pedido subsidiário de reafirmação da DER
- [ ] Remessa necessária avaliada (art. 496, § 3º, I) e não usada como substituto do recurso
- [ ] Pedido de tutela recursal fundamentado, se o benefício ainda não foi implantado
- [ ] Honorários: base de cálculo pela Súmula 111 enfrentada
- [ ] Juros e correção remetidos ao núcleo

## Erros a evitar
- Interpor apelação contra sentença de JEF (o recurso é inominado) ou dirigir ao TJ recurso da competência delegada (vai ao TRF).
- Inovar em apelação com período ou fato não alegado na inicial: a reafirmação da DER respeita a causa de pedir.
- Ignorar que o benefício implantado por tutela pode ter de ser devolvido se a sentença for reformada (Tema 692/STJ) — avisar o cliente por escrito.
- Pedir honorários sobre parcelas posteriores à sentença (Súmula 111).
- Calcular atrasados "de cabeça": a conta é do software de cálculo, e juros/correção vêm do núcleo.

## Integração com o núcleo
`prazos-processuais`, `juros-e-correcao`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

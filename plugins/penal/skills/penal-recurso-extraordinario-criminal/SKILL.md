---
name: penal-recurso-extraordinario-criminal
description: >
  Redige recurso extraordinário em matéria criminal ao STF (CF art. 102, III e
  § 3º; CPP art. 638; CPC arts. 1.029 e 1.035), com preliminar formal e
  fundamentada de repercussão geral, prequestionamento da questão
  constitucional e enfrentamento das Súmulas 279, 282, 284, 356 e 636 do STF.
  Use quando o usuário pedir RE criminal, recurso extraordinário contra acórdão
  de TJ, TRF, STJ ou turma recursal do JECRIM, ofensa direta à Constituição em
  processo penal (ampla defesa, presunção de inocência, inviolabilidade de
  domicílio, prova ilícita, juiz natural), repercussão geral ou agravo em RE (ARE).
metadata:
  area: penal
  tipo_peca: recurso
  verificado_em: 2026-11-25
---
# Recurso extraordinário criminal

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: decisão de única ou última instância (TJ, TRF, turma recursal do JECRIM, STJ) que contraria **diretamente** a Constituição, declara inconstitucional tratado ou lei federal, ou julga válida lei/ato local contestado em face da Constituição ou de lei federal (CF 102, III, a a d).
- Não usar:
  - violação de lei federal (CP, CPP, LEP) — `penal-recurso-especial-criminal` (interpor REsp e RE em petições distintas quando houver as duas matérias);
  - acórdão omisso sobre a questão constitucional — antes, `penal-embargos-de-declaracao` (Súmula 356/STF);
  - acórdão não unânime na apelação/RESE — antes, `penal-embargos-infringentes-e-de-nulidade`;
  - constrangimento à liberdade com urgência — `penal-habeas-corpus` (pode correr junto);
  - RE cível — `civel-recurso-extraordinario`.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Íntegra da decisão recorrida e dos embargos de declaração, se houve.
2. Data da intimação e calendário de suspensões do tribunal de origem.
3. Qual dispositivo **constitucional** foi violado e em que trecho do acórdão ele foi debatido.
4. Se a ofensa é direta ou depende de interpretar lei (se depende, é REsp — Súmula 636/STF).
5. Tema de repercussão geral já existente sobre a matéria (número, tese, situação).
6. Situação do réu (preso, pena, regime, risco de prescrição).

## Prazo e contagem
- 15 dias (CPC 1.003, § 5º, por remissão do CPP 638). O CPP 798 manda contar prazos de forma contínua; o STJ aplica essa regra aos recursos excepcionais criminais (ver `penal-recurso-especial-criminal`). Para o STF, conte em **dias corridos** por cautela [VERIFICAR: precedente do STF sobre a contagem no RE criminal não localizado no JuriBase].
- Feriado local: comprovar no ato da interposição (CPC 1.003, § 6º).
- Prescrição: o sobrestamento do RE na origem à espera de tema de repercussão geral **não suspende automaticamente** a prescrição da pretensão punitiva (STF, Tema 1303). Calcule a prescrição antes de recorrer (`penal-dosimetria`).
- Conferência de prazos: `prazos-processuais`.

## Estrutura da peça
Interposição ao Presidente/Vice-Presidente do tribunal de origem → razões ao STF: tempestividade e cabimento → **preliminar de repercussão geral** em tópico próprio → síntese → prequestionamento → ofensa direta à Constituição, tese por tese → afastamento dos óbices → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Repercussão geral** (CF 102, § 3º; CPC 1.035): demonstrar questões relevantes do ponto de vista econômico, político, social ou jurídico que ultrapassem o interesse subjetivo da causa (§ 1º). Há presunção quando o acórdão contraria súmula ou jurisprudência dominante do STF (§ 3º, I). Tópico formal, mesmo que pareça óbvio.
- **Prequestionamento**: a questão constitucional precisa estar no acórdão (Súmula 282/STF); se omisso, embargos de declaração (Súmula 356/STF).
- **Ofensa direta**: violação reflexa (que exige reinterpretar lei) não abre o RE (Súmula 636/STF, quanto à legalidade).
- **Sem reexame de prova** (Súmula 279/STF); **sem direito local** (Súmula 280/STF).
- **Esgotamento**: cabendo recurso ordinário na origem, o RE é inadmissível (Súmula 281/STF).
- **Fundamentação completa**: atacar todos os fundamentos suficientes (Súmula 283/STF) com clareza (Súmula 284/STF).
- **Turma recursal do JECRIM**: cabe RE (Súmula 640/STF); não cabe REsp.

## Fundamentos verificados
- CF art. 5º, LV; art. 102, III, a a d, e § 3º; CPP arts. 638 e 798; CPC arts. 1.003, 1.029, 1.030, 1.035 e 1.042.
- Súmulas 279, 280, 281, 282, 283, 284, 356, 636 e 640 do STF.
- STF, Tema 1303 da repercussão geral (sobrestamento e prescrição).
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Admissão e remessa ao STF; reconhecimento da repercussão geral.
- Provimento para anular o processo ou a prova ilícita e derivadas, absolver, ou cassar o acórdão com retorno à origem.
- Efeito suspensivo, se houver risco concreto (CPC 1.029, § 5º).
- Concessão de habeas corpus de ofício, como pedido subsidiário, quando a ilegalidade for evidente.

## Checklist pré-protocolo
- [ ] Prazo contado em dias corridos; suspensões comprovadas
- [ ] Preliminar formal de repercussão geral, com o § 1º e, se for o caso, o § 3º do CPC 1.035
- [ ] Dispositivo constitucional indicado e encontrado no acórdão (ou embargos opostos)
- [ ] Ofensa direta demonstrada, sem depender de lei infraconstitucional
- [ ] Nenhum pedido de reexame de prova
- [ ] Tema de repercussão geral pesquisado e distinguido, se contrário
- [ ] Prescrição calculada (Tema 1303)
- [ ] REsp em peça separada, se houver matéria federal

## Erros a evitar
- Omitir a preliminar de repercussão geral ou escrevê-la de forma genérica.
- Transformar violação de lei federal em "ofensa ao devido processo legal" — o STF trata como reflexa.
- Confiar que o sobrestamento protege da prescrição.
- No ARE, deixar de impugnar cada fundamento da inadmissão.
- Interpor um só recurso misturando matéria constitucional e federal.

## Integração com o núcleo
`prazos-processuais`, `verificacao-de-citacoes` (temas de repercussão geral e sua situação), `fidelidade-factual`, `estilo-forense`.

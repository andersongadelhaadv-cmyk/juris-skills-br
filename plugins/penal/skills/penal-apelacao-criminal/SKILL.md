---
name: penal-apelacao-criminal
description: >
  Redige a petição de interposição e as razões de apelação criminal da defesa
  (CPP arts. 593 a 603), inclusive contra decisões do Tribunal do Júri (art. 593,
  III), com efeitos, prazos de 5 dias para interpor e 8 dias para arrazoar.
  Use quando o usuário pedir apelação criminal, razões de apelação, recurso contra
  sentença condenatória, apelação do júri, contrarrazões de apelação ou recurso
  contra sentença penal.
metadata:
  area: penal
  tipo_peca: recurso-penal
  verificado_em: 2026-11-01
---
# Apelação criminal

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: sentença definitiva de condenação ou absolvição de juiz singular (593, I); decisões definitivas ou com força de definitivas não sujeitas a RESE (593, II), como impronúncia e absolvição sumária do júri (CPP 416); decisões do júri nas hipóteses taxativas do 593, III.
- Também para contrarrazões ao recurso da acusação (mesma estrutura, pedido de desprovimento).
- Não usar: decisões do rol do art. 581 (ver `penal-recurso-em-sentido-estrito`); decisões do juiz da execução (ver `penal-agravo-em-execucao`). Quando cabível apelação, não cabe RESE, ainda que de parte da decisão (593 §4º).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Sentença integral e data da intimação do réu e do defensor.
2. Memoriais da defesa e da acusação; atas de audiência; mídia dos depoimentos.
3. No júri: ata da sessão (CPP 495), quesitos e respostas, sentença do juiz-presidente.
4. Situação prisional e se houve execução provisória (júri — CPP 492, I, e; STF Tema 1068).
5. Objetivo: absolvição, nulidade, nova sessão do júri, redução de pena, regime.

## Prazo e contagem
- Interposição: 5 dias (CPP 593 caput). Razões: 8 dias após a intimação para arrazoar (CPP 600); 3 dias em contravenção. Contrarrazões: 8 dias.
- Prazo contínuo (CPP 798), a partir da intimação (Súmula 710 STF). Intimação da sentença deve alcançar réu e defensor; o prazo corre da última intimação.
- O ofendido não habilitado pode apelar em 15 dias após o fim do prazo do MP (CPP 598 p.ú.) — relevante para contrarrazões.
- Pode-se declarar na interposição que as razões serão apresentadas no tribunal (CPP 600 §4º).
- Use `prazos-processuais`.

## Estrutura da peça
Resumo (detalhe em [estrutura](references/estrutura.md)): (1) petição de interposição ao juízo de origem, com fundamento legal e eventual opção do 600 §4º; (2) razões ao tribunal: tempestividade e cabimento, síntese, preliminares, mérito, dosimetria, pedidos.

## Requisitos e preliminares
- Apelação do júri é de fundamentação vinculada: o efeito devolutivo fica restrito aos fundamentos da interposição (Súmula 713 STF). Indique na interposição a(s) alínea(s) do 593, III.
- Alínea d (decisão manifestamente contrária à prova): só uma apelação pelo mesmo motivo (593 §3º). Contra absolvição por quesito genérico, ver STF Tema 1087 (limites à anulação quando acolhida tese de clemência).
- Efeitos: sentença condenatória tem efeito suspensivo como regra (CPP 597), mas a prisão pode ser mantida por decisão fundamentada (CPP 387 §1º); absolutória não impede a soltura (596). Júri com pena igual ou superior a 15 anos: execução provisória e apelação sem efeito suspensivo (CPP 492 I, e, §§4º a 6º), e o STF fixou a execução imediata independentemente do total da pena (Tema 1068).
- Renúncia do réu sem assistência do defensor não impede o conhecimento da apelação do defensor (Súmula 705 STF).
- Proibição de reformatio in pejus no recurso exclusivo da defesa (CPP 617); tribunal não pode acolher contra o réu nulidade não arguida pela acusação (Súmula 160 STF).

## Fundamentos verificados
Resumo (detalhe em [fundamentos](references/fundamentos.md)): CPP 492, 593, 596, 597, 598, 600, 601, 609 p.ú., 617; Súmulas 160, 705, 713 do STF; STF Temas 1068 e 1087.

## Pedidos e requerimentos
- Preliminar: anulação do processo ou da sentença a partir do ato viciado.
- Mérito: absolvição (inciso do art. 386), desclassificação, afastamento de qualificadoras e majorantes.
- Júri: novo julgamento (593 §3º) ou retificação da pena pelo próprio tribunal (593 §§1º e 2º).
- Pena: redimensionamento, regime, substituição, detração, sursis.
- Atribuição de efeito suspensivo quando cabível (CPP 492 §§5º e 6º) e direito de aguardar em liberdade.
- Prequestionamento explícito dos dispositivos federais e constitucionais para eventual REsp/RE.

## Checklist pré-protocolo
- [ ] Prazo de interposição (5 dias) contado da última intimação.
- [ ] No júri, alíneas do 593, III indicadas já na interposição.
- [ ] Razões dentro de 8 dias ou opção pelo 600 §4º feita na interposição.
- [ ] Cada tese com remissão a folhas e minutagem.
- [ ] Nulidades do plenário com registro em ata (CPP 571, VIII) — se não houver, explicar por que a nulidade é absoluta.
- [ ] Pedido de efeito suspensivo, se pena de júri >= 15 anos, com os requisitos do 492 §5º.
- [ ] Dispositivos prequestionados; teses para embargos infringentes previstas se o acórdão não for unânime (CPP 609 p.ú.).
- [ ] Precedentes conferidos em `verificacao-de-citacoes`.

## Erros a evitar
- Interpor apelação do júri sem indicar a alínea, ou ampliar nas razões fundamentos não indicados (Súmula 713 STF).
- Usar a alínea d para pedir absolvição direta pelo tribunal: o efeito é novo júri.
- Confundir prazo de interposição (5) e de razões (8).
- Esquecer de requerer o efeito suspensivo nas condenações do júri.
- Omitir o prequestionamento, inviabilizando REsp/RE.

## Integração com o núcleo
- `prazos-processuais`: 5 + 8 dias contínuos, embargos de declaração (CPP 619, 2 dias) e infringentes (10 dias).
- `verificacao-de-citacoes`: todo precedente.
- `fidelidade-factual`: transcrição da sentença e da ata.
- `estilo-forense`: razões por teses numeradas.
- `juros-e-correcao`: se houver discussão do valor mínimo de reparação; não fixar índice na peça penal.
- Skills relacionadas: `penal-dosimetria`, `penal-plenario-do-juri`.

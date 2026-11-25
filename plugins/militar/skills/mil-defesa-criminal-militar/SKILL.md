---
name: mil-defesa-criminal-militar
description: >
  Estrutura a defesa técnica no processo penal militar (CPM, Decreto-Lei
  1.001/1969; CPPM, Decreto-Lei 1.002/1969): competência da Justiça Militar,
  rejeição da denúncia, nulidades, interrogatório, alegações escritas e
  sustentação oral perante o Conselho de Justiça ou o juiz singular. Use quando
  o usuário pedir defesa de militar ou de civil processado por crime militar,
  alegações escritas no CPPM, preliminar de incompetência da Justiça Militar,
  nulidade no processo penal militar ou estratégia de defesa em ação penal militar.
metadata:
  area: militar
  tipo_peca: contestacao
  verificado_em: 2026-11-25
---
# Defesa criminal militar

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: ação penal militar em curso na Justiça Militar da União (JMU) ou estadual (JME), da denúncia às alegações escritas e à sessão de julgamento.
- Não usar: crime comum julgado na Justiça comum (`penal-resposta-a-acusacao`, `penal-alegacoes-finais`); prisão a combater de imediato (`mil-habeas-corpus`, `mil-liberdade-provisoria`); decisão interlocutória recorrível (`mil-recurso-em-sentido-estrito`); condenação transitada (`mil-revisao-criminal`); punição só disciplinar (`mil-recurso-disciplinar`).

## Entradas mínimas (perguntar o que faltar; nunca supor fatos)
1. Denúncia completa, decisão de recebimento e data da citação.
2. Situação do acusado na data do fato: militar da ativa, da reserva, reformado ou civil; Força ou corporação estadual; em serviço ou não; local (sujeito ou não à administração militar).
3. Tipo imputado (CPM ou legislação penal comum trazida pelo art. 9º, II, do CPM) e pena máxima.
4. Vítima: militar, civil, patrimônio ou ordem administrativa militar.
5. IPM, laudos, fé de ofício e antecedentes; prova da defesa (testemunhas, documentos).
6. Fase atual e prazos em curso; se há prisão ou menagem.
7. Processo disciplinar paralelo pelo mesmo fato (efeitos e estratégia comum).

## Prazo e contagem
- Alegações escritas: oito dias, sucessivos, após o MP (CPPM art. 428); com mais de cinco acusados e advogados distintos, doze dias em comum (art. 428, § 1º). Alegação fora do prazo é desentranhada (art. 428, § 2º).
- Diligências finais: cinco dias após a última testemunha de defesa (art. 427).
- Sustentação oral na sessão: até três horas para a defesa, com tréplica de até uma hora (art. 433, §§ 1º e 2º).
- Instrução: 50 dias com acusado preso e 90 dias solto, do recebimento da denúncia (art. 390) — base para excesso de prazo.
- Contagem e prorrogação: `prazos-processuais`.

## Estrutura da peça
Preliminares (competência, inépcia, nulidades) → mérito (atipicidade, falta de prova, excludentes do CPM) → subsidiários (desclassificação, pena) → pedidos. Roteiro em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Competência é a primeira tese a testar. Crime militar em tempo de paz segue o art. 9º do CPM (redação das Leis 13.491/2017 e 14.688/2023): o inciso II alcança também crimes da legislação penal comum praticados nas situações das alíneas a a e.
- Doloso contra a vida de civil cometido por militar: júri (CPM art. 9º, § 1º), salvo militar das Forças Armadas nos contextos do § 2º (JMU).
- JME: juiz de direito julga sozinho os crimes militares contra civis; os demais vão ao Conselho de Justiça (CF art. 125, § 5º). JMU: juiz federal julga sozinho civis e militares corréus (Lei 8.457/1992, art. 30, I-B).
- Súmula 90/STJ (crime militar na JME, crime comum simultâneo na Justiça comum) e Súmula 78/STJ (policial militar estadual responde na JM de sua corporação ainda que o fato ocorra em outra unidade federativa).
- Rejeição da denúncia: requisitos do art. 77 e hipóteses do art. 78 do CPPM (fato que não é crime militar, punibilidade extinta, incompetência, ilegitimidade).
- Nulidades: rol do art. 500 do CPPM, sempre com demonstração de prejuízo (art. 499).
- Interrogatório: o CPPM o coloca antes das testemunhas (art. 302); o CPP o põe ao final (art. 400). Pedir o interrogatório ao final, com base no HC 127.900/AM do STF referido pelo STJ, e registrar o pedido em ata para evitar preclusão [VERIFICAR: julgado do STF não localizado no JuriBase; conferir no portal do STF a aplicação ao processo penal militar].
- Suprimento de omissões do CPPM pelo CPP só quando compatível com a índole do processo militar (CPPM art. 3º, a).

## Fundamentos verificados
- CPM arts. 9º e 125 (prescrição, redação da Lei 14.688/2023); CPPM arts. 3º, 77, 78, 302, 303, 390, 427 a 433, 499 e 500; CF arts. 5º, LV, 124 e 125, §§ 3º a 5º; Lei 8.457/1992, art. 30.
- Súmulas 90 e 78 do STJ.
- STJ, REsp 2.091.667 (5ª Turma, 21/05/2024): aplica o entendimento do STF de que o interrogatório é o último ato da instrução.
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Declínio de competência (Justiça comum, júri ou outra JM), com remessa dos autos.
- Nulidade do processo a partir do ato viciado, com indicação do prejuízo.
- Absolvição, com indicação da hipótese (fato inexistente, não ser crime, falta de prova, excludente).
- Subsidiariamente: desclassificação, reconhecimento da prescrição (CPM art. 125), pena mínima e benefícios cabíveis.
- Diligências do art. 427 do CPPM, com justificativa de pertinência.

## Checklist pré-protocolo
- [ ] Situação funcional, local e vítima conferidos contra o art. 9º do CPM
- [ ] Redação do art. 9º vigente na data do fato (Leis 13.491/2017 e 14.688/2023)
- [ ] Competência de órgão (juiz singular x Conselho) conferida
- [ ] Prescrição calculada pela pena máxima e pelos marcos interruptivos
- [ ] Nulidades arguidas com prejuízo concreto e no momento oportuno
- [ ] Pedido de interrogatório ao final registrado
- [ ] Prazo de oito dias das alegações controlado

## Erros a evitar
- Tratar o processo militar como se fosse o rito comum e perder prazo curto do CPPM.
- Arguir nulidade sem prejuízo (art. 499) ou depois da preclusão.
- Ignorar o deslocamento ao júri quando a vítima do crime doloso contra a vida é civil.
- Confundir punição disciplinar com crime militar: o mesmo fato pode gerar os dois, com instâncias independentes.

## Integração com o núcleo
`prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

---
name: penal-resposta-a-acusacao
description: >
  Redige a resposta à acusação do procedimento comum e do júri (CPP arts. 396,
  396-A, 397 e 406) e a defesa prévia da Lei de Drogas (Lei 11.343/2006, art. 55),
  com preliminares, pedido de absolvição sumária e rol de testemunhas. Use quando
  o usuário pedir resposta à acusação, defesa preliminar, defesa prévia, defesa
  escrita, peça após a citação, absolvição sumária ou rol de testemunhas da defesa.
metadata:
  area: penal
  tipo_peca: resposta-acusacao
  verificado_em: 2026-11-01
---
# Resposta à acusação e defesa prévia

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: citação no rito ordinário ou sumário (CPP 396), na primeira fase do júri (CPP 406) e notificação na Lei de Drogas (art. 55, defesa prévia anterior ao recebimento da denúncia).
- Usar também para a resposta nomeada pelo juízo (CPP 396-A §2º; LD 55 §3º).
- Não usar: Juizado Especial (rito sumaríssimo da Lei 9.099 tem defesa oral antes do recebimento); alegações finais (ver `penal-alegacoes-finais`); HC para trancar a ação (ver `penal-habeas-corpus`).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Denúncia ou queixa integral, decisão de recebimento (ou de notificação, na LD) e data da citação/notificação.
2. Inquérito: laudos, autos de apreensão, depoimentos, relatório final.
3. Situação prisional do acusado e eventuais cautelares em curso.
4. Antecedentes (FAC/certidões) para avaliar ANPP, transação, suspensão do processo.
5. Versão do cliente e testemunhas que a defesa pretende ouvir (nome, qualificação, endereço, o que sabem).
6. Estratégia: revelar ou não a tese de mérito agora (é legítimo reservar o mérito).

## Prazo e contagem
- 10 dias (CPP 396; CPP 406 no júri; LD art. 55). Prazos penais são contínuos e peremptórios (CPP 798): não se interrompem em fim de semana ou feriado; exclui-se o dia do começo e inclui-se o do vencimento (798 §1º); termo final em domingo/feriado prorroga para o dia útil seguinte (798 §3º).
- Conta-se da citação pessoal, não da juntada do mandado (Súmula 710 do STF). Citação por edital: conta do comparecimento do acusado ou do defensor constituído (CPP 396 p.ú.; 406 §1º).
- Suspensão de 20/12 a 20/01 (CPP 798-A), salvo réu preso e procedimentos da Lei Maria da Penha.
- Defensoria Pública: prazo em dobro (LC 80/1994, art. 44, I, e correlatas estaduais).
- Confirme a data com a skill `prazos-processuais`.

## Estrutura da peça
Resumo (detalhe em [estrutura](references/estrutura.md)):
1. Endereçamento e qualificação; indicação do rito.
2. Síntese da imputação.
3. Preliminares: nulidades, incompetência, inépcia, falta de justa causa (CPP 395), exceções em apartado (396-A §1º), propostas despenalizadoras não oferecidas (ANPP, art. 89 da Lei 9.099).
4. Absolvição sumária (CPP 397), se houver causa manifesta.
5. Mérito (opcional; pode ser reservado para as alegações finais).
6. Provas: documentos, perícias, diligências e rol de testemunhas qualificadas.
7. Pedidos.

## Requisitos e preliminares
- Limite de testemunhas: 8 no ordinário (CPP 401) e na primeira fase do júri (406 §3º); 5 no sumário (CPP 532) e na Lei de Drogas (art. 55 §1º). Não entram no limite as que não prestam compromisso e as referidas (401 §1º).
- Requerer intimação quando necessário; caso contrário, a defesa assume o ônus de levar a testemunha.
- Absolvição sumária (CPP 397): excludente manifesta de ilicitude; excludente manifesta de culpabilidade (salvo inimputabilidade); fato evidentemente atípico; extinção da punibilidade. No júri a absolvição sumária é a do art. 415 e ocorre após a instrução.
- Lei de Drogas: defesa prévia antes do recebimento; peça deve pedir a rejeição da denúncia; o juiz decide em 5 dias (art. 55 §4º).
- Exceções (suspeição, incompetência, litispendência, coisa julgada, ilegitimidade) correm em apartado.

## Fundamentos verificados
Resumo (detalhe em [fundamentos](references/fundamentos.md)): CPP 395, 396, 396-A, 397, 401, 406, 532, 798; LD 55; Súmula 710 STF; Súmula 707 STF; Súmula 523 STF; STJ Tema 1258 (reconhecimento de pessoas).

## Pedidos e requerimentos
- Acolhimento das preliminares (nulidade, rejeição tardia da denúncia por falta de justa causa, remessa ao juízo competente).
- Absolvição sumária com indicação do inciso do art. 397.
- Subsidiariamente: remessa ao MP para análise de ANPP ou suspensão condicional do processo; revogação ou substituição de cautelares.
- Produção de provas especificadas e intimação das testemunhas arroladas.

## Checklist pré-protocolo
- [ ] Data da citação conferida e prazo contínuo calculado (CPP 798) com `prazos-processuais`.
- [ ] Rito identificado e limite de testemunhas respeitado (8, 5 ou 5).
- [ ] Cada testemunha com nome, qualificação, endereço e pedido de intimação, se for o caso.
- [ ] Preliminares com o dispositivo e o prejuízo concreto demonstrado.
- [ ] Inciso do art. 397 indicado para cada tese de absolvição sumária.
- [ ] Verificado cabimento de ANPP (CPP 28-A) e de suspensão do processo (Lei 9.099, art. 89).
- [ ] Documentos anexados e identificados.
- [ ] Precedentes acrescentados passaram por `verificacao-de-citacoes`.
- [ ] Nenhum fato afirmado sem lastro nos autos ou na entrevista (`fidelidade-factual`).

## Erros a evitar
- Perder o prazo achando que é em dias úteis: no processo penal é contínuo.
- Contar da juntada do mandado (Súmula 710 STF manda contar da intimação).
- Arrolar testemunhas acima do limite ou sem qualificação, ou deixar o rol para depois (preclusão).
- Pedir absolvição sumária por "dúvida razoável" sobre autoria: o art. 397 exige causa manifesta; dúvida é mérito.
- Na Lei de Drogas, apresentar resposta como se a denúncia já tivesse sido recebida, sem pedir a rejeição.
- Antecipar tese de mérito que dá à acusação tempo de reforçar prova, sem decisão estratégica.
- Ignorar o ANPP para fatos anteriores à Lei 13.964/2019 em processos sem trânsito (ver `penal-anpp`).

## Integração com o núcleo
- `prazos-processuais`: cálculo do prazo contínuo e das suspensões.
- `verificacao-de-citacoes`: todo precedente adicional.
- `fidelidade-factual`: fatos só dos autos ou do cliente.
- `estilo-forense`: redação final.
- `juros-e-correcao`: apenas se houver discussão de valor mínimo de reparação (CPP 387, IV).

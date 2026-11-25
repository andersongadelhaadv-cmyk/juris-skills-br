---
name: penal-arguicao-de-nulidades
description: >
  Redige petição de arguição de nulidade processual penal (CPP arts. 563 a 573),
  com enquadramento no art. 564, demonstração de prejuízo, momento de arguição
  (art. 571), extensão aos atos dependentes (art. 573) e desentranhamento de
  prova ilícita (art. 157). Use quando o usuário pedir para arguir nulidade no
  processo criminal, apontar vício de citação, intimação, defesa, fundamentação
  ou competência, pedir anulação de ato e dos atos derivados, ou enfrentar a
  tese de nulidade de algibeira e de ausência de prejuízo.
metadata:
  area: penal
  tipo_peca: requerimento
  verificado_em: 2026-11-25
---
# Arguição de nulidades processuais penais

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: petição autônoma ao juízo da causa para declarar nulo um ato (citação, intimação, ausência ou deficiência de defesa, decisão sem fundamentação, incompetência, ilegitimidade, falta de formalidade essencial) e os atos que dele dependem; ou capítulo de nulidade dentro de outra peça.
- Não usar como peça principal quando a nulidade já deve ir em peça própria do rito:
  - na primeira manifestação após a citação: `penal-resposta-a-acusacao`;
  - nos memoriais: `penal-alegacoes-finais`;
  - após a sentença: `penal-apelacao-criminal` ou `penal-recurso-em-sentido-estrito`;
  - com prisão ou ameaça à liberdade, ou nulidade manifesta que exige via rápida: `penal-habeas-corpus`;
  - após o trânsito em julgado: `penal-revisao-criminal`;
  - vício no inquérito ou no PIC, antes da ação: `penal-defesa-no-inquerito-policial` e `penal-defesa-em-pic`.
- Nulidade no processo civil: `civel-*`; no processo administrativo disciplinar: `adm-defesa-em-pad`.

## Entradas mínimas (perguntar o que faltar; nunca supor fatos)
1. Rito (comum ordinário, sumário, sumaríssimo, júri, especial) e fase atual.
2. O ato viciado: o que aconteceu, data, folha ou ID nos autos.
3. A forma legal violada (dispositivo) e o que deveria ter acontecido.
4. O prejuízo concreto à defesa: o que a defesa deixou de fazer, provar ou contraditar por causa do vício.
5. Se a defesa contribuiu para o vício ou aceitou seus efeitos (CPP 565 e 572, III).
6. Se o vício já foi alegado antes, quando e com que resultado (preclusão).
7. Atos posteriores que dependem do ato viciado (para o pedido de extensão).

## Prazo e contagem
- Momento de arguição: CPP 571, conforme a fase (incisos I a VIII). Vários incisos remetem a artigos já reformados (406, 500, 537); adapte à fase equivalente do rito atual e registre essa leitura na peça.
- Regra prática: nulidade surgida em audiência ou sessão se argui logo após ocorrer (571, VIII), com registro em ata; as demais, na primeira oportunidade de falar nos autos.
- Nulidades relativas não arguidas a tempo ficam sanadas (572, I). A alegação guardada para depois é tratada como "nulidade de algibeira" e rejeitada.
- Contagem de prazos e suspensão de fim de ano (CPP 798-A): `prazos-processuais`.

## Estrutura da peça
Endereçamento ao juízo da causa → síntese do ato viciado → enquadramento legal (564) → natureza (absoluta ou relativa) → tempestividade (571) → prejuízo concreto (563 e 566) → ausência de causa da defesa (565) → extensão (573 §§ 1º e 2º) → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Prejuízo: sempre demonstre. A jurisprudência do STJ exige prejuízo concreto mesmo em nulidade alegada como absoluta; não confie na presunção.
- Defesa ausente é nulidade absoluta; defesa deficiente só anula com prova de prejuízo (Súmula 523/STF). Diferencie expressamente.
- Incompetência anula só os atos decisórios (567); por prevenção é relativa (Súmula 706/STF).
- Ilegitimidade do representante pode ser sanada a qualquer tempo (568); omissões da denúncia podem ser supridas até a sentença (569).
- Comparecimento do réu supre a falta de citação ou intimação (570), mas o juiz deve suspender ou adiar o ato se a irregularidade puder prejudicar a parte.
- Prova ilícita: pedido próprio de desentranhamento e inutilização (157 e §§), além da nulidade dos derivados (157 § 1º, salvo fonte independente).

## Fundamentos verificados
- CF 5º LIV, LV e LVI; CF 93 IX (decisões fundamentadas, sob pena de nulidade).
- CPP 563 (prejuízo), 564 I a V e parágrafo único, 565, 566, 567, 568, 569, 570, 571, 572, 573; CPP 157 e §§ (prova ilícita).
- Súmulas 523 e 706 do STF.
- STJ: nulidade exige prejuízo concreto (AgRg no RHC 218.825, 6ª Turma, 2026); vício não arguido no momento oportuno preclui — "nulidade de algibeira" (AgRg na RvCr 6.633, 3ª Seção, 2025).
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Declaração de nulidade do ato, com indicação precisa (folha/ID e data).
- Declaração expressa dos atos alcançados (573 §§ 1º e 2º) e sua renovação ou retificação (573 caput).
- Desentranhamento e inutilização da prova ilícita e das derivadas (157), quando for o caso.
- Pedido subsidiário: se o juízo entender relativa, que reconheça a arguição tempestiva e o prejuízo demonstrado.
- Registro do pré-questionamento (dispositivos legais e constitucionais) para recurso futuro.
- Réu preso e nulidade que contamina o título da prisão: pedir também o relaxamento (`penal-liberdade-provisoria-e-relaxamento`).

## Checklist pré-protocolo
- [ ] Ato viciado identificado com folha/ID e data
- [ ] Inciso e alínea do art. 564 (ou outra norma) indicados
- [ ] Natureza (absoluta/relativa) fundamentada, sem depender só dela
- [ ] Prejuízo concreto narrado com fatos dos autos
- [ ] Tempestividade demonstrada (571) e ausência de aceitação (572, III)
- [ ] Defesa não deu causa ao vício (565)
- [ ] Atos dependentes listados para a extensão (573)
- [ ] Dispositivos pré-questionados
- [ ] Prazos conferidos em `prazos-processuais`

## Erros a evitar
- Alegar nulidade "absoluta" sem narrar prejuízo e confiar na presunção.
- Guardar a nulidade para o recurso: é o caminho da preclusão (572, I) e da tese de algibeira.
- Arguir vício a que a própria defesa deu causa ou que aceitou (565 e 572, III).
- Pedir a nulidade de "todo o processo" sem indicar quais atos dependem do viciado.
- Confundir defesa ausente com defesa deficiente (Súmula 523/STF).
- Tratar incompetência como se anulasse a instrução inteira (567 limita aos decisórios).

## Integração com o núcleo
`prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`, `roteador-de-pecas`.

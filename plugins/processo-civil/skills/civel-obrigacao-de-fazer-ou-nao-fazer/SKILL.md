---
name: civel-obrigacao-de-fazer-ou-nao-fazer
description: >
  Redige petição inicial de ação de obrigação de fazer ou de não fazer com
  pedido de tutela específica ou de resultado prático equivalente (CPC, arts.
  497 a 501), tutela inibitória e de remoção do ilícito, multa periódica e
  medidas de apoio (arts. 536 e 537), conversão em perdas e danos só a pedido
  ou por impossibilidade, e alerta da Súmula 410/STJ (Tema 1.296). Use quando o
  usuário pedir ação para obrigar alguém a fazer algo, cumprir contrato em
  espécie, parar de fazer algo, desfazer obra, abster-se de ato ilícito,
  entregar documento, emitir declaração de vontade ou fixar astreintes.
metadata:
  area: processo-civil
  tipo_peca: inicial
  verificado_em: 2026-11-25
---
# Ação de obrigação de fazer ou de não fazer

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar quando o bem da vida é **a própria conduta** do réu: prestar serviço, concluir obra, transferir registro, fornecer documento, retirar algo do ar, abster-se de concorrência, cessar ruído, desfazer construção, emitir declaração de vontade (CPC, art. 501).
- Usar também para a **tutela inibitória** (impedir que o ilícito ocorra, se repita ou continue) e de **remoção do ilícito**, que dispensam prova de dano, culpa ou dolo (art. 497, parágrafo único).
- Não usar (skill vizinha mais específica):
  - Plano de saúde, medicamento ou tratamento → `consumidor-plano-de-saude`, `saude-medicamento-tratamento-sus`.
  - Remoção de conteúdo na internet → `digital-remocao-de-conteudo`.
  - Escritura definitiva de imóvel compromissado → `imob-adjudicacao-compulsoria`.
  - Entrega de coisa (dar, não fazer) → `civel-peticao-inicial`, observando o art. 498.
  - Só a tutela urgente, com pedido principal depois → `civel-tutela-provisoria`.
  - Obrigação reconhecida em título extrajudicial → `civel-execucao-titulo-extrajudicial`.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Fonte da obrigação: contrato (cláusula exata), lei, ato ilícito ou dever de vizinhança.
2. A conduta devida, descrita de forma verificável: o quê, onde, como, em que prazo.
3. A prestação é **personalíssima** (só o réu pode cumprir) ou pode ser executada por terceiro? (muda a estratégia: CC, arts. 247 e 249).
4. Prova do descumprimento e da notificação ao réu, com datas.
5. Urgência concreta e o dano que a demora causa.
6. O cliente prefere o cumprimento ou a indenização? Há prejuízos já sofridos para cumular?
7. Patrimônio do réu (multa só funciona contra quem pode pagá-la).

## Prazo e contagem
- Prescrição conforme a fonte da obrigação: contratual sem prazo específico, 10 anos (CC, art. 205, na linha da 2ª Seção do STJ); reparação civil cumulada, 3 anos (art. 206, § 3º, V). Na obrigação de não fazer continuada, cada violação renova o ilícito [VERIFICAR: termo inicial em obrigação negativa de trato sucessivo não foi conferido em precedente].
- O prazo para cumprir é fixado pelo juiz; peça prazo concreto e razoável (art. 537, caput). Contagem: `prazos-processuais`.

## Estrutura da peça
Endereçamento → qualificação → síntese → fatos → fonte e conteúdo da obrigação → descumprimento → tutela específica e resultado equivalente → tutela provisória com multa e medidas de apoio → pedidos (principal, subsidiário de conversão, perdas e danos cumuladas) → provas → valor da causa → audiência. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Pedido determinado**: descrever a conduta como deverá constar da ordem judicial; ordem vaga é inexequível.
- **Conversão em perdas e danos**: só se o autor pedir ou se a tutela específica for impossível (art. 499). Em responsabilidade contratual dos arts. 441, 618 e 757 do CC e em responsabilidade subsidiária ou solidária, o juiz dá primeiro ao réu a faculdade de cumprir em espécie (art. 499, parágrafo único, Lei 14.833/2024).
- **Multa**: independe de pedido, cabe em tutela provisória, sentença ou execução, deve ser suficiente e compatível e com prazo razoável (art. 537); é devida desde o descumprimento (§ 4º) e pode ser revista quanto às parcelas vincendas (§ 1º). Indenização não exclui a multa (art. 500).
- **Intimação pessoal**: a cobrança da multa exige prévia intimação pessoal do devedor (Súmula 410/STJ), entendimento mantido sob o CPC/2015 no Tema 1.296. Peça expressamente a intimação pessoal da decisão que fixar a multa.

## Fundamentos verificados
CPC arts. 497 a 501, 536, 537, 300, 311, 292, 319; CC arts. 247, 248, 249, 251; Súmula 410/STJ; Tema 1.296/STJ (REsp 2.096.505). Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Tutela de urgência (art. 300) ou da evidência (art. 311) para cumprimento imediato, com prazo, multa periódica e teto sugerido, e **intimação pessoal** do réu.
- Medidas de apoio (art. 536, § 1º): busca e apreensão, remoção de pessoas e coisas, desfazimento de obra, impedimento de atividade nociva, força policial.
- Procedência para impor a obrigação ou a abstenção, com tutela específica ou resultado prático equivalente (art. 497).
- Subsidiariamente, autorização para execução por terceiro à custa do réu (CC, art. 249) ou conversão em perdas e danos (art. 499).
- Perdas e danos já sofridos, cumulados; correção e juros pelo núcleo `juros-e-correcao`.
- Citação; custas e honorários; provas.

## Checklist pré-protocolo
- [ ] Conduta descrita de forma verificável (o quê, onde, como, prazo)
- [ ] Fonte da obrigação juntada (contrato, lei, prova do ilícito)
- [ ] Prova do descumprimento e da notificação
- [ ] Pedido de multa com valor, periodicidade e prazo razoável
- [ ] Pedido expresso de intimação pessoal (Súmula 410 / Tema 1.296)
- [ ] Pedido subsidiário de execução por terceiro ou de conversão
- [ ] Valor da causa pelo conteúdo econômico da obrigação (art. 292, § 3º)

## Erros a evitar
- Pedir "que o réu cumpra o contrato" sem dizer qual conduta: a ordem não se executa.
- Pedir só perdas e danos quando o cliente quer o resultado: a conversão é escolha do autor (art. 499).
- Multa simbólica ou desproporcional: o juiz revê (art. 537, § 1º) e o efeito coercitivo se perde.
- Deixar de pedir a intimação pessoal e ver a multa acumulada ser afastada.
- Para prestação personalíssima, não prever a alternativa de perdas e danos se o réu se recusar (CC, art. 247).

## Integração com o núcleo
`prazos-processuais`, `juros-e-correcao`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

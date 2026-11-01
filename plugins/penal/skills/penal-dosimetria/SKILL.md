---
name: penal-dosimetria
description: >
  Analisa e impugna a dosimetria da pena pelo critério trifásico (CP arts. 59 e
  68), com regime inicial (art. 33 e STF Tema 972), substituição (art. 44), sursis
  (art. 77), detração e súmulas do STJ e do STF sobre pena-base, atenuantes e
  majorantes, inclusive no feminicídio autônomo (art. 121-A, Lei 14.994/2024).
  Use quando o usuário pedir cálculo de pena, revisão da dosimetria, pena-base,
  atenuante abaixo do mínimo, regime inicial, hediondo em regime semiaberto,
  substituição da pena ou tese de redução de pena.
metadata:
  area: penal
  tipo_peca: outro
  verificado_em: 2026-11-01
---
# Dosimetria da pena

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: teses de pena em alegações finais, apelação, embargos, revisão criminal, HC; conferência do cálculo da sentença.
- Não usar sozinha para a peça: combine com `penal-alegacoes-finais`, `penal-apelacao-criminal` ou `penal-revisao-criminal`. Frações de execução ficam em `penal-progressao-de-regime`.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Sentença (ou memoriais da acusação) com a fundamentação de cada fase.
2. Tipo penal, pena cominada, qualificadoras, majorantes e minorantes reconhecidas.
3. Folha de antecedentes com datas de trânsito e extinção das penas anteriores (CP 64, I — período depurador de 5 anos).
4. Tempo de prisão provisória (detração para regime — CPP 387 §2º).
5. Confissão, menoridade relativa ou idade acima de 70 na sentença, reparação do dano.

## Prazo e contagem
A dosimetria segue o prazo da peça em que for discutida (apelação: 5 + 8 dias; memoriais: 5 dias), contínuo (CPP 798). Use `prazos-processuais`.

## Estrutura da peça
Resumo (detalhe em [estrutura](references/estrutura.md)): quadro com as três fases da sentença x pena pretendida; impugnação por vetor; fase 2; fase 3; concurso de crimes; regime; substituição; sursis; detração; pedido com o quantum.

## Requisitos e preliminares
- Fase 1 (CP 59): oito vetores; cada vetor negativo exige fundamento concreto que extrapole o tipo. Inquéritos e ações em curso não agravam a pena-base (Súmula 444 STJ). A mesma condenação não pode ser maus antecedentes e reincidência (Súmula 241 STJ).
- Fase 2 (CP 61 a 66): atenuante não leva abaixo do mínimo (Súmula 231 STJ, vigente). Confissão atenua mesmo que não usada pelo juiz (Súmula 545 STJ, redação revisada em 10/09/2025). Menoridade relativa e maior de 70 na sentença, salvo crime com violência sexual contra a mulher (CP 65, I, Lei 15.160/2025).
- Fase 3 (CP 68 p.ú.): no concurso de majorantes da parte especial, o juiz pode aplicar só a maior; no roubo, aumento acima do mínimo exige fundamento concreto, não o número de majorantes (Súmula 443 STJ).
- Regime (CP 33 §§2º e 3º): pena-base no mínimo impede regime mais gravoso só pela gravidade abstrata (Súmula 440 STJ; Súmulas 718 e 719 STF). Reincidente com pena até 4 anos e circunstâncias favoráveis pode iniciar no semiaberto (Súmula 269 STJ). Hediondo: o regime fechado obrigatório do art. 2º §1º da Lei 8.072/1990 é inconstitucional; aplicam-se os critérios do CP 33 (STF Tema 972). Detração entra no cálculo do regime (CPP 387 §2º).
- Feminicídio (CP 121-A, Lei 14.994/2024): crime autônomo, reclusão de 20 a 40 anos; causas de aumento de 1/3 até a metade no §2º; circunstâncias do §1º comunicam-se ao coautor (§3º). Lei mais grave: não retroage a fatos anteriores à vigência da Lei 14.994/2024 (sancionada em 09/10/2024, publicada no DOU de 10/10/2024 e em vigor na publicação, art. 10; antes, o feminicídio era qualificadora do art. 121 §2º, VI). Fato até 09/10/2024 segue a lei anterior.
- Substituição (CP 44): pena até 4 anos, sem violência ou grave ameaça (ou crime culposo), não reincidente em doloso (com exceção do §3º). Vedada em violência doméstica com violência ou grave ameaça (Súmula 588 STJ).

## Fundamentos verificados
Resumo (detalhe em [fundamentos](references/fundamentos.md)): CP 33, 44, 59, 61 a 68, 77, 121-A; CPP 387; Súmulas 231, 241, 269, 440, 443, 444, 545, 588 STJ; Súmulas 718 e 719 STF; STF Tema 972.

## Pedidos e requerimentos
- Pena-base no mínimo legal (ou redução proporcional ao vetor afastado).
- Reconhecimento e aplicação das atenuantes; afastamento de agravantes não debatidas (no júri, só as alegadas — CPP 492, I, b).
- Causas de diminuição na fração máxima; majorantes na fração mínima.
- Regime inicial mais brando; substituição; sursis; detração.

## Checklist pré-protocolo
- [ ] Quadro das três fases montado (sentença x pretensão).
- [ ] Cada vetor negativo confrontado com a prova e com o tipo (bis in idem).
- [ ] Reincidência e maus antecedentes conferidos com datas (período depurador).
- [ ] Súmula 231 tratada como vigente; tese contrária só como superação expressa.
- [ ] Regime pedido considera detração e Tema 972 (hediondo).
- [ ] Lei do tempo do fato aplicada (feminicídio, CP 65 I).
- [ ] Precedentes conferidos em `verificacao-de-citacoes`.

## Erros a evitar
- Aceitar "culpabilidade elevada" ou "consequências graves" genéricas.
- Pedir atenuante abaixo do mínimo como se fosse pacífico.
- Afirmar que hediondo tem regime fechado obrigatório.
- Aplicar o art. 121-A a fato anterior à vigência da Lei 14.994/2024.
- Esquecer o valor mínimo de reparação (CPP 387, IV) e sua atualização — que segue o núcleo.

## Integração com o núcleo
- `juros-e-correcao`: correção do valor mínimo de reparação; nunca fixar índice aqui.
- `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

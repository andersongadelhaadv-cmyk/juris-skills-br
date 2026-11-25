---
name: trabalhista-recurso-adesivo
description: >
  Redige recurso adesivo no processo do trabalho (CPC art. 997, aplicado por
  força da CLT art. 769 e da Súmula 283 do TST), cabível em recurso ordinário,
  agravo de petição, recurso de revista e embargos, no prazo de 8 dias das
  contrarrazões, com matéria independente da do recurso principal. Use quando o
  usuário pedir recurso adesivo trabalhista, aderir ao recurso da parte
  contrária, recorrer depois de perder o prazo do recurso próprio havendo
  sucumbência recíproca, ou avaliar o risco de o adesivo cair junto com o
  principal.
metadata:
  area: trabalhista
  tipo_peca: recurso
  verificado_em: 2026-11-25
---
# Recurso adesivo trabalhista

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: houve sucumbência recíproca (CPC art. 997, §1º), a parte não recorreu no prazo próprio e a parte contrária interpôs recurso ordinário, agravo de petição, recurso de revista ou embargos ao TST (Súmula 283/TST).
- Não usar: a parte ainda está no prazo do recurso independente (prefira o recurso próprio, que não depende do outro): `trabalhista-recurso-ordinario`, `trabalhista-agravo-de-peticao`, `trabalhista-recurso-de-revista`, `trabalhista-embargos-sdi1`; agravo de instrumento ou embargos de declaração, que não estão na lista da Súmula 283; recurso adesivo cível (CPC art. 997, §2º, II: apelação, RE e REsp — ver `civel-apelacao`).

## Entradas mínimas (perguntar o que faltar; nunca supor fatos)
1. Decisão recorrida e capítulos em que a parte ficou vencida.
2. Recurso principal da outra parte: espécie, data da intimação para contrarrazões, matérias.
3. Situação de admissibilidade do recurso principal (tempestivo? preparado? há risco de desistência?).
4. Preparo exigível da parte que adere (depósito recursal e custas, se for o empregador condenado) [VERIFICAR valores vigentes].
5. Matérias que a parte quer devolver ao tribunal.

## Prazo e contagem
- 8 dias, que é o prazo de contrarrazões ao recurso principal (Súmula 283/TST; CPC art. 997, §2º, I).
- Peças distintas: contrarrazões ao principal e razões do adesivo, ambas no mesmo prazo.
- Contagem, intimação e suspensões: `prazos-processuais`.

## Estrutura da peça
Petição de interposição ao juízo perante o qual o principal foi interposto → razões dirigidas ao tribunal → cabimento (sucumbência recíproca + espécie da Súmula 283) → tempestividade (prazo de contrarrazões) → preparo → mérito, capítulo por capítulo → pedidos. Roteiro em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Subordinação:** o adesivo segue as regras de admissibilidade e de julgamento do recurso independente e não é conhecido se houver desistência do principal ou se este for inadmissível (CPC art. 997, §2º, caput e III). Avaliar o risco antes de abrir mão do recurso próprio.
- **Matéria livre:** não precisa ter relação com a matéria do recurso principal (Súmula 283/TST).
- **Mesmos pressupostos:** se o adesivo é de revista ou de embargos, valem todas as exigências desses recursos (transcendência, prequestionamento, divergência específica etc.); use a skill do recurso correspondente para o mérito.
- **Aplicação ao processo do trabalho:** CLT art. 769 e CPC art. 15 (supletividade), com a compatibilidade afirmada pela Súmula 283/TST.

## Fundamentos verificados
- CPC art. 997, §§1º e 2º (I e III).
- CLT art. 769; CPC art. 15.
- Súmula 283/TST: compatível com o processo do trabalho; cabe em 8 dias no RO, AP, RR e embargos; matéria não precisa se relacionar com a do recurso da parte contrária.
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Recebimento e processamento do adesivo junto com o principal.
- Conhecimento e provimento para reformar os capítulos indicados.
- Juros e correção, se a reforma alterar valores: `juros-e-correcao`.

## Checklist pré-protocolo
- [ ] Sucumbência recíproca demonstrada
- [ ] Espécie do principal está na lista da Súmula 283
- [ ] Prazo de contrarrazões (8 dias) conferido
- [ ] Contrarrazões e adesivo em peças separadas (ou capítulos claramente distintos)
- [ ] Preparo do adesivo recolhido, se exigível
- [ ] Pressupostos específicos do recurso (revista/embargos) cumpridos
- [ ] Cliente informado de que o adesivo cai se o principal for desistido ou inadmitido

## Erros a evitar
- Interpor adesivo em agravo de instrumento ou em embargos de declaração.
- Tratar o adesivo como contrarrazões (ou vice-versa) e perder um dos dois.
- Esquecer o preparo, presumindo que o adesivo é isento.
- Escolher o adesivo quando ainda havia prazo para o recurso próprio.

## Integração com o núcleo
`prazos-processuais`, `juros-e-correcao`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

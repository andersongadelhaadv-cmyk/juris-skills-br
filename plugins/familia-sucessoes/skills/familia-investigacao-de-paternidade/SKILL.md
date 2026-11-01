---
name: familia-investigacao-de-paternidade
description: >
  Redige ação de investigação de paternidade (ou maternidade), cumulada ou não com
  alimentos e petição de herança, com pedido de exame de DNA (Lei 8.560/1992, art. 2º-A;
  CC arts. 1.596 a 1.617; Súmula 301 do STJ). Use quando o usuário pedir investigação de
  paternidade, reconhecimento de paternidade, exame de DNA, DNA com parentes do falecido,
  paternidade post mortem, multiparentalidade, paternidade socioafetiva e biológica.
metadata:
  area: familia-sucessoes
  tipo_peca: inicial
  verificado_em: 2026-11-01
---
# Investigação de paternidade

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: filho sem paternidade registrada ou com registro que se quer complementar (multiparentalidade); investigação contra suposto pai vivo ou contra herdeiros do falecido; cumulação com alimentos e petição de herança.
- Não usar: negatória de paternidade/anulatória de registro pelo pai registral (CC 1.601, 1.604) — estrutura diferente; reconhecimento voluntário (cartório, CC 1.609).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Dados do autor (idade; se menor, representante) e certidão de nascimento.
2. Suposto pai: vivo ou falecido; endereço; herdeiros conhecidos (se falecido).
3. Relato do relacionamento da mãe com o suposto pai (período, provas: fotos, mensagens, testemunhas).
4. Existência de paternidade registral ou socioafetiva com outra pessoa.
5. Interesse em alimentos (necessidade/possibilidade) e herança (inventário aberto ou concluído).
6. Exame de DNA extrajudicial já feito, se houver.

## Prazo e contagem
- Investigação de paternidade é imprescritível; a petição de herança não é (Súmula 149 STF).
- Alimentos fixados na sentença de procedência são devidos desde a citação (Súmula 277 STJ).
- Prazos do rito das ações de família (CPC 693 e seguintes); contagem via `prazos-processuais`.

## Estrutura da peça
Endereçamento → qualificação → fatos (relacionamento e concepção) → direito ao estado de filiação → prova (DNA; presunção pela recusa) → alimentos → herança (se cabível) → tutela (alimentos provisórios com indícios) → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Competência: domicílio do alimentando quando cumulada com alimentos (Súmula 1 STJ; CPC 53, II); nas demais, regra geral.
- Legitimidade: filho (CC 1.606); MP após averiguação oficiosa sem reconhecimento (Lei 8.560 art. 2º §4º), sem excluir quem tenha legítimo interesse (§6º). Réus: suposto pai ou, se falecido, seus herdeiros.
- Qualquer pessoa com justo interesse pode contestar (CC 1.615).
- Segredo de justiça (CPC 189, II); MP intervém se houver incapaz.
- Paternidade socioafetiva registrada não impede o reconhecimento da biológica, com efeitos próprios (STF Tema 622).

## Fundamentos verificados
CF 227 §6º e CC 1.596 (igualdade dos filhos); Lei 8.560 arts. 2º e 2º-A (recusa gera presunção; DNA em parentes, Lei 14.138/2021); CC 1.606, 1.609, 1.614 a 1.616; Súmulas 301 e 277 STJ; Súmula 1 STJ; Súmula 149 STF; STF Tema 622. Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- [ ] Exame de DNA no réu ou, se falecido/desaparecido, em parentes consanguíneos, preferindo os de grau mais próximo, a expensas do autor (Lei 8.560 art. 2º-A §2º) — com pedido de gratuidade se cabível.
- [ ] Advertência de que a recusa gera presunção de paternidade, apreciada com o conjunto probatório (Lei 8.560 art. 2º-A §§1º e 2º; Súmula 301 STJ).
- [ ] Declaração da paternidade e averbação no registro civil (nome do pai, avós paternos; sobrenome, se pedido).
- [ ] Alimentos provisórios com base em indícios e definitivos desde a citação (Súmula 277 STJ) — usar `familia-acao-de-alimentos` para o capítulo.
- [ ] Petição de herança e reserva de quinhão no inventário, se houver (CPC 628 §2º).
- [ ] Multiparentalidade: manutenção do pai registral/socioafetivo e inclusão do biológico, se for o caso (Tema 622).

## Checklist pré-protocolo
- [ ] Certidão de nascimento atualizada.
- [ ] Indícios do relacionamento à época da concepção.
- [ ] Polo passivo completo (todos os herdeiros, se pai falecido).
- [ ] Parentes indicados para coleta de DNA, em ordem de proximidade.
- [ ] Definido se haverá pedido de alimentos e/ou herança (muda competência e réus).

## Erros a evitar
- Afirmar que a recusa ao DNA "prova" a paternidade: gera presunção relativa, a ser apreciada com as demais provas.
- Esquecer herdeiros no polo passivo da investigação post mortem.
- Pedir alimentos retroativos a data anterior à citação.
- Tratar a petição de herança como imprescritível.
- Requerer exclusão automática do pai socioafetivo sem pedido nem prova.

## Integração com o núcleo
`prazos-processuais`, `juros-e-correcao` (alimentos e herança), `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

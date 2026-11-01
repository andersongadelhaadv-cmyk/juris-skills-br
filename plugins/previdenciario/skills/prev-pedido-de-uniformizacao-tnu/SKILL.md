---
name: prev-pedido-de-uniformizacao-tnu
description: >
  Redige pedido de uniformização de interpretação de lei federal no Juizado
  Especial Federal, dirigido à Turma Regional ou à Turma Nacional de
  Uniformização (Lei 10.259/2001, art. 14; Regimento Interno da TNU, Resolução
  CJF 586/2019, arts. 12 a 14). Use quando o usuário pedir PEDILEF, incidente de
  uniformização, recurso à TNU, divergência entre turmas recursais, agravo contra
  inadmissão do pedido de uniformização ou cotejo analítico.
metadata:
  area: previdenciario
  tipo_peca: outro
  verificado_em: 2026-11-01
---
# Pedido de uniformização (TRU/TNU)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: acórdão de Turma Recursal do JEF que diverge, em questão de DIREITO MATERIAL, de: turma de outra região, súmula ou jurisprudência dominante do STJ ou da TNU (TNU); ou de turma da mesma região (TRU) (Lei 10.259, art. 14, §§1º e 2º; RITNU, art. 12, §1º).
- Não usar para: matéria processual (TNU Súmula 43); reexame de fatos e provas (TNU Súmula 42); acórdão em consonância com entendimento dominante do STF, STJ e TNU.
- Questão constitucional: recurso extraordinário (Lei 10.259, art. 15). Contrariedade da TNU a súmula/jurisprudência do STJ: pedido ao STJ (art. 14, §4º; RITNU, art. 31).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Acórdão recorrido (íntegra) e data da intimação.
2. Embargos de declaração opostos? Resultado e data.
3. Tese jurídica de direito material em disputa, em uma frase.
4. Paradigma(s): número do processo, órgão, data, íntegra ou link oficial; ou súmula/tema.
5. Fatos incontroversos fixados no acórdão (o pedido não pode depender de revê-los).

## Prazo e contagem
- 15 dias da intimação do acórdão recorrido, em dias úteis (RITNU, arts. 12 e 27, §2º). Contrarrazões no mesmo prazo (art. 12, §2º).
- Agravo contra inadmissão: 15 dias (art. 14, §§2º e 3º). Verificar qual agravo cabe conforme o fundamento da inadmissão (§5º se ambos).
- No JEF o INSS não tem prazo diferenciado (Lei 10.259, art. 9º).
- Conferir alterações posteriores do regimento [VERIFICAR resoluções CJF após 2025 sobre os arts. 12 a 14].

## Estrutura da peça   (detalhe em [estrutura](references/estrutura.md))
1. Petição de interposição à Turma Recursal de origem (dirigida ao Presidente).
2. Razões à TRU/TNU: cabimento, tempestividade, questão de direito material, prequestionamento.
3. Paradigma e cotejo analítico.
4. Mérito: qual a interpretação correta.
5. Pedidos.

## Requisitos e preliminares
- Paradigma válido, identificado, com cópia ou link oficial (dispensada a cópia para repetitivo do STJ ou representativo da TNU) (RITNU, art. 14, V).
- Cotejo analítico: demonstrar similitude fática e solução jurídica oposta, trecho a trecho; transcrever ementas não basta.
- Atacar todos os fundamentos suficientes do acórdão (art. 14, V, f).
- Questão de direito "pura": formular a tese sem depender de reavaliar laudo ou testemunhas.

## Fundamentos verificados   (detalhe em [fundamentos](references/fundamentos.md))
- Lei 10.259, art. 14 (cabimento; TRU, TNU e STJ); art. 15 (RE).
- RITNU (Res. CJF 586/2019), arts. 12, 13, 14, 27, §2º, e 31.
- TNU Súmulas 42 e 43.

## Pedidos e requerimentos
- Admissão e remessa à TNU (ou TRU).
- Conhecimento e provimento para fixar a tese X e reformar o acórdão; ou anulação com retorno à Turma de origem para adequação.
- Se houver tema afetado, sobrestamento.

## Checklist pré-protocolo
- [ ] Prazo de 15 dias úteis conferido (inclusive efeito de embargos de declaração).
- [ ] Divergência sobre direito material, não processual.
- [ ] Paradigma de outra região (TNU) ou da mesma região (TRU), ou súmula/jurisprudência dominante do STJ/TNU.
- [ ] Paradigma verificado em `verificacao-de-citacoes` com link oficial.
- [ ] Cotejo analítico em quadro comparativo.
- [ ] Nenhum pedido de reexame de prova.

## Erros a evitar
- Usar paradigma da mesma turma recursal ou decisão monocrática sem caráter de jurisprudência dominante [VERIFICAR regra do regimento].
- Fazer "cotejo" apenas com ementas.
- Discutir valoração do laudo pericial (Súmula 42 TNU).
- Citar paradigma de memória: sempre confirmar número e link.

## Integração com o núcleo
- `prazos-processuais` (15 dias úteis; agravos).
- `verificacao-de-citacoes` (obrigatório para cada paradigma).
- `fidelidade-factual` (o que o acórdão recorrido fixou).
- `estilo-forense`; `juros-e-correcao` se a tese envolver índice de atualização.

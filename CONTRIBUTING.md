# Como contribuir

Toda contribuição passa por pull request e pelo validador.

## Regras de conteúdo

1. **Texto próprio.** Não copie trechos de outros materiais. Texto de lei e enunciado de súmula podem ser transcritos, desde que venham da fonte oficial.
2. **Nada de memória.** Número de processo, relator, data de julgamento e ementa só entram se confirmados em fonte oficial ou no JuriBase.
3. **Registro de verificação.** Toda norma e todo precedente citado entram no `fontes.yaml` da skill, com status, URL e data da consulta.
4. **Juros e correção.** Skills de área não definem taxa própria: remetem a `nucleo/juros-e-correcao`.
5. **Na dúvida, marque.** Escreva `[VERIFICAR: motivo]` em vez de afirmar.

## Status aceitos no `fontes.yaml`

| Status | Quando usar |
| --- | --- |
| `LEI` | Norma conferida nos dados abertos do Senado, na Câmara ou no texto compilado oficial |
| `CONFIRMADO` | Precedente, súmula ou tema confirmado no JuriBase ou no site do tribunal |
| `DIVERGENCIA_CORRIGIDA` | Citação existia com dado diferente e foi corrigida |
| `VERIFICAR` | Não foi possível confirmar; o texto da skill traz `[VERIFICAR]` |

Campo opcional por item: `revisar_ate: AAAA-MM-DD`. Use em tese de Turma, tema com
julgamento pendente e valores que mudam (teto de depósito recursal, alçadas). Quando a
data passa, o validador falha até a citação ser reconferida e a data, renovada.

## O que o validador cobra

- **Citação com registro.** Toda súmula, tema, ADI/ADC/ADPF e processo (REsp, RE, HC
  e afins) citado no `SKILL.md` ou em `references/` precisa de item no `fontes.yaml`.
  As lacunas que já existiam estão em `scripts/pendencias-citacoes.txt`: elas só geram
  aviso, e a lista só pode diminuir. Citação nova sem registro faz o CI falhar.
- **Registro e texto coerentes.** Item com status `VERIFICAR` exige `[VERIFICAR]` no
  texto da skill.
- **Validade.** `verificado_em` com mais de 90 dias gera aviso; com mais de 180, erro.
  Em `previdenciario` e `tributario-fazenda`, 45 e 90 dias. O CI roda também toda
  segunda-feira, então a skill vence mesmo sem commit novo.

## Estrutura de uma skill

```
plugins/<area>/skills/<nome>/
  SKILL.md                  até 200 linhas
  references/estrutura.md   roteiro da peça
  references/fundamentos.md fundamentos verificados
  fontes.yaml               registro de verificação
```

## Antes de abrir o pull request

```bash
python3 -m unittest scripts/test_validar.py
python3 scripts/validar.py
claude plugin validate .
```

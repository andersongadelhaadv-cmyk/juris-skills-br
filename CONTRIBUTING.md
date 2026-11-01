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
python3 scripts/validar.py
claude plugin validate .
```

---
name: consumidor-defesa-do-fornecedor
description: >
  Redige contestação do fornecedor (empresa, banco, operadora, companhia aérea,
  varejista) em ação de consumo, com as excludentes dos arts. 12, § 3º, e 14, § 3º,
  do CDC, ausência de dano, culpa exclusiva do consumidor ou de terceiro,
  resistência à inversão do ônus, Súmula 385 do STJ e impugnação do valor. Use
  quando o usuário pedir contestação para empresa ré, defesa de banco em fraude
  ou golpe, defesa contra dano moral, defesa em ação de negativação, defesa de
  companhia aérea ou de plano de saúde, ou quando atuar do lado do fornecedor.
metadata:
  area: consumidor
  tipo_peca: contestacao
  verificado_em: 2026-11-01
---
# Contestação do fornecedor em ação de consumo

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: defesa do réu fornecedor em ação indenizatória, de vício, negativação, revisional, repetição, plano de saúde ou transporte aéreo.
- Não usar sem adaptação: Juizado (contestação na audiência, regras da Lei 9.099/1995); reconvenção (peça própria no corpo da contestação, CPC 343).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Data da citação/juntada do AR ou mandado e data da audiência (termo inicial do prazo).
2. Versão do fornecedor com documentos: contrato assinado/eletrônico, logs, gravações, geolocalização, telas de sistema, protocolos, comunicações enviadas, comprovante de notificação.
3. O que o fornecedor fez após a reclamação (estorno, solução, oferta de acordo).
4. Há outras anotações legítimas em nome do autor? (Súmula 385.)
5. Houve participação de terceiro (golpista, outra empresa da cadeia) ou conduta do próprio autor (senha fornecida, uso inadequado)?
6. Limites de alçada para acordo e política do cliente.

## Prazo e contagem
- Contestação: 15 dias úteis (CPC 335, 219), contados conforme art. 335, I a III (audiência, protocolo de cancelamento ou citação). Calcular com `prazos-processuais`.
- Juizado: até a audiência de instrução, conforme regra local.
- Prejudiciais: decadência (CDC 26) para pedido redibitório; prescrição (CDC 27 ou prazo específico) para indenização — conferir datas.

## Estrutura da peça
Tempestividade → preliminares (CPC 337) → prejudiciais (prescrição/decadência) → impugnação da inversão do ônus → mérito: fatos do fornecedor; inexistência de defeito; excludentes; ausência de dano; Súmula 385 → impugnação de valores → pedidos subsidiários → provas. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Princípio da eventualidade e impugnação específica (CPC 336 e 341): todo fato não impugnado presume-se verdadeiro.
- Preliminares típicas: ilegitimidade passiva (comerciante fora do art. 13; empresa estranha à cadeia), incompetência (Juizado com prova pericial complexa), inépcia (revisional sem incontroverso — CPC 330 § 2º), impugnação ao valor da causa e à gratuidade, falta de interesse (ex.: plano de saúde sem requerimento prévio — exigência das teses do STF).
- Denunciação da lide é vedada na hipótese do art. 13 p.ú. (CDC art. 88) — usar regresso autônomo.

## Fundamentos verificados
- CDC art. 12 § 3º (não colocou no mercado; defeito inexiste; culpa exclusiva do consumidor ou de terceiro); art. 14 § 3º (defeito inexiste; culpa exclusiva); art. 14 § 4º (profissional liberal: culpa).
- STJ: fraude por engenharia social com senha e dispositivos legítimos do consumidor → fortuito externo e culpa exclusiva; Súmula 479 afastada sem falha do sistema bancário (REsp 2.238.532). Contraponto: Súmula 479 (fortuito interno).
- Súmula 385 (inscrição preexistente legítima); Súmula 404 (AR dispensável); Súmula 359 (notificação é do mantenedor).
- Atraso de voo: dano moral não presumido (AREsp 3.038.979); CBA 251-A e 256.
- Fraude bancária sem peculiaridades: sem dano moral (REsp 2.195.198); dobra com modulação (EAREsp 1.501.756).
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Acolhimento das preliminares/prejudiciais; no mérito, improcedência.
- Subsidiariamente: fixação moderada do dano moral (método bifásico, precedentes análogos); devolução simples em vez de dobro; abatimento de valores já estornados; termos iniciais de juros/correção conforme `juros-e-correcao` do núcleo.
- Indeferimento ou delimitação da inversão do ônus; produção das provas indicadas.
- Condenação do autor por litigância de má-fé apenas com fatos concretos (CPC 80).

## Checklist pré-protocolo
- [ ] Prazo calculado em dias úteis e termo inicial correto
- [ ] Todos os fatos da inicial impugnados especificamente
- [ ] Documentos técnicos (logs, contratos, gravações) juntados e explicados
- [ ] Excludente escolhida descrita com prova (não só alegada)
- [ ] Súmula 385 verificada no extrato do autor (casos de negativação)
- [ ] Pedidos subsidiários de valor (dano moral, dobro, juros) formulados
- [ ] Preliminares realmente cabíveis (evitar preliminar genérica)
- [ ] Proposta de acordo avaliada com o cliente

## Erros a evitar
- Alegar "fato de terceiro" quando o risco é inerente à atividade (fortuito interno — Súmula 479 em banco).
- Contestação genérica sem impugnar cada fato (CPC 341).
- Defender limitação contratual de responsabilidade vedada (CDC arts. 25 e 51, I).
- Denunciar a lide nos casos do art. 13 do CDC (art. 88).
- Deixar de pedir, subsidiariamente, redução do valor e repetição simples.
- Juntar documentos sem explicar o que provam.

## Integração com o núcleo
`juros-e-correcao` (termos iniciais e índices na defesa subsidiária), `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

---
name: consumidor-defesa-procon
description: >
  Redige a defesa (impugnação) e o recurso do fornecedor em processo
  administrativo sancionador do Procon ou de outro órgão do SNDC, com base no
  Decreto 2.181/1997 (auto de infração, defesa em 20 dias, recurso em 10 dias com
  efeito suspensivo quanto à multa, atenuantes e agravantes, dosimetria) e nos
  arts. 55 a 57 do CDC. Use quando o usuário pedir defesa em auto de infração do
  Procon, impugnação de multa do Procon, recurso administrativo contra sanção
  consumerista, redução da multa, nulidade do processo administrativo ou
  estratégia antes da inscrição em dívida ativa.
metadata:
  area: consumidor
  tipo_peca: outro
  verificado_em: 2026-11-25
---
# Defesa em processo administrativo do Procon (Decreto 2.181/1997)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: fornecedor notificado de auto de infração ou de ato de instauração de processo administrativo por órgão de defesa do consumidor (Procon estadual/municipal, Senacon).
- Usar também para o recurso à autoridade superior contra a decisão condenatória.
- Não usar: reclamação individual de consumidor em audiência de conciliação no Procon (não é processo sancionador); ação judicial do consumidor (`consumidor-defesa-do-fornecedor`).
- Após o fim da via administrativa: anulação judicial ou mandado de segurança (`adm-mandado-de-seguranca`, `civel-peticao-inicial`); multa já executada: `trib-embargos-a-execucao-fiscal` ou `trib-excecao-pre-executividade-fiscal`.
- Sanção da ANPD por dados pessoais: `digital-defesa-em-processo-sancionador-anpd`.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Íntegra do auto de infração ou do ato de instauração e da notificação, com a data exata do recebimento.
2. Órgão autuante (estadual, municipal, Senacon) e a lei/portaria local de procedimento e de dosimetria.
3. Fatos imputados, dispositivos indicados, número de reclamações e período.
4. Documentos do fornecedor: atendimento dado ao consumidor, políticas, contratos, peça publicitária, comprovantes de solução.
5. Histórico: primariedade ou decisões administrativas irrecorríveis nos últimos 5 anos (reincidência).
6. Faturamento informado ou estimado pelo órgão (base da condição econômica) e adesão ao Consumidor.gov.br.

## Prazo e contagem
- Defesa/impugnação: 20 dias do recebimento da notificação (Decreto 2.181/1997, arts. 42 e 44); o auto de infração segue o mesmo prazo (art. 38 c/c 42).
- Recurso: 10 dias da intimação da decisão (art. 49); na Senacon, 10 dias ao Secretário (art. 50).
- Os prazos são preclusivos (art. 54). Pagamento da multa definitiva e inscrição em dívida ativa se não paga em 30 dias (art. 55).
- Lei ou portaria local pode fixar contagem e prazos próprios: conferir antes de protocolar. Contagem em geral: `prazos-processuais`.

## Estrutura da peça
Tempestividade → preliminares (competência, requisitos do auto/ato, notificação, cerceamento, prescrição) → mérito (inexistência da infração, atipicidade, fato isolado já resolvido) → dosimetria (pena-base, atenuantes, agravantes, bis in idem, proporcionalidade) → pedidos e provas. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Requisitos do auto de infração (art. 35) e do ato de instauração (art. 40): identificação, descrição dos fatos, dispositivos infringidos, assinatura, prazo de defesa. Ausência = nulidade a arguir.
- Competência do órgão: os órgãos estaduais e municipais criados por lei fiscalizam e julgam no processo administrativo (art. 4º).
- Decisão deve conter resumo da defesa, apreciação das provas e dosimetria fundamentada (art. 46): falta de motivação sustenta o recurso e a anulação judicial.
- Poder de polícia do Procon independe do número de reclamações (AgInt no AREsp 2.155.897): não fundar a defesa só em "reclamação única".
- Prescrição intercorrente da Lei 9.873/1999 não se aplica a processos estaduais ou municipais (EDcl no AgInt no AREsp 1.990.648): buscar prazo na lei local [VERIFICAR: norma local de prescrição].

## Fundamentos verificados
- CDC arts. 55, 56, 57 e 105.
- Decreto 2.181/1997 arts. 4º, 18, 25, 26, 26-A, 27, 28, 28-A, 33, 35, 38, 40, 42, 44, 45, 46, 49, 50, 54, 55.
- STJ: AgInt no AREsp 2.155.897; EDcl no AgInt no AREsp 1.990.648; AgInt no AgInt no AREsp 761.885 (critérios de multa em portaria do Procon não são lei federal para fins de recurso especial).
- Valores-limite da multa do art. 57: texto compilado indica alteração por medida provisória de 2026 [VERIFICAR: redação vigente e conversão].
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Recebimento da defesa como tempestiva.
- Nulidade do auto/ato ou do processo (vícios formais, competência, cerceamento).
- Arquivamento por inexistência da infração ou por baixa lesividade com solução do caso (art. 33, § 4º, e arts. 33-A e 33-B — conferir aplicabilidade local).
- Subsidiariamente: reclassificação da gravidade, aplicação das atenuantes do art. 25, afastamento de agravantes não comprovadas (rol taxativo, art. 26-A), vedação de dupla contagem (art. 28-A) e redução da multa pela proporcionalidade (art. 28; CDC art. 57).
- Produção de provas (documentos, testemunhas, diligências — art. 45).
- No recurso contra multa: efeito suspensivo (art. 49, § 1º).

## Checklist pré-protocolo
- [ ] Data de recebimento da notificação e prazo (20 ou 10 dias) conferidos, inclusive norma local
- [ ] Autoridade julgadora indicada corretamente (art. 44)
- [ ] Cada requisito do art. 35/40 conferido no auto/ato
- [ ] Prova de solução dada aos consumidores juntada
- [ ] Primariedade demonstrada (certidão) ou reincidência contestada (prazo de 5 anos — art. 27)
- [ ] Faturamento usado na dosimetria impugnado com documento
- [ ] Atenuantes do art. 25 pedidas uma a uma
- [ ] Procuração e atos constitutivos juntados

## Erros a evitar
- Defesa genérica que não ataca a dosimetria: a redução da multa costuma ser o resultado útil.
- Perder o prazo preclusivo (art. 54) contando como prazo judicial em dias úteis sem conferir a norma local.
- Recorrer sem pedir expressamente o efeito suspensivo da multa.
- Deixar de produzir prova na via administrativa e depois buscar revisão no STJ, onde fatos e dosimetria esbarram na Súmula 7 (AgInt no AREsp 2.155.897).
- Invocar prescrição intercorrente da Lei 9.873/1999 em processo estadual/municipal.

## Integração com o núcleo
`prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`; atualização da multa: `juros-e-correcao`.

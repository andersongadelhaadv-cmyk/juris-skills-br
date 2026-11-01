---
name: trib-mandado-de-seguranca
description: >
  Redige mandado de segurança tributário, repressivo ou preventivo, com base na
  Lei 12.016/2009 (prazo decadencial de 120 dias do art. 23), inclusive para
  declarar o direito à compensação (Súmula 213 STJ). Use quando o usuário pedir
  MS tributário, mandado de segurança contra cobrança, exclusão de tributo da
  base de cálculo, liminar para suspender exigibilidade, MS para compensar,
  writ contra delegado da Receita, secretário de Fazenda ou fiscal de tributos.
metadata:
  area: tributario-fazenda
  tipo_peca: mandado-seguranca
  verificado_em: 2026-11-01
---
# Mandado de segurança tributário

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: ato concreto (lançamento, indeferimento, negativa de certidão, exigência em fiscalização) ou ameaça concreta decorrente de norma de efeitos concretos que já incide sobre o impetrante (MS preventivo); declaração do direito de compensar; afastamento de exigência futura.
- Não usar: quando o caso depende de perícia ou prova a produzir (use `trib-acao-anulatoria` ou `trib-repeticao-de-indebito`); para cobrar valores pretéritos em dinheiro (Súmula 269 STF); contra lei em tese (Súmula 266 STF); para convalidar compensação já feita pelo contribuinte (Súmula 460 STJ).
- Créditos já em execução fiscal: avalie `trib-embargos-a-execucao-fiscal` ou `trib-excecao-pre-executividade-fiscal`.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
- Ato impugnado (cópia), data da ciência e quem o praticou ou de quem emana a ordem (art. 6º, §3º).
- Tributo, período, base legal da exigência e tese jurídica.
- Prova documental pré-constituída completa (guias, declarações, notificações, contrato social).
- Se há processo administrativo pendente com recurso de efeito suspensivo (art. 5º, I) ou ação judicial com o mesmo objeto.
- Se o pedido inclui compensação, quais tributos e períodos; se o indébito já foi habilitado ou compensado.
- Ente e órgão de representação judicial (PGFN, PGE, Procuradoria do Município).

## Prazo e contagem
- 120 dias da ciência do ato (art. 23), prazo decadencial, que não se suspende nem se interrompe. Constitucionalidade do prazo: Súmula 632 STF.
- MS preventivo não se sujeita a esse prazo enquanto o ato não se concretiza; nas relações de trato sucessivo, cada nova exigência renova a lesão. Documente a razão pela qual a impetração é tempestiva.
- Informações da autoridade: 10 dias (art. 7º, I). Use `prazos-processuais` para os prazos recursais.

## Estrutura da peça
Endereçamento (competência pela sede da autoridade e categoria funcional) → qualificação do impetrante → autoridade coatora e pessoa jurídica (art. 6º) → cabimento e tempestividade → fatos → direito líquido e certo → liminar (art. 7º, III) → pedidos → valor da causa → documentos. Roteiro em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Prova pré-constituída: sem ela, denegação sem mérito (art. 6º, §5º; art. 19).
- Autoridade correta: quem pratica ou ordena o ato; erro de indicação gera extinção ou emenda conforme o juízo.
- Liminar: fundamento relevante + risco de ineficácia (art. 7º, III); o juiz pode exigir caução. Agravo de instrumento da decisão (art. 7º, §1º).
- Compensação: o MS declara o direito (Súmula 213 STJ); a compensação só se faz após o trânsito em julgado (CTN art. 170-A). O art. 7º, §2º, que vedava liminar para compensação, foi declarado inconstitucional pelo STF na ADI 4.296 (acórdão de 09/06/2021, DOU de 28/06/2021), conforme a ficha da Lei 12.016 no Senado. Mesmo assim, a compensação depende do trânsito em julgado (CTN art. 170-A): não peça compensação imediata por liminar.
- Restituição em dinheiro de indébito reconhecido judicialmente: via precatório, não administrativa (Tema 1262 STF). O contribuinte pode optar entre precatório e compensação (Súmula 461 STJ).
- Sem honorários (art. 25; Súmula 512 STF; Súmula 105 STJ) e sem efeitos patrimoniais pretéritos (Súmula 271 STF).

## Fundamentos verificados
Lei 12.016/2009 arts. 1º, 5º, 6º, 7º, 10, 14, 19, 23 e 25; CTN arts. 151, IV, 170 e 170-A; Súmulas 213, 460 e 461 STJ; 266, 269, 271, 512 e 632 STF; Súmula 105 STJ; Tema 1262 STF. Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Liminar para suspender a exigibilidade (CTN art. 151, IV) e impedir atos de cobrança, inscrição em dívida ativa e negativa de certidão.
- Notificação da autoridade (art. 7º, I) e ciência ao órgão de representação (art. 7º, II); oitiva do MP.
- Concessão da segurança para reconhecer a inexigibilidade e, se for o caso, declarar o direito de compensar os valores recolhidos nos 5 anos anteriores à impetração e no curso do processo, após o trânsito em julgado (art. 170-A), com atualização pelo critério indicado em `juros-e-correcao`.
- Valor da causa: o benefício econômico estimado (não um valor simbólico).

## Checklist pré-protocolo
- [ ] Ciência do ato documentada e prazo de 120 dias conferido.
- [ ] Autoridade coatora e pessoa jurídica corretas; competência pela sede da autoridade.
- [ ] Toda a prova documental anexada; nada depende de perícia.
- [ ] Nenhum recurso administrativo com efeito suspensivo pendente sobre o mesmo ato (art. 5º, I).
- [ ] Pedido de compensação condicionado ao trânsito em julgado; nenhum pedido de cobrança pretérita.
- [ ] Tese confrontada com precedentes vinculantes atuais via `verificacao-de-citacoes`.
- [ ] Valor da causa compatível com o proveito econômico; custas recolhidas.

## Erros a evitar
- Usar MS como ação de cobrança ou para receber restituição em espécie de períodos anteriores.
- Pedir liminar para compensar créditos de imediato (CTN art. 170-A).
- Pedir que o juiz convalide compensação já feita (Súmula 460 STJ).
- Impetrar contra a norma abstrata, sem ato ou ameaça concreta ao impetrante.
- Indicar como coator o Ministro ou o Secretário quando o ato é do delegado ou do fiscal.
- Escrever taxa de juros ou índice próprio: remeta a `juros-e-correcao`.

## Integração com o núcleo
- `prazos-processuais`: prazo do art. 23 e prazos recursais.
- `juros-e-correcao`: atualização do indébito a compensar (sem taxa escrita na peça de área).
- `verificacao-de-citacoes`: todo precedente acrescentado.
- `fidelidade-factual`: data de ciência, valores e documentos.
- `estilo-forense`: revisão final.

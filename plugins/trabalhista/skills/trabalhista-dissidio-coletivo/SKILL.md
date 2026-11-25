---
name: trabalhista-dissidio-coletivo
description: >
  Redige representação de dissídio coletivo de natureza econômica, jurídica ou
  de greve (CLT arts. 856 a 875; CF art. 114, §§2º e 3º), com o pressuposto do
  comum acordo (Tema 841/STF), a manutenção da data-base (CLT art. 616, §3º),
  a assembleia autorizadora e a competência TRT x SDC/TST. Use quando o usuário
  pedir dissídio coletivo, ação de revisão de sentença normativa, dissídio de
  greve, defesa de sindicato patronal ou empresa em dissídio, ou estratégia após
  negociação coletiva frustrada.
metadata:
  area: trabalhista
  tipo_peca: inicial
  verificado_em: 2026-11-25
---
# Dissídio coletivo

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: (a) **econômico** — criar ou rever condições de trabalho após negociação frustrada; (b) **jurídico** — interpretar norma coletiva ou sentença normativa já existente; (c) **de greve** — declarar abusividade ou não da greve e fixar condições; (d) **revisão** de sentença normativa com mais de 1 ano de vigência (CLT arts. 873 e 874).
- Também: defesa do suscitado (falta de comum acordo, negociação não esgotada, assembleia irregular).
- Não usar: anular cláusula de CCT/ACT já firmada (`trabalhista-acao-anulatoria-clausula-coletiva`); cobrar cláusula de norma coletiva para trabalhadores (ação de cumprimento — use `trabalhista-reclamacao` adaptada); direito difuso ou coletivo fora da negociação (ação civil pública, fora desta skill); empregado público estatutário (`adm-*`).

## Entradas mínimas (perguntar o que faltar; nunca supor fatos)
1. Categorias e base territorial (define TRT ou TST).
2. Instrumento coletivo ou sentença normativa vigente e seu termo final.
3. Histórico da negociação: pautas, atas de reuniões, mediação, propostas e recusas.
4. Edital, ata e lista de presença da assembleia que autorizou o dissídio (quórum).
5. Há concordância expressa ou tácita do suscitado? Há greve em curso? Atividade essencial?
6. O suscitado é pessoa jurídica de direito público?

## Prazo e contagem
- Para o novo instrumento vigorar no dia seguinte ao termo do anterior, o dissídio deve ser instaurado nos 60 dias anteriores a esse termo (CLT art. 616, §3º) [VERIFICAR: uso e efeitos do protesto judicial para preservar a data-base, conforme regimento e jurisprudência da SDC].
- Vigência da sentença normativa: até 4 anos (CLT art. 868, parágrafo único). Revisão: após 1 ano (art. 873).
- Recurso ordinário contra decisão do TRT: 8 dias (CLT art. 895, II). Contagem: `prazos-processuais`.

## Estrutura da peça
Endereçamento → legitimidade e assembleia → esgotamento da negociação → pressuposto do comum acordo (ou sua dispensa) → natureza do dissídio → cláusulas propostas, uma a uma, com justificativa → bases da conciliação → pedidos. Roteiro em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Legitimidade:** empregadores ou seus sindicatos e sindicatos de empregados (CLT art. 857); na falta de sindicato, federação e, depois, confederação (parágrafo único). Instauração também pelo presidente do tribunal ou pelo MPT quando houver suspensão do trabalho (art. 856) e pelo MPT em greve em atividade essencial (CF art. 114, §3º).
- **Assembleia:** a representação sindical depende de aprovação em assembleia com o quórum do art. 859 da CLT [VERIFICAR: aplicação atual do quórum na jurisprudência da SDC].
- **Negociação prévia:** dissídio econômico só depois de esgotadas as tentativas de celebrar CCT ou ACT (CLT art. 616, §4º; CF art. 114, §2º).
- **Comum acordo:** exigência constitucional para o dissídio econômico, declarada constitucional pelo STF (Tema 841). Em caso de greve, a SDC tem admitido o ajuizamento por qualquer das partes sem comum acordo (ROT 250-68.2022.5.17.0000).
- **Ente público empregador:** só cláusulas de natureza social (OJ 5 da SDC).
- **Requisitos formais da representação:** qualificação das partes, natureza do estabelecimento, motivos do dissídio e bases da conciliação (CLT art. 858).
- **Competência:** TRT da base territorial; SDC do TST se o conflito exceder a jurisdição de um TRT (Lei 7.701/1988, art. 2º).

## Fundamentos verificados
- CF art. 114, §§2º e 3º; CLT arts. 616 §§3º e 4º, 856 a 860, 864, 868, 873, 874, 895 II; Lei 7.701/1988, art. 2º.
- STF Tema 841 (RE 1.002.295): comum acordo constitucional.
- OJ 5 da SDC/TST; SDC, ROT 250-68.2022.5.17.0000 (greve dispensa o comum acordo).
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Designação de audiência de conciliação (CLT art. 860).
- Fixação das cláusulas propostas, uma a uma, respeitadas as disposições mínimas legais e as convencionadas anteriormente (CF art. 114, §2º).
- Data de início e prazo de vigência (art. 868, parágrafo único).
- No dissídio de greve: declaração de abusividade ou não, e efeitos sobre os dias parados [VERIFICAR jurisprudência da SDC antes de afirmar a regra de desconto].
- Extensão a outros empregados, se for o caso (art. 868).
- Reajustes: índice e cálculo pelo núcleo `juros-e-correcao`, sem taxa própria nesta skill.

## Checklist pré-protocolo
- [ ] Base territorial e tribunal competente definidos
- [ ] Atas de negociação e prova da recusa juntadas
- [ ] Edital, ata e quórum da assembleia conferidos
- [ ] Comum acordo provado (expresso/tácito) ou hipótese de dispensa (greve) fundamentada
- [ ] Prazo de 60 dias antes do termo final verificado
- [ ] Cláusulas numeradas, com justificativa e fonte de dados
- [ ] Ente público? Só cláusulas sociais

## Erros a evitar
- Ajuizar dissídio econômico sem prova de negociação nem de comum acordo.
- Perder a data-base por protocolar fora dos 60 dias.
- Juntar ata de assembleia sem lista de presença e sem a pauta específica.
- Pedir cláusula econômica contra ente público (OJ 5 da SDC).
- Confundir dissídio jurídico (interpretação) com ação anulatória (validade).

## Integração com o núcleo
`prazos-processuais`, `juros-e-correcao`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

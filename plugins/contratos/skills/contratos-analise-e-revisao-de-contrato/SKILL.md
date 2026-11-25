---
name: contratos-analise-e-revisao-de-contrato
description: >
  Revisa e audita contrato recebido da outra parte: lê cláusula a cláusula,
  monta mapa de riscos (alto, médio, baixo), aponta cláusulas leoninas ou
  inválidas, propõe redação alternativa em marcas de revisão e entrega
  relatório ao cliente em linguagem de negócio, com base nos arts. 113, 421 a
  480 do Código Civil e na Lei 13.874/2019. Use quando o usuário pedir para
  revisar, analisar, auditar, "dar uma olhada" ou comentar uma minuta antes de
  assinar, ou quiser saber quais cláusulas negociar.
metadata:
  area: contratos
  tipo_peca: parecer
  verificado_em: 2026-11-25
---
# Análise e revisão de contrato

Ferramenta de apoio; o advogado responsável revisa todo documento antes de assinar ou enviar.

## Quando usar / quando não usar
- Usar: minuta recebida antes da assinatura; contraproposta; due diligence de contratos de uma empresa; checagem de aditivo.
- Não usar: redigir do zero (`contratos-elaboracao-de-contrato` e skills por tipo); opinião formal sobre validade ou execução de contrato já firmado e em conflito (`contratos-parecer-sobre-contrato`).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. A minuta completa, com todos os anexos citados no corpo. Anexo faltante = ponto cego; registrar no relatório.
2. Qual lado o cliente ocupa e qual o objetivo comercial (fechar rápido, reduzir risco, ganhar exclusividade...).
3. Poder de barganha: minuta de adesão imposta ou negociação entre iguais? (muda a régua: arts. 421-A, 423 e 424 do CC; CDC se houver consumidor).
4. Valor e duração estimados do negócio (para dimensionar multas e tetos).
5. Pontos que o cliente já sabe que não aceita ou que já foram negociados.
6. Prazo para devolver a revisão.

## Prazos relevantes
- Anulação por erro, dolo, coação, lesão: 4 anos, decadencial (art. 178), se o cliente já assinou e quer desfazer.
- Prescrição do inadimplemento contratual: 10 anos (art. 205), conforme a 2ª Seção do STJ; dívida líquida em instrumento: 5 anos (art. 206, § 5º, I).
- Vícios redibitórios: 30 dias (móvel) ou 1 ano (imóvel), art. 445.
- Prazos processuais: `prazos-processuais`.

## Método (passo a passo)
1. **Leitura de mapa:** partes, objeto, preço, prazo, saída. Se algo essencial falta, pare e liste.
2. **Leitura de risco:** cláusula a cláusula, classificar em vermelho (inválida ou inaceitável), amarelo (negociável, desequilibrada) e verde (aceitável).
3. **Teste de coerência:** definições x uso; corpo x anexos; multa x limitação de responsabilidade; prazo x aviso prévio.
4. **Proposta de redação:** para cada vermelho e amarelo, texto alternativo pronto para colar (marca de revisão ou tabela "de/para").
5. **Relatório ao cliente:** resumo executivo (até 10 linhas), top 5 riscos, o que negociar, o que aceitar.
Detalhe em [estrutura](references/estrutura.md).

## Riscos e cláusulas sensíveis (checar sempre)
- **Objeto e escopo:** indeterminado ou alterável unilateralmente (art. 104, II; art. 122 — condição puramente potestativa).
- **Preço:** reajuste por índice escolhido depois, ou por "tabela vigente" de uma parte só.
- **Responsabilidade:** exoneração total, inclusive por dolo; teto irrisório; exclusão de lucros cessantes só para um lado.
- **Caso fortuito e força maior:** cláusula que transfere todo risco ao cliente (art. 393 permite assumir, mas deve ser consciente).
- **Cláusula penal:** acima da obrigação principal (art. 412) ou desproporcional; lembrar que o juiz deve reduzi-la (art. 413 — AREsp 2.978.644), mas em contrato paritário a cláusula penal tende a receber interpretação restrita (REsp 2.013.493).
- **Rescisão assimétrica:** só uma parte pode resilir; aviso prévio incompatível com o investimento exigido (art. 473, parágrafo único).
- **Renúncia antecipada** a direito resultante da natureza do negócio, em adesão (art. 424).
- **Exclusividade e não concorrência:** sem limite de tempo, território e objeto; a jurisprudência do STJ valida a cláusula quando há esses limites (AREsp 3.082.023).
- **Foro e arbitragem:** foro sem pertinência (CPC, art. 63, § 1º); arbitragem em adesão sem destaque (Lei 9.307/1996, art. 4º, § 2º).
- **LGPD:** cliente tratado como controlador sem controle real; ausência de cláusula de incidente; suboperadores livres.
- **Cessão e mudança de controle:** a outra parte pode ceder o contrato sem anuência.
- **Renovação automática** com janela curta de denúncia.

## Fundamentos verificados
- CC: arts. 104, 113, 122, 178, 205, 206, 393, 412, 413, 421, 421-A, 422, 423, 424, 445, 473, 474, 476, 478.
- Lei 13.874/2019, art. 7º; LGPD arts. 5º, 39; CPC art. 63; Lei 9.307/1996 art. 4º; CDC arts. 2º e 51, I.
- STJ: AREsp 2.978.644 (art. 413, ordem pública); REsp 2.013.493 (cláusula penal em contrato paritário: interpretação restrita); AREsp 3.082.023 (não concorrência com limites); REsp 1.799.039 (paridade e intervenção mínima); AgInt nos EREsp 1.685.808 (prescrição decenal).
Detalhe em [fundamentos](references/fundamentos.md).

## Checklist antes de enviar a revisão
- [ ] Todos os anexos recebidos e lidos (ou ausência registrada)
- [ ] Cada cláusula classificada (vermelho / amarelo / verde)
- [ ] Toda crítica acompanhada de redação alternativa
- [ ] Coerência multa x teto de responsabilidade x seguro
- [ ] Riscos expressos em linguagem de negócio (o que pode custar e quando)
- [ ] Nenhuma afirmação sobre fato do negócio sem confirmação do cliente
- [ ] Citações conferidas (`verificacao-de-citacoes`); juros e índices pelo núcleo
- [ ] Versão com marcas de revisão + versão limpa

## Erros a evitar
- Reescrever o contrato inteiro: revise o que importa e preserve a negociação.
- Marcar como "ilegal" o que é apenas desfavorável: em contrato paritário a alocação de riscos pactuada é respeitada (art. 421-A).
- Ignorar anexos (SLA, tabela de preços, política de dados), onde costuma estar o risco real.
- Entregar ao cliente lista técnica sem priorização nem recomendação.
- Confiar que o juiz vai reduzir a multa: negociar agora é mais barato.

## Integração com o núcleo
`juros-e-correcao` (encargos e reajuste), `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

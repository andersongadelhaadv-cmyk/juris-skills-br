---
name: trib-compliance-tributario
description: >
  Estrutura programa de compliance tributário e redige relatório de revisão
  de rotinas fiscais (obrigações principais e acessórias, guarda de
  documentos, responsabilidade de administradores, autorregularização por
  denúncia espontânea), com base no CTN, arts. 100, 113-A, 135, 138, 173, 174
  e 195, e nas Súmulas 360, 430, 435 e 436 do STJ. Use quando o usuário pedir
  programa de compliance tributário, revisão de rotinas fiscais, diagnóstico
  de conformidade tributária, matriz de riscos fiscais, política interna de
  tributos ou plano de autorregularização antes de fiscalização.
metadata:
  area: tributario-fazenda
  tipo_peca: parecer
  verificado_em: 2026-11-25
---
# Compliance tributário — programa e revisão de rotinas

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo e todo relatório antes da entrega ao cliente.

Produz dois entregáveis: (1) o **programa** (governança, política, matriz de riscos, rotinas, controles, treinamento, monitoramento) e (2) o **relatório de revisão** de rotinas já existentes, com achados, risco e plano de ação. Não calcula tributo nem fixa alíquota: aponta onde o cálculo do cliente precisa ser conferido.

## Quando usar / quando não usar
- Usar: (a) empresa sem processo tributário formal; (b) revisão periódica de rotinas (apuração, declarações, retenções, documentos fiscais, cadastros); (c) preparação para auditoria, investimento ou venda; (d) plano de autorregularização antes de fiscalização; (e) definir quem responde pelo quê entre diretoria, contabilidade e jurídico.
- Não usar:
  - Programa de integridade anticorrupção ou compliance regulatório setorial: `reg-programa-integridade-compliance`.
  - Desenho de nova estrutura para reduzir carga: `trib-planejamento-tributario`.
  - Dúvida pontual de interpretação: `trib-parecer-tributario`.
  - Fiscalização já iniciada ou auto lavrado: `trib-defesa-administrativa-e-carf`.
  - Due diligence de aquisição: `soc-due-diligence-societaria` (o capítulo fiscal pode usar esta skill).
  - Adequação à reforma do consumo: `trib-reforma-tributaria-ibs-cbs`.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Atividades, CNAEs, estabelecimentos e entes tributantes envolvidos.
2. Regime de apuração de cada tributo e quem apura (interno, escritório contábil, sistema).
3. Lista de obrigações acessórias entregues e calendário real (não o teórico).
4. Organograma: quem decide, quem assina, quem revisa.
5. Histórico: autuações, parcelamentos, transações, certidões, ações judiciais e decisões que o cliente aplica.
6. Normas e soluções de consulta que o cliente segue como orientação.
7. Amostra documental para teste (notas, apurações, declarações de períodos escolhidos).

## Prazo e contagem
- Janela de revisão: períodos ainda não alcançados pela decadência (CTN, arts. 150, § 4º, e 173, I) e créditos não prescritos (art. 174). Guarda de livros e comprovantes até a prescrição (art. 195, parágrafo único).
- Autorregularização só exclui a responsabilidade antes de qualquer procedimento administrativo ou medida de fiscalização relacionada à infração (art. 138, parágrafo único). Registrar a data de cada termo de início recebido.
- Prazos processuais e de impugnação: `prazos-processuais`.

## Estrutura do entregável
Programa: governança → política → matriz de riscos → rotinas e controles → evidências → treinamento → monitoramento. Relatório: escopo e amostra → achados por rotina → risco → causa → plano de ação com dono e data. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Escopo por escrito: tributos, entes, períodos, amostra. Fora do escopo vai declarado.
- Achado só com evidência (documento, período, valor informado pelo cliente).
- Separar erro de interpretação (risco de lançamento) de erro operacional (atraso, omissão) e de indício de fraude (escalar ao advogado; risco penal — Lei 8.137/1990).
- Responsabilidade pessoal de administrador exige ato com excesso de poderes ou infração de lei, contrato ou estatuto (CTN, art. 135, III); o simples inadimplemento não basta (Súmula 430/STJ); a dissolução irregular presumida legitima redirecionamento (Súmula 435/STJ). O programa deve impedir encerramento de fato sem baixa.
- Declaração entregue constitui o crédito (Súmula 436/STJ): declarar e não pagar não é denúncia espontânea (Súmula 360/STJ).

## Fundamentos verificados
- CTN, art. 100 e parágrafo único: observar atos normativos, decisões administrativas com eficácia normativa e práticas reiteradas da administração exclui penalidades, juros de mora e atualização da base de cálculo. *Uso:* documentar a norma seguida em cada rotina.
- CTN, art. 107, §§ 1º a 3º (LC 236/2026): consulta e pareceres jurídicos; vinculação limitada ao órgão; solução vale para o consulente.
- CTN, art. 113-A (LC 236/2026): penalidades proporcionais, com tetos graduados — percentual só da norma conferida no dia.
- CTN, art. 138 (redação da LC 236/2026): denúncia espontânea com pagamento do tributo e juros (ou depósito), excluindo inclusive a multa de mora.
- CTN, art. 135, III; arts. 173, I, 174 e 195, parágrafo único.
- CTN, art. 194-A (LC 236/2026): precedente vinculante do STF/STJ vincula a administração — o programa monitora esses precedentes.
- Súmulas 360, 430, 435 e 436 do STJ.
Detalhe em [fundamentos](references/fundamentos.md).

## Conteúdo essencial do programa
- Política tributária aprovada pela administração (apetite a risco, alçadas, quando consultar o jurídico, quando formular consulta formal).
- Matriz de riscos por tributo e rotina, com probabilidade, impacto e controle.
- Calendário de obrigações com responsável, revisor e evidência de entrega.
- Registro de normas, soluções de consulta e decisões judiciais aplicadas (com data e abrangência).
- Rotina de monitoramento normativo e de precedentes vinculantes.
- Procedimento de autorregularização: quem decide, como calcula (núcleo `juros-e-correcao`), como paga antes de qualquer termo de início.
- Gestão de certidões e cadastros (CNPJ, inscrições, domicílio tributário eletrônico).
- Canal interno para dúvidas e para reportar irregularidade.
- Treinamento e revisão anual do programa.

## Checklist pré-entrega
- [ ] Escopo, períodos e amostra declarados
- [ ] Cada achado com evidência, risco, causa e dono
- [ ] Achados com indício de fraude separados e escalados
- [ ] Decadência e prescrição dos períodos revisados indicadas
- [ ] Autorregularização avaliada antes de qualquer termo de início
- [ ] Nenhum percentual, alíquota ou valor de memória
- [ ] Juros e correção remetidos ao núcleo
- [ ] Nenhum `[VERIFICAR]` pendente no texto final

## Erros a evitar
- Tratar parcelamento como denúncia espontânea; avaliar caso a caso a norma do parcelamento [VERIFICAR a lei do programa específico].
- Prometer exclusão de multa a tributo declarado e pago com atraso (Súmula 360/STJ).
- Programa "de papel": política sem calendário, responsável e evidência.
- Ignorar a responsabilidade pessoal do administrador ao desenhar encerramento de filial ou da empresa.
- Confundir compliance tributário com integridade anticorrupção (outra lei, outro entregável).

## Integração com o núcleo
`juros-e-correcao`, `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

---
name: soc-due-diligence-societaria
description: >
  Conduz e redige relatório de due diligence jurídica (auditoria legal) de
  sociedade-alvo em aquisição, investimento ou reorganização: lista de
  documentos, checagem societária (atos, quóruns, poderes, ônus sobre
  quotas), contingências cíveis, fiscais e trabalhistas, e tradução de cada
  achado em preço, garantia ou condição, com base nos arts. 1.003, 1.057 e
  1.146 do Código Civil, 132 e 133 do CTN e 10-A da CLT. Use quando o usuário
  pedir due diligence, auditoria jurídica de empresa, checklist de documentos
  para compra de empresa, relatório de red flags ou análise de passivo antes
  de investir.
metadata:
  area: societario
  tipo_peca: parecer
  verificado_em: 2026-11-25
---
# Due diligence jurídica societária

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: auditoria prévia à compra de quotas/ações, à entrada de investidor, à incorporação/fusão ou a uma reorganização societária; também "vendor due diligence" (auditoria preparada pelo vendedor).
- Não usar: auditoria de imóvel isolado (`imob-analise-de-matricula-e-due-diligence`); adequação à LGPD como produto principal (skill `lgpd-saas-adequacao`, se disponível, ou plugin `digital`); redação do contrato da operação (`soc-ma-compra-de-quotas-e-acoes`); opinião sobre uma questão societária pontual (`soc-parecer-societario`).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Tipo de operação (compra de participação, compra de ativos, incorporação, investimento minoritário) e lado do cliente.
2. Sociedade-alvo e controladas: CNPJ, tipo, sede, atividade; se há grupo.
3. Escopo combinado: áreas (societária, contratos, cível, fiscal, trabalhista/previdenciária, ambiental, regulatória, imobiliária, PI, dados pessoais), período de retroação, valor de materialidade.
4. Acesso ao data room: lista do que foi entregue e do que falta; entrevistas com gestores.
5. Prazo do cliente e formato de relatório (red flag ou completo).
6. Restrições de confidencialidade (NDA assinado: `contratos-nda-confidencialidade`).

## Prazo e contagem
- Janela de retroação: defina por matéria e pelo prazo de prescrição/decadência aplicável — confira cada prazo antes de afirmá-lo no relatório (`verificacao-de-citacoes`).
- Responsabilidade de ex-sócio cedente: até 2 anos da averbação (art. 1.003, parágrafo único, e art. 1.032 do CC); ex-sócio na Justiça do Trabalho: ações ajuizadas até 2 anos após averbada a alteração (art. 10-A da CLT).
- Trespasse: alienante solidário por 1 ano (art. 1.146 do CC).
- Certidões têm validade curta: registre a data de emissão e renove antes do fechamento. Prazos processuais: `prazos-processuais`.

## Estrutura da peça
Sumário executivo (red flags com recomendação) → escopo, premissas e limitações → metodologia e documentos analisados → achados por área (fato, risco, base legal, estimativa, recomendação) → matriz de riscos → providências pré e pós-fechamento → anexos (lista de documentos, certidões). Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Escopo e materialidade por escrito antes de começar; o relatório só fala do que foi visto.
- Cada achado classificado: alto (impede ou reprecifica), médio (garantia ou indenização específica), baixo (providência pós-fechamento).
- Separe passivo **da sociedade** (que o comprador herda indiretamente ao comprar quotas) do passivo **pessoal** dos vendedores.
- Na compra de ativos/estabelecimento, verifique sucessão: tributária (art. 133 do CTN), dívidas contabilizadas (art. 1.146 do CC). Em fusão/incorporação: art. 132 do CTN e arts. 232 e 233 da LSA.
- Mudança na estrutura jurídica não afeta direitos adquiridos dos empregados (art. 10 da CLT).

## Fundamentos verificados
- CC arts. 1.003, 1.032, 1.057 (cessão de quotas e responsabilidade de ex-sócio), 1.146 (trespasse).
- CTN arts. 132 e 133 (sucessão tributária).
- CLT arts. 10 e 10-A (sucessão e ex-sócio).
- Lei 6.404/1976, arts. 232 e 233 (credores em incorporação, fusão e cisão).
- STJ, AgInt nos EDcl no REsp 1.759.517 (limite da responsabilidade do cedente).
Detalhe em [fundamentos](references/fundamentos.md).

## Checklist de documentos (núcleo societário)
- [ ] Ato constitutivo e todas as alterações, com certidão simplificada e de inteiro teor da Junta
- [ ] Acordos de sócios/acionistas, opções, contratos de mútuo conversível ou de investimento
- [ ] Livros e atas (S.A.: registro de ações, atas de assembleia e de conselho)
- [ ] Procurações vigentes e poderes de administradores
- [ ] Ônus sobre quotas/ações (penhor, penhora, usufruto, alienação fiduciária)
- [ ] Participações em outras sociedades, consórcios e SCPs
- [ ] Certidões: distribuidores cíveis, fiscais e trabalhistas (sociedade e sócios relevantes), CND federal, estadual, municipal, FGTS, CNDT, protestos
- [ ] Contratos relevantes com cláusula de mudança de controle ou exclusividade
- [ ] Licenças e alvarás; passivo ambiental
- [ ] Contencioso: relatório dos patronos com valor e prognóstico
- [ ] Marcas, domínios, software (titularidade)
- [ ] Tratamento de dados pessoais (políticas, incidentes)

## Erros a evitar
- Relatório que só descreve documentos: todo achado precisa de recomendação (preço, garantia, indenização específica, condição precedente ou providência).
- Afirmar "inexistência de passivo" com base em certidão: certidão negativa prova o que consta do distribuidor, não a ausência de risco.
- Ignorar o grupo econômico e as controladas.
- Prazo prescricional citado de memória (use `verificacao-de-citacoes`).
- Calcular atualização de contingências com índice próprio (use `juros-e-correcao`).
- Expor dados pessoais de empregados e clientes no relatório além do necessário.

## Integração com o núcleo
`soc-ma-compra-de-quotas-e-acoes` (a operação), `soc-parecer-societario`, `juros-e-correcao`, `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

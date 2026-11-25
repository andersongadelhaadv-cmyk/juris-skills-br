---
name: imob-analise-de-matricula-e-due-diligence
description: >
  Analisa a matrícula do imóvel ato por ato e conduz a due diligence imobiliária
  (vendedor, imóvel e riscos de fraude), com base na Lei 6.015/1973 (matrícula,
  registro, averbação, continuidade) e na concentração dos atos na matrícula da
  Lei 13.097/2015 (arts. 54 a 58), entregando relatório de riscos e lista de
  certidões. Use quando o usuário pedir para ler ou interpretar uma matrícula,
  checar se o imóvel está livre e desembaraçado, montar checklist de certidões
  antes de comprar, avaliar risco de fraude à execução, penhora, indisponibilidade
  ou alienação fiduciária, ou preparar relatório de due diligence para cliente.
metadata:
  area: imobiliario
  tipo_peca: outro
  verificado_em: 2026-11-25
---
# Análise de matrícula e due diligence imobiliária

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: (a) leitura da matrícula e da cadeia dominial; (b) checklist de certidões do vendedor e do imóvel; (c) relatório de riscos antes de promessa, escritura, garantia ou arrematação; (d) defesa de adquirente com base na boa-fé registral.
- Não usar: redação do contrato (`imob-compra-e-venda-de-imovel`); opinião conclusiva sobre a viabilidade do negócio (`imob-parecer-juridico-imobiliario`, que consome este relatório); embargos de terceiro já com penhora (`imob-embargos-de-terceiro`, com este relatório como prova da boa-fé); divergência de área (`imob-retificacao-de-area`); imóvel em inventário (`sucessoes-inventario-judicial`); desapropriação (`adm-desapropriacao-defesa`).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Certidão de inteiro teor da matrícula, recente (data de emissão).
2. Finalidade: compra à vista, financiada, garantia, permuta, incorporação, arrematação.
3. Vendedor: pessoa física (estado civil, regime, cônjuge) ou jurídica (atos societários, situação fiscal, recuperação judicial).
4. Matrículas e transcrições anteriores, se a matrícula for recente ou fruto de abertura/unificação.
5. Situação física e de posse (ocupante, vistoria), inscrição municipal e débitos de IPTU e condomínio.
6. Se rural: CCIR, ITR, CAR e georreferenciamento [VERIFICAR: regras específicas não cobertas nesta skill].
7. Apetite de risco do cliente (até onde estender a pesquisa além do mínimo legal).

## Prazo e contagem
- Sem prazo processual. Fixe no relatório a **data de corte** (emissão de cada certidão) e recomende revalidar perto da assinatura.
- Prenotação: o registro produz efeitos desde a apresentação do título (CC, art. 1.246) — orientar a apresentação imediata do título após a escritura.
- Prazos de eventual ação: `prazos-processuais`.

## Método (ordem de leitura da matrícula)
1. Cabeçalho: número, cartório, descrição do imóvel e proprietário (Lei 6.015/1973, art. 176, § 1º).
2. Atos em ordem: cada registro (R) e averbação (Av) — o que constitui, transfere, onera ou cancela (arts. 167 e 172).
3. Continuidade: o outorgante atual é o titular do último registro? (arts. 195 e 237).
4. Ônus vigentes: hipoteca, alienação fiduciária, penhora, arresto, indisponibilidade, usufruto, servidão, cláusulas de inalienabilidade, citação de ações, averbação premonitória.
5. Cancelamentos: conferir que cada ônus baixado tem averbação de cancelamento própria.
6. Descrição: divergência entre matrícula, IPTU e realidade → retificação (art. 213) antes do negócio.
Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Mínimo legal para a escritura: ITBI, certidões fiscais e de propriedade e ônus reais (Lei 7.433/1985, art. 1º, § 2º).
- Concentração na matrícula: o negócio é eficaz contra atos anteriores que não estejam inscritos na matrícula (citação de ação real ou reipersecutória, averbação de execução admitida, restrições e indisponibilidades, ações que levem à insolvência, constrições) — Lei 13.097/2015, art. 54, I a V; situações não inscritas não são oponíveis ao terceiro de boa-fé (§ 1º), com ressalvas legais.
- Ressalvas do § 1º: arts. 129 e 130 da Lei 11.101/2005 (falência) e aquisições/extinções de propriedade que independem de registro (ex.: usucapião). Não vender ao cliente "risco zero".
- A lei dispensa certidões forenses para validade, eficácia e boa-fé (art. 54, § 2º), mas não impede que o advogado as recomende para medir risco.
- Não se aplica a imóveis públicos (art. 58).

## Fundamentos verificados
- Lei 6.015/1973, arts. 167, 169, 172, 176, 195, 196, 213, 237.
- Lei 13.097/2015, arts. 54 (redação das Leis 14.382/2022 e 14.825/2024), 55, 56 e 58.
- Lei 7.433/1985, art. 1º, § 2º; CC, arts. 1.227, 1.245, 1.246, 1.247.
- Súmula 375/STJ e REsp 1.959.861 (sem penhora registrada, cabe ao credor provar a má-fé do adquirente); AgInt no REsp 1.810.306 (averbação premonitória gera presunção absoluta de fraude); Súmula 308/STJ (hipoteca da construtora × adquirente).
Detalhe em [fundamentos](references/fundamentos.md).

## Entrega (relatório de due diligence)
- Identificação do imóvel e do titular; data de corte de cada certidão.
- Quadro de atos da matrícula (R/Av, data, conteúdo, situação: vigente ou cancelado).
- Quadro de riscos: alto, médio, baixo — com fundamento e providência (baixa, quitação, anuência, retificação, cláusula contratual, retenção de parte do preço).
- Certidões obtidas, certidões recomendadas e certidões dispensadas pelo cliente (registrar a escolha).
- Condições para assinatura (o que precisa estar resolvido antes).

## Checklist pré-entrega
- [ ] Matrícula de inteiro teor recente
- [ ] Cada ato lido e classificado (vigente / cancelado)
- [ ] Continuidade conferida até o vendedor
- [ ] Ônus do art. 54 da Lei 13.097/2015 pesquisados na matrícula
- [ ] Certidões da Lei 7.433/1985 e pesquisa complementar decidida com o cliente
- [ ] Vendedor PJ: falência/recuperação (ressalva do § 1º)
- [ ] Descrição física conferida com a matrícula
- [ ] Débitos propter rem (IPTU, condomínio) levantados
- [ ] Riscos e providências redigidos em linguagem que o cliente entenda

## Erros a evitar
- Ler só o último ato e ignorar ônus não cancelados mais antigos.
- Tratar a Lei 13.097/2015 como blindagem total (há ressalvas legais e aquisições fora do registro).
- Ignorar o regime de bens e a outorga conjugal do vendedor.
- Aceitar descrição divergente "porque sempre foi assim".
- Não datar as certidões: relatório sem data de corte não prova nada.

## Integração com o núcleo
`prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

---
name: contratos-licenca-de-software-e-saas
description: >
  Redige e revisa contrato de licença de uso de software (on-premise) e contrato
  de software como serviço (SaaS), com base na Lei 9.609/1998, no Código Civil e
  na LGPD (Lei 13.709/2018) para o tratamento de dados, com SLA remetido a
  contratos-sla-nivel-de-servico. Use quando o usuário pedir contrato de
  licença de programa, termos de uso ou contrato de assinatura de plataforma,
  acordo de tratamento de dados (DPA) entre cliente e fornecedor, cláusula de
  limitação de responsabilidade, escrow de código-fonte ou desenvolvimento sob
  encomenda com titularidade do código.
metadata:
  area: contratos
  tipo_peca: contrato
  verificado_em: 2026-11-25
---
# Licença de software e SaaS

Ferramenta de apoio; o advogado responsável revisa todo documento antes de assinar ou enviar.

## Quando usar / quando não usar
- Usar: licença de uso (instalação no cliente); SaaS por assinatura; contrato B2B com DPA; desenvolvimento sob encomenda com cessão ou licença do código; revisão de minuta de fornecedor estrangeiro.
- Não usar: transferência de tecnologia com entrega de fontes para exploração (exige registro no INPI — art. 11 da Lei 9.609/1998; trate como contrato próprio); compra e venda de hardware; contrato de trabalho do desenvolvedor.
- Níveis de serviço, créditos e janelas de manutenção: `contratos-sla-nivel-de-servico`.
- Sigilo das partes: `contratos-nda-confidencialidade`.

## Entradas mínimas (perguntar o que faltar; nunca supor fatos)
1. Modelo: licença on-premise, SaaS, híbrido ou desenvolvimento sob encomenda.
2. Lado do cliente: fornecedor ou contratante; contratante é empresa ou consumidor pessoa física.
3. Titularidade do software e de componentes de terceiros (inclusive licenças de código aberto).
4. Métrica de cobrança (usuário, volume, módulo), reajuste, inadimplência e suspensão.
5. Dados pessoais tratados, categorias sensíveis, local de hospedagem e subcontratados (inclusive no exterior).
6. Disponibilidade e suporte esperados (para o anexo de SLA).
7. Valor do contrato e exposição tolerada (para calibrar o teto de responsabilidade).
8. Plano de saída: exportação de dados, prazo e formato.

## Prazos relevantes
- Validade técnica da versão comercializada deve constar do contrato e do documento fiscal (art. 7º); assistência técnica durante esse prazo (art. 8º).
- Contratação por consumidor fora do estabelecimento (on-line): arrependimento em 7 dias (CDC, art. 49).
- Incidente de segurança: comunicação à ANPD e aos titulares quando houver risco ou dano relevante (LGPD, art. 48); o prazo vem de regulamento da ANPD [VERIFICAR: prazo regulamentar vigente].
- Renovação automática e aviso de não renovação: defina dias corridos ou úteis por escrito (`prazos-processuais` só para prazos judiciais).

## Estrutura do documento
Definições → objeto (licença ou serviço) → escopo e restrições de uso → implantação → preço e reajuste → suporte e SLA (anexo) → propriedade intelectual → dados pessoais (DPA) → segurança → confidencialidade → garantias → limitação de responsabilidade → vigência, suspensão e rescisão → saída e portabilidade → lei e foro. Roteiro em [estrutura](references/estrutura.md).

## Riscos e cláusulas sensíveis
- **Natureza do direito.** Software é protegido pelo regime de direito autoral (art. 2º); o uso no país se dá por contrato de licença (art. 9º). Escreva "licença não exclusiva, intransferível, limitada ao prazo e ao escopo", não "venda".
- **Titularidade no desenvolvimento.** Programa feito por empregado ou contratado para esse fim pertence, em regra, ao contratante (art. 4º). Para prestador PJ, não confie na regra: escreva a cessão ou a licença expressamente, inclusive de bibliotecas reutilizáveis do fornecedor.
- **Cláusulas nulas em licença de programa estrangeiro.** São nulas as que limitem indevidamente a comercialização ou isentem as partes de responsabilidade por vícios, por ações de terceiros ou por violação de direitos de autor (art. 10).
- **Limitação de responsabilidade.** Em B2B paritário, teto e exclusão de lucros cessantes são negociáveis (CC, arts. 421 e 421-A). Com consumidor, cláusula que exonere ou atenue a responsabilidade por vício é nula; para consumidor pessoa jurídica, só limitação em situação justificável (CDC, art. 51, I). Ressalve dolo, culpa grave, violação de dados e de propriedade intelectual.
- **LGPD — papéis.** Em regra, o cliente é controlador e o fornecedor SaaS é operador (art. 5º, VI e VII), que segue as instruções do controlador (art. 39). O operador responde solidariamente quando descumpre a lei ou as instruções lícitas (art. 42, § 1º, I). Defina instruções, subcontratação, segurança (art. 46), registro das operações (art. 37), apoio em incidentes (art. 48) e transferência internacional (art. 33).
- **Suspensão por inadimplência.** Preveja aviso prévio e preservação dos dados por prazo definido; suspensão abrupta de sistema crítico gera disputa.
- **Arbitragem em termos de adesão.** Só eficaz com o destaque do art. 4º, § 2º, da Lei 9.307/1996.
- **Tributação** do licenciamento e do SaaS (ISS, ICMS, IRRF e remessas): fora do escopo desta skill [VERIFICAR com a área tributária antes de fixar o preço "com ou sem impostos"].

## Fundamentos verificados
- Lei 9.609/1998: arts. 2º, 3º, 4º, 6º, 7º, 8º, 9º, 10, 11 e 12.
- LGPD: arts. 5º (VI e VII), 7º, 33, 37, 39, 42, 46 e 48.
- CC: arts. 412, 413, 416, 421, 421-A, 422, 423 e 424. CDC: arts. 2º, 49 e 51, I. Lei 9.307/1996, art. 4º, § 2º. Lei 13.874/2019, art. 3º, VIII.
- Nenhum precedente específico sobre licença de software foi encontrado no JuriBase em 2026-11-25.
Detalhe em [fundamentos](references/fundamentos.md).

## Checklist antes de assinar/enviar
- [ ] Modelo correto (licença x serviço x encomenda) e titularidade do código expressa
- [ ] Componentes de terceiros e código aberto listados, com licenças compatíveis
- [ ] Prazo de validade técnica informado (licença comercializada)
- [ ] Papéis LGPD definidos e DPA anexo com segurança, subcontratados e incidentes
- [ ] Transferência internacional com base do art. 33
- [ ] Teto de responsabilidade coerente com o tipo de cliente (B2B x consumidor)
- [ ] Anexo de SLA presente ou remetido a documento próprio
- [ ] Plano de saída com prazo e formato de exportação
- [ ] Encargos de mora remetidos ao núcleo `juros-e-correcao`
- [ ] Arbitragem (se houver) com destaque formal

## Erros a evitar
- Chamar de "venda de software" o que é licença.
- Aceitar "o fornecedor não responde por nada" em contrato com consumidor.
- Deixar o fornecedor como "controlador" sem querer, por usar os dados para fins próprios.
- Omitir o destino dos dados ao fim do contrato.
- Usar cláusula padrão estrangeira com lei e foro estrangeiros sem avaliar exequibilidade no Brasil.

## Integração com o núcleo
`verificacao-de-citacoes`, `fidelidade-factual` (escopo técnico, métricas, nomes de produtos), `estilo-forense`, `juros-e-correcao` (mora e multas), `prazos-processuais` (se houver litígio).

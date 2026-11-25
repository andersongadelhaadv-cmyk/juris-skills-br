---
name: imob-regularizacao-fundiaria-reurb
description: >
  Estrutura requerimento de instauração de Regularização Fundiária Urbana
  (Reurb-S ou Reurb-E) ao Município, acompanhamento do procedimento até a
  Certidão de Regularização Fundiária (CRF) e seu registro, com base na Lei
  13.465/2017 (legitimação fundiária, legitimação de posse, isenções da
  Reurb-S, impugnação de titulares e confrontantes). Use quando o usuário pedir
  para regularizar bairro, núcleo ou loteamento informal, titular moradores
  de ocupação consolidada, requerer Reurb pela associação de moradores,
  impugnar Reurb que atinge imóvel do cliente ou registrar a CRF no cartório.
metadata:
  area: imobiliario
  tipo_peca: requerimento
  verificado_em: 2026-11-25
---
# Regularização Fundiária Urbana (Reurb-S e Reurb-E)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: (a) requerimento de instauração da Reurb por legitimado; (b) defesa de titular de domínio ou confrontante notificado (impugnação); (c) acompanhamento da classificação, do projeto, da decisão e da CRF; (d) registro da CRF e resposta a nota devolutiva.
- Não usar: imóvel isolado com mera divergência de medidas (`imob-retificacao-de-area`); adquirente individual que quer reaver o que pagou ou suspender prestações ao loteador (`imob-loteamento-irregular-defesa-do-adquirente`); usucapião individual (`imob-usucapiao-judicial`); desapropriação contra o cliente (`adm-desapropriacao-defesa`); omissão do Município discutida em juízo (`adm-mandado-de-seguranca` ou ação civil pública conforme o caso).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Quem é o cliente: legitimado requerente (art. 14), titular de domínio, confrontante, loteador, ocupante.
2. Localização e perímetro do núcleo; matrículas e transcrições atingidas (pedir certidões).
3. Prova de existência e consolidação do núcleo e da data de formação (fotos aéreas, cadastros de IPTU, contas de serviços), especialmente se anterior a 22/12/2016.
4. Perfil de renda predominante dos ocupantes (define Reurb-S ou Reurb-E).
5. Área pública ou privada; restrições ambientais ou de risco conhecidas.
6. Legislação municipal sobre Reurb (decretos, leis locais) e órgão competente.
7. Situação de cada ocupante: possui outro imóvel? já recebeu legitimação? uso residencial ou não?

## Prazo e contagem
- Classificação da modalidade pelo Município: até **180 dias**, ou indeferimento fundamentado (art. 30, § 2º).
- Impugnação de titulares, confinantes e terceiros notificados: **30 dias** do recebimento da notificação (art. 31, § 1º).
- Registro: o Oficial emite nota de exigência ou pratica os atos em **15 dias**; o procedimento registral termina em **60 dias**, prorrogáveis por igual período com justificativa (art. 44, caput e § 5º).
- Legitimação de posse: conversão automática em propriedade após **5 anos** do registro, atendidos os requisitos do art. 183 da Constituição (art. 26).
- Prazos de recursos administrativos: lei municipal [VERIFICAR na norma local]. Prazos judiciais: `prazos-processuais`.

## Estrutura da peça
Requerimento ao Município → legitimidade → identificação do núcleo → enquadramento como núcleo urbano informal consolidado → modalidade pretendida → instrumentos jurídicos → documentos e pedidos. Roteiro e modelo de impugnação em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Legitimados** (art. 14): entes federativos e sua administração indireta; beneficiários, individual ou coletivamente (cooperativas, associações de moradores e afins); proprietários, loteadores e incorporadores; Defensoria Pública; Ministério Público.
- **Modalidade** (art. 13): Reurb-S para núcleo ocupado predominantemente por população de baixa renda, declarado por ato do Executivo municipal; Reurb-E para os demais. A classificação é do Município, caso a caso (art. 30, I).
- **Legitimação fundiária** (art. 23): aquisição originária, só no âmbito da Reurb, para núcleo consolidado existente em 22/12/2016; na Reurb-S, o beneficiário não pode ser proprietário de outro imóvel nem ter recebido legitimação anterior (§ 1º).
- **Legitimação de posse** (arts. 25 e 26): título que reconhece a posse, convertível em propriedade.
- **Fases** (art. 28): requerimento → processamento com notificações → projeto → saneamento → decisão → CRF → registro.
- **Regresso**: em parcelamento informal feito por particular, concluída a Reurb, há direito de regresso contra os responsáveis pela implantação (art. 14, § 2º).
- **Poder-dever do Município**: o STJ reconhece a obrigação municipal de fiscalizar e regularizar o parcelamento irregular (AgInt no AREsp 1.762.074).

## Fundamentos verificados
- Lei 13.465/2017: arts. 9º, § 2º; 11, I, II, III e VI; 13 e § 1º; 14 e § 2º; 15; 23; 25; 26; 28; 30; 31, § 1º; 32; 35; 40; 41; 42; 44.
- STJ: AgInt no AREsp 1.762.074 (poder-dever municipal); REsp 1.796.394 (usucapião judicial independe de prévia via extrajudicial).
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Instauração da Reurb e classificação na modalidade adequada, com justificativa de renda (Reurb-S) ou indicação dos responsáveis por custos (Reurb-E).
- Notificação dos titulares de domínio, confinantes e terceiros (art. 31).
- Elaboração ou aprovação do projeto de regularização (art. 35) e indicação dos instrumentos (art. 15) para cada situação.
- Decisão que aprove o projeto e declare os ocupantes e seus direitos (art. 40); expedição da CRF (art. 41).
- No registro: isenção de custas e emolumentos dos atos listados no art. 13, § 1º, na Reurb-S; dispensa de comprovação de tributos (art. 44, § 3º).

## Checklist pré-protocolo
- [ ] Legitimidade do requerente demonstrada (estatuto e ata, se associação)
- [ ] Perímetro e matrículas atingidas identificados
- [ ] Prova da consolidação e da data do núcleo (marco de 22/12/2016 quando relevante)
- [ ] Modalidade pretendida justificada; lei municipal conferida
- [ ] Restrições ambientais e áreas de risco levantadas
- [ ] Instrumento escolhido para cada perfil de ocupante (fundiária, posse, usucapião, CDRU, compra e venda)
- [ ] Lista de titulares e confrontantes com endereço
- [ ] Controle dos prazos de 180, 30, 15 e 60 dias

## Erros a evitar
- Pedir legitimação fundiária para núcleo formado depois de 22/12/2016 (art. 9º, § 2º).
- Prometer isenção de emolumentos na Reurb-E (a lista do art. 13, § 1º, é da Reurb-S).
- Incluir na legitimação fundiária da Reurb-S beneficiário que já é proprietário de outro imóvel (art. 23, § 1º).
- Deixar a impugnação do cliente passar dos 30 dias do recebimento da notificação.
- Ignorar o regresso contra o loteador ou incorporador irregular (art. 14, § 2º).
- Tratar a Reurb como via para discutir domínio entre particulares — litígio de propriedade segue a via judicial.

## Integração com o núcleo
`prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

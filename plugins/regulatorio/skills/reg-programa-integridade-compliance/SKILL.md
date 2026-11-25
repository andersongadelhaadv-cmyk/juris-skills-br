---
name: reg-programa-integridade-compliance
description: >
  Estrutura programa de integridade anticorrupção e redige parecer de
  compliance regulatório (diagnóstico de aderência da empresa a normas
  setoriais e à Lei 12.846/2013), com base nos arts. 5º, 6º, 7º, VIII, 16 e 25
  da Lei 12.846/2013, nos arts. 23, 56 e 57 do Decreto 11.129/2022 e no art. 25,
  § 4º, da Lei 14.133/2021. Use quando o usuário pedir programa de compliance,
  código de conduta anticorrupção, avaliação de programa de integridade,
  plano de integridade para contrato de grande vulto, parecer de compliance
  regulatório, gap analysis regulatório ou matriz de riscos de integridade.
metadata:
  area: regulatorio
  tipo_peca: parecer
  verificado_em: 2026-11-25
---
# Programa de integridade e parecer de compliance regulatório

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: (a) desenhar ou revisar programa de integridade (Lei 12.846/2013; Decreto 11.129/2022); (b) relatório de perfil e de conformidade do programa para processo administrativo de responsabilização (PAR) ou leniência; (c) plano de integridade exigido em contrato de grande vulto (Lei 14.133/2021, art. 25, § 4º); (d) parecer de compliance regulatório: diagnóstico de aderência a normas de agência, com riscos e plano de ação.
- Não usar:
  - Defesa em processo sancionador já instaurado por agência: `reg-defesa-processo-sancionador-agencia`.
  - Ação de improbidade contra agentes: `adm-defesa-em-improbidade`.
  - Adequação à LGPD: skills `digital-*` (por exemplo `digital-politica-de-privacidade-e-termos-de-uso`).
  - Parecer sobre um contrato específico: `contratos-parecer-sobre-contrato`.
  - Sanção em licitação: `adm-defesa-em-processo-sancionador-licitacao`.

## Entradas mínimas (perguntar o que faltar; nunca supor fatos)
1. Finalidade: programa novo, revisão, avaliação em PAR/leniência, exigência contratual ou parecer regulatório.
2. Perfil (Decreto 11.129/2022, art. 57, § 1º): número de empregados, faturamento e enquadramento como ME/EPP, governança, grupo econômico, intermediários, setor, países, interação com o setor público.
3. Contratos, licenças e outorgas com o poder público; agências que regulam a empresa.
4. Políticas existentes: código de conduta, canal de denúncia, due diligence de terceiros, brindes e hospitalidade, doações e patrocínios, conflito de interesses.
5. Histórico: investigações, sanções, autuações, denúncias internas.
6. Para parecer regulatório: lista de normas aplicáveis informada ou a levantar, e evidências de cumprimento (relatórios, laudos, protocolos).

## Prazo e contagem
- Contrato de grande vulto: programa implantado em 6 meses da celebração do contrato, conforme regulamento (Lei 14.133/2021, art. 25, § 4º) [VERIFICAR regulamento aplicável ao ente contratante].
- Redução da multa no PAR exige programa anterior ao ato lesivo para o percentual máximo (Decreto 11.129/2022, art. 23, parágrafo único, III).
- Prescrição das infrações da Lei 12.846/2013: 5 anos da ciência ou da cessação, interrompida pela instauração do processo (art. 25).
- Prazos de PAR e de leniência: `prazos-processuais` e norma do órgão.

## Estrutura do documento
Programa: diagnóstico de riscos → pilares (Decreto 11.129/2022, art. 57, I a XV) → políticas → governança → monitoramento. Parecer: consulta → normas aplicáveis → achados → classificação de risco → recomendações e plano de ação → conclusão. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Responsabilidade objetiva** da pessoa jurídica por atos lesivos em seu interesse ou benefício (Lei 12.846/2013, arts. 1º e 2º): o programa não afasta a responsabilidade, mas pesa na dosimetria (art. 7º, VIII) e na redução da multa (Decreto 11.129/2022, art. 23, V).
- **Efetividade, não papel**: o programa é avaliado pela aplicação prática, adequação aos riscos e efetividade em relação ao ato investigado (Decreto 11.129/2022, arts. 56 e 57, § 2º).
- **Proporcionalidade ao porte**: ME/EPP e porte reduzido justificam programa simplificado (art. 57, § 1º).
- **Parecer regulatório**: só afirmar cumprimento com evidência documental; norma setorial não conferida vai como [VERIFICAR]. Respostas a consultas e súmulas da agência vinculam o órgão (LINDB, art. 30) e devem ser buscadas.

## Fundamentos verificados
- Lei 12.846/2013: arts. 1º, 2º, 5º, 6º, 7º (VIII), 16 e 25.
- Decreto 11.129/2022: art. 23 (V e parágrafo único, III), art. 56, art. 57 (I a XV, §§ 1º e 2º).
- Lei 14.133/2021: art. 25, § 4º.
- LINDB: art. 30.
Detalhe em [fundamentos](references/fundamentos.md).

## Cláusulas essenciais (programa) / conclusões (parecer)
- Compromisso formal da alta direção e recursos (art. 57, I).
- Código de conduta e políticas para todos, inclusive administradores, e extensão a terceiros (II e III).
- Treinamento periódico (IV); gestão de riscos com reavaliação (V).
- Registros contábeis e controles internos (VI e VII); procedimentos para licitações, contratos e interação com o setor público (VIII).
- Instância independente com autoridade (IX); canal de denúncia com proteção ao denunciante de boa-fé (X).
- Medidas disciplinares (XI); remediação imediata (XII); due diligence de terceiros, PEP, patrocínios e doações (XIII); due diligence em operações societárias (XIV); monitoramento contínuo (XV).
- No parecer: cada achado com norma, evidência, risco (alto/médio/baixo) e providência com responsável e prazo.

## Checklist de entrega
- [ ] Matriz de riscos feita antes das políticas (não copiar modelo genérico)
- [ ] Os 15 parâmetros do art. 57 endereçados ou justificada a dispensa pelo porte
- [ ] Evidências de aplicação previstas (registros de treinamento, atas, relatórios do canal)
- [ ] Data de implantação documentada (relevante para a redução da multa)
- [ ] No parecer, cada norma setorial citada conferida ou marcada [VERIFICAR]
- [ ] Linguagem que não constitua confissão, se houver investigação em curso

## Erros a evitar
- Programa "de prateleira", sem risco mapeado: perde o valor na dosimetria.
- Prometer que o programa afasta a responsabilidade objetiva.
- Implantar depois do fato e pedir a redução máxima.
- Parecer regulatório que afirma conformidade sem evidência.
- Confundir leniência (art. 16: primeiro a cooperar, cessação, admissão) com mera colaboração.

## Integração com o núcleo
`verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`, `prazos-processuais`, `juros-e-correcao` (multas e ressarcimento).

---
name: digital-contrato-dpa-operador
description: >
  Elabora ou revisa acordo de tratamento de dados pessoais (DPA) entre
  controlador e operador — instruções, segurança, suboperadores, incidentes,
  apoio aos direitos dos titulares, auditoria, devolução ou eliminação ao fim,
  responsabilidade e transferência internacional —, com base nos arts. 37 a 40,
  42, 46 e 33 a 36 da LGPD e nas cláusulas-padrão da Resolução CD/ANPD 19/2024.
  Use quando o usuário pedir DPA, adendo de proteção de dados, anexo LGPD de
  contrato de SaaS, nuvem, folha, call center, marketing ou TI, revisão do DPA
  de fornecedor estrangeiro ou cláusula de transferência internacional.
metadata:
  area: digital
  tipo_peca: contrato
  verificado_em: 2026-11-25
---
# Acordo de tratamento de dados (DPA) — controlador e operador

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: contrato principal em que uma parte trata dados pessoais **em nome** da outra (LGPD art. 5º, VII) — SaaS, hospedagem, processamento de folha, atendimento terceirizado, agência de marketing, contabilidade.
- Usar para revisar o DPA padrão de fornecedor (geralmente pró-operador) e para o anexo de transferência internacional.
- Não usar: o contrato principal em si (`contratos-licenca-de-software-e-saas`, `contratos-prestacao-de-servicos`, `contratos-prestacao-de-servicos-pj`); níveis de serviço (`contratos-sla-nivel-de-servico`); confidencialidade sem tratamento de dados pessoais (`contratos-nda-confidencialidade`); duas empresas que decidem cada uma sobre os dados (controladoras independentes ou conjuntas — o DPA de operador não serve; adaptar como acordo de compartilhamento); parecer sobre contrato pronto (`contratos-parecer-sobre-contrato`).

## Entradas mínimas (perguntar o que faltar; nunca supor fatos)
1. Quem decide finalidade e meios (controlador) e quem executa (operador)? A qualificação vem dos fatos, não do rótulo do contrato.
2. Atividade de tratamento: categorias de dados, de titulares, finalidade, base legal do controlador, duração.
3. Há dados sensíveis (art. 5º, II) ou de crianças e adolescentes (art. 14)?
4. Onde ficam os dados: país, nuvem, provedores; há acesso remoto do exterior?
5. Suboperadores já usados ou previstos.
6. Medidas de segurança ofertadas (criptografia, controle de acesso, logs, certificações).
7. Qual lado o cliente representa (controlador ou operador) e o poder de negociação.
8. Contrato principal: prazo, rescisão, limitação de responsabilidade, foro.

## Prazo e contagem
- **Incidente:** o controlador tem 3 dias úteis, do conhecimento, para comunicar ANPD e titulares (Res. CD/ANPD 15/2024, arts. 6º e 9º). O DPA deve obrigar o operador a avisar em prazo bem menor (ex.: 24 a 48 horas), sem que a LGPD fixe esse número — é escolha contratual.
- **Direitos dos titulares:** declaração completa em 15 dias (LGPD art. 19, II); o operador deve devolver o pedido e os dados ao controlador com folga.
- **Cláusulas-padrão:** quem usa cláusulas contratuais para transferência internacional tinha 12 meses da publicação da Res. 19/2024 para incorporar as cláusulas-padrão (art. 2º, parágrafo único) — prazo já esgotado; contrato vigente sem elas está irregular.
- Prazos processuais em eventual litígio: `prazos-processuais`.

## Estrutura da peça
Partes e papéis → objeto e anexo descritivo do tratamento → instruções documentadas → confidencialidade de pessoal → segurança → suboperadores → incidentes → apoio aos direitos dos titulares, ao RIPD e à ANPD → registro e auditoria → transferência internacional → término (devolução ou eliminação) → responsabilidade e regresso → disposições finais. Cláusulas detalhadas em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Instruções:** o operador trata segundo as instruções do controlador, que verifica seu cumprimento (art. 39). Prever instrução por escrito e dever do operador de alertar sobre instrução que considere ilícita.
- **Registro:** ambos mantêm registro das operações (art. 37). O operador deve fornecer o seu ao controlador quando pedido.
- **RIPD:** a ANPD pode exigir o relatório do controlador (art. 38); o operador fornece as informações técnicas necessárias.
- **Segurança:** medidas técnicas e administrativas do art. 46, desde a concepção (§ 2º), mantidas após o fim do tratamento (art. 47) e aderentes ao art. 49.
- **Responsabilidade perante o titular:** o operador responde solidariamente quando descumpre a lei ou não segue as instruções lícitas, equiparando-se ao controlador (art. 42, § 1º, I); quem paga tem regresso proporcional (§ 4º). Cláusula entre as partes não afasta direito do titular; serve para regresso e repartição de custos.
- **Excludentes:** só as do art. 43 (não tratou; tratou sem violar a lei; culpa exclusiva do titular ou de terceiro).
- **Transferência internacional:** exige uma das hipóteses do art. 33. Usando cláusulas-padrão, adotá-las **na íntegra e sem alteração**, e nenhuma outra cláusula pode contrariá-las (Res. 19/2024, anexo I, art. 16, caput e § 2º). O titular pode pedir a íntegra das cláusulas (art. 17).

## Fundamentos verificados
- LGPD: arts. 5º (VI, VII, X), 6º, 16, 33 a 36, 37 a 40, 42 a 44, 46, 47, 49.
- Res. CD/ANPD 15/2024, arts. 6º e 9º; Res. CD/ANPD 19/2024, art. 2º e anexo I, arts. 15 a 17.
- CDC art. 51, I (em contrato de consumo, cláusula que atenue responsabilidade é nula).
Detalhe em [fundamentos](references/fundamentos.md).

## Cláusulas essenciais
- Anexo descritivo: dados, titulares, finalidade, duração, local de armazenamento.
- Tratamento só por instrução documentada; vedado uso para fins próprios do operador.
- Confidencialidade de empregados e prestadores com acesso.
- Lista de medidas de segurança mínimas, com revisão periódica.
- Suboperador só com autorização (específica ou geral com aviso prévio e direito de objeção), com as mesmas obrigações e responsabilidade do operador pelos atos dele.
- Aviso de incidente em horas, com as informações do art. 6º, § 2º, da Res. 15/2024, e cooperação na investigação.
- Encaminhamento ao controlador, em prazo curto, de todo pedido de titular ou da ANPD; o operador não responde ao titular em nome do controlador sem instrução.
- Direito de auditoria (ou relatório independente), com aviso e custos definidos.
- Ao término: devolução e/ou eliminação, com certificado, ressalvadas guardas legais (art. 16).
- Transferência internacional: hipótese do art. 33 e cláusulas-padrão como anexo inalterado.
- Responsabilidade, regresso, seguro cibernético e limite entre as partes (sem oponibilidade ao titular).

## Checklist pré-protocolo
- [ ] Papéis qualificados pelos fatos (quem decide finalidade e meios)
- [ ] Anexo descritivo completo, sem "todos os dados necessários"
- [ ] Prazo de aviso de incidente compatível com os 3 dias úteis do controlador
- [ ] Regime de suboperadores com lista atual anexada
- [ ] Destino dos dados no término e certificado de eliminação
- [ ] Transferência internacional mapeada; cláusulas-padrão sem edição
- [ ] Limitação de responsabilidade conferida contra o art. 42 e, se consumo, contra o CDC
- [ ] Coerência com o contrato principal (prazo, foro, rescisão, prevalência)

## Erros a evitar
- Chamar de "operador" quem usa os dados para fins próprios (ex.: treinar produto, vender leads): isso é controlador.
- Copiar DPA estrangeiro com referência só ao GDPR, sem LGPD e sem as cláusulas-padrão da ANPD.
- Editar as cláusulas-padrão ou contrariá-las em outra cláusula (invalida o mecanismo).
- Prazo de aviso de incidente "sem demora indevida", sem número.
- Esquecer o fim do contrato: dados ficam com o fornecedor indefinidamente.
- Achar que o limite de responsabilidade entre as partes vale contra o titular.

## Integração com o núcleo
`verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`, `prazos-processuais`. Multas contratuais e atualização de valores: `juros-e-correcao`.

---
name: amb-auditoria-compliance
description: >
  Conduz auditoria jurídica ambiental (due diligence) e estrutura programa de
  compliance ambiental, com parecer de riscos nas três esferas (civil objetiva
  e propter rem, administrativa e penal), checagem de licenças, Cadastro
  Técnico Federal, relatório anual da TCFA, CAR, passivos e contratos. Use
  quando o usuário pedir due diligence ambiental na compra de imóvel ou de
  empresa, parecer de passivo ambiental, matriz de risco, política e
  procedimentos de conformidade ambiental ou revisão de cláusulas ambientais
  em contratos e operações de M&A.
metadata:
  area: ambiental
  tipo_peca: parecer
  verificado_em: 2026-11-25
---
# Auditoria e compliance ambiental

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: parecer de due diligence ambiental, matriz de riscos, programa de conformidade (política, procedimentos, controles, treinamento, canal de reporte), cláusulas ambientais de contratos.
- Não usar:
  - programa de integridade regulatório geral (anticorrupção, agências): `reg-programa-integridade-compliance`;
  - due diligence societária sem foco ambiental: `soc-due-diligence-societaria`;
  - análise de matrícula para compra de imóvel urbano: `imob-analise-de-matricula-e-due-diligence`;
  - licença em si: `amb-licenca-de-operacao-corretiva`; litígio já instaurado: `amb-defesa-*`.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Objetivo: aquisição (imóvel, quotas/ações, ativos), financiamento, auditoria interna ou implantação de programa.
2. Atividades exercidas, unidades, CNAE e enquadramento como potencialmente poluidoras.
3. Licenças (prévia, instalação, operação) com condicionantes e vencimentos; outorgas de água; autorizações de supressão.
4. Inscrição no Cadastro Técnico Federal e entrega do relatório anual; TCFA.
5. Imóveis: matrículas, CAR, reserva legal, APP, áreas contaminadas.
6. Histórico: autos de infração, embargos, TAC, ACP, inquéritos, processos penais (da empresa, dos sócios e dos vendedores anteriores).
7. Contratos com terceiros que gerem risco (transporte e destinação de resíduos, fornecedores de madeira/insumos, arrendatários).

## Prazo e contagem
- Relatório anual de atividades ao IBAMA até 31 de março (Lei 6.938, art. 17-C, § 1º).
- Vencimento e renovação de licenças e condicionantes: calendário próprio de cada licença e da norma estadual [VERIFICAR caso a caso]; mudanças da Lei 15.190/2025 (Lei Geral do Licenciamento) com vigência a conferir [VERIFICAR].
- Prazos de defesa e recurso em processo sancionador: `amb-defesa-auto-de-infracao` e `prazos-processuais`.

## Estrutura do parecer
Escopo e limitações → documentos analisados → mapa de responsabilidades por esfera → achados por tema (licenciamento, cadastros, imóveis, resíduos, contencioso) → classificação de risco → recomendações e cláusulas → plano de ação. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e premissas jurídicas
- Civil: objetiva (Lei 6.938, art. 14, § 1º), solidária e *propter rem* — o adquirente do imóvel responde pelo passivo, e os anteriores também (Súmula 623; Tema 1.204/STJ; Lei 12.651, art. 2º, § 2º). Poluidor indireto inclui quem financia ou se beneficia (art. 3º, IV).
- Administrativa: subjetiva (AREsp 2.957.178); multa é pessoal e não se transmite ao herdeiro que não concorreu para a infração (REsp 1.823.083) — distinguir passivo de multa e passivo de reparação na operação. Multa pode ser aplicada sem advertência prévia (Tema 1.159/STJ).
- Penal: empresa e dirigentes (Lei 9.605, arts. 2º e 3º); crimes de omissão de obrigação de relevante interesse ambiental (art. 68) e de laudo/relatório falso ou enganoso (art. 69-A) atingem gestores e consultores.
- Desconsideração da personalidade quando obstáculo ao ressarcimento ambiental (Lei 9.605, art. 4º).

## Fundamentos verificados
- CF, art. 225, § 3º.
- Lei 6.938/1981: arts. 3º, IV; 9º; 10; 14, § 1º; 17, II; 17-B; 17-C, § 1º.
- Lei 9.605/1998: arts. 2º, 3º, 4º, 60, 68, 69-A, 70, 72.
- Lei 12.651/2012: arts. 2º, § 2º; 29.
- Súmula 623/STJ; Tema 1.204/STJ; Tema 1.159/STJ; REsp 1.823.083; AREsp 2.957.178.
Detalhe em [fundamentos](references/fundamentos.md).

## Recomendações e cláusulas essenciais
- Em aquisições: declarações e garantias ambientais específicas; indenização por passivo anterior sem limite curto de prazo (a reparação é imprescritível — Tema 999/STF); retenção de preço/escrow; condição precedente de regularização (CAR, licença, TAC); responsabilidade por multas pendentes do vendedor.
- Em contratos com terceiros: exigência de licença do transportador/destinador, comprovantes de destinação, direito de auditoria, rescisão por descumprimento, seguro ambiental quando houver.
- No programa: responsável interno com autonomia; matriz de licenças e condicionantes com alertas; registro e reporte de incidentes; treinamento; revisão de laudos técnicos antes do protocolo (risco do art. 69-A); comunicação imediata de perigo (atenuante do art. 14, III, da Lei 9.605).

## Checklist do parecer
- [ ] Escopo e documentos não fornecidos declarados como limitação
- [ ] Cada achado ligado à esfera (civil, administrativa, penal) e ao responsável
- [ ] Licenças e condicionantes conferidas com datas
- [ ] CTF, relatório anual e TCFA verificados
- [ ] CAR e reserva legal dos imóveis cruzados com imagens
- [ ] Contencioso e TACs listados com valores e status
- [ ] Recomendações priorizadas (crítico, alto, médio, baixo) com responsável e prazo

## Erros a evitar
- Tratar passivo de reparação como se fosse limitado no tempo ou extinto pela venda (Tema 999/STF; Súmula 623).
- Somar multas administrativas ao passivo do adquirente como se fossem *propter rem* (REsp 1.823.083).
- Concluir "sem risco" sem ter visto licenças, condicionantes e contencioso — registrar o que não foi entregue.
- Redigir parecer que endossa laudo técnico não revisado (art. 69-A).

## Integração com o núcleo
`verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`, `prazos-processuais`; cláusulas: `contratos-analise-e-revisao-de-contrato`; M&A: `soc-ma-compra-de-quotas-e-acoes`.

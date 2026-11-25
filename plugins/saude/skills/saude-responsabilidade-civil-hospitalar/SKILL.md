---
name: saude-responsabilidade-civil-hospitalar
description: >
  Redige petição inicial de ação indenizatória contra hospital, clínica ou
  estabelecimento de saúde privado por falha do serviço hospitalar (infecção
  hospitalar, enfermagem, equipamentos, estrutura, demora de atendimento ou de
  leito), com responsabilidade objetiva do CDC art. 14 e a distinção entre
  falha do serviço próprio e ato culposo do médico. Use quando o usuário pedir
  ação contra hospital, infecção hospitalar ou pós-cirúrgica, queda do paciente
  internado, erro de enfermagem ou medicação, falta de UTI, morte em hospital
  particular ou responsabilidade solidária do hospital pelo médico.
metadata:
  area: saude
  tipo_peca: inicial
  verificado_em: 2026-11-25
---
# Responsabilidade civil hospitalar (inclusive infecção hospitalar)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: dano causado por serviço do próprio estabelecimento — hotelaria e internação, enfermagem, esterilização, medicação, equipamentos, exames, segurança do paciente, triagem e demora — ou pelo médico preposto do hospital.
- Dano atribuído só à técnica de médico que o paciente escolheu e que apenas usou a estrutura: `saude-indenizacao-erro-medico` (o hospital, aí, tende a não responder sem culpa do preposto).
- Hospital público, ou atendimento pelo SUS em hospital conveniado: `adm-responsabilidade-civil-do-estado` (CF art. 37, § 6º; Tema 940/STF); a prescrição segue o regime da Fazenda/prestadora.
- Cobrança do hospital contra o paciente, termo de responsabilidade, cheque-caução: fora desta skill (`consumidor-acao-indenizatoria` ou `civel-contestacao`).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Datas de internação, procedimentos, alta, reinternação; setor (UTI, centro cirúrgico, enfermaria).
2. Prontuário completo, inclusive folhas de enfermagem, prescrições, controle de infecção, culturas e antibiogramas.
3. Infecção: quando surgiu (sinais, exames), qual agente, se havia surto conhecido, se o paciente já chegou infectado.
4. Vínculo do médico com o hospital: empregado, plantonista, corpo clínico, médico externo escolhido pelo paciente.
5. Danos: tratamento adicional, sequela, perda de renda, óbito e dependentes, dano estético.
6. Atendimento particular, por plano ou pelo SUS? (define réu e prescrição).

## Prazo e contagem
- Paciente consumidor contra hospital privado: 5 anos do conhecimento do dano e da autoria (CDC art. 27).
- Hospital privado conveniado ao SUS: prescrição quinquenal do art. 1º-C da Lei 9.494/1997 (REsp 2.200.981, 3ª Turma, 2025). Hospital público: Decreto 20.910/1932.
- Prazos processuais: `prazos-processuais`.

## Estrutura da peça
Fatos com linha do tempo → relação de consumo → responsabilidade objetiva pelo serviço hospitalar (CDC 14) → falha concreta (infecção, enfermagem, estrutura) e/ou culpa do médico preposto → nexo causal → danos → prova (ônus legal do art. 14, § 3º; perícia) → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Duas trilhas, não misturar.** (a) Serviço próprio do hospital (internação, instalações, equipamentos, serviços auxiliares): responsabilidade objetiva do art. 14 do CDC. (b) Ato técnico do médico: o hospital responde se o médico for seu preposto e houver culpa dele — a objetiva do hospital "não é absoluta" (AgInt no REsp 1.892.763, 4ª Turma, 2024; AgInt no AREsp 2.348.178, 3ª Turma, 2024).
- **Infecção hospitalar** é tratada como falha do serviço próprio: responsabilidade objetiva do hospital (AgInt nos EDcl no AREsp 2.590.580, 3ª Turma, 2024; AgInt no AREsp 2.415.362, 3ª Turma, 2024 — falha de esterilização com surto conhecido).
- **Ônus da prova.** Na objetiva, o hospital só se exime provando inexistência do defeito ou culpa exclusiva do consumidor ou de terceiro (CDC art. 14, § 3º) — inversão *ope legis*. Mas o nexo continua do autor: laudo inconclusivo sobre a origem da infecção levou à improcedência no REsp 2.134.033 (4ª Turma, 2025). Antecipe a perícia: culturas, tempo de surgimento, protocolo da CCIH.
- **Perda de uma chance** (ex.: demora de leito de UTI) também se aplica ao hospital (AgInt no AREsp 2.141.017, 3ª Turma, 2023).
- **Polo passivo.** Hospital; médico, se houver culpa pessoal (solidariedade — CC art. 942, parágrafo único); operadora, se a rede credenciada é dela (avaliar caso a caso).

## Fundamentos verificados
- CDC arts. 6º, VIII; 14, caput, §§ 1º e 3º; 27. CC arts. 932, III, 933, 942, 948, 949, 950. CPC arts. 300 e 373, § 1º.
- STJ: AgInt nos EDcl no AREsp 2.590.580 e AgInt no AREsp 2.415.362 (infecção — objetiva); AgInt no REsp 1.892.763 e AgInt no AREsp 2.348.178 (limite da objetiva; médico preposto exige culpa); REsp 2.134.033 (sem nexo, sem indenização); AgInt no AREsp 2.141.017 (perda de uma chance do hospital); REsp 2.200.981 (prescrição — conveniado ao SUS).
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Danos materiais e lucros cessantes (CC art. 949); pensão (CC art. 950); óbito (CC art. 948).
- Dano moral e dano estético, separados; dano moral reflexo dos familiares, se for o caso, com legitimidade descrita.
- Subsidiariamente, perda de uma chance.
- Exibição do prontuário integral e dos registros da Comissão de Controle de Infecção Hospitalar do período.
- Perícia por infectologista (infecção) ou especialista pertinente; quesitos na inicial.
- Juros e correção: núcleo `juros-e-correcao`.

## Checklist pré-protocolo
- [ ] Trilha definida: serviço próprio (objetiva) x ato médico (culpa do preposto)
- [ ] Vínculo do médico com o hospital provado ou a provar
- [ ] Infecção: data de surgimento, agente, culturas e indícios de origem hospitalar
- [ ] Nexo explicado; pedido subsidiário de perda de uma chance
- [ ] Particular, plano ou SUS? (réu e prescrição)
- [ ] Prontuário e registros de CCIH requeridos
- [ ] Quesitos e assistente técnico
- [ ] Juros e correção remetidos ao núcleo

## Erros a evitar
- Afirmar que o hospital responde objetivamente por qualquer ato do médico: para o ato técnico, é preciso culpa do preposto.
- Supor que a objetiva dispensa o nexo: o autor ainda prova a origem do dano.
- Processar hospital público com base só no CDC: o regime é o da CF art. 37, § 6º.
- Omitir que o paciente chegou com infecção comunitária: o réu vai provar.
- Fixar taxa de juros na peça.

## Integração com o núcleo
`juros-e-correcao`, `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

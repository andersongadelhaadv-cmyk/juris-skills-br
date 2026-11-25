---
name: saude-defesa-do-medico
description: >
  Redige contestação do médico (e, se for o caso, da clínica) em ação
  indenizatória por erro médico: ilegitimidade em atendimento público (Tema
  940/STF), prescrição, obrigação de meio e responsabilidade subjetiva (CDC
  art. 14, § 4º), ausência de culpa e de nexo causal, risco inerente informado,
  impugnação de danos e estratégia pericial. Use quando o usuário pedir defesa
  de médico, contestação em ação de erro médico, defesa de cirurgião plástico,
  defesa de clínica por ato do médico ou resposta a pedido de indenização por
  complicação cirúrgica.
metadata:
  area: saude
  tipo_peca: contestacao
  verificado_em: 2026-11-25
---
# Defesa do médico em ação de erro médico

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: contestação do médico réu (particular, plano, corpo clínico) e, com adaptações, da clínica demandada pelo ato do médico.
- Defesa de hospital por falha do serviço próprio (infecção, enfermagem, estrutura): adapte a partir de `saude-responsabilidade-civil-hospitalar` (o regime lá é objetivo) e de `civel-contestacao`.
- Defesa do ente público ou da Fazenda: `fazenda-contestacao-fazendaria`. Defesa ética no CRM ou criminal: fora desta skill.
- Estrutura geral de contestação (prazo, preliminares, reconvenção): `civel-contestacao`.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Petição inicial, documentos e decisão de citação (data de juntada do mandado/AR).
2. Prontuário completo, termo de consentimento, fotos pré e pós-operatórias, mensagens trocadas com o paciente.
3. Onde e como atendeu: consultório particular, plano, plantão em hospital privado, hospital público ou conveniado ao SUS.
4. Relato técnico do médico: indicação, técnica, intercorrência, conduta adotada, retornos oferecidos e faltas do paciente.
5. Literatura e protocolos que sustentam a conduta; nome de assistente técnico.
6. Seguro de responsabilidade civil profissional (denunciação da lide?) e existência de processo ético ou criminal.

## Prazo e contagem
- Contestação: prazo e termo inicial pelo núcleo `prazos-processuais` (dias úteis).
- Prescrição a examinar: CDC art. 27 (5 anos do conhecimento do dano e da autoria) na relação de consumo; regime da Fazenda/prestadora no atendimento público ou conveniado (Decreto 20.910/1932; Lei 9.494/1997, art. 1º-C — REsp 2.200.981, 3ª Turma, 2025). Fixe a data da ciência com documentos do próprio autor.

## Estrutura da peça
Síntese → preliminares (ilegitimidade, prescrição, inépcia) → fatos sob a ótica técnica → regime de culpa e obrigação de meio → ausência de culpa → ausência de nexo → informação e risco inerente → impugnação dos danos → prova pericial → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Ilegitimidade passiva** se o atendimento foi prestado por agente de ente público ou de prestadora de serviço público: a ação deve ser proposta contra o Estado ou a prestadora (Tema 940/STF; CF art. 37, § 6º).
- **Prescrição**: conferir a data do conhecimento do dano (alta, diagnóstico da sequela, nova cirurgia) e o regime aplicável (acima).
- **Regime de culpa**: médico é profissional liberal (CDC art. 14, § 4º; CC art. 951). A objetiva do hospital não se estende ao ato técnico do médico (AgInt no AREsp 2.348.178, 3ª Turma, 2024).
- **Obrigação de meio**: o médico não promete cura; o autor deve provar a conduta abaixo do padrão técnico. Se o procedimento for estético, a jurisprudência do STJ trata como resultado com culpa presumida (REsp 2.173.636, 4ª Turma, 2024): então a defesa precisa provar excludente — fato da vítima (descumprimento das orientações pós-operatórias), caso fortuito, reação orgânica imprevisível — ou demonstrar que a parte do procedimento era reparadora.
- **Nexo causal** é ônus do autor, mesmo em responsabilidade objetiva (AgInt no AgInt no AREsp 2.158.891, 3ª Turma, 2023). Complicação conhecida e possível na literatura, tratada corretamente, não é erro.
- **Inversão do ônus** (CDC art. 6º, VIII; CPC art. 373, § 1º): se requerida, pedir que seja decidida antes da instrução, com oportunidade de produzir prova (CPC art. 373, § 1º, parte final).
- **Perda de uma chance**: exigir a demonstração de chance séria e real e de relação com a conduta (AgInt no REsp 1.923.907, 3ª Turma, 2023).
- **Termo de consentimento** específico e informação documentada afastam a tese de defeito de informação (CDC art. 14, caput; CC art. 15) — sustente com o documento e o prontuário.

## Fundamentos verificados
- CDC arts. 6º, VIII; 14, § 4º; 27. CC arts. 15, 186, 951. CPC arts. 373, § 1º. CF art. 37, § 6º.
- STF: Tema 940. STJ: REsp 2.173.636; AgInt no AREsp 2.348.178; AgInt no AgInt no AREsp 2.158.891; AgInt no REsp 1.923.907; REsp 2.134.033 (laudo inconclusivo afasta o dever de indenizar); REsp 1.989.585 (vedada a cumulação restituição + nova cirurgia); REsp 2.200.981.
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Acolhimento das preliminares (ilegitimidade, prescrição); no mérito, improcedência.
- Subsidiariamente: afastar pensão sem prova de redução da capacidade; afastar cumulação indevida de restituição do preço com custeio de nova cirurgia por terceiro (REsp 1.989.585, 3ª Turma, 2022); reduzir moral/estético a parâmetros proporcionais.
- Perícia por especialista na área do procedimento; quesitos e assistente técnico desde já.
- Denunciação da lide à seguradora, se houver apólice (avaliar conveniência).
- Juros e correção: impugnar termo inicial e índices remetendo ao núcleo `juros-e-correcao`.

## Checklist pré-protocolo
- [ ] Prazo de contestação conferido no núcleo
- [ ] Atendimento público ou conveniado? Ilegitimidade (Tema 940)
- [ ] Prescrição calculada da ciência do dano
- [ ] Natureza da obrigação enfrentada (meio; ou resultado com excludente)
- [ ] Cada alegação de culpa da inicial rebatida com prontuário e literatura
- [ ] Nexo e complicações inerentes explicados
- [ ] Termo de consentimento e orientações pós-operatórias juntados
- [ ] Danos impugnados item a item
- [ ] Quesitos e assistente técnico
- [ ] Juros e correção pelo núcleo

## Erros a evitar
- Negar o fato sem explicar a técnica: a contestação deve ensinar o juiz e o perito.
- Defender cirurgia estética como "obrigação de meio" sem enfrentar a jurisprudência de resultado.
- Omitir faltas do paciente aos retornos e descumprimento de orientações (fato da vítima).
- Juntar prontuário incompleto ou com anotações posteriores não datadas.
- Deixar de impugnar especificamente cada dano e cada fato: o que não for impugnado tende a ser presumido verdadeiro (ver `civel-contestacao`).

## Integração com o núcleo
`prazos-processuais`, `juros-e-correcao`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`; estrutura geral em `civel-contestacao`.

---
name: saude-indenizacao-erro-medico
description: >
  Redige petição inicial de ação indenizatória por erro médico contra o médico
  (e, quando couber, a clínica ou o hospital), com a distinção entre obrigação
  de meio e de resultado, culpa do profissional liberal (CDC art. 14, § 4º),
  danos dos arts. 948 a 951 do CC, perda de uma chance e dever de informação.
  Use quando o usuário pedir ação por erro médico, cirurgia malsucedida,
  cirurgia plástica estética com resultado ruim, diagnóstico tardio ou errado,
  sequela de procedimento, morte do paciente por negligência médica ou
  indenização por falta de consentimento informado.
metadata:
  area: saude
  tipo_peca: inicial
  verificado_em: 2026-11-25
---
# Indenização por erro médico

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: dano ao paciente atribuído à conduta do médico (diagnóstico, indicação, técnica cirúrgica, acompanhamento pós-operatório, prescrição, informação), em atendimento particular ou por plano de saúde.
- Falha do próprio hospital (infecção, enfermagem, equipamento, estrutura, demora de leito): `saude-responsabilidade-civil-hospitalar` — as duas teses costumam andar juntas; escolha a skill pelo réu principal e cruze os fundamentos.
- Atendimento em hospital público ou pelo SUS: a ação vai contra o ente ou a prestadora de serviço público, não contra o médico (Tema 940/STF) — `adm-responsabilidade-civil-do-estado`.
- Defesa do médico: `saude-defesa-do-medico`. Negativa de cobertura pelo plano: `consumidor-plano-de-saude`.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Linha do tempo: consultas, exames, diagnóstico, procedimento, alta, complicações, novas cirurgias — com datas.
2. Prontuário completo (pedir à instituição se ainda não tiver), laudos, receitas, termo de consentimento assinado.
3. Natureza do procedimento: estético puro, reparador, terapêutico, diagnóstico. Qual resultado foi prometido (por escrito, mensagens, fotos de "antes e depois")?
4. Quem atendeu: médico escolhido pelo paciente, plantonista, membro do corpo clínico, médico só "locatário" do centro cirúrgico.
5. Danos: despesas, perda de renda, sequela, incapacidade (parcial/total, temporária/permanente), dano estético (fotos), óbito e dependentes.
6. Parecer de médico assistente ou assistente técnico já obtido? Houve sindicância no CRM ou inquérito?
7. Data em que o paciente soube do dano e de quem o causou (termo da prescrição).

## Prazo e contagem
- Paciente consumidor contra médico/clínica particular: 5 anos do conhecimento do dano e da autoria (CDC art. 27). Registre essa data na peça.
- Atendimento em hospital privado conveniado ao SUS: prescrição quinquenal do art. 1º-C da Lei 9.494/1997, segundo o REsp 2.200.981 (3ª Turma, 2025). Contra o ente público: Decreto 20.910/1932, art. 1º.
- Se o fato também for apurado no juízo penal, avaliar o art. 200 do CC: o STJ aplicou-o para fixar o termo inicial no trânsito em julgado da sentença penal condenatória (AgInt no REsp 1.802.741, 1ª Turma, 2023).
- Prazos processuais: `prazos-processuais`.

## Estrutura da peça
Fatos com linha do tempo → relação de consumo e regime de culpa (CDC 14 § 4º) → meio x resultado → culpa (negligência, imprudência, imperícia) e/ou violação do dever de informação → nexo causal (ou perda de uma chance) → danos por espécie → prova pericial e ônus → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Regime: médico é profissional liberal; responde com culpa (CDC art. 14, § 4º; CC art. 951). A clínica ou o hospital responde por culpa do médico preposto (CC arts. 932, III, e 933) e solidariamente (CC art. 942, parágrafo único).
- Obrigação de meio (regra): o autor prova a culpa — conduta abaixo do padrão técnico exigível. Peça a inversão do ônus (CDC art. 6º, VIII) ou a distribuição dinâmica (CPC art. 373, § 1º) por ser do médico a posse do prontuário e do conhecimento técnico.
- Obrigação de resultado (cirurgia plástica estética não reparadora): a culpa é presumida, com inversão do ônus da prova; o médico só se exime provando causa excludente (REsp 2.173.636, 4ª Turma, 2024; AREsp 2.766.520, 3ª Turma, 2025). Cirurgia mista (estética + reparadora): separar as partes do pedido.
- Nexo causal é sempre do autor, inclusive quando a responsabilidade é objetiva (AgInt no AgInt no AREsp 2.158.891, 3ª Turma, 2023). Por isso, a perícia é o centro da causa.
- Perda de uma chance: indenização da chance séria e real de cura ou sobrevida perdida pela conduta, quando não se prova que ela causou todo o dano (AgInt no REsp 1.923.907, 3ª Turma, 2023). Pedido subsidiário recomendável.
- Dever de informação: risco não informado é defeito de informação (CDC arts. 6º, III, e 14, caput); CC art. 15 veda tratamento com risco de vida sem anuência. Termo genérico não supre informação específica — tese a sustentar com prova; precedente específico não conferido [VERIFICAR: jurisprudência do STJ sobre consentimento informado].

## Fundamentos verificados
- CDC arts. 6º, III e VIII; 14, caput, §§ 1º, 3º e 4º; 27. CC arts. 15, 186, 927, 932, III, 933, 942, 948, 949, 950, 951. CPC arts. 300, 373, § 1º.
- STJ: REsp 2.173.636 e AREsp 2.766.520 (estética = resultado, culpa presumida); AgInt no REsp 1.923.907 (perda de uma chance em erro médico); AgInt no AgInt no AREsp 2.158.891 (nexo é ônus do autor); REsp 2.200.981 (prescrição quinquenal — hospital conveniado ao SUS).
- STF: Tema 940 (no serviço público, ação contra o ente, não contra o médico).
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Danos materiais: despesas de tratamento, novas cirurgias, medicamentos, deslocamentos (CC art. 949), com documentos.
- Lucros cessantes até o fim da convalescença e pensão por redução da capacidade (CC art. 950), com opção de pagamento único (parágrafo único) justificada.
- Óbito: despesas, funeral, luto e alimentos aos dependentes (CC art. 948).
- Dano moral e dano estético, em pedidos separados e valores fundamentados.
- Subsidiariamente: indenização pela perda de uma chance.
- Inversão do ônus da prova; exibição do prontuário integral; perícia médica por especialista da área; quesitos na inicial.
- Juros e correção: remeter ao núcleo `juros-e-correcao` (termo inicial depende de a relação ser contratual ou extracontratual).

## Checklist pré-protocolo
- [ ] Prontuário integral juntado (ou pedido de exibição fundamentado)
- [ ] Natureza do procedimento definida: meio, resultado ou misto
- [ ] Culpa descrita em conduta concreta (o que devia ter sido feito e não foi)
- [ ] Nexo causal explicado em linguagem técnica e apoiado em parecer
- [ ] Perda de uma chance como pedido subsidiário, se o nexo for incerto
- [ ] Polo passivo: médico, clínica/hospital (corpo clínico ou preposto), plano (rede credenciada)
- [ ] Atendimento público? Então réu é o ente (Tema 940)
- [ ] Prescrição conferida a partir da ciência do dano
- [ ] Quesitos e assistente técnico indicados
- [ ] Juros e correção remetidos ao núcleo

## Erros a evitar
- Tratar todo procedimento como obrigação de resultado: fora da estética pura, a regra é meio e a culpa precisa ser provada.
- Narrar resultado ruim sem apontar a falha técnica: insucesso não é, por si, erro.
- Processar o médico de hospital público pessoalmente (ilegitimidade — Tema 940).
- Pedir dano estético dentro do moral, sem individualizar.
- Juntar só a parte do prontuário favorável; o réu juntará o resto.
- Fixar taxa de juros na peça em vez de remeter ao núcleo.

## Integração com o núcleo
`juros-e-correcao`, `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`. Tutela de urgência para custeio de tratamento: `civel-tutela-provisoria`.

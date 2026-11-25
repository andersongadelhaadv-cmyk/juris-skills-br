---
name: amb-licenca-de-operacao-corretiva
description: >
  Redige o requerimento de licenciamento corretivo — Licença de Operação
  Corretiva (LOC) — para regularizar atividade ou empreendimento que já opera sem
  licença ambiental válida, com base nos arts. 3º, XXXII, 5º, VI, 26 e 47 da Lei
  15.190/2025 e na LC 140/2011, incluindo termo de compromisso e extinção da
  punibilidade do art. 60 da Lei 9.605/1998. Use quando o cliente operar sem
  licença ou com licença vencida, tiver sido autuado ou embargado por falta de
  licença, quiser regularizar o empreendimento espontaneamente, negociar termo
  de compromisso de regularização ou converter processo corretivo antigo ao novo
  regime.
metadata:
  area: ambiental
  tipo_peca: requerimento
  verificado_em: 2026-11-25
---
# Licença de Operação Corretiva (licenciamento corretivo)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: atividade em funcionamento sem licença válida que busca regularização pela LOC (Lei 15.190/2025, art. 26), espontaneamente ou após autuação.
- Não usar:
  - empreendimento ainda não instalado → licenciamento ordinário (LP/LI/LO ou LAU/LAC), sem LOC;
  - licença vigente com condicionante a discutir → `amb-recurso-no-licenciamento`;
  - defesa da multa ou do embargo lavrado por operar sem licença → `amb-defesa-auto-de-infracao` (pode correr em paralelo; o pedido de LOC é argumento de dosimetria e de levantamento do embargo);
  - regularização fundiária urbana → `imob-regularizacao-fundiaria-reurb`;
  - defesa criminal pelo art. 60 da Lei 9.605/1998 → plugin `penal`.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Descrição da atividade, localização, porte e potencial poluidor; enquadramento na lista do ente licenciador.
2. Desde quando opera; se havia, na data de início, exigência legal de licença (decide as medidas compensatórias do art. 26, § 4º).
3. Se operava sem licença válida **na data de publicação da Lei 15.190/2025** (requisito do art. 26, caput) — ou se iniciou depois (art. 26, § 9º).
4. Licenças anteriores, vencidas ou indeferidas; processos corretivos já em curso (art. 26, § 6º).
5. Autos de infração, embargos, inquéritos ou ações penais e civis em curso.
6. Estudos disponíveis (RCA, PCA, laudos, monitoramentos) e responsável técnico.
7. Ente competente para licenciar (LC 140/2011, arts. 7º a 9º e 13).
8. Lei e regulamento estadual/municipal sobre licenciamento corretivo.

## Prazo e contagem
- Não há prazo decadencial para pedir a LOC, mas o pedido **espontâneo** é o que dá direito à extinção da punibilidade do crime do art. 60 da Lei 9.605/1998 (art. 26, § 5º). Quanto antes, melhor; registre a data do protocolo.
- Prazo máximo de análise da LOC: 3 meses (art. 47, III). Exigências de complementação suspendem o prazo (LC 140/2011, art. 14, § 2º). Decurso sem decisão não gera licença tácita; a pedido, instaura competência supletiva (art. 47, § 3º).
- Vigência da Lei 15.190/2025: 180 dias após a publicação (art. 67).
- Prazos de recurso contra o indeferimento: lei de processo administrativo do ente (`prazos-processuais`).

## Estrutura da peça
Requerimento ao órgão licenciador → qualificação do empreendedor e do empreendimento → histórico da operação → enquadramento no art. 26 → estudos (RCA e PCA) → proposta de termo de compromisso → medidas compensatórias → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Hipótese legal:** atividade que, na data de publicação da Lei 15.190/2025, operava sem licença válida (art. 26, caput). Atividade que não se enquadre deve seguir o procedimento da sua tipologia, salvo decisão justificada da autoridade que admita a LOC — e nesse caso não há extinção da punibilidade (art. 26, § 9º).
- **Estudos:** RCA e PCA (art. 5º, § 1º, VI, conforme o art. 26). A autoridade considera estudos e licenças anteriores, no que couber (art. 26, § 8º).
- **Modalidade:** por adesão e compromisso, observado o art. 22 (art. 26, § 1º); se não couber, termo de compromisso firmado antes da emissão, coerente com o RCA e o PBA (§ 2º), com critérios, procedimentos e responsabilidades (§ 3º).
- **Medidas compensatórias:** se a atividade começou quando a lei já exigia licença, a autoridade define compensação pelos impactos da falta de licença (art. 26, § 4º).
- **Inviabilidade:** se a regularização for inviável, descomissionamento ou outra medida e recuperação ambiental, sem prejuízo das sanções (art. 26, § 7º).
- **Depois da LOC:** durante a vigência, pedir a LO nos prazos e procedimentos fixados (art. 26, § 10).
- **Efeito penal:** na LOC pedida espontaneamente, o cumprimento das exigências extingue a punibilidade do art. 60 da Lei 9.605/1998; durante o termo de compromisso, ficam suspensos processos, cumprimento de penas e prazos prescricionais (art. 26, § 5º). Coordene com o criminalista.
- **Limite:** a LOC regulariza para frente; não apaga dano nem o dever de repará-lo (STF, Tema 999) e não legitima fato consumado (Súmula 613/STJ).

## Fundamentos verificados
- Lei 15.190/2025, arts. 3º, XXXII, 5º, 26, 47, 60 e 67.
- LC 140/2011, arts. 13 e 14; Lei 6.938/1981, art. 10.
- Lei 9.605/1998, art. 60 (na remissão do art. 26, § 5º, da Lei 15.190/2025).
- Súmula 613/STJ; STF, Tema 999.
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Instauração do licenciamento corretivo e expedição da LOC.
- Reconhecimento expresso de que o pedido é espontâneo (para fins do art. 26, § 5º), com data do protocolo.
- Adesão e compromisso (§ 1º) ou celebração de termo de compromisso (§ 2º), com minuta proposta.
- Aproveitamento de estudos e licenças anteriores (§ 8º).
- Lista única de exigências de complementação (LC 140/2011, art. 14, § 1º).
- Pedido conexo, no processo sancionador: levantamento ou suspensão do embargo enquanto cumprido o termo (fundamentar no processo do auto, não presumir efeito automático).

## Checklist pré-protocolo
- [ ] Data de início da operação e situação na data de publicação da Lei 15.190/2025 documentadas
- [ ] Ente licenciador correto (LC 140/2011)
- [ ] RCA e PCA assinados por profissional habilitado, com ART
- [ ] Autos, embargos e processos penais mapeados e cliente orientado sobre o efeito do § 5º
- [ ] Minuta de termo de compromisso com cronograma exequível
- [ ] Proposta de medidas compensatórias, se o início foi sob exigência legal de licença
- [ ] Regulamento estadual/municipal do licenciamento corretivo conferido
- [ ] Situação de eventuais ações de controle de constitucionalidade contra a Lei 15.190/2025 conferida [VERIFICAR]

## Erros a evitar
- Tratar a LOC como anistia: ela não extingue multa já aplicada nem a obrigação de reparar.
- Prometer extinção da punibilidade quando o pedido não é espontâneo ou a atividade cai no § 9º.
- Assinar termo de compromisso com cronograma que o cliente não consegue cumprir (descumprimento reabre sanções e prazos).
- Protocolar no ente errado e perder a espontaneidade discutindo competência.
- Esquecer de pedir a LO durante a vigência da LOC (§ 10).

## Integração com o núcleo
`prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

---
name: trabalhista-contrato-de-trabalho
description: >
  Elabora contrato individual de trabalho regido pela CLT, escolhendo a
  modalidade (prazo indeterminado, determinado, experiência, intermitente, tempo
  parcial, teletrabalho, empregado hipersuficiente) e redigindo as cláusulas de
  função, jornada, compensação, remuneração, descontos, transferência,
  confidencialidade e extinção (CLT arts. 442-B a 452-A, 58-A, 59, 75-B, 75-C,
  444 parágrafo único, 468, 469 e 507-A). Use quando o usuário pedir contrato de
  trabalho, contrato de experiência, contrato intermitente, contrato de
  teletrabalho, minuta de admissão de empregado ou modelo de contrato CLT.
metadata:
  area: trabalhista
  tipo_peca: contrato
  verificado_em: 2026-11-25
---
# Elaboração de contrato de trabalho (CLT)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: admissão de empregado urbano ou rural regido pela CLT, em qualquer das modalidades do art. 443, com ou sem teletrabalho.
- Não usar: revisar contrato já assinado ou minuta recebida (use `trabalhista-revisao-de-contrato-de-trabalho`); contratação de prestador PJ ou autônomo (use `contratos-prestacao-de-servicos-pj` e confira o risco em `trabalhista-vinculo-de-emprego`); representante comercial (`contratos-representacao-comercial`); estágio, aprendizagem, temporário e doméstico têm lei própria — tratar à parte, com a lei específica conferida [VERIFICAR: leis especiais não conferidas nesta skill].

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Empregador (razão social, CNPJ, atividade) e empregado (qualificação, escolaridade — relevante para o art. 444 parágrafo único).
2. Função, CBO se houver, local de trabalho e se a função admite transferência.
3. Modalidade pretendida e o **motivo** (prazo determinado só nas hipóteses do art. 443 §2º).
4. Jornada (horário, intervalo, escala), forma de controle e regime de compensação desejado.
5. Salário, forma de pagamento, comissões, prêmios, benefícios e utilidades.
6. Norma coletiva aplicável à categoria (convenção ou acordo coletivo) — ela pode prevalecer sobre a lei e sobre o contrato (arts. 611-A e 611-B).
7. Teletrabalho: presencial, híbrido ou remoto; equipamentos; despesas; local de residência.
8. Necessidade de confidencialidade, propriedade intelectual, não concorrência ou arbitragem.

## Prazo e contagem
- Anotação da admissão na CTPS em até 5 dias úteis (art. 29).
- Prazo determinado: até 2 anos; experiência: até 90 dias; prorrogação uma única vez, sob pena de virar prazo indeterminado (arts. 445 e 451).
- Intermitente: convocação com pelo menos 3 dias corridos; resposta em 1 dia útil, silêncio = recusa (art. 452-A §§1º-2º).
- Prazos processuais, se houver litígio: `prazos-processuais`.

## Estrutura da peça
Qualificação → objeto e função → modalidade e prazo → local e transferência → jornada e compensação → remuneração e descontos → teletrabalho (se houver) → deveres, uniforme e conduta → confidencialidade e propriedade intelectual → extinção → disposições gerais e foro. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e escolha da modalidade
- **Empregado** é a pessoa física que presta serviço não eventual, subordinado e mediante salário (art. 3º); o contrato não afasta o vínculo se a realidade o mostrar (art. 9º).
- **Prazo determinado** só vale para serviço transitório, atividade empresarial transitória ou experiência (art. 443 §2º). Gestante tem estabilidade mesmo em contrato a prazo (Súmula 244, III, do TST).
- **Intermitente**: obrigatoriamente escrito, com valor da hora não inferior ao horário do salário mínimo nem ao dos colegas da mesma função; pagamento ao fim de cada período das parcelas do art. 452-A §6º; aeronautas excluídos (art. 443 §3º).
- **Tempo parcial**: até 30 h semanais sem extras, ou até 26 h com até 6 extras (art. 58-A).
- **Teletrabalho**: deve constar expressamente do contrato (art. 75-C); conceito no art. 75-B; volta ao presencial por ordem do empregador com transição mínima de 15 dias e aditivo (art. 75-C §2º).
- **Hipersuficiente** (diploma superior e salário igual ou superior a duas vezes o teto do RGPS): livre estipulação nas matérias do art. 611-A, com preponderância sobre o coletivo (art. 444 parágrafo único); cláusula compromissória de arbitragem possível acima de duas vezes o teto, por iniciativa ou concordância expressa do empregado (art. 507-A). Valor do teto: conferir na fonte oficial do ano, nunca de memória.

## Fundamentos verificados
- CLT arts. 2º, 3º, 9º, 29, 58-A, 59 (§§2º, 5º, 6º), 59-B, 75-B, 75-C, 442-B, 443, 444, 445, 451, 452-A, 456-A, 462 §1º, 468, 469, 507-A, 611-A, 611-B.
- Súmula 244 do TST (gestante; item III, contrato a prazo).
Detalhe em [fundamentos](references/fundamentos.md).

## Cláusulas essenciais
- Função e atribuições descritas sem engessar (cláusula de compatibilidade de tarefas), atenção ao art. 468.
- Jornada, intervalo e controle; compensação: mesmo mês por acordo individual tácito ou escrito (art. 59 §6º), banco de horas semestral por acordo individual escrito (art. 59 §5º), anual só por norma coletiva (art. 59 §2º).
- Salário-base e cada parcela variável com critério objetivo; descontos autorizados, inclusive por dano culposo, só se pactuados (art. 462 §1º).
- Transferência: cláusula explícita só vale se houver real necessidade de serviço (art. 469 §1º); prever o adicional do §3º para transferência provisória.
- Teletrabalho: regime, equipamentos, reembolso de despesas, tempo de conexão fora da jornada (art. 75-B §5º), localidade.
- Uniforme e higienização (art. 456-A).
- Confidencialidade e cessão de direitos sobre criações; não concorrência pós-contratual só com limite de tempo, território e contrapartida [VERIFICAR: requisitos jurisprudenciais não confirmados no JuriBase].
- Experiência/prazo: datas de início e término, cláusula de prorrogação única.

## Checklist pré-protocolo
- [ ] Modalidade compatível com o motivo real da contratação
- [ ] Norma coletiva da categoria lida (piso, jornada, banco de horas, benefícios)
- [ ] Salário igual ou acima do piso e do mínimo; hora do intermitente conferida
- [ ] Regime de compensação dentro do instrumento exigido pelo art. 59
- [ ] Teletrabalho expresso no contrato, com equipamentos e despesas
- [ ] Cláusula de transferência com justificativa de necessidade
- [ ] Descontos por dano previstos expressamente
- [ ] Teto do RGPS do ano conferido em fonte oficial, se hipersuficiente
- [ ] Datas e prorrogação únicas no contrato a prazo

## Erros a evitar
- Usar contrato a prazo ou de experiência para função permanente sem justificativa do art. 443 §2º.
- Prorrogar a experiência duas vezes ou somar mais de 90 dias.
- Pactuar banco de horas anual por acordo individual (exige norma coletiva).
- Copiar cláusula de "livre estipulação" para quem não é hipersuficiente.
- Chamar de autônomo quem terá subordinação e habitualidade: o art. 442-B não protege contrato que esconde vínculo (art. 9º).
- Omitir o regime de teletrabalho e depois exigir presença sem aditivo.

## Integração com o núcleo
`estilo-forense`, `fidelidade-factual`, `verificacao-de-citacoes`; valores atualizados de condenação, se o tema virar litígio, pelo `juros-e-correcao`.

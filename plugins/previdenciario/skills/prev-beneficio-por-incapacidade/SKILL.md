---
name: prev-beneficio-por-incapacidade
description: >
  Prepara ação de concessão ou restabelecimento de auxílio por incapacidade
  temporária e de aposentadoria por incapacidade permanente (Lei 8.213/1991,
  arts. 25, 26, 42 a 47 e 59 a 62), com foco em perícia, DII, DIB, carência e
  isenções. Use quando o usuário pedir auxílio-doença, aposentadoria por
  invalidez, benefício por incapacidade, alta programada, cessação indevida,
  perícia do INSS negada, quesitos de perícia ou acréscimo de 25%.
metadata:
  area: previdenciario
  tipo_peca: inicial
  verificado_em: 2026-11-01
---
# Benefícios por incapacidade (temporária e permanente)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: indeferimento por perícia contrária; cessação (alta) sem recuperação; conversão do auxílio temporário em aposentadoria por incapacidade permanente; acréscimo de 25% (art. 45).
- Incapacidade de origem ocupacional ou auxílio-acidente: ver `prev-acidentario` (competência estadual).
- Pessoa sem qualidade de segurado e de baixa renda: avaliar BPC (`prev-bpc-loas`).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Doença/lesão (CID), data de início da doença (DID) e da incapacidade (DII), com documentos médicos datados.
2. Atividade habitual detalhada (tarefas, esforço, jornada), escolaridade e idade.
3. CNIS: categoria, última contribuição, número de contribuições, períodos de desemprego.
4. Histórico de benefícios (NB, DIB, DCB) e decisão do INSS (perícia, data, motivo).
5. Pedido de prorrogação feito ou não antes da cessação.

## Prazo e contagem
- Sem decadência para concessão; prescrição quinquenal.
- Benefício cessado: requerer prorrogação no INSS antes da DCB (art. 60, §9º); da reavaliação cabe recurso ao CRPS em 30 dias (art. 60, §11).
- Benefício por análise documental: duração máxima de 30 dias (art. 60, §11-F, Lei 15.265/2025).
- Prazos processuais em dias úteis (CPC, art. 219).

## Estrutura da peça   (detalhe em [estrutura](references/estrutura.md))
1. Competência (JEF/Vara Federal) e interesse de agir (requerimento ou cessação).
2. Qualidade de segurado na DII (art. 15).
3. Carência ou isenção (arts. 25, I; 26, II; 151) e regra da reaquisição (art. 27-A).
4. Incapacidade: natureza, extensão, duração, relação com a atividade habitual.
5. Condições pessoais e sociais (TNU Súmula 47).
6. DIB pretendida e fundamentação.
7. Tutela de urgência.
8. Quesitos e pedidos.

## Requisitos e preliminares
- Qualidade de segurado: 12 meses após cessar contribuições, +12 se mais de 120 contribuições sem perda, +12 se desempregado registrado (art. 15, II e §§1º-2º).
- Carência: 12 contribuições (art. 25, I); isenta em acidente de qualquer natureza, doença profissional/do trabalho e doenças da lista (art. 26, II; art. 151). Após perda da qualidade, metade da carência (art. 27-A).
- Doença preexistente à filiação não gera direito, salvo progressão ou agravamento (arts. 42, §2º, e 59, §1º); incapacidade preexistente ao reingresso afasta o direito (TNU Súmula 53). Por isso a DII é o ponto decisivo.
- Perícia judicial: pedir especialista na doença; segurado com AIDS exige infectologista (art. 60, §16).
- Aposentadoria por incapacidade permanente: incapacidade total e insuscetível de reabilitação (art. 42); incapacidade parcial pode levar a ela à luz das condições pessoais (TNU Súmula 47).

## Fundamentos verificados   (detalhe em [fundamentos](references/fundamentos.md))
- Lei 8.213, arts. 15, 25, 26, 27-A, 42, 43, 45, 59, 60, 62, 101, 151.
- EC 103, art. 26: cálculo (60% + 2 p.p.; 100% se acidente do trabalho/doença ocupacional, §3º).
- TNU Súmulas 47, 53 e 72; STJ Súmula 576.

## Pedidos e requerimentos
- Concessão/restabelecimento do auxílio por incapacidade temporária desde a DER ou a DCB, com conversão em aposentadoria por incapacidade permanente se constatada incapacidade definitiva.
- Acréscimo de 25% se houver necessidade de assistência permanente (art. 45).
- Fixação de DCB compatível com a perícia e manutenção até reabilitação (art. 62).
- Tutela de urgência.
- Atrasados conforme `juros-e-correcao`; sem desconto dos meses trabalhados por necessidade (TNU Súmula 72).

## Checklist pré-protocolo
- [ ] DII documentada e posterior à (re)filiação.
- [ ] Qualidade de segurado calculada na DII, com prorrogações.
- [ ] Carência ou isenção demonstrada.
- [ ] Descrição da atividade habitual anexada (declaração do empregador ou do próprio segurado).
- [ ] Quesitos específicos (DID, DII, prognóstico, possibilidade de reabilitação).
- [ ] Pedido de perito especialista.
- [ ] Juros e correção remetidos ao núcleo.

## Erros a evitar
- Deixar de provar a DII: o INSS fixa a DII antes da filiação e o pedido cai.
- Pedir só auxílio temporário quando os laudos indicam incapacidade definitiva (ou vice-versa) sem pedido sucessivo.
- Não pedir prorrogação antes da DCB e depois alegar cessação indevida sem requerimento.
- Ignorar o trabalho exercido durante a incapacidade (explicar com a Súmula 72 da TNU).
- Escrever índices de correção na peça.

## Integração com o núcleo
- `juros-e-correcao` para atrasados.
- `prazos-processuais` (manifestação sobre laudo, recursos).
- `verificacao-de-citacoes` para precedentes adicionais.
- `fidelidade-factual` para datas dos laudos e do CNIS; `estilo-forense`.

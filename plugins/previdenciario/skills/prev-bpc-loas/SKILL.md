---
name: prev-bpc-loas
description: >
  Estrutura o pedido judicial de benefício de prestação continuada à pessoa com
  deficiência ou idosa de 65 anos ou mais (CF, art. 203, V; Lei 8.742/1993, arts.
  20, 20-B e 21), incluindo renda per capita igual ou inferior a 1/4 do salário
  mínimo, flexibilização do critério e estrangeiro residente. Use quando o usuário
  pedir BPC, LOAS, amparo assistencial, benefício assistencial ao idoso ou à
  pessoa com deficiência, miserabilidade, CadÚnico ou laudo social.
metadata:
  area: previdenciario
  tipo_peca: inicial
  verificado_em: 2026-11-01
---
# BPC/LOAS (pessoa com deficiência e pessoa idosa)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: indeferimento ou cessação do BPC por renda, por não reconhecimento da deficiência ou por pendência cadastral (CadÚnico, biometria).
- Não usar se houver qualidade de segurado e incapacidade: o benefício previdenciário é preferível (ver `prev-beneficio-por-incapacidade`); o BPC não gera 13º nem pensão.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Requerente: idade, deficiência (impedimento, duração, CID), nacionalidade e residência no Brasil.
2. Composição familiar exata sob o mesmo teto (art. 20, §1º) e renda de cada membro, com origem.
3. Benefícios de até 1 SM recebidos por idoso ou pessoa com deficiência do grupo (excluídos do cálculo, art. 20, §14).
4. Gastos com saúde, fraldas, alimentação especial, medicamentos não fornecidos pelo SUS (art. 20-B, III).
5. CPF, inscrição e data de atualização do CadÚnico; biometria (art. 20, §§12, 12-A e 12-B).
6. Requerimento e decisão do INSS.

## Prazo e contagem
- Sem decadência para concessão (STF Tema 313); prescrição quinquenal.
- Revisão bienal do benefício (art. 21); dispensa de reavaliação médica quando o impedimento for permanente, irreversível ou irrecuperável (art. 21, §5º, Lei 15.157/2025).
- Prazos processuais em dias úteis (CPC, art. 219).

## Estrutura da peça   (detalhe em [estrutura](references/estrutura.md))
1. Competência (JEF) e interesse de agir.
2. Requisito pessoal: idade ou deficiência (impedimento de longo prazo, mínimo 2 anos, art. 20, §§2º e 10).
3. Requisito econômico: cálculo da renda per capita com exclusões legais.
4. Flexibilização: outros meios de prova da miserabilidade.
5. Estrangeiro residente, se for o caso.
6. Provas: perícia médica e estudo social.
7. Pedidos e tutela.

## Requisitos e preliminares
- Renda: per capita IGUAL OU INFERIOR a 1/4 do salário mínimo (art. 20, §3º, redação da Lei 14.176/2021). O regulamento pode ampliar até 1/2 SM segundo os critérios do art. 20-B (art. 20, §11-A).
- O critério de 1/4 não é absoluto: STF Tema 27 (inconstitucionalidade do critério como requisito obrigatório) e STJ Tema 185 (renda é elemento objetivo; miserabilidade pode ser provada por outros meios). Lei: art. 20, §11.
- Exclusões da renda: BPC ou benefício previdenciário de até 1 SM de idoso ou pessoa com deficiência do grupo (art. 20, §14); auxílios de rompimento de barragens, estágio e aprendizagem (§9º). STF Tema 312 (omissão parcial do Estatuto da Pessoa Idosa).
- Vedada dedução não prevista em lei no cálculo da renda (art. 20, §3º-A, Lei 15.077/2024): argumentar a vulnerabilidade pelos §§11 e 11-A e pelo art. 20-B, não como "dedução".
- Estrangeiro residente no País tem direito (STF Tema 173).
- Deficiência: avaliação biopsicossocial, médica e social (art. 20, §§2º, 2º-A e 6º).

## Fundamentos verificados   (detalhe em [fundamentos](references/fundamentos.md))
- CF, art. 203, V; Lei 8.742, arts. 20, 20-B e 21.
- STF Temas 27, 312 e 173; STJ Tema 185.

## Pedidos e requerimentos
- Concessão do BPC desde a DER (ou restabelecimento desde a cessação).
- Perícia médica e estudo social por assistente social, com quesitos.
- Tutela de urgência (natureza alimentar e vulnerabilidade).
- Atrasados conforme `juros-e-correcao`.
- Gratuidade da justiça; prioridade de tramitação.

## Checklist pré-protocolo
- [ ] Grupo familiar descrito estritamente pelo art. 20, §1º (quem mora junto e é parente listado).
- [ ] Renda per capita calculada com e sem as exclusões legais.
- [ ] Prova de gastos do art. 20-B, III (receitas, notas, negativas do SUS).
- [ ] CadÚnico atualizado e biometria regular.
- [ ] Impedimento de longo prazo (2 anos) documentado.
- [ ] Per capita comparada com o salário mínimo vigente em cada data (2026: R$ 1.621,00, Decreto 12.797/2025; 1/4 = R$ 405,25).

## Erros a evitar
- Escrever "renda inferior a 1/4" (a lei vigente diz igual ou inferior).
- Incluir no grupo familiar filhos casados, avós ou parentes não listados no §1º.
- Computar BPC ou aposentadoria de 1 SM de outro idoso/deficiente do grupo.
- Tratar gastos médicos como dedução (vedada pelo §3º-A); usá-los como prova de vulnerabilidade.
- Negar o direito a estrangeiro residente.

## Integração com o núcleo
- `juros-e-correcao` para atrasados.
- `prazos-processuais`; `verificacao-de-citacoes`; `fidelidade-factual` (renda e composição familiar); `estilo-forense`.

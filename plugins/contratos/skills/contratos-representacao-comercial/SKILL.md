---
name: contratos-representacao-comercial
description: >
  Redige e revisa contrato de representação comercial autônoma regido pela Lei
  4.886/1965, com os elementos obrigatórios do art. 27, a indenização mínima de
  1/12 da alínea j, o aviso prévio do art. 34, zona e exclusividade, base de
  cálculo da comissão, vedação do del credere e registro no Conselho Regional.
  Use quando o usuário pedir contrato de representante comercial, revisão de
  minuta da representada ou do representante, cálculo de risco rescisório,
  notificação de rescisão de representação ou análise de comissões pagas a
  menor.
metadata:
  area: contratos
  tipo_peca: contrato
  verificado_em: 2026-11-25
---
# Representação comercial autônoma

Ferramenta de apoio; o advogado responsável revisa todo documento antes de assinar ou enviar.

## Quando usar / quando não usar
- Usar: pessoa física ou jurídica que, sem vínculo de emprego e de forma não eventual, intermedeia negócios mercantis por conta da representada, transmitindo propostas ou pedidos (art. 1º); contrato novo, aditivo, rescisão ou notificação.
- Não usar: agente ou distribuidor sem registro no Conselho Regional ou que tem a mercadoria à disposição (`contratos-agencia-e-distribuicao`); vendedor com subordinação, pessoalidade e controle de jornada (risco trabalhista — fora desta skill).
- Competência: a Justiça Comum julga a relação entre representante e representada que preenche os requisitos da Lei 4.886/1965 (Tema 550/STF).

## Entradas mínimas (perguntar o que faltar; nunca supor fatos)
1. Lado do cliente: representada ou representante.
2. Registro do representante no Conselho Regional (número e situação) — decisivo para a incidência da lei.
3. Produtos, zona e exclusividade (de zona e de representação).
4. Comissão: percentual, base de cálculo, momento do pagamento.
5. Prazo: determinado ou indeterminado; contratos anteriores entre as mesmas partes.
6. Histórico de comissões pagas (para o cálculo da indenização em caso de rescisão).
7. Metas, política de recusa de pedidos e de preços.
8. Se o representante tem subordinados ou subrepresentantes.

## Prazos relevantes
- Comissões pagas até o dia 15 do mês seguinte ao da liquidação da fatura (art. 32, § 1º); atrasadas sofrem correção monetária (art. 32, § 2º) — índice e juros pelo núcleo `juros-e-correcao`.
- Recusa de pedidos: 15, 30, 60 ou 120 dias, conforme a praça do comprador, se o contrato não fixar outro prazo (art. 33).
- Aviso prévio: contrato por prazo indeterminado com mais de 6 meses — mínimo de 30 dias ou pagamento de 1/3 das comissões dos 3 meses anteriores (art. 34).
- Prazo determinado prorrogado vira indeterminado (art. 27, § 2º); contrato sucedido por outro em até 6 meses também (§ 3º).
- Prescrição: 5 anos para a ação do representante (art. 44, parágrafo único); para diferenças de comissão, prazo quinquenal (AgInt no AREsp 2.452.954, 3ª Turma, 2024), e a pretensão nasce mês a mês, com o pagamento a menor (AgInt nos EDcl no REsp 1.840.797, 3ª Turma, 2024).
- Prazos judiciais: `prazos-processuais`.

## Estrutura do documento
Partes e registro → objeto e produtos → zona e exclusividade → prazo → comissão e base de cálculo → pagamento → recusa de pedidos → obrigações do representante → obrigações da representada → justa causa (arts. 35 e 36) → rescisão sem justa causa, aviso e indenização → foro. Roteiro em [estrutura](references/estrutura.md).

## Riscos e cláusulas sensíveis
- **Indenização da alínea j.** Rescisão sem justa causa pela representada: no mínimo 1/12 do total da retribuição auferida durante toda a representação (art. 27, j); a prazo certo, média mensal × metade dos meses restantes (art. 27, § 1º). Devida com o aviso prévio quando a rescisão é por culpa da representada (AgInt no AREsp 1.954.005, 3ª Turma, 2025).
- **Registro no Conselho Regional.** Para o STJ, a ausência de registro afasta o regime da Lei 4.886/1965 e atrai o Código Civil (REsp 2.230.428, 4ª Turma, 2026; REsp 2.027.337, 3ª Turma, 2023). Para a representada, exigir e arquivar o comprovante; para o representante, regularizar antes de assinar.
- **Base de cálculo.** A comissão incide sobre o valor total das mercadorias (art. 32, § 4º); é norma cogente, e a tolerância a descontos de impostos não gera supressio (REsp 2.034.962, 3ª Turma, 2023).
- **Redução da comissão.** Vedadas alterações que reduzam a média dos resultados dos últimos 6 meses (art. 32, § 7º).
- **Del credere vedado.** Não transfira ao representante o risco de inadimplência do comprador (art. 43); não há comissão se o não pagamento decorre de insolvência do comprador (art. 33).
- **Exclusividade de zona.** Não se presume (art. 31); havendo, o representante recebe comissão também pelas vendas diretas da representada na zona. Exclua expressamente contas ou canais, se for o caso.
- **Justa causa.** Use as hipóteses legais (arts. 35 e 36). Crise econômica, mesmo com recuperação judicial, não foi aceita como força maior (REsp 2.216.261, 4ª Turma, 2026).
- **Pagamento antecipado da indenização** embutido nas comissões mensais: risco de não ser aceito como quitação [VERIFICAR: posição atual do STJ].
- **Foro.** Domicílio do representante (art. 39).

## Fundamentos verificados
- Lei 4.886/1965: arts. 1º, 2º, 27 (alínea j e §§ 1º a 3º), 31, 32, 33, 34, 35, 36, 39, 43 e 44.
- CC: arts. 413, 421, 421-A e 422.
- Tema 550/STF; STJ: REsp 2.034.962, AgInt no AREsp 2.452.954, AgInt nos EDcl no REsp 1.840.797, AgInt no AREsp 1.954.005, REsp 2.230.428, REsp 2.027.337, REsp 2.130.885, REsp 2.216.261.
Detalhe em [fundamentos](references/fundamentos.md).

## Checklist antes de assinar/enviar
- [ ] Registro do representante no Conselho Regional conferido e arquivado
- [ ] Todos os elementos do art. 27 presentes, inclusive indenização da alínea j
- [ ] Zona e exclusividade expressas; exclusões nomeadas
- [ ] Base de cálculo pelo valor total das mercadorias
- [ ] Prazos de pagamento e de recusa de pedidos
- [ ] Sem cláusula del credere
- [ ] Histórico de contratos anteriores avaliado (§§ 2º e 3º do art. 27)
- [ ] Foro no domicílio do representante
- [ ] Correção e juros das comissões remetidos ao núcleo `juros-e-correcao`

## Erros a evitar
- Suceder contratos a prazo e achar que o último é a prazo certo.
- Descontar impostos da base da comissão por "costume".
- Reduzir comissão por aditivo e ignorar a média de 6 meses.
- Rescindir alegando crise financeira como força maior.
- Contratar representante sem registro e presumir a incidência da Lei 4.886/1965 (ou, do outro lado, presumir que a falta de registro elimina todo direito: as comissões contratadas seguem exigíveis — REsp 2.130.885, 3ª Turma, 2025).

## Integração com o núcleo
`prazos-processuais` (prescrição quinquenal, aviso prévio), `verificacao-de-citacoes`, `fidelidade-factual` (histórico de comissões), `estilo-forense`, `juros-e-correcao` (correção das comissões, indenização).

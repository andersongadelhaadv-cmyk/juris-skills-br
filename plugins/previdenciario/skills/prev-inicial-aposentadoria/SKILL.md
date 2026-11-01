---
name: prev-inicial-aposentadoria
description: >
  Monta a petição inicial de concessão de aposentadoria do RGPS contra o INSS,
  enquadrando o segurado na regra permanente ou nas transições da EC 103/2019
  (arts. 15 a 20) ou no direito adquirido até 13/11/2019. Use quando o usuário
  pedir ação de aposentadoria, aposentadoria por idade, por tempo de contribuição,
  regra de pontos, pedágio de 50% ou 100%, idade mínima progressiva ou
  "qual regra de transição se aplica".
metadata:
  area: previdenciario
  tipo_peca: inicial
  verificado_em: 2026-11-01
---
# Petição inicial de aposentadoria (RGPS)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: concessão de aposentadoria programada, por idade (urbana ou híbrida) ou por tempo de contribuição com base em regra de transição ou direito adquirido.
- Aposentadoria especial: ver `prev-aposentadoria-especial`. Rural/segurado especial: `prev-tempo-rural-e-segurado-especial`. Servidor público: `prev-rpps-servidor`. Revisão de benefício já concedido: `prev-revisao-de-beneficio`.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Sexo, data de nascimento e se é professor da educação básica com tempo exclusivo de magistério.
2. Data de filiação ao RGPS (antes ou depois de 13/11/2019).
3. Tempo de contribuição na data de 13/11/2019 e na DER (planilha dia a dia).
4. Requerimento administrativo: número, DER, decisão e motivo (STF Tema 350).
5. Períodos controvertidos e a prova de cada um.
6. Valor da causa estimado (atrasados + 12 vincendas) para definir JEF ou vara comum.

## Prazo e contagem
- Não há decadência para a concessão inicial (STF Tema 313); prescrição das parcelas anteriores a 5 anos do ajuizamento (Lei 8.213, art. 103, p.ú.).
- Juizado Especial Federal: até 60 salários mínimos, competência absoluta onde instalado (Lei 10.259, art. 3º, caput e §§2º e 3º).
- Prazos processuais em dias úteis (CPC, art. 219). No JEF não há prazo diferenciado para o INSS (Lei 10.259, art. 9º); na vara comum, prazo em dobro (CPC, art. 183).

## Estrutura da peça   (detalhe em [estrutura](references/estrutura.md))
1. Endereçamento (JEF ou Vara Federal; vara estadual só na competência delegada, CF art. 109, §3º).
2. Qualificação e prioridade de tramitação, se idoso.
3. Interesse de agir: requerimento e indeferimento.
4. Fatos: linha do tempo contributiva.
5. Direito: enquadramento em cada regra possível, com tabela de requisitos.
6. Períodos controvertidos e prova.
7. Cálculo da RMI e do benefício mais vantajoso.
8. Tutela de urgência ou de evidência, se cabível.
9. Pedidos, provas e valor da causa.

## Requisitos e preliminares
Regras da EC 103/2019 (texto conferido no Senado) e marcos de 2026:
- Direito adquirido (art. 3º): requisitos cumpridos até a entrada em vigor (publicação em 13/11/2019); cálculo pela lei da época.
- Pontos (art. 15): 30/35 anos de contribuição (M/H) e pontos que, em 2026, são 93 (M) e 103 (H); limite 100/105. Professor: 25/30 anos; 88/98 pontos em 2026, limite 92/100.
- Idade progressiva (art. 16): 30/35 anos de contribuição; idade em 2026 de 59 anos e 6 meses (M) e 64 anos e 6 meses (H); limite 62/65. Professor: 25/30 anos e 54a6m/59a6m em 2026, limite 57/60.
- Pedágio de 50% (art. 17): só para quem tinha mais de 28/33 anos em 13/11/2019; sem idade mínima; cálculo com fator previdenciário.
- Idade (art. 18): 62 (M, limite atingido em 2023) e 65 (H), com 15 anos de contribuição para ambos.
- Pedágio de 100% (art. 20): 57/60 anos de idade, 30/35 de contribuição e período adicional igual ao que faltava em 13/11/2019; professor 52/55 e 25/30. Renda de 100% da média (art. 26, §3º).
- Permanente (art. 19, para filiados depois de 13/11/2019): 62/65 anos e 15/20 anos de contribuição.
- Cálculo geral (art. 26): média de 100% dos salários desde 07/1994; 60% + 2 pontos por ano acima de 20 anos (H) ou 15 anos (M).
Conferir sempre os números na data exata da DER: a planilha é feita em dias (arts. 15, §2º).

## Fundamentos verificados   (detalhe em [fundamentos](references/fundamentos.md))
- EC 103/2019, arts. 3º, 15 a 20 e 26; CF, art. 201, §7º.
- Lei 8.213/1991, arts. 25, II (carência de 180), 29-A, 48, 49.
- STF Tema 350 (prévio requerimento), Tema 313 (sem decadência para concessão), Tema 334 (melhor benefício).
- TNU, Súmula 75 (CTPS).

## Pedidos e requerimentos
- Reconhecimento e averbação dos períodos controvertidos.
- Concessão da aposentadoria pela regra mais vantajosa, desde a DER, ou com reafirmação da DER, se os requisitos forem completados depois.
- Pagamento das parcelas vencidas com correção e juros conforme `juros-e-correcao` do núcleo (não escrever índice na peça sem conferir lá).
- Tutela de urgência para implantação, se houver idade avançada ou risco alimentar.
- Justiça gratuita; prioridade de tramitação; honorários (fora do JEF de 1º grau).

## Checklist pré-protocolo
- [ ] Planilha de tempo em dias em 13/11/2019 e na DER, com cada regra simulada.
- [ ] Prova do requerimento administrativo e da decisão.
- [ ] Toda a prova dos períodos foi apresentada ao INSS (Tema 350).
- [ ] Valor da causa calculado e competência (JEF x vara) definida.
- [ ] Pedido de melhor benefício e de reafirmação da DER incluído.
- [ ] Juros e correção remetidos ao núcleo.
- [ ] Teto e salário mínimo de 2026 conferidos na portaria oficial [VERIFICAR].

## Erros a evitar
- Usar números de pontos ou idade de outro ano; os acréscimos são anuais desde 01/01/2020.
- Aplicar o art. 17 a quem não tinha mais de 28/33 anos em 13/11/2019.
- Esquecer que o art. 18 não tem pedágio, mas exige idade; e que o art. 20 exige idade e pedágio.
- Pedir aposentadoria por tempo de contribuição "pura" sem direito adquirido até 13/11/2019.
- Escrever taxa de juros na peça (usar o núcleo).

## Integração com o núcleo
- `juros-e-correcao` para atrasados (obrigatório em todo pedido condenatório).
- `prazos-processuais` para prazos de réplica e recursos.
- `verificacao-de-citacoes` para todo precedente acrescentado.
- `fidelidade-factual` para conferir tempo e datas com CNIS e CTPS.
- `estilo-forense` para a redação final.

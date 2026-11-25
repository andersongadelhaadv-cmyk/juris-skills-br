---
name: amb-recurso-auto-de-infracao
description: >
  Redige o recurso administrativo contra a decisão de primeira instância que
  homologou auto de infração ambiental do IBAMA, do ICMBio ou de órgão estadual
  ou municipal do SISNAMA, com base no art. 71 da Lei 9.605/1998, nos arts. 127
  a 131 do Decreto 6.514/2008 e na Lei 9.784/1999. Use quando o cliente for
  notificado do julgamento do auto de infração, da manutenção ou majoração da
  multa, do indeferimento da conversão em serviços ambientais ou da manutenção
  do embargo, e precisar recorrer à segunda instância administrativa em 20 dias,
  pedir efeito suspensivo, reconsideração ou alegar prescrição intercorrente.
metadata:
  area: ambiental
  tipo_peca: recurso
  verificado_em: 2026-11-25
---
# Recurso administrativo contra decisão em auto de infração ambiental

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: decisão de 1ª instância no processo sancionador ambiental (homologação do auto, majoração, indeferimento de conversão, manutenção de embargo ou apreensão).
- Não usar:
  - ainda não houve julgamento → `amb-defesa-auto-de-infracao`;
  - decisão de 2ª instância (última) → via judicial: `trib-acao-anulatoria` (anulatória de débito não tributário) ou, com prova pré-constituída e prazo de 120 dias, `adm-mandado-de-seguranca`;
  - crédito já inscrito e executado → `trib-embargos-a-execucao-fiscal` ou `trib-excecao-pre-executividade-fiscal`;
  - ato do licenciamento (condicionante, indeferimento de licença) → `amb-recurso-no-licenciamento`.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Decisão recorrida na íntegra, parecer técnico e jurídico que a embasaram, e a notificação com data de ciência.
2. Defesa, alegações finais e provas já apresentadas (o que foi pedido e não apreciado).
3. Histórico completo de movimentações do processo (para prescrição intercorrente).
4. Se houve majoração: a notificação prévia do art. 123 do Decreto foi feita?
5. Se houve pedido de conversão: termos do pedido e motivo do indeferimento.
6. Prejuízo concreto da execução imediata (embargo que paralisa produção, apreensão de bem de trabalho).
7. Objetivo: reformar, anular, reduzir, converter ou ganhar tempo para regularização.

## Prazo e contagem
- 20 dias da ciência da decisão (Lei 9.605/1998, art. 71, III; Decreto 6.514/2008, art. 127). A notificação do julgamento também abre 5 dias para pagar com desconto (art. 126) — prazo curto, avise o cliente no mesmo dia.
- Recurso intempestivo, a órgão incompetente ou por ilegítimo não é conhecido (art. 131).
- Deferida a conversão, suspende-se o prazo do recurso hierárquico (art. 145, § 3º).
- Estados e municípios: conferir a lei local; a Lei 9.784/1999 (prazo geral de 10 dias, art. 59) só vale no âmbito federal e subsidiariamente.
- Contagem: `prazos-processuais`.

## Estrutura da peça
Petição de interposição à autoridade que decidiu (com pedido de reconsideração) → razões à autoridade superior: tempestividade, efeito suspensivo, síntese, preliminares, mérito, dosimetria, conversão, pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Endereçamento:** à autoridade que proferiu a decisão, que pode reconsiderar em 5 dias; se não reconsiderar, encaminha à autoridade superior, 2ª e última instância (Decreto, art. 127, §§ 1º e 2º; Lei 9.784/1999, art. 56, § 1º).
- **Efeito suspensivo:** a regra é não ter; quanto à **multa**, o recurso tem efeito suspensivo (Decreto, art. 128, § 2º). Para embargo, apreensão e demais medidas, peça expressamente, demonstrando justo receio de dano de difícil ou incerta reparação (art. 128; Lei 9.784/1999, art. 61, parágrafo único).
- **Agravamento em 2ª instância:** a autoridade superior pode confirmar, modificar, anular ou revogar (Decreto, art. 129). Se o resultado puder piorar a situação do recorrente, ele deve ser cientificado antes para se manifestar (Lei 9.784/1999, art. 64, parágrafo único). A antiga vedação de agravar em instância recursal (art. 130, § 2º, do Decreto) e a 3ª instância no CONAMA foram revogadas pelo Decreto 11.080/2022: hoje o risco de reformatio in pejus é real, e a garantia é a ciência prévia.
- **Nulidades da 1ª instância:** decisão sem motivação explícita, clara e congruente (Decreto, art. 125; Lei 9.784/1999, art. 50, § 1º); provas requeridas recusadas sem fundamentação (art. 120); majoração sem a notificação prévia de 10 dias (art. 123); falta de intimação para alegações finais (art. 122); medida administrativa não apreciada na decisão (art. 124).
- **Prescrição intercorrente:** reexamine todo o período até o recurso — inclusive o tempo em que o processo aguardou julgamento (Lei 9.873/1999, art. 1º, § 1º; STJ, REsp 2.223.324). Em processo estadual/municipal, a Lei 9.873/1999 não se aplica (AgInt no REsp 2.018.177).

## Fundamentos verificados
- Lei 9.605/1998, art. 71; Decreto 6.514/2008, arts. 120 a 131, 145 e 146.
- Lei 9.784/1999, arts. 2º, 50, 56, 59, 61, 64 e 69.
- Lei 9.873/1999, art. 1º, § 1º, e art. 1º-A; Súmula 467/STJ (prazo para executar a multa).
- Responsabilidade administrativa subjetiva (STJ, AgInt no REsp 2.240.077) e Tema repetitivo 1159 (multa sem advertência prévia é válida).
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Reconsideração pela autoridade recorrida.
- Efeito suspensivo para embargo, apreensão ou outra medida (o da multa decorre do art. 128, § 2º — requeira que conste).
- Anulação da decisão por vício de motivação ou cerceamento, com retorno à 1ª instância.
- Reconhecimento da prescrição (punitiva ou intercorrente).
- Reforma para julgar o auto insubsistente; subsidiariamente, reduzir a multa e afastar a majoração.
- Reforma do indeferimento da conversão (art. 145, § 4º), com o projeto ajustado.
- Ciência prévia de qualquer possibilidade de agravamento (Lei 9.784/1999, art. 64, parágrafo único).

## Checklist pré-protocolo
- [ ] Data da ciência e termo final dos 20 dias conferidos; prazo de 5 dias para pagamento com desconto comunicado ao cliente
- [ ] Interposição dirigida à autoridade que decidiu, com pedido de reconsideração
- [ ] Efeito suspensivo pedido para cada medida não pecuniária, com prova do dano
- [ ] Cada fundamento da decisão rebatido (o que não for atacado tende a ser mantido)
- [ ] Prescrição intercorrente recalculada até a data do recurso
- [ ] Provas da defesa recusadas sem fundamento apontadas
- [ ] Decisão do cliente sobre conversão/pagamento registrada por escrito
- [ ] Juros e correção remetidos ao núcleo

## Erros a evitar
- Repetir a defesa sem enfrentar os fundamentos da decisão.
- Esquecer de pedir efeito suspensivo para o embargo: ele segue produzindo efeito.
- Perder o prazo de 5 dias do desconto achando que corre junto com os 20 do recurso.
- Juntar documento novo sem explicar por que não veio antes (o órgão pode recusar como protelatório, art. 120).
- Tratar a 2ª instância como passo obrigatório para ir a juízo: não há exigência de esgotar a via administrativa, mas o MS não cabe contra ato sujeito a recurso com efeito suspensivo sem caução (Lei 12.016/2009, art. 5º, I) — veja `adm-mandado-de-seguranca`.
- Assinar termo de compromisso da conversão sem saber que ele implica renúncia ao recurso (art. 146, § 4º).

## Integração com o núcleo
`prazos-processuais`, `juros-e-correcao`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

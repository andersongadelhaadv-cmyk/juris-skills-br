---
name: consumidor-recurso-consumerista
description: >
  Monta as teses de mérito consumeristas de recurso inominado (Lei 9.099/1995,
  arts. 41 a 46) ou de apelação (CPC, arts. 1.009 a 1.013) em ação de consumo,
  de qualquer dos lados: relação de consumo e teoria finalista mitigada,
  inversão do ônus da prova como regra de instrução (art. 6º, VIII, do CDC),
  responsabilidade objetiva, nulidade de cláusula, dano moral (existência e
  valor) e repetição em dobro. Use quando o usuário pedir recurso contra
  sentença em ação de consumo, recurso inominado contra empresa ou consumidor,
  apelação em ação de consumo, majoração ou redução de dano moral, ou reforma
  da sentença que negou a inversão do ônus da prova.
metadata:
  area: consumidor
  tipo_peca: recurso
  verificado_em: 2026-11-25
---
# Recurso em ação de consumo (enfoque consumerista)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: recurso contra sentença em ação de consumo, quando o núcleo da controvérsia é de direito do consumidor (CDC aplicável ou não, ônus da prova, defeito do serviço, cláusula abusiva, dano moral, dobra).
- Esta skill cuida das **teses**. Forma, cabimento, preparo e efeitos ficam nas skills de processo:
  - recurso inominado e contrarrazões no JEC: `civel-juizado-especial`;
  - apelação e contrarrazões: `civel-apelacao`;
  - embargos de declaração para prequestionar: `civel-embargos-de-declaracao`;
  - recurso especial: `civel-recurso-especial`.
- Não usar: decisão interlocutória (`civel-agravo-de-instrumento`); sentença homologatória de acordo no JEC (irrecorrível — Lei 9.099/1995, art. 41).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Sentença integral e data da intimação; embargos opostos?
2. Inicial, contestação e decisões sobre prova (houve decisão de inversão do ônus? em que momento?).
3. Provas produzidas e indeferidas.
4. Lado do cliente e o que se quer reformar (capítulo por capítulo).
5. Valores: condenação, dano moral fixado, valores a restituir (simples ou em dobro).
6. Juizado ou Justiça comum; gratuidade concedida?

## Prazo e contagem
- Recurso inominado: 10 dias da ciência da sentença; preparo nas 48 horas seguintes à interposição, sem intimação, sob pena de deserção (Lei 9.099/1995, art. 42, caput e § 1º); o preparo abrange as despesas dispensadas no primeiro grau, salvo gratuidade (art. 54, parágrafo único).
- Apelação: 15 dias (CPC art. 1.003, § 5º).
- Contagem em dias úteis e feriados locais: `prazos-processuais` (obrigatório conferir).

## Estrutura da peça
Peça de interposição (pela skill processual) → razões: síntese da sentença → admissibilidade → preliminares (nulidade por inversão do ônus aplicada na sentença sem oportunidade de prova; cerceamento) → mérito capítulo a capítulo com a tese consumerista → pedido de nova decisão. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Dialeticidade: impugnar especificamente cada fundamento da sentença, sob pena de não conhecimento (CPC art. 932, III; art. 1.010, II a IV).
- Inversão do ônus é regra de instrução: aplicada só na sentença ou no acórdão, sem oportunizar prova, gera decisão surpresa e nulidade (REsp 2.165.719). Do lado do consumidor, pedir a anulação para reabrir a instrução, não só a reforma.
- Inversão não é automática: exige verossimilhança ou hipossuficiência (REsp 1.971.102). Do lado do fornecedor, atacar a falta de fundamentação da decisão que inverteu.
- Recurso inominado só tem efeito devolutivo, salvo efeito suspensivo para evitar dano irreparável (Lei 9.099/1995, art. 43): pedir fundamentadamente.
- No JEC, o recorrente vencido paga custas e honorários de 10% a 20% (art. 55): avaliar o risco com o cliente.

## Fundamentos verificados
- Lei 9.099/1995, arts. 41, 42, 43, 46, 54, parágrafo único, e 55.
- CPC arts. 932, III; 1.003, § 5º; 1.009; 1.010, II a IV; 1.013, caput e § 3º; 357, III; 373, § 1º.
- CDC arts. 2º, 3º, 6º, VIII, 14, 42, parágrafo único, 51.
- Teoria finalista mitigada (AgInt no AREsp 2.498.507); inversão como regra de instrução (REsp 2.165.719); inversão não automática (REsp 1.971.102).
- Inscrição indevida: dano moral in re ipsa e revisão do valor só se irrisório ou exorbitante no STJ (AREsp 2.786.762; AgInt no AREsp 2.226.426).
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Conhecimento e provimento para reformar (ou anular) a sentença no capítulo X.
- Anulação com retorno para instrução, quando a inversão foi aplicada como regra de julgamento.
- Julgamento imediato do mérito pela causa madura, quando cabível na apelação (CPC art. 1.013, § 3º).
- Majoração ou redução do dano moral com parâmetros concretos (gravidade, duração, conduta do fornecedor, precedentes da própria turma ou câmara confirmados).
- Repetição em dobro ou simples conforme `consumidor-repeticao-em-dobro`; juros e correção pelo núcleo `juros-e-correcao`.
- Efeito suspensivo (JEC, art. 43), quando houver dano irreparável.
- Prequestionamento explícito dos dispositivos do CDC, se houver chance de recurso especial.

## Checklist pré-protocolo
- [ ] Prazo e preparo conferidos (`prazos-processuais`; 48 horas no JEC)
- [ ] Cada fundamento da sentença impugnado especificamente
- [ ] Momento da decisão de inversão do ônus identificado nos autos
- [ ] Tese de dano moral com parâmetros, não só "valor irrisório"
- [ ] Precedentes da turma ou câmara local confirmados no JuriBase
- [ ] Risco de honorários recursais/art. 55 explicado ao cliente
- [ ] Peça de interposição feita pela skill processual

## Erros a evitar
- Repetir a inicial ou a contestação sem enfrentar a sentença.
- Pedir só a reforma quando a inversão foi aplicada na sentença: o vício é de procedimento (anulação).
- Discutir valor de dano moral em recurso especial fora das hipóteses de valor irrisório ou exorbitante.
- Esquecer o preparo do JEC, que inclui as custas dispensadas no primeiro grau.
- Citar súmula ou acórdão de turma recursal de memória: confirmar no JuriBase (`verificacao-de-citacoes`).

## Integração com o núcleo
`prazos-processuais`, `juros-e-correcao`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

---
name: prev-averbacao-tempo-de-contribuicao
description: >
  Estrutura a ação declaratória de reconhecimento e averbação de tempo de
  contribuição no RGPS (STJ Súmula 242; Lei 8.213/1991, arts. 55, 94 e 96) para
  vínculo urbano fora do CNIS, serviço militar e aluno-aprendiz, com início de
  prova material e regras de contagem recíproca. Use quando o usuário pedir
  averbação de tempo, reconhecimento de vínculo urbano sem registro no CNIS,
  CTPS antiga não computada, tempo de serviço militar obrigatório ou voluntário,
  tempo de aluno-aprendiz de escola técnica, seminarista ou ação declaratória de
  tempo de serviço para aposentadoria futura.
metadata:
  area: previdenciario
  tipo_peca: inicial
  verificado_em: 2026-11-25
---
# Averbação de tempo de contribuição (urbano, militar, aluno-aprendiz)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: o segurado quer declarar e averbar períodos antes de pedir a aposentadoria (ou junto com o pedido) — vínculo urbano em CTPS ausente do CNIS, vínculo sem anotação, serviço militar, aluno-aprendiz.
- Tempo rural ou de segurado especial: `prev-tempo-rural-e-segurado-especial`.
- Tempo especial (insalubre, perigoso) e conversão: `prev-aposentadoria-especial`.
- Contagem do tempo para aposentadoria de servidor no RPPS e CTC no ente: `prev-rpps-servidor`.
- Pedido de benefício com tempo já reconhecido: `prev-aposentadoria-por-idade-urbana` ou `prev-inicial-aposentadoria`.
- Acerto do CNIS ainda não pedido ao INSS: `prev-requerimento-administrativo`.
- Reconhecimento do vínculo contra o empregador: Justiça do Trabalho (cuidado com o STJ Tema 1188 — ver abaixo).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Cada período: datas inicial e final, empregador ou órgão, função, cidade.
2. Documentos de cada período, com data: CTPS, ficha de registro, holerites, termo de rescisão, FGTS, RAIS, declarações; certificado de reservista ou certidão das Forças Armadas; certidão da escola técnica com a forma de retribuição do aprendiz.
3. Extrato CNIS e a contagem do INSS (o que foi e o que não foi computado).
4. Se o período foi usado em outro regime (RPPS, inatividade militar remunerada).
5. Reclamatória trabalhista: houve sentença de mérito ou só acordo homologado? Quais provas havia?
6. Requerimento ao INSS (acerto do CNIS, averbação ou benefício) e a decisão.
7. Finalidade: aposentadoria no RGPS ou CTC para outro regime.

## Prazo e contagem
- Declaratória pura de tempo não tem parcelas; havendo pedido de benefício, prescrevem as parcelas vencidas há mais de 5 anos do ajuizamento (Lei 8.213, art. 103, p.ú.).
- Sem decadência para a concessão inicial (STF Tema 313).
- Contar o tempo em dias e indicar se cada período conta também como carência.
- Prazos processuais: `prazos-processuais`.

## Estrutura da peça   (detalhe em [estrutura](references/estrutura.md))
1. Competência (JEF/Vara Federal) e cabimento da declaratória (STJ Súmula 242).
2. Interesse de agir: período e documentos levados ao INSS (STF Tema 350).
3. Um tópico por período: natureza (urbano, militar, aluno-aprendiz), prova e enquadramento.
4. Tabela final: período, dias, conta para carência?, prova.
5. Pedidos de declaração e averbação (e de benefício, se for o caso).

## Requisitos e preliminares
- Cabimento: ação declaratória para reconhecimento de tempo de serviço para fins previdenciários (STJ Súmula 242).
- Prova: início de prova material contemporânea; prova exclusivamente testemunhal não basta, salvo força maior ou caso fortuito, inclusive em justificação administrativa ou judicial (art. 55, §3º).
- Urbano com CTPS: anotação sem defeito formal tem presunção relativa de veracidade, ainda que fora do CNIS (TNU Súmula 75). Juntar a CTPS inteira (sequência de anotações, contribuição sindical, férias, alterações salariais).
- Recolhimento a cargo do empregador: atraso no recolhimento não prejudica a empregada doméstica (TNU Tema 29); para o empregado em geral, o mesmo argumento se apoia na responsabilidade legal do empregador [VERIFICAR: precedente específico para empregado urbano não conferido].
- Reclamatória trabalhista: sentença homologatória de acordo só vale como início de prova se apoiada em prova material contemporânea (STJ Tema 1188). Sentença de mérito com instrução tem peso maior, mas o INSS não foi parte — juntar as provas do processo trabalhista.
- Serviço militar: conta o serviço militar, inclusive voluntário, e o alternativo do CF, art. 143, §1º, desde que não usado para inatividade remunerada nas Forças Armadas ou aposentadoria no serviço público (art. 55, I). Prova: certidão de tempo de serviço da Força.
- Contagem recíproca (art. 94): tempo de outro regime entra por certidão; não se conta tempo já usado em outro regime nem tempo público concomitante com privado (art. 96, II e III); não há contagem em dobro (art. 96, I).
- Aluno-aprendiz: exige, simultaneamente, retribuição em dinheiro ou auxílios materiais, à conta do orçamento, como contraprestação de trabalho, na execução de bens e serviços para terceiros (TNU Súmula 18 / Tema 216); retribuição à conta da União ainda que indireta (STJ, AgInt no AREsp 2.376.131). A certidão da escola deve demonstrar os quatro elementos.
- Seminarista: a TNU tem teses em sentidos diversos (Temas 66 e 355) [VERIFICAR: qual tese prevalece hoje].
- Período em que a atividade não gerava filiação obrigatória: averbação depende de indenização das contribuições (art. 55, §1º; art. 96, IV).

## Fundamentos verificados   (detalhe em [fundamentos](references/fundamentos.md))
- Lei 8.213/1991, arts. 55, I, II, §§1º e 3º; 94; 96, I a IV; 103, p.ú.
- STJ Súmula 242; STJ Tema 1188; STJ, AgInt no AREsp 2.376.131.
- TNU Súmulas 18 e 75; TNU Temas 29, 66, 216 e 355.
- STF Temas 313 e 350.

## Pedidos e requerimentos
- Declaração do tempo de contribuição de __/__/__ a __/__/__ (um item por período), na condição de __.
- Condenação do INSS a averbar os períodos no CNIS e a computá-los como tempo de contribuição (e como carência, quando cabível).
- Se houver pedido de benefício: concessão desde a DER, com atrasados pelo núcleo `juros-e-correcao`.
- Expedição de CTC, se o destino for outro regime.
- Prova testemunhal para complementar o início de prova material; exibição do processo administrativo.

## Checklist pré-protocolo
- [ ] Cada período com documento contemporâneo, datado, em nome do segurado.
- [ ] Períodos levados ao INSS antes (cópia do requerimento e da decisão).
- [ ] Militar: certidão da Força e declaração de que não houve uso em outro regime.
- [ ] Aluno-aprendiz: certidão que demonstre os quatro elementos da Súmula 18 da TNU.
- [ ] Reclamatória: provas materiais do processo trabalhista juntadas, não só o acordo.
- [ ] Tabela de dias e de carência por período.
- [ ] Se houver pedido condenatório, juros e correção remetidos ao núcleo.

## Erros a evitar
- Pedir averbação de aluno-aprendiz com certidão que só atesta matrícula.
- Juntar só o acordo trabalhista homologado.
- Pedir a contagem do serviço militar já aproveitado em inatividade ou em RPPS.
- Somar tempo público concomitante com privado para o mesmo benefício.
- Pedir averbação de período anterior à filiação obrigatória sem tratar da indenização.

## Integração com o núcleo
- `juros-e-correcao` (só se houver pedido condenatório); `prazos-processuais`; `verificacao-de-citacoes`; `fidelidade-factual` (datas e documentos por período); `estilo-forense`.

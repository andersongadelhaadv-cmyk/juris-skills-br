---
name: trib-recurso-administrativo-estadual
description: >
  Redige recurso no processo administrativo tributário estadual (ICMS, IPVA,
  ITCMD e taxas), contra decisão de primeira instância que manteve auto de
  infração, dirigido ao tribunal administrativo ou conselho de contribuintes do
  Estado, a partir das normas gerais do CTN (arts. 151, III, 208-A a 208-J e
  211-B, LC 236/2026) e da lei processual do próprio Estado, que deve ser
  conferida caso a caso. Use quando o usuário pedir recurso ordinário ou
  voluntário ao conselho de contribuintes, recurso ao tribunal de impostos e
  taxas, recurso contra decisão que manteve auto de infração de ICMS, recurso
  especial ou de revista na câmara superior estadual, ou defesa em segunda
  instância administrativa estadual.
metadata:
  area: tributario-fazenda
  tipo_peca: recurso
  verificado_em: 2026-11-25
---
# Recurso no processo administrativo tributário estadual

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: decisão de primeira instância estadual desfavorável (total ou parcial) em auto de infração ou notificação de lançamento de tributo estadual; recurso à câmara superior do órgão estadual por divergência, quando a lei local o prever.
- Não usar: impugnação inicial ao auto (`trib-defesa-administrativa-e-carf`, adaptando à lei local); processo federal no CARF (`trib-defesa-administrativa-e-carf`, `trib-recurso-especial-csrf`); via judicial (`trib-acao-anulatoria`, `trib-mandado-de-seguranca`, `trib-embargos-a-execucao-fiscal`); auto de infração não tributário (ambiental, consumerista, sanitário: `adm-recurso-contra-auto-de-infracao`, `amb-recurso-auto-de-infracao`, `consumidor-defesa-procon`).
- Esta skill é genérica de propósito: não cita nenhuma lei estadual. Antes de redigir, obtenha e leia a lei e o regimento do órgão julgador do Estado. Sem eles, não afirme prazo, efeito, alçada nem nome do recurso.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
- Estado, tributo e órgão julgador; lei do processo administrativo tributário e regimento interno vigentes, com os artigos de prazo, cabimento, efeitos, alçada e sustentação oral.
- Auto de infração, impugnação apresentada, decisão de primeira instância e prova da data da ciência (DTE estadual, postal, pessoal).
- Matérias vencidas e o que foi decidido sobre cada uma; eventual remessa necessária (recurso de ofício) da parte favorável.
- Provas já juntadas e eventual fato ou documento novo, com a razão de não ter sido apresentado antes.
- Ação judicial com o mesmo objeto; interesse em programa de parcelamento ou anistia estadual.

## Prazo e contagem
- O prazo é o da lei estadual. Leia o artigo e anote se é em dias úteis ou corridos e o termo inicial.
- O CTN, após a LC 236/2026, fixa 20 dias para recurso voluntário e para recurso especial e 5 dias para embargos, em dias úteis, com suspensão de 20/12 a 20/01 (CTN art. 208-D, II a IV, §§3º e 5º). Mas o art. 211-B dá aos Estados 2 anos para adaptar a legislação; só se o Estado não adaptar nesse prazo os arts. 208-A a 208-J passam a valer diretamente. A LC 236/2026 foi publicada em 04/09/2026.
- Consequência prática: até lá, vale a lei estadual. Se ela der prazo menor que o do CTN, protocole pelo menor; não aposte em aplicação direta do CTN antes do fim do prazo de adaptação.
- Embargos de declaração interrompem o prazo dos demais recursos pelo CTN (art. 208-C, §1º); confira se a lei estadual já prevê o mesmo.
- Use `prazos-processuais`.

## Estrutura da peça
Endereçamento → qualificação → tempestividade e cabimento → síntese do auto e da decisão → preliminares (nulidade da decisão, cerceamento, decadência) → mérito por infração → multa → pedido de diligência ou perícia, se a lei admitir → pedidos. Roteiro em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Duplo grau: o CTN o assegura como norma geral (art. 208-A) e o exige nos entes com mais de 100 mil habitantes (§1º). O recurso voluntário e a remessa necessária cabem contra a decisão de primeira instância (art. 208-C).
- Sem depósito, caução ou arrolamento como condição do recurso (Súmula Vinculante 21; Súmula 373 do STJ). Se a lei estadual exigir, impugne a exigência.
- Exigibilidade suspensa enquanto pende o recurso (CTN art. 151, III).
- Fatos e direito devem ser expostos na primeira oportunidade de manifestação (CTN art. 208-D, §7º): inovação no recurso tende a não ser conhecida; justifique o que for novo (fato superveniente, prova de contraposição, matéria de ordem pública).
- Nulidades: ato de autoridade incompetente e lançamento sem fundamentação legal são nulos; a nulidade só atinge atos dependentes; não se pronuncia se o mérito puder ser decidido a favor do contribuinte (CTN art. 208-H).
- Vinculação: súmulas vinculantes, decisões do STF e do STJ transitadas em repercussão geral ou repetitivos, controle concentrado, resolução do Senado e súmulas do próprio tribunal administrativo vinculam o julgamento (CTN art. 208-G). Use-as em favor do contribuinte.
- Ação judicial com o mesmo objeto implica renúncia ao recurso administrativo; o contribuinte deve informar (CTN art. 208-E).
- Decisão definitiva favorável ao contribuinte não pode ser revista por recurso hierárquico a Secretário ou outro agente do Executivo (CTN art. 208-C, §2º).

## Fundamentos verificados
CTN arts. 151, III, 208-A, 208-C, 208-D, 208-E, 208-G, 208-H e 211-B (LC 236/2026); Súmula Vinculante 21; Súmula 373 do STJ. Lei estadual: a conferir em cada caso. Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Conhecimento do recurso, com efeito suspensivo, e manutenção da suspensão da exigibilidade.
- Nulidade da decisão recorrida ou do lançamento; subsidiariamente, cancelamento total ou parcial da exigência; subsidiariamente, redução ou exclusão da multa.
- Diligência ou perícia com quesitos, se a lei local admitir nessa fase.
- Intimação do procurador e sustentação oral, na forma do regimento.

## Checklist pré-protocolo
- [ ] Lei estadual e regimento lidos; artigos de prazo, cabimento e efeitos anotados na peça.
- [ ] Data da ciência provada; prazo contado pela lei estadual (e pelo menor, se houver dúvida).
- [ ] Cada matéria vencida atacada; nada deixado por omissão.
- [ ] Nenhuma tese nova sem justificativa (CTN art. 208-D, §7º).
- [ ] Precedentes vinculantes e súmulas do órgão estadual conferidos na fonte oficial.
- [ ] Declaração sobre ação judicial com o mesmo objeto.
- [ ] Programas estaduais de anistia ou parcelamento avaliados com o cliente antes do protocolo.

## Erros a evitar
- Aplicar o prazo do CTN ou do Decreto 70.235 sem ler a lei estadual.
- Citar artigo de lei estadual ou súmula de conselho estadual de memória.
- Repetir a impugnação sem enfrentar os fundamentos da decisão recorrida.
- Juntar prova nova sem justificar por que não veio na impugnação.
- Ajuizar ação sobre o mesmo objeto sem alertar o cliente da renúncia ao recurso.
- Calcular multa e juros com taxa própria: use `juros-e-correcao`.

## Integração com o núcleo
- `prazos-processuais`: prazo da lei estadual e suspensão de fim de ano.
- `juros-e-correcao`: atualização do crédito e simulação de anistia.
- `verificacao-de-citacoes`: precedentes e súmulas do órgão estadual.
- `fidelidade-factual`: confronto entre o auto, a decisão e as provas.
- `estilo-forense`: revisão final.

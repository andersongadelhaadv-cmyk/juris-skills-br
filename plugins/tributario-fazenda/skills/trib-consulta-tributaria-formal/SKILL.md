---
name: trib-consulta-tributaria-formal
description: >
  Redige consulta formal à Receita Federal sobre interpretação da legislação
  tributária aplicável a fato determinado, com os requisitos de eficácia do
  Decreto 70.235/1972 (arts. 46 a 53) e o rito de instância única da Lei
  9.430/1996 (arts. 48 a 50), inclusive o recurso especial por divergência entre
  soluções de consulta. Use quando o usuário pedir consulta tributária, consulta
  fiscal formal, solução de consulta, pergunta oficial ao Fisco sobre como
  tributar uma operação, consulta sobre classificação fiscal, recurso de
  divergência contra solução de consulta, ou quiser segurança jurídica antes de
  adotar um procedimento tributário.
metadata:
  area: tributario-fazenda
  tipo_peca: requerimento
  verificado_em: 2026-11-25
---
# Consulta tributária formal (federal)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: dúvida real e específica sobre a interpretação de dispositivo da legislação tributária federal aplicável a fato determinado, já ocorrido ou a ocorrer; classificação fiscal de mercadorias; recurso especial contra solução de consulta divergente de outra sobre a mesma matéria.
- Não usar: cliente já sob procedimento fiscal ou intimado sobre o fato (a consulta será ineficaz); auto de infração lavrado (`trib-defesa-administrativa-e-carf`); pedido de restituição ou compensação; tese de inconstitucionalidade (o Fisco não a acolhe; avalie `trib-mandado-de-seguranca` ou `trib-repeticao-de-indebito`).
- Estados e Municípios: a consulta segue a lei do ente. Use esta skill só como roteiro e confira a legislação local antes de afirmar prazo ou efeito.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
- Consulente (sujeito passivo, órgão público ou entidade representativa de categoria), domicílio tributário e adesão ao Domicílio Tributário Eletrônico.
- Descrição completa e exata do fato: operação, partes, fluxo financeiro, contratos, datas, valores. A descrição incompleta torna a consulta ineficaz (Decreto 70.235 art. 52, VIII).
- Tributo envolvido (um por consulta, salvo matérias conexas, segundo a Receita Federal) e os dispositivos que geram a dúvida.
- Se há procedimento fiscal em curso, intimação recebida, decisão anterior (consulta ou litígio) ou ação judicial sobre o mesmo fato.
- Se o fato já ocorreu e se o prazo de recolhimento ainda não venceu (decisivo para multa e juros).
- Interpretação que o consulente defende, com os fundamentos.

## Prazo e contagem
- Não há prazo para consultar. O que importa é a ordem dos atos: protocolar antes de qualquer procedimento fiscal e, se possível, antes do vencimento do tributo.
- Consulta feita dentro do prazo legal de pagamento afasta os juros de mora enquanto pendente (CTN art. 161, §2º). A Receita Federal informa que a consulta eficaz, protocolada antes do vencimento, impede multa e juros de mora até o 30º dia após a ciência da solução.
- A consulta não suspende o prazo de recolhimento de tributo retido na fonte ou autolançado nem o de entrega de declaração (Decreto 70.235 art. 49). Se o consulente quiser se proteger, pague ou deposite e discuta depois.
- Proteção contra fiscalização: da apresentação até o 30º dia após a ciência da decisão, não se instaura procedimento fiscal sobre a matéria consultada (Decreto art. 48).
- Recurso especial por divergência: 30 dias da ciência da solução (Lei 9.430 art. 48, §6º) ou, para quem conhecer solução divergente da que observa, 30 dias da publicação (§10).
- Prazo para a Receita responder: a regulamentar pelo Executivo (Lei 9.430 art. 48, §15); a Receita não estima prazo. Use `prazos-processuais`.

## Estrutura da peça
Endereçamento → qualificação e DTE → declarações de eficácia → descrição do fato → dispositivos e dúvida → interpretação do consulente → quesitos objetivos → documentos. Roteiro em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Por escrito, no domicílio tributário, perante o órgão da administração do tributo (Decreto art. 47); pode ser por meio eletrônico (Lei 9.430 art. 48, §14).
- Legitimados: sujeito passivo, órgãos da administração pública e entidades representativas de categorias econômicas ou profissionais (Decreto art. 46). Consulta de entidade só protege os associados depois da ciência da decisão (art. 51).
- A consulta não produz efeito se (Decreto art. 52): desatender os arts. 46 e 47; vier de quem já foi intimado a cumprir a obrigação ou está sob procedimento fiscal sobre a matéria; o fato já tiver sido decidido em consulta ou litígio do consulente; o fato estiver disciplinado em ato normativo publicado antes ou definido em disposição literal de lei; o fato for crime ou contravenção; ou a descrição for incompleta ou inexata, salvo inexatidão escusável.
- Instância única: não cabe recurso nem pedido de reconsideração da solução ou do despacho de ineficácia (Lei 9.430 arts. 48, caput e §3º, e 49, que afasta os arts. 54 a 58 do Decreto). A única via é o recurso especial por divergência, sem efeito suspensivo (art. 48, §§5º a 7º).
- A solução observa os atos normativos vigentes (Lei 9.430 art. 48, §2º) e é publicada (§4º).
- Mudança de entendimento posterior só atinge fatos geradores ocorridos após a ciência do consulente ou a publicação da nova orientação (§12).

## Fundamentos verificados
Decreto 70.235/1972 arts. 46 a 53; Lei 9.430/1996 arts. 48 a 50; CTN art. 161, §2º; orientação oficial da Receita Federal sobre a formalização da consulta. Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Recebimento da consulta e reconhecimento de sua eficácia.
- Resposta a quesitos objetivos e fechados ("sim ou não, e por quê"), um por dispositivo.
- Confirmação da interpretação do consulente, indicada de forma expressa.
- Intimação pelo DTE.

## Checklist pré-protocolo
- [ ] Nenhum procedimento fiscal, intimação ou decisão anterior sobre o fato.
- [ ] Fato descrito por completo, com documentos; nenhuma hipótese genérica.
- [ ] Um tributo por consulta (ou conexão demonstrada).
- [ ] Dispositivos exatos e dúvida real (fato não regulado literalmente por lei ou ato normativo publicado).
- [ ] Interpretação do consulente exposta e fundamentada.
- [ ] Prazo de recolhimento ainda em aberto, se o objetivo é evitar juros e multa; tributo retido ou autolançado recolhido no prazo.
- [ ] Regulamento vigente da Receita Federal conferido (formulário, declarações, canal).
- [ ] Cliente ciente de que a resposta vincula o próprio consulente e não admite recurso, salvo divergência.

## Erros a evitar
- Consultar quando a fiscalização já começou: ineficácia e falsa sensação de proteção.
- Descrever o fato de modo vago ou favorável demais; a solução só protege o fato descrito.
- Acreditar que a consulta suspende o recolhimento de tributo retido ou autolançado.
- Usar a consulta para pedir que o Fisco deixe de aplicar lei por inconstitucionalidade.
- Pedir reconsideração da solução desfavorável: não cabe (Lei 9.430 art. 48, §3º).
- Perder os 30 dias do recurso por divergência.

## Integração com o núcleo
- `prazos-processuais`: 30 dias do recurso de divergência e 30º dia após a ciência.
- `juros-e-correcao`: efeito sobre juros e multa de mora em caso de recolhimento posterior à solução.
- `verificacao-de-citacoes`: soluções de consulta ou precedentes citados.
- `fidelidade-factual`: descrição do fato fiel aos documentos.
- `estilo-forense`: revisão final.

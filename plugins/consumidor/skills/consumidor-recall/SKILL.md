---
name: consumidor-recall
description: >
  Redige notificação e ação de obrigação de fazer (com indenização, se houver
  dano) ligadas a recall: produto que o fornecedor sabe ou deveria saber
  perigoso, dever de comunicar autoridades e consumidores e de custear os
  anúncios (CDC art. 10), responsabilidade pelo fato do produto do fabricante
  (art. 12) e do comerciante (art. 13). Use quando o usuário pedir execução de
  reparo de recall negado ou atrasado, peça de recall indisponível, acidente com
  produto chamado a recall, recall não comunicado, ou orientação ao fornecedor
  sobre o dever de chamamento.
metadata:
  area: consumidor
  tipo_peca: inicial
  verificado_em: 2026-11-25
---
# Recall e fato do produto (CDC, arts. 10, 12 e 13)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: (a) consumidor com produto convocado a recall cujo reparo é negado, atrasado ou condicionado; (b) produto perigoso no mercado sem chamamento, embora o fornecedor saiba do risco; (c) acidente com produto objeto de recall — a skill organiza a prova do conhecimento do risco e remete a indenização ao modelo próprio; (d) consultoria ao fornecedor sobre o dever do art. 10, § 1º.
- Não usar como base única para indenização por acidente de consumo: a peça indenizatória é `consumidor-acao-indenizatoria` (prazo do art. 27); esta skill fornece o capítulo do recall.
- Vício sem risco à segurança (produto não funciona): `consumidor-vicio-do-produto-ou-servico`.
- Defesa do fabricante em ação de fato do produto: `consumidor-defesa-do-fornecedor`; autuação administrativa por falta de recall: `consumidor-defesa-procon`.
- Dimensão coletiva (lote inteiro, risco difuso): `consumidor-acao-coletiva`.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Produto, marca, modelo, lote/chassi/número de série, data e local da compra, nota fiscal.
2. Existência de campanha de recall: comunicado, data, defeito descrito, risco, solução oferecida (consultar o portal oficial de recalls e guardar cópia).
3. Tentativas de agendamento ou reparo: datas, protocolos, respostas, alegação de falta de peça.
4. Houve acidente ou dano? Descrição, laudos, boletim, despesas médicas, perícia.
5. Uso do produto foi suspenso? Gastos com transporte alternativo ou locação.
6. Quem vendeu e quem fabricou/importou (identificáveis ou não — art. 13).

## Prazo e contagem
- Indenização por fato do produto: 5 anos do conhecimento do dano e da autoria (art. 27).
- Reparo do defeito em si, sem acidente: avaliar se a pretensão é de vício (decadência do art. 26) ou de cumprimento do dever do art. 10 [VERIFICAR: prazo para exigir a execução do recall não conferido em fonte oficial].
- Prazos processuais: `prazos-processuais`.

## Estrutura da peça
Fatos e documentos do recall → dever legal de não colocar e de retirar/corrigir produto perigoso (art. 10) → defeito de segurança (art. 12, § 1º) → legitimidade do fabricante e, nas hipóteses do art. 13, do comerciante → tutela de urgência para reparo → danos → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- O próprio comunicado de recall é prova do conhecimento do defeito pelo fornecedor; junte-o sempre.
- As excludentes do fabricante são as do art. 12, § 3º (não colocou no mercado; defeito inexistente; culpa exclusiva do consumidor ou de terceiro). Argumento: o recall não figura entre elas — sustentar como interpretação do texto legal, sem atribuí-la a precedente não conferido.
- Comerciante responde quando o fabricante não pode ser identificado, o produto não tem identificação clara ou o perecível foi mal conservado (art. 13); quem paga tem regresso (art. 13, p.u.).
- Consumidor que não atendeu ao chamado: a defesa alegará culpa exclusiva; prepare prova de que o comunicado não chegou ou de que o reparo foi negado.

## Fundamentos verificados
- CDC arts. 6º, I e III; 10, caput e §§ 1º a 3º; 12, caput, §§ 1º e 3º; 13; 27; 84.
- STJ, AREsp 2.712.471 (fato do produto; incêndio de veículo com recall do ABS; responsabilidade solidária e prescrição discutidas; recurso desprovido).
- TJRS, 5018947-18.2024.8.21.0001 (recall não realizado; obrigação de fazer c/c dano moral contra concessionária e fabricante).
- TJBA, RI 0019111-74.2021.8.05.0080 (recall de emissões; mera notícia do recall não gerou dano moral).
- Norma infralegal do procedimento de chamamento [VERIFICAR: portaria vigente do Ministério da Justiça não conferida em fonte oficial].
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Tutela de urgência: execução do reparo do recall em prazo certo, com multa (art. 84, §§ 3º e 4º), e, se necessário, bem substituto enquanto o produto não puder ser usado com segurança.
- Obrigação de fazer definitiva: reparo/substituição gratuitos.
- Danos materiais (transporte alternativo, despesas) e, havendo acidente, materiais, morais e estéticos — ver `consumidor-acao-indenizatoria`.
- Exibição de documentos: comunicado às autoridades, relatórios da campanha, registro do atendimento do veículo/lote.
- Inversão do ônus (art. 6º, VIII).
- Juros e correção pelo núcleo `juros-e-correcao`.

## Checklist pré-protocolo
- [ ] Comunicado de recall juntado (ou prova de que não houve, embora o risco fosse conhecido)
- [ ] Identificação do produto (lote/chassi/série) bate com a campanha
- [ ] Protocolos de agendamento e recusas documentados
- [ ] Réus corretos (fabricante/importador; comerciante só no art. 13; concessionária pela falha no serviço)
- [ ] Risco atual à segurança demonstrado para a urgência
- [ ] Prazo (art. 26 ou 27) definido conforme a causa de pedir
- [ ] Juros/correção remetidos ao núcleo

## Erros a evitar
- Pedir dano moral só porque o produto foi chamado a recall: há julgado afastando (TJBA, RI 0019111-74.2021.8.05.0080). Mostre fato concreto (recusa, privação prolongada, acidente).
- Processar só o comerciante fora das hipóteses do art. 13.
- Tratar recall como vício e perder o prazo decadencial quando a pretensão é indenizatória (art. 27).
- Omitir que o consumidor atendeu ao chamado: é o primeiro ponto da defesa.

## Integração com o núcleo
`juros-e-correcao`, `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

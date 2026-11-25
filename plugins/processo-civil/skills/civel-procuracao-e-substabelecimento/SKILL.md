---
name: civel-procuracao-e-substabelecimento
description: >
  Redige procuração judicial (ad judicia et extra) e substabelecimento, com
  ou sem reserva de poderes, e as petições de revogação, renúncia e
  regularização da representação, com base no CPC (arts. 76, 104, 105, 111,
  112, 272, §§ 2º e 5º, e 287), no Código Civil (arts. 654, 655, 667 e 692) e
  na Lei 8.906/1994 (arts. 5º, 15, § 3º, e 26). Use quando o usuário pedir
  procuração para processo, poderes especiais (transigir, receber, dar
  quitação, desistir, declarar hipossuficiência), substabelecimento com ou
  sem reserva, pedido de intimação exclusiva, renúncia ou revogação de
  mandato, ou correção de vício de representação apontado pelo juiz.
metadata:
  area: processo-civil
  tipo_peca: outro
  verificado_em: 2026-11-25
---
# Procuração judicial e substabelecimento

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: (a) procuração do cliente ao advogado ou à equipe, para o foro em geral e com poderes especiais; (b) substabelecimento com ou sem reserva; (c) pedido de intimação exclusiva em nome de advogado ou sociedade; (d) renúncia do advogado; (e) revogação pelo cliente com constituição de novo patrono; (f) juntada urgente de procuração após ato praticado sem ela (art. 104); (g) resposta a intimação para regularizar representação (art. 76).
- Não usar:
  - Procuração para negócio extrajudicial (venda de imóvel, gestão de bens): é mandato civil com poderes especiais e, conforme o ato, instrumento público — use `imob-compra-e-venda-de-imovel` ou `contratos-elaboracao-de-contrato` e confirme a forma exigida.
  - Contrato de honorários: `contratos-prestacao-de-servicos`.
  - Representação de sociedade em ato societário: `soc-*`.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Outorgante: pessoa física (qualificação completa) ou jurídica (razão social, CNPJ, quem a representa e o ato que dá esse poder — contrato social, estatuto, ata).
2. Outorgados: nome, OAB e endereço completo de cada advogado; sociedade de advogados (nome, registro na OAB, endereço) se houver.
3. Finalidade: processo específico (número) ou foro em geral; fases (conhecimento, recurso, cumprimento).
4. Poderes especiais desejados — cada um, expressamente (art. 105).
5. Assinatura: digital (certificado ou plataforma) ou física.
6. Substabelecimento: com ou sem reserva; processo; quem substabelece e a quem; se há pedido de intimação exclusiva; arranjo de honorários com o substabelecido.
7. Renúncia/revogação: data da comunicação ao cliente e prova dela; novo advogado já constituído?

## Prazo e contagem
- Ato urgente sem procuração (evitar preclusão, decadência ou prescrição): juntar o instrumento em 15 dias, prorrogáveis por igual período (art. 104, § 1º; Lei 8.906/1994, art. 5º, § 1º). Sem ratificação, o ato é ineficaz e o advogado responde por despesas e perdas e danos (§ 2º).
- Renúncia: o advogado continua a representar o mandante por 10 dias após a notificação, se necessário para evitar prejuízo (art. 112, § 1º; Lei 8.906/1994, art. 5º, § 3º).
- Revogação: o cliente constitui novo advogado no mesmo ato; não o fazendo em 15 dias, aplica-se o art. 76 (art. 111).
- Vício de representação: o juiz suspende e fixa prazo para sanar (art. 76); nos tribunais superiores, o instrumento juntado deve ter data anterior ao recurso (ver Fundamentos).
- Contagem: `prazos-processuais`.

## Estrutura da peça
Procuração: outorgante → outorgados (nome, OAB, endereço; sociedade) → poderes gerais para o foro → poderes especiais, um a um → finalidade e alcance → poder de substabelecer → local, data, assinatura. Substabelecimento: substabelecente → substabelecido → processo → com/sem reserva → pedido de intimação → assinatura. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Forma**: instrumento público ou particular assinado pela parte; assinatura digital admitida (art. 105, caput e § 1º). Particular deve indicar lugar, qualificação, data, objetivo e extensão dos poderes (art. 654, § 1º, do CC); terceiro pode exigir firma reconhecida (§ 2º).
- **Dados obrigatórios**: nome, OAB e endereço completo do advogado (art. 105, § 2º); se integrar sociedade, nome, registro e endereço dela (§ 3º). Procuração outorgada individualmente aos advogados, com indicação da sociedade (Lei 8.906/1994, art. 15, § 3º).
- **Poderes especiais** exigem cláusula específica (art. 105): receber citação, confessar, reconhecer a procedência do pedido, transigir, desistir, renunciar ao direito, receber, dar quitação, firmar compromisso e assinar declaração de hipossuficiência econômica.
- **Alcance temporal**: salvo disposição em contrário, a procuração da fase de conhecimento vale para todas as fases, inclusive o cumprimento de sentença (art. 105, § 4º).
- **Petição inicial** vem com procuração que indique os endereços eletrônico e não eletrônico do advogado (art. 287).
- **Substabelecimento**: pode ser por instrumento particular mesmo que o mandato seja público (art. 655 do CC); o substabelecido pode substabelecer, salvo vedação expressa (STJ, REsp 2.211.500). Responsabilidade do substabelecente pelo substabelecido: art. 667 do CC.
- **Mandato judicial** segue a lei processual e, supletivamente, o Código Civil (art. 692 do CC).

## Fundamentos verificados
- CPC arts. 76, 104, 105, 111, 112, 272, §§ 2º e 5º, 287.
- CC arts. 654, 655, 667, 692.
- Lei 8.906/1994, arts. 5º, 15, § 3º, 26.
- STJ: Súmula 115; EREsp 1.409.260 (intimação exclusiva desatendida = nulidade); AgInt no REsp 2.030.668; REsp 2.211.500; AREsp 2.539.473 (art. 26); AgInt no AREsp 2.504.944; AgInt no REsp 1.837.482 (revogação tácita).
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Juntada da procuração ou do substabelecimento e anotação do(s) nome(s) na autuação.
- Intimação **exclusiva** em nome do advogado ou da sociedade indicados, sob pena de nulidade (art. 272, §§ 2º e 5º) — pedido expresso, repetido em cada instância.
- Renúncia: juntada da prova da notificação ao cliente (art. 112) e pedido de exclusão do nome após os 10 dias.
- Revogação: juntada da nova procuração e exclusão dos antigos patronos.
- Regularização (art. 76): juntada do instrumento ou da cadeia completa de substabelecimentos.

## Checklist pré-protocolo
- [ ] Outorgante correto; pessoa jurídica com o ato constitutivo que prova quem assina.
- [ ] Nome, OAB e endereço completo de cada advogado; dados da sociedade, se houver.
- [ ] Poderes especiais escritos um a um, conforme a necessidade do caso.
- [ ] Data da outorga **anterior** a qualquer ato já praticado (recurso, petição).
- [ ] Cadeia de substabelecimentos completa até quem assina a peça.
- [ ] Pedido de intimação exclusiva, se desejado, feito expressamente.
- [ ] Assinatura válida (digital verificável ou física legível).

## Erros a evitar
- Procuração genérica usada para acordo, levantamento de valores ou desistência: faltam poderes especiais (art. 105).
- Recurso assinado por advogado sem procuração ou com cadeia incompleta: no STJ, a juntada posterior com data posterior ao recurso não sana (Súmula 115 e precedentes).
- Esperar nulidade de intimação feita em nome de outro advogado constituído sem ter pedido intimação exclusiva.
- Nova procuração sem ressalva de poderes: revoga tacitamente a anterior — conferir se é isso que o cliente quer.
- Substabelecido com reserva cobrar honorários diretamente do cliente sem intervenção do substabelecente (Lei 8.906/1994, art. 26).
- Renunciar sem provar a notificação ao cliente.

## Integração com o núcleo
`prazos-processuais` (15 dias do art. 104; 10 dias da renúncia; prazo do art. 76), `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`. Poderes para acordo: `civel-acordo-judicial-e-extrajudicial`.

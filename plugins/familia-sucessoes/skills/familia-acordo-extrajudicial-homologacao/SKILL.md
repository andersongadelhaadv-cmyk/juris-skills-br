---
name: familia-acordo-extrajudicial-homologacao
description: >
  Redige o termo de acordo extrajudicial de família (alimentos, guarda, convivência,
  partilha) e a petição conjunta de homologação em jurisdição voluntária (CPC arts. 515,
  III, 719 a 725, VIII; Lei 13.140/2015, art. 3º § 2º; CC arts. 840 a 849 e 1.707). Use
  quando o usuário pedir homologação de acordo de alimentos, acordo de guarda e visitas
  feito fora do processo, acordo de partilha para homologar, termo de mediação familiar
  para levar ao juiz ou acordo assinado pelos pais que precisa virar título judicial.
metadata:
  area: familia-sucessoes
  tipo_peca: requerimento
  verificado_em: 2026-11-25
---
# Acordo extrajudicial de família e pedido de homologação

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: as partes já se entenderam fora do processo sobre alimentos (filhos ou ex-cônjuge), guarda, convivência, partilha ou uso de bem comum, e querem título executivo judicial (CPC 515, III), com a homologação feita pelo juiz (CPC 725, VIII).
- Usar também para o acordo que resolve **parte** do conflito (Lei 13.140, art. 3º § 1º), deixando o resto para ação própria.
- Não usar:
  - divórcio ou dissolução de união estável consensuais com pedido de decretação: `familia-divorcio` ou `familia-uniao-estavel` (CPC 731 e 732);
  - acordo dentro de processo já em curso: petição de acordo nos próprios autos (CPC 515, II); a estrutura de cláusulas daqui serve de base;
  - partilha posterior ao divórcio sem consenso: `familia-partilha-posterior-e-sobrepartilha`;
  - litígio sobre guarda ou alimentos: `familia-guarda-e-convivencia`, `familia-acao-de-alimentos`, `familia-revisional-e-exoneracao-de-alimentos`;
  - acordo descumprido: `familia-execucao-de-alimentos`;
  - acordo sobre verbas de natureza civil ou consumerista: `consumidor-acordo-judicial`.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Partes, filhos (nome, idade, incapacidade), endereço de cada um e quem detém a guarda de fato.
2. Matéria do acordo: alimentos, guarda, convivência, partilha, uso de imóvel, despesas extraordinárias, plano de saúde, escola.
3. Alimentos: valor ou percentual, base de cálculo, data e forma de pagamento (desconto em folha, depósito, Pix), conta do credor, reajuste, 13º e férias, despesas extraordinárias e rateio.
4. Guarda e convivência: modalidade, cidade-base, calendário completo (semanas, feriados, férias, datas comemorativas), logística de entrega.
5. Partilha: bens com matrícula, Renavam, extratos; valores; reposição em dinheiro; quem assume cada dívida.
6. Houve mediação? Termo assinado por mediador? Cada parte tem advogado próprio?
7. Histórico de violência doméstica, medida protetiva vigente ou processo pendente (pergunta obrigatória).
8. Existe processo anterior sobre o mesmo tema (prevenção, revisão de acordo anterior)?

## Prazo e contagem
- Não há prazo para pedir homologação; o acordo vale entre as partes desde a assinatura, mas só a homologação forma título judicial (CPC 515, III).
- Jurisdição voluntária: decisão em 10 dias (CPC 723); MP intimado quando houver incapaz (CPC 721 e 698).
- Recurso contra a sentença e demais prazos: `prazos-processuais`.

## Estrutura da peça
Petição conjunta (ambas as partes, com advogados ou advogado comum) → qualificação → síntese da relação familiar → objeto e cláusulas do acordo (ou termo anexo) → fundamentos (autonomia, transação, interesse do filho) → pedido de homologação com remessa ao MP → pedidos acessórios (ofício ao empregador, averbação, expedição de formal). Roteiro completo em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Competência: vara de família do foro aplicável à matéria; com filho incapaz, o domicílio de quem tem a guarda (CPC 53, I, "a", por analogia). Verificar prevenção de processo anterior.
- Alimentos de filho incapaz, guarda e convivência são direitos indisponíveis, mas transigíveis no modo de exercício: o consenso **deve** ser homologado em juízo, com oitiva do MP (Lei 13.140, art. 3º § 2º). Não há escritura pública que substitua a homologação nessa parte.
- O credor pode não exercer, mas não pode renunciar aos alimentos (CC 1.707): cláusula de "renúncia" de alimentos do filho é nula; para ex-cônjuge, a renúncia expressa costuma ser aceita, mas o tema é sensível [VERIFICAR: jurisprudência atual do STJ sobre renúncia de alimentos entre ex-cônjuges].
- Transação sobre direitos patrimoniais de caráter privado (CC 841) — partilha, reposição, uso de bem — é livre entre capazes; desigualdade relevante na partilha pode configurar doação tributável (ITCMD, lei estadual).
- O juiz pode recusar homologação de acordo que contrarie a lei ou de licitude duvidosa (CPC 142; STJ, AgInt no AREsp 2.141.778, 3ª Turma, 2023). Redigir cláusulas claras e equilibradas evita a recusa e a conversão em litígio.
- Violência doméstica: com medida protetiva vigente ou indícios, não use guarda compartilhada como cláusula padrão (CC 1.584 § 2º) e avalie se a mediação é adequada; o MP intervém (CPC 698, p.ú.).

## Fundamentos verificados
CPC 53, I; 142; 487, III, "b"; 515, II e III; 698; 719 a 725, VIII; Lei 13.140/2015, arts. 3º e 20, p.ú.; CC 840, 841, 849, 1.583, 1.584, 1.694 e 1.707; STJ AgInt no AREsp 2.141.778; STJ AgInt no AREsp 2.338.512; STJ REsp 2.072.706. Detalhe em [fundamentos](references/fundamentos.md).

## Cláusulas essenciais
- [ ] Alimentos: valor ou percentual com base de cálculo definida (salário bruto menos descontos obrigatórios? incide sobre 13º, férias, PLR?), vencimento, forma e conta, reajuste por índice ou salário mínimo, despesas extraordinárias com rateio e forma de comprovação.
- [ ] Desconto em folha com ofício ao empregador e dados da fonte pagadora.
- [ ] Guarda e convivência: plano detalhado, com regra para mudança de cidade, viagens ao exterior, comunicação por vídeo.
- [ ] Partilha: relação individualizada dos bens com matrícula/registro, valor, destino de cada um, reposição, assunção de dívidas e prazo para transferências.
- [ ] Quitação recíproca **delimitada** ao objeto do acordo (evitar quitação geral que alcance bens desconhecidos).
- [ ] Multa por descumprimento de cláusula de fazer (entrega da criança, transferência de bem), sem confundir com alimentos.
- [ ] Foro, eleição de mediação prévia para conflitos futuros e responsabilidade por custas e honorários.

## Pedidos e requerimentos
- Homologação por sentença, com resolução de mérito (CPC 487, III, "b"), formando título executivo judicial (CPC 515, III).
- Intimação do MP (incapaz ou violência doméstica).
- Ofício ao empregador para desconto em folha; expedição de formal ou carta de sentença para registro da partilha.
- Gratuidade, se cabível; segredo de justiça (CPC 189, II).

## Checklist pré-protocolo
- [ ] Assinatura de ambas as partes e dos advogados; procurações com poderes para transigir.
- [ ] Certidões de nascimento dos filhos; matrículas e documentos dos bens.
- [ ] Base de cálculo dos alimentos sem ambiguidade; exemplo numérico na própria cláusula, se útil.
- [ ] Pergunta sobre violência doméstica registrada.
- [ ] Nenhuma cláusula de renúncia a alimentos do filho.
- [ ] Partilha desigual avaliada quanto ao ITCMD.
- [ ] Prevenção e processos anteriores verificados.

## Erros a evitar
- Deixar o acordo de alimentos sem homologação e depois tentar a prisão civil sem título adequado: confira, antes, qual rito o título permite em `familia-execucao-de-alimentos`.
- Base de cálculo vaga ("30% dos rendimentos") que gera discussão sobre 13º, férias e verbas rescisórias.
- Supor que o acordo de parcelamento extingue a execução: a simples homologação de parcelamento, sem renúncia, não impede a prisão civil se descumprido (STJ, AgInt no AREsp 2.338.512, 4ª Turma, 2024).
- Quitação geral e irrestrita na partilha, que impede depois a sobrepartilha de bem omitido.
- Plano de convivência genérico ("visitas livres").

## Integração com o núcleo
`prazos-processuais`, `juros-e-correcao` (reajuste e atualização de alimentos e reposições — nunca fixar taxa aqui), `verificacao-de-citacoes`, `fidelidade-factual` (valores, datas, bens), `estilo-forense`.

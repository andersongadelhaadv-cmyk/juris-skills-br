---
name: penal-defesa-no-inquerito-policial
description: >
  Organiza a atuação da defesa no inquérito policial e redige as peças da fase
  investigativa: requerimento de diligências ao delegado (CPP art. 14), razões
  e quesitos (EOAB art. 7º, XXI, "a"), manifestação contra indiciamento (Lei
  12.830/2013, art. 2º, § 6º), assistente técnico em perícia e preparo do
  cliente para o interrogatório policial. Use quando o usuário pedir defesa no
  inquérito, acompanhar depoimento na delegacia, requerer diligência ou perícia,
  apresentar versão defensiva antes da denúncia ou contestar indiciamento.
metadata:
  area: penal
  tipo_peca: requerimento
  verificado_em: 2026-11-25
---
# Defesa no inquérito policial

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: investigado (ou pessoa que pode vir a ser) em inquérito policial em curso; acompanhamento de oitiva e interrogatório; requerimento de diligências, perícia, juntada de documentos; razões e quesitos; manifestação contra indiciamento; preparação para eventual ANPP.
- Não usar:
  - só um requerimento avulso de diligência, sem a estratégia da fase — `penal-requerimento-de-diligencias-inquerito`;
  - negativa de vista ou de cópia dos autos — `penal-acesso-aos-autos-do-inquerito`;
  - investigação conduzida pelo próprio Ministério Público (PIC) — `penal-defesa-em-pic`;
  - prisão em flagrante, custódia, preventiva — `penal-liberdade-provisoria-e-relaxamento`;
  - trancamento do inquérito por falta de justa causa ou atipicidade — `penal-habeas-corpus`;
  - negociação do acordo — `penal-anpp`;
  - inquérito policial militar — `mil-defesa-criminal-militar`; crime ambiental — `amb-defesa-crime-ambiental`; crime cibernético — `digital-crime-cibernetico`.

## Entradas mínimas (perguntar o que faltar; nunca supor fatos)
1. Número do inquérito, delegacia, crime investigado e data dos fatos.
2. Condição do cliente: investigado, indiciado, testemunha, vítima; preso ou solto.
3. Se há sigilo decretado e se a defesa já teve acesso aos autos (o que foi visto).
4. Intimação recebida: data, hora, local e na condição de quê.
5. Versão do cliente, documentos e testemunhas que podem esclarecer o fato.
6. Medidas cautelares já deferidas (busca, quebra de sigilo, interceptação).
7. Se o cliente é advogado ou se houve busca em escritório (aplica-se o EOAB art. 7º, §§ 6º-A a 6º-I).
8. Antecedentes e interesse em ANPP (requisitos do CPP 28-A).

## Prazo e contagem
- O inquérito não tem prazo de defesa fixo: atue cedo, antes do relatório final.
- Prazos de conclusão (CPP 10 e leis especiais) e prazos do juiz das garantias: `prazos-processuais`.
- Intimação para oitiva: compareça com o cliente ou peça redesignação fundamentada por escrito antes da data.

## Estrutura da peça
Requerimento ao delegado: qualificação e procuração → síntese do fato investigado → versão defensiva (sem confissão) → diligências requeridas, cada uma com pertinência → quesitos e assistente técnico → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Procuração: dispensada para examinar autos sem sigilo; exigida se houver sigilo (EOAB 7º § 10).
- Diligências: o investigado pode requerer qualquer diligência, mas a autoridade decide (CPP 14). Fundamente a pertinência de cada uma e registre o pedido por escrito; o indeferimento vira fundamento para pedir ao juiz das garantias ou ao MP.
- Assistente técnico em perícia: pedido ao juiz das garantias (CPP 3º-B, XVI).
- Direito ao silêncio e assistência de advogado (CF 5º LXIII). O advogado tem o direito de assistir o cliente no interrogatório e no depoimento, sob pena de nulidade absoluta desse ato e dos derivados (EOAB 7º, XXI, incluído pela Lei 13.245/2016).
- A Lei 14.365/2022 não alterou o inciso XXI; ela trata, na fase investigativa, da busca em escritório de advocacia (EOAB 7º, §§ 6º-A a 6º-I) e criou a suspensão de prazos de fim de ano (CPP 798-A).
- Confissão e ANPP: o STJ, no Tema 1303, considerou inidônea a recusa de ANPP fundada na falta de confissão no inquérito e admitiu que a confissão seja feita perante o MP. Oriente o cliente antes de qualquer interrogatório.
- Vícios do inquérito, em regra, não anulam a ação penal (STJ, AgRg no RHC 210.434). Atue para produzir prova útil, não para colecionar nulidades.

## Fundamentos verificados
- CF 5º LV e LXIII.
- CPP 3º-B, XV e XVI; 6º; 14; 20; 155.
- EOAB (Lei 8.906/1994) 7º, XIV, XXI e "a", §§ 10, 11 e 12; §§ 6º-A a 6º-I (Lei 14.365/2022).
- Lei 12.830/2013, art. 2º, § 6º (indiciamento privativo do delegado, por ato fundamentado).
- Lei 13.869/2019, art. 32 (negar acesso aos autos é crime).
- STJ: Tema 1303 (ANPP e confissão no inquérito); AgRg no RHC 210.434 (vícios do inquérito); AgRg no HC 984.153 (ausência de advogado na lavratura do flagrante); AgRg no Inq 1.534 (indeferimento de diligência complementar).
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Juntada de procuração, documentos e versão escrita do investigado.
- Diligências específicas (oitiva de testemunhas, requisição de imagens, perícias, extratos), cada uma com prazo de preservação quando houver risco de perda (ex.: imagens de câmera).
- Quesitos e indicação de assistente técnico.
- Que a oitiva do cliente ocorra com a presença do advogado, com cópia do termo.
- Não indiciamento, ou indiciamento fundamentado nos termos da Lei 12.830/2013, art. 2º, § 6º.
- Remessa do requerimento indeferido ao MP e ao juiz das garantias.

## Checklist pré-protocolo
- [ ] Procuração juntada (obrigatória se houver sigilo)
- [ ] Versão defensiva sem confissão e sem fato que o cliente não confirmou
- [ ] Cada diligência com pertinência e urgência justificadas
- [ ] Quesitos objetivos e assistente técnico indicado
- [ ] Cliente orientado sobre silêncio e sobre o Tema 1303 (ANPP)
- [ ] Protocolo com recibo ou registro no sistema da polícia
- [ ] Prazos conferidos em `prazos-processuais`

## Erros a evitar
- Levar o cliente ao interrogatório sem ter lido os autos acessíveis.
- Narrar fatos que o cliente não confirmou ou que o incriminam.
- Requerer diligências genéricas: serão indeferidas sem consequência.
- Apostar em nulidade do inquérito para derrubar a ação penal.
- Pedido verbal sem registro: o indeferimento verbal não deixa rastro para o juiz das garantias.
- Atribuir o inciso XXI do art. 7º do EOAB à Lei 14.365/2022 (a origem é a Lei 13.245/2016).

## Integração com o núcleo
`prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`, `roteador-de-pecas`.

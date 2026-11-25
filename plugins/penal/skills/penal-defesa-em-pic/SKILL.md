---
name: penal-defesa-em-pic
description: >
  Organiza a defesa no procedimento investigatório criminal (PIC) conduzido pelo
  Ministério Público e redige as peças dessa fase: manifestação e informações do
  investigado (Res. CNMP 181/2017, art. 9º), requerimento de diligências,
  controle de prazo (art. 13), impugnação de excesso ou de ato sujeito à reserva
  de jurisdição e pedido de arquivamento (art. 19), à luz do Tema 184 do STF.
  Use quando o usuário receber notificação do MP para depor, for investigado em
  PIC, quiser apresentar versão ao promotor ou procurador, pedir arquivamento ou
  contestar investigação do MP sem prazo ou sem controle.
metadata:
  area: penal
  tipo_peca: requerimento
  verificado_em: 2026-11-25
---
# Defesa em procedimento investigatório criminal (PIC) do Ministério Público

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: PIC instaurado por portaria do MP; notificação para depor ou prestar informações; pedido de diligência ao membro do MP; manifestação pelo arquivamento; controle de prazo e de atos que exigem ordem judicial.
- Não usar:
  - investigação conduzida pela polícia — `penal-defesa-no-inquerito-policial`;
  - só a negativa de vista ou cópia — `penal-acesso-aos-autos-do-inquerito`;
  - proposta ou negociação de acordo — `penal-anpp`;
  - trancamento por falta de justa causa ou constrangimento à liberdade — `penal-habeas-corpus`;
  - inquérito civil ou ação de improbidade — `adm-defesa-em-improbidade`;
  - procedimento do MP Eleitoral sobre ilícito eleitoral não criminal — `eleitoral-*`.

## Entradas mínimas (perguntar o que faltar; nunca supor fatos)
1. Portaria de instauração: data, fatos delimitados, membro e unidade do MP.
2. Notificação recebida: data, antecedência (mínimo de 48 h, salvo urgência — art. 7º § 4º da Res. 181), condição (investigado ou testemunha), se menciona o fato e a faculdade de defensor (art. 7º § 5º).
3. Prorrogações já feitas e se foram fundamentadas (art. 13).
4. Diligências realizadas e se alguma dependia de ordem judicial (quebra de sigilo, busca, interceptação).
5. Se houve comunicação ao juiz das garantias ou ao juízo competente (CPP 3º-B, IV).
6. Versão do cliente, documentos e testemunhas.
7. Antecedentes e interesse em ANPP.

## Prazo e contagem
- Conclusão do PIC: 90 dias, com prorrogações sucessivas por igual período, por decisão fundamentada do membro (Res. 181, art. 13). Confira se cada prorrogação tem fundamentação concreta.
- O STF exige investigação do MP "por prazo razoável" (Tema 184). Prorrogação genérica ou PIC aberto há anos sem diligência útil é fundamento de controle judicial.
- Prazos de manifestação e eventual habeas corpus: `prazos-processuais`.

## Estrutura da peça
Manifestação ao membro do MP: qualificação e procuração → síntese dos fatos da portaria → questões preliminares (atribuição, prazo, reserva de jurisdição, comunicação ao juiz) → informações do investigado (art. 9º) → diligências requeridas → pedido de arquivamento ou de diligências. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Base do poder investigatório: o MP pode investigar por autoridade própria e por prazo razoável, respeitando direitos do investigado, reserva de jurisdição e prerrogativas do advogado, sob controle jurisdicional dos atos documentados (STF, Tema 184).
- Atribuição: PIC apura infração penal de iniciativa pública e é presidido por membro com atribuição criminal (Res. 181, art. 1º). Fato de ação privada ou membro sem atribuição é preliminar.
- Reserva de jurisdição: quebra de sigilo bancário, fiscal, telefônico, busca domiciliar e interceptação dependem de ordem judicial. Diligência dessa natureza sem decisão é prova ilícita (CF 5º LVI; CPP 157).
- Direitos do investigado no PIC: apresentar informações com defensor (art. 9º); defensor examina os autos (art. 9º § 1º; procuração se houver sigilo, § 2º); acesso amplo ao que já está documentado (art. 21, parágrafo único).
- Arquivamento: promovido fundamentadamente pelo membro e apresentado ao juízo ou ao órgão superior interno (art. 19 e § 1º).
- A Res. 181 consultada é a compilada até a Res. 201/2019. Ela não incorpora, no texto, o regime atual do CPP 28 nem eventuais efeitos de julgamentos posteriores do STF sobre o PIC [VERIFICAR: versão vigente no CNMP e decisões do STF sobre comunicação do PIC ao juiz e prazos].

## Fundamentos verificados
- CF 5º LV, LVI e LXIII; CF 129, I, VI, VII e VIII.
- CPP 3º-B, IV (juiz das garantias informado da instauração de qualquer investigação); 28-A; 157.
- Resolução CNMP 181/2017, arts. 1º, 3º, 7º (§§ 1º, 4º e 5º), 9º, 13, 16, 19 e 21.
- EOAB 7º, XIV e XXI.
- STF, Tema 184 (RE 593.727).
- STJ, Tema 1303 (confissão para ANPP pode ser feita perante o MP; recusa por falta de confissão no inquérito é inidônea).
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Juntada de procuração e acesso integral ao que estiver documentado.
- Recebimento das informações escritas do investigado (art. 9º), ou registro da opção pelo silêncio.
- Diligências específicas, com pertinência.
- Reconhecimento de excesso de prazo ou de falta de fundamentação nas prorrogações, com conclusão ou arquivamento.
- Desentranhamento de elemento colhido sem ordem judicial, quando exigida.
- Arquivamento fundamentado (art. 19), com ciência ao juízo competente.
- Subsidiário: análise de ANPP, se cabível (`penal-anpp`).

## Checklist pré-protocolo
- [ ] Portaria e todas as prorrogações lidas e datadas
- [ ] Atribuição do membro e natureza da ação penal conferidas
- [ ] Diligências sujeitas à reserva de jurisdição identificadas, com ou sem ordem judicial
- [ ] Comunicação ao juízo/juiz das garantias conferida
- [ ] Versão do cliente sem confissão e sem fato não confirmado
- [ ] Procuração juntada (obrigatória se houver sigilo)
- [ ] Prazos conferidos em `prazos-processuais`

## Erros a evitar
- Tratar o PIC como ilegítimo em si: o STF reconhece o poder investigatório do MP (Tema 184). Ataque o excesso concreto.
- Confessar no PIC apenas para viabilizar ANPP sem orientação: a confissão do art. 28-A pode ser feita no momento do acordo (Tema 1303).
- Ignorar as prorrogações: a falta de fundamentação concreta é o argumento mais forte de controle.
- Aplicar ao PIC regras do inquérito policial sem conferir a Res. 181 e a remissão ao CPP (art. 21).

## Integração com o núcleo
`prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`, `roteador-de-pecas`.

---
name: digital-resposta-a-titular-de-dados
description: >
  Redige a resposta do controlador a requisição de titular de dados pessoais
  (confirmação, acesso, correção, eliminação, portabilidade, informação sobre
  compartilhamento, revogação de consentimento, oposição e revisão de decisão
  automatizada), com base nos arts. 17 a 22 da LGPD e nos prazos do art. 19.
  Use quando o usuário receber pedido de titular, e-mail ao encarregado/DPO,
  reclamação encaminhada pela ANPD ou pelo Procon sobre dados, ou quando o
  titular quiser formular o próprio requerimento ao controlador.
metadata:
  area: digital
  tipo_peca: outro
  verificado_em: 2026-11-25
---
# Resposta a requisição de titular de dados

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: resposta formal do controlador a qualquer direito do art. 18 ou do art. 20; também o requerimento do titular ao controlador (roteiro inverso em [estrutura](references/estrutura.md)).
- Não usar: incidente de segurança que exige comunicação coletiva (`digital-notificacao-de-incidente-lgpd`); ação judicial de reparação (`digital-indenizacao-por-vazamento-de-dados`); retirada de conteúdo publicado por terceiro em plataforma (`digital-remocao-de-conteudo`); cadastro de crédito e escore (`consumidor-negativacao-indevida`); redação de política de privacidade (`digital-politica-de-privacidade-e-termos-de-uso`).

## Entradas mínimas (perguntar o que faltar; nunca supor fatos)
1. Cópia do pedido, data de recebimento e canal (o prazo do art. 19, II, conta do requerimento).
2. Direito exercido (art. 18, I a IX; art. 20) — pedido genérico deve ser enquadrado e, se preciso, esclarecido com o titular.
3. Quem pede: o próprio titular ou representante legalmente constituído (art. 18, § 3º)? Como foi confirmada a identidade?
4. O cliente é o controlador? Se não for, quem é (art. 18, § 4º, I)?
5. Mapa dos dados do titular: origem, finalidade, base legal, critérios, compartilhamentos, prazo de guarda, transferência internacional.
6. Há obrigação legal ou outro motivo do art. 16 para manter os dados?
7. Decisão automatizada envolvida (crédito, perfil, score interno)?
8. O cliente é agente de pequeno porte elegível (Res. CD/ANPD 2/2022, arts. 3º, 14 e 15)?

## Prazo e contagem
- **Confirmação ou acesso simplificado:** imediato (LGPD art. 19, I). Pequeno porte: até 15 dias do requerimento (Res. 2/2022, art. 15).
- **Declaração clara e completa** (origem, inexistência de registro, critérios, finalidade): até **15 dias** do requerimento (art. 19, II). Pequeno porte elegível: em dobro (Res. 2/2022, art. 14, III).
- **Demais direitos do art. 18:** sem custo, "nos prazos e nos termos previstos em regulamento" (art. 18, § 5º). Regulamento geral da ANPD sobre direitos dos titulares não conferido nesta skill [VERIFICAR: conferir em gov.br/anpd se já editado]. Na falta, responder no mesmo prazo de 15 dias é a prática prudente. Pequeno porte: dobro (Res. 2/2022, art. 14, I).
- **Cópia das cláusulas de transferência internacional:** 15 dias (Res. CD/ANPD 19/2024, anexo I, art. 17, § 1º).
- A ANPD pode fixar prazos setoriais (art. 19, § 4º). Prazos processuais, se judicializar: `prazos-processuais`.

## Estrutura da peça
Identificação do pedido → enquadramento no direito exercido → resposta de mérito (atendimento, atendimento parcial ou impossibilidade fundamentada) → providências adotadas e comunicadas a terceiros → canais e direito de petição à ANPD e ao consumidor. Roteiro por direito em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Gratuidade:** o atendimento é sem custo para o titular (art. 18, § 5º).
- **Impossibilidade imediata:** responder dizendo que não é agente de tratamento (indicando quem é, quando possível) ou as razões de fato ou de direito que impedem a providência (art. 18, § 4º).
- **Eliminação:** pode ser recusada quando a conservação se apoia no art. 16 (obrigação legal, pesquisa, transferência lícita, uso exclusivo anonimizado); diga qual hipótese e por quanto tempo.
- **Compartilhamento:** depois de corrigir, eliminar, anonimizar ou bloquear, informar os agentes com quem houve compartilhamento, salvo impossibilidade ou esforço desproporcional (art. 18, § 6º).
- **Portabilidade:** observa segredo comercial e não inclui dados já anonimizados (art. 18, V e § 7º).
- **Decisão automatizada:** informar critérios e procedimentos, ressalvado segredo; negar com base em segredo autoriza auditoria da ANPD (art. 20, §§ 1º e 2º).
- **Não retaliar:** dados do exercício regular de direitos não podem ser usados contra o titular (art. 21).
- **Identidade:** confirmar antes de entregar dados, com exigência proporcional; entregar dados a terceiro errado é, ele próprio, incidente.
- **Incidente de segurança não afasta o dever de informar:** o STJ manteve a obrigação de informar compartilhamentos (art. 18, VII) e de fornecer declaração completa e cópia dos dados (art. 19, II) após vazamento atribuído a ataque hacker (REsp 2.147.374).

## Fundamentos verificados
- LGPD: arts. 9º, 16, 17, 18, 19, 20, 21, 22, 41 (encarregado recebe reclamações).
- Res. CD/ANPD 2/2022, arts. 3º, 14 e 15; Res. CD/ANPD 19/2024, anexo I, art. 17.
- STJ, REsp 2.147.374 (3ª Turma, julg. 03/12/2024).
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
Na resposta do controlador, deixar expresso:
- O que foi atendido, em que data e por qual meio seguro (art. 19, § 2º).
- O que não foi atendido e o fundamento legal específico.
- Os terceiros comunicados (art. 18, § 6º).
- O canal do encarregado e o direito de petição à ANPD e aos órgãos de defesa do consumidor (art. 18, §§ 1º e 8º).

## Checklist pré-protocolo
- [ ] Data do requerimento registrada e prazo calculado
- [ ] Direito exercido identificado inciso por inciso
- [ ] Identidade ou representação conferida, com documentação guardada
- [ ] Mapa de dados do titular levantado com TI e áreas de negócio
- [ ] Toda recusa com fundamento legal específico (arts. 16, 18 § 4º, 20 § 1º)
- [ ] Terceiros comunicados após correção ou eliminação
- [ ] Linguagem clara; sem cobrança
- [ ] Resposta e prova de envio arquivadas

## Erros a evitar
- Responder "seus dados estão seguros" sem dizer quais dados, de onde vieram e para que servem.
- Recusar eliminação de forma genérica, sem indicar a hipótese do art. 16.
- Cobrar taxa ou exigir cadastro novo para atender.
- Exigir documentação excessiva que, na prática, impede o exercício do direito.
- Tratar o pedido como reclamação comum de SAC e perder o prazo de 15 dias.
- Afirmar que o vazamento por hacker dispensa o dever de informação (REsp 2.147.374).

## Integração com o núcleo
`prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

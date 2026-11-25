---
name: saude-rescisao-unilateral-plano-de-saude
description: >
  Redige ação de restabelecimento de plano de saúde cancelado unilateralmente
  pela operadora, com tutela de urgência, com base no art. 13, parágrafo único,
  II e III, da Lei 9.656/1998 (plano individual: só fraude ou inadimplência de
  mais de 60 dias com notificação até o 50º dia) e nos Temas 1047 e 1082 do STJ
  (planos coletivos). Use quando o usuário pedir reativação do plano cancelado,
  cancelamento por atraso sem notificação, cancelamento depois de a operadora
  aceitar pagamento, rescisão por suposta fraude ou doença preexistente,
  cancelamento durante internação ou resilição de plano coletivo empresarial
  pequeno ou por adesão.
metadata:
  area: saude
  tipo_peca: inicial
  verificado_em: 2026-11-25
---
# Cancelamento unilateral do plano de saúde — ação de restabelecimento

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: a operadora **cancelou ou suspendeu o contrato** e o beneficiário quer voltar a ter o plano (com ou sem indenização): inadimplência sem notificação válida; cancelamento após aceitar pagamento ou renegociar; alegação de fraude sem prova; cancelamento durante internação; resilição de coletivo empresarial com menos de 30 vidas sem motivação; resilição de coletivo sem aviso prévio.
- Não usar: o contrato está ativo e o problema é negativa de procedimento (`consumidor-plano-de-saude`); o plano coletivo foi cancelado e o único objetivo é **manter um tratamento em curso até a alta** (Tema 1082 já está operacionalizado em `consumidor-plano-de-saude`; aqui ele entra como pedido subsidiário); manutenção do ex-empregado ou aposentado no plano da empresa (arts. 30 e 31 da Lei 9.656/1998: tese própria, adaptar com cuidado); defesa da operadora (`consumidor-defesa-do-fornecedor`); notificação prévia (`saude-notificacao-extrajudicial-plano-de-saude`).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Tipo de contrato: **individual/familiar**, coletivo por adesão, coletivo empresarial (quantas vidas?), autogestão. Data de adesão e de cancelamento.
2. Motivo informado pela operadora e o documento do cancelamento.
3. Inadimplência: meses em atraso nos **últimos 12 meses** (consecutivos ou não), datas de vencimento e pagamento, extrato.
4. Notificação: houve? Por qual meio, para qual endereço, em que dia da inadimplência, com AR? Quem recebeu?
5. Depois da notificação, a operadora emitiu boleto, recebeu mensalidade ou renegociou? Comprovantes.
6. Alguém está **internado** ou em tratamento contínuo? Relatório médico.
7. Fraude/doença preexistente alegada: declaração de saúde, perícia, processo administrativo na ANS.
8. Coletivo: estipulante, contrato coletivo, aviso de resilição, motivação apresentada, oferta de migração ou portabilidade.

## Prazo e contagem
- Urgência: com internação ou tratamento em curso, a peça é de tutela (CPC, art. 300) para restabelecer em horas/dias.
- Teste aritmético do art. 13, p.ú., II: (a) mais de **60 dias** de não pagamento, consecutivos ou não, **nos últimos 12 meses**; (b) notificação comprovada **até o 50º dia** de inadimplência. Faltando qualquer um, o cancelamento de plano individual é irregular. Faça a conta dia a dia, com as datas reais.
- Prescrição de indenização por cancelamento indevido: conferir com `verificacao-de-citacoes` [VERIFICAR: prazo específico para cancelamento indevido não conferido]. Prazos processuais: `prazos-processuais`.

## Estrutura da peça
Tutela de urgência em destaque → tipo de contrato → regra aplicável (individual: art. 13; coletivo: contrato + Temas 1047/1082) → vício do cancelamento → boa-fé (pagamento aceito) → urgência → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Individual/familiar:** a rescisão unilateral é vedada, salvo fraude ou inadimplência qualificada com notificação até o 50º dia (art. 13, p.ú., II); e é vedada **em qualquer hipótese durante a internação do titular** (art. 13, p.ú., III).
- **Notificação:** a lei não exige notificação pessoal; carta com AR no endereço do titular foi considerada válida (REsp 1.995.100; AREsp 2.704.018). O ataque eficaz é outro: notificação ausente, tardia (depois do 50º dia), para endereço errado ou sem prova de entrega.
- **Comportamento contraditório:** renegociar ou receber mensalidade depois da notificação mantém o contrato (REsp 1.995.100; REsp 2.217.087). Junte os boletos e comprovantes posteriores.
- **Fraude:** exige prova robusta da operadora (REsp 2.216.966).
- **Coletivos:** o art. 13, p.ú., não se aplica; a resilição imotivada é admitida após 12 meses de vigência e com notificação prévia (REsp 1.866.598; AgInt no REsp 1.830.974, que menciona antecedência mínima de 60 dias). Exceções: coletivo empresarial com menos de 30 beneficiários exige **motivação idônea** (Tema 1047, REsp 1.856.311, julg. 05/03/2026); e, mesmo na resilição regular, a operadora mantém os cuidados de quem está internado ou em tratamento essencial até a alta, se o titular pagar a mensalidade integral (Tema 1082, REsp 1.842.751).
- Oferta de plano individual após cancelar o coletivo: há julgados negando a obrigação quando a operadora não comercializa a modalidade (AgInt no AgInt no AREsp 2.017.300; REsp 1.833.615) e julgados admitindo a migração (REsp 2.216.966). Pedir como subsidiário, com prova de que a operadora vende plano individual.
- Autogestão: retirar fundamentos de CDC.

## Fundamentos verificados
- Lei 9.656/1998, art. 13, caput e parágrafo único, I, II e III; arts. 30 e 31 (só para distinguir).
- CDC, arts. 6º, VIII, 47 e 51, IV e XI; CPC, art. 300.
- STJ: REsp 1.995.100; AREsp 2.704.018; REsp 2.217.087; REsp 2.216.966; REsp 1.866.598; AgInt no REsp 1.830.974; Tema 1047 (REsp 1.856.311); Tema 1082 (REsp 1.842.751); REsp 1.988.124 (coletivo: dever de notificar os beneficiários).
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Tutela de urgência: restabelecimento imediato do contrato nas mesmas condições (carências cumpridas, mesma rede e segmentação), sob multa diária, com autorização do depósito das mensalidades vencidas e vincendas.
- Declaração de nulidade do cancelamento e manutenção definitiva do contrato.
- Subsidiariamente: continuidade do tratamento até a alta (Tema 1082) e/ou oferta de plano individual compatível, sem novas carências.
- Reembolso de despesas pagas no período sem cobertura (ver `saude-reembolso-plano-de-saude`) e dano moral com fatos concretos.
- Juros e correção: `juros-e-correcao`.

## Checklist pré-protocolo
- [ ] Tipo de contrato e número de vidas (coletivo empresarial) identificados
- [ ] Conta dos 60 dias nos últimos 12 meses feita com datas reais
- [ ] Data da notificação x 50º dia de atraso conferida
- [ ] Prova de pagamento ou renegociação posterior à notificação juntada
- [ ] Internação ou tratamento em curso documentado
- [ ] Mensalidades depositadas ou oferecidas
- [ ] Pedido subsidiário (Tema 1082 / migração) incluído
- [ ] Multa e prazo de cumprimento propostos

## Erros a evitar
- Aplicar o art. 13, p.ú., II a plano coletivo, ou tratar coletivo empresarial pequeno como se fosse coletivo comum.
- Alegar só "falta de notificação pessoal" quando houve carta com AR no endereço correto.
- Pedir restabelecimento sem oferecer o pagamento das mensalidades em aberto.
- Esquecer o art. 13, p.ú., III quando o titular estava internado na data do cancelamento.
- Pedir migração para plano individual como direito automático.

## Integração com o núcleo
`juros-e-correcao`, `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

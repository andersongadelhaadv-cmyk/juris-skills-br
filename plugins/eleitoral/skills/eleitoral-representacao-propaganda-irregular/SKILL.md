---
name: eleitoral-representacao-propaganda-irregular
description: >
  Redige representação por propaganda eleitoral irregular pelo rito sumário
  do art. 96 da Lei 9.504/1997 (defesa em 48 horas, recurso em 24 horas), e a
  defesa do representado. Use quando o usuário pedir representação por
  propaganda antecipada, propaganda em bem público, anonimato ou ataque na
  internet, pedido de remoção de conteúdo eleitoral, multa por propaganda
  irregular, ou precisar defender candidato ou partido representado por
  propaganda.
metadata:
  area: eleitoral
  tipo_peca: inicial
  verificado_em: 2026-11-25
---
# Representação por propaganda irregular (art. 96)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: (a) propaganda antes de 15 de agosto com pedido explícito de voto (Lei 9.504/1997, arts. 36 e 36-A); (b) propaganda em bem público ou de uso comum (art. 37); (c) anonimato ou ataque na internet (art. 57-D); (d) demais descumprimentos da Lei 9.504/1997 sem rito próprio; (e) defesa do representado nesses casos.
- Não usar: propaganda que caracteriza abuso de poder ou uso indevido dos meios de comunicação com gravidade — `eleitoral-aije`; captação ilícita de sufrágio (art. 41-A) e conduta vedada (art. 73) seguem o rito do art. 22 da LC 64/1990 — `eleitoral-aije` / `eleitoral-defesa-abuso-de-poder`; recurso da decisão — `eleitoral-recurso-eleitoral`; ofensa pessoal fora do contexto eleitoral — `digital-ofensas-em-redes-sociais`; remoção de conteúdo não eleitoral — `digital-remocao-de-conteudo`.

## Entradas mínimas (perguntar o que faltar; nunca supor fatos)
1. Eleição, cargo e circunscrição (define o juízo — art. 96, I a III).
2. Quem fez a propaganda, quem se beneficiou e prova do prévio conhecimento do beneficiário.
3. Prova preservada: URL, captura com data/hora, ata notarial, fotos com localização, cópia do material.
4. Data do fato (antes ou depois de 15 de agosto) e conteúdo literal (há pedido explícito de voto?).
5. Pedido pretendido: remoção, cessação, restauração do bem, multa.
6. Para a defesa: data da notificação e se houve retirada espontânea.

## Prazo e contagem
- Defesa: 48 horas da notificação (art. 96, § 5º).
- Decisão: 24 horas após o prazo de defesa (art. 96, § 7º).
- Recurso: 24 horas da publicação; contrarrazões em igual prazo da notificação (art. 96, § 8º). Julgamento do recurso: 48 horas (art. 96, § 9º).
- Prazo em horas: conferir forma de contagem e funcionamento do cartório em período eleitoral em `prazos-processuais` e na resolução do pleito [VERIFICAR: resolução do TSE sobre representações, no site do TSE].

## Estrutura da peça
Endereçamento → legitimidade → fatos com prova → dispositivo violado → responsabilidade do autor e do beneficiário → tutela de remoção/cessação → pedidos. Defesa: preliminares → atipicidade → ausência de prévio conhecimento → retirada → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Legitimidade: partido, coligação ou candidato (art. 96, caput); a ação deles não impede a do MP (art. 96-B, § 1º).
- Competência: juiz eleitoral (municipal), TRE (federal, estadual, distrital) ou TSE (presidencial) — art. 96, I a III; juízes auxiliares nos tribunais (§ 3º).
- A inicial relata fatos e indica provas, indícios e circunstâncias (§ 1º).
- Ações sobre o mesmo fato são reunidas no juízo da primeira; com trânsito em julgado anterior, a nova não é conhecida salvo prova nova (art. 96-B, caput e §§ 2º e 3º).
- Sanção ao candidato não se estende ao partido sem prova de participação (art. 96, § 11).
- Juiz sem iniciativa de ofício para impor multa: [VERIFICAR: Súmula 18 do TSE — JuriBase sem cobertura do TSE].

## Fundamentos verificados
- Lei 9.504/1997: art. 96 (rito), art. 96-B (reunião de ações), art. 36 e § 3º (propaganda só após 15 de agosto; multa de R$ 5.000 a R$ 25.000 ou o custo, se maior), art. 36-A (sem pedido explícito de voto não há propaganda antecipada), art. 37 e § 1º (bens públicos; restauração e multa de R$ 2.000 a R$ 8.000), art. 57-D (anonimato vedado na internet; multa de R$ 5.000 a R$ 30.000; remoção de ataques).
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Liminar de remoção/cessação/recolhimento, com indicação precisa (URL, endereço, peça).
- Notificação do representado para defesa em 48 horas.
- Procedência com multa no patamar legal fundamentado e, no art. 37, restauração do bem.
- Intimação do MP Eleitoral.
- Defesa: improcedência; subsidiariamente, multa no mínimo; afastamento do beneficiário sem prévio conhecimento.

## Checklist pré-protocolo
- [ ] Juízo competente pelo tipo de eleição
- [ ] Prova do conteúdo com data e autoria (URL específica, não só o perfil)
- [ ] Pedido explícito de voto demonstrado (se propaganda antecipada)
- [ ] Prévio conhecimento do beneficiário provado ou pedido só contra o autor
- [ ] Verificado se há ação anterior sobre o mesmo fato (art. 96-B)
- [ ] Prazo de 48h/24h anotado em horas

## Erros a evitar
- Tratar como propaganda antecipada a mera exaltação de pré-candidato sem pedido explícito de voto (art. 36-A).
- Pedir cassação em representação do art. 96: aqui as sanções são multa, remoção e restauração; gravidade vai para a AIJE.
- Indicar só o perfil, sem a URL da publicação: inviabiliza a remoção.
- Perder o prazo de 24 horas do recurso contando em dias.
- Estender a multa ao partido sem prova de participação (art. 96, § 11).

## Integração com o núcleo
`prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

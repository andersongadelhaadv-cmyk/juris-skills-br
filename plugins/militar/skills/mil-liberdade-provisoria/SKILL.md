---
name: mil-liberdade-provisoria
description: >
  Redige pedido de liberdade na Justiça Militar ao juiz da causa: relaxamento de
  flagrante ilegal, revogação da prisão preventiva (CPPM arts. 254 a 259),
  liberdade provisória (CPPM arts. 270 e 271) e menagem (CPPM arts. 263 a 269),
  com medidas cautelares diversas como alternativa. Use quando o usuário pedir
  soltura de militar ou civil preso por crime militar, revogação de preventiva
  na auditoria militar, concessão de menagem, liberdade provisória no CPPM ou
  substituição da prisão por cautelares em processo penal militar.
metadata:
  area: militar
  tipo_peca: requerimento
  verificado_em: 2026-11-25
---
# Liberdade provisória, revogação de preventiva e menagem (CPPM)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: primeiro pedido ao juiz natural (juiz federal da JM, juiz de direito do juízo militar ou Conselho de Justiça) para soltar o preso ou evitar a prisão.
- Não usar: pedido já negado pelo juiz e prisão mantida — `mil-habeas-corpus` ou `mil-recurso-em-sentido-estrito` (decisão sobre preventiva e menagem é recorrível: CPPM art. 516, h e i); crime comum — `penal-liberdade-provisoria-e-relaxamento`.

## Entradas mínimas (perguntar o que faltar; nunca supor fatos)
1. Auto de prisão em flagrante ou decreto de preventiva, com data e fundamentos.
2. Tipo imputado e pena máxima (decide menagem e liberdade provisória).
3. Se o crime é culposo; se está entre os tipos excluídos pelo art. 270, parágrafo único, b, do CPPM.
4. Reincidência (impede menagem — art. 269); antecedentes; fé de ofício.
5. Residência, unidade em que serve, família, trabalho; propostas de condições.
6. Andamento: IPM, denúncia, audiências (excesso de prazo).

## Prazo e contagem
- Pedido sem prazo: pode ser renovado se mudarem as circunstâncias (art. 259).
- MP opina sobre menagem em três dias (art. 264, § 1º).
- Marcos de excesso: detenção no IPM (art. 18), denúncia (art. 79), instrução (art. 390).
- Indeferimento: RESE em três dias (art. 518) — `mil-recurso-em-sentido-estrito`. Contagem: `prazos-processuais`.

## Estrutura da peça
Endereçamento → síntese da prisão → ilegalidade (relaxamento) → ausência de requisitos da preventiva → hipótese de liberdade provisória ou menagem → cautelares alternativas → pedidos. Roteiro em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Relaxamento: prisão ilegal será relaxada (CF art. 5º, LXV). Atacar primeiro a forma: flagrante inexistente, falta de comunicação ao juiz, prazo do art. 18 do CPPM excedido.
- Preventiva exige prova do fato e indícios de autoria (art. 254) e um dos casos do art. 255 (ordem pública, instrução, periculosidade, aplicação da lei penal militar, hierarquia e disciplina). Decisão fundamentada (art. 256). Não se decreta quando o juiz presume que o acusado não fugirá nem perturbará a justiça (art. 257) nem quando há excludente prevista nos dispositivos do CPM indicados no art. 258.
- Hierarquia e disciplina (art. 255, e) não se presume: exigir fato concreto que a ameace.
- Liberdade provisória: obrigatória se não houver pena privativa cominada; facultativa no crime culposo (com exceções) e na detenção até dois anos, salvo os tipos listados no art. 270, parágrafo único, b.
- Menagem: crimes com pena máxima até quatro anos, conforme natureza do crime e antecedentes (art. 263); vedada ao reincidente (art. 269); cassada se o beneficiário sair do lugar ou faltar a ato (art. 265); cessa com a sentença condenatória (art. 267). Menagem em residência ou cidade não conta na pena (art. 268).
- Cautelares diversas do CPP (art. 319): são examinadas em processos de crime militar pelo STJ (AgRg no HC 1.079.774), mas a aplicação depende da compatibilidade com o CPPM (art. 3º, a). Pedir de forma subsidiária e fundamentar.

## Fundamentos verificados
- CF art. 5º, LXV e LXVI; CPPM arts. 3º, 18, 79, 254 a 259, 263 a 271, 390, 516, h e i; CPP art. 319.
- TJMS, HC 1419260-34.2024.8.12.0000 (liberdade concedida por falta dos requisitos do art. 255 do CPPM); STJ, AgRg no HC 1.079.774 (crimes militares: cautelares diversas consideradas).
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Relaxamento da prisão ilegal, com alvará de soltura.
- Revogação da preventiva por falta de requisitos ou pela desnecessidade (arts. 257 e 259).
- Liberdade provisória (art. 270) ou menagem (art. 263), indicando o lugar (art. 264).
- Subsidiariamente, cautelares diversas, com as condições propostas.
- Ciência ao MP e comunicação à autoridade militar a que o acusado está subordinado.

## Checklist pré-protocolo
- [ ] Pena máxima conferida (menagem até quatro anos; detenção até dois anos)
- [ ] Tipo conferido contra a lista de exclusões do art. 270, parágrafo único, b
- [ ] Reincidência verificada (art. 269)
- [ ] Fundamento concreto do decreto enfrentado alínea por alínea do art. 255
- [ ] Prazos dos arts. 18, 79 e 390 calculados
- [ ] Endereço e local de menagem indicados

## Erros a evitar
- Pedir menagem para reincidente ou para crime com pena máxima acima de quatro anos.
- Copiar o regime de fiança do CPP sem conferir o CPPM: fundamente nos arts. 263 a 271 (menagem e liberdade provisória) e, subsidiariamente, nas cautelares.
- Ignorar o fundamento de hierarquia e disciplina, comum nos decretos militares.
- Ir direto ao tribunal sem pedir ao juiz da causa (supressão de instância).

## Integração com o núcleo
`prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

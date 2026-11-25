---
name: amb-defesa-acao-civil-publica
description: >
  Redige contestação do réu em ação civil pública ambiental (Lei 7.347/1985),
  enfrentando legitimidade, nexo causal, existência e extensão do dano, regime
  do Código Florestal (áreas consolidadas, art. 68, PRA), dano moral coletivo e
  inversão do ônus. Use quando o usuário for réu (empresa, produtor rural,
  proprietário, incorporadora ou município) citado em ACP do Ministério Público
  ou de associação por desmatamento, APP, reserva legal, poluição, resíduos ou
  falta de licença.
metadata:
  area: ambiental
  tipo_peca: contestacao
  verificado_em: 2026-11-25
---
# Defesa em ação civil pública ambiental

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: contestação (e manifestação sobre tutela de urgência) em ACP ambiental.
- Não usar:
  - autor da ACP: `amb-acao-civil-publica`;
  - negociar acordo antes ou durante o processo: `amb-termo-ajustamento-conduta`;
  - auto de infração administrativo: `amb-defesa-auto-de-infracao`;
  - denúncia criminal pelo mesmo fato: `amb-defesa-crime-ambiental`;
  - recurso contra liminar: `civel-agravo-de-instrumento`; contestação cível genérica: `civel-contestacao`.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Inicial completa, decisão liminar e data da citação/juntada.
2. Histórico do imóvel ou da atividade: quando adquiriu, de quem, o que já existia (fotos antigas, imagens de satélite com data).
3. Licenças, autorizações, CAR, adesão a PRA, termos de compromisso e TAC.
4. Laudo técnico próprio (ou possibilidade de contratar assistente técnico).
5. Outras ações, inquéritos ou autos de infração sobre o mesmo fato.
6. Data dos fatos frente ao marco de 22/07/2008 do Código Florestal.

## Prazo e contagem
- Contestação: CPC, art. 335 (prazo em dias úteis, dobra para Fazenda e MP) — contar com `prazos-processuais`.
- Prescrição da reparação ambiental: não alegue — a pretensão é imprescritível (Tema 999/STF). Só discuta prescrição de pedido de natureza diversa, com fundamento próprio (ex.: obrigação de TAC sem conteúdo reparatório — AREsp 1.941.907).

## Estrutura da peça
Tempestividade → preliminares → impugnação aos fatos com prova técnica → nexo causal → dano (existência, extensão, reversibilidade) → regime do Código Florestal → dano moral coletivo → ônus da prova → tutela de urgência → pedidos e provas. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Ilegitimidade ativa: associação sem pertinência temática ou sem 1 ano de constituição, sem dispensa (Lei 7.347, art. 5º, V, e § 4º).
- Competência e prevenção: foro do local do dano e prevenção por ação anterior idêntica (art. 2º e parágrafo único); conexão/litispendência com outra ACP (CPC, art. 337, VI e VIII).
- Falta de interesse: obrigação já assumida em TAC ou termo de compromisso do PRA com título executivo (Lei 7.347, art. 5º, § 6º; Lei 12.651, art. 59, § 3º).
- Ilegitimidade passiva: responsabilidade objetiva não dispensa nexo causal; demonstre ausência de vínculo com a atividade (AgInt no AREsp 2.045.914).
- Ente público: a execução contra ele é subsidiária (Súmula 652/STJ).

## Fundamentos verificados
- Lei 6.938/1981, art. 14, § 1º — responsabilidade sem culpa, mas com dano e nexo.
- Lei 12.651/2012: art. 59 (PRA; § 4º veda autuação por infrações anteriores a 22/07/2008 durante o prazo e o cumprimento do termo), art. 66 (regularização da reserva legal por recomposição, regeneração ou compensação), art. 67 (imóvel até 4 módulos fiscais), art. 68 (supressão conforme percentuais da época).
- Dano precisa ser comprovado: AgInt no AREsp 1.682.237 (STJ, 1ª T., 2023).
- Sem dano ambiental reconhecido, não há dano moral coletivo: AgInt no AREsp 2.663.902 (STJ, 2ª T., 2025); simples violação de norma não basta: AgInt no REsp 1.962.771 (STJ, 1ª T., 2023).
- Inversão do ônus não é automática e não pode impor prova diabólica: AREsp 2.836.654 (STJ, 3ª T., 2025).
- Contra o réu (conhecer para enfrentar): Súmulas 613, 618, 623 e 629/STJ; Tema 1.204/STJ; risco integral (REsp 2.102.646).
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Acolhimento das preliminares (extinção sem mérito, remessa ao juízo competente, reunião de ações).
- Improcedência por ausência de nexo ou de dano; subsidiariamente, redução do objeto à área efetivamente degradada.
- Reconhecimento do regime de área consolidada / art. 68 / art. 67, conforme o caso.
- Afastamento do dano moral coletivo ou fixação proporcional.
- Revogação ou modulação da tutela (prazo exequível, PRAD em vez de paralisação total).
- Perícia judicial, assistente técnico, quesitos; prova documental histórica (Lei 12.651, art. 68, § 1º).
- Juros/correção, se houver condenação: `juros-e-correcao`.

## Checklist pré-protocolo
- [ ] Prazo contado (dias úteis; dobro se aplicável)
- [ ] Preliminares de legitimidade, competência, conexão e interesse examinadas
- [ ] Linha do tempo do imóvel com imagens datadas (antes/depois de 22/07/2008)
- [ ] CAR, PRA, TAC, licenças juntados
- [ ] Laudo técnico contrário ou quesitos formulados
- [ ] Teses contrárias consolidadas enfrentadas, não ignoradas
- [ ] Pedido subsidiário de redução do objeto e de prazos realistas

## Erros a evitar
- Alegar prescrição da reparação ambiental ou fato consumado (Tema 999/STF; Súmula 613).
- Sustentar que a licença ou a boa-fé na compra afastam a responsabilidade civil (risco integral; Súmula 623).
- Negar o dano sem prova técnica própria e sem pedir perícia.
- Ignorar que a dispensa de recomposição pelo art. 68 exige prova de que a supressão respeitou a lei da época.
- Confundir a responsabilidade civil (objetiva) com a administrativa e a penal (subjetivas): teses de culpa servem nas outras esferas.

## Integração com o núcleo
`prazos-processuais`, `juros-e-correcao`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

---
name: trib-amicus-curiae
description: >
  Redige pedido de ingresso e manifestação como amicus curiae em causa
  tributária (CPC art. 138; arts. 983, 1.035, §4º, e 1.038, I; Lei 9.868/1999,
  art. 7º, §2º) em recurso repetitivo, repercussão geral, IRDR, ADI/ADC ou
  processo subjetivo de grande repercussão. Use quando o usuário pedir amicus
  curiae tributário, ingresso de associação, sindicato, federação ou entidade
  de classe em tema repetitivo do STJ, repercussão geral do STF ou ADI sobre
  tributo, memorial de amigo da corte ou manifestação técnica em IRDR sobre
  ICMS, ISS, PIS/Cofins ou contribuições.
metadata:
  area: tributario-fazenda
  tipo_peca: requerimento
  verificado_em: 2026-11-25
---
# Manifestação como amicus curiae em matéria tributária

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: entidade (associação, federação, sindicato, conselho, instituto técnico) ou pessoa com representatividade adequada quer contribuir com dados e argumentos em controvérsia tributária de **efeito amplo**: tema repetitivo (art. 1.038, I), repercussão geral (art. 1.035, §4º), IRDR (art. 983), ADI/ADC (Lei 9.868, art. 7º, §2º) ou causa individual de relevância, especificidade ou repercussão social (art. 138).
- O amicus **não é parte**: não defende direito próprio no caso e, em regra, não recorre.
- Não usar: quem tem interesse jurídico próprio na causa (pedido de assistência no próprio processo, ou ação própria como `trib-mandado-de-seguranca` e `trib-declaratoria-inexistencia-relacao-tributaria`); empresa que quer só ver seu caso julgado junto (pedir sobrestamento no próprio processo); recurso da parte (`trib-agravo-de-instrumento`, `civel-recurso-especial`, `civel-recurso-extraordinario`).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Processo/tema: tribunal, classe, número, relator, tema repetitivo ou de repercussão geral, fase (afetado, pautado, julgado).
2. Requerente: estatuto, finalidade institucional, abrangência (nacional, regional), número de associados, atuação prévia no tema.
3. Contribuição concreta: estudo econômico, dados setoriais, impacto arrecadatório, aspecto técnico da operação tributada, direito comparado.
4. Posição defendida (pró-contribuinte, pró-fisco ou só técnica) e eventual conflito com associados.
5. Representação: procuração da entidade e ata que autoriza o ingresso, se o estatuto exigir.

## Prazo e contagem
- Quando solicitado ou admitido, o amicus se manifesta em **15 dias** da intimação (CPC art. 138, caput).
- Pedido espontâneo: protocole o quanto antes. O STJ já não conheceu de pedido apresentado após a inclusão em pauta (AgInt no MS 25.655) e considera descabido o ingresso depois do julgamento (EDcl no AgInt no AREsp 1.615.770). Regras de pauta do regimento interno de cada tribunal: confira.
- IRDR: interessados se manifestam no prazo comum de 15 dias (art. 983). Contagem: `prazos-processuais`.

## Estrutura da peça
Petição ao relator → qualificação e representatividade → relevância, especificidade ou repercussão → contribuição útil e diferente das partes → manifestação de mérito tributário (curta e técnica) → pedidos (admissão, poderes, sustentação oral). Roteiro em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Requisitos do art. 138**: relevância da matéria, especificidade do tema ou repercussão social da controvérsia (objetivos) e **representatividade adequada** do requerente (subjetivo). Na ADI, relevância e representatividade dos postulantes (Lei 9.868, art. 7º, §2º).
- **Poderes**: definidos pelo juiz ou relator na decisão que admite (art. 138, §2º). Peça expressamente memoriais, sustentação oral e juntada de documentos.
- **Recursos**: a intervenção não autoriza recurso, salvo embargos de declaração e recurso contra o julgamento do IRDR (art. 138, §§1º e 3º). Embargos de declaração só por amicus já **admitido** (EDcl nos EAREsp 664.888).
- **Decisão sobre o ingresso é irrecorrível**: a Corte Especial do STJ assentou que não cabe agravo interno contra decisão que indefere o amicus, orientação aplicada pela Primeira Seção em matéria tributária (AgInt no REsp 1.828.606). Por isso, a petição precisa convencer na primeira vez.

## Fundamentos verificados
CPC arts. 138, 983, 1.035, §4º, e 1.038, I; Lei 9.868/1999, art. 7º, §2º; STJ: AgInt no REsp 1.828.606, AgInt no MS 25.655, EDcl no AgInt no AREsp 1.615.770, EDcl nos EAREsp 664.888. Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Admissão como amicus curiae, com definição de poderes (memoriais, sustentação oral, juntada de estudos).
- Intimação dos atos processuais em nome dos advogados indicados.
- Recebimento da manifestação técnica e dos documentos anexos.
- Inscrição para sustentação oral, nos termos do regimento interno.
- Sem pedido de condenação ou de tutela em favor próprio.

## Checklist pré-protocolo
- [ ] Fase do processo conferida (antes da pauta; nunca após o julgamento)
- [ ] Estatuto, ata e procuração anexados; abrangência e finalidade demonstradas
- [ ] Contribuição que as partes não trouxeram (dados, técnica, impacto) explicitada
- [ ] Manifestação de mérito objetiva, sem repetir as razões das partes
- [ ] Pedido expresso de poderes e de sustentação oral
- [ ] Cliente ciente: indeferimento é irrecorrível e o amicus não recorre do mérito (salvo ED e IRDR)

## Erros a evitar
- Pedir ingresso depois da inclusão em pauta ou do julgamento.
- Petição genérica que só adere à tese de uma parte, sem contribuição própria.
- Interpor agravo interno contra o indeferimento: não é conhecido.
- Opor embargos de declaração sem ter sido admitido.
- Confundir amicus com assistente e pedir efeitos da decisão para si.

## Integração com o núcleo
`prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

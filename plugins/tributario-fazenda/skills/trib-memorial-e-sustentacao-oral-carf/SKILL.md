---
name: trib-memorial-e-sustentacao-oral-carf
description: >
  Prepara memorial escrito e roteiro de sustentação oral para julgamento no CARF
  e na Câmara Superior de Recursos Fiscais, em reunião síncrona (presencial,
  virtual ou híbrida) ou assíncrona (plenário virtual), com base no Decreto
  70.235/1972 art. 25, §12, e no Regimento Interno do CARF (Portaria MF
  1.634/2023, arts. 95, 96, 102, 103, 107, 108 e 110). Use quando o usuário pedir
  memorial ao CARF, memoriais para o relator, sustentação oral no CARF ou na
  CSRF, roteiro de 15 minutos, vídeo de sustentação para plenário virtual,
  pedido de retirada de pauta ou preparação para a sessão de julgamento.
metadata:
  area: tributario-fazenda
  tipo_peca: outro
  verificado_em: 2026-11-25
---
# Memorial e sustentação oral no CARF

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: processo com recurso voluntário, de ofício ou especial incluído (ou prestes a ser incluído) em pauta do CARF ou da CSRF; preparação do memorial, do roteiro oral, do vídeo para reunião assíncrona e dos pedidos de pauta.
- Não usar: para redigir a impugnação ou o recurso voluntário (`trib-defesa-administrativa-e-carf`) ou o recurso especial (`trib-recurso-especial-csrf`). O memorial não substitui o recurso: não amplia a matéria nem traz prova nova.
- Tribunal administrativo estadual ou municipal: aproveite a lógica, mas siga o regimento local (`trib-recurso-administrativo-estadual`).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
- Número do processo, turma, relator e data de publicação da pauta (DOU e sítio do CARF).
- Modalidade da reunião: síncrona (presencial, não presencial ou híbrida) ou assíncrona.
- Peças já apresentadas (impugnação, decisão da DRJ, recurso, contrarrazões, acórdão recorrido) e as matérias em julgamento.
- Precedentes favoráveis e contrários da própria turma e da CSRF, já conferidos; súmulas do CARF aplicáveis.
- Pluralidade de sujeitos passivos (tempo dividido) e se há outro advogado sustentando.

## Prazo e contagem
- Pauta publicada no DOU e no sítio do CARF com, no mínimo, 10 dias de antecedência do início da reunião (RICARF art. 102, §1º). O prazo de tudo começa nela: acompanhe a publicação.
- Reunião síncrona: sustentação e acompanhamento dependem de requerimento com a antecedência fixada em ato do Presidente do CARF (RICARF art. 95). O prazo e a forma constam do ato vigente e da própria pauta [VERIFICAR: prazo do requerimento no ato do Presidente do CARF vigente na data].
- Reunião assíncrona: vídeo ou áudio da sustentação, limitado a 15 minutos, e memorial em arquivo de texto em até 5 dias após a publicação da pauta (RICARF art. 103 e §1º). Fora do prazo ou do formato, são desconsiderados (§3º).
- Enquanto não houver o sistema eletrônico de votos do art. 92, §2º, a reunião assíncrona segue o rito sumário do art. 132: pedido de sustentação em até 5 dias da pauta retira o processo para sessão síncrona (art. 132, §§1º e 3º). Confira na pauta qual regime está sendo aplicado.
- Retirada de pauta a pedido da parte: em até 4 dias úteis do início da reunião, uma única vez por parte, salvo caso fortuito ou força maior (RICARF art. 108, §1º).
- Pedido de exclusão da reunião assíncrona por controvérsia relevante e disseminada ou complexidade probatória: no prazo da sustentação (RICARF art. 104, III).
- Use `prazos-processuais` para dias úteis e para a pausa de 20/12 a 20/01.

## Estrutura da peça
Memorial: capa curta → o que está em julgamento → resumo dos fatos incontroversos → três teses no máximo, cada uma com a prova (folha/ID) e o precedente → resposta antecipada ao fundamento contrário mais forte → pedido. Roteiro oral: abertura de 30 segundos → tese principal → prova decisiva → precedente → pedido. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Direito de sustentar assegurado ao procurador do sujeito passivo (Decreto 70.235 art. 25, §12) e de apresentar memoriais antes do julgamento, inclusive em meio digital (RICARF arts. 95 e 107).
- Tempo: 15 minutos, prorrogáveis pelo presidente; 10 minutos em embargos de declaração, limitados aos pontos admitidos; 30 minutos divididos entre vários sujeitos passivos (RICARF art. 96, I a III).
- Recursos repetitivos em lote: sustentação complementar dos processos não sorteados, no julgamento do paradigma (art. 96, IV e VI).
- Retorno de diligência: nova sustentação, mesmo que já feita antes (art. 96, V).
- Ordem na sessão: relatório, sustentação do recorrente, sustentação da parte adversa, voto do relator, debates (RICARF art. 110). Em recurso especial da Fazenda, o contribuinte fala depois da Procuradoria.
- Na sessão síncrona, a sustentação pode ser por videoconferência em tempo real ou por arquivo de áudio ou vídeo, conforme ato do Presidente do CARF (art. 110, §1º). Queda de conexão do patrono por mais de 5 minutos retira o processo de pauta uma única vez (art. 110, §§14 e 15).
- Preferência para sustentação às pessoas do art. 1º da Lei 10.048/2000 (RICARF art. 108, §7º).
- Os julgadores não afastam lei por inconstitucionalidade (Decreto art. 26-A; RICARF art. 98): não gaste o tempo com isso.

## Fundamentos verificados
Decreto 70.235/1972 arts. 25, §§9º-A e 12, e 26-A; RICARF (Portaria MF 1.634/2023) arts. 95, 96, 98, 102, 103, 104, 105, 107, 108, 110 e 132. Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Requerimento de sustentação oral e de acompanhamento, no canal e prazo indicados na pauta.
- Juntada do memorial (síncrona: antes do julgamento; assíncrona: em 5 dias da pauta).
- Se necessário: retirada de pauta (art. 108, §1º), exclusão da reunião assíncrona (art. 104), preferência (art. 108, §7º).
- No fecho do memorial: provimento do recurso nos termos já deduzidos; se o julgamento se resolver por voto de qualidade, lembrar a exclusão das multas e o cancelamento da representação fiscal para fins penais (Decreto art. 25, §9º-A).

## Checklist pré-protocolo
- [ ] Data de publicação da pauta anotada; prazo de 5 dias (assíncrona) ou do ato do Presidente (síncrona) calculado.
- [ ] Modalidade da reunião conferida na pauta.
- [ ] Memorial com no máximo 3 teses, citando folhas/IDs dos autos.
- [ ] Nenhuma tese nova e nenhum documento novo no memorial.
- [ ] Precedentes e súmulas do CARF conferidos no portal oficial; nada de memória.
- [ ] Roteiro cronometrado abaixo de 15 minutos (ou do tempo dividido).
- [ ] Vídeo ou áudio no formato e tamanho do ato do Presidente do CARF (art. 103, §2º).
- [ ] Teste de conexão e plano B para videoconferência.

## Erros a evitar
- Ler o recurso em voz alta: o relator já leu; a sustentação escolhe e hierarquiza.
- Memorial longo que repete o recurso: o relator e os demais conselheiros recebem dezenas por reunião.
- Perder o prazo de 5 dias da reunião assíncrona: a sustentação é desconsiderada (art. 103, §3º).
- Pedir retirada de pauta tarde ou pela segunda vez (art. 108, §1º).
- Pedir que a turma declare lei inconstitucional.
- Citar acórdão do CARF sem conferir número, turma e data.

## Integração com o núcleo
- `prazos-processuais`: prazos contados da pauta.
- `verificacao-de-citacoes`: precedentes da turma e da CSRF citados no memorial.
- `fidelidade-factual`: cada afirmação de fato com a folha ou o ID dos autos.
- `estilo-forense`: texto curto e oral.
- `juros-e-correcao`: se o memorial mencionar valores atualizados.

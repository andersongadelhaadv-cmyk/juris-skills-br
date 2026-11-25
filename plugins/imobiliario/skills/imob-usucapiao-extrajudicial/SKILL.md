---
name: imob-usucapiao-extrajudicial
description: >
  Prepara o requerimento de reconhecimento extrajudicial de usucapião no
  Registro de Imóveis (Lei 6.015/1973, art. 216-A), com ata notarial, planta e
  memorial com ART, certidões, justo título ou justificação administrativa,
  notificações e editais. Use quando o usuário pedir usucapião em cartório,
  regularizar imóvel sem ir ao Judiciário, montar o pedido ao registrador,
  responder a nota de exigência, tratar de confrontante que não assinou ou de
  impugnação que leva o caso ao juiz.
metadata:
  area: imobiliario
  tipo_peca: requerimento
  verificado_em: 2026-11-25
---
# Usucapião extrajudicial (art. 216-A da Lei 6.015/1973)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: os requisitos materiais de alguma modalidade de usucapião estão presentes (ver `imob-usucapiao-judicial` para tempo, área e demais requisitos) e há chance real de **anuência ou silêncio** dos titulares e confrontantes; documentação de posse razoável.
- Não usar:
  - litígio declarado com o titular ou confrontante, ou prova da posse que dependa de muita testemunha controvertida: `imob-usucapiao-judicial` (a via extrajudicial é facultativa — STJ, REsp 1.796.394);
  - promessa de compra e venda quitada com vendedor omisso: compare com `imob-adjudicacao-compulsoria` (art. 216-B), muitas vezes mais simples;
  - imóvel público: não usucapível (CF arts. 183, § 3º, e 191, parágrafo único);
  - inventário do possuidor falecido: `sucessoes-inventario-extrajudicial` (a posse se transmite aos herdeiros — CC art. 1.206).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Matrícula/transcrição (ou certidão negativa de registro) e titulares de direitos registrados.
2. Modalidade pretendida e tempo de posse, com a cadeia de antecessores e datas.
3. Documentos de posse: justo título, recibos, cessões, IPTU/ITR, contas, fotos (inciso IV).
4. Profissional para planta e memorial com ART/RRT e lista dos confrontantes (nomes, endereços).
5. Quem já concordou e assina a planta; quem está em lugar incerto.
6. Domicílio do requerente (certidões dos distribuidores da comarca do imóvel **e** do domicílio).
7. Se é unidade em condomínio edilício ou confronta com condomínio (síndico).
8. Estado civil e regime de bens do requerente.

## Prazo e contagem
- Os prazos de posse são os da modalidade (CC arts. 1.238 a 1.242, 1.240-A; CF arts. 183 e 191) — conferir na skill judicial.
- Prazos do procedimento no cartório (art. 216-A): **15 dias** para o titular/confrontante notificado se manifestar, valendo o silêncio como concordância (§ 2º); **15 dias** para União, Estado, DF e Município (§ 3º); **15 dias** do edital para terceiros (§ 4º); notificado em lugar incerto: edital publicado **duas vezes**, 15 dias cada, silêncio = concordância (§ 13).
- Prenotação prorrogada até o acolhimento ou a rejeição (§ 1º).
- Prazo para resposta a nota de exigência e para suscitar dúvida: normas estaduais e `prazos-processuais` [VERIFICAR: normas da corregedoria local].

## Estrutura do requerimento
Endereçamento ao Oficial do Registro de Imóveis da situação → qualificação e representação por advogado → modalidade e requisitos → posse e cadeia → documentos do art. 216-A, I a IV → pedido de notificações e editais → pedido de registro com abertura de matrícula. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Advogado obrigatório** (art. 216-A, *caput*); procuração com poderes específicos.
- Documentos do art. 216-A: I — **ata notarial** do tempo de posse do requerente e antecessores; II — **planta e memorial descritivo** com ART/RRT, assinados pelos titulares registrados e confrontantes; III — **certidões negativas** dos distribuidores da comarca do imóvel e do domicílio; IV — **justo título** ou outros documentos de origem, continuidade, natureza e tempo da posse.
- Falta ou insuficiência do inciso IV: **justificação administrativa** na própria serventia (§ 15).
- Condomínio edilício: unidade autônoma dispensa o consentimento dos confrontantes, bastando notificar o síndico (§ 11); confrontante que é condomínio: notificar o síndico (§ 12).
- Edital eletrônico pode substituir o jornal, se autorizado pelo órgão correicional (§ 14).
- **Impugnação**: justificada → autos ao juízo, emendando-se para o procedimento comum; injustificada → o registrador não a admite, cabendo dúvida (§ 10). Rejeição não impede a ação judicial (§ 9º).
- Regulamentação nacional do CNJ (procedimento, ata notarial, emolumentos) [VERIFICAR: provimento vigente e artigos não conferidos — o site do CNJ recusou o acesso automatizado].

## Fundamentos verificados
- Lei 6.015/1973, art. 216-A e §§ 1º a 15.
- CC arts. 1.206, 1.238 a 1.244; CF arts. 183 e 191.
- STJ, REsp 1.796.394 (via facultativa); REsp 2.217.542 (os requisitos extrajudiciais, como a ART, não se estendem à ação judicial — e confirmam que **aqui** são exigíveis).
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos (requerimento ao registrador)
- Autuação e prorrogação da prenotação (§ 1º).
- Notificação pessoal ou por correio com AR dos titulares e confrontantes que não assinaram (§ 2º); edital para os não encontrados (§ 13).
- Cientificação da União, do Estado/DF e do Município (§ 3º); edital para terceiros (§ 4º).
- Justificação administrativa, se necessária (§ 15); diligências (§ 5º).
- Registro da aquisição, com abertura de matrícula se for o caso (§ 6º).
- Subsidiariamente, em caso de exigência indevida: suscitação de dúvida (§ 7º).

## Checklist pré-protocolo
- [ ] Ata notarial lavrada, cobrindo toda a cadeia possessória
- [ ] Planta e memorial com ART/RRT; assinaturas colhidas e lista dos faltantes com endereço
- [ ] Certidões dos distribuidores (comarca do imóvel e do domicílio)
- [ ] Justo título ou documentos de posse; plano B de justificação (§ 15)
- [ ] Procuração com poderes específicos
- [ ] Imóvel não público; modalidade e área conferidas
- [ ] Custos de emolumentos e ata notarial informados ao cliente
- [ ] Plano para impugnação (migração ao juízo — § 10)

## Erros a evitar
- Usar a via extrajudicial contra titular que já declarou oposição: a impugnação manda tudo ao juiz, com custo dobrado.
- Ata notarial que só reproduz declarações do requerente, sem documentos, testemunhas ou constatação.
- Esquecer as certidões do domicílio do requerente (só juntar as da comarca do imóvel).
- Memorial com confrontações diferentes da matrícula sem explicar a divergência.
- Tratar o silêncio do notificado como recusa — pela lei, é concordância (§§ 2º e 13).

## Integração com o núcleo
`prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`, `imob-usucapiao-judicial`.

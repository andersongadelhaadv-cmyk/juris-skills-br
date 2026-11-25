---
name: intl-contrato-internacional
description: >
  Elabora ou revisa contrato internacional (compra e venda de mercadorias,
  fornecimento, distribuição, prestação de serviços transfronteiriça) com
  escolha de lei aplicável, foro ou arbitragem, idioma, moeda e regime da
  Convenção de Viena (CISG, Decreto 8.327/2014), à luz do art. 9º da LINDB,
  dos arts. 21 a 25 do CPC e da Lei 9.307/1996. Use quando o usuário pedir
  contrato com parte estrangeira, cláusula de lei aplicável, cláusula
  arbitral internacional, eleição de foro estrangeiro, exclusão ou aplicação
  da CISG, ou parecer sobre risco de contrato internacional.
metadata:
  area: internacional
  tipo_peca: contrato
  verificado_em: 2026-11-25
---
# Contrato internacional

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: contrato em que as partes têm estabelecimento em países diferentes, ou cuja execução, pagamento ou entrega atravessa fronteira; cláusula de lei aplicável, foro estrangeiro ou arbitragem com sede no exterior; decidir se a CISG incide e se convém excluí-la.
- Não usar: contrato puramente doméstico (`contratos-elaboracao-de-contrato`, `contratos-compra-e-venda-empresarial`); revisão de minuta enviada pela outra parte sem elemento estrangeiro (`contratos-analise-e-revisao-de-contrato`); comprador destinatário final (o CDC pode afastar a cláusula de foro estrangeiro — ver Fundamentos; `consumidor-*`); executar no Brasil sentença ou laudo já proferidos lá fora (`intl-homologacao-sentenca-estrangeira`).

## Entradas mínimas (perguntar o que faltar; nunca supor fatos)
1. Partes: nome, país de constituição, **país do estabelecimento** relevante para o contrato, representantes e poderes.
2. Objeto: mercadoria (CISG) ou serviço/licença/distribuição (CISG não incide como regra).
3. Onde nasce a proposta (quem propõe e onde reside) — decide a lei pelo art. 9º, § 2º, da LINDB se não houver escolha válida.
4. Onde o contrato será cumprido (entrega, pagamento, prestação) e onde estão os bens do devedor (onde se vai executar).
5. Preferência de solução de disputa: Judiciário brasileiro, foro estrangeiro ou arbitragem (instituição, sede, idioma, número de árbitros).
6. Moeda, câmbio, Incoterm desejado, garantias (carta de crédito, seguro), prazo e regras de rescisão.
7. Há consumidor ou parte aderente? Há ente público?

## Prazo e contagem
- Não há prazo de propositura; os prazos relevantes são os do contrato e os da CISG para o comprador: comunicar a desconformidade em prazo razoável, com teto de dois anos da entrega efetiva (art. 39 da CISG) — fixe prazos de inspeção e denúncia por escrito.
- Prescrição da pretensão contratual: depende da lei aplicável escolhida; se for a brasileira, confira o prazo na fonte e registre [VERIFICAR via `verificacao-de-citacoes`]. Prazos processuais: `prazos-processuais`.

## Estrutura da peça
Qualificação → considerandos (incluir o elemento de estraneidade) → definições → objeto e especificações → preço, moeda e pagamento → entrega/Incoterm e transferência de riscos → conformidade, inspeção e denúncia → garantias → força maior/exoneração → rescisão por violação essencial → limitação de responsabilidade → confidencialidade → lei aplicável → solução de disputas → idioma prevalente → notificações → assinaturas. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares (pontos de decisão)
- **Lei aplicável.** A LINDB manda reger a obrigação pela lei do país onde se constituiu (art. 9º, caput), e a do contrato pelo lugar onde reside o proponente (§ 2º). O art. 9º não menciona escolha de lei pelas partes, e o alcance dessa escolha no Judiciário estatal não foi conferido em precedente [VERIFICAR: sem precedente confirmado no JuriBase]; na arbitragem a escolha é expressa (Lei 9.307/1996, art. 2º, § 1º). Se o contrato puder ir ao Judiciário brasileiro, alinhe a escolha com o lugar de constituição ou prefira a arbitragem.
- **Forma no Brasil.** Se a obrigação for executada no Brasil e depender de forma essencial, a forma brasileira será observada (art. 9º, § 1º).
- **Foro.** Cláusula de foro exclusivo estrangeiro afasta a jurisdição brasileira se o réu a alegar na contestação (CPC, art. 25), salvo competência exclusiva (art. 23: imóveis no Brasil etc.). Diga "exclusivo" expressamente.
- **Arbitragem.** Cláusula compromissória por escrito (Lei 9.307/1996, art. 4º, § 1º); em contrato de adesão, só com destaque e visto específico (§ 2º). Laudo proferido fora do Brasil precisa de homologação pelo STJ (art. 35).
- **CISG.** Aplica-se à compra e venda de mercadorias entre partes com estabelecimentos em Estados contratantes diferentes (art. 1). As partes podem excluí-la ou derrogá-la (art. 6). Decida conscientemente: excluir, aplicar ou aplicar com ajustes.

## Fundamentos verificados
- LINDB arts. 9º (caput, §§ 1º e 2º), 13, 14 e 17.
- CPC arts. 21 a 25 e 192 (art. 63 [VERIFICAR: redação atual]); Lei 9.307/1996 arts. 2º, 4º, 34, 35, 38 e 39; Decreto 4.311/2002 (Convenção de Nova York).
- CISG (Decreto 8.327/2014): arts. 1, 4, 6, 7, 11, 25, 35, 39, 49, 74 e 79.
- STJ: validade em abstrato da cláusula de foro estrangeiro (AgInt no AREsp 2.523.075, 4ª Turma, 2025); afastamento só com obstáculo concreto de acesso à justiça (REsp 2.206.798, 3ª Turma, 2025); abusividade frente a consumidor brasileiro (REsp 2.210.341, 4ª Turma, 2025).
- STJ: dívida em moeda estrangeira convertida pela cotação da data da contratação (AgInt nos EDcl no REsp 2.017.292, 3ª Turma, 2023) — correção posterior pelo núcleo `juros-e-correcao`.
Detalhe em [fundamentos](references/fundamentos.md).

## Cláusulas essenciais
- Lei aplicável com indicação da CISG (aplicar ou excluir, art. 6) e da lei subsidiária para o que a CISG não regula (validade, propriedade — art. 4).
- Solução de disputas: arbitragem (instituição, sede, regras, idioma, árbitros) **ou** foro exclusivo; nunca as duas sem hierarquia clara.
- Incoterm com versão indicada; momento da transferência de risco.
- Prazo de inspeção e de denúncia de vício (diálogo com o art. 39 da CISG).
- Violação essencial e rescisão (arts. 25 e 49 da CISG), com prazo suplementar.
- Exoneração por impedimento alheio (art. 79 da CISG) e lista de eventos.
- Limitação de perdas e danos (art. 74 da CISG trata da previsibilidade).
- Idioma prevalente e tradução juramentada para uso no Brasil (CPC, art. 192, parágrafo único).
- Notificações: endereços, e-mails e efeito de recebimento.

## Checklist pré-assinatura
- [ ] Estabelecimento de cada parte identificado (decide a CISG)
- [ ] Lei aplicável compatível com o foro escolhido
- [ ] Cláusula de foro dita "exclusiva" ou arbitragem com sede definida
- [ ] Verificado se há competência exclusiva brasileira (art. 23 do CPC)
- [ ] Cláusula arbitral escrita e, se adesão, destacada e vistada
- [ ] CISG aplicada ou excluída expressamente
- [ ] Moeda, câmbio e cotação de conversão definidos
- [ ] Poderes de assinatura conferidos; documentos estrangeiros apostilados (`intl-apostilamento-legalizacao`)

## Erros a evitar
- Escolher lei estrangeira e foro brasileiro sem prever prova do direito estrangeiro (LINDB, art. 14).
- Cláusula "foro de Nova York ou São Paulo" sem exclusividade: o Judiciário brasileiro continua competente (art. 25 exige exclusividade).
- Cláusula arbitral patológica (instituição inexistente, sede indefinida).
- Ignorar que a CISG incide por padrão quando os dois países são contratantes.
- Usar cláusula de foro estrangeiro contra consumidor brasileiro.
- Fixar taxa de juros ou índice sem passar pelo núcleo.

## Integração com o núcleo
`juros-e-correcao` (juros, correção e conversão monetária), `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`. Vizinhas: `contratos-elaboracao-de-contrato`, `contratos-compra-e-venda-empresarial`, `contratos-agencia-e-distribuicao`, `intl-homologacao-sentenca-estrangeira`.

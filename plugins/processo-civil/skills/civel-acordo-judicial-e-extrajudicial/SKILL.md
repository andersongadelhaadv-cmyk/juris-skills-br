---
name: civel-acordo-judicial-e-extrajudicial
description: >
  Redige minuta de acordo cível (transação dos arts. 840 a 850 do Código
  Civil), judicial ou extrajudicial, e a petição de homologação: em processo
  em curso (CPC arts. 334, § 11, 487, III, b, e 515, II) ou como autocomposição
  extrajudicial levada ao juiz pela jurisdição voluntária (arts. 515, III, e
  725, VIII), ou ainda como título executivo extrajudicial referendado pelos
  advogados (art. 784, IV). Use quando o usuário pedir acordo cível, termo de
  transação, minuta de composição, petição de homologação de acordo, acordo
  antes da citação, acordo em cumprimento de sentença, revisão de proposta de
  acordo da parte contrária ou cláusulas de quitação, multa e inadimplemento.
metadata:
  area: processo-civil
  tipo_peca: outro
  verificado_em: 2026-11-25
---
# Acordo cível judicial e extrajudicial (transação e homologação)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: (a) acordo em processo cível em curso, em qualquer fase (antes da citação, na audiência do art. 334, em recurso, no cumprimento de sentença ou na execução); (b) acordo extrajudicial que se quer homologar em juízo sem processo prévio (art. 725, VIII); (c) instrumento de transação que vale como título executivo extrajudicial, sem homologação (art. 784, IV); (d) revisão crítica da proposta enviada pela parte contrária.
- Não usar:
  - Acordo em ação de consumo: `consumidor-acordo-judicial`.
  - Acordo trabalhista: `trabalhista-acordo-extrajudicial`.
  - Alimentos, guarda, divórcio: `familia-divorcio`, `familia-acao-de-alimentos`, `familia-guarda-e-convivencia` (direitos indisponíveis, MP intervém).
  - Distrato de contrato sem litígio: `contratos-distrato-e-rescisao`; aditivo: `contratos-aditivo-contratual`.
  - Transação tributária: `trib-*`; termo de ajustamento de conduta ambiental: `amb-termo-ajustamento-conduta`.
  - Renegociação bancária sem processo: `banc-renegociacao-extrajudicial-de-divida`.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Processo (número, vara, fase) ou, se extrajudicial, a relação jurídica e o litígio que se previne.
2. Partes exatas, inclusive terceiros que entram no acordo (art. 515, § 2º) e fiadores ou devedores solidários (art. 844 do CC).
3. Valor, forma de pagamento (à vista, parcelas, datas, conta), obrigação de fazer ou entregar.
4. O que se quita e o que fica de fora (quitação restrita ao objeto ou geral).
5. Custas e honorários: quem paga; se há honorários de sucumbência já fixados e se o advogado anui (art. 24, § 4º, da Lei 8.906/1994).
6. Procuração com poderes especiais para transigir, receber e dar quitação (art. 105 do CPC) — de ambos os lados.
7. Garantias pretendidas (multa, vencimento antecipado, garantia real ou fidejussória).
8. Se há incapaz, interesse indisponível ou ente público (limita ou condiciona a transação).

## Prazo e contagem
- Não há prazo para transigir; pode ocorrer a qualquer tempo, inclusive após a sentença.
- Custas: transação antes da sentença dispensa as custas remanescentes (art. 90, § 3º, do CPC); silêncio sobre despesas = divisão igual (§ 2º). Escreva a cláusula expressamente.
- Prazos de parcelas e de cumprimento: datas de calendário, não "dias" soltos.
- Ação para anular a transação homologada (art. 966, § 4º, do CPC; art. 849 do CC): prazo [VERIFICAR: conferir o prazo decadencial aplicável ao vício alegado — não registrado aqui].
- Contagem processual: `prazos-processuais`.

## Estrutura da peça
Minuta: qualificação → considerandos (litígio e processo) → objeto → obrigações e cronograma → multa e inadimplemento → quitação → custas e honorários → pedido de homologação e extinção → foro e assinaturas. Petição: comunicação do acordo, pedido de homologação (art. 487, III, b), suspensão até o cumprimento, se as partes assim pactuarem, renúncia ao prazo recursal. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Objeto: só direitos patrimoniais de caráter privado (art. 841 do CC).
- Forma: com direitos já contestados em juízo, escritura pública ou termo nos autos assinado pelas partes e homologado (art. 842 do CC). Na prática, petição conjunta assinada pelas partes e advogados.
- Interpretação restritiva: a transação não transmite direitos, só declara ou reconhece (art. 843). Tudo o que importa deve estar escrito.
- Indivisibilidade: nulidade de uma cláusula invalida toda a transação, salvo direitos independentes entre si (art. 848). Separe as obrigações autônomas.
- Anulação só por dolo, coação ou erro essencial quanto à pessoa ou coisa controversa; erro de direito sobre a questão controvertida não anula (art. 849).
- Representação: procuração com poder especial de transigir (art. 105) — sem ele, o advogado não assina sozinho.
- Antes da citação: a transação pode ser homologada mesmo sem advogado constituído pelo réu (STJ, REsp 2.062.295 e REsp 2.158.785).
- O juiz pode recusar a homologação de acordo de licitude duvidosa (STJ, AgInt no AREsp 2.141.778).

## Fundamentos verificados
- CC arts. 840 a 850 (transação); CPC arts. 3º, §§ 2º e 3º; 90, §§ 2º e 3º; 105; 334, §§ 10 e 11; 487, III, b; 515, II, III e § 2º; 725, VIII; 784, II a IV; 966, § 4º.
- Lei 8.906/1994, art. 24, § 4º (acordo não prejudica honorários sem anuência do advogado).
- STJ: homologatória é título judicial e se executa por cumprimento de sentença, com multa e honorários (REsp 1.968.015); competência da anulatória é do juízo que homologou (REsp 2.064.264).
Detalhe em [fundamentos](references/fundamentos.md).

## Cláusulas essenciais
- Objeto e valor certos; forma, conta e datas de pagamento.
- Obrigação de fazer com prazo e destinatário (ex.: baixa de gravame, entrega de documento).
- Cláusula penal (art. 847 do CC) proporcional e vencimento antecipado das parcelas.
- Retomada: inadimplido, executa-se o acordo (título judicial) — e não o crédito original, salvo cláusula expressa de restabelecimento.
- Quitação condicionada ao cumprimento integral, delimitada ao objeto.
- Custas e honorários (inclusive sucumbência já fixada).
- Juros e correção de parcelas: remeter ao núcleo `juros-e-correcao`; não fixar índice de memória.
- Pedido de homologação e de extinção com resolução de mérito; renúncia ao prazo recursal.

## Checklist pré-protocolo
- [ ] Poderes especiais (transigir, receber, dar quitação) conferidos nos autos para todos os advogados que assinam.
- [ ] Todas as partes e terceiros obrigados assinam.
- [ ] Objeto patrimonial e disponível (art. 841); incapaz ou ente público tratados à parte.
- [ ] Cláusula de custas e honorários escrita (art. 90, §§ 2º e 3º; art. 24, § 4º, da Lei 8.906/1994).
- [ ] Datas de calendário, conta bancária e comprovação de pagamento definidas.
- [ ] Multa e vencimento antecipado redigidos; o que se executa em caso de inadimplemento está claro.
- [ ] Quitação delimitada; ressalvas expressas.
- [ ] Extrajudicial sem homologação: assinatura dos advogados dos transatores (art. 784, IV) ou de duas testemunhas (art. 784, III).

## Erros a evitar
- Quitação geral "de toda e qualquer obrigação" sem o cliente saber o que renuncia.
- Esquecer os honorários de sucumbência já fixados: o advogado pode cobrá-los mesmo após o acordo (art. 24, § 4º).
- Advogado sem poder de transigir assinando sozinho.
- Cláusula nula que contamina todo o acordo por não separar obrigações independentes (art. 848).
- Acordo sobre direito indisponível ou de incapaz sem as cautelas próprias.
- Prometer ao cliente que a homologação é automática: o juiz controla a licitude.

## Integração com o núcleo
`juros-e-correcao` (parcelas, multa, atualização), `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`. Execução do acordo descumprido: `civel-cumprimento-de-sentenca` (homologado) ou `civel-execucao-titulo-extrajudicial` (art. 784, IV).

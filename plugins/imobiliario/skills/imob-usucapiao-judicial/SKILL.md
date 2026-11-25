---
name: imob-usucapiao-judicial
description: >
  Redige ação de usucapião de imóvel — extraordinária, ordinária, especial
  urbana e rural (CF arts. 183 e 191), familiar por abandono do lar (CC art.
  1.240-A) e coletiva do Estatuto da Cidade — pelo procedimento comum, com
  citação pessoal dos confinantes e editais. Use quando o usuário pedir ação de
  usucapião, regularizar imóvel sem escritura pela posse prolongada, escolher a
  modalidade e o prazo aplicável, somar a posse dos antecessores, ou responder
  a usucapião alegada como defesa.
metadata:
  area: imobiliario
  tipo_peca: inicial
  verificado_em: 2026-11-25
---
# Usucapião judicial de imóvel

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: possuidor com *animus domini* (posse como dono), contínua e sem oposição, pelo prazo da modalidade, que quer a declaração judicial do domínio (art. 1.241 do CC); também para redigir a usucapião como **matéria de defesa** (Súmula 237/STF).
- Não usar:
  - há consenso dos titulares e documentação completa — avalie o cartório: `imob-usucapiao-extrajudicial` (a via extrajudicial é facultativa — STJ, REsp 1.796.394);
  - há promessa de compra e venda quitada e o vendedor some ou se recusa a outorgar a escritura: `imob-adjudicacao-compulsoria` costuma ser mais direta;
  - quer só proteger a posse atual contra invasor: `imob-reintegracao-de-posse`;
  - núcleo urbano informal a regularizar como um todo: `imob-regularizacao-fundiaria-reurb`; só corrigir medidas da matrícula: `imob-retificacao-de-area`;
  - partilha do imóvel no divórcio (sem os requisitos do art. 1.240-A): `familia-divorcio`;
  - **imóvel público**: não é usucapível (CF arts. 183, § 3º, e 191, parágrafo único).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Matrícula ou transcrição do imóvel (ou certidão de que não há registro) e titular registral.
2. Planta e memorial descritivo; área exata (decide a modalidade especial: 250 m² urbano / 50 ha rural).
3. Início da posse, como começou (compra informal, herança, ocupação, permissão) e a cadeia de possuidores anteriores.
4. Prova da posse com *animus domini*: IPTU/ITR, contas, benfeitorias, fotos antigas, declarações, testemunhas.
5. Houve oposição judicial ou extrajudicial? Ações possessórias contra o possuidor e o resultado?
6. Uso: moradia própria/da família? Trabalho produtivo? O autor tem outro imóvel? Já usucapiu antes?
7. Justo título e boa-fé (para a ordinária): documento, data, por que não foi registrado.
8. Confinantes: nomes e endereços; se é unidade em condomínio.
9. Estado civil e regime de bens do autor.

## Prazo e contagem
Modalidades e prazos (CC e CF):
- **Extraordinária** — 15 anos, sem título nem boa-fé; **10 anos** se houver moradia habitual ou obras/serviços produtivos (art. 1.238 e parágrafo único).
- **Ordinária** — 10 anos com justo título e boa-fé; **5 anos** se adquirido onerosamente com base em registro depois cancelado, com moradia ou investimentos (art. 1.242).
- **Especial urbana** — 5 anos, área urbana até 250 m², moradia, sem outro imóvel, uma única vez (CF art. 183; CC art. 1.240; Estatuto da Cidade art. 9º). Lei municipal de lote mínimo não a impede (STF, Tema 815).
- **Especial rural** — 5 anos, até 50 ha, produtiva pelo trabalho próprio ou da família, com moradia, sem outro imóvel (CF art. 191; CC art. 1.239).
- **Familiar** — 2 anos de posse direta e exclusiva, imóvel urbano até 250 m² compartilhado com ex-cônjuge/companheiro que abandonou o lar, moradia, sem outro imóvel (CC art. 1.240-A).
- **Coletiva** — núcleo urbano informal há mais de 5 anos, área total ÷ possuidores < 250 m² (Estatuto da Cidade art. 10).
- *Accessio possessionis*: soma da posse dos antecessores, contínuas e pacíficas — e, na ordinária, com justo título e boa-fé (arts. 1.207 e 1.243).
- Causas que impedem, suspendem ou interrompem a prescrição aplicam-se à usucapião (art. 1.244). A citação em possessória **julgada improcedente** não interrompe o prazo (STJ, AgInt no AgInt no AREsp 1.863.294).
- O prazo pode se completar **no curso da ação** (STJ, AgInt no REsp 1.948.445).
- Prazos processuais: `prazos-processuais`.

## Estrutura da peça
Foro da situação (art. 47) → modalidade e requisitos → posse e cadeia possessória → descrição do imóvel → citações (titular, confinantes, edital) → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Procedimento comum (art. 318 do CPC); não há rito especial no CPC/2015.
- **Confinantes citados pessoalmente**, salvo unidade autônoma de condomínio (art. 246, § 3º, do CPC; Súmula 391/STF); possuidor citado pessoalmente (Súmula 263/STF); **edital** para interessados incertos (art. 259, I).
- Requisitos próprios da usucapião extrajudicial (como planta com ART) **não** se estendem à ação judicial (STJ, REsp 2.217.542) — mas memorial preciso evita exigências e facilita o registro.
- Posse precária (comodato, permissão, tolerância) não gera usucapião enquanto não houver inversão do caráter da posse (CC arts. 1.200, 1.203 e 1.208) — prove o momento da inversão.
- Especial urbana (Estatuto): MP intervém; gratuidade inclusive no registro; demais ações petitórias/possessórias sobre o imóvel ficam sobrestadas (Estatuto arts. 11 e 12).
- Rejeição do pedido extrajudicial não impede a ação (art. 216-A, § 9º, da Lei 6.015/1973).

## Fundamentos verificados
- CF arts. 183 e 191. CC arts. 1.200, 1.203, 1.207, 1.208, 1.238 a 1.244. Estatuto da Cidade arts. 9º a 13.
- CPC arts. 47, 246, § 3º, 259, I, 318. Lei 6.015/1973, art. 216-A, § 9º.
- Súmulas 237, 263 e 391 do STF; STF Tema 815; STJ REsp 1.796.394, REsp 2.217.542, AgInt no REsp 1.948.445, AgInt no AgInt no AREsp 1.863.294.
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Citação pessoal do titular registral, dos confinantes e de eventuais possuidores; edital para réus incertos e desconhecidos.
- Ciência aos entes públicos conforme a praxe e as normas locais [VERIFICAR: fundamento e forma da cientificação das Fazendas na via judicial].
- Produção de prova testemunhal, documental e pericial (topografia).
- Declaração do domínio e mandado de registro, com abertura de matrícula se necessário (a sentença é título — art. 1.241, parágrafo único).
- Gratuidade, quando cabível (assegurada ao autor da especial urbana pelo art. 12 do Estatuto, inclusive no registro).

## Checklist pré-protocolo
- [ ] Modalidade escolhida e cada requisito (tempo, área, moradia, outro imóvel, título/boa-fé) provado
- [ ] Cadeia possessória documentada, com datas
- [ ] Inversão do caráter da posse demonstrada, se a origem foi precária
- [ ] Planta/memorial e confrontações coerentes com a matrícula
- [ ] Confinantes, titular e possuidores listados para citação pessoal
- [ ] Imóvel não é público
- [ ] Usucapião anterior do autor descartada (modalidades especiais)
- [ ] Cônjuge/regime de bens considerados

## Erros a evitar
- Pedir usucapião especial sem provar que o autor não tem outro imóvel ou com área acima do limite.
- Confundir posse com detenção ou tolerância (caseiro, comodatário, parente "deixado" no imóvel).
- Omitir confinante ou citá-lo só por edital.
- Ignorar ação possessória anterior procedente contra o autor (interrompe o prazo).
- Somar posse de antecessor sem prova de continuidade.

## Integração com o núcleo
`prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`, `civel-peticao-inicial`, `civel-contestacao` (usucapião como defesa).

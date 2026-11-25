---
name: intl-homologacao-sentenca-estrangeira
description: >
  Redige pedido de homologação de decisão estrangeira (judicial ou arbitral)
  no STJ, ou a contestação a esse pedido, com base no art. 105, I, i, da CF,
  nos arts. 960 a 965 do CPC, nos arts. 15 e 17 da LINDB e nos arts. 34 a 40
  da Lei 9.307/1996. Use quando o usuário pedir para validar no Brasil
  sentença de divórcio, guarda, alimentos ou condenação proferida no
  exterior, homologar laudo arbitral estrangeiro, contestar homologação por
  falta de citação válida, ou cumprir depois a sentença homologada.
metadata:
  area: internacional
  tipo_peca: inicial
  verificado_em: 2026-11-25
---
# Homologação de decisão estrangeira (STJ)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: dar eficácia no Brasil a sentença judicial definitiva estrangeira, decisão não judicial que aqui teria natureza jurisdicional (CPC, art. 961, § 1º) ou laudo arbitral proferido fora do Brasil; contestar o pedido (polo passivo).
- Não usar: divórcio consensual puro — produz efeitos sem homologação do STJ (art. 961, § 5º; averbação direta, ver Erros a evitar); decisão interlocutória ou medida de urgência estrangeira — vai por carta rogatória (`intl-carta-rogatoria-exequatur`); pedido estrangeiro de prova ou informação sem decisão a delibar (`intl-cooperacao-auxilio-direto`); ação nova no Brasil sobre o mesmo conflito (`civel-peticao-inicial`; o art. 24 do CPC afasta litispendência).

## Entradas mínimas (perguntar o que faltar; nunca supor fatos)
1. Cópia integral da decisão estrangeira (inteiro teor, não só a certidão), com prova de que é **eficaz no país de origem**.
2. Como e onde o requerido foi citado no processo estrangeiro; onde ele morava à época (Brasil ou exterior); se compareceu ou se defendeu.
3. Se arbitral: convenção de arbitragem (cláusula ou compromisso) original ou cópia certificada.
4. Tradução oficial (juramentada) de tudo que estiver em língua estrangeira, salvo tratado que dispense.
5. Apostila ou legalização consular dos documentos, ou tratado que dispense (`intl-apostilamento-legalizacao`).
6. Endereço atual do requerido; se há bens no Brasil; se há ação no Brasil com o mesmo objeto ou decisão brasileira transitada.
7. Objeto: há imóvel no Brasil, inventário ou partilha de bens aqui? (competência exclusiva — art. 23 do CPC e art. 964).

## Prazo e contagem
- Não há prazo para pedir a homologação. Para a contestação e recursos no STJ, os prazos estão no RISTJ [VERIFICAR: RISTJ não conferido nesta skill] — conte com `prazos-processuais`.
- Após homologada, o cumprimento segue no juízo federal (CPC, art. 965; CF, art. 109, X), com citação para cumprir ou liquidar em 15 dias (art. 515, § 1º).

## Estrutura da peça
Endereçamento ao Presidente do STJ → qualificação (requerido com endereço completo) → objeto → síntese da decisão estrangeira → requisitos do art. 963 um a um → ausência de competência exclusiva (art. 964) → ausência de ofensa à ordem pública, soberania e dignidade (LINDB, art. 17) → pedidos → documentos. Contestação: matéria restrita aos requisitos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Art. 963 do CPC:** (I) autoridade competente; (II) citação regular, ainda que verificada a revelia; (III) eficácia no país de origem; (IV) não ofensa à coisa julgada brasileira; (V) tradução oficial, salvo tratado; (VI) não haver manifesta ofensa à ordem pública.
- **Trânsito em julgado:** o CPC exige eficácia, não mais trânsito (HDE 6.581, 2025).
- **Citação do réu domiciliado no Brasil:** a regra é a carta rogatória; citação postal de quem tem endereço no Brasil é nula (AgInt na HDE 7.684, 2024), com flexibilização excepcional quando houve ciência inequívoca e defesa assegurada (AgInt nos EDcl na HDE 8.123, 2024). Réu domiciliado no exterior: vale a lei do lugar da citação.
- **Laudo arbitral:** denegação só nas hipóteses dos arts. 38 e 39 da Lei 9.307/1996; citação postal vale com prova inequívoca de recebimento (art. 39, parágrafo único; AgInt nos EDcl na HDE 6.541, 2024).
- **Juízo de delibação:** o STJ não revisa o mérito nem adita a decisão estrangeira (HDE 5.431, 2022); prescrição e existência de bens são temas da execução (HDE 10.022, 2026).
- **Homologação parcial** é possível (art. 961, § 2º); tutela de urgência e execução provisória cabem no próprio pedido (art. 961, § 3º).

## Fundamentos verificados
- CF art. 105, I, i; art. 109, X. CPC arts. 24, 26, § 2º, 515, VIII, e § 1º, 960 a 965. LINDB arts. 15 e 17. Lei 9.307/1996 arts. 34 a 39. Decreto 4.311/2002 (Convenção de Nova York), arts. IV e V.
- STJ: HDE 6.581 (2025); AgInt na HDE 7.684 (2024); AgInt nos EDcl na HDE 8.123 (2024); AgInt nos EDcl na HDE 6.541 (2024); HDE 5.431 (2022); HDE 10.022 (2026).
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Citação do requerido (por carta de ordem ou rogatória, conforme o domicílio) [VERIFICAR: forma de citação no RISTJ].
- Homologação total (ou parcial, indicando os capítulos) da decisão estrangeira.
- Tutela de urgência ou execução provisória, se houver risco (art. 961, § 3º).
- Expedição de carta de sentença para cumprimento no juízo federal competente (art. 965).
- Gratuidade, se cabível; custas e honorários.
- Contestação: indeferimento por falta de requisito específico do art. 963/964 ou dos arts. 38 e 39 da Lei 9.307/1996 — nunca por discordância com o mérito.

## Checklist pré-protocolo
- [ ] Inteiro teor da decisão + prova de eficácia no país de origem
- [ ] Prova da citação (e de onde o réu morava na data)
- [ ] Convenção de arbitragem juntada (se laudo)
- [ ] Tradução juramentada de todos os documentos estrangeiros
- [ ] Apostila ou legalização (ou tratado que dispense)
- [ ] Ausência de decisão brasileira transitada sobre o mesmo objeto
- [ ] Ausência de matéria de competência exclusiva (imóvel/partilha no Brasil)
- [ ] Endereço atualizado do requerido

## Erros a evitar
- Juntar só certidão ou resumo da sentença, sem o inteiro teor.
- Ignorar que o réu morava no Brasil e foi citado por correio ou edital no exterior.
- Pedir homologação de partilha de imóvel situado no Brasil (art. 964 c/c art. 23, III).
- Discutir o mérito da causa na contestação: o STJ só delibera.
- Mandar ao STJ divórcio consensual puro (art. 961, § 5º); se houver guarda, alimentos ou partilha, a homologação continua necessária — confirme o alcance [VERIFICAR: regulamentação da averbação direta pelo CNJ não conferida].
- Fixar juros ou correção no pedido de cumprimento sem o núcleo.

## Integração com o núcleo
`juros-e-correcao`, `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`. Vizinhas: `intl-apostilamento-legalizacao`, `intl-carta-rogatoria-exequatur`, `civel-cumprimento-de-sentenca`, `familia-divorcio`, `familia-execucao-de-alimentos`.

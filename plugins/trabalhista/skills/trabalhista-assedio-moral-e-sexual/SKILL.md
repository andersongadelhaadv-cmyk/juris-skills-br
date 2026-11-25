---
name: trabalhista-assedio-moral-e-sexual
description: >
  Estrutura o pedido (ou a defesa) de indenização por assédio moral e por assédio
  sexual no trabalho, com base nos arts. 223-A a 223-G da CLT (parâmetros
  orientativos após as ADIs 6050, 6069 e 6082), na responsabilidade do empregador
  pelos atos de prepostos (CC arts. 932, III, e 933) e no dever de prevenção da
  Lei 14.457/2022. Use quando o usuário pedir indenização por assédio moral,
  humilhação pelo chefe, cobrança vexatória de metas, isolamento ou perseguição,
  assédio sexual de superior ou colega, ou defesa da empresa contra essa acusação.
metadata:
  area: trabalhista
  tipo_peca: inicial
  verificado_em: 2026-11-25
---
# Assédio moral e sexual no trabalho (indenização)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: pedido de dano extrapatrimonial por conduta abusiva reiterada (assédio moral) ou por constrangimento de cunho sexual (assédio sexual), dentro de reclamação trabalhista; ou defesa da reclamada contra esse pedido.
- A peça é uma reclamação: use a estrutura de `trabalhista-reclamacao` e acrescente os tópicos desta skill. Defesa: `trabalhista-contestacao` + o roteiro de defesa em [estrutura](references/estrutura.md).
- Não usar como peça autônoma quando o objetivo é sair do emprego: aí o pedido principal é `trabalhista-rescisao-indireta` (art. 483, "e"), e esta skill entra como tópico do dano.
- Doença psíquica com nexo e pedido de estabilidade ou pensão: `trabalhista-acidente-e-doenca-ocupacional`.
- Jornada exaustiva que impede a vida fora do trabalho: `trabalhista-dano-existencial`.
- Programa preventivo, canal de denúncia, política interna: `trabalhista-compliance`.
- Notícia-crime de assédio sexual (CP art. 216-A): fora do escopo trabalhista; plugin `penal`.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Quem praticou (cargo, relação hierárquica com a vítima) e se ainda está na empresa.
2. Condutas concretas, com datas aproximadas, frequência e local (reunião, mensagem, grupo de aplicativo).
3. Provas disponíveis: mensagens, e-mails, áudios, prints, testemunhas, atas, atestados, CAT, registro no canal de denúncia.
4. Se a vítima comunicou a empresa (RH, ouvidoria, CIPA, canal) e qual foi a resposta.
5. Consequências: afastamento, tratamento médico, transferência, dispensa após a denúncia.
6. Situação do contrato (ativo ou extinto, data da extinção) e último salário contratual.
7. Para a defesa: política interna, registros de apuração, sanções aplicadas ao agressor.

## Prazo e contagem
- Prescrição: cinco anos na vigência do contrato, até dois anos após a extinção (CF art. 7º, XXIX). Registrar a data da última conduta e da extinção.
- Prazos processuais (contestação, recursos): `prazos-processuais`.

## Estrutura da peça
Fatos com linha do tempo → caracterização (moral ou sexual) → ilicitude e responsabilidade do empregador → omissão na prevenção → dano e quantificação (art. 223-G como critério orientativo) → pedidos. Roteiro em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Assédio moral**: conduta abusiva, reiterada, que degrada o ambiente e atinge a dignidade. Distinguir de cobrança legítima e de conflito pontual; o fato isolado grave pode gerar dano moral comum, sem a etiqueta de assédio.
- **Assédio sexual**: no campo trabalhista basta o constrangimento de natureza sexual não desejado; a figura penal (CP art. 216-A) exige superioridade hierárquica ou ascendência e intuito de vantagem sexual. Não importar para a reclamação os requisitos penais como condição do dano.
- **Responsabilidade do empregador**: responde pelos atos de empregados e prepostos no exercício do trabalho ou em razão dele, independentemente de culpa própria (CC arts. 932, III, e 933); solidariedade com o autor (CC art. 942, parágrafo único). Todos os que concorreram respondem na proporção da ação ou omissão (CLT art. 223-E).
- **Dever de prevenção**: empresas com CIPA devem ter regras de conduta, canal de denúncia com anonimato, apuração e capacitação ao menos anual (Lei 14.457/2022, art. 23). A ausência reforça a culpa; a existência e o uso efetivo são o núcleo da defesa.
- **Ônus da prova**: do autor quanto ao fato constitutivo (CLT art. 818, I). Pedir distribuição diversa (art. 818, § 1º) quando a prova estiver sob controle da empresa (gravações, registros do canal, apurações internas), antes da instrução (art. 818, § 2º).
- **Polo passivo**: empregador; incluir o agressor pessoa física é decisão estratégica a avaliar com o cliente.

## Fundamentos verificados
CF arts. 5º, X, e 7º, XXIX; CLT arts. 223-A a 223-G, 483 "e", 818 e 840 § 1º; CC arts. 927, 932 III, 933 e 942; Lei 14.457/2022 art. 23; CP art. 216-A; ADIs 6050, 6069 e 6082 (critérios do art. 223-G orientativos; valor acima do teto admitido), na ementa transcrita pelo TST; precedente do TST sobre assédio moral como causa de rescisão indireta. Detalhes em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Indenização por dano extrapatrimonial, com valor fundamentado nos critérios do art. 223-G, caput, e classificação da gravidade (§ 1º), sem tratá-la como teto.
- Pedidos distintos se houver dano moral e dano material do mesmo ato (art. 223-F); valores discriminados.
- Se a vítima quer sair: rescisão indireta (art. 483, "e") em tópico próprio (`trabalhista-rescisao-indireta`).
- Dispensa após denúncia: avaliar pedido de nulidade/reintegração ou indenização por dispensa discriminatória [VERIFICAR: fundamento legal específico conforme o caso].
- Distribuição dinâmica do ônus da prova e exibição de documentos (apurações internas, registros do canal, gravações).
- Valores liquidados (art. 840 § 1º); correção e juros pelo núcleo `juros-e-correcao`.

## Checklist pré-protocolo
- [ ] Linha do tempo com cada conduta, data, autor e prova correspondente.
- [ ] Moral e sexual tratados em tópicos separados, se ambos ocorreram.
- [ ] Hierarquia do agressor e comunicação à empresa documentadas.
- [ ] Prescrição conferida pela data da extinção e da última conduta.
- [ ] Valor do dano justificado critério a critério (art. 223-G), sem invocar a tabela como limite.
- [ ] Testemunhas identificadas e sem impedimento evidente.
- [ ] Pedidos liquidados; juros e correção remetidos ao núcleo.

## Erros a evitar
- Narrar "assédio" genericamente, sem fatos datados nem autor identificado.
- Confundir cobrança de metas legítima com assédio; o abuso está no modo (exposição, ameaça, ridicularização), não na meta.
- Exigir na petição os elementos do crime do art. 216-A para o dano trabalhista.
- Na defesa, limitar-se a negar: sem prova de política, canal, apuração e sanção, a negativa genérica pesa contra a empresa.
- Expor dados íntimos da vítima além do necessário; pedir segredo de justiça quando o caso o justificar.

## Integração com o núcleo
`juros-e-correcao`, `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual` (fatos só como narrados e provados), `estilo-forense`.

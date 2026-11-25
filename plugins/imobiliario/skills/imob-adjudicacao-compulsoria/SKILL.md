---
name: imob-adjudicacao-compulsoria
description: >
  Redige ação de adjudicação compulsória (CC arts. 1.417 e 1.418) ou monta o
  pedido extrajudicial no Registro de Imóveis (Lei 6.015/1973, art. 216-B)
  para o promitente comprador quitado obter o registro do imóvel quando o
  vendedor se recusa, sumiu ou morreu sem outorgar a escritura definitiva —
  com a Súmula 239/STJ (dispensa do registro da promessa). Use quando o usuário
  pedir escritura que o vendedor não passa, contrato de gaveta quitado, cessão
  de direitos sem escritura, loteadora extinta, ou escolher entre via judicial
  e cartório.
metadata:
  area: imobiliario
  tipo_peca: inicial
  verificado_em: 2026-11-25
---
# Adjudicação compulsória (judicial e extrajudicial)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: promessa de compra e venda (ou cessão/promessa de cessão) de imóvel, **preço integralmente pago**, e o promitente vendedor (ou seus sucessores/cessionários) não outorga a escritura definitiva. Também legitima o **promitente vendedor** que quer transferir e o comprador não recebe o título (art. 216-B, § 1º, só na via extrajudicial).
- Não usar:
  - preço não quitado ou discutido: cobrança/consignação ou revisão — `contratos-distrato-e-rescisao`, `contratos-analise-e-revisao-de-contrato`;
  - não há instrumento algum e a prova é só a posse longa: `imob-usucapiao-judicial` / `imob-usucapiao-extrajudicial`;
  - o comprador já tem escritura registrada e quer entrar no imóvel: `imob-imissao-na-posse`;
  - o imóvel foi penhorado em execução contra o vendedor: `imob-embargos-de-terceiro` (Súmula 84/STJ);
  - vendedor falecido com inventário aberto: avalie alvará/autorização no inventário (`sucessoes-inventario-judicial`).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Instrumento de promessa e todas as cessões, na ordem (cadeia completa até o requerente).
2. **Prova da quitação integral**: recibos, extratos, termo de quitação, declaração do vendedor.
3. Cláusula de arrependimento? (Art. 1.417 exige promessa sem arrependimento para o direito real.)
4. Matrícula atualizada: titular, ônus (hipoteca, **alienação fiduciária**, penhoras), se a promessa foi registrada.
5. Situação do vendedor: vivo, falecido (herdeiros/espólio), pessoa jurídica extinta, paradeiro.
6. Notificação para outorga da escritura e resposta.
7. ITBI: valor e possibilidade de recolhimento (exigido na via extrajudicial).
8. Estado civil do requerente e do vendedor ao tempo do contrato.

## Prazo e contagem
- Prescrição da pretensão adjudicatória: não conferida em fonte oficial [VERIFICAR: a busca no JuriBase não retornou cobertura sobre o tema; confira antes de afirmar imprescritibilidade].
- Via extrajudicial: o inadimplemento se caracteriza pela não celebração do título em **15 dias** contados da notificação extrajudicial feita pelo registrador (art. 216-B, § 1º, II).
- Prazos processuais: `prazos-processuais`.

## Estrutura da peça
Judicial: foro da situação (art. 47 do CPC) → promessa e cadeia de cessões → quitação → recusa/omissão → direito à adjudicação (arts. 1.417 e 1.418; Súmula 239) → pedidos. Extrajudicial: requerimento ao registrador com os documentos do art. 216-B, § 1º. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Quitação integral do preço** é requisito; o ônus da prova é do promitente comprador (STJ, AgInt nos EDcl no AREsp 2.425.946; REsp 2.231.032).
- **Registro da promessa é dispensável** para a adjudicação (Súmula 239/STJ; STJ, AREsp 2.256.025). O registro só confere direito real oponível a terceiros (art. 1.417).
- **Polo passivo**: promitente vendedor ou terceiros a quem os direitos foram cedidos (art. 1.418); falecido → espólio ou herdeiros; cedentes intermediários conforme a cadeia.
- **Alienação fiduciária registrada** sobre o bem: a propriedade é do credor fiduciário — a adjudicação pode tornar-se impossível e converter-se em perdas e danos (STJ, REsp 2.095.461). Cheque a matrícula antes.
- Consentimento/citação de cônjuges em ação real imobiliária: art. 73 do CPC.
- **Extrajudicial (art. 216-B)**: advogado obrigatório; não depende do registro prévio da promessa nem da regularidade fiscal do vendedor (§ 2º); a promessa ou o instrumento de cessão/sucessão serve de título (§ 3º).
- Regulamentação nacional do CNJ para o art. 216-B [VERIFICAR: provimento e artigos não conferidos — o site do CNJ recusou o acesso automatizado].

## Fundamentos verificados
- CC arts. 1.245, 1.417 e 1.418. Lei 6.015/1973, art. 216-B. CPC arts. 47 e 73.
- Súmula 239/STJ; STJ: AgInt nos EDcl no AREsp 2.425.946, REsp 2.231.032, AREsp 2.256.025, REsp 2.095.461.
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Judicial: citação; declaração/adjudicação do imóvel ao autor; sentença como título e **mandado ao registro de imóveis**; subsidiariamente, se impossível a adjudicação, conversão em perdas e danos (juros e correção pelo núcleo `juros-e-correcao`); tutela de urgência para averbar a ação na matrícula, se houver risco de alienação a terceiro (art. 300).
- Extrajudicial: notificação do promitente vendedor pelo registrador (§ 1º, II); registro do domínio em nome do requerente (§ 3º).

## Checklist pré-protocolo
- [ ] Cadeia de instrumentos completa e coerente com a matrícula
- [ ] Quitação integral provada documentalmente
- [ ] Ausência de cláusula de arrependimento (ou superação dela)
- [ ] Matrícula sem alienação fiduciária ou ônus que impeça a transferência
- [ ] Polo passivo correto (vendedor, espólio/herdeiros, cedentes)
- [ ] Via escolhida: extrajudicial (ata notarial, certidões, ITBI, procuração específica) ou judicial
- [ ] Prescrição tratada com cautela [VERIFICAR]
- [ ] Juros/correção remetidos ao núcleo (pedido subsidiário)

## Erros a evitar
- Ajuizar sem prova da quitação ("o vendedor nunca cobrou" não basta).
- Achar que a falta de registro da promessa impede a ação (Súmula 239 diz o contrário).
- Pular um elo da cadeia de cessões.
- Ignorar alienação fiduciária ou hipoteca na matrícula.
- Ir ao cartório sem recursos para o ITBI ou sem a ata notarial do art. 216-B, § 1º, III.

## Integração com o núcleo
`prazos-processuais`, `juros-e-correcao`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`, `civel-peticao-inicial`, `civel-tutela-provisoria`.

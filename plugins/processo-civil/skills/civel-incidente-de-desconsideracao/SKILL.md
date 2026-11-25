---
name: civel-incidente-de-desconsideracao
description: >
  Redige o pedido de instauração do incidente de desconsideração da
  personalidade jurídica (CPC, arts. 133 a 137) em relação civil ou empresarial
  regida pela teoria maior do art. 50 do Código Civil (desvio de finalidade ou
  confusão patrimonial), inclusive a desconsideração inversa, e a manifestação
  de defesa do sócio ou da sociedade citada. Use quando o usuário pedir para
  atingir bens de sócio ou administrador de empresa devedora fora do CDC,
  incluir sócio no polo passivo em execução ou cumprimento de sentença, alcançar
  bens que o devedor esconde em empresa (inversa) ou defender quem foi citado
  no IDPJ.
metadata:
  area: processo-civil
  tipo_peca: requerimento
  verificado_em: 2026-11-25
---
# Incidente de desconsideração da personalidade jurídica (CPC 133-137; CC 50)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: credor civil ou empresarial quer estender a obrigação da pessoa jurídica aos bens do sócio/administrador beneficiado pelo abuso (direta) ou da sociedade usada para blindar bens do sócio devedor (inversa — CC art. 50, § 3º; CPC art. 133, § 2º).
- Usar também do lado de quem foi citado no incidente (manifestação do art. 135).
- Não usar: relação de consumo, em que vale a teoria menor do art. 28, § 5º, do CDC — `consumidor-desconsideracao-personalidade-juridica`.
- Crédito tributário ou execução fiscal: `trib-*` (redirecionamento tem regime próprio). Crédito trabalhista: `trabalhista-*`.
- Só há bem alienado a terceiro, sem abuso societário: fraude à execução ou contra credores, com `civel-cumprimento-de-sentenca` ou `civel-execucao-titulo-extrajudicial`.
- Ação autônoma contra o sócio por ato próprio (responsabilidade direta do administrador): `civel-peticao-inicial`.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Título e fase: conhecimento, cumprimento de sentença ou execução de título extrajudicial; número do processo e valor atualizado.
2. Diligências patrimoniais já feitas contra a PJ e o resultado (bloqueio, Renajud, pesquisa de imóveis, certidões).
3. Ficha da Junta Comercial com quadro societário atual e histórico; quem administra de fato.
4. **Fatos concretos de abuso**, com documento: pagamento de despesas do sócio pela empresa (ou o inverso), transferência de bens ou recebíveis sem contraprestação, conta bancária comum, sucessão por empresa nova com mesmo endereço/clientes/empregados, esvaziamento patrimonial às vésperas da dívida.
5. Para a inversa: bens do devedor pessoa física registrados em nome de sociedade, integralização simulada, uso pessoal de bens sociais.
6. Pedido será feito na inicial ou em incidente?

## Prazo e contagem
- Não há prazo próprio para requerer; cabe em qualquer fase do conhecimento, no cumprimento de sentença e na execução (art. 134, caput). Atenção à prescrição da pretensão executória e à intercorrente [VERIFICAR: prazo aplicável ao caso via `verificacao-de-citacoes`].
- Citado: 15 dias para manifestar-se e requerer provas (art. 135).
- A instauração suspende o processo, salvo se o pedido vier na inicial (art. 134, §§ 2º e 3º).
- Contagem em dias úteis e termo inicial: `prazos-processuais`.

## Estrutura da peça
Pedido do credor: endereçamento ao juízo da causa → qualificação do(s) requerido(s) → histórico do crédito e das tentativas frustradas → pressupostos do art. 50 do CC, fato a fato → por que encerramento irregular e falta de bens não bastam, mas aqui há mais (Tema 1210) → pedido de instauração, comunicação ao distribuidor, citação e tutela cautelar se houver risco de dissipação → provas → pedidos. Defesa do sócio: preliminares → ausência de abuso → impugnação de cada fato → honorários. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- O requerimento deve **demonstrar os pressupostos legais específicos** (art. 134, § 4º): abuso caracterizado por desvio de finalidade (§ 1º do art. 50) ou confusão patrimonial (§ 2º).
- Encerramento irregular e inexistência de bens penhoráveis, sozinhos, **não** caracterizam o abuso (STJ, Tema 1210).
- Grupo econômico, por si só, não autoriza a medida (CC art. 50, § 4º); mera expansão ou alteração do objeto social não é desvio (§ 5º).
- Só responde o sócio ou administrador **beneficiado direta ou indiretamente** pelo abuso (caput do art. 50): individualize cada requerido.
- Legitimidade: a parte ou o Ministério Público, quando lhe couber intervir (art. 133, caput).
- Pedido na inicial dispensa o incidente; o sócio é citado como réu (art. 134, § 2º).

## Fundamentos verificados
- CPC arts. 133 a 137 (cabimento, suspensão, citação em 15 dias, decisão interlocutória, ineficácia da alienação em fraude após o acolhimento).
- CC art. 50, caput e §§ 1º a 5º (redação da Lei 13.874/2019).
- STJ, Tema 1210 (REsp 1.873.811 e REsp 1.873.187, 2ª Seção, rel. Min. Raul Araújo, julg. 07/05/2026): mero encerramento irregular ou inexistência de bens penhoráveis não caracteriza a desconsideração do art. 50.
- STJ, Corte Especial, REsp 2.072.206 (rel. Min. Ricardo Villas Bôas Cueva, julg. 13/02/2025) e EREsp 2.042.753 (rel. Min. Mauro Campbell Marques, julg. 02/04/2025): rejeitado o pedido, cabem honorários de sucumbência em favor de quem foi chamado ao incidente.
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Do credor: instauração do incidente; anotação no distribuidor (art. 134, § 1º); citação de cada requerido (art. 135); tutela de urgência cautelar (indisponibilidade/arresto) se houver risco concreto, com fundamento autônomo (`civel-tutela-provisoria`); produção das provas indicadas (ofícios, quebra de sigilo bancário/fiscal fundamentada, perícia contábil); acolhimento para incluir os requeridos no polo passivo, com declaração de ineficácia das alienações em fraude (art. 137).
- Do requerido: rejeição do pedido; honorários de sucumbência (precedentes da Corte Especial acima), com base no art. 85 do CPC [VERIFICAR: parâmetro aplicável — Tema 1076/STJ não conferido nesta skill]; liberação de constrições.
- Juros e correção do crédito: `juros-e-correcao`.

## Checklist pré-protocolo
- [ ] Teoria correta: CC art. 50 (civil/empresarial), não CDC art. 28
- [ ] Cada requerido individualizado, com o benefício que obteve do abuso
- [ ] Ao menos um fato concreto de desvio ou confusão, documentado — não só "empresa fechou e não tem bens"
- [ ] Tema 1210 enfrentado expressamente
- [ ] Diligências patrimoniais contra a PJ comprovadas
- [ ] Pedido de anotação no distribuidor e de citação
- [ ] Cautelar pedida com perigo concreto (se for o caso)
- [ ] Prescrição verificada; prazos pelo núcleo

## Erros a evitar
- Pedir a desconsideração só com base em certidão de baixa/inaptidão e penhora frustrada (Tema 1210 afasta).
- Incluir todos os sócios indistintamente, inclusive minoritário sem gestão e sem benefício.
- Confundir com redirecionamento fiscal ou com teoria menor do CDC.
- Inverter o rito: penhorar bens do sócio antes de citá-lo no incidente, salvo cautelar fundamentada.
- Na defesa, esquecer de pedir honorários quando o incidente é rejeitado.
- Na inversa, não provar que os bens da sociedade pertencem de fato ao sócio devedor.

## Integração com o núcleo
`prazos-processuais`, `juros-e-correcao`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`. Recurso contra a decisão: `civel-agravo-de-instrumento` (do relator: `civel-agravo-interno`, art. 136, parágrafo único).

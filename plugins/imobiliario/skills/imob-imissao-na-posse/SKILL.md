---
name: imob-imissao-na-posse
description: >
  Redige ação de imissão na posse do adquirente (proprietário que nunca teve a
  posse) contra o alienante ou terceiro que ocupa o imóvel, ação petitória
  fundada no art. 1.228 do CC, em procedimento comum, com tutela de urgência ou
  de evidência. Use quando o usuário pedir ação para entrar no imóvel comprado,
  arrematado ou recebido, vendedor que não entrega as chaves, ex-proprietário
  ou ocupante que permanece no imóvel após o registro, ou quando precisar
  diferenciar imissão de possessória e de despejo.
metadata:
  area: imobiliario
  tipo_peca: inicial
  verificado_em: 2026-11-25
---
# Imissão na posse

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: proprietário com título registrado (ou titular de outro direito real que confira posse) que **nunca exerceu a posse** e quer ingressar no imóvel ocupado pelo alienante, por quem dele recebeu a coisa ou por terceiro sem título oponível.
- Não usar:
  - autor que **já teve a posse** e a perdeu: `imob-reintegracao-de-posse`;
  - imóvel **locado** ao tempo da alienação: a retomada é por despejo (STJ, REsp 1.864.878): `imob-acao-de-despejo`;
  - promitente comprador **sem escritura** que quer o título: `imob-adjudicacao-compulsoria` (depois, se preciso, a imissão);
  - desfazimento do contrato de compra e venda: `contratos-distrato-e-rescisao`;
  - arrematação em leilão extrajudicial de alienação fiduciária: há regime próprio na Lei 9.514/1997 [VERIFICAR: dispositivos não conferidos nesta skill].

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Matrícula atualizada com o registro do título do autor (art. 1.245 do CC: sem registro, o alienante continua dono).
2. O título: escritura, carta de arrematação/adjudicação, formal de partilha; cláusula de entrega da posse e prazo.
3. Quem ocupa e a que título se diz ocupante (alienante, parente dele, locatário, comodatário, invasor).
4. Notificação para desocupação: data e resposta.
5. Há ação discutindo o título, usucapião ou locação em curso?
6. Benfeitorias alegadas pelo ocupante; ocupação onerosa (aluguel/taxa de ocupação pretendida).
7. Estado civil do autor (art. 73 do CPC: consentimento do cônjuge em ação real imobiliária, salvo separação absoluta).

## Prazo e contagem
- Não há prazo decadencial próprio; mas o tempo de ocupação do réu pode alimentar usucapião, que ele pode arguir em defesa (Súmula 237/STF; STJ, REsp 1.896.813). Verifique a cadeia possessória do ocupante antes de ajuizar.
- Indenização pela ocupação (perdas e danos) segue a prescrição da pretensão reparatória [VERIFICAR: prazo e termo inicial não conferidos nesta skill].
- Prazos processuais: `prazos-processuais`.

## Estrutura da peça
Foro da situação (art. 47) → título registrado → ausência de posse anterior → ocupação injusta do réu → direito de reaver (art. 1.228) → tutela provisória → indenização pela ocupação → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Natureza petitória**: a ação se funda no direito de propriedade (*ius possidendi*) e exige a higidez do título — anulado o título definitivamente, a ação perde o objeto (STJ, AgInt no REsp 2.200.316).
- **Procedimento comum** (art. 318 do CPC): a imissão não tem rito especial e **não é dúplice**; o réu não formula pedido contraposto, salvo a **retenção por benfeitorias**, que deve ser deduzida na contestação (STJ, REsp 2.055.270).
- Legitimidade passiva: quem detém a posse; se o ocupante alega título próprio (locação, comodato com o alienante), enfrente a oponibilidade.
- Litisconsórcio e consentimento conjugal: art. 73, *caput* e § 1º, I, do CPC (ação real imobiliária).

## Fundamentos verificados
- CC arts. 1.228 (*caput*) e 1.245 (§§ 1º e 2º); 1.219 (retenção do possuidor de boa-fé).
- CPC arts. 47, 73, 300, 311, 318.
- STJ: AgInt no REsp 2.200.316; REsp 2.055.270; REsp 1.896.813; REsp 1.864.878. Súmula 237/STF.
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Tutela de urgência (art. 300): título registrado + ocupação sem causa + perigo concreto (deterioração, encargos correndo, impossibilidade de uso). Atenção à irreversibilidade (art. 300, § 3º).
- Tutela da evidência (art. 311, IV): prova documental suficiente sem contraprova capaz de gerar dúvida — **não cabe liminar** nesse inciso (art. 311, parágrafo único); pedir após a contestação.
- Imissão definitiva com mandado e prazo para desocupação voluntária, sob pena de remoção.
- Indenização pela ocupação desde a notificação ou a citação (fundamentar o termo inicial); juros e correção pelo núcleo `juros-e-correcao`.
- Citação, provas, custas, honorários, valor da causa.

## Checklist pré-protocolo
- [ ] Matrícula com o título do autor **registrado**
- [ ] Prova de que o autor nunca teve a posse (senão, possessória)
- [ ] Ocupante identificado e a que título ocupa
- [ ] Locação descartada (se houver, despejo)
- [ ] Notificação de desocupação juntada
- [ ] Risco de usucapião do ocupante avaliado
- [ ] Consentimento/participação do cônjuge (art. 73)
- [ ] Tutela adequada (urgência x evidência, sem pedir liminar no art. 311, IV)
- [ ] Juros/correção remetidos ao núcleo

## Erros a evitar
- Propor imissão com contrato particular não registrado — falta o título de propriedade (art. 1.245, § 1º).
- Usar imissão contra locatário — via é o despejo.
- Tratar a imissão como possessória e pedir a liminar do art. 562.
- Ignorar a retenção por benfeitorias alegada na contestação (é apreciável, apesar do nome "pedido contraposto").
- Ajuizar sem checar ação anulatória do título ou usucapião pendentes (prejudicialidade).

## Integração com o núcleo
`prazos-processuais`, `juros-e-correcao`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`, `civel-peticao-inicial`, `civel-tutela-provisoria`.

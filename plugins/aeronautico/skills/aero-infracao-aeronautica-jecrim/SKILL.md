---
name: aero-infracao-aeronautica-jecrim
description: >
  Orienta a defesa no Juizado Especial Criminal (estadual ou federal) de
  infração de menor potencial ofensivo ligada à aviação: contravenção de abuso
  na prática da aviação (LCP art. 35), atentado culposo à segurança do
  transporte aéreo com sinistro (CP art. 261, § 3º) e crimes leves cometidos a
  bordo (CF art. 109, IX; Lei 10.259/2001), com composição civil, transação
  penal e suspensão condicional (Lei 9.099/1995). Use quando o usuário pedir
  defesa de piloto por voo baixo ou acrobacia, pouso em local não autorizado,
  termo circunstanciado por incidente a bordo, passageiro indisciplinado ou
  transação penal em caso aeronáutico.
metadata:
  area: aeronautico
  tipo_peca: outro
  verificado_em: 2026-11-25
---
# Infração aeronáutica no Juizado Especial Criminal

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: termo circunstanciado ou denúncia por (a) acrobacia ou voo baixo fora da zona permitida, ou pouso fora de local destinado (LCP art. 35); (b) atentado culposo à segurança do transporte aéreo com sinistro (CP art. 261, § 3º); (c) crime de pena máxima até 2 anos praticado a bordo (ameaça, lesão leve, injúria etc. — conferir a pena do tipo no caso).
- Não usar: atentado doloso (CP art. 261, caput e § 1º — pena acima de 2 anos): `penal-resposta-a-acusacao`, `penal-anpp`, `penal-habeas-corpus`; multa da ANAC pelo mesmo fato (`aero-recurso-multa-anac` — instâncias independentes, correm juntas); indenização à vítima (`aero-acidente-aereo-indenizacao` ou `civel-juizado-especial`).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Termo circunstanciado ou denúncia, com o tipo imputado e a pena máxima.
2. Onde ocorreu: em solo, em voo, **a bordo** de aeronave; local de pouso/decolagem.
3. Qualidade do cliente: piloto (licença, habilitação, tipo de operação), passageiro, tripulante.
4. Antecedentes: condenação definitiva a pena privativa de liberdade; transação penal nos últimos 5 anos (impedem a transação).
5. Vítima identificada? Houve dano reparável (composição civil)?
6. Provas: plano de voo, dados de radar/tráfego, NOTAM, autorização de pouso, vídeos, testemunhas, relatório da tripulação.
7. Auto de infração da ANAC sobre o mesmo fato (datas — interessa à prescrição administrativa).

## Prazo e contagem
- Recurso de apelação no JECRIM: 10 dias da ciência da sentença, por petição escrita com razões; contrarrazões em 10 dias; julgamento por turma recursal (Lei 9.099, art. 82).
- Prescrição penal e demais prazos: `prazos-processuais` e o Código Penal; se o fato também gerou multa da ANAC, a prescrição administrativa segue o prazo penal (Lei 9.873/1999, art. 1º, § 2º).

## Estrutura da peça
Competência → fase preliminar (composição civil e transação) → defesa oral antes do recebimento da denúncia → teses de mérito → suspensão condicional como alternativa → recurso. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Menor potencial ofensivo**: contravenções e crimes com pena máxima não superior a 2 anos (Lei 9.099, art. 61). A LCP art. 35 prevê prisão simples de 15 dias a 3 meses ou multa; o CP art. 261, § 3º, detenção de 6 meses a 2 anos.
- **Competência**:
  - Crime cometido **a bordo de aeronave**: Justiça Federal (CF art. 109, IX), e o Juizado Especial Federal Criminal julga os de menor potencial (Lei 10.259/2001, art. 2º).
  - **Contravenção**: a CF exclui as contravenções da competência federal no inciso IV do art. 109; se essa exclusão alcança contravenção a bordo (inciso IX) não foi conferido em jurisprudência [VERIFICAR] — sustente a competência que favorecer o cliente e documente.
  - Territorial: lugar da infração (Lei 9.099, art. 63).
- **Termo circunstanciado e flagrante**: autor encaminhado ao Juizado ou que se compromete a comparecer não fica preso em flagrante nem presta fiança (art. 69, parágrafo único).
- **Composição civil**: homologada, é título executivo; em ação privada ou pública condicionada, implica renúncia à queixa ou representação (art. 74). Lesão leve e culposa dependem de representação (art. 88).
- **Transação penal**: vedada se houve condenação definitiva a pena privativa de liberdade, transação nos 5 anos anteriores ou circunstâncias desfavoráveis (art. 76, § 2º); aceita, não gera reincidência e só fica registrada para impedir nova transação em 5 anos (§ 4º).
- **Suspensão condicional do processo**: pena mínima igual ou inferior a 1 ano; 2 a 4 anos de prova (art. 89).
- **Defesa antes do recebimento**: aberta a audiência, a defesa responde à acusação e só então o juiz recebe ou rejeita a denúncia (art. 81) — é o momento das teses de atipicidade.

## Fundamentos verificados
- Lei 9.099/1995 arts. 61, 63, 69, 72, 74, 75, 76, 81, 82, 88, 89; Lei 10.259/2001 art. 2º.
- Decreto-Lei 3.688/1941 (LCP) art. 35; Código Penal art. 261; CF art. 109, IV e IX; Lei 9.873/1999 art. 1º, § 2º.
- STJ: AgInt no AREsp 2.314.672 (prazo penal na prescrição administrativa de fato também criminoso).
Detalhe em [fundamentos](references/fundamentos.md).

## Teses de defesa (escolher conforme a prova)
- **LCP art. 35**: o tipo exige voo baixo ou acrobacia **fora da zona em que a lei o permite**, ou pouso fora de lugar destinado — prove autorização, zona permitida, emergência ou pouso de precaução. Aplicação a drones não conferida [VERIFICAR].
- **CP art. 261, § 3º**: exige culpa e sinistro; discuta nexo causal (meteorologia, falha mecânica, ordem de controle) e ausência de sinistro.
- **Fato a bordo**: contexto (crise de saúde, ordem de tripulante desproporcional), autoria, prova da tripulação.
- **Independência das instâncias**: absolvição penal por inexistência do fato ou negativa de autoria repercute no processo da ANAC; leve a sentença ao processo administrativo.

## Pedidos e requerimentos
- Designação de audiência preliminar com proposta de composição civil.
- Transação penal em termos proporcionais (ou recusa fundamentada da proposta).
- Rejeição da denúncia (art. 81) por atipicidade ou falta de justa causa.
- Suspensão condicional do processo como alternativa (art. 89).
- Absolvição; subsidiariamente, pena de multa.

## Checklist pré-protocolo
- [ ] Pena máxima do tipo conferida (cabe no art. 61?)
- [ ] Competência (federal a bordo / estadual / contravenção) definida e justificada
- [ ] Antecedentes e transação anterior levantados
- [ ] Prova técnica de voo requisitada (radar, NOTAM, autorização)
- [ ] Processo da ANAC sobre o mesmo fato mapeado
- [ ] Prazo de 10 dias para apelação controlado

## Erros a evitar
- Aceitar transação penal sem medir o impacto na licença e no processo da ANAC.
- Levar contravenção a bordo à Justiça Federal sem enfrentar o art. 109, IV, da CF.
- Tratar como menor potencial o atentado doloso do CP art. 261, caput.
- Esperar o recebimento da denúncia para apresentar as teses de atipicidade (art. 81).

## Integração com o núcleo
`prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

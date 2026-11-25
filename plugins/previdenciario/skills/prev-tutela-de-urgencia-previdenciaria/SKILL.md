---
name: prev-tutela-de-urgencia-previdenciaria
description: >
  Redige o pedido de tutela de urgência ou da evidência para implantar ou
  restabelecer benefício previdenciário ou assistencial contra o INSS (CPC, arts.
  300, 302 e 311; Lei 10.259, art. 4º), enfrentando a irreversibilidade, a
  Súmula 729/STF e o risco de devolução se a tutela cair (Tema 692/STJ; Lei
  8.213, art. 115, II). Use quando o usuário pedir liminar para o INSS implantar
  benefício, restabelecer auxílio por incapacidade cessado, BPC urgente, tutela
  antecipada previdenciária ou tutela da evidência com tese repetitiva.
metadata:
  area: previdenciario
  tipo_peca: requerimento
  verificado_em: 2026-11-25
---
# Tutela de urgência previdenciária

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: tópico de tutela na petição inicial ou petição incidental para implantar ou restabelecer benefício (incapacidade, BPC, pensão, aposentadoria), quando a prova documental já sustenta o direito e a espera causa dano à subsistência.
- Usar a tutela da evidência quando a prova for documental e houver tese de repetitivo ou súmula vinculante (CPC, art. 311, II), ou quando o INSS abusar do direito de defesa (art. 311, I).
- Não usar para recorrer de tutela negada (`prev-agravo-de-instrumento-previdenciario`) nem para pedir só que o INSS decida o requerimento (`prev-mandado-de-seguranca-demora-inss`). Técnica geral (antecedente, estabilização): `civel-tutela-provisoria`. Benefício em si: `prev-beneficio-por-incapacidade`, `prev-bpc-loas`, `prev-pensao-por-morte`, `prev-inicial-aposentadoria`.

## Entradas mínimas (perguntar o que faltar; nunca supor fatos)
1. Benefício pretendido e decisão do INSS (indeferimento, cessação, demora), com data e motivo.
2. Prova de cada requisito: CNIS (qualidade de segurado, carência), laudos e atestados recentes, CadÚnico/renda, certidão de óbito e dependência, conforme o benefício.
3. Situação de urgência: renda atual da família, despesas essenciais, doença, idade, dependentes.
4. Se o segurado já recebeu valores por tutela antes, ou se há benefício ativo que possa ser inacumulável [VERIFICAR: Lei 8.213, art. 124].
5. Rito: procedimento comum, JEF ou competência delegada.

## Prazo e contagem
- Não há prazo próprio para pedir a tutela; quanto antes, menor o dano. A cessação recente de benefício por incapacidade reforça o perigo.
- Recurso contra a decisão: 15 dias úteis (CPC, art. 1.003, § 5º); no JEF, conferir o regimento. Ver `prazos-processuais`.

## Estrutura da peça
Tópico próprio, depois dos fatos e do direito: probabilidade (requisito por requisito, com documento) → perigo de dano (concreto) → reversibilidade (verba alimentar, desconto legal, Súmula 729/STF) → tutela da evidência, se cabível → pedido com prazo e multa. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Urgência: probabilidade do direito + perigo de dano ou risco ao resultado útil (CPC, art. 300). Perigo de irreversibilidade impede a tutela antecipada (art. 300, § 3º) — enfrente-o expressamente.
- No JEF, o juiz pode deferir medidas cautelares no curso do processo para evitar dano de difícil reparação (Lei 10.259, art. 4º).
- Em benefício por incapacidade, sem perícia judicial o juiz costuma esperar o laudo: pedir perícia antecipada ou com urgência e juntar laudos particulares recentes e detalhados.
- Responsabilidade: se a sentença for desfavorável, a parte responde pelo prejuízo da efetivação (CPC, art. 302, I); em matéria previdenciária, o STJ fixou o dever de devolver com desconto de até 30% (Tema 692) e a lei prevê o desconto (Lei 8.213, art. 115, II). **Informe o cliente por escrito antes de pedir.**
- A restrição da ADC 4 não alcança tutela em causa previdenciária (Súmula 729/STF).

## Fundamentos verificados
- CPC, arts. 300, 302 e 311; Lei 10.259, art. 4º; Lei 8.213, art. 115, II.
- Súmula 729/STF.
- Tema 692/STJ (Pet 12.482/DF, 1ª Seção, julg. 11/05/2022): reformada a tutela, devolução dos valores, admitido desconto de até 30% do benefício em manutenção.
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Tutela de urgência (ou da evidência) para implantar/restabelecer o benefício X em prazo fixado, com multa diária e intimação da agência responsável pelo cumprimento.
- Subsidiariamente: perícia médica ou social com urgência e reapreciação da tutela após o laudo.
- Confirmação da tutela na sentença (com efeito imediato — CPC, art. 1.012, § 1º, V).

## Checklist pré-protocolo
- [ ] Cada requisito do benefício provado por documento
- [ ] Perigo concreto descrito (não basta "verba alimentar" genérica)
- [ ] Irreversibilidade e Tema 692 enfrentados na peça
- [ ] Cliente informado por escrito do risco de devolução
- [ ] Ausência de benefício inacumulável ativo conferida
- [ ] Pedido com prazo, multa e destinatário do cumprimento
- [ ] Tutela da evidência: tese repetitiva ou súmula vinculante indicada com número

## Erros a evitar
- Pedir tutela sem prova mínima da incapacidade ou da miserabilidade e queimar a credibilidade do pedido.
- Esconder do cliente o risco de devolução (Tema 692).
- Usar a tutela da evidência do art. 311, II, sem tese de repetitivo ou súmula vinculante pertinente.
- Pedir "pagamento dos atrasados" em tutela: o pedido é implantação; atrasados vêm na sentença, com juros e correção pelo núcleo `juros-e-correcao`.

## Integração com o núcleo
`prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`, `juros-e-correcao` (só para os atrasados na sentença).

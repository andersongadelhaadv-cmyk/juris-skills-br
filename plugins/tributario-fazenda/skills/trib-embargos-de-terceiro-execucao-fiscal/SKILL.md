---
name: trib-embargos-de-terceiro-execucao-fiscal
description: >
  Redige embargos de terceiro contra penhora, arresto ou indisponibilidade em
  execução fiscal (CPC arts. 674 a 681, aplicados pela LEF art. 1º), enfrentando
  a fraude à execução fiscal do CTN art. 185 e o Tema 290/STJ (marco na
  inscrição em dívida ativa, presunção absoluta, Súmula 375 inaplicável) e a
  reserva de bens do parágrafo único. Use quando o usuário pedir embargos de
  terceiro em execução fiscal, comprador de imóvel ou veículo penhorado por
  dívida tributária do vendedor, bem bloqueado por dívida fiscal de outra
  pessoa, meação do cônjuge em execução fiscal, ou honorários nesses embargos.
metadata:
  area: tributario-fazenda
  tipo_peca: inicial
  verificado_em: 2026-11-25
---
# Embargos de terceiro em execução fiscal

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: quem **não é parte** na execução fiscal sofre constrição sobre bem que possui ou de que é titular (CPC art. 674): adquirente de imóvel ou veículo do devedor, cônjuge ou companheiro na defesa da meação ou de bens próprios, possuidor por promessa de compra e venda, atingido sem ter participado de incidente de desconsideração, credor com garantia real não intimado.
- Não usar:
  - execução cível comum (credor privado), sobretudo de imóvel: `imob-embargos-de-terceiro` — lá vale a Súmula 375/STJ, aqui não;
  - o próprio executado ou o sócio já incluído no polo passivo: `trib-embargos-a-execucao-fiscal`, `trib-excecao-pre-executividade-fiscal`, `trib-defesa-redirecionamento-socio`;
  - bloqueio em medida cautelar fiscal contra o próprio requerido: `trib-defesa-cautelar-fiscal`.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Número da execução fiscal, juízo, exequente, executado, ato de constrição e data.
2. Data da **inscrição em dívida ativa** de cada crédito executado (consta da CDA) e data da citação do devedor.
3. Título do embargante e sua data: escritura, promessa (com data certa: firma reconhecida, registro, pagamento rastreável), recibo de veículo, partilha.
4. Cadeia de alienações (se o embargante comprou de quem comprou do devedor).
5. Patrimônio remanescente do devedor na data da alienação (reserva de bens suficientes).
6. Prova da posse: contas, IPTU, financiamento, documentos do veículo.
7. Quando e como o embargante soube da constrição; fase da execução (houve arrematação ou adjudicação? carta assinada?).
8. Cônjuge: regime de bens e destinação da dívida.

## Prazo e contagem
- Na execução: até 5 dias depois da adjudicação, da alienação por iniciativa particular ou da arrematação, sempre antes da assinatura da carta (CPC art. 675). Terceiro identificado deve ser intimado pessoalmente (parágrafo único).
- Contestação do embargado: 15 dias (art. 679); prazos da Fazenda e contagem em dias úteis: `prazos-processuais`.

## Estrutura da peça
Distribuição por dependência ao juízo da execução fiscal (art. 676) → qualidade de terceiro → posse/domínio e data do título → inexistência de fraude (marco do Tema 290 ou reserva de bens) → liminar (art. 678) → pedidos. Roteiro em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Petição com prova sumária da posse ou do domínio e da qualidade de terceiro, documentos e rol de testemunhas (art. 677); polo passivo: o exequente e, se foi ele quem indicou o bem, também o executado (§ 4º).
- **Fraude à execução fiscal**: presume-se fraudulenta a alienação ou oneração de bens por sujeito passivo com crédito tributário **inscrito em dívida ativa** (CTN art. 185, redação da LC 118/2005), salvo reserva de bens ou rendas suficientes ao total pago da dívida (parágrafo único).
- **Tema 290/STJ** (REsp 1.141.990): Súmula 375/STJ não se aplica à execução fiscal; para alienações a partir de 09/06/2005, basta a inscrição em dívida ativa; antes disso, o marco é a citação; a presunção é absoluta e a boa-fé do adquirente é irrelevante (AgInt no AREsp 2.212.660, 1ª Turma, 2025; AgInt no REsp 1.982.766, 1ª Turma, 2022). Alienações sucessivas e cautelas na compra também não afastam a fraude (AgInt no REsp 1.853.907, 1ª Turma, 2023).
- **Teses viáveis do terceiro**, portanto:
  1. título com data certa **anterior à inscrição** (ou à citação, se anterior a 09/06/2005);
  2. o devedor reservou bens ou rendas suficientes na data da alienação — o tribunal deve examinar essa exceção (AgInt no REsp 1.820.873, 1ª Turma, 2023);
  3. o crédito não é tributário — o art. 185 do CTN trata de crédito tributário [VERIFICAR: regra de fraude para dívida ativa não tributária no tribunal local];
  4. o bem nunca foi do executado, ou o embargante defende meação/bem próprio.
- Promitente comprador sem registro tem legitimidade se tiver posse (Súmula 84/STJ) — mas a data certa da promessa é decisiva diante do art. 185.
- Bem de família alienado em fraude à execução fiscal: o STJ afastou a proteção da Lei 8.009/1990 (AgInt no AREsp 2.186.364, 2ª Turma, 2025). Avalie o risco antes de insistir.

## Fundamentos verificados
CPC arts. 674 a 681; LEF art. 1º; CTN art. 185 (LC 118/2005); Súmulas 84, 303 e 375/STJ; Tema 290/STJ (pelos acórdãos indicados); Tema 872/STJ; AgInt no REsp 1.820.873; AgInt no AREsp 2.186.364. Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Liminar (art. 678): suspensão das medidas constritivas e manutenção ou reintegração provisória da posse; caução pode ser exigida, salvo hipossuficiência.
- Audiência preliminar para prova da posse, se necessário (art. 677, § 1º).
- Procedência: cancelamento da constrição e reconhecimento do domínio ou da posse (art. 681); ofício ao registro de imóveis ou ao órgão de trânsito.
- Honorários pela causalidade: quem deu causa à constrição (Súmula 303/STJ); se o embargante não registrou ou não atualizou o título, ele arca, salvo se a Fazenda resistir à pretensão após conhecer a alienação (Tema 872/STJ).
- Eventuais valores: `juros-e-correcao`.

## Checklist pré-protocolo
- [ ] Data da inscrição de cada CDA × data certa do título do embargante
- [ ] Data da citação do devedor, se a alienação for anterior a 09/06/2005
- [ ] Prova da reserva de bens do devedor (se for a tese)
- [ ] Tempestividade (art. 675) e carta ainda não assinada
- [ ] Distribuição por dependência ao juízo da execução fiscal
- [ ] Polo passivo conforme art. 677, § 4º
- [ ] Risco de honorários avaliado (Tema 872)

## Erros a evitar
- Fundar a defesa na boa-fé do adquirente ou na falta de averbação da penhora (Súmula 375 não se aplica — Tema 290).
- Usar a data do registro quando o título tem data certa anterior — e vice-versa, apresentar contrato sem data certa.
- Confundir com execução cível e usar o modelo de `imob-embargos-de-terceiro` sem adaptar a fraude.
- Ignorar a cadeia de alienações: a fraude alcança aquisições sucessivas.
- Pedir honorários contra a Fazenda quando o próprio embargante não registrou o título e a Fazenda não resistiu.

## Integração com o núcleo
`prazos-processuais`, `juros-e-correcao`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`, `civel-tutela-provisoria`.

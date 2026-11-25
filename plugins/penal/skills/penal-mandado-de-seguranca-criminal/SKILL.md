---
name: penal-mandado-de-seguranca-criminal
description: >
  Redige mandado de segurança em matéria penal (CF art. 5º, LXIX; Lei
  12.016/2009) contra ato de juiz criminal, delegado ou membro do MP que viole
  direito líquido e certo sem tocar a liberdade de locomoção: acesso aos autos
  do inquérito (SV 14), restituição de bem apreendido, prerrogativas do
  advogado, habilitação de assistente, quebra de sigilo de terceiro. Use quando
  o usuário pedir mandado de segurança criminal, MS contra juiz criminal ou
  delegado, ou quando o ato não puder ser atacado por habeas corpus nem por
  recurso com efeito suspensivo.
metadata:
  area: penal
  tipo_peca: inicial
  verificado_em: 2026-11-25
---
# Mandado de segurança em matéria penal

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: ato ilegal ou abusivo de autoridade no inquérito ou no processo penal que fere direito líquido e certo **não amparado por habeas corpus** (CF 5º LXIX): negativa de acesso a elementos já documentados (SV 14), apreensão de bem de terceiro ou sem interesse probatório quando inexistente via própria eficaz, violação de prerrogativa profissional, indeferimento de habilitação de assistente de acusação, ordem dirigida a terceiro não investigado.
- Não usar: ameaça ou restrição à locomoção do cliente, ainda que indireta (`penal-habeas-corpus`); decisão sujeita a recurso com efeito suspensivo ou decisão transitada em julgado (Lei 12.016, art. 5º, II e III; Súmula 267/STF); para dar efeito suspensivo a recurso criminal do MP (Súmula 604/STJ); MS contra ato administrativo comum (`adm-mandado-de-seguranca`); MS tributário (`trib-mandado-de-seguranca`); decisões do juiz da execução (`penal-agravo-em-execucao`).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Ato impugnado: o que foi decidido ou feito, por quem (cargo, juízo, delegacia), em que data, e **data da ciência** pelo cliente.
2. Prova documental pré-constituída do ato e do direito (cópias, certidões, protocolo do pedido negado).
3. Qual recurso caberia contra o ato e se ele tem efeito suspensivo.
4. Quem é o impetrante (investigado, terceiro proprietário, advogado, vítima) e a pessoa jurídica a que a autoridade se vincula.
5. Urgência concreta (perecimento do bem, audiência marcada, prazo de defesa correndo).
6. Se o MS for do MP ou do assistente contra decisão favorável ao réu: identificar o réu, que é litisconsorte necessário (Súmula 701/STF).

## Prazo e contagem
- Decadência: 120 dias contados da ciência do ato pelo interessado (Lei 12.016, art. 23). Registre a data da ciência com documento.
- Informações da autoridade em 10 dias; parecer do MP em 10 dias; decisão em 30 dias (arts. 7º, I, e 12).
- Contagem e prazos recursais: `prazos-processuais`.

## Estrutura da peça
Competência (tribunal a que se vincula a autoridade judicial; juízo de 1º grau se a autoridade for policial) → partes e autoridade coatora → cabimento (por que não HC e não recurso) → tempestividade → direito líquido e certo com prova documental → liminar → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Direito líquido e certo = fatos provados por documento já na inicial; não há instrução probatória.
- Contra ato judicial: só quando não houver recurso com efeito suspensivo ou correição (Lei 12.016, art. 5º, II; Súmula 267/STF). O STJ aplica a Súmula 267 a MS contra decisão de juízo criminal com recurso próprio existente (AgRg no RMS 73.168).
- Indicar a autoridade coatora e a pessoa jurídica a que ela pertence (art. 6º).
- Competência originária por regimento interno e Constituição Estadual [VERIFICAR: regimento do tribunal competente].
- Não há honorários de sucumbência (art. 25).

## Fundamentos verificados
- CF 5º LXIX; Lei 12.016/2009, arts. 1º, 5º, 6º, 7º, 10, 12, 14, 18, 23 e 25.
- SV 14/STF (acesso do defensor a elementos documentados); Súmulas 267 e 701/STF; Súmula 604/STJ.
- STJ, AgRg no RMS 73.168 (Súmula 267 em matéria criminal).
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
1. Liminar para suspender o ato ou determinar a providência (art. 7º, III), com prazo de cumprimento.
2. Notificação da autoridade coatora para informações em 10 dias e ciência ao órgão de representação da pessoa jurídica (art. 7º, I e II).
3. Citação do réu como litisconsorte, quando o impetrante for o MP ou o assistente (Súmula 701/STF).
4. Vista ao MP.
5. Concessão da segurança, confirmando a liminar.

## Checklist pré-protocolo
- [ ] Data da ciência documentada e menos de 120 dias
- [ ] Demonstração expressa de que não cabe HC nem recurso com efeito suspensivo
- [ ] Toda prova juntada com a inicial (não há dilação probatória)
- [ ] Autoridade coatora e pessoa jurídica corretamente indicadas
- [ ] Competência conferida no regimento interno
- [ ] Litisconsorte necessário incluído quando o caso exigir
- [ ] Liminar com fundamento relevante e risco de ineficácia demonstrados

## Erros a evitar
- Impetrar MS quando o caso é de HC (qualquer reflexo na locomoção) ou quando há recurso com efeito suspensivo.
- Usar MS para rediscutir prova ou mérito da imputação.
- Pedir acesso a diligência ainda em curso: a SV 14 cobre elementos **já documentados**.
- Deixar a ciência sem data comprovada e perder os 120 dias.
- Esquecer o réu no MS do MP (nulidade por falta de litisconsorte, Súmula 701/STF).

## Integração com o núcleo
`prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

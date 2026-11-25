---
name: amb-defesa-auto-de-infracao
description: >
  Redige a defesa administrativa contra auto de infração ambiental lavrado pelo
  IBAMA, ICMBio ou por órgão estadual ou municipal do SISNAMA, com base nos arts.
  70 a 76 da Lei 9.605/1998, no Decreto 6.514/2008, na Lei 9.873/1999 e na LC
  140/2011. Use quando o cliente receber auto de infração ambiental, multa do
  IBAMA, termo de embargo, apreensão ou interdição e precisar apresentar defesa
  ou impugnação no prazo de 20 dias, discutir prescrição, nulidade do auto,
  competência do órgão autuante, culpa, dosimetria da multa ou pedir conversão
  da multa em serviços ambientais.
metadata:
  area: ambiental
  tipo_peca: contestacao
  verificado_em: 2026-11-25
---
# Defesa em auto de infração ambiental

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: primeira manifestação do autuado no processo administrativo sancionador ambiental, federal (IBAMA, ICMBio) ou estadual/municipal (órgão do SISNAMA), contra auto de infração e medidas administrativas lançadas com ele (embargo, apreensão, suspensão).
- Não usar:
  - já houve decisão de 1ª instância → `amb-recurso-auto-de-infracao`;
  - processo já encerrado e crédito em cobrança → ação anulatória ou embargos à execução fiscal (`trib-acao-anulatoria`, `trib-embargos-a-execucao-fiscal`);
  - ilegalidade evidente provada só com documentos e urgência (embargo que paralisa a atividade) → avaliar `amb-mandado-de-seguranca-licenciamento` ou `adm-mandado-de-seguranca`;
  - ação civil pública de reparação do dano → `civel-contestacao` (a esfera é outra);
  - crime ambiental → plugin `penal`.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Cópia integral do auto de infração, do relatório de fiscalização e dos termos lavrados juntos (embargo, apreensão, depósito).
2. Data da ciência do auto e a forma (pessoal, postal com AR, edital, eletrônica).
3. Órgão autuante e esfera (federal, estadual, municipal) e qual órgão licencia a atividade.
4. Data do fato (ou da cessação, se infração permanente ou continuada) — decisiva para a prescrição.
5. Licenças, autorizações, CAR, protocolos e condicionantes existentes na data do fato.
6. Quem praticou a conduta (o autuado, empregado, arrendatário, terceiro, possuidor anterior).
7. Valor da multa, enquadramento legal indicado e critérios de majoração usados.
8. Antecedentes do autuado e porte econômico; documentos de atenuantes.
9. Objetivo do cliente: anular, reduzir, converter em serviços ou pagar com desconto.

## Prazo e contagem
- 20 dias da ciência do auto para defesa (Lei 9.605/1998, art. 71, I; Decreto 6.514/2008, art. 113). No mesmo prazo o autuado pode optar por solução legal: pagamento com desconto, parcelamento ou conversão em serviços (Decreto 6.514/2008, art. 96, § 5º).
- Defesa fora do prazo, por ilegítimo ou a órgão incompetente não é conhecida (art. 117 do Decreto).
- Procuração: juntar com a defesa; o art. 116 admite pedir até 15 dias para juntá-la.
- Estados e municípios: conferir a lei estadual/municipal de processo administrativo, que pode fixar prazo diverso.
- Contagem administrativa não segue automaticamente o CPC: confira a regra do órgão e use `prazos-processuais`.

## Estrutura da peça
Endereçamento à unidade autuante → qualificação e tempestividade → síntese do auto → preliminares (prescrição, nulidade, incompetência) → mérito (fato, autoria, culpa) → dosimetria → medidas administrativas → pedido subsidiário de conversão → provas → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Forma:** por escrito, com fatos, fundamentos e especificação justificada das provas (art. 115 do Decreto). O ônus de provar o alegado é do autuado (art. 118): junte tudo já com a defesa.
- **Prescrição punitiva (federal):** 5 anos da prática do ato ou da cessação (Lei 9.873/1999, art. 1º; Decreto 6.514/2008, art. 21). Interrupções: art. 2º da Lei 9.873/1999 e art. 22 do Decreto.
- **Prescrição intercorrente (federal):** processo paralisado por mais de 3 anos, pendente de julgamento ou despacho (Lei 9.873/1999, art. 1º, § 1º). Basta despacho que impulsione de fato o feito; certificações vazias e movimentações repetitivas não afastam a paralisação (STJ, REsp 2.223.324; AREsp 3.195.730).
- **Estados e municípios:** o STJ não aplica a Lei 9.873/1999 a processos estaduais e municipais (AgInt no REsp 2.018.177) e não extrai prescrição intercorrente do Decreto 20.910/1932 (AgInt nos EDcl no REsp 2.075.288). Busque lei local específica.
- **Nulidade do auto:** requisitos do art. 97 do Decreto (identificação do autuado, descrição clara e objetiva, dispositivos infringidos, sem rasuras). Vício que obrigaria a mudar o fato descrito é insanável (art. 100, § 1º); erro só de enquadramento é retificável (art. 100, § 3º) — não aposte nele como tese principal.
- **Competência:** cabe ao órgão licenciador lavrar o auto contra atividade licenciada; os demais entes podem fiscalizar, e prevalece o auto do licenciador (LC 140/2011, art. 17, caput e § 3º). O STJ admite atuação do IBAMA mesmo com licença estadual (REsp 1.971.073): a tese de incompetência só se sustenta com prova de auto do licenciador sobre o mesmo fato ou de duplicidade (Lei 9.605/1998, art. 76).

## Fundamentos verificados
- Lei 9.605/1998, arts. 70 a 76; Decreto 6.514/2008, arts. 3º, 4º, 21, 22, 96 a 100, 113 a 126, 139 a 145.
- Lei 9.873/1999, arts. 1º, 1º-A e 2º; Lei 9.784/1999, arts. 2º e 50 (motivação, aplicação subsidiária — art. 69).
- LC 140/2011, art. 17; CF, art. 5º, LIV e LV.
- Responsabilidade administrativa ambiental exige dolo ou culpa (STJ, AgInt no REsp 2.240.077; AgInt nos EDcl no REsp 1.967.742).
- Multa não depende de advertência prévia (STJ, Tema repetitivo 1159, REsp 1.993.783).
Detalhe e ressalvas em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Reconhecimento da prescrição (punitiva ou intercorrente) e arquivamento.
- Nulidade do auto (vício insanável) ou da autuação por incompetência/duplicidade.
- Insubsistência por ausência de conduta, autoria ou culpa.
- Subsidiariamente: redução da multa ao mínimo ou ao patamar proporcional (art. 4º do Decreto: gravidade, antecedentes, situação econômica) e substituição por advertência quando cabível.
- Levantamento ou revisão do embargo/apreensão (a decisão deve apreciá-los, art. 124 do Decreto).
- Subsidiariamente: conversão da multa em serviços ambientais (arts. 139 a 145 do Decreto); pedido até as alegações finais (art. 142), com desconto maior se feito já na defesa (art. 143, § 2º — confira os percentuais vigentes no dia).
- Produção de provas especificadas (perícia, vistoria, testemunhas, imagens de satélite) e intimação para alegações finais (art. 122).

## Checklist pré-protocolo
- [ ] Data da ciência documentada e prazo de 20 dias conferido
- [ ] Esfera do órgão definida (federal x estadual/municipal) e lei de processo aplicável
- [ ] Prescrição punitiva e intercorrente calculadas com datas na peça
- [ ] Requisitos do art. 97 conferidos item a item no auto
- [ ] Órgão licenciador identificado (art. 17 da LC 140/2011) e existência de outro auto sobre o mesmo fato
- [ ] Culpa/autoria enfrentadas com documento (contrato, B.O., laudo)
- [ ] Critérios de majoração do relatório de fiscalização impugnados um a um
- [ ] Decisão do cliente sobre conversão ou pagamento com desconto registrada por escrito
- [ ] Procuração e atos constitutivos juntados
- [ ] Juros e correção remetidos ao núcleo

## Erros a evitar
- Defender só o mérito e perder a prescrição intercorrente: leia o histórico de movimentações inteiro.
- Aplicar a Lei 9.873/1999 a auto estadual ou municipal sem lei local que a adote.
- Alegar "faltou advertência prévia" como nulidade: o Tema 1159 do STJ afasta.
- Sustentar incompetência do IBAMA só porque há licença estadual (REsp 1.971.073).
- Deixar a conversão para depois das alegações finais: precluiu (art. 142).
- Confundir a sanção com a reparação do dano: a reparação é imprescritível (STF, Tema 999) e não sai pela defesa administrativa.
- Assinar termo de compromisso de conversão sem avisar o cliente de que implica renúncia ao recurso (art. 146, § 4º).

## Integração com o núcleo
`prazos-processuais`, `juros-e-correcao`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

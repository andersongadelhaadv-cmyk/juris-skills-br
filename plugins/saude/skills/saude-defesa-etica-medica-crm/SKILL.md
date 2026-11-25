---
name: saude-defesa-etica-medica-crm
description: >
  Redige a defesa do médico em sindicância e processo ético-profissional (PEP)
  no Conselho Regional de Medicina — manifestação preliminar, defesa prévia,
  alegações finais, sustentação oral — e o recurso ao CFM, com base na Lei
  3.268/1957, na Lei 6.838/1980 (prescrição) e no Código de Processo
  Ético-Profissional (Resolução CFM 2.306/2022, com as alterações da
  2.424/2025). Use quando o usuário pedir defesa de médico no CRM, resposta a
  denúncia ética, defesa prévia em PEP, alegações finais no CRM, recurso ao
  CFM contra censura, suspensão ou cassação, prescrição da punição ética,
  interdição cautelar ou revisão de condenação ética.
metadata:
  area: saude
  tipo_peca: contestacao
  verificado_em: 2026-11-25
---
# Defesa ético-disciplinar do médico no CRM e recurso ao CFM

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: médico denunciado ou investigado no CRM — sindicância (fase investigativa), PEP (fase acusatória), interdição cautelar, julgamento, recurso ao CFM, pedido de revisão após o trânsito.
- Não usar: ação de indenização por erro médico (`saude-defesa-do-medico` para a contestação; `saude-indenizacao-erro-medico` para a inicial); processo penal pelo mesmo fato (`penal-resposta-a-acusacao`); servidor público médico em PAD do ente (`adm-defesa-em-pad`); anulação judicial da decisão do conselho (`adm-mandado-de-seguranca` ou `civel-peticao-inicial`). A jurisdição ética não afasta a comum quando o fato é crime (Lei 3.268/1957, art. 21, p.ú.).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Fase atual e cópia integral dos autos (denúncia, relatório conclusivo da sindicância, portaria de instauração, mandado de citação, artigos do Código de Ética Médica imputados).
2. Data do fato, data em que o CRM tomou conhecimento, data da citação e da juntada do comprovante (contagem de prazo e prescrição).
3. Prontuário, termos de consentimento, prescrições, registros do hospital, escalas, protocolos clínicos usados.
4. Versão do médico, por escrito, com a cronologia do atendimento.
5. Testemunhas possíveis (até 3 na defesa prévia), pareceres técnicos, literatura.
6. Antecedentes éticos, TAC anterior, processos judiciais pelo mesmo fato.
7. Houve proposta de conciliação, TAC ou interdição cautelar?

## Prazo e contagem (CPEP)
- Prazos **contínuos**, contados da juntada aos autos do comprovante da citação/intimação, excluindo o dia do começo e incluindo o do vencimento; início e fim prorrogados se cair em dia sem expediente (arts. 131 e 132). Suspensão entre 20/12 e 20/01 (art. 13).
- Citação por aplicativo/e-mail: cumprida com a confirmação de recebimento em até 3 dias; prazo começa no dia útil seguinte à certificação (art. 41, § 3º).
- Defesa prévia: **30 dias** (art. 43, § 1º). Alegações finais: **15 dias**, sucessivos, primeiro o denunciante (art. 83). Manifestação após diligências: 10 dias (art. 90, § 2º). Suspeição: 15 dias do conhecimento do fato (art. 109).
- Recurso da decisão do PEP: **30 dias** da juntada do comprovante de intimação, com efeito devolutivo e suspensivo (art. 100 e § 1º); contrarrazões em 30 dias (art. 101). Recurso contra interdição cautelar: **5 dias** (art. 31).
- Prescrição: ver Requisitos. Contagem de prazo judicial posterior: `prazos-processuais`.

## Estrutura da peça
Sindicância: manifestação preliminar objetiva. PEP: preliminares → prescrição → mérito por artigo imputado → provas → pedido. Recurso: tempestividade → nulidades → mérito → dosimetria. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Sindicância é investigativa**, sem contraditório pleno, mas admite manifestação preliminar escrita do denunciado (art. 15, §§ 1º e 2º). Use-a para evitar a instauração do PEP: documento, prontuário, cronologia. Não há recurso do denunciado contra a instauração do PEP (art. 21, § 6º).
- **Conciliação e TAC**: só fora dos casos de lesão corporal grave, violação à dignidade sexual ou óbito (arts. 22 e 23, § 2º); vedado acerto pecuniário na conciliação (art. 22, § 4º); TAC não cabe em sindicância com denunciante no polo ativo (art. 26); descumprido, instaura-se o PEP (art. 27, p.ú.); quem firma TAC fica impedido de firmar outro, sobre qualquer assunto, por 5 anos (art. 28).
- **Prescrição**: a Lei 6.838/1980 fixa 5 anos "contados da data de verificação do fato" (art. 1º); o CPEP conta 5 anos do "efetivo conhecimento do fato pelo CRM" (art. 116), interrompidos pela citação ou conhecimento expresso, pelo protocolo da defesa prévia e pela decisão condenatória recorrível (art. 117). Processo paralisado há mais de 3 anos pendente de despacho ou julgamento é arquivado (Lei 6.838, art. 3º; CPEP, art. 118). Quando o termo inicial muda o resultado, sustente a regra da lei sobre a da resolução [VERIFICAR: jurisprudência sobre o termo inicial não encontrada no JuriBase].
- **Nulidades**: alegar na primeira oportunidade, sob pena de preclusão, salvo nulidade absoluta (art. 115); demonstrar prejuízo (art. 110). Mandado de citação sem o relatório conclusivo da sindicância é vício a apontar (art. 40, p.ú.).
- **Impedimento/suspeição** do sindicante, instrutor ou relator: petição específica (arts. 108 e 109).
- **Interdição cautelar**: exige probabilidade de autoria e materialidade, gravidade concreta e atualidade (até 6 meses do conhecimento dos fatos), referendo do CFM; decisão sem esses elementos é nula (art. 30, §§ 2º a 4º).

## Fundamentos verificados
- Lei 3.268/1957: art. 21 (competência disciplinar do CRM; jurisdição comum preservada) e art. 22 (penas: advertência confidencial, censura confidencial, censura pública, suspensão até 30 dias, cassação *ad referendum* do CFM; gradação; oitiva do acusado; recurso ao CFM em 30 dias).
- Lei 6.838/1980, arts. 1º a 3º (prescrição quinquenal, interrupção, arquivamento após 3 anos de paralisação).
- CPEP (Res. CFM 2.306/2022, alterada pela 2.424/2025), dispositivos citados acima e em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Sindicância: arquivamento por ausência de indícios de materialidade/autoria (art. 19, III).
- PEP: acolhimento das preliminares e da prescrição; absolvição por artigo imputado; subsidiariamente, pena mínima na gradação do art. 22 da Lei 3.268/1957, confidencial em vez de pública.
- Produção de prova: oitiva de até 3 testemunhas, juntada de prontuário e pareceres, diligências.
- Recurso: reforma integral; subsidiariamente, redução da pena; lembrar que o agravamento só ocorre com recurso do denunciante (art. 100, § 2º).
- Revisão (após o trânsito): prova nova que possa inocentar ou prova falsa na condenação; sem efeito suspensivo; sem agravamento (arts. 121 e 124).

## Checklist pré-protocolo
- [ ] Data de juntada do comprovante de citação/intimação e prazo contínuo conferidos (inclui recesso 20/12–20/01)
- [ ] Prescrição calculada pelos dois termos iniciais (fato x conhecimento pelo CRM)
- [ ] Cada artigo do Código de Ética Médica imputado respondido em tópico próprio
- [ ] Nulidades arguidas nesta primeira oportunidade
- [ ] Até 3 testemunhas qualificadas (nome, profissão, telefone, e-mails e endereço)
- [ ] Procuração com telefone e endereços do advogado (art. 43, § 3º)
- [ ] Prontuário juntado com cuidado de sigilo (processo é sigiloso)
- [ ] No recurso: competência (Câmara do CFM ou Pleno) conforme a pena

## Erros a evitar
- Tratar a sindicância como mera formalidade e só se defender no PEP.
- Contar prazo em dias úteis (o CPEP usa dias contínuos).
- Defesa genérica, sem enfrentar cada artigo imputado e a conduta descrita no relatório conclusivo.
- Deixar de arguir nulidade relativa na primeira manifestação.
- Juntar prova clínica sem cronologia e sem explicar a conduta à luz da literatura.
- Admitir TAC sem medir o impedimento de firmar outro no futuro.

## Integração com o núcleo
`prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

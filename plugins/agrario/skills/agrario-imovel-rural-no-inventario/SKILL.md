---
name: agrario-imovel-rural-no-inventario
description: >
  Prepara o dossiê e o plano de partilha do imóvel rural no inventário judicial
  ou extrajudicial — CCIR (Lei 4.947/1966, art. 22, § 2º), ITR dos últimos cinco
  exercícios (Lei 9.393/1996, art. 21), CAR (Lei 12.651/2012, art. 29),
  georreferenciamento e certificação no INCRA, fração mínima de parcelamento e
  indivisibilidade abaixo do módulo (Estatuto da Terra, art. 65). Use quando o
  usuário pedir inventário com fazenda, sítio ou chácara rural, lista de
  documentos do imóvel rural para a partilha, exigência do cartório sobre CCIR,
  ITR ou georreferenciamento, ou divisão de terra rural entre herdeiros.
metadata:
  area: agrario
  tipo_peca: outro
  verificado_em: 2026-11-25
---
# Imóvel rural no inventário

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: (a) montar a documentação do imóvel rural para o inventário (judicial ou em cartório); (b) planejar a partilha da terra entre herdeiros sem violar o módulo e a fração mínima; (c) responder a nota de exigência do registrador na partilha de imóvel rural; (d) orientar o inventariante sobre ITR, CCIR e CAR durante o processo.
- Não usar sozinha: o inventário em si — `sucessoes-inventario-judicial` ou `sucessoes-inventario-extrajudicial` (esta skill é o anexo rural daquelas); planejamento sucessório em vida — `sucessoes-planejamento-e-partilha-em-vida`; ITCMD — regras no inventário e no plugin tributário (`trib-*`); correção de medidas na matrícula — `imob-retificacao-de-area`; titulação de posse em terra pública — `agrario-regularizacao-fundiaria-rural`.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Matrícula(s) atualizada(s) e cadeia dominial; se a área está toda registrada ou há posse sem título.
2. CCIR vigente (código do imóvel no SNCR) e titular cadastrado.
3. NIRF e declarações/recibos do ITR dos últimos 5 exercícios; débitos ou parcelamentos.
4. Recibo do CAR e situação (ativo, pendente, cancelado); reserva legal e APP declaradas.
5. Área total (ha), módulo fiscal e fração mínima de parcelamento do município (consta do CCIR).
6. Georreferenciamento: já certificado no SIGEF? Matrícula já georreferenciada?
7. Número de herdeiros e meeiro; interesse de cada um (dividir, manter em condomínio, vender).
8. Arrendamentos, parcerias, financiamentos rurais, CPR e hipotecas vigentes; benfeitorias e rebanho.

## Prazo e contagem
- Prazos do inventário (abertura, conclusão) e da partilha: `prazos-processuais` e as skills de sucessões.
- ITR: o inventariante segue declarando o imóvel; a partilha exige a quitação dos 5 últimos exercícios (Lei 9.393/1996, art. 21).
- Georreferenciamento: a exigência para transferência e desmembramento consta do Decreto 4.449/2002, art. 10, a partir de 21/10/2029 (redação do Decreto 12.689/2025) [VERIFICAR com o registrador local a exigência atual na partilha].

## Estrutura do dossiê e do plano de partilha
Identificação do imóvel → situação registral → situação cadastral (CCIR/SNCR) → fiscal (ITR) → ambiental (CAR) → georreferenciamento → contratos e ônus → proposta de partilha compatível com o módulo → pendências e providências. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e cautelas
- CCIR: nenhuma partilha, amigável ou judicial, é homologada sem o certificado de cadastro (Lei 4.947/1966, art. 22, § 2º); acompanhado de prova de quitação do ITR dos 5 últimos exercícios, ressalvados inexigibilidade e dispensa (§ 3º). A escritura menciona os dados do CCIR (§ 6º).
- ITR: quitação dos 5 últimos exercícios para qualquer ato de registro (Lei 9.393/1996, art. 21); o registrador que descumprir responde solidariamente (parágrafo único). APP e reserva legal saem da área tributável (art. 10, § 1º, II).
- Indivisibilidade: o imóvel rural não se divide em áreas inferiores ao módulo (Estatuto da Terra, art. 65) nem à fração mínima de parcelamento; o ato que infringir é nulo (Lei 5.868/1972, art. 8º e § 3º). Sem área para quinhões acima da fração mínima: atribuir a um herdeiro com reposição, manter condomínio ou vender.
- Desmembramento na partilha: memorial georreferenciado com ART e certificação do INCRA (Lei 6.015/1973, art. 176, §§ 3º a 5º); em autos judiciais, a descrição segue o mesmo padrão (art. 225, § 3º).
- CAR: é declaratório e não prova propriedade (Lei 12.651/2012, art. 29, § 2º); deve ser atualizado com os novos titulares. O registro da reserva legal no CAR dispensa a averbação na matrícula (art. 18, § 4º).
- Arrendamento vigente: a transmissão não extingue o contrato (Estatuto da Terra, art. 92, § 5º — o adquirente se sub-roga); herdeiros devem ser informados. Ver `agrario-arrendamento-e-parceria-rural`.
- Crédito rural: comprovação do ITR dos 5 últimos exercícios condiciona crédito e incentivos (Lei 9.393/1996, art. 20).

## Fundamentos verificados
- Lei 4.947/1966, art. 22, §§ 1º a 6º (redação da Lei 10.267/2001 nos §§ 3º a 8º).
- Lei 9.393/1996, arts. 10, § 1º, II, 20 e 21.
- Lei 5.868/1972, art. 8º. Estatuto da Terra, arts. 65 e 92, § 5º.
- Lei 6.015/1973, art. 176, §§ 3º a 5º, e art. 225, § 3º. Decreto 4.449/2002, arts. 9º e 10.
- Lei 12.651/2012, arts. 18, § 4º, e 29.
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e providências
- Juntada de matrícula, CCIR, certidão negativa ou positiva com efeito de negativa do ITR (5 exercícios) e recibo do CAR.
- Autorização judicial para o inventariante pagar ITR em atraso, atualizar o CCIR e retificar o CAR, se necessário.
- Plano de partilha com quinhões acima da fração mínima, ou atribuição com reposição, ou condomínio, ou venda.
- Se houver desmembramento: memorial georreferenciado e certificação antes do registro do formal ou da escritura.
- Avaliação da terra nua e das benfeitorias para o ITCMD e para a igualdade dos quinhões.

## Checklist pré-protocolo
- [ ] Matrícula atualizada e área registrada x área real
- [ ] CCIR vigente em nome do falecido ou dos titulares atuais
- [ ] ITR dos últimos 5 exercícios quitado (ou exigibilidade suspensa)
- [ ] CAR ativo e coerente com reserva legal e APP
- [ ] Módulo fiscal e fração mínima conferidos no CCIR
- [ ] Partilha sem quinhão rural abaixo da fração mínima
- [ ] Georreferenciamento/certificação se houver desmembramento
- [ ] Contratos agrários e ônus informados aos herdeiros

## Erros a evitar
- Partilhar a fazenda em lotes menores que a fração mínima (nulidade).
- Lavrar a escritura ou pedir homologação sem CCIR e sem ITR quitado.
- Tratar o recibo do CAR como prova de domínio ou de área.
- Descrever no formal de partilha a área "de fato" diferente da registrada sem retificação.
- Esquecer o arrendatário, que continua com o contrato perante os herdeiros.

## Integração com o núcleo
`prazos-processuais`, `juros-e-correcao`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

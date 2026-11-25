---
name: prev-certidao-de-tempo-de-contribuicao
description: >
  Prepara requerimento ao INSS e, se negado, ação para expedição ou retificação
  de Certidão de Tempo de Contribuição (CTC) para contagem recíproca em regime
  próprio (CF, art. 201, § 9º; Lei 8.213/1991, arts. 94 a 99), com tempo
  especial discriminado data a data (TNU Tema 278), indenização de períodos
  (STJ Temas 609 e 1.103) e vedações do art. 96. Use quando o usuário pedir CTC,
  certidão de tempo do INSS para averbar no serviço público, contagem
  recíproca, CTC com tempo especial, indenização de tempo rural ou de
  contribuinte individual para levar ao RPPS, ou retificação de CTC.
metadata:
  area: previdenciario
  tipo_peca: requerimento
  verificado_em: 2026-11-25
---
# Certidão de Tempo de Contribuição (CTC) para regime próprio

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: (a) requerer ao INSS a CTC de períodos do RGPS para averbar em RPPS; (b) incluir na CTC período omitido ou tempo especial; (c) indenizar período (rural, contribuinte individual) para poder certificá-lo; (d) ação contra indeferimento ou omissão do INSS.
- Não usar: aposentadoria do servidor no RPPS, abono de permanência, conversão de tempo especial pelo regime de destino → `prev-rpps-servidor`. Ex-servidor que quer levar tempo do RPPS para o RGPS: a CTC é emitida pelo próprio RPPS (Lei 8.213, art. 96, VI) → ação contra o ente, ver `adm-mandado-de-seguranca` ou `adm-acao-anulatoria-de-ato-administrativo`. Reconhecimento de tempo rural sem contagem recíproca → `prev-tempo-rural-e-segurado-especial`. Recurso administrativo → `prev-recurso-crps`.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. CNIS completo e CTPS; períodos que o cliente quer certificar, com origem (empregado, rural, contribuinte individual, militar).
2. Regime de destino (União, Estado, Município) e finalidade (aposentadoria, abono, vantagem funcional).
3. Períodos já averbados ou usados em outra aposentadoria (art. 96, III) e vínculos concomitantes com serviço público (art. 96, II).
4. Recolhimentos como contribuinte individual ou facultativo pelo plano simplificado (art. 94, § 2º).
5. Documentos de tempo especial (PPP, LTCAT) e pedido para que constem na CTC.
6. Requerimento ao INSS, CTC já emitida (se houver) e decisão de indeferimento ou exigência.

## Prazo e contagem
- Lei conferida não fixa prazo para pedir a CTC. Prazo para ação contra indeferimento de CTC não foi conferido [VERIFICAR: aplicação do art. 103 da Lei 8.213 e da ADI 6096 a certidão, que não é benefício].
- Prazos processuais e recursais: `prazos-processuais`. Recurso administrativo: `prev-recurso-crps`.
- Encargos da indenização: só incidem multa e juros sobre período posterior à MP 1.523/1996 (STJ Tema 1.103). Não escrever taxa: conferir o cálculo do INSS e remeter a `juros-e-correcao`.

## Estrutura da peça   (detalhe em [estrutura](references/estrutura.md))
1. Requerimento administrativo: identificação, regime de destino, quadro de períodos, tempo especial data a data, pedido de cálculo de indenização se for o caso.
2. Ação (se negado): competência (Justiça Federal; JEF até 60 salários mínimos — Lei 10.259, art. 3º), interesse de agir, períodos controvertidos, prova, vedações do art. 96 enfrentadas, pedidos.

## Requisitos e preliminares
- **Interesse de agir:** pedido prévio ao INSS (STF Tema 350, item I). Fato ou documento novo deve ser levado antes ao INSS.
- **Vedações do art. 96 (enfrentar uma a uma):** sem contagem em dobro ou em condições especiais (I); sem contagem de tempo concomitante de serviço público e atividade privada (II); tempo usado para aposentar num sistema não conta no outro (III); vedada CTC só com registro de tempo sem contribuição efetiva, salvo exceções legais (V); vedada desaverbação de tempo que gerou vantagem remuneratória a servidor em atividade (VIII).
- **Tempo especial:** os períodos especiais reconhecidos pelo regime de origem devem constar da CTC, discriminados data a data (art. 96, IX). O segurado tem direito à certidão do tempo especial; a conversão e a contagem cabem ao regime de destino, e na contagem RGPS → RPPS da União a conversão é possível para tempo até a EC 103/2019 (TNU Tema 278). Servidor: STF Tema 942; após a EC 103, depende de lei complementar do ente.
- **Indenização:** tempo anterior ou posterior à filiação obrigatória só conta mediante indenização (art. 96, IV); a multa não se aplica a tempo anterior à obrigatoriedade de filiação (art. 96, § 2º, Lei 15.363/2026). Tempo rural anterior à Lei 8.213: cabe certidão para averbação, mas o cômputo no RPPS exige comprovar o pagamento da indenização (STJ Tema 609; TNU Tema 35).
- **Plano simplificado:** período recolhido na forma do art. 21, § 2º, da Lei 8.212 não conta para RPPS sem complementação (art. 94, § 2º).
- **Tempo fictício:** vedado (CF, art. 201, § 14); é nula a aposentadoria de RPPS com contagem recíproca sem a contribuição correspondente (EC 103, art. 25, § 3º).

## Fundamentos verificados   (detalhe em [fundamentos](references/fundamentos.md))
- CF, art. 201, §§ 9º, 9º-A e 14; EC 103/2019, art. 25, §§ 2º e 3º.
- Lei 8.213/1991, arts. 94 (caput, §§ 1º e 2º), 96 (I a IX, §§ 1º e 2º) e 99; Lei 10.259/2001, art. 3º.
- STF Temas 350 e 942; STJ Temas 609 e 1.103; TNU Temas 35 e 278.

## Pedidos e requerimentos
- Expedição (ou retificação) da CTC com os períodos X a Y, discriminando data a data os períodos especiais.
- Cálculo da indenização dos períodos Z, sem multa e juros para competências anteriores à MP 1.523/1996, e emissão da CTC após o pagamento.
- Tutela de urgência só se houver prazo funcional concreto (aposentadoria iminente, abono) e prova.
- Na ação: condenação do INSS a emitir a CTC no prazo fixado, sob multa.

## Checklist pré-protocolo
- [ ] Quadro de períodos com origem, prova e situação no CNIS.
- [ ] Nenhum período concomitante com serviço público ou já usado em aposentadoria.
- [ ] Tempo especial com PPP/LTCAT e pedido de discriminação data a data.
- [ ] Períodos que exigem indenização identificados; cálculo do INSS conferido (Tema 1.103).
- [ ] Recolhimentos do plano simplificado complementados ou excluídos.
- [ ] Requerimento prévio e decisão do INSS juntados.
- [ ] Nenhuma taxa de juros ou índice escrito na peça.

## Erros a evitar
- Pedir ao INSS que **converta** o tempo especial na CTC: o pedido é de certificar o tempo especial data a data; a conversão é do regime de destino (Tema 278).
- Converter tempo especial posterior a 13/11/2019 (EC 103, art. 25, § 2º; Tema 942).
- Levar tempo rural anterior a 1991 ao RPPS sem a indenização (Tema 609).
- Aceitar cálculo de indenização com multa e juros sobre período anterior à MP 1.523/1996 (Tema 1.103).
- Ignorar o plano simplificado (art. 94, § 2º) e ter o período recusado pelo RPPS.

## Integração com o núcleo
- `juros-e-correcao` (indenização e eventuais diferenças); `prazos-processuais`; `verificacao-de-citacoes`; `fidelidade-factual` (datas do CNIS e da CTC); `estilo-forense`.

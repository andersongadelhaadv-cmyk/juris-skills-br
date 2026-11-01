---
name: adm-defesa-em-processo-sancionador-licitacao
description: >
  Redige defesa prévia, alegações finais, recurso ou pedido de reconsideração de
  licitante ou contratado em processo de responsabilização da Lei 14.133/2021
  (arts. 155 a 163, 166 e 167): advertência, multa, impedimento de licitar e
  declaração de inidoneidade, com prescrição e dosimetria. Use quando o usuário
  pedir defesa em PAR, defesa contra multa contratual, impedimento de licitar,
  inidoneidade, inexecução contratual, sanção a fornecedor, reabilitação ou
  exclusão do CEIS/CNEP.
metadata:
  area: administrativo-licitacoes
  tipo_peca: defesa-administrativa
  verificado_em: 2026-11-01
---
# Defesa em processo sancionador de licitações e contratos

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: intimação para defesa por infração do art. 155 (inexecução, não manutenção da proposta, documentação falsa, fraude, atraso injustificado etc.); recurso contra sanção aplicada; pedido de reabilitação (art. 163).
- Não usar para ato lesivo julgado exclusivamente pela Lei 12.846/2013: quando houver concurso, a apuração é conjunta e segue o rito da Lei 12.846/2013 (art. 159) — adaptar a defesa ao rito e à autoridade daquela lei.
- Contrato assinado sob a Lei 8.666/1993 continua regido por ela (art. 190); nesse caso, aplicar o regime sancionador revogado e marcar a peça como regime histórico.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Intimação: data de recebimento, sanção cogitada, infração imputada (inciso do art. 155), autoridade e comissão.
2. Edital, contrato, aditivos, matriz de riscos, notificações trocadas e respostas do cliente.
3. Data em que a Administração teve ciência da infração e data de instauração do processo (prescrição).
4. Causas do inadimplemento alegadas pelo cliente e prova (fato da Administração, força maior, atraso de pagamento, falha de projeto).
5. Valor do contrato e eventual cálculo da multa; garantias prestadas; pagamentos retidos.
6. Programa de integridade existente (atenuante e condição de reabilitação).
7. Antecedentes do cliente (outras sanções, registros no CEIS/CNEP).

## Prazo e contagem
- Multa (art. 156, II): defesa em 15 dias úteis da intimação (art. 157).
- Impedimento e inidoneidade (art. 156, III e IV): processo de responsabilização por comissão de 2 ou mais servidores estáveis; defesa escrita e especificação de provas em 15 dias úteis (art. 158, caput); alegações finais em 15 dias úteis se houver nova prova (art. 158, § 2º).
- Recurso contra advertência, multa e impedimento: 15 dias úteis (art. 166). Inidoneidade: apenas pedido de reconsideração, 15 dias úteis (art. 167). Ambos com efeito suspensivo (art. 168).
- Prescrição: 5 anos da ciência da infração pela Administração; interrompida pela instauração do processo de responsabilização; suspensa por acordo de leniência ou decisão judicial que inviabilize a apuração (art. 158, § 4º).
- Contagem em dias úteis (art. 183). Conferir com `prazos-processuais`.

## Estrutura da peça (resumo; detalhe em [estrutura](references/estrutura.md))
Endereçamento à comissão → tempestividade → preliminares (prescrição, competência, comissão, cerceamento) → fatos → mérito (atipicidade, excludentes, culpa da Administração) → dosimetria subsidiária → provas → pedidos.

## Requisitos e preliminares
- Prescrição quinquenal do art. 158, § 4º (cálculo com datas).
- Competência: inidoneidade exige autoridade do art. 156, § 6º (ministro, secretário ou autoridade máxima da entidade) e análise jurídica prévia.
- Comissão: composição do art. 158, caput e § 1º.
- Correspondência sanção × infração: advertência só para o inciso I do art. 155 (art. 156, § 2º); impedimento para os incisos II a VII (§ 4º); inidoneidade para VIII a XII ou casos graves de II a VII (§ 5º).
- Indeferimento de provas só por decisão fundamentada (art. 158, § 3º).
- Desconsideração da personalidade jurídica exige contraditório e análise jurídica prévia (art. 160).

## Fundamentos verificados (resumo; detalhe em [fundamentos](references/fundamentos.md))
Lei 14.133/2021: arts. 103, 124, II, "d", 137, § 2º e § 3º, 155 a 163, 166 a 168, 183, 190. LINDB (DL 4.657/1942), arts. 20, 22 e 28. Lei 12.846/2013 (apuração conjunta).

## Pedidos e requerimentos
- Reconhecimento da prescrição ou de nulidade, com arquivamento.
- No mérito, absolvição por atipicidade ou excludente (fato da Administração, força maior, caso fortuito).
- Subsidiariamente, sanção menos grave, com fundamentação pelos critérios do art. 156, § 1º; multa no mínimo, nos limites de 0,5% a 30% do valor do contrato (art. 156, § 3º).
- Produção de provas especificadas (documental, pericial, testemunhal).
- Compensação de valores retidos e exclusão de cumulação indevida (art. 156, §§ 7º e 8º).
- Qualquer valor devolvido ou compensado: atualização pela skill `juros-e-correcao`.

## Checklist pré-protocolo
- [ ] Prazo de 15 dias úteis contado da intimação.
- [ ] Datas de ciência da infração e de instauração conferidas (prescrição).
- [ ] Infração imputada identificada pelo inciso exato do art. 155.
- [ ] Sanção cogitada compatível com a infração (art. 156, §§ 2º, 4º e 5º).
- [ ] Autoridade e comissão competentes.
- [ ] Provas especificadas já na defesa (art. 158).
- [ ] Atenuantes documentadas, inclusive programa de integridade (art. 156, § 1º, V).
- [ ] Ressalvas de desequilíbrio contratual registradas (ligação com `adm-pedido-de-reequilibrio-economico-financeiro`).

## Erros a evitar
- Invocar prazos de defesa da Lei 8.666/1993 para contrato regido pela Lei 14.133/2021 (ou o inverso: ver art. 190).
- Esquecer de especificar provas na defesa escrita.
- Tratar a prescrição do art. 158, § 4º como contada do fato (o termo é a ciência pela Administração).
- Recorrer de inidoneidade com "recurso hierárquico" (cabe só reconsideração).
- Não pedir dosimetria subsidiária.

## Integração com o núcleo
- `prazos-processuais`: prazos em dias úteis e prescrição.
- `juros-e-correcao`: valores compensados ou a restituir.
- `verificacao-de-citacoes`: decisões de tribunais de contas e acórdãos acrescentados.
- `fidelidade-factual`: cronologia contratual e notificações.
- `estilo-forense`: revisão final.

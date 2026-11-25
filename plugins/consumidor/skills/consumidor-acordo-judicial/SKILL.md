---
name: consumidor-acordo-judicial
description: >
  Redige minuta de acordo (transação) em ação de consumo e a petição de
  homologação, no Juizado Especial ou na Justiça comum, com base nos arts. 840
  a 850 do Código Civil, nos arts. 90, §§ 2º e 3º, 487, III, b, e 515, II e III,
  do CPC e nos arts. 22 e 41 da Lei 9.099/1995, cuidando de obrigação de fazer
  (baixa de negativação, cancelamento de contrato), prazo, multa, quitação e
  honorários (art. 24, § 4º, da Lei 8.906/1994). Use quando o usuário pedir
  acordo com a empresa ré, minuta de transação, proposta de acordo na
  audiência de conciliação, petição de homologação ou revisão de proposta de
  acordo enviada pelo fornecedor.
metadata:
  area: consumidor
  tipo_peca: outro
  verificado_em: 2026-11-25
---
# Acordo em ação de consumo (transação e homologação)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: acordo em processo de consumo em curso (inicial, audiência, recurso, cumprimento de sentença), de qualquer dos lados; revisão da proposta do fornecedor antes de o cliente aceitar.
- Usar também para acordo extrajudicial que se quer homologar (CPC art. 515, III).
- Não usar:
  - Acordo trabalhista: `trabalhista-acordo-extrajudicial`.
  - Repactuação global de dívidas: `consumidor-superendividamento` (plano do art. 104-A).
  - Distrato de contrato sem litígio: `contratos-distrato-e-rescisao`.
  - Acordo em ação coletiva ou termo de ajustamento de conduta: `consumidor-acao-coletiva`.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Número do processo, juízo (JEC ou vara), fase (antes ou depois da sentença; trânsito em julgado?).
2. Pedidos da inicial e o que já foi decidido (tutela, sentença, acórdão), com valores.
3. Proposta em discussão: valor, forma e data de pagamento; obrigações de fazer (baixa de negativação, cancelamento, estorno, entrega, conserto).
4. Dados para pagamento (conta do cliente ou do advogado, com poderes para receber e dar quitação na procuração).
5. Honorários: contratuais (percentual, quem paga) e sucumbenciais já fixados?
6. O cliente está de acordo com cada item? (acordo é ato da parte; registrar a anuência).
7. Há outros processos ou dívidas entre as mesmas partes a incluir ou excluir da quitação?

## Prazo e contagem
- Acordo pode ser celebrado a qualquer tempo, inclusive após a sentença e no cumprimento.
- Transação antes da sentença dispensa as custas remanescentes (CPC art. 90, § 3º).
- Prazos do acordo: fixar em dias corridos ou úteis expressamente e data-limite. Prazos processuais: `prazos-processuais`.

## Estrutura da peça
Qualificação e processo → considerações (objeto do litígio, sem confissão) → cláusulas: obrigação de pagar, obrigações de fazer, prazos, multa por descumprimento, quitação delimitada, custas e honorários, foro → pedido de homologação e extinção (CPC 487, III, b). Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Objeto transacionável: direitos patrimoniais de caráter privado (CC art. 841).
- Concessões mútuas (CC art. 840); a transação se interpreta restritivamente (art. 843) e só vincula quem nela intervém (art. 844): incluir todos os réus que devem cumprir.
- Poderes especiais na procuração para transigir, receber e dar quitação.
- No JEC, a conciliação homologada vale como título executivo (Lei 9.099/1995, art. 22, parágrafo único) e a sentença homologatória não comporta recurso inominado (art. 41).
- A sentença homologatória é título executivo judicial (CPC art. 515, II); o acordo pode incluir terceiro e relação não deduzida em juízo (art. 515, § 2º).

## Fundamentos verificados
- CC arts. 840, 841, 843, 844, 849 (anulação só por dolo, coação ou erro essencial; não por erro de direito).
- CPC arts. 90, §§ 2º e 3º; 487, III, b; 515, II, III e § 2º; 334, §§ 4º e 8º.
- Lei 9.099/1995, arts. 22, parágrafo único, e 41.
- Lei 8.906/1994, arts. 23 e 24, § 4º: acordo sem aquiescência do advogado não prejudica os honorários.
- STJ: acordo sem anuência do advogado não atinge sucumbenciais já fixados (REsp 1.893.086; AgInt no AREsp 2.575.449); transação anterior à fixação não gera sucumbência (AgInt nos EDcl no AREsp 2.106.962); advogado que participa do acordo e nada ressalva aquiesce (REsp 2.141.990); homologação não exige a participação do advogado (AgInt no REsp 2.076.641).
Detalhe em [fundamentos](references/fundamentos.md).

## Cláusulas essenciais
- Valor líquido, forma (depósito judicial, Pix, transferência), data e titular da conta.
- Obrigação de fazer com prazo e prova de cumprimento (ex.: baixa de todas as anotações do contrato X em até N dias, com comprovação nos autos).
- Multa por descumprimento (cláusula penal) proporcional e com teto; vencimento antecipado das parcelas.
- Quitação delimitada ao objeto da ação (não "geral e irrestrita" se houver outros contratos).
- Custas (art. 90, §§ 2º e 3º) e honorários: contratuais preservados; sucumbenciais já fixados só com anuência expressa do advogado.
- Ausência de confissão de culpa, se o fornecedor exigir — avaliar o efeito para o cliente.
- Correção e juros em caso de atraso: remeter ao núcleo `juros-e-correcao`, sem taxa improvisada.

## Checklist pré-protocolo
- [ ] Anuência do cliente a cada cláusula registrada (assinatura ou mensagem guardada)
- [ ] Procuração com poderes para transigir, receber e dar quitação
- [ ] Todos os réus obrigados assinam
- [ ] Obrigações de fazer com prazo, prova e multa
- [ ] Quitação delimitada
- [ ] Honorários sucumbenciais já fixados tratados expressamente
- [ ] Conta de pagamento conferida
- [ ] Pedido de homologação e extinção

## Erros a evitar
- Quitação ampla que apaga outros contratos ou anotações não discutidos.
- Esquecer a baixa da negativação ou o cancelamento do contrato e acordar só o dinheiro.
- Multa sem prazo de cumprimento definido: inexequível.
- Acordo que renuncia aos sucumbenciais do advogado sem a assinatura dele (Lei 8.906/1994, art. 24, § 4º).
- Contar com recurso contra a homologação no JEC (art. 41 o exclui): revisar tudo antes de assinar.

## Integração com o núcleo
`juros-e-correcao`, `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

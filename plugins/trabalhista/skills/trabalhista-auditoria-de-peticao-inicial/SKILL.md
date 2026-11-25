---
name: trabalhista-auditoria-de-peticao-inicial
description: >
  Audita petição inicial trabalhista contra os requisitos do art. 840 §1º da
  CLT (juízo, qualificação, breve exposição dos fatos, pedido certo,
  determinado e com valor, data e assinatura), o rito sumaríssimo (arts. 852-A
  e 852-B), documentos (art. 787), competência territorial (art. 651),
  prescrição (art. 11) e gratuidade (art. 790 §§3º-4º), devolvendo relatório
  de conformidade pedido a pedido com a consequência de cada falha (extinção do
  pedido, arquivamento, emenda — Súmula 263 do TST). Use quando o usuário pedir
  para conferir, auditar ou revisar uma reclamação trabalhista antes de
  protocolar, checar o art. 840, ou procurar inépcia na inicial do reclamante.
metadata:
  area: trabalhista
  tipo_peca: parecer
  verificado_em: 2026-11-25
---
# Auditoria de petição inicial trabalhista (art. 840 §1º)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar (lado do reclamante): conferir a minuta antes do protocolo e corrigir falhas que levam à extinção de pedidos ou ao arquivamento.
- Usar (lado da reclamada): achar pedidos sem valor, indeterminados ou sem causa de pedir para a preliminar da defesa.
- Não usar: redigir a inicial (use `trabalhista-reclamacao`); análise de risco completa da ação recebida (use `trabalhista-triagem-de-reclamatoria`); inicial cível (use `civel-peticao-inicial`).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Texto integral da inicial (ou minuta) e lista de documentos anexos.
2. Rito pretendido ou indicado e valor da causa.
3. Data de ajuizamento (ou prevista) e data da extinção do contrato.
4. Local da prestação de serviços e vara escolhida.
5. Se a reclamada inclui ente da Administração Pública (excluído do sumaríssimo).
6. Para quem se audita (reclamante ou reclamada).

## Prazo e contagem
- Prescrição: confrontar a data de ajuizamento com a extinção (biênio) e marcar o corte quinquenal (art. 11; CF art. 7º, XXIX).
- Emenda determinada pelo juízo: 15 dias (CPC art. 321, aplicado pela Súmula 263 do TST); contagem em dias úteis pelo `prazos-processuais`.

## Estrutura do relatório
Identificação → enquadramento do rito → checagem dos requisitos do art. 840 §1º (item a item) → auditoria pedido a pedido (certeza, determinação, valor, causa de pedir, documento) → competência, prescrição, gratuidade e honorários → consequências e correções sugeridas. Detalhe em [estrutura](references/estrutura.md).

## Requisitos (art. 840 §1º) — o que conferir
1. **Designação do juízo** — vara competente pelo local da prestação de serviços (art. 651).
2. **Qualificação das partes** — no sumaríssimo, nome e endereço corretos da reclamada são ônus do autor, sem citação por edital (art. 852-B, II).
3. **Breve exposição dos fatos** — cada pedido precisa de fato que o sustente.
4. **Pedido certo, determinado e com indicação de valor** — um valor para cada pedido, inclusive reflexos se pedidos à parte.
5. **Data e assinatura** do reclamante ou do representante.
- **Documentos**: a reclamação deve vir com os documentos em que se fundar (art. 787).

## Consequências de cada falha
- Pedido sem os requisitos do §1º: **extinção sem resolução do mérito** daquele pedido (art. 840 §3º).
- Sumaríssimo sem pedido certo ou determinado com valor, ou sem nome e endereço corretos: **arquivamento** e custas sobre o valor da causa (art. 852-B §1º).
- Defeito sanável em geral: o juiz deve intimar para emenda em 15 dias, indicando o que corrigir, antes de indeferir (Súmula 263 do TST; CPC art. 321), salvo as hipóteses do CPC art. 330.
- Valor da causa e dos pedidos: são estimativa (IN 41/2018 do TST, art. 12 §2º, transcrita em acórdão confirmado). Se a condenação fica limitada a esses valores é questão afetada ao Pleno do TST como Tema 35 de IRR, sem suspensão dos processos [VERIFICAR: tese ainda não conferida].

## Fundamentos verificados
- CLT arts. 11, 651, 787, 790 §§3º-4º, 791-A, 840 §§1º-3º, 852-A, 852-B.
- CPC arts. 321 e 330 (subsidiários, CLT art. 769).
- Súmula 263 do TST; TST, Ag-AIRR-1000065-58.2024.5.02.0065 (Tema 35 afetado; IN 41/2018 art. 12 §2º).
Detalhe em [fundamentos](references/fundamentos.md).

## Pontos de atenção por rito
- **Sumaríssimo**: valor da causa até 40 salários mínimos na data do ajuizamento; vedado se houver ente da Administração direta, autárquica ou fundacional (art. 852-A). Conferir o salário mínimo vigente em fonte oficial, nunca de memória.
- **Ordinário**: os mesmos requisitos do §1º; o risco é a extinção pedido a pedido.
- **Gratuidade**: salário igual ou inferior a 40% do teto do RGPS (concessão facultada, art. 790 §3º) ou comprovação de insuficiência (§4º); teto do ano em fonte oficial.
- **Honorários**: pedido de sucumbência de 5% a 15% (art. 791-A); para a sucumbência do beneficiário da gratuidade, ver `trabalhista-reclamacao` (ADI 5766).

## Checklist de entrega
- [ ] Rito confere com o valor da causa e com o polo passivo
- [ ] Cada pedido tem fato, valor e (quando houver) documento
- [ ] Reflexos com valor próprio ou embutidos de forma explícita
- [ ] Competência territorial conferida (art. 651)
- [ ] Prescrição bienal e quinquenal marcadas
- [ ] Gratuidade com documento compatível com o art. 790 §§3º-4º
- [ ] Assinatura e data presentes
- [ ] Relatório indica a consequência de cada falha e a correção

## Erros a evitar
- Valor "a apurar em liquidação" sem estimativa: é a principal causa de extinção do pedido.
- Pedido genérico ("demais verbas de direito", "diferenças que forem apuradas").
- Sumaríssimo com endereço incerto da reclamada.
- Escolher o sumaríssimo contra ente público.
- Para a defesa: pedir a extinção de toda a ação quando só alguns pedidos falham (o §3º atinge o pedido).
- Afirmar que os valores da inicial limitam (ou não) a condenação como se fosse tese firmada: o Tema 35 está pendente.

## Integração com o núcleo
`prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`; estimativa de valores dos pedidos e atualização pelo `juros-e-correcao`.

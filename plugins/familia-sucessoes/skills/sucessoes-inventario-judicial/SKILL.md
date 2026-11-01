---
name: sucessoes-inventario-judicial
description: >
  Redige a abertura de inventário judicial e suas peças (primeiras declarações, arrolamento
  sumário e comum, colação, habilitação de crédito, plano de partilha, sobrepartilha) pelo
  CPC arts. 610 a 673, com orientação sobre ITCMD. Use quando o usuário pedir abertura de
  inventário, inventário judicial, arrolamento, primeiras declarações, nomeação de
  inventariante, remoção de inventariante, partilha judicial, sobrepartilha, alvará.
metadata:
  area: familia-sucessoes
  tipo_peca: requerimento
  verificado_em: 2026-11-01
---
# Inventário judicial

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: herdeiros em desacordo; interessado incapaz quando a via extrajudicial não for possível ou não for escolhida; testamento sem autorização judicial para escritura; credores e questões que exigem juiz.
- Não usar: todos capazes e concordes, sem óbice — avaliar `sucessoes-inventario-extrajudicial` (mais rápido); questões de alta indagação que dependem de prova não documental (vão às vias ordinárias, CPC 612).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Certidão de óbito; último domicílio do falecido; data do óbito.
2. Estado civil, regime de bens, data do casamento/união; certidões.
3. Herdeiros: nomes, parentesco, capacidade, endereços; testamento (certidão da Central de testamentos).
4. Bens com documentos: matrículas, veículos, contas, aplicações, quotas sociais, créditos; dívidas do espólio.
5. Doações em vida a herdeiros (colação).
6. Quem está na posse e administração dos bens (inventariante).
7. Estado e lei estadual do ITCMD aplicáveis.

## Prazo e contagem
- Abertura em 2 meses da abertura da sucessão; conclusão em 12 meses seguintes, prorrogáveis (CPC 611). Atraso pode gerar multa estadual (Súmula 542 STF).
- Compromisso do inventariante em 5 dias (CPC 617 p.ú.); primeiras declarações em 20 dias do compromisso (CPC 620).
- Manifestação sobre as primeiras declarações: 15 dias (CPC 627). Contagem via `prazos-processuais`.

## Estrutura da peça
Petição de abertura → nomeação de inventariante → primeiras declarações → citações → avaliação → últimas declarações → ITCMD → partilha → sentença → formal. Arrolamento sumário (todos capazes e concordes, CPC 659) e arrolamento comum (até 1.000 salários mínimos, CPC 664). Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Legitimidade: quem está na posse e administração (CPC 615) e os concorrentes do CPC 616.
- Ordem de nomeação do inventariante (CPC 617).
- Foro: domicílio do autor da herança no Brasil, ainda que o óbito tenha ocorrido no exterior; sem domicílio certo, situação dos imóveis (CPC 48).
- MP se houver incapaz; Fazenda sempre intimada (CPC 626).
- Companheiro sobrevivente concorre como cônjuge (STF Temas 809/498); direito real de habitação (CC 1.831).
- ITCMD: alíquota vigente na abertura da sucessão (Súmula 112 STF). Desde a EC 132/2023, o imposto deve ser progressivo e a competência sobre móveis é do Estado do domicílio do falecido (CF 155 §1º, II e VI). A LC 227/2026 (publicada em janeiro de 2026) traz normas gerais do ITCMD, mas depende de lei de cada Estado, sujeita à anterioridade — conferir a lei estadual vigente na data do óbito.

## Fundamentos verificados
CPC 610 a 673; CC 1.784, 1.829 a 1.839, 1.845 a 1.847, 2.002 a 2.007, 2.015 a 2.017; CF 155 §1º; Súmulas 112 e 542 STF; STF Temas 809, 825. Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- [ ] Abertura do inventário e nomeação do inventariante indicado.
- [ ] Prazo para primeiras declarações ou apresentação imediata.
- [ ] Citação dos herdeiros, intimação da Fazenda e do MP (se houver incapaz).
- [ ] Alvarás (venda de bem para pagar ITCMD/dívidas; levantamento de valores) com justificativa.
- [ ] Uso e fruição antecipados de bem por herdeiro (CPC 647 p.ú.), se útil.
- [ ] Reserva de bens para credores ou herdeiro preterido (CPC 628 §2º, 642, 663).
- [ ] Homologação/julgamento da partilha e expedição de formal ou carta de adjudicação.

## Checklist pré-protocolo
- [ ] Certidão de óbito, certidões de estado civil e de nascimento dos herdeiros.
- [ ] Busca de testamento (Central notarial).
- [ ] Matrículas atualizadas e extratos.
- [ ] Doações a descendentes listadas para colação.
- [ ] Cálculo de meação e quinhões conforme regime e ordem de vocação.
- [ ] Lei estadual do ITCMD aplicável na data do óbito conferida (alíquotas, base, isenções).
- [ ] Avaliação de quotas sociais (CPC 620 §1º, II; 630 p.ú.).

## Erros a evitar
- Aplicar o CC 1.790 ao companheiro (inconstitucional).
- Calcular ITCMD com alíquota da data da partilha ou do pagamento, em vez da data do óbito (Súmula 112 STF).
- Tratar as regras da LC 227/2026 como já aplicáveis sem lei estadual vigente.
- Omitir bens doados em vida (sonegação, CC 2.002).
- Discutir no inventário questão que dependa de prova oral (CPC 612; 627 §3º; 641 §2º).
- Perder o prazo de 2 meses sem informar o cliente sobre a multa estadual.

## Integração com o núcleo
`prazos-processuais`, `juros-e-correcao` (créditos e dívidas do espólio, reposições), `verificacao-de-citacoes`, `fidelidade-factual` (bens e valores), `estilo-forense`.

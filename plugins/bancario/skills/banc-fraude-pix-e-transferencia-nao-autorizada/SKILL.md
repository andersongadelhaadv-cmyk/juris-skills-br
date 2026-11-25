---
name: banc-fraude-pix-e-transferencia-nao-autorizada
description: >
  Redige ação declaratória de inexigibilidade cumulada com restituição e
  indenização contra instituição financeira por Pix, TED, empréstimo ou
  pagamento não autorizado (invasão de conta, celular furtado, golpe da falsa
  central, transações atípicas), com Súmula 479 do STJ, art. 14 do CDC e o
  contraponto da engenharia social com credenciais legítimas. Use quando o
  usuário pedir ação contra o banco por Pix que não fez, conta invadida,
  empréstimo contratado por golpista, sequência de transferências fora do
  perfil ou devolução de dinheiro desviado da conta.
metadata:
  area: bancario
  tipo_peca: inicial
  verificado_em: 2026-11-25
---
# Fraude em conta: Pix e transferências não autorizadas

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: valores saíram da conta do cliente (Pix, TED, pagamento de boleto, empréstimo seguido de transferência) sem autorização válida, por invasão, furto do aparelho, clonagem ou golpe em que o banco deixou passar operações atípicas.
- Não usar:
  - Só para pedir o bloqueio e a devolução pelo próprio arranjo Pix, antes da ação: `banc-med-pix-devolucao`.
  - Conta aberta em nome do cliente por terceiro: `banc-conta-aberta-indevidamente`.
  - Negativação decorrente da fraude, sem desvio de saldo: `consumidor-negativacao-indevida`.
  - Defesa do banco nessa ação: `consumidor-defesa-do-fornecedor`.
  - Persecução penal do golpista: `digital-crime-cibernetico`.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Extrato do período, com cada operação contestada: data, hora, valor, tipo, destinatário (nome, banco, chave).
2. Como ocorreu: celular furtado/roubado, link ou ligação falsa, acesso remoto, senha fornecida? Quem digitou e confirmou as operações? (decide entre falha do banco e o precedente da engenharia social).
3. Perfil habitual da conta: valores médios, horários, uso de Pix, limite contratado. As operações destoam? Houve empréstimo contratado minutos antes?
4. Quando e por qual canal avisou o banco; protocolos; houve pedido de MED/bloqueio? Resposta?
5. Boletim de ocorrência; reclamação na ouvidoria e no Banco Central (`banc-reclamacao-bacen-e-ouvidoria`).
6. O cliente é idoso ou hipervulnerável? A verba atingida é salário ou benefício?
7. Prejuízos além do valor: juros do empréstimo, contas não pagas, negativação.

## Prazo e contagem
- Prescrição: fato do serviço (art. 14 do CDC) atrai o prazo de 5 anos do art. 27, contado do conhecimento do dano e da autoria. Se houver controvérsia sobre o enquadramento, conte pelo prazo menor e registre a data em que o cliente soube das operações.
- Agir rápido não é prazo legal, mas é prova: aviso imediato ao banco e pedido de MED pesam na análise da falha e da mitigação.
- Prazos processuais em dias úteis: `prazos-processuais`.

## Estrutura da peça
Fatos com tabela de operações → relação de consumo e responsabilidade objetiva → defeito do serviço (fortuito interno; operações atípicas; falha na prevenção) → afastamento da culpa exclusiva → inexigibilidade de empréstimo fraudulento → danos materiais e morais → tutela de urgência → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Polo passivo: banco do cliente (pagador). Incluir o banco de destino só com fato concreto contra ele (conta aberta sem cautela, inércia no bloqueio); a responsabilidade dele é casuística.
- Ônus: pedir inversão (CDC art. 6º, VIII) e exibição de logs (IP, dispositivo, geolocalização, horário, canal, registros de autenticação e de alertas antifraude) — CPC arts. 396 a 400.
- Antecipe a tese do banco: credenciais legítimas e participação do cliente. O ponto da peça é mostrar o que o sistema do banco deveria ter detectado.

## Fundamentos verificados
- CDC arts. 6º VIII, 14 caput, § 1º e § 3º, 27; CC arts. 186 e 927.
- Súmula 297/STJ (CDC aplica-se a bancos) e Súmula 479/STJ (fortuito interno por fraude de terceiros).
- REsp 2.229.519 (3ª Turma, 2025): banco deve manter mecanismos de detecção; validar operações atípicas e alheias ao perfil revela defeito; lista de critérios (perfil, horário, intervalo, sequência, meio, empréstimo atípico prévio).
- AREsp 2.949.395 (4ª Turma, 2026): nove transações em curto espaço, fora do perfil, configuram falha de segurança.
- AgInt no AREsp 2.201.401 (3ª Turma, 2023): golpe do motoboy, idosas hipervulneráveis, movimentações atípicas, concorrência de causas.
- Contraponto: REsp 2.238.532 (4ª Turma, 2026) — engenharia social com senha e dispositivo do cliente = fortuito externo; e AREsp 3.145.766 (4ª Turma, 2026), Pix voluntário sem cautelas mínimas.
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Tutela de urgência (CPC art. 300): suspensão das parcelas do empréstimo fraudulento e abstenção de negativação, com multa (CPC art. 537).
- Declaração de inexigibilidade das operações e do empréstimo vinculado.
- Restituição dos valores desviados e dos encargos pagos; se o pedido for em dobro, ver `consumidor-repeticao-em-dobro`.
- Dano moral com fatos concretos (verba alimentar, idoso, negativação, demora na solução).
- Inversão do ônus e exibição dos registros técnicos sob pena do art. 400 do CPC.
- Juros e correção: sempre pelo núcleo `juros-e-correcao`.

## Checklist pré-protocolo
- [ ] Tabela de operações conferida contra o extrato
- [ ] Narrativa honesta sobre senha, dispositivo e quem confirmou
- [ ] Prova do perfil habitual (extratos de meses anteriores)
- [ ] Protocolos do aviso ao banco, BO, ouvidoria e reclamação no BC
- [ ] REsp 2.238.532 enfrentado (distinção concreta)
- [ ] Pedido de exibição de logs especificado
- [ ] Prescrição conferida
- [ ] Juros e correção remetidos ao núcleo

## Erros a evitar
- Omitir que o cliente forneceu senha ou confirmou a operação: o banco provará pelos logs e a credibilidade cai.
- Invocar a Súmula 479 como automática no golpe com credenciais legítimas; o caminho é demonstrar o defeito (atipicidade, falta de bloqueio, demora após o aviso).
- Processar só o banco de destino sem fato contra ele.
- Pedir dano moral genérico, sem circunstâncias.
- Escrever taxa de juros na petição.

## Integração com o núcleo
`juros-e-correcao`, `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

---
name: imob-distrato-imobiliario
description: >
  Redige ação de resolução de promessa de compra e venda de imóvel na planta
  (ou instrumento de distrato) com restituição das parcelas pagas, aplicando a
  Lei 13.786/2018 (arts. 67-A e 43-A da Lei 4.591/1964; art. 32-A da Lei
  6.766/1979), a Súmula 543/STJ, o Tema 1.002/STJ e o Tema 1.095/STJ quando há
  alienação fiduciária registrada. Use quando o usuário pedir distrato com
  construtora ou loteadora, devolução de valores por desistência do comprador,
  rescisão por atraso na entrega da obra, retenção abusiva, arrependimento em
  estande de vendas ou cálculo do que a incorporadora pode reter.
metadata:
  area: imobiliario
  tipo_peca: inicial
  verificado_em: 2026-11-25
---
# Distrato e resolução de promessa de compra e venda na planta

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: (a) desistência do adquirente (resolução por fato a ele imputado); (b) resolução por culpa da incorporadora ou loteadora (atraso além da tolerância, vício, descumprimento); (c) arrependimento em 7 dias em estande ou fora da sede; (d) minuta de distrato amigável.
- Não usar: compra e venda entre particulares sem incorporação, quando o tema é só o inadimplemento (`contratos-distrato-e-rescisao` ou `imob-compra-e-venda-de-imovel`); contestação da incorporadora (use esta skill como base e `civel-contestacao`); revisão do financiamento bancário já assinado (`imob-revisao-de-financiamento-sfh`); defeito da obra sem pedido de resolução (`consumidor-vicio-do-produto-ou-servico`); loteamento irregular (`imob-loteamento-irregular-defesa-do-adquirente`).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Contrato e quadro-resumo (art. 35-A da Lei 4.591/1964) — **data de assinatura** (antes ou depois de 28/12/2018 decide o regime).
2. Incorporação com **patrimônio de afetação**? (muda pena e prazo de restituição). Imóvel em loteamento (Lei 6.766/1979) ou em incorporação (Lei 4.591/1964)?
3. Planilha de todos os pagamentos, com datas e destinatário (incorporadora, corretor, banco).
4. Corretagem: valor, quem recebeu, se estava destacada no quadro-resumo.
5. Prazo de entrega contratado, cláusula de tolerância e data real do habite-se/entrega.
6. Houve entrega das chaves ou posse? Desde quando (fruição)?
7. Há financiamento com **alienação fiduciária registrada** ou garantia não registrada?
8. Notificações trocadas e proposta de distrato recebida.

## Prazo e contagem
- Arrependimento em estande ou fora da sede: 7 dias improrrogáveis, comprovado por carta registrada com AR, contado da postagem (Lei 4.591/1964, art. 67-A, §§ 10 e 11).
- Restituição (contratos sob a Lei 13.786/2018, desistência do adquirente): com patrimônio de afetação, até 30 dias após o habite-se (§ 5º); sem afetação, parcela única após 180 dias do desfazimento (§ 6º); revendida a unidade antes, em até 30 dias da revenda (§ 7º).
- Atraso além de 180 dias da tolerância: restituição integral e multa em até 60 dias da resolução (art. 43-A, § 1º).
- Prescrição da pretensão de restituição: não conferida aqui [VERIFICAR via `verificacao-de-citacoes`]. Prazos processuais: `prazos-processuais`.

## Estrutura da peça
Fatos e linha do tempo → regime aplicável (data do contrato; afetação; loteamento ou incorporação) → causa da resolução (comprador ou vendedor) → valores a restituir e retenções admissíveis → abusividade do excesso → forma e prazo da devolução → tutela (suspensão de cobranças e de negativação) → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Polo passivo: incorporadora/loteadora; corretora se a restituição da corretagem for pedida e ela recebeu diretamente.
- Foro: ação pessoal de restituição; verificar foro de eleição em contrato de consumo.
- Alienação fiduciária **registrada** e inadimplemento do devedor constituído em mora: a resolução segue a Lei 9.514/1997, não o art. 53 do CDC (Tema 1.095/STJ). Sem registro, ou com culpa do vendedor, o Tema 1.095 não incide; garantia não registrada está afetada no Tema 1.420/STJ [VERIFICAR: julgamento].
- Separe o que foi pago à incorporadora do que foi pago ao banco: o art. 67-A fala em valores pagos diretamente ao incorporador.

## Fundamentos verificados
- Lei 4.591/1964, arts. 35-A, 43-A e 67-A (Lei 13.786/2018, vigente desde 28/12/2018); Lei 6.766/1979, art. 32-A (loteamentos).
- CDC, arts. 49, 51 (II e IV) e 53; CC, art. 413.
- Súmula 543/STJ: restituição imediata — integral se culpa exclusiva do vendedor, parcial se o comprador deu causa.
- Tema 1.002/STJ: em contratos **anteriores** à Lei 13.786/2018, resolução por iniciativa do comprador de forma diversa da cláusula penal — juros de mora do trânsito em julgado (enunciado reproduzido no AgInt no REsp 2.180.534, 2026).
- Contratos anteriores à lei: retenção de 25% como referência (AgInt no AgInt no AREsp 2.369.969, 3ª Turma, 2024); percentual e base de cálculo afetados nos Temas 1.464 e 1.465/STJ [VERIFICAR: julgamento].
- Tema 1.095/STJ (REsp 1.891.498, 2ª Seção, 2022): alienação fiduciária registrada e mora do devedor → Lei 9.514/1997.
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Declaração de resolução do contrato (ou homologação do distrato), com indicação da causa.
- Restituição: integral (culpa do vendedor) ou com retenção limitada ao teto legal/contratual válido (culpa do comprador); declaração de abusividade do excedente (CDC, art. 51, IV; CC, art. 413).
- Devolução da corretagem quando o caso permitir (arrependimento do § 10; culpa do vendedor; corretagem não destacada).
- Multa contratual por atraso, sem cumular as do art. 43-A, §§ 1º e 2º (§ 3º).
- Tutela de urgência: suspensão da exigibilidade das parcelas vincendas e proibição de negativação.
- Correção monetária e juros, termo e índice: núcleo `juros-e-correcao` (indicar apenas o termo inicial pedido e o fundamento).

## Checklist pré-protocolo
- [ ] Data do contrato frente a 28/12/2018 e regime escolhido de forma expressa
- [ ] Afetação comprovada ou afastada (matrícula do empreendimento)
- [ ] Planilha de pagamentos separando incorporadora, corretor e banco
- [ ] Causa da resolução demonstrada (desistência x atraso x vício)
- [ ] Retenção pretendida pela ré confrontada com o teto legal (25% ou 50% com afetação; 10% do valor do contrato em loteamento, art. 32-A, II)
- [ ] Fruição só se houve posse (incorporação: 0,5% sobre o valor atualizado do contrato, pro rata die; loteamento: até 0,75% sobre o valor atualizado do contrato — conferir a periodicidade no texto legal)
- [ ] Alienação fiduciária: registrada ou não? Tema 1.095 enfrentado
- [ ] Pedido de tutela com multa
- [ ] Juros e correção remetidos ao núcleo

## Erros a evitar
- Aplicar a Lei 13.786/2018 a contrato anterior a ela (ou o contrário).
- Pedir restituição integral quando a desistência é do comprador sem alegar abusividade da retenção.
- Cumular a multa da resolução por atraso (art. 43-A, § 1º) com a indenização mensal do § 2º.
- Ignorar alienação fiduciária registrada e pedir devolução pelo art. 53 do CDC.
- Pedir fruição contra o comprador que nunca recebeu a posse.
- Esquecer que o distrato pode pactuar condições diferentes da lei (art. 67-A, § 13): ler o termo assinado antes de litigar.

## Integração com o núcleo
`juros-e-correcao`, `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

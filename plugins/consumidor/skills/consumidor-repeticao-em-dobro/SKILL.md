---
name: consumidor-repeticao-em-dobro
description: >
  Estrutura o pedido de repetição do indébito em dobro do art. 42, parágrafo
  único, do CDC (como ação autônoma ou capítulo de outra peça), com a tese da
  Corte Especial do STJ (conduta contrária à boa-fé objetiva, independentemente
  de má-fé), sua modulação temporal e a afetação do Tema 929. Use quando o
  usuário pedir devolução em dobro, restituição de cobrança indevida, descontos
  não autorizados em conta ou benefício, tarifa cobrada sem contratação,
  "pagar duas vezes o que cobraram" ou defesa contra pedido de dobra.
metadata:
  area: consumidor
  tipo_peca: inicial
  verificado_em: 2026-11-02
---
# Repetição do indébito em dobro (CDC art. 42, p.ú.)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: o consumidor **pagou** quantia indevidamente cobrada por fornecedor, em relação de consumo.
- Também serve à defesa do fornecedor (engano justificável; modulação; cobrança não paga).
- Não usar: cobrança apenas lançada e não paga (sem pagamento não há dobro do art. 42); cobrança judicial de dívida já paga — regime do Código Civil (art. 940), outra lógica.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Cada pagamento indevido: data, valor, meio (boleto, débito em conta, desconto em folha/benefício, fatura).
2. Por que é indevido: inexistência de contratação, valor acima do pactuado, cobrança após cancelamento, tarifa ilegal etc.
3. Natureza do contrato: privado ou contratual público (concessionária de serviço público — telefonia, água, energia)? Afeta a modulação.
4. Houve reclamação? Resposta do fornecedor? Devolução parcial?
5. O fornecedor tem justificativa (erro sistêmico isolado, interpretação razoável, ordem judicial)?

## Prazo e contagem
- Prescrição — cobrança indevida dentro de relação contratual: 10 anos (art. 205 do CC); não se aplica o prazo trienal do enriquecimento sem causa (art. 206, § 3º, IV), porque há causa jurídica prévia e a repetição é ação específica (AgInt nos EAREsp 2.764.264, Segunda Seção, 2026, julgado em caso de previdência complementar). Também decenal: serviços não contratados cobrados por telefonia (AgRg no AREsp 723.011) e revisional bancária com repetição (REsp 2.230.380).
- Prescrição — sem contrato válido (fraude, empréstimo não celebrado): o STJ aplicou o art. 27 do CDC (5 anos) ao consumidor por equiparação (AREsp 2.481.029). Na dúvida sobre o enquadramento, conte pelo prazo menor.
- **Marco da modulação:** a tese de que a dobra independe de má-fé aplica-se aos indébitos de natureza contratual **não pública** cobrados **após a publicação** do acórdão da Corte Especial (DJe 30/03/2021). Antes disso, nesses contratos, exige-se má-fé, sob pena de devolução simples. Para contratos de natureza pública (ex.: telefonia), a modulação não se aplica.
- **Tema 929/STJ:** acórdão de 22/09/2026 registra que as hipóteses de aplicação da repetição em dobro foram afetadas ao Tema 929, com suspensão nacional dos processos a partir da interposição de REsp/AREsp. Conferir o estado do tema na data da peça.

## Estrutura da peça
Pagamentos indevidos (tabela) → relação de consumo → ilicitude da cobrança → requisitos da dobra → enquadramento temporal (antes/depois de 30/03/2021; contrato público ou não) → ausência de engano justificável → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Requisitos: (1) cobrança indevida; (2) pagamento pelo consumidor; (3) ausência de engano justificável (ônus do fornecedor).
- Separar os pagamentos por data em relação ao marco de 30/03/2021 quando o contrato for privado: pedir dobro pós-marco e, para os anteriores, dobro com prova de má-fé ou, subsidiariamente, devolução simples.

## Fundamentos verificados
- CDC art. 42, p.ú.; arts. 39 III (produto/serviço não solicitado = amostra grátis, art. 39 p.ú.), 6º VIII.
- STJ, Corte Especial: tese da boa-fé objetiva e modulação (indébitos de natureza contratual não pública cobrados após a publicação — DJe 30/03/2021), conforme transcrita no EAREsp 1.501.756 e no AgInt nos EDcl no REsp 2.043.984.
- STJ: concessionária de telefonia — regime contratual público, fora da modulação (AgInt nos EDcl no REsp 2.043.984).
- STJ: EDcl no AREsp 3.194.853 (22/09/2026) — afetação ao Tema 929 e suspensão.
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Declaração de inexigibilidade da cobrança e cessação dos descontos (tutela, se em curso).
- Restituição em dobro dos valores pagos indevidamente após o marco temporal (tabela) e, quanto aos anteriores, em dobro por má-fé demonstrada ou, subsidiariamente, de forma simples.
- Correção e juros "legais" (texto do art. 42 p.ú.): índices e termos pelo núcleo `juros-e-correcao`.
- Dano moral só com fatos que extrapolem o aborrecimento (desconto em verba alimentar, idoso, demora).
- Pedido subsidiário de sobrestamento/continuidade conforme o estado do Tema 929.

## Checklist pré-protocolo
- [ ] Prova de cada pagamento (não só da cobrança)
- [ ] Tabela separando pagamentos antes e depois de 30/03/2021
- [ ] Natureza do contrato (pública x privada) identificada
- [ ] Tema 929 consultado na data do protocolo
- [ ] Engano justificável antecipado e refutado
- [ ] Prescrição conferida
- [ ] Juros/correção remetidos ao núcleo

## Erros a evitar
- Pedir dobro de valor apenas cobrado e não pago.
- Aplicar a tese sem a modulação a indébitos privados anteriores a 30/03/2021.
- Aplicar a modulação a contratos de concessionária de serviço público (telefonia).
- Escrever "1% ao mês" como juros legais.
- Ignorar a suspensão nacional do Tema 929 quando o processo já estiver em fase de REsp/AREsp.

## Integração com o núcleo
`juros-e-correcao`, `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

---
name: trabalhista-triagem-de-reclamatoria
description: >
  Faz a triagem de reclamação trabalhista recebida pela empresa antes da
  defesa: conferência da notificação e da audiência (CLT arts. 841, 843 e 844),
  prazo da exceção de incompetência (art. 800), prescrição (art. 11), mapa de
  pedidos com ônus da prova (art. 818; Súmulas 212 e 338 do TST), documentos a
  levantar, parcela incontroversa (art. 467), responsabilidade de terceiros
  (Súmula 331) e matriz de risco por pedido para decidir entre defesa e acordo.
  Use quando o usuário pedir análise de risco de reclamatória, triagem de
  processo trabalhista novo, avaliação de ação recebida, o que fazer ao receber
  notificação da Justiça do Trabalho ou provisão para contingência trabalhista.
metadata:
  area: trabalhista
  tipo_peca: parecer
  verificado_em: 2026-11-25
---
# Triagem de reclamatória recebida (risco antes da defesa)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: a reclamada acabou de ser notificada e precisa, antes de escrever a defesa, saber prazos, riscos, documentos e se vale propor acordo.
- Não usar: redigir a contestação (use `trabalhista-contestacao`, alimentada por esta triagem); conferir só os requisitos formais da inicial (use `trabalhista-auditoria-de-peticao-inicial`); processo já em execução (use `trabalhista-impugnacao-de-calculos` ou `trabalhista-embargos-a-execucao`).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Notificação (data de recebimento), inicial completa e documentos do reclamante.
2. Data, hora, modalidade (presencial/telepresencial) e tipo da audiência (inicial ou una).
3. Rito (ordinário ou sumaríssimo) e valor da causa.
4. Ficha do empregado: admissão, saída, função, salário, motivo da extinção, TRCT e comprovante de pagamento.
5. Número de trabalhadores no estabelecimento (registro de ponto obrigatório acima de 20 — art. 74 §2º).
6. Existência de tomador, terceirizada, grupo econômico ou sócios no polo.
7. Versão da empresa para cada pedido e quem pode servir de preposto e testemunha.

## Prazo e contagem
- **Audiência**: a primeira desimpedida depois de 5 dias do recebimento da notificação (art. 841). Prazo menor que isso é nulidade a arguir.
- **Exceção de incompetência territorial**: em 5 dias da notificação, antes da audiência, em peça que sinalize a exceção (art. 800); suspende o processo.
- **Defesa escrita**: pelo PJe até a audiência (art. 847 parágrafo único).
- **Prescrição**: bienal contada da extinção e quinquenal retroativa ao ajuizamento (art. 11; CF art. 7º, XXIX); aviso prévio indenizado integra o tempo de serviço (art. 487 §1º) — considerar ao contar o biênio.
- Contagem em dias úteis e feriados locais: `prazos-processuais`.

## Estrutura da triagem
Dados do processo e prazos → preliminares e prejudiciais possíveis → mapa de pedidos (fato, ônus, prova disponível, risco, valor pedido) → documentos a levantar → incontroverso a pagar em audiência → terceiros e solidariedade → estimativa de exposição → recomendação (defesa, acordo ou ambos) → providências com responsável. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares a mapear
- **Audiência e revelia**: ausência da reclamada = revelia e confissão quanto à matéria de fato (art. 844); presente o advogado, aceitam-se defesa e documentos mesmo sem a parte (§5º); hipóteses em que a revelia não produz efeitos (§4º).
- **Preposto**: deve conhecer os fatos e suas declarações obrigam a empresa (art. 843 §1º); não precisa ser empregado (art. 843 §3º, posterior à Súmula 377 do TST).
- **Inépcia/extinção de pedidos** sem valor ou indeterminados (art. 840 §§1º e 3º) — ver `trabalhista-auditoria-de-peticao-inicial`.
- **Incompetência territorial** (art. 800), **prescrição** (art. 11), **ilegitimidade** de terceiros.

## Fundamentos verificados
- CLT arts. 2º §2º, 11, 74 §2º, 467, 477 §§6º e 8º, 487 §1º, 791-A, 800, 818, 840, 841, 843, 844, 847.
- TST: Súmula 212 (ônus do término do contrato), Súmula 338 (controles de ponto), Súmula 331 (terceirização; IV e VI), Súmula 462 (multa do art. 477 §8º com vínculo reconhecido em juízo), Súmula 377 (preposto — ver ressalva).
Detalhe em [fundamentos](references/fundamentos.md).

## Matriz de risco (por pedido)
- **Provável**: ônus da empresa e documento inexistente ou ruim (ex.: jornada sem cartões em estabelecimento com mais de 20 trabalhadores; cartões britânicos — Súmula 338, III; verbas rescisórias sem comprovante).
- **Possível**: prova testemunhal decisiva, documentos incompletos, tese jurídica controvertida.
- **Remoto**: documento sólido, prescrição clara, pedido sem causa de pedir.
- Valor: usar o valor atribuído na inicial como teto provisório; atualização e juros pelo núcleo `juros-e-correcao`; sem tabela de INSS/IR de memória.
- Lembrar o custo de perder: honorários de sucumbência de 5% a 15% (art. 791-A) e multa de 50% sobre o incontroverso não pago em audiência (art. 467).

## Recomendações típicas
- Pagar ou depositar em audiência a parte incontroversa das verbas rescisórias (art. 467).
- Avaliar acordo quando a soma dos riscos prováveis supera o custo de defesa e a multa do art. 477 §8º é provável (Súmula 462).
- Arguir a incompetência territorial dentro dos 5 dias, se cabível.
- Preparar preposto e testemunhas; levantar documentos com prazo interno antes da audiência.

## Checklist de entrega
- [ ] Data da notificação, da audiência e do prazo do art. 800 calculados
- [ ] Prescrição bienal e quinquenal verificadas com datas
- [ ] Cada pedido com ônus, prova, risco e valor pedido
- [ ] Lista de documentos com responsável e prazo
- [ ] Incontroverso identificado e valor indicado
- [ ] Terceiros/grupo econômico analisados
- [ ] Recomendação clara: defesa, acordo (faixa) ou ambos
- [ ] Atualização de valores remetida ao `juros-e-correcao`

## Erros a evitar
- Descobrir no dia da audiência que o prazo do art. 800 passou.
- Classificar jornada como risco remoto sem saber quantos trabalhadores há no estabelecimento.
- Aplicar a Súmula 338, I, com o número de empregados antigo: o art. 74 §2º hoje fala em mais de 20 trabalhadores; a redação da súmula consultada ainda menciona mais de 10 [VERIFICAR: atualização do enunciado no portal do TST].
- Mandar preposto sem conhecimento dos fatos: a confissão ficta pesa igual.
- Somar valores sem separar o que é pedido principal do que é reflexo.

## Integração com o núcleo
`prazos-processuais`, `juros-e-correcao`, `fidelidade-factual`, `verificacao-de-citacoes`, `estilo-forense`.

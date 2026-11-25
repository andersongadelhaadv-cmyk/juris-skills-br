---
name: contratos-prestacao-de-servicos
description: >
  Redige contrato de prestação de serviços civil ou empresarial, regido pelos
  arts. 593 a 609 do Código Civil e pela teoria geral dos contratos: escopo,
  níveis de serviço, remuneração, prazo máximo de quatro anos, aviso prévio,
  responsabilidade, confidencialidade, LGPD e rescisão. Use quando o usuário
  pedir contrato de prestação de serviços, contrato de consultoria, de
  manutenção, de assessoria, de serviços técnicos ou profissionais, ou
  quiser ajustar um modelo desse tipo a um caso concreto.
metadata:
  area: contratos
  tipo_peca: contrato
  verificado_em: 2026-11-25
---
# Contrato de prestação de serviços

Ferramenta de apoio; o advogado responsável revisa todo documento antes de assinar ou enviar.

## Quando usar / quando não usar
- Usar: serviço lícito, material ou imaterial, mediante retribuição (art. 594), não sujeito à CLT nem a lei especial (art. 593).
- Não usar: prestador pessoa jurídica que trabalha como se fosse empregado, com risco de vínculo (`contratos-prestacao-de-servicos-pj`); obra com resultado e materiais (empreitada, arts. 610 e seguintes — use `contratos-elaboracao-de-contrato` adaptando); revisão de minuta alheia (`contratos-analise-e-revisao-de-contrato`).
- Tomador consumidor final (art. 2º do CDC): aplica-se o CDC; não use limitação ou exoneração de responsabilidade do fornecedor (art. 51, I).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Partes, CNPJ/CPF, representantes; quem é o cliente do escritório (tomador ou prestador).
2. Escopo exato: atividades, entregáveis, o que está fora do escopo, local e forma de execução.
3. Obrigação de meio ou de resultado? Há níveis de serviço (prazos de atendimento, disponibilidade)?
4. Remuneração: fixa, por hora, por entrega, êxito; vencimentos; reembolso de despesas; tributos e retenções.
5. Prazo: determinado (máximo legal de 4 anos — art. 598) ou indeterminado; renovação.
6. O prestador precisa de habilitação legal (conselho profissional, licença)? (art. 606)
7. Pode subcontratar? Quem são os profissionais-chave?
8. Acesso a dados pessoais, informações confidenciais ou propriedade intelectual gerada.
9. Seguro de responsabilidade, garantias, retenções.

## Prazos relevantes
- Duração máxima de 4 anos por contrato, mesmo para obra certa (art. 598). Para relação mais longa, novo contrato ao fim do período.
- Sem prazo estipulado, qualquer parte pode resolver mediante aviso prévio, com antecedência conforme a periodicidade da retribuição (art. 599, parágrafo único).
- Prescrição por inadimplemento contratual: 10 anos (art. 205), inclusive ressarcimento de valores pagos a mais em prestação de serviço (AgInt nos EDcl no AREsp 2.038.138); cobrança de valor líquido fixado no contrato: 5 anos (art. 206, § 5º, I).
- Prazos processuais: `prazos-processuais`.

## Estrutura do documento (cláusulas essenciais)
Partes → objeto e escopo (anexo técnico) → forma de execução e autonomia técnica → níveis de serviço → obrigações do prestador → obrigações do tomador → remuneração, reembolsos e tributos → prazo → pessoal e subcontratação → propriedade intelectual → confidencialidade e LGPD → responsabilidade e seguro → rescisão e transição → penalidades → comunicações → foro ou arbitragem → assinaturas. Detalhe em [estrutura](references/estrutura.md).

## Riscos e cláusulas sensíveis
- **Escopo:** a falta de definição atrai o art. 601 (o prestador se obriga a qualquer serviço compatível com suas forças e condições) — delimite.
- **Retribuição:** sem ajuste, é arbitrada pelo costume (art. 596) e paga ao final (art. 597). Defina valor e cronograma.
- **Saída antecipada:** contrato por prazo ou obra certa — prestador que sai sem justa causa responde por perdas e danos (art. 602); tomador que dispensa sem justa causa paga o vencido e metade do que restaria (art. 603). Avalie se quer manter essa regra legal ou substituí-la por multa e aviso prévio expressos.
- **Cláusulas de remuneração na rescisão:** em contrato paritário, o STJ tem prestigiado o que foi pactuado (REsp 1.799.039; REsp 2.235.996 — honorários de êxito condicionados à permanência do contrato, entre pessoas jurídicas).
- **Pessoalidade e cessão:** nenhuma parte transfere o direito aos serviços ou substitui o prestador sem anuência (art. 605) — preveja subcontratação expressamente se desejada.
- **Habilitação:** sem habilitação legal, o prestador não pode cobrar a retribuição normal (art. 606).
- **Aliciamento:** quem alicia prestador vinculado por contrato escrito paga o equivalente a dois anos de retribuição (art. 608) — útil em cláusula de não aliciamento.
- **Cláusula penal:** proporcional; o juiz reduz a excessiva (art. 413).
- **LGPD:** se o prestador trata dados por conta do tomador, ele é operador (art. 5º, VII) e segue instruções do controlador (art. 39); cláusula de incidentes, suboperadores, eliminação ao fim.
- **Risco trabalhista:** se a execução tiver pessoalidade, habitualidade e subordinação de pessoa física, migre para `contratos-prestacao-de-servicos-pj`.

## Fundamentos verificados
- CC: arts. 593 a 609 (prestação de serviço); 205, 206, 412, 413, 421, 421-A, 422, 473 a 477.
- Lei 13.874/2019, art. 7º; LGPD arts. 5º, VI e VII, 39; CDC arts. 2º e 51, I.
- STJ: REsp 1.799.039; REsp 2.235.996; AgInt nos EDcl no AREsp 2.038.138; AREsp 2.978.644 (art. 413).
Detalhe em [fundamentos](references/fundamentos.md).

## Checklist antes de assinar/enviar
- [ ] Escopo e exclusões em anexo, com entregáveis e critérios de aceite
- [ ] Meio ou resultado definido; SLA e consequência do descumprimento
- [ ] Remuneração, vencimentos, reembolsos, tributos e retenções
- [ ] Prazo dentro de 4 anos (art. 598) e regra de renovação
- [ ] Aviso prévio e efeitos da saída antecipada (arts. 599, 602, 603) ajustados por escrito
- [ ] Subcontratação e substituição de pessoal (art. 605)
- [ ] Habilitação legal do prestador conferida (art. 606)
- [ ] Propriedade intelectual e confidencialidade com prazo pós-contrato
- [ ] LGPD (papéis, instruções, incidentes, eliminação)
- [ ] Juros e correção remetidos ao núcleo

## Erros a evitar
- Contrato "por prazo indeterminado" que na prática vira relação de emprego disfarçada.
- Prazo de 5 anos ou mais num só instrumento (art. 598).
- Prever exclusividade, horário e chefia sobre pessoa física prestadora sem avaliar o risco trabalhista.
- Omitir o que acontece com material, acessos e dados no fim do contrato.
- Fixar taxa de juros ou índice de memória: use `juros-e-correcao`.

## Integração com o núcleo
`juros-e-correcao`, `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

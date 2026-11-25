---
name: digital-notificacao-de-incidente-lgpd
description: >
  Conduz a resposta jurídica a incidente de segurança com dados pessoais:
  avaliação de risco ou dano relevante, comunicação à ANPD, comunicação aos
  titulares, declaração de comunicação e registro interno, com base no art. 48
  da LGPD e no Regulamento de Comunicação de Incidente de Segurança (Resolução
  CD/ANPD nº 15/2024). Use quando o usuário relatar vazamento, invasão,
  ransomware, acesso indevido, envio de dados ao destinatário errado, perda de
  base ou de dispositivo, ou pedir para notificar a ANPD ou avisar clientes e
  usuários sobre incidente.
metadata:
  area: digital
  tipo_peca: notificacao
  verificado_em: 2026-11-25
---
# Notificação de incidente de segurança (LGPD)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: o cliente é **controlador** e confirmou evento adverso que comprometeu confidencialidade, integridade, disponibilidade ou autenticidade de dados pessoais (Res. 15/2024, art. 3º, XII).
- Usar também para o parecer interno que conclui **não** comunicar: o registro é obrigatório mesmo sem comunicação (art. 10).
- Não usar: o cliente é o **titular** atingido e quer reparação (`digital-indenizacao-por-vazamento-de-dados`); o cliente é **operador** e precisa avisar o controlador — o dever nasce do contrato (`digital-contrato-dpa-operador`); pedido individual de informação após o vazamento (`digital-resposta-a-titular-de-dados`); defesa em ação de consumo (`consumidor-defesa-do-fornecedor`).

## Entradas mínimas (perguntar o que faltar; nunca supor fatos)
1. Data e hora em que o controlador **soube que o incidente afetou dados pessoais** (termo inicial do prazo) e, se possível, data da ocorrência.
2. Descrição do evento e causa provável; o incidente está contido?
3. Categorias de dados afetados (identificação, autenticação, financeiros, sensíveis, sigilo profissional etc.).
4. Número de titulares afetados — discriminar crianças, adolescentes e idosos — e total de titulares da atividade afetada.
5. Medidas de segurança existentes **antes** e adotadas **depois** (criptografia que torne os dados ininteligíveis pesa a favor — LGPD art. 48, § 3º).
6. Operador envolvido, se houver; encarregado (nome e contato) ou representante com procuração.
7. O controlador é agente de pequeno porte? Faz tratamento de alto risco? (afeta o prazo).
8. Meios usuais de contato com os titulares (e-mail, app, SMS, carta) e se é possível identificá-los individualmente.
9. Legislação setorial com prazo próprio (financeiro, saúde, telecom etc.) [VERIFICAR caso a caso].

## Prazo e contagem
- **ANPD: 3 dias úteis** do conhecimento de que o incidente afetou dados pessoais (Res. 15/2024, art. 6º, caput e § 1º), salvo prazo de legislação específica.
- **Titulares: 3 dias úteis**, mesmo termo inicial (art. 9º, caput).
- **Complementação** à ANPD: até 20 dias úteis da comunicação, de forma fundamentada (art. 6º, § 3º). Comunicar no prazo com o que se tem e completar depois é melhor do que atrasar.
- **Declaração** de que os titulares foram comunicados: até 3 dias úteis após o fim do prazo do art. 9º (art. 9º, § 4º).
- **Pequeno porte:** prazos do art. 6º (caput e § 3º) e do art. 9º contados em dobro (arts. 6º, § 8º, e 9º, § 6º), desde que o agente não esteja excluído pela Res. 2/2022, art. 3º (alto risco, faturamento acima do limite, grupo econômico).
- Divulgação ampla (sem contato individual possível): no mínimo 3 meses no site, app, redes e canais de atendimento (art. 9º, § 3º).
- Registro interno: guarda mínima de 5 anos (art. 10).
- Contagem de prazos processuais, se o caso virar processo: `prazos-processuais`.

## Estrutura da peça
Quatro documentos, nesta ordem:
1. **Parecer de avaliação de risco** — o incidente pode afetar significativamente interesses e direitos fundamentais **e** envolve ao menos um critério do art. 5º? Conclusão: comunicar / não comunicar.
2. **Comunicação à ANPD** — formulário eletrônico da ANPD (art. 6º, § 4º), com os 12 itens do art. 6º, § 2º, e documento de vínculo do encarregado ou procuração (art. 6º, §§ 5º e 6º).
3. **Comunicação aos titulares** — linguagem simples, direta e individualizada (art. 9º, § 1º), com os 7 itens do art. 9º e recomendações práticas de mitigação.
4. **Registro do incidente** — conteúdo mínimo do art. 10, § 1º.
Roteiro detalhado em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Quem comunica:** o controlador, por meio do encarregado (com prova do vínculo) ou de representante constituído com poderes perante a ANPD (art. 6º, § 5º). Sem esses documentos no prazo, a ANPD pode abrir procedimento de apuração (§ 7º).
- **Teste de relevância (art. 5º):** cumulativo — impacto significativo (impedir exercício de direitos ou uso de serviço, danos materiais ou morais, discriminação, fraude, roubo de identidade — § 1º) **e** ao menos um critério: dados sensíveis; de crianças, adolescentes ou idosos; financeiros; de autenticação; protegidos por sigilo legal, judicial ou profissional; ou em larga escala.
- **Sigilo:** pedir à ANPD, fundamentadamente, o sigilo de informações comerciais ou industriais (art. 7º).
- **Coerência:** o que se diz à ANPD, aos titulares e à imprensa deve ser o mesmo; tudo pode ser usado em ação de indenização.
- Não reconhecer culpa nem antecipar valores na comunicação: descrever fatos e medidas.

## Fundamentos verificados
- LGPD (Lei 13.709/2018): art. 46 (medidas de segurança), art. 47 (dever persiste após o tratamento), art. 48 (comunicação; conteúdo mínimo do § 1º; poderes da ANPD do § 2º; dados ininteligíveis do § 3º), art. 52 (sanções).
- Resolução CD/ANPD nº 15/2024 (Regulamento de Comunicação de Incidente de Segurança): arts. 3º, 5º, 6º, 7º, 9º, 10, 19.
- Resolução CD/ANPD nº 2/2022 (agentes de pequeno porte): arts. 3º e 14.
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
Na comunicação à ANPD:
- Registro da comunicação preliminar, com protesto pela complementação em 20 dias úteis.
- Sigilo das informações comerciais e de segurança indicadas (art. 7º).
- Declaração de agente de pequeno porte, quando for o caso (art. 6º, § 2º, IX).
- Juntada posterior da declaração de comunicação aos titulares (art. 9º, § 4º).

## Checklist pré-protocolo
- [ ] Data do conhecimento documentada (e-mail, ticket, log) e prazo calculado em dias úteis
- [ ] Teste do art. 5º feito por escrito, com os dois requisitos
- [ ] Os 12 itens do art. 6º, § 2º, preenchidos ou justificada a falta
- [ ] Motivo da demora explicado, se fora do prazo (art. 6º, § 2º, V; art. 9º, IV)
- [ ] Prova do vínculo do encarregado ou procuração anexada
- [ ] Texto aos titulares revisado para linguagem simples, sem jargão técnico
- [ ] Meio de envio aos titulares definido; plano B de divulgação ampla por 3 meses
- [ ] Pedido de sigilo formulado, se houver segredo comercial
- [ ] Registro interno aberto (art. 10), inclusive se a conclusão for não comunicar

## Erros a evitar
- Contar o prazo da data da ocorrência ou da conclusão da perícia: conta do **conhecimento de que dados pessoais foram afetados**.
- Esperar a investigação terminar para comunicar: a lei admite complementação.
- Comunicar só a ANPD e esquecer os titulares (os prazos correm juntos).
- Aviso genérico ("pode ter havido um incidente") sem riscos concretos nem orientações ao titular.
- Usar prazo dobrado de pequeno porte sem conferir as exclusões do art. 3º da Res. 2/2022.
- Não guardar o registro do incidente não comunicado.

## Integração com o núcleo
`prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`. Ações decorrentes: `digital-indenizacao-por-vazamento-de-dados`. Valores e atualização, se houver: `juros-e-correcao`.

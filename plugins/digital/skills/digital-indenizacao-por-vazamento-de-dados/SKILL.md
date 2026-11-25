---
name: digital-indenizacao-por-vazamento-de-dados
description: >
  Redige ação do titular contra controlador e/ou operador por vazamento ou
  exposição indevida de dados pessoais — obrigação de fazer (informação,
  contenção) cumulada com indenização por danos materiais e morais —, com base
  nos arts. 42 a 45 da LGPD, no CDC e na jurisprudência do STJ que separa dados
  comuns (dano não presumido) de dados sensíveis e de fraude viabilizada pelo
  vazamento. Use quando o usuário pedir ação por vazamento de dados, dados
  expostos por empresa, golpe com dados vazados, ataque hacker a fornecedor,
  dados de saúde ou bancários expostos ou indenização com base na LGPD.
metadata:
  area: digital
  tipo_peca: inicial
  verificado_em: 2026-11-25
---
# Indenização por vazamento de dados pessoais

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: o cliente é **titular** cujos dados foram expostos por falha de segurança ou tratamento irregular de empresa ou órgão, com ou sem fraude posterior.
- Não usar: o cliente é a empresa (comunicação: `digital-notificacao-de-incidente-lgpd`; defesa em ação de consumo: `consumidor-defesa-do-fornecedor`); quer só informação ou eliminação, sem litígio (`digital-resposta-a-titular-de-dados`); ofensa ou exposição feita por pessoa em rede social (`digital-ofensas-em-redes-sociais`, `digital-remocao-de-conteudo`); negativação decorrente de fraude (`consumidor-negativacao-indevida`); fraude bancária sem vazamento atribuível (`consumidor-acao-indenizatoria`); réu ente público (`adm-responsabilidade-civil-do-estado`).

## Entradas mínimas (perguntar o que faltar; nunca supor fatos)
1. Como o cliente soube: comunicação do controlador, notícia, aviso de terceiro, golpe sofrido? Guardar o documento.
2. Quais dados vazaram: comuns (nome, CPF, endereço, telefone) ou **sensíveis** (saúde, biometria, religião etc. — LGPD art. 5º, II), financeiros, senhas, dados sigilosos de operação.
3. Relação com o réu: cliente/consumidor, empregado, paciente, ou sem relação (consumidor por equiparação — CDC art. 17).
4. Consequências concretas: golpe consumado, tentativa, contratações fraudulentas, contatos de criminosos, perdas financeiras, tempo gasto, abalo comprovável.
5. Nexo: o golpista usou informação que só o réu tinha? (decisivo para o dano moral).
6. Operador envolvido (nuvem, call center, fornecedor de TI)?
7. Pedido prévio ao controlador (arts. 18 e 19) e resposta recebida.
8. Datas: do incidente, do conhecimento do dano e da autoria (termo inicial da prescrição consumerista).

## Prazo e contagem
- **Relação de consumo (inclusive por equiparação):** 5 anos do conhecimento do dano e de sua autoria (CDC art. 27). Em relação de consumo, a LGPD remete à legislação consumerista (LGPD art. 45).
- **Fora de relação de consumo:** prazo não conferido em precedente específico de LGPD [VERIFICAR: STJ sem precedente localizado no JuriBase sobre prescrição em vazamento fora do CDC].
- Prazos processuais em dias úteis: `prazos-processuais`.

## Estrutura da peça
Fatos e linha do tempo → relação de consumo / equiparação → incidente e tratamento irregular (art. 44) → responsabilidade do controlador e do operador (arts. 42 e 43; CDC art. 14) → dano moral conforme a categoria dos dados → dano material → obrigação de fazer (arts. 18, VII, e 19, II) → inversão do ônus → tutela de urgência → pedidos. Roteiro em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Foro:** domicílio do consumidor autor (CDC art. 101, I).
- **Polo passivo:** controlador; operador solidariamente se descumpriu a lei ou as instruções (LGPD art. 42, § 1º, I); controladores diretamente envolvidos (§ 1º, II).
- **Excludentes do réu (art. 43):** não tratou; tratou sem violar a lei; culpa exclusiva do titular ou de terceiro. Ataque hacker **não** é excludente automática: o réu precisa provar que o vazamento decorreu exclusivamente do ataque e que oferecia a segurança esperada (REsp 2.147.374; LGPD art. 44, III). Banco: fraude de terceiro é fortuito interno (Súmula 479/STJ).
- **Ônus da prova:** inversão pela LGPD (art. 42, § 2º) e pelo CDC (art. 6º, VIII); redistribuição dinâmica (CPC art. 373, § 1º). Pedir exibição do relatório do incidente e da comunicação à ANPD.
- **Prova antecipada:** se o réu nega o incidente, considerar produção antecipada (CPC art. 381).
- **Dano moral — enfrentar a jurisprudência de frente:**
  - Dados **comuns**, sem consequência: o STJ (2ª Turma) afirmou que o vazamento, por si só, não gera dano moral presumido; o titular deve provar o dano (AREsp 2.130.619). Na mesma linha, a 3ª Turma, para compartilhamento com consentimento e base legal sem dano concreto (REsp 2.211.708).
  - Dados **sensíveis**: a 3ª Turma reconheceu dano moral presumido e responsabilidade objetiva em vazamento de dados sensíveis de segurado (REsp 2.121.904).
  - **Fraude viabilizada pelo vazamento**: a 3ª Turma reconheceu dano moral quando o golpe usou dados sigilosos vazados pelo banco (REsp 2.187.854).
  - Não há tese repetitiva localizada sobre o tema [VERIFICAR: busca no JuriBase sem cobertura para afetação]. Com dados comuns, descreva e prove consequências concretas.

## Fundamentos verificados
- CF art. 5º, X e LXXIX; LGPD arts. 5º, II, 6º, 18, 19, 42 a 46, 48; CDC arts. 6º, 14, 17, 27, 101; CPC arts. 300, 373, 381, 497, 537.
- STJ: AREsp 2.130.619; REsp 2.147.374; REsp 2.121.904; REsp 2.187.854; REsp 2.211.708; Súmula 479.
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Tutela de urgência (CPC art. 300) para informar, em prazo curto, quais dados vazaram, com quem houve compartilhamento e medidas adotadas, com multa (CPC art. 537).
- Obrigação de fazer definitiva: lista de compartilhamentos (LGPD art. 18, VII), declaração completa e cópia dos dados (art. 19, II), medidas de segurança e eliminação de excessos (CPC art. 497).
- Danos materiais comprovados (valores do golpe, despesas).
- Dano moral, com valor fundamentado nas circunstâncias (categoria dos dados, consequências, conduta do réu após o incidente); juros e correção pelo núcleo `juros-e-correcao`.
- Inversão do ônus da prova e exibição do relatório do incidente e da comunicação à ANPD.

## Checklist pré-protocolo
- [ ] Prova do vazamento e de que os dados do cliente estavam no conjunto
- [ ] Categoria dos dados definida (comuns, sensíveis, financeiros, sigilosos)
- [ ] Consequências concretas documentadas — ou, se não houver, risco do AREsp 2.130.619 exposto ao cliente
- [ ] Nexo entre o dado vazado e o golpe demonstrado
- [ ] Operador incluído no polo se houver indício de falha dele
- [ ] Prescrição calculada (art. 27 do CDC, se consumo)
- [ ] Pedido de obrigação de fazer além da indenização
- [ ] Juros e correção remetidos ao núcleo

## Erros a evitar
- Pedir dano moral "in re ipsa" por vazamento de dados comuns sem prova de consequência.
- Classificar CPF, endereço ou telefone como dado sensível (o art. 5º, II, é taxativo, conforme o AREsp 2.130.619).
- Aceitar "ataque hacker" como excludente sem exigir prova da segurança adotada.
- Esquecer o pedido de informação dos arts. 18, VII, e 19, II, que costuma ser acolhido mesmo sem dano moral.
- Citar precedente da 3ª Turma como se fosse posição pacífica do STJ.

## Integração com o núcleo
`juros-e-correcao`, `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

---
name: trabalhista-terceirizacao
description: >
  Estrutura o pedido (ou a defesa) de responsabilidade do tomador na
  terceirização e no trabalho temporário pela Lei 6.019/1974 (arts. 4º-A a 5º-D,
  10 §7º): licitude da terceirização de qualquer atividade (Tema 725 do STF),
  responsabilidade subsidiária do contratante privado, regime da Administração
  Pública (Temas 246 e 1118 do STF; Súmula 331 do TST, com item I cancelado) e
  quarentena de 18 meses. Use quando o usuário pedir incluir o tomador na
  reclamação, responsabilidade subsidiária, terceirizada sem receber verbas,
  defesa da tomadora ou do ente público, ou contrato de prestação de serviços.
metadata:
  area: trabalhista
  tipo_peca: outro
  verificado_em: 2026-11-25
---
# Terceirização e responsabilidade do tomador (Lei 6.019/1974)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar (empregado): incluir a tomadora no polo passivo e pedir sua responsabilidade subsidiária pelas verbas do período em que se beneficiou do trabalho. Tópico da `trabalhista-reclamacao`.
- Usar (tomadora privada ou ente público): defesa contra a responsabilização. Tópico da `trabalhista-contestacao`.
- Usar (consultivo): requisitos da prestadora e cláusulas do contrato de prestação de serviços.
- Não usar: pedido de vínculo direto com a tomadora por fraude (pessoalidade e subordinação direta, pejotização): `trabalhista-vinculo-de-emprego`. Licitação e fiscalização do contrato administrativo em si: plugin `administrativo-licitacoes`.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Quem é a empregadora (prestadora) e quem é a tomadora; se a tomadora é privada ou integra a Administração Pública.
2. Período exato em que o trabalhador prestou serviço à tomadora (pode ser menor que o contrato com a prestadora).
3. Local de trabalho (dependências da tomadora ou outro) e quem dava ordens no dia a dia.
4. Verbas não pagas e situação da prestadora (ativa, fechada, em recuperação, falida).
5. Se a tomadora é ente público: houve notificação formal à Administração sobre o descumprimento (por trabalhador, sindicato, MPT, MTE, Defensoria)? Com qual data e resposta?
6. Se é trabalho temporário: motivo da contratação, duração, prorrogação.
7. Se o trabalhador ou o sócio da prestadora era ex-empregado da tomadora e quando saiu (quarentena de 18 meses).

## Prazo e contagem
- Prescrição: cinco anos, até dois anos após a extinção do contrato (CF art. 7º, XXIX). Ajuizar contra a tomadora dentro do mesmo prazo.
- Temporário: até 180 dias, prorrogáveis por até 90 (Lei 6.019/1974, art. 10, §§ 1º e 2º); nova colocação na mesma tomadora só após 90 dias do término (§ 5º).
- Prazos processuais: `prazos-processuais`.

## Estrutura da peça
Relação triangular (prestadora, tomadora, período) → inadimplemento da prestadora → fundamento da responsabilidade (privada ou pública) → limites (período da prestação) → pedidos contra cada ré. Roteiro em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Licitude**: é lícita a terceirização de qualquer atividade, inclusive a principal, mantida a responsabilidade subsidiária da contratante (Tema 725 do STF; Lei 6.019/1974, arts. 4º-A e 5º-A). Não há vínculo entre a contratante e os empregados da prestadora (art. 4º-A, § 2º); a ilicitude, se houver, vem de fraude concreta (pessoalidade e subordinação direta), não da natureza da atividade. O item I da Súmula 331 do TST foi cancelado por perda de eficácia a partir de 11/11/2017.
- **Tomadora privada**: responde subsidiariamente pelas obrigações trabalhistas do período da prestação (art. 5º-A, § 5º); no temporário, art. 10, § 7º. Precisa ter participado do processo e constar do título (Súmula 331, IV).
- **Administração Pública**: o inadimplemento não transfere automaticamente a responsabilidade (Tema 246 do STF). Não há responsabilidade amparada só na inversão do ônus da prova; o autor precisa provar comportamento negligente ou nexo causal. Há negligência quando a Administração fica inerte após notificação formal do descumprimento (Tema 1118 do STF). A Administração responde pelas condições de segurança, higiene e salubridade no seu local de trabalho (Tema 1118; art. 5º-A, § 3º). Não se forma vínculo com o ente público (Súmula 331, II).
- **Requisitos da prestadora**: CNPJ, registro e capital social mínimo conforme o número de empregados (art. 4º-B); capacidade econômica compatível (art. 4º-A).
- **Quarentena**: não pode ser contratada a PJ cujos titulares ou sócios prestaram serviço à contratante nos 18 meses anteriores, salvo aposentados (art. 5º-C); ex-empregado dispensado só volta como terceirizado após 18 meses (art. 5º-D).
- **Abrangência**: a responsabilidade subsidiária abrange todas as verbas da condenação do período da prestação (Súmula 331, VI).

## Fundamentos verificados
Lei 6.019/1974, arts. 2º, 4º-A, 4º-B, 4º-C, 5º-A, 5º-B, 5º-C, 5º-D, 9º, 10, 12 e 16; CF art. 7º, XXIX; Temas 725, 246 e 1118 do STF; Súmula 331 do TST (itens II a VI; item I cancelado). ADPF 324 não localizada na base consultada. Detalhes em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Condenação da prestadora (empregadora) nas verbas devidas.
- Responsabilidade subsidiária da tomadora pelo período da prestação, com indicação das datas.
- Ente público: fatos e provas da negligência (notificação formal e inércia; falta de exigência de comprovação de quitação) — não basta pedir inversão do ônus.
- Pedido de exibição do contrato de prestação de serviços e dos documentos de fiscalização.
- Valores liquidados (CLT art. 840 § 1º); correção e juros pelo núcleo `juros-e-correcao`.

## Checklist pré-protocolo
- [ ] Tomadora no polo passivo desde a inicial (sem isso não há título contra ela).
- [ ] Período de prestação à tomadora delimitado com prova (crachá, escala, e-mails, testemunhas).
- [ ] Natureza da tomadora identificada (privada x pública) e fundamento correspondente.
- [ ] Ente público: notificação formal e data da inércia documentadas, ou outra prova concreta de negligência.
- [ ] Não invocar o item I da Súmula 331 nem a tese de "atividade-fim ilícita".
- [ ] Temporário: prazos do art. 10 conferidos.
- [ ] Pedidos liquidados; juros e correção remetidos ao núcleo.

## Erros a evitar
- Pedir vínculo com a tomadora só porque o serviço era sua atividade principal (superado pelo Tema 725).
- Pedir responsabilidade do ente público com base apenas no inadimplemento ou na inversão do ônus da prova (Temas 246 e 1118).
- Esquecer de limitar a responsabilidade ao período em que a tomadora se beneficiou do trabalho.
- Na defesa da tomadora privada, negar a subsidiariedade em tese: o debate útil é o período e a efetiva prestação.

## Integração com o núcleo
`juros-e-correcao`, `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

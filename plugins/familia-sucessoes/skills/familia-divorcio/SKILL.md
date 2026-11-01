---
name: familia-divorcio
description: >
  Redige divórcio litigioso ou consensual (judicial ou por escritura), com partilha, guarda,
  convivência, alimentos e nome, a partir da EC 66/2010 (CF art. 226 §6º), CPC arts. 693 a
  699-A e 731 a 733 e Res. CNJ 35/2007 com as alterações de 2024 e 2026. Use quando o
  usuário pedir divórcio, divórcio litigioso, divórcio consensual, divórcio em cartório,
  divórcio extrajudicial, partilha de bens no divórcio, divórcio com filhos menores.
metadata:
  area: familia-sucessoes
  tipo_peca: inicial
  verificado_em: 2026-11-01
---
# Divórcio (litigioso, consensual judicial e extrajudicial)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: dissolução do casamento, com ou sem partilha, guarda, convivência e alimentos.
- Não usar: união estável (use `familia-uniao-estavel`); somente guarda/convivência (use `familia-guarda-e-convivencia`); somente alimentos (use `familia-acao-de-alimentos`).
- Separação judicial: não é mais requisito nem figura autônoma (STF Tema 1053); não redigir pedido de separação.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Certidão de casamento atualizada, data do casamento, regime de bens, pacto antenupcial.
2. Data da separação de fato (relevante para a partilha e para frutos/administração).
3. Filhos: idades, incapacidade, nascituro; com quem estão; proposta de guarda, convivência e alimentos.
4. Bens e dívidas: imóveis (matrícula), veículos, contas, investimentos, quotas, FGTS/previdência, dívidas comuns; o que é particular (anterior, herança, doação, sub-rogação).
5. Alimentos entre cônjuges: necessidade e capacidade.
6. Nome: manter ou retomar o de solteiro.
7. Consenso ou litígio; histórico de violência doméstica.

## Prazo e contagem
- Não há prazo mínimo de casamento nem de separação de fato (EC 66/2010).
- Litigioso: citação com antecedência mínima de 15 dias da audiência (CPC 695 §2º); sem acordo, contestação pelo procedimento comum (CPC 697 e 335). Contagem via `prazos-processuais`.

## Estrutura da peça
Litigioso: endereçamento → qualificação → casamento e regime → filhos → pedido de divórcio (direito potestativo) → partilha → guarda/convivência/alimentos → nome → tutelas → pedidos. Consensual: petição conjunta com as cláusulas do CPC 731. Escritura: minuta para o tabelião (CPC 733; Res. CNJ 35). Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Competência (CPC 53, I), em ordem: havendo filho incapaz, foro de quem tem sua guarda; sem filho incapaz, o último domicílio comum; se ninguém mais mora lá, o do réu; a vítima de violência doméstica pode ajuizar no próprio domicílio.
- Segredo de justiça (CPC 189, II); MP só com incapaz ou vítima de violência doméstica (CPC 698).
- O divórcio pode ser decretado sem prévia partilha (CC 1.581; Súmula 197 STJ) — pedir decretação liminar ou julgamento parcial do divórcio e prosseguir quanto ao resto.
- Extrajudicial (CPC 733): sem nascituro nem filhos incapazes, salvo se guarda, convivência e alimentos já estiverem resolvidos judicialmente (Res. CNJ 35, art. 34 §2º, na redação da Res. 571/2024); advogado obrigatório.
- Inventário/partilha em escritura não depende mais de prévio recolhimento do ITCMD (Res. CNJ 35, art. 15, na redação da Res. CNJ 695/2026), mas a escritura registra as obrigações tributárias declaradas e o tabelião comunica o fisco — relevante quando a partilha do divórcio for desigual (possível doação tributável).

## Fundamentos verificados
CF 226 §6º; CC 1.571, 1.581, 1.639, 1.658 a 1.660; CPC 53, 189, 693 a 699-A, 731 a 733; Súmula 197 STJ; STF Temas 1053 e 1236; Súmula 377 STF; Súmula 655 STJ. Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- [ ] Decretação do divórcio (se possível, em tutela de evidência ou julgamento antecipado parcial).
- [ ] Partilha conforme regime, com relação individualizada de bens e dívidas; subsidiariamente, partilha em fase posterior (CPC 731 p.ú.).
- [ ] Guarda, convivência e alimentos dos filhos (ou remissão à ação própria).
- [ ] Alimentos entre cônjuges, se houver necessidade.
- [ ] Nome: manutenção ou retorno ao de solteiro.
- [ ] Averbação no registro civil e no registro de imóveis.
- [ ] Gratuidade, segredo, honorários.

## Checklist pré-protocolo
- [ ] Regime de bens confirmado na certidão/pacto (e Tema 1236 STF para maiores de 70 anos).
- [ ] Bens particulares separados dos comuns, com prova da origem.
- [ ] Data da separação de fato informada.
- [ ] Na via extrajudicial: ausência de nascituro/incapazes, ou prova de prévia resolução judicial das questões dos filhos.
- [ ] Partilha desigual: avaliação de ITCMD sobre o excesso (lei estadual).
- [ ] Pergunta sobre violência doméstica registrada (CPC 699-A em ações de guarda).

## Erros a evitar
- Pedir "separação judicial" ou condicionar o divórcio a prazo.
- Amarrar a decretação do divórcio ao fim da discussão patrimonial.
- Partilhar bens particulares (herança, doação, anteriores ao casamento) como comuns.
- Esquecer dívidas comuns e FGTS/aplicações na relação de bens.
- Lavrar escritura com filho incapaz sem decisão judicial prévia sobre guarda, convivência e alimentos.

## Integração com o núcleo
`prazos-processuais`, `juros-e-correcao` (reposições, aluguel por uso exclusivo, alimentos), `verificacao-de-citacoes`, `fidelidade-factual` (bens e datas), `estilo-forense`.

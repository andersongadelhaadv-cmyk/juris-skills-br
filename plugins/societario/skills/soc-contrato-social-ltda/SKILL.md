---
name: soc-contrato-social-ltda
description: >
  Elabora contrato social de sociedade limitada (pluripessoal ou unipessoal) e
  suas alterações, com as cláusulas obrigatórias do art. 997 e o regime dos
  arts. 1.052 a 1.087 do Código Civil: capital e quotas, administração,
  deliberações e quóruns, cessão de quotas, exclusão, morte, retirada e
  apuração de haveres. Use quando o usuário pedir contrato social de LTDA,
  constituir empresa limitada, sociedade limitada unipessoal, alteração ou
  consolidação contratual, cláusula de exclusão por justa causa, cláusula de
  apuração de haveres ou revisão de contrato social antes do registro.
metadata:
  area: societario
  tipo_peca: contrato
  verificado_em: 2026-11-25
---
# Contrato social de sociedade limitada

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

O produto é uma minuta para registro na Junta Comercial (sociedade empresária, CC art. 1.150) ou no Registro Civil das Pessoas Jurídicas (sociedade simples que adota o tipo limitada). Toda escolha que a lei deixa ao contrato precisa ser feita de forma expressa: o silêncio do contrato atrai a regra supletiva, que costuma ser justamente a que o cliente não queria.

## Quando usar / quando não usar
- Usar: constituição de LTDA; LTDA unipessoal (CC art. 1.052, § 1º); alteração contratual (entrada e saída de sócio, capital, objeto, sede, administração); consolidação; revisão de contrato antigo para incluir exclusão por justa causa ou critério de haveres.
- Não usar:
  - pacto parassocial entre os sócios (voto, preferência, tag/drag, lock-up): `soc-acordo-de-socios`;
  - ata da deliberação que aprova a alteração: `soc-ata-de-reuniao-de-socios`;
  - holding patrimonial ou familiar: `soc-holding-familiar` (e o parecer sucessório em `sucessoes-planejamento-e-partilha-em-vida`);
  - parceria, consórcio, SCP ou joint venture contratual: `contratos-parceria-e-joint-venture`;
  - litígio (dissolução parcial, exclusão judicial, apuração de haveres): `soc-dissolucao-parcial-e-exclusao-de-socio`;
  - compra e venda de quotas: `soc-ma-compra-de-quotas-e-acoes`.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Sócios: qualificação completa, estado civil e regime de bens (cônjuge de sócio afeta cessão e sucessão), se algum é pessoa jurídica, estrangeiro ou incapaz.
2. Denominação ou firma pretendida, objeto (atividades), sede, filiais, prazo (determinado ou indeterminado).
3. Natureza: empresária ou simples (organização dos fatores de produção); isso define o registro.
4. Capital: valor, número e valor das quotas, divisão entre sócios, forma e prazo de integralização (dinheiro ou bens; bens exigem descrição e avaliação).
5. Administração: quem administra, se sócio ou não, poderes, assinatura isolada ou conjunta, limites (alienar imóvel, dar garantia, contrair dívida acima de X), pró-labore.
6. Regência supletiva: simples (padrão) ou sociedade anônima (CC art. 1.053, parágrafo único).
7. Política de saída: cessão a terceiros, direito de preferência, morte (herdeiros entram ou haveres são pagos), exclusão por justa causa, critério e prazo de pagamento de haveres.
8. Conselho fiscal? Forma das deliberações (reunião ou assembleia; meio digital)? Exercício social e destinação de lucros.

## Prazo e contagem
- Registro: o art. 998 fixa 30 dias para a inscrição da sociedade simples; para a empresária, conferir o prazo da lei de registro e as normas do DREI [VERIFICAR: prazo e efeito retroativo do arquivamento na Junta].
- Responsabilidade pela estimação de bens conferidos ao capital: solidária por 5 anos da data do registro (art. 1.055, § 1º).
- Cedente responde solidariamente por 2 anos após averbada a cessão (art. 1.003, parágrafo único); sócio que sai responde por 2 anos após averbada a resolução (art. 1.032).
- Prazos processuais em litígio societário: `prazos-processuais`.

## Estrutura da peça
Preâmbulo (qualificação) → denominação, sede, objeto, prazo → capital e quotas → integralização e responsabilidade → administração → deliberações e quóruns → conselho fiscal (se houver) → exercício, balanço e lucros → cessão e preferência → retirada, exclusão, morte e incapacidade → apuração e pagamento de haveres → dissolução e liquidação → foro ou arbitragem → declaração de desimpedimento do administrador → fecho. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Conteúdo mínimo: art. 997 (qualificação, denominação, objeto, sede, prazo, capital, quotas, administradores, participação nos lucros e perdas), aplicado à limitada pelo art. 1.054, mais a firma social se houver.
- Pacto separado que contrarie o contrato é ineficaz perante terceiros (art. 997, parágrafo único) — o que precisa valer contra todos vai no contrato.
- Vedada contribuição que consista em prestação de serviços (art. 1.055, § 2º).
- Responsabilidade de cada sócio limitada ao valor das quotas, mas todos respondem solidariamente pela integralização do capital (art. 1.052).
- Quota indivisível perante a sociedade; condôminos representados por um deles ou pelo inventariante (art. 1.056).
- Administrador não sócio: designação depende de 2/3 dos sócios enquanto o capital não estiver integralizado e de mais da metade do capital depois (art. 1.061).
- Exclusão extrajudicial por justa causa só existe se o contrato a previr (art. 1.085). Sem a cláusula, resta a via judicial (art. 1.030).

## Fundamentos verificados
- CC arts. 997, 998, 1.003, 1.004, 1.010, 1.026 a 1.032, 1.052 a 1.087, 1.150, 1.152.
- CPC arts. 599 e 606 (dissolução parcial; critério supletivo de haveres).
- STJ, REsp 2.170.665 (exclusão extrajudicial exige previsão contratual; documento assinado por todos pode valer como aditamento).
- STJ, REsp 2.020.490 e REsp 1.892.139 (haveres: prevalece o contrato; omisso ou mera repetição da lei, balanço de determinação; fundo de comércio entra, expectativa de lucro futuro não).
Detalhe em [fundamentos](references/fundamentos.md).

## Cláusulas essenciais
- **Capital**: valor, quotas, titularidade, integralização (prazo, forma; bens descritos com valor).
- **Administração**: nome, poderes, forma de assinatura, atos que exigem aprovação prévia dos sócios, prazo do mandato, remuneração.
- **Deliberações**: reunião (até 10 sócios) ou assembleia (obrigatória acima de 10 — art. 1.072, § 1º); participação e voto a distância (art. 1.080-A); quóruns legais e eventuais quóruns qualificados.
- **Cessão de quotas**: regra própria em vez da supletiva do art. 1.057 (livre entre sócios; a estranho, salvo oposição de mais de 1/4 do capital); direito de preferência, prazo e procedimento.
- **Morte de sócio**: escolher entre liquidação da quota, ingresso dos herdeiros ou acordo (art. 1.028); prever representação do espólio.
- **Exclusão por justa causa**: cláusula expressa (art. 1.085), procedimento (convocação específica, ciência do acusado, defesa).
- **Haveres**: critério (data-base, método de avaliação, intangíveis, ágio), prazo e forma de pagamento; o silêncio leva ao art. 1.031 e ao art. 606 do CPC.
- **Regência supletiva** pela LSA, se desejada (art. 1.053, parágrafo único) — necessária para acordo de quotistas arquivado com eficácia típica do art. 118 da LSA [VERIFICAR: extensão da aplicação do art. 118 à limitada].
- **Solução de conflitos**: foro ou cláusula compromissória por escrito (Lei 9.307/1996, art. 4º).

## Checklist pré-protocolo
- [ ] Todos os itens do art. 997 presentes, sem lacuna
- [ ] Natureza (empresária x simples) e órgão de registro corretos
- [ ] Capital: soma das quotas confere com o capital; prazo de integralização definido
- [ ] Bens conferidos descritos e avaliados; imóvel com matrícula e anuência do cônjuge quando exigida
- [ ] Administrador designado, com poderes e limites; declaração de desimpedimento
- [ ] Cláusulas de saída (cessão, morte, exclusão, haveres) escolhidas expressamente
- [ ] Quóruns conferidos com os arts. 1.061, 1.063, 1.076 e 1.085
- [ ] Viabilidade de nome e atividades (CNAE) conferida na Junta antes de assinar
- [ ] Juros e correção de haveres em atraso remetidos ao núcleo

## Erros a evitar
- Copiar modelo da Junta sem cláusula de exclusão: o sócio problemático só sai por ação judicial.
- Cláusula de haveres que apenas repete o art. 1.031 — o STJ aplica o balanço de determinação (REsp 2.020.490), o que pode não ser o pretendido.
- Usar quórum de unanimidade ou de 3/4 para alteração contratual como se fosse a regra atual: o art. 1.076 vigente exige mais da metade do capital (redação da Lei 14.451/2022) — quórum maior só se o contrato fixar.
- Esquecer o cônjuge e o regime de bens: herdeiros do cônjuge e o ex-cônjuge concorrem aos lucros, sem entrar de imediato na sociedade (art. 1.027).
- Prever "sócio de serviço" (vedado no art. 1.055, § 2º).
- Deixar o pagamento de haveres sem prazo nem parcelamento: a regra supletiva é dinheiro em 90 dias (art. 1.031, § 2º).

## Integração com o núcleo
`juros-e-correcao` (atualização de haveres), `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

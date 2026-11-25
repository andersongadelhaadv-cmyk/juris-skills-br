---
name: soc-acordo-de-socios
description: >
  Elabora acordo de acionistas (Lei 6.404/1976, art. 118) e acordo de quotistas
  em sociedade limitada, com cláusulas de voto e bloco de controle, direito de
  preferência, tag along e drag along contratuais, lock-up, não concorrência,
  impasse (deadlock), saída e solução de conflitos por arbitragem. Use quando
  o usuário pedir acordo de sócios, acordo de acionistas, acordo de quotistas,
  pacto parassocial, cláusula de tag along ou drag along, opção de compra ou
  venda entre sócios, shotgun, regras de governança entre sócios ou
  arquivamento do acordo na sede da companhia.
metadata:
  area: societario
  tipo_peca: contrato
  verificado_em: 2026-11-25
---
# Acordo de sócios (acionistas e quotistas)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

O acordo de sócios é contrato entre alguns ou todos os sócios, separado do estatuto ou do contrato social. Na S.A., o art. 118 da LSA dá a ele eficácia perante a companhia (se arquivado na sede) e perante terceiros (se averbado). Na limitada, a eficácia típica do art. 118 depende de fundamentação cuidadosa — e o que precisa valer contra terceiros deve estar no contrato social (CC art. 997, parágrafo único).

## Quando usar / quando não usar
- Usar: acordo de voto e de controle; regras de transferência de participação (preferência, tag/drag, lock-up, opções); governança entre sócios (indicação de administradores e conselheiros, matérias reservadas); impasse; não concorrência e confidencialidade entre sócios; entrada de investidor.
- Não usar:
  - cláusulas que precisam constar do próprio contrato social (exclusão por justa causa, critério de haveres oponível à sociedade, regência supletiva): `soc-contrato-social-ltda`;
  - ata que delibera em cumprimento do acordo: `soc-ata-de-reuniao-de-socios`;
  - holding familiar (o acordo é peça acessória da estrutura): `soc-holding-familiar`;
  - parceria entre empresas sem participação societária comum: `contratos-parceria-e-joint-venture`;
  - memorando pré-negocial com investidor: `contratos-memorando-de-entendimentos`;
  - compra e venda de participação (SPA/contrato de cessão): `soc-ma-compra-de-quotas-e-acoes`;
  - confidencialidade isolada: `contratos-nda-confidencialidade`.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Tipo societário (S.A. aberta ou fechada; LTDA) e cópia do estatuto ou contrato social vigente.
2. Partes do acordo (todos os sócios ou um bloco?), participação de cada um, cônjuges e regimes de bens.
3. Objetivo dominante: manter controle, proteger minoritário, preparar entrada ou saída de investidor, sucessão familiar.
4. Matérias de voto vinculado e forma de formar a vontade do bloco (reunião prévia, quórum, desempate).
5. Regras de transferência desejadas: preferência, tag along (percentual e preço), drag along (gatilho e preço mínimo), lock-up, opções de compra/venda e seus gatilhos (morte, divórcio, desligamento, inadimplemento).
6. Indicação de administradores/conselheiros; matérias que exigem unanimidade ou supermaioria.
7. Prazo do acordo (determinado, indeterminado, ou vinculado à condição) e hipóteses de denúncia.
8. Foro ou arbitragem (câmara, sede, idioma).

## Prazo e contagem
- Acordo com prazo fixado ou condição resolutiva só pode ser denunciado segundo suas estipulações (LSA art. 118, § 6º). Acordo por prazo indeterminado: prever expressamente a denúncia e o aviso prévio [VERIFICAR: regime de denúncia imotivada de acordo por prazo indeterminado].
- Mandato para voto outorgado no acordo pode ter prazo superior ao do art. 126, § 1º, da LSA (art. 118, § 7º).
- Prazos internos (exercício de preferência, notificação de tag/drag) devem ser fixados no texto; não há prazo supletivo legal para todos eles.
- Prazos de execução específica ou de arbitragem: `prazos-processuais`.

## Estrutura da peça
Partes e considerandos → definições → ações/quotas vinculadas → acordo de voto e reunião prévia → governança (indicações, matérias reservadas) → transferência (lock-up, preferência, tag, drag, opções) → impasse → não concorrência e confidencialidade → inadimplemento e execução específica → prazo e denúncia → arquivamento e averbação → solução de conflitos → disposições gerais e anuência da sociedade. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Objeto típico na S.A.: compra e venda de ações, preferência para adquiri-las, exercício do direito de voto ou do poder de controle (art. 118, caput).
- Eficácia: perante a companhia, com o arquivamento na sede; perante terceiros, com averbação nos livros de registro e nos certificados (art. 118, caput e § 1º).
- O acordo não exime o acionista da responsabilidade pelo exercício do voto e do poder de controle (art. 118, § 2º, que remete aos arts. 115 a 117).
- Ações averbadas não podem ser negociadas em bolsa ou balcão (art. 118, § 4º).
- Indicar representante dos acionistas vinculados para comunicação com a companhia (art. 118, § 10).
- Na limitada: prever a regência supletiva pela LSA no contrato social (CC art. 1.053, parágrafo único) quando se quiser invocar o regime do art. 118; arquivar o acordo na sede, colher anuência da sociedade e reproduzir no contrato social as restrições que precisem valer contra terceiros [VERIFICAR: extensão do art. 118 ao acordo de quotistas].
- Quotas e ações com usufruto: regular quem vota. Na S.A., sem regra no ato do gravame, voto só com acordo prévio entre nu-proprietário e usufrutuário (LSA art. 114).

## Fundamentos verificados
- Lei 6.404/1976, arts. 114 e 118 (caput e §§ 1º a 11).
- CC arts. 997, parágrafo único; 1.053, parágrafo único; 1.057; 1.074, § 2º.
- Lei 9.307/1996, arts. 4º e 5º (cláusula compromissória).
- Jurisprudência específica sobre acordo de quotistas: sem cobertura no JuriBase na consulta de 2026-11-25 [VERIFICAR].
Detalhe em [fundamentos](references/fundamentos.md).

## Cláusulas essenciais
- **Vinculação**: participações abrangidas, inclusive as adquiridas depois (bonificação, subscrição).
- **Reunião prévia**: convocação, quórum, maioria, desempate, prazo antes da assembleia, ata da reunião prévia.
- **Voto vinculado e controle**: obrigação de votar conforme a reunião prévia; consequência do voto contrário (não cômputo — art. 118, § 8º) e da ausência ou abstenção (voto pelo prejudicado com as ações do omisso — § 9º).
- **Governança**: indicação e destituição de administradores e conselheiros; matérias reservadas com quórum próprio.
- **Lock-up** com prazo e exceções (transferência a holding do próprio sócio, sucessão).
- **Preferência**: notificação com preço e condições, prazo, rateio, consequência do silêncio.
- **Tag along** (venda conjunta) e **drag along** (venda forçada), com gatilho, preço igual ou mínimo e proteção do arrastado.
- **Opções de compra/venda** por evento (morte, divórcio, saída do executivo, inadimplemento), com critério de preço objetivo.
- **Impasse**: escalonamento, mediação, shotgun/russian roulette ou venda conjunta.
- **Não concorrência e não aliciamento** com prazo, território e escopo razoáveis.
- **Execução específica** (art. 118, § 3º) e multa sem prejuízo da tutela específica.
- **Arquivamento/averbação** e anuência da sociedade.
- **Cláusula compromissória** escrita (Lei 9.307/1996, art. 4º).

## Checklist pré-protocolo
- [ ] Compatibilidade com o estatuto/contrato social (nada no acordo contraria o ato constitutivo sem ajuste deste)
- [ ] Todos os cônjuges com interesse patrimonial cientes ou anuentes, quando cabível
- [ ] Gatilhos e preços de tag, drag e opções objetivos e calculáveis
- [ ] Reunião prévia com quórum e desempate definidos
- [ ] Prazo e hipóteses de denúncia escritos
- [ ] Representante para comunicação com a sociedade indicado
- [ ] Arquivamento na sede e averbação nos livros/certificados previstos
- [ ] Na LTDA: regência supletiva da LSA prevista no contrato social e restrições oponíveis reproduzidas nele
- [ ] Atualização monetária e juros de preços diferidos remetidos ao núcleo

## Erros a evitar
- Colocar no acordo, e só nele, a restrição que precisa valer contra terceiros (CC art. 997, parágrafo único).
- Drag along sem preço mínimo nem igualdade de condições — convite ao litígio pelo minoritário arrastado.
- Prazo indeterminado sem cláusula de denúncia.
- Voto vinculado em matéria de interesse pessoal conflitante — o acordo não afasta o impedimento (CC art. 1.074, § 2º; LSA art. 118, § 2º).
- Esquecer o usufruto: doação de quotas com reserva sem regra de voto trava deliberações.
- Arbitragem sem câmara, sede e regras definidas, ou com cláusula vazia.

## Integração com o núcleo
`juros-e-correcao`, `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

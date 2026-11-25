---
name: soc-ata-de-reuniao-de-socios
description: >
  Redige edital de convocação, ata de reunião ou assembleia de sócios de
  sociedade limitada e deliberação escrita unânime, conferindo matéria,
  forma, convocação, instalação e quórum (CC arts. 1.071 a 1.080-A e 1.152),
  inclusive aprovação de contas, alteração contratual, destituição de
  administrador, exclusão de sócio por justa causa e reunião digital. Use
  quando o usuário pedir ata de reunião de sócios, ata de assembleia de LTDA,
  edital de convocação, aprovação de contas anual, deliberação de exclusão
  de sócio, ata para arquivar na Junta Comercial ou conferência de quórum.
metadata:
  area: societario
  tipo_peca: outro
  verificado_em: 2026-11-25
---
# Ata de reunião ou assembleia de sócios (LTDA)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

A ata é a prova da deliberação. Vício de convocação, de instalação ou de quórum compromete a deliberação e abre espaço para anulação e para a responsabilidade ilimitada de quem aprovou matéria contrária à lei ou ao contrato (CC art. 1.080). A skill cobre a sociedade limitada; para S.A. (assembleia geral ordinária ou extraordinária), seguir a LSA e conferir os artigos antes de redigir [VERIFICAR].

## Quando usar / quando não usar
- Usar: assembleia ou reunião anual de contas (art. 1.078); alteração contratual; designação ou destituição de administrador; aumento ou redução de capital; exclusão de sócio por justa causa (art. 1.085); incorporação, fusão, dissolução; nomeação de liquidante; deliberação escrita de todos os sócios (art. 1.072, § 3º).
- Não usar:
  - redação do contrato social ou da alteração consolidada em si: `soc-contrato-social-ltda`;
  - reunião prévia de bloco de controle: `soc-acordo-de-socios`;
  - exclusão judicial, dissolução parcial ou haveres em juízo: `soc-dissolucao-parcial-e-exclusao-de-socio`;
  - ação para anular deliberação: `civel-peticao-inicial` / `civel-contestacao`, com os fundamentos daqui.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Contrato social vigente (forma de deliberação, quóruns próprios, regência supletiva, cláusula de exclusão).
2. Quadro de sócios atualizado, com participação no capital; capital integralizado ou não.
3. Ordem do dia exata; documentos de suporte (balanço, laudo, alteração contratual proposta).
4. Número de sócios (mais de 10 exige assembleia — art. 1.072, § 1º).
5. Como foi ou será a convocação (edital publicado, ciência escrita de todos, comparecimento de todos) e datas.
6. Presentes, representados (procuração a sócio ou advogado com poderes especificados — art. 1.074, § 1º), participação a distância.
7. Votos de cada sócio por item, inclusive abstenções, impedimentos e votos divergentes.
8. Se exclusão: fatos imputados, data da ciência do acusado, defesa apresentada.

## Prazo e contagem
- Assembleia anual: nos 4 meses seguintes ao término do exercício (art. 1.078); documentos à disposição dos sócios não administradores até 30 dias antes (art. 1.078, § 1º).
- Convocação por edital: ao menos três publicações; 8 dias entre a primeira e a realização em primeira convocação; 5 dias nas posteriores (art. 1.152, § 3º). Dispensada se todos comparecerem ou se declararem por escrito cientes de local, data, hora e ordem do dia (art. 1.072, § 2º).
- Convocação por sócio: administradores retardam por mais de 60 dias nos casos previstos; titulares de mais de 1/5 do capital, se o pedido fundamentado não for atendido em 8 dias (art. 1.073).
- Arquivamento: cópia da ata no registro em 20 dias (art. 1.075, § 2º); posse do administrador designado em ato separado em 30 dias e averbação em 10 (art. 1.062).
- Recesso do dissidente de alteração contratual, fusão ou incorporação: 30 dias da reunião (art. 1.077).
- Anulação da aprovação de contas: extingue-se em 2 anos (art. 1.078, § 4º). Prazo para anular outras deliberações da limitada [VERIFICAR].
- Prazos processuais: `prazos-processuais`.

## Estrutura da peça
Edital (se houver) → ata: cabeçalho → data, hora, local ou meio digital → presença e quórum de instalação → convocação ou dispensa → mesa (presidente e secretário sócios) → ordem do dia → deliberações item a item com votos → encerramento, lavratura e assinaturas. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Instalação** da assembleia: 3/4 do capital em primeira convocação; qualquer número em segunda (art. 1.074). A reunião segue, nas omissões do contrato, as regras da assembleia (art. 1.079).
- **Quóruns de deliberação** (art. 1.076, redação da Lei 14.451/2022):
  - mais da metade do capital: designação de administrador em ato separado, destituição, remuneração, modificação do contrato social, incorporação, fusão, dissolução ou cessação da liquidação, pedido de concordata (art. 1.071, II a VI e VIII);
  - maioria dos presentes: aprovação de contas, nomeação e destituição de liquidantes e julgamento de suas contas, e demais casos (art. 1.071, I e VII);
  - especiais: administrador não sócio — 2/3 dos sócios até a integralização e mais da metade do capital depois (art. 1.061); destituição de sócio nomeado administrador no contrato — mais da metade do capital, salvo cláusula diversa (art. 1.063, § 1º); exclusão por justa causa — mais da metade do capital (art. 1.085).
  - Quórum maior fixado no contrato prevalece.
- **Impedimento**: o sócio não vota matéria que lhe diga respeito diretamente (art. 1.074, § 2º) — confirmado em caso concreto pelo STJ (REsp 1.757.560).
- **Mesa**: presidente e secretário escolhidos entre os sócios presentes (art. 1.075).
- **Exclusão**: só com cláusula contratual de justa causa, reunião ou assembleia especialmente convocada e ciência do acusado em tempo hábil para comparecer e se defender, salvo sociedade de dois sócios (art. 1.085, parágrafo único).
- **Digital**: participação e voto a distância conforme regulamento do Poder Executivo federal (art. 1.080-A) [VERIFICAR: norma do DREI vigente sobre reunião digital].
- Deliberação conforme a lei e o contrato vincula ausentes e dissidentes (art. 1.072, § 5º).

## Fundamentos verificados
- CC arts. 1.061, 1.062, 1.063, 1.071 a 1.080-A, 1.085, 1.152, § 3º.
- STJ, REsp 1.757.560 (impedimento do art. 1.074, § 2º; quórum do art. 1.061).
- STJ, REsp 2.170.665 (exclusão extrajudicial exige previsão contratual).
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
Não se aplica (peça societária). Encerrar a ata com: autorização aos administradores para arquivar e praticar os atos necessários; declaração de que a ata é cópia fiel da lavrada em livro próprio (quando houver livro); assinaturas exigidas pela Junta.

## Checklist pré-protocolo
- [ ] Forma correta (reunião x assembleia; mais de 10 sócios = assembleia)
- [ ] Convocação provada (edital com datas e veículos) ou dispensa documentada (todos presentes ou ciência escrita)
- [ ] Quórum de instalação conferido com o capital de cada presente
- [ ] Cada item com quórum próprio calculado sobre o capital total, não sobre os presentes, quando a lei exige
- [ ] Impedimentos registrados e votos impedidos não computados
- [ ] Exclusão: cláusula contratual transcrita, convocação específica, ciência do acusado e defesa registradas
- [ ] Alteração contratual aprovada anexada ou transcrita
- [ ] Prazo de 20 dias para arquivamento controlado

## Erros a evitar
- Calcular "mais da metade do capital" sobre o capital presente.
- Ata genérica ("aprovado por unanimidade") sem registrar quem votou e como — fragiliza a prova e o cômputo de impedidos.
- Exclusão aprovada em reunião sem ponto específico na pauta ou sem dar ao acusado tempo de defesa.
- Presidir ou secretariar com não sócio, contra o art. 1.075.
- Aprovar contas sem disponibilizar os documentos 30 dias antes.
- Usar quóruns revogados (3/4 para alteração contratual) por modelo antigo.

## Integração com o núcleo
`prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`, `juros-e-correcao` (se a ata fixar haveres a pagar).

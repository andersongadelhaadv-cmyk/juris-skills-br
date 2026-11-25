---
name: familia-adocao
description: >
  Redige pedido de adoção de criança ou adolescente (ECA arts. 39 a 52-D e 165 a 170) —
  unilateral, conjunta, por parente, de quem já tem a guarda (intuitu personae nas
  hipóteses do art. 50, § 13), póstuma — e de maior de 18 anos (CC art. 1.619), inclusive
  cumulada com destituição do poder familiar. Use quando o usuário pedir ação de adoção,
  adoção unilateral pelo padrasto ou madrasta, adoção do enteado, adoção por avós ou tios,
  adoção de quem já está sob guarda, adoção póstuma, adoção de maior, habilitação para
  adoção ou regularizar "adoção à brasileira".
metadata:
  area: familia-sucessoes
  tipo_peca: inicial
  verificado_em: 2026-11-25
---
# Adoção

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: adoção unilateral (cônjuge/companheiro adota o filho do outro); adoção conjunta; adoção por parente com vínculo afetivo; adoção por quem detém tutela ou guarda legal (ECA 50, § 13); adoção póstuma (ECA 42, § 6º); adoção de maior (CC 1.619); habilitação no cadastro (ECA 197-A e seguintes).
- Não usar: guarda ou convivência sem rompimento do vínculo de origem (`familia-guarda-e-convivencia`); reconhecimento de paternidade socioafetiva/multiparentalidade sem desligar o pai registral (avaliar `familia-investigacao-de-paternidade`); desconstituir paternidade registral (`familia-negatoria-de-paternidade`); adoção internacional com pretendente residente em país da Convenção de Haia de 1993 (ECA 51 a 52-D: exige Autoridades Centrais — esta skill só dá o mapa); homologação de adoção estrangeira (`intl-homologacao-sentenca-estrangeira`).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Adotante(s): idade, estado civil, união estável (prova), residência, renda, antecedentes; diferença de idade com o adotando (mínimo 16 anos).
2. Adotando: idade, certidão, com quem vive, desde quando, se está acolhido, se tem irmãos.
3. Pais biológicos: conhecidos? vivos? consentem? já destituídos do poder familiar? paradeiro?
4. Origem da convivência: como a criança chegou ao adotante (entrega direta, guarda judicial, acolhimento). Pergunta obrigatória — define se há cadastro a observar.
5. Adotante habilitado no SNA? Desde quando?
6. Pedido de troca de prenome ou só do sobrenome.
7. Adotando com 12 anos ou mais: está de acordo?

## Prazo e contagem
- Prazos do ECA contam em dias corridos, excluído o dia do começo e incluído o do vencimento, sem dobra para Fazenda e MP (ECA 152, § 2º). Não aplicar a contagem em dias úteis do CPC por reflexo.
- Estágio de convivência: máximo de 90 dias, prorrogável por igual período (ECA 46, caput e § 2º-A); pode ser dispensado se já houver tutela ou guarda legal por tempo suficiente; guarda de fato, sozinha, não dispensa (§§ 1º e 2º).
- Prazo máximo para concluir a ação de adoção: 120 dias, prorrogável uma vez (ECA 47, § 10). Destituição do poder familiar: 120 dias (ECA 163).
- Quem recebeu a guarda após entrega voluntária tem 15 dias, do fim do estágio, para propor a adoção (ECA 19-A, § 7º).
- Pais que consentiram: retratação até a audiência e arrependimento em 10 dias da sentença de extinção do poder familiar (ECA 166, § 5º).
- Contagem fora do ECA: `prazos-processuais`.

## Estrutura da peça
Endereçamento (Vara da Infância e Juventude; adoção de maior conforme organização judiciária) → qualificação com os requisitos do ECA 165 → modalidade de adoção e enquadramento (cadastro ou exceção do 50, § 13) → vínculo e reais vantagens (ECA 43) → consentimento ou destituição → estágio de convivência → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Adoção é medida excepcional e irrevogável (ECA 39, § 1º); vedada por procuração (§ 2º); prevalecem os interesses do adotando (§ 3º).
- Podem adotar maiores de 18 anos, qualquer estado civil (ECA 42); não podem os ascendentes e irmãos do adotando (§ 1º) — o STJ admitiu flexibilizar essa vedação em caso excepcional de avó (REsp 2.169.622). Conjunta: casados ou em união estável (§ 2º); divorciados e ex-companheiros nas condições do § 4º.
- Consentimento dos pais (ECA 45), dispensado se desconhecidos ou destituídos (§ 1º); adolescente maior de 12 anos consente em audiência (ECA 45, § 2º; 28, § 2º). Consentimento só vale após o nascimento e se ratificado em audiência (ECA 166, §§ 4º e 6º).
- Sem consentimento e com pais conhecidos: cumular com destituição do poder familiar (ECA 155 e seguintes; citação pessoal e resposta em 10 dias, ECA 158).
- Candidato não cadastrado só adota nas hipóteses do ECA 50, § 13 (unilateral; parente com vínculo; tutela ou guarda legal de criança maior de 3 anos ou adolescente, sem má-fé). Fora delas, o STJ tem ponderado o cadastro com o melhor interesse quando o vínculo já está formado (HC 878.386), mas isso é exceção a provar, não regra.
- Tutor ou curador só adota depois de prestar contas (ECA 44).
- Competência: Justiça da Infância e Juventude (ECA 148, III), pelo domicílio dos pais ou responsável (ECA 147).

## Fundamentos verificados
ECA 19-A, 28, 39 a 52-D, 147, 148, 152, 155, 158, 163, 165, 166, 197-A, 197-E, 199-A; CC 1.596, 1.618, 1.619. STJ: HC 878.386 (cadastro × melhor interesse); REsp 2.195.119 (adoção póstuma com vontade incontroversa); REsp 2.169.622 (adoção por avó, flexibilização); REsp 1.839.932 (adoção não se revoga por enfraquecimento de laços). Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Guarda provisória para fins de adoção (liminar), com estágio de convivência ou sua dispensa fundamentada.
- Destituição do poder familiar, se cumulada; citação pessoal dos genitores.
- Estudo psicossocial pela equipe interprofissional (ECA 46, § 4º; 28, § 1º).
- Audiência para consentimento dos pais e do adolescente.
- Procedência para constituir a adoção, com mandado de registro (cancelamento do assento original, novo registro sem observação de origem — ECA 47).
- Nome: sobrenome do adotante e, se requerido, novo prenome, com oitiva do adotando (ECA 47, §§ 5º e 6º).
- Prioridade de tramitação (ECA 152, § 1º; 47, § 9º se houver deficiência ou doença crônica); intimação do MP; segredo de justiça.

## Checklist pré-protocolo
- [ ] Modalidade identificada e enquadrada (cadastro ou exceção do ECA 50, § 13), com prova.
- [ ] Diferença de 16 anos e vedações do ECA 42, § 1º checadas.
- [ ] Documentos do ECA 165 e, se for habilitação, do ECA 197-A.
- [ ] Situação dos pais: consentimento por escrito (a ratificar em audiência) ou pedido de destituição.
- [ ] Concordância do adolescente maior de 12 anos sondada.
- [ ] Origem da convivência narrada com transparência (sem omitir entrega direta).
- [ ] Grupo de irmãos considerado (ECA 28, § 4º).
- [ ] Prazos em dias corridos (ECA 152, § 2º).

## Erros a evitar
- Tratar a adoção unilateral como simples troca de nome: há desligamento do genitor substituído, que precisa consentir ou ser destituído.
- Omitir que a criança foi entregue diretamente pela mãe: o juízo descobre no estudo e a omissão pode levar ao acolhimento.
- Pedir adoção por avós ou irmãos como se fosse permitida: a vedação é a regra; a exceção do STJ exige fundamentação concreta.
- Contar prazos do ECA em dias úteis.
- Prometer revogação futura: a adoção é irrevogável.
- Juntar consentimento dado antes do nascimento (não vale).

## Integração com o núcleo
`prazos-processuais` (prazos fora do ECA), `verificacao-de-citacoes`, `fidelidade-factual` (origem da convivência e datas), `estilo-forense`.

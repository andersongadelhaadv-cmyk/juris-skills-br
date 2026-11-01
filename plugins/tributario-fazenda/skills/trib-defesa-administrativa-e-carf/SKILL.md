---
name: trib-defesa-administrativa-e-carf
description: >
  Redige impugnação administrativa a auto de infração e recurso voluntário ao
  CARF no processo administrativo fiscal federal (Decreto 70.235/1972, com prazos
  de 20 dias úteis dados pela LC 227/2026), observando as normas gerais de
  processo administrativo fiscal do CTN (arts. 208-A a 208-J, LC 236/2026) e o
  voto de qualidade restabelecido pela Lei 14.689/2023. Use quando o usuário pedir
  impugnação de auto de infração, defesa administrativa, manifestação de
  inconformidade, recurso voluntário, recurso ao CARF, DRJ, defesa no contencioso
  administrativo tributário federal, estadual ou municipal.
metadata:
  area: tributario-fazenda
  tipo_peca: defesa-administrativa
  verificado_em: 2026-11-01
---
# Defesa administrativa tributária e recurso ao CARF

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: impugnação de auto de infração ou notificação de lançamento (1ª instância: DRJ no plano federal); recurso voluntário ao CARF; defesas equivalentes em Estados e Municípios (aplique a lei local e, onde omissa, as normas gerais do CTN arts. 208-A a 208-J).
- Recurso especial à Câmara Superior: use esta skill como base, mas trate a divergência com cuidado (ver Prazo).
- Não usar: quando o cliente já optou pela via judicial sobre o mesmo objeto (renúncia: CTN art. 208-E, p.ú.; LEF art. 38, p.ú.).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
- Auto de infração/notificação integral, termo de verificação fiscal, anexos e data da ciência (pessoal, postal, eletrônica/DTE).
- Ente tributante e lei processual aplicável (federal: Decreto 70.235; estadual/municipal: lei local).
- Documentos que provam a tese (a prova documental preclui depois da impugnação: Decreto 70.235 art. 16, §4º).
- Se a matéria está em discussão judicial (dever de informar: Decreto 70.235 art. 16, V; CTN art. 208-E).
- Valor do crédito e interesse em pagamento ou parcelamento com redução de multa (CTN art. 142, §5º).

## Prazo e contagem
- **Federal, impugnação**: 20 dias úteis da intimação (Decreto 70.235 arts. 10, V e 15, redação da LC 227/2026, com efeitos desde a publicação em 14/01/2026).
- **Federal, recurso voluntário**: 20 dias úteis da ciência da decisão, com efeito suspensivo (art. 33).
- **Recurso especial à CSRF**: o Decreto mantém 15 dias (art. 37, §2º; 10 dias úteis para CBS, §5º), enquanto o CTN art. 208-D, III fixa 20 dias úteis como garantia geral [VERIFICAR qual prevalece no CARF; na dúvida, protocole em 15 dias].
- **Embargos de declaração**: 5 dias (CTN art. 208-D, IV), com efeito interruptivo (art. 208-C, §1º).
- Suspensão de prazos de 20/12 a 20/01 (Decreto 70.235 art. 5º-A; CTN art. 208-D, §5º).
- Estados e Municípios: lei local; as garantias mínimas do CTN (20 dias úteis) devem ser adotadas em até 2 anos e se aplicam diretamente se o ente não legislar (CTN art. 211-B).
- Use `prazos-processuais`.

## Estrutura da peça
Endereçamento → qualificação → tempestividade → síntese da autuação → informação sobre ação judicial → preliminares (nulidade, decadência) → mérito ponto a ponto → multa → diligências/perícia com quesitos → pedidos. Roteiro em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Matéria não contestada expressamente torna-se incontroversa (Decreto 70.235 art. 17): impugne cada infração.
- Diligência ou perícia: motivos, quesitos e perito, sob pena de se ter por não formulado (art. 16, IV e §1º).
- Nulidades: autoridade incompetente e preterição do direito de defesa (Decreto art. 59); lançamento sem fundamentação legal e requisitos do auto (CTN arts. 208-B e 208-H). Se o mérito puder ser decidido a favor, a nulidade não é pronunciada (art. 59, §3º).
- Vinculação: o julgador administrativo deve observar súmulas e precedentes vinculantes do STF e STJ e súmulas do tribunal administrativo (CTN art. 208-G; Decreto art. 25, §13). Os órgãos de julgamento não afastam lei por inconstitucionalidade, salvo exceções do art. 26-A.
- Voto de qualidade: a Lei 14.689/2023 restabeleceu o desempate pelo presidente (representante da Fazenda) e, nesse caso, exclui as multas e cancela a representação fiscal para fins penais (Decreto art. 25, §§9º e 9º-A).
- Sem depósito ou arrolamento como condição do recurso (Súmula Vinculante 21; CTN art. 151, §2º).
- Multa: tetos do CTN art. 113-A (LC 236/2026) [VERIFICAR aplicação a fatos anteriores].
- Súmulas do CARF: cite apenas após conferir número e redação no site oficial do CARF; a base de jurisprudência usada nesta skill não as cobre.

## Fundamentos verificados
Decreto 70.235/1972 arts. 5º, 5º-A, 9º, 10, 14 a 17, 23, 25, 26-A, 33, 37, 42 e 59; CTN arts. 113-A, 142, 151, III e §2º, 208-A a 208-J e 211-B; Lei 14.689/2023; LC 227/2026; LC 236/2026; Súmula Vinculante 21. Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Reconhecimento da tempestividade e suspensão da exigibilidade (CTN art. 151, III).
- Nulidade do lançamento; subsidiariamente, cancelamento total ou parcial; subsidiariamente, redução ou exclusão da multa.
- Diligência/perícia com quesitos.
- Intimação do procurador (inclusive por DTE, CTN art. 127-A) e sustentação oral no julgamento colegiado (Decreto art. 25, §12).

## Checklist pré-protocolo
- [ ] Data da ciência confirmada e prazo em dias úteis calculado, com a suspensão de 20/12 a 20/01.
- [ ] Toda infração impugnada; nada deixado como incontroverso por omissão.
- [ ] Todas as provas documentais juntadas agora (preclusão do art. 16, §4º).
- [ ] Pedido de perícia com quesitos e perito.
- [ ] Declaração sobre ação judicial com o mesmo objeto.
- [ ] Análise de pagamento/parcelamento com redução de multa antes do prazo (CTN art. 142, §5º).
- [ ] Súmulas do CARF conferidas no site oficial antes de citar.

## Erros a evitar
- Usar o prazo antigo de 30 dias corridos (alterado pela LC 227/2026 para 20 dias úteis).
- Guardar documentos para o recurso voluntário.
- Pedir que a DRJ ou o CARF declare lei inconstitucional fora das hipóteses do art. 26-A.
- Ajuizar ação com o mesmo objeto sem avisar o cliente da renúncia ao recurso.
- Citar súmula do CARF de memória.
- Calcular multa e juros com taxa própria: use `juros-e-correcao`.

## Integração com o núcleo
- `prazos-processuais`: prazos em dias úteis e suspensão de fim de ano.
- `juros-e-correcao`: atualização de valores e simulação de pagamento com redução.
- `verificacao-de-citacoes`: todo precedente acrescentado.
- `fidelidade-factual`: confronto entre o termo de verificação e os documentos.
- `estilo-forense`: revisão final.

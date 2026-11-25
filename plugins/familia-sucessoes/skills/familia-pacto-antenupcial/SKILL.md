---
name: familia-pacto-antenupcial
description: >
  Elabora minuta de pacto antenupcial para escritura pública — escolha do regime
  (separação convencional, comunhão universal, participação final nos aquestos ou regime
  misto), cláusulas patrimoniais, afastamento da separação obrigatória do maior de 70 anos
  e registro (CC arts. 1.639, 1.640, 1.653 a 1.657; Lei 6.015/1973, arts. 167 e 244; STF
  Tema 1236). Use quando o usuário pedir pacto antenupcial, escritura de regime de bens
  antes do casamento, separação total de bens, cláusulas do pacto, pacto para maior de 70
  anos ou revisão de minuta de pacto feita pelo cartório.
metadata:
  area: familia-sucessoes
  tipo_peca: contrato
  verificado_em: 2026-11-25
---
# Pacto antenupcial

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: nubentes que querem regime diferente da comunhão parcial, ou comunhão parcial com cláusulas específicas; maior de 70 anos que pretende afastar a separação obrigatória (STF Tema 1236); revisão de minuta padrão de cartório.
- Não usar:
  - casal já casado que quer trocar de regime: ação de alteração do regime (CC 1.639 § 2º), com autorização judicial [fora desta skill; usar `civel-peticao-inicial` com os requisitos do § 2º];
  - contrato de convivência na união estável: `familia-uniao-estavel` (CC 1.725);
  - holding, doações e planejamento sucessório amplo: `soc-holding-familiar`, `sucessoes-planejamento-e-partilha-em-vida`;
  - partilha após o fim do casamento: `familia-divorcio` ou `familia-partilha-posterior-e-sobrepartilha`.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Qualificação, idade e estado civil de cada nubente (divorciado com partilha pendente? viúvo com inventário aberto? — causas suspensivas levam à separação obrigatória, CC 1.641, I).
2. Idade: algum nubente com mais de 70 anos? Algum depende de suprimento judicial para casar (CC 1.641, III)? Menor em idade núbil (CC 1.654)?
3. Patrimônio atual de cada um: imóveis (matrículas), quotas e empresas, investimentos, dívidas.
4. Objetivo: proteger empresa familiar? separar patrimônio futuro? comunicar só o imóvel residencial? regras para frutos e rendimentos?
5. Filhos de relações anteriores e expectativa sucessória (o regime repercute na herança — CC 1.829, I).
6. Domicílio conjugal e locais dos imóveis (registro e averbações — Lei 6.015, art. 244).
7. Data prevista do casamento e cartório da habilitação.

## Prazo e contagem
- O pacto deve ser feito antes do casamento; sem casamento posterior, é ineficaz (CC 1.653). Não há prazo legal fixo entre escritura e casamento [VERIFICAR: norma de serviço da corregedoria estadual sobre validade da escritura para a habilitação].
- Eficácia perante terceiros só após registro no Registro de Imóveis do domicílio conjugal (CC 1.657; Lei 6.015, arts. 167, I, 12, 178, V, e 244).
- Prazos processuais, se houver litígio posterior: `prazos-processuais`.

## Estrutura do documento
Minuta para o tabelião: qualificação → declarações (capacidade, ausência de causa suspensiva, patrimônio declarado) → regime escolhido → cláusulas patrimoniais → cláusulas de administração e despesas → cláusulas proibidas evitadas → condição de eficácia (casamento) → registro e averbações. Roteiro em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Forma: escritura pública, sob pena de nulidade (CC 1.653); opção pela comunhão parcial é reduzida a termo na habilitação, sem pacto (CC 1.640, p.ú.).
- Liberdade de estipulação antes do casamento (CC 1.639), limitada pela nulidade da cláusula que contrarie disposição absoluta de lei (CC 1.655).
- Menor: eficácia depende de aprovação do representante legal, salvo regime obrigatório de separação (CC 1.654); havendo autorização para casar, seu instrumento é transcrito na escritura (CC 1.537).
- Separação obrigatória (CC 1.641): nos casos dos incisos I e III não há escolha; no inciso II (maior de 70), o regime pode ser afastado por escritura pública (STF Tema 1236, tese vinculante). Sem o afastamento, atenção à Súmula 377 STF e, na união estável, à Súmula 655 STJ (comunicação dos aquestos com prova do esforço comum).
- Participação final nos aquestos: pode-se convencionar a livre disposição dos imóveis particulares (CC 1.656).
- Separação convencional: administração exclusiva e livre alienação (CC 1.687), dispensa de outorga para imóveis (CC 1.647, I); despesas do casal proporcionais aos rendimentos, salvo estipulação (CC 1.688).

## Fundamentos verificados
CC 426, 1.537, 1.639 a 1.641, 1.647, 1.653 a 1.657, 1.660, 1.668, 1.672, 1.687, 1.688, 1.829, I, 1.845; Lei 6.015/1973, arts. 70, 7º, 167, 178, V, e 244; STF Tema 1236; Súmula 377 STF; Súmula 655 STJ; STJ AgInt no REsp 1.969.999. Detalhe em [fundamentos](references/fundamentos.md).

## Cláusulas essenciais
- [ ] Regime escolhido, nomeado com o artigo do CC, e efeito a partir do casamento (CC 1.639 § 1º).
- [ ] Relação dos bens de cada nubente na data da escritura (prova futura de bem particular).
- [ ] Regra para frutos e rendimentos de bens particulares (na comunhão parcial, os frutos se comunicam — CC 1.660, V; se a intenção for outra, dizer expressamente, observado o CC 1.655).
- [ ] Quotas e empresa: valorização, lucros reinvestidos, aportes do outro cônjuge.
- [ ] Imóvel residencial: comunica ou não; regra para financiamento pago por ambos.
- [ ] Despesas do lar e contribuição proporcional (CC 1.688).
- [ ] Livre disposição de imóveis particulares, se participação final (CC 1.656).
- [ ] Doações entre os nubentes (com ou sem incomunicabilidade — CC 1.668, IV).
- [ ] Declaração de ciência dos efeitos sucessórios do regime.
- [ ] Autorização para registro e averbação nas matrículas.

## Checklist pré-assinatura
- [ ] Nenhum nubente em causa suspensiva (CC 1.641, I) sem providência prévia (partilha do casamento anterior, inventário).
- [ ] Maior de 70: cláusula expressa de afastamento do CC 1.641, II (Tema 1236), com relato de que a escolha foi livre e informada.
- [ ] Nenhuma cláusula que disponha sobre herança de pessoa viva (CC 426) ou que retire direitos de terceiros.
- [ ] Nenhuma cláusula sobre guarda, alimentos de filhos ou deveres conjugais pessoais travestida de cláusula patrimonial.
- [ ] Domicílio conjugal e matrículas listados para registro e averbações.
- [ ] Minuta lida e explicada a cada nubente separadamente (prova de vontade livre).

## Erros a evitar
- Assinar pacto "padrão" de separação total sem perceber que, no regime de separação **convencional**, o cônjuge concorre com descendentes na herança (CC 1.829, I, só exclui a separação obrigatória) e é herdeiro necessário (CC 1.845).
- Cláusula de renúncia à herança ou ao direito concorrencial do cônjuge: risco de nulidade pelo CC 426 e 1.655; tema sem jurisprudência confirmada no JuriBase [VERIFICAR: posição atual do STJ].
- Deixar de registrar no Livro 3 e de averbar nas matrículas: o pacto não vale contra terceiros (CC 1.657; Lei 6.015, art. 244).
- Supor que a separação convencional impede toda partilha: sociedade de fato entre cônjuges pode ser provada caso a caso (STJ, AgInt no REsp 1.969.999).
- Para o maior de 70 sem pacto, presumir separação total: a Súmula 377 STF e a Súmula 655 STJ podem levar à comunicação dos aquestos.

## Integração com o núcleo
`verificacao-de-citacoes`, `fidelidade-factual` (bens, matrículas, datas), `estilo-forense`; `juros-e-correcao` só se houver cláusula de compensação financeira com atualização (nunca fixar índice aqui sem remeter ao núcleo).

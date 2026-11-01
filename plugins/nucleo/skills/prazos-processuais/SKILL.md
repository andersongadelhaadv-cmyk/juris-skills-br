---
name: prazos-processuais
description: >
  Calcula e confere prazos processuais no cível (CPC arts. 219 a 232, dias
  úteis), trabalhista (CLT art. 775), penal (CPP art. 798, dias corridos),
  juizados (Lei 9.099, art. 12-A; Leis 10.259 e 12.153) e contra a Fazenda,
  com termo inicial por modo de intimação (DJEN e Domicílio Judicial
  Eletrônico, Res. CNJ 455/2022; CPC arts. 224 e 231; Lei 11.419, arts. 4º e
  5º), prazo em dobro e recesso. Use quando o usuário pedir prazo, vencimento,
  "até quando posso", tempestividade, contagem, dias úteis, prazo em dobro,
  recesso forense, intimação pelo DJEN, pelo DJe, pelo Domicílio ou pelo
  portal, citação eletrônica, ou tabela de prazos.
metadata:
  area: nucleo
  tipo_peca: outro
  verificado_em: 2026-11-01
---
# Prazos processuais

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

O resultado desta skill é uma data provável de vencimento com a memória da
contagem. Ela não substitui a conferência no sistema do tribunal, nos atos de
suspensão do tribunal e no calendário de feriados locais.

## Quando usar / quando não usar
- Usar: antes de redigir qualquer peça com prazo; ao alegar intempestividade da
  parte contrária; ao conferir certidão de decurso.
- Não usar para prescrição ou decadência de direito material (são prazos de
  direito material: contagem do CC art. 132, sem a regra dos dias úteis do CPC 219,
  que vale só para prazos processuais, conforme seu parágrafo único).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Ramo e rito: cível comum, juizado cível, JEF, juizado da Fazenda, trabalhista, penal.
2. Ato a praticar (contestação, apelação, ED etc.).
3. Modo e data da comunicação: DJEN ou DJe (data de disponibilização), Domicílio
   Judicial Eletrônico ou portal (data do envio e da consulta), mandado, correio,
   audiência, carga, citação eletrônica (data da confirmação).
4. Quem pratica: particular, Fazenda, MP, Defensoria, núcleo de prática jurídica;
   litisconsortes com escritórios distintos; autos físicos ou eletrônicos.
5. Comarca/seção e tribunal (para feriados locais e portarias de suspensão).

## Prazo e contagem (regras de base)
- **Cível (CPC)**: só dias úteis (art. 219); exclui o dia do começo e inclui o do
  vencimento (art. 224); suspensão de 20/12 a 20/01 (art. 220).
- **DJEN (Diário de Justiça Eletrônico Nacional)**: é o meio de intimação do advogado
  quando a lei não exige intimação pessoal; outra comunicação simultânea (aba do
  sistema, e-mail) é só informativa (Res. CNJ 455/2022, art. 11, §§2º e 3º, com a
  redação da Res. 569/2024). Publicação = 1º dia útil seguinte à disponibilização;
  a contagem começa no 1º dia útil seguinte à publicação (CPC 224, §§2º e 3º; Lei
  11.419, art. 4º, §§3º e 4º). O DJe do tribunal segue a mesma regra.
- **Domicílio Judicial Eletrônico**: só para citação eletrônica e para comunicações
  que exigem intimação pessoal (Res. CNJ 455/2022, art. 18). Intimação: feita no dia
  da consulta (em dia não útil, no 1º dia útil seguinte); sem consulta em 10 dias
  corridos do envio, considera-se feita no fim desse prazo (Res. 455, art. 20, caput,
  §§1º e 4º; Lei 11.419, art. 5º, §§1º a 3º); o prazo começa no dia útil seguinte
  (CPC 231, V). Citação confirmada: prazo de resposta a partir do 5º dia útil seguinte
  à confirmação (CPC 231, IX; Res. 455, art. 20, §3º-B). Detalhe em
  [fundamentos](references/fundamentos.md), seção 1-A.
- **Portal próprio do tribunal**: mesma regra da consulta e dos 10 dias corridos
  (Lei 11.419, art. 5º, §3º).
- **Trabalhista**: dias úteis (CLT 775); suspensão de 20/12 a 20/01 (CLT 775-A).
- **Penal**: dias corridos, contínuos e peremptórios (CPP 798); vencimento em dia
  sem expediente prorroga para o dia útil seguinte (§3º); contam-se da intimação, não da
  juntada do mandado (Súm. 710/STF); suspensão de 20/12 a 20/01, salvo réu preso,
  Maria da Penha e medidas urgentes (CPP 798-A). Recursos penais nos tribunais
  superiores também correm em dias corridos (STJ, AgRg no AREsp 2.552.378).
- **Juizados (Lei 9.099)**: dias úteis para todo ato, inclusive recurso (art. 12-A);
  aplica-se ao JEF e ao juizado da Fazenda por remissão (Lei 10.259, art. 1º;
  Lei 12.153, art. 27).
- Protocolo eletrônico até 24h do último dia, pelo horário do juízo (CPC 213; Lei
  11.419, art. 10, §1º). Indisponibilidade do sistema prorroga (CPC 224, §1º).

## Estrutura da peça
Quando a tempestividade for discutível, a peça traz tópico "Da tempestividade"
com a memória de contagem. Modelo e passo a passo em
[estrutura](references/estrutura.md).

## Requisitos e preliminares
- Prazo em dobro: MP (CPC 180), Fazenda e suas autarquias e fundações (CPC 183),
  Defensoria e núcleos de prática jurídica conveniados (CPC 186, §3º), todos a
  partir da intimação pessoal. Não há dobra quando a lei fixa prazo próprio
  (arts. 180, §2º; 183, §2º; 186, §4º).
- Litisconsortes com escritórios distintos: dobro só em autos físicos (CPC 229 e §2º);
  nunca nos embargos à execução (CPC 915, §3º).
- Juizados federais e da Fazenda: não há prazo diferenciado para o ente público
  (Lei 10.259, art. 9º; Lei 12.153, art. 7º).
- Justiça do Trabalho, entes públicos: dobro para recurso (DL 779/1969, art. 1º, III).
- Feriado local: comprovar no ato de interpor o recurso (CPC 1.003, §6º, redação da
  Lei 14.939/2024; o tribunal pode mandar corrigir).

## Fundamentos verificados (tabela resumida)
| Ato | Prazo | Base |
|---|---|---|
| Contestação (comum) | 15 dias úteis | CPC 335 |
| Réplica | 15 dias úteis | CPC 350 e 351 |
| Apelação, agravo de instrumento, REsp, RE, RO, agravos internos e respostas | 15 dias úteis | CPC 1.003, §5º; 1.070 |
| Embargos de declaração (cível) | 5 dias úteis | CPC 1.023 |
| Pagamento voluntário / impugnação ao cumprimento | 15 + 15 dias úteis | CPC 523 e 525 |
| Embargos à execução | 15 dias úteis | CPC 915 |
| Fazenda: impugnação ao cumprimento / embargos à execução | 30 dias | CPC 535; 910 |
| Embargos à execução fiscal / impugnação da Fazenda | 30 dias (úteis × corridos: ver nota) | LEF 16 e 17 |
| Juizado: recurso inominado e resposta | 10 dias úteis | Lei 9.099, 42 e 12-A |
| Juizado: embargos de declaração | 5 dias úteis | Lei 9.099, 49 |
| Trabalhista: RO, RR, AP, AI, embargos no TST e contrarrazões | 8 dias úteis | CLT 895, 896, 897, 894; Lei 5.584, art. 6º |
| Trabalhista: ED | 5 dias úteis | CLT 897-A |
| Trabalhista: embargos à execução / impugnação | 5 dias (Fazenda: 30) | CLT 884; Lei 9.494, art. 1º-B |
| Penal: apelação | 5 dias corridos (razões: 8) | CPP 593 e 600 |
| Penal: RESE | 5 dias corridos (razões: 2) | CPP 586 e 588 |
| Penal: ED | 2 dias corridos | CPP 382 e 619 |
| Penal: resposta à acusação | 10 dias corridos | CPP 396 e 406 |
| Penal: agravo em execução | 5 dias corridos | LEP 197; Súm. 700/STF |
| Habeas corpus / revisão criminal | sem prazo | CPP 647 e 622 |
| Mandado de segurança | 120 dias (decadencial) | Lei 12.016, art. 23 |

Nota LEF: a lei fixa 30 dias e manda aplicar o CPC subsidiariamente (LEF 1º); a
contagem em dias úteis (CPC 219) não foi conferida em fonte oficial [VERIFICAR]. Por
cautela, conte em dias corridos e não deixe para o último dia.

Tabela completa e notas em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Restituição de prazo por justa causa (CPC 223, §§1º e 2º) ou por falecimento ou
  força maior (CPC 1.004), com prova do impedimento.
- Juntada de comprovante de feriado local ou de indisponibilidade do sistema.

## Checklist pré-protocolo
- [ ] Ramo e regra de contagem certos (úteis × corridos).
- [ ] Termo inicial conforme o modo de intimação (CPC 231; DJEN/DJe; Domicílio; portal).
- [ ] Intimação pessoal (Fazenda, MP, Defensoria) conferida no Domicílio, não no DJEN.
- [ ] Dobra aplicável ou expressamente afastada.
- [ ] Recesso de 20/12 a 20/01 e exceções penais considerados.
- [ ] Feriados nacionais, locais e portarias do tribunal conferidos; comprovante anexado.
- [ ] Vencimento anotado com margem; protocolo antes do último dia sempre que possível.

## Erros a evitar
- Contar em dias úteis o prazo penal, inclusive REsp e agravo em matéria penal.
- Aplicar dobra do CPC 229 em processo eletrônico.
- Contar a partir da disponibilização no DJEN ou no DJe, e não da publicação.
- Esperar a intimação pela aba do sistema quando já houve publicação no DJEN: o prazo
  corre da publicação.
- Tratar a citação eletrônica como intimação: o prazo de resposta começa no 5º dia útil
  após a confirmação, não no dia seguinte.
- Esquecer que o ED interrompe o prazo (CPC 1.026; CLT 897-A, §3º; Lei 9.099, arts. 50
  e 83, §2º) e o recurso seguinte corre por inteiro.
- Tratar o prazo de 8 dias trabalhista como 15 por analogia ao CPC.

## Integração com o núcleo
- `fidelidade-factual`: data e modo da intimação vêm da certidão ou da aba de expedientes.
- `verificacao-de-citacoes`: antes de citar precedente sobre tempestividade.
- `juros-e-correcao`: prazos de impugnação ao cálculo dependem do regime de atualização.
- `estilo-forense`: tópico de tempestividade curto e objetivo.

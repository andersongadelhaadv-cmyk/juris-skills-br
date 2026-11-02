---
name: familia-uniao-estavel
description: >
  Redige ação de reconhecimento e dissolução de união estável (inclusive post mortem), com
  partilha, alimentos e efeitos sucessórios (CC arts. 1.723 a 1.727; STF Temas 809, 498 e
  529). Use quando o usuário pedir reconhecimento de união estável, dissolução de união
  estável, união estável post mortem, partilha entre companheiros, meação de companheiro,
  direito de herança de companheiro, contrato de convivência.
metadata:
  area: familia-sucessoes
  tipo_peca: inicial
  verificado_em: 2026-11-01
---
# União estável: reconhecimento e dissolução

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: declarar a existência e o período da união; dissolver; partilhar; pedir alimentos entre companheiros; reconhecer post mortem para meação, herança e benefícios.
- Não usar: casamento (use `familia-divorcio`); dissolução consensual sem incapazes, que pode ir a cartório (CPC 733; Res. CNJ 35, art. 46-A) — esta skill traz a minuta em [estrutura](references/estrutura.md).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Data de início e de fim (ou do óbito); como a convivência era pública, contínua e duradoura com objetivo de família.
2. Provas: escritura ou contrato de convivência, conta conjunta, dependência em plano/IR/INSS, comprovantes de mesmo endereço, fotos, testemunhas, filhos comuns.
3. Impedimentos: algum dos companheiros era casado? Se sim, estava separado de fato? Desde quando?
4. Regime: contrato escrito? Algum dos companheiros tinha mais de 70 anos no início?
5. Bens e dívidas com data e forma de aquisição.
6. Filhos; necessidade de alimentos ou guarda.
7. Post mortem: herdeiros do falecido (serão os réus), inventário aberto?

## Prazo e contagem
- Reconhecimento: sem prazo. Petição de herança prescreve (Súmula 149 STF) e o prazo conta da abertura da sucessão, sem suspensão ou interrupção pela ação de reconhecimento do vínculo (STJ Tema 1200). Duração do prazo: não conferida em fonte oficial [VERIFICAR: prazo aplicável à petição de herança].
- Prazos processuais pelo rito das ações de família; contagem via `prazos-processuais`.

## Estrutura da peça
Endereçamento → qualificação → requisitos da união (fato a fato) → período → regime → partilha → alimentos/guarda → efeitos sucessórios (post mortem) → tutela → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Requisitos materiais: convivência pública, contínua, duradoura e com objetivo de constituir família (CC 1.723); coabitação não é requisito legal, mas é prova forte.
- Impedimentos do CC 1.521 impedem a união, salvo casado separado de fato ou judicialmente (CC 1.723 §1º); relação simultânea a casamento/união é concubinato (CC 1.727) e não gera união paralela (STF Tema 529).
- Uniões homoafetivas: entidade familiar com o mesmo regime da união estável (STF, ADI 4277 e ADPF 132, interpretação conforme do CC 1.723); a publicidade pode ser relativizada quando presentes os demais requisitos (STJ, REsp 2.203.770).
- Competência e rito: CPC 53, I, e 693 e seguintes. Post mortem: réus são os herdeiros (ou o espólio, se ainda não partilhado — conferir orientação do tribunal local).

## Fundamentos verificados
CF 226 §3º; CC 1.723 a 1.727, 1.725 (comunhão parcial supletiva), 1.641, II; STF Temas 809/498 (sucessão igual à do cônjuge, art. 1.829), 529 (vedação de uniões paralelas) e 1236 (maior de 70 anos); STF ADI 4277/ADPF 132; STJ Tema 1200; Súmula 655 STJ; Súmula 149 STF. Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- [ ] Declaração da união estável com termo inicial e final.
- [ ] Dissolução e partilha dos bens adquiridos onerosamente no período (comunhão parcial, salvo contrato escrito).
- [ ] Alimentos entre companheiros e/ou aos filhos; guarda e convivência.
- [ ] Post mortem: reconhecimento da qualidade de herdeiro/meeiro e reserva de quinhão no inventário; direito real de habitação, se cabível (CC 1.831 aplicado por equiparação — conferir).
- [ ] Tutelas: arrolamento/indisponibilidade de bens; reserva de bens no inventário (CPC 628 §2º).
- [ ] Averbação/registro, quando houver.

## Checklist pré-protocolo
- [ ] Linha do tempo com datas de início, eventos e fim.
- [ ] Ao menos três tipos diferentes de prova.
- [ ] Verificação de casamento anterior (certidão atualizada) e da data da separação de fato.
- [ ] Contrato de convivência lido: regime, data de assinatura, eventual retroatividade.
- [ ] Idade de cada companheiro no início (separação obrigatória x Tema 1236).

## Erros a evitar
- Aplicar o CC 1.790 (concorrência sucessória diferenciada): foi declarado inconstitucional (Temas 809 e 498).
- Pedir reconhecimento de união paralela a casamento ou a outra união (Tema 529).
- Tratar namoro qualificado como união sem demonstrar o objetivo atual de constituir família.
- Esquecer de incluir todos os herdeiros no polo passivo do post mortem.
- Partilhar bens adquiridos antes do início da união ou por herança/doação.
- Dar efeito retroativo ao regime escolhido em contrato ou escritura posterior ao início da convivência: o STJ atribui eficácia ex nunc (REsp 2.246.314).

## Integração com o núcleo
`prazos-processuais`, `juros-e-correcao` (reposições e alimentos), `verificacao-de-citacoes`, `fidelidade-factual` (datas e provas), `estilo-forense`.

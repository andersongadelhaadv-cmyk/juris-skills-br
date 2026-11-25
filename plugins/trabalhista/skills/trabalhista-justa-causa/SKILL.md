---
name: trabalhista-justa-causa
description: >
  Orienta a aplicação da dispensa por justa causa pelo empregador (CLT art. 482:
  enquadramento na alínea, apuração, imediatidade, proporcionalidade, comunicação)
  e a defesa do empregado que busca a reversão, com ônus da prova do empregador
  (CLT art. 818, II; Súmula 212 do TST) e as Súmulas 32 e 73 do TST. Use quando o
  usuário pedir para aplicar justa causa, redigir carta de dispensa por falta
  grave, avaliar se a falta justifica a dispensa, reverter justa causa, anular
  dispensa por improbidade, desídia, abandono de emprego ou insubordinação.
metadata:
  area: trabalhista
  tipo_peca: outro
  verificado_em: 2026-11-25
---
# Justa causa — aplicação e defesa (CLT art. 482)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar (empresa): decidir se a falta comporta justa causa, montar o dossiê, redigir a comunicação de dispensa e preparar a defesa futura.
- Usar (empregado): pedir a reversão da justa causa em dispensa imotivada, com as verbas correspondentes. A peça é a reclamação (`trabalhista-reclamacao`) com o tópico desta skill; na defesa da empresa em juízo, `trabalhista-contestacao`.
- Não usar: falta do empregador (`trabalhista-rescisao-indireta`); empregado estável que exige inquérito para apuração de falta grave [VERIFICAR: hipóteses legais e procedimento do inquérito antes de orientar]; servidor público estatutário (plugin `administrativo-licitacoes`).
- Advertências e suspensões, sem dispensa, como política interna: `trabalhista-compliance`.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. O fato: o que ocorreu, quando, onde, quem viu, qual prova existe (vídeo, documento, sistema, testemunha, boletim).
2. Quando a empresa soube do fato e quando reagiu (decisivo para a imediatidade).
3. Histórico disciplinar: advertências e suspensões anteriores, datas e motivos, assinadas ou testemunhadas.
4. Função, tempo de casa e eventual condição especial (deficiência, gestante, estabilidade, afastamento previdenciário).
5. Norma interna ou contratual violada e prova de ciência do empregado.
6. Tratamento dado a outros empregados em situação igual (isonomia).
7. Para o empregado: como foi comunicado, o que assinou, se recebeu verbas e quais.

## Prazo e contagem
- **Imediatidade**: a punição deve seguir o conhecimento do fato, admitido o tempo razoável de apuração. Demora sem justificativa é lida como perdão tácito.
- Abandono após benefício previdenciário: presume-se se o empregado não retornar em 30 dias da cessação nem justificar (Súmula 32 do TST).
- Prescrição para reverter: cinco anos, até dois anos após a extinção (CF art. 7º, XXIX).
- Prazos processuais: `prazos-processuais`.

## Estrutura da peça
Empresa: dossiê (fato, prova, enquadramento, histórico, imediatidade, proporcionalidade) → comunicação de dispensa com a alínea → defesa em juízo. Empregado: fato controvertido → ausência de prova robusta → vícios (imediatidade, proporcionalidade, bis in idem, isonomia) → reversão e verbas. Roteiro em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Tipicidade**: enquadrar o fato em alínea do art. 482 (a improbidade; b incontinência de conduta ou mau procedimento; c negociação habitual concorrente ou prejudicial; d condenação criminal transitada sem suspensão da pena; e desídia; f embriaguez habitual ou em serviço; g violação de segredo; h indisciplina ou insubordinação; i abandono; j e k ato lesivo da honra ou ofensa física, no serviço ou contra o empregador e superiores, salvo legítima defesa; l jogos de azar constantes; m perda dolosa de habilitação profissional).
- **Gravidade e proporcionalidade**: a falta precisa romper a confiança. Faltas leves pedem gradação (advertência, suspensão); falta grave admite dispensa direta. O TST desafetou, em 2026, o tema repetitivo sobre a necessidade de gradação, por entender que a análise é casuística — não há tese vinculante; argumentar com os fatos.
- **Nexo e atualidade**: a punição se refere ao fato apontado e não pode punir duas vezes o mesmo fato (sem dupla punição).
- **Ônus da prova**: do empregador, que alega fato impeditivo (CLT art. 818, II); negados o serviço e a dispensa, o término do contrato é ônus do empregador (Súmula 212 do TST). A jurisprudência exige prova robusta.
- **Justa causa no aviso prévio**: retira as verbas indenizatórias, salvo abandono (Súmula 73 do TST).

## Fundamentos verificados
CLT arts. 482 (a a m), 484 e 818; CF art. 7º, XXIX; Súmulas 32, 73 e 212 do TST; desafetação do tema de gradação de penalidades pelo Pleno do TST (2026); acórdão do TST sobre exigência de prova robusta. Detalhes em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- **Empregado**: reversão da justa causa em dispensa sem justa causa; aviso prévio, 13º e férias proporcionais com 1/3, indenização do FGTS, guias de saque e seguro-desemprego (ou indenização substitutiva), retificação da CTPS; dano moral apenas se a imputação foi abusiva ou divulgada (não decorre automaticamente da reversão).
- **Pedido subsidiário**: culpa recíproca (art. 484 — indenização reduzida à metade), quando cabível.
- **Empresa (defesa)**: manutenção da justa causa; subsidiariamente, culpa recíproca.
- Valores liquidados (art. 840 § 1º); correção e juros pelo núcleo `juros-e-correcao`.

## Checklist pré-protocolo
- [ ] Alínea do art. 482 indicada e coerente com o fato descrito.
- [ ] Data do fato, data do conhecimento e data da dispensa registradas.
- [ ] Prova do fato anexada ou testemunhas arroladas (empresa).
- [ ] Histórico disciplinar documentado (gradação, quando a falta não é grave).
- [ ] Isonomia checada (outros casos iguais tratados igual).
- [ ] Condição especial do empregado considerada (estabilidade, deficiência, afastamento).
- [ ] Verbas devidas mesmo na justa causa pagas (saldo de salário, férias vencidas com 1/3).

## Erros a evitar
- Capitular em alínea genérica ("mau procedimento") um fato que se encaixa em alínea específica, ou trocar a alínea na contestação.
- Aplicar a justa causa semanas depois sem apuração formal que explique a demora.
- Punir duas vezes o mesmo fato (advertência e depois dispensa pelo mesmo episódio).
- Basear a dispensa em prova que a empresa não poderá exibir em juízo.
- Para o empregado: pedir dano moral automático pela reversão, sem fato ofensivo autônomo.

## Integração com o núcleo
`juros-e-correcao`, `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

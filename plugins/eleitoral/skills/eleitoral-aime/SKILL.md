---
name: eleitoral-aime
description: >
  Redige ação de impugnação de mandato eletivo (AIME) com base no art. 14,
  §§ 10 e 11, da Constituição, ajuizada em até 15 dias da diplomação, em
  segredo de justiça, por abuso de poder econômico, corrupção ou fraude. Use
  quando o usuário pedir AIME, impugnação de mandato, cassação de mandato de
  eleito já diplomado, fraude à cota de gênero, compra de votos descoberta
  após a eleição ou abuso econômico que não foi objeto de AIJE.
metadata:
  area: eleitoral
  tipo_peca: inicial
  verificado_em: 2026-11-25
---
# Ação de impugnação de mandato eletivo (AIME)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: impugnar o mandato de eleito diplomado por (a) abuso do poder econômico, (b) corrupção ou (c) fraude, com prova, até 15 dias da diplomação (CF, art. 14, § 10).
- Não usar: abuso de poder político puro, uso indevido dos meios de comunicação ou condutas dos arts. 30-A, 41-A e 73 dentro dos seus prazos — `eleitoral-aije`; inelegibilidade superveniente ou falta de condição de elegibilidade após o registro — recurso contra expedição de diploma (CE, art. 262), ver `eleitoral-recurso-eleitoral`; defesa do impugnado — `eleitoral-defesa-abuso-de-poder`; crime eleitoral — `penal-*`.

## Entradas mínimas (perguntar o que faltar; nunca supor fatos)
1. Data da diplomação (marco dos 15 dias) e cargo do impugnado; titular e vice/suplentes envolvidos.
2. Qual dos três fundamentos: abuso econômico, corrupção ou fraude — com o fato concreto de cada um.
3. Provas pré-constituídas (a Constituição exige que a ação seja instruída com provas): documentos, mídias, ata notarial, prova emprestada de outros processos, testemunhas.
4. Se já houve AIJE ou representação sobre o mesmo fato e em que fase está.
5. Legitimidade do cliente (partido, coligação, candidato, MP).

## Prazo e contagem
- 15 dias contados da diplomação (CF, art. 14, § 10). Natureza decadencial e forma de contagem (inclusive em feriado e recesso) firmadas pela jurisprudência do TSE [VERIFICAR: contagem do prazo da AIME na jurisprudência do TSE — JuriBase sem cobertura do TSE]. Controle em `prazos-processuais`.
- Rito: a jurisprudência aplica o procedimento dos arts. 3º e seguintes da LC 64/1990 [VERIFICAR: rito da AIME fixado pelo TSE]. Nesse rito: contestação em 7 dias (art. 4º), alegações em 5 dias (art. 6º).

## Estrutura da peça
Endereçamento (segredo de justiça) → legitimidade e tempestividade → fatos → enquadramento (abuso econômico / corrupção / fraude) → gravidade e reflexo na legitimidade do mandato → provas → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Tramita em segredo de justiça; o autor responde por ação temerária ou de manifesta má-fé (CF, art. 14, § 11) — e a arguição temerária de abuso é crime (LC 64/1990, art. 25).
- Prova é requisito de admissibilidade (CF, art. 14, § 10: "instruída com provas").
- Legitimidade ativa: a Constituição não define; a prática segue os legitimados do art. 3º da LC 64/1990 [VERIFICAR: legitimidade ativa da AIME na jurisprudência do TSE].
- Polo passivo: o diplomado; na majoritária, titular e vice [VERIFICAR: Súmula 38 do TSE].
- Competência: órgão que diplomou (juiz eleitoral, TRE ou TSE) [VERIFICAR: regra de competência da AIME].
- Fraude: hipótese recorrente é a fraude à cota de gênero nas candidaturas proporcionais [VERIFICAR: Súmula 73 do TSE e requisitos — JuriBase sem cobertura do TSE].

## Fundamentos verificados
- CF, art. 14, §§ 9º, 10 e 11.
- LC 64/1990, arts. 3º a 8º (rito aplicado por empréstimo), 25.
- STF, Tema 986 (RE 1.096.029): novas eleições automáticas se cassado o eleito na majoritária (CE, art. 224, § 3º).
- Recurso de decisão que cassa mandato tem efeito suspensivo (CE, art. 257, § 2º).
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Tramitação em segredo de justiça (CF, art. 14, § 11).
- Citação para contestar; produção de prova testemunhal e documental; requisição de prova emprestada.
- Procedência para desconstituir o mandato do impugnado (e do vice, se majoritária).
- Na majoritária, novas eleições (Tema 986/STF); na proporcional, efeito sobre os votos e o quociente [VERIFICAR: destino dos votos em AIME proporcional — resolução e jurisprudência do TSE].
- Intimação do MP Eleitoral.

## Checklist pré-protocolo
- [ ] Data da diplomação documentada e 15 dias contados
- [ ] Fundamento enquadrado só em abuso econômico, corrupção ou fraude
- [ ] Provas anexadas na inicial (não só prometidas)
- [ ] Pedido de segredo de justiça
- [ ] Titular e vice no polo passivo (majoritária)
- [ ] Risco de ação temerária avaliado (art. 14, § 11; LC 64/1990, art. 25)

## Erros a evitar
- Usar a AIME para abuso de poder político sem conteúdo econômico (fora dos três fundamentos).
- Ajuizar sem prova pré-constituída e confiar na instrução.
- Divulgar a ação: segredo de justiça.
- Perder o prazo por contar dias úteis ou esperar o fim do recesso sem conferir a regra.
- Ignorar AIJE já julgada sobre o mesmo fato.

## Integração com o núcleo
`prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

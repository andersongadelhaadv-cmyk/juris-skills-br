---
name: mil-revisao-criminal
description: >
  Redige revisão criminal de condenação transitada em julgado na Justiça Militar
  (CPPM arts. 550 a 562), com as hipóteses do art. 551 (sentença contrária à
  evidência dos autos, prova falsa, prova nova), competência do STM ou do
  TJ/TJM, legitimidade e efeitos da absolvição sobre os direitos perdidos. Use
  quando o usuário pedir revisão criminal militar, rescisão de condenação do
  Conselho de Justiça, prova nova após condenação por crime militar,
  restabelecimento de direitos do militar condenado ou redução de pena por erro.
metadata:
  area: militar
  tipo_peca: inicial
  verificado_em: 2026-11-25
---
# Revisão criminal militar

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: processo findo (condenação transitada) na JMU ou na JME com erro quanto aos fatos, sua apreciação, avaliação ou enquadramento (CPPM art. 550), nas hipóteses do art. 551.
- Não usar: processo ainda com recurso cabível (apelação ou RESE — `mil-recurso-em-sentido-estrito`); prisão ilegal atual (`mil-habeas-corpus`, que cabe também após a sentença nas hipóteses do art. 468); condenação na Justiça comum (`penal-revisao-criminal`); reintegração ao serviço como pedido principal (`mil-reintegracao-e-reforma`, que pode usar a absolvição obtida aqui).

## Entradas mínimas (perguntar o que faltar; nunca supor fatos)
1. Sentença e acórdão condenatórios e certidão de trânsito em julgado (art. 555, § 1º).
2. A hipótese do art. 551 que se pretende provar e a prova correspondente (documento, perícia, depoimento falso comprovado, prova nova).
3. Pedidos revisionais anteriores e seus fundamentos (reiteração só com prova ou fundamento novo — art. 552, parágrafo único).
4. Situação do condenado: cumprindo pena, solto, falecido (legitimidade do art. 553).
5. Efeitos extrapenais sofridos (exclusão, perda de posto ou graduação, proventos).

## Prazo e contagem
- Sem prazo: a revisão pode ser requerida a qualquer tempo (art. 552), inclusive após a morte do condenado, por cônjuge, ascendente, descendente ou irmão (art. 553).
- Prova nova produzida antes da revisão (justificação, perícia) segue o rito próprio; prazos processuais: `prazos-processuais`.

## Estrutura da peça
Endereçamento ao presidente do tribunal → legitimidade e trânsito → hipótese do art. 551 → demonstração do erro → efeitos (art. 558) → pedidos. Roteiro em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Competência: STM, nos processos findos na JMU (CPPM art. 554; Lei 8.457/1992, art. 6º, I, e). Na JME, o segundo grau é o TJ ou o TJM (CF art. 125, § 3º); conferir o regimento local.
- Instrução: certidão de trânsito em julgado e peças que comprovem os fatos alegados; o relator pode apensar os autos originais (art. 555, §§ 1º e 2º).
- Relator, de preferência, ministro que não atuou antes como relator ou revisor (art. 555).
- Hipóteses taxativas do art. 551: (a) sentença contrária à evidência dos autos; (b) fundada em depoimentos, exames ou documentos comprovadamente falsos; (c) prova nova que invalide a condenação ou autorize diminuir a pena.
- Mero reexame da prova já valorada tende a ser rejeitado (TJTO, Revisão Criminal 0012059-41.2023.8.27.2700).
- Não há recurso contra a decisão da revisão (art. 562). Cabimento de recursos constitucionais não conferido [VERIFICAR].

## Fundamentos verificados
- CPPM arts. 468, 550 a 562; CF art. 125, § 3º; Lei 8.457/1992, art. 6º, I, e.
- TJTO, Revisão Criminal 0012059-41.2023.8.27.2700 (Pleno, 15/02/2024): revisão cabível nas hipóteses do art. 551 do CPPM; alteração de pena só com erro técnico ou injustiça evidente.
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Procedência para absolver, alterar a classificação do crime, modificar a pena ou anular o processo (art. 558).
- Restabelecimento de todos os direitos perdidos em razão da condenação (art. 559), com comunicação à autoridade militar.
- Apensamento dos autos originais (art. 555, § 2º).
- Vista ao procurador-geral (art. 556).
- Se falecido o condenado: nomeação de curador (art. 561).

## Checklist pré-protocolo
- [ ] Certidão de trânsito em julgado juntada
- [ ] Hipótese do art. 551 indicada e provada documentalmente
- [ ] Prova nova é efetivamente nova (não apenas releitura da antiga)
- [ ] Revisão anterior verificada (art. 552, parágrafo único)
- [ ] Pedido de restabelecimento de direitos (art. 559) incluído
- [ ] Tribunal competente conferido no regimento

## Erros a evitar
- Usar a revisão como segunda apelação.
- Esquecer o pedido do art. 559: sem ele, os efeitos funcionais ficam para outra ação.
- Temer agravamento: a pena nunca pode ser agravada na revisão (art. 558, parágrafo único) — use isso para tranquilizar o cliente, não para dispensar prova.

## Integração com o núcleo
`prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

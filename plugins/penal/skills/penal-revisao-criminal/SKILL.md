---
name: penal-revisao-criminal
description: >
  Redige revisão criminal contra condenação transitada em julgado (CPP arts. 621
  a 631), nas hipóteses de contrariedade à lei ou à evidência dos autos, prova
  falsa e prova nova, com justificação criminal prévia e pedido de indenização
  (art. 630). Use quando o usuário pedir revisão criminal, ação revisional,
  desconstituir condenação definitiva, prova nova de inocência, retratação da
  vítima após o trânsito ou erro judiciário.
metadata:
  area: penal
  tipo_peca: outro
  verificado_em: 2026-11-01
---
# Revisão criminal

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: condenação (ou absolvição imprópria) transitada em julgado, nas hipóteses taxativas do art. 621: I — sentença contrária ao texto expresso da lei ou à evidência dos autos; II — fundada em depoimentos, exames ou documentos comprovadamente falsos; III — novas provas de inocência ou de circunstância que diminua a pena.
- Não usar: como terceira instância para reavaliar a prova já valorada (o STJ rejeita a revisão como "nova apelação"); contra absolvição própria (não existe revisão pro societate); se ainda cabe recurso.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Certidão de trânsito em julgado e cópia integral do processo.
2. Hipótese do art. 621 pretendida e o elemento que a sustenta.
3. Prova nova: o que é, quando surgiu, por que não pôde ser produzida antes; se testemunhal, justificação criminal já feita ou a fazer.
4. Situação da pena (em cumprimento, extinta, réu falecido — legitimidade do art. 623).
5. Revisões anteriores (reiteração só com novas provas — 622 p.ú.).

## Prazo e contagem
- Sem prazo: a qualquer tempo, antes ou depois da extinção da pena (CPP 622).
- O condenado não precisa recolher-se à prisão para requerer (Súmula 393 STF).
- Recursos internos (agravo regimental, embargos): prazos contínuos (CPP 798). Use `prazos-processuais`.

## Estrutura da peça
Resumo (detalhe em [estrutura](references/estrutura.md)): endereçamento ao tribunal competente (CPP 624); legitimidade; cabimento (inciso do 621); fatos e trânsito; fundamentos; pedido de efeitos (absolvição, nova classificação, redução de pena, anulação); indenização (630); documentos.

## Requisitos e preliminares
- Competência (CPP 624): o tribunal que proferiu a condenação ou, sendo de 1º grau, o tribunal de 2º grau competente; STF e STJ para as próprias condenações (regimentos).
- Relator que não tenha atuado no processo (625).
- Instrução com certidão de trânsito e peças necessárias (625 §1º); se insuficiente, indeferimento liminar (625 §3º).
- Prova nova testemunhal ou declaração da vítima: deve passar por justificação criminal com contraditório; declaração em ata notarial não basta (STJ, REsp 2.170.160).
- Revaloração jurídica de fatos incontroversos é admitida (STJ, AgRg na RvCr 6.818); reexame subjetivo da prova não (STJ, REsp 2.244.764).
- Proibida a reformatio in pejus (626 p.ú.).

## Fundamentos verificados
Resumo (detalhe em [fundamentos](references/fundamentos.md)): CPP 621 a 631; Súmula 393 STF; precedentes do STJ sobre limites da revisão e prova nova.

## Pedidos e requerimentos
- Procedência para absolver, alterar a classificação, reduzir a pena ou anular o processo (626).
- Liminar para suspender a execução, quando houver prova robusta [VERIFICAR: admissibilidade de tutela de urgência na revisão no regimento do tribunal].
- Reconhecimento do direito à indenização (630), salvo hipóteses do §2º.
- Restabelecimento de direitos perdidos (627).

## Checklist pré-protocolo
- [ ] Trânsito em julgado certificado.
- [ ] Inciso do art. 621 escolhido e demonstrado com documentos.
- [ ] Prova nova colhida em justificação judicial com contraditório.
- [ ] Explicado por que a prova é nova (não disponível ou não produzida antes).
- [ ] Tribunal competente conferido (624).
- [ ] Revisões anteriores mapeadas (622 p.ú.).
- [ ] Precedentes conferidos em `verificacao-de-citacoes`.

## Erros a evitar
- Repetir a apelação com a mesma prova, pedindo nova valoração.
- Juntar declaração escrita ou ata notarial da testemunha sem justificação criminal.
- Esquecer o pedido de indenização (630) quando cabível.
- Ajuizar sem a certidão de trânsito.

## Integração com o núcleo
- `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.
- `juros-e-correcao`: a indenização do art. 630 é liquidada no cível — remeter ao núcleo para atualização; não fixar índice aqui.

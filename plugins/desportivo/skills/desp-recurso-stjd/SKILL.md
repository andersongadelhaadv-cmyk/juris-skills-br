---
name: desp-recurso-stjd
description: >
  Redige recurso voluntário contra decisão de Comissão Disciplinar ou de
  Tribunal de Justiça Desportiva, dirigido ao TJD Pleno ou ao Superior
  Tribunal de Justiça Desportiva (STJD), com pedido de efeito suspensivo, nos
  termos do art. 53 da Lei 9.615/1998 e dos arts. 136 a 150 do CBJD. Use quando
  o usuário pedir recurso ao STJD, recurso voluntário desportivo, efeito
  suspensivo de suspensão por partidas, reforma de punição aplicada pelo TJD ou
  redução de pena imposta pela Justiça Desportiva.
metadata:
  area: desportivo
  tipo_peca: recurso
  verificado_em: 2026-11-25
---
# Recurso voluntário ao STJD

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: decisão condenatória (ou absolutória, se cliente for a parte contrária) de Comissão Disciplinar ou de TJD em processo regido pelo CBJD.
- Não usar: defesa em primeira instância (`desp-defesa-disciplinar`); decisão do Tribunal Pleno do STJD, que é irrecorrível internamente salvo regra internacional da modalidade (CBJD, art. 136, § 1º) — ver `desp-recurso-tas-cas` ou `desp-mandado-seguranca-suspensao-atleta`; matéria antidopagem (`desp-defesa-antidoping`).

## Entradas mínimas (perguntar o que faltar; nunca supor fatos)
1. Decisão recorrida: data e hora da proclamação do resultado, ata, e se a ata registrou que o acórdão será redigido depois.
2. Pena aplicada (partidas, prazo, multa) e o que já foi cumprido.
3. Órgão de origem e órgão competente para o recurso (TJD Pleno ou STJD, conforme o regimento e a competição).
4. Tabela de emolumentos e forma de pagamento.
5. Íntegra dos autos: denúncia, defesa, provas, vídeo, ata da sessão.
6. Próximas partidas do atleta ou do clube (urgência do efeito suspensivo).

## Prazo e contagem
- Razões em três dias, contados da proclamação do resultado (CBJD, art. 138, I); se a ata registrar acórdão a ser redigido, o prazo corre do dia seguinte à intimação da juntada do acórdão (art. 138, parágrafo único).
- Prazos contínuos, com prorrogação para o primeiro dia útil (CBJD, art. 43).
- Urgência: interposição por meio eletrônico, com remessa do original em três dias (CBJD, art. 139).
- Contrarrazões: três dias comuns (art. 138-C).
- Texto do CBJD usado aqui: consolidado de 2009 — conferir a redação vigente e o regimento.

## Estrutura da peça
Petição de interposição ao órgão de origem (com indicação do órgão competente e do comprovante de emolumentos) → razões dirigidas à instância superior → tempestividade e preparo → pedido de efeito suspensivo → preliminares → mérito → dosimetria → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Protocolo perante o órgão que proferiu a decisão; indicar o órgão competente; juntar no protocolo a prova do pagamento dos emolumentos, sob pena de deserção (CBJD, art. 138, I a III).
- Irrecorríveis: decisões do Pleno do STJD (art. 136, § 1º) e decisões de TJD que só impuseram multa até R$ 1.000,00 (art. 136, § 2º).
- Proibição de reformatio in pejus no recurso da defesa (art. 140); pena pode ser reduzida mesmo em recurso só da Procuradoria (art. 140-A).
- Efeito devolutivo amplo (art. 142); instância superior pode reduzir pena em parte não recorrida (art. 142, parágrafo único).
- Não se admite prova nova em instância recursal, salvo reexibição a critério do relator (art. 150).

## Efeito suspensivo
- Regra: efeito apenas devolutivo (CBJD, art. 147).
- Efeito suspensivo legal quando a pena exceder duas partidas consecutivas ou quinze dias (Lei 9.615/1998, art. 53, § 4º; CBJD, art. 147-B, I), a pedido do punido, e só no que exceder esse limite (art. 147-B, § 1º); multa tem a exigibilidade suspensa até o trânsito (art. 147-B, II e § 2º).
- Efeito suspensivo pelo relator: verossimilhança e risco de dano irreparável, vedado se houver grave perigo de irreversibilidade (art. 147-A); decisão irrecorrível, mas revogável (art. 147-A, § 2º).

## Fundamentos verificados
- Lei 9.615/1998, arts. 52 e 53, §§ 3º e 4º.
- CBJD (consolidado de 2009): arts. 43, 136 a 142, 146 a 150.
- CF, art. 217, §§ 1º e 2º.
Detalhe em [fundamentos](references/fundamentos.md). Precedentes do STJD não estão na base do JuriBase [VERIFICAR: conferir no repositório oficial do tribunal antes de citar].

## Pedidos e requerimentos
- Recebimento com efeito suspensivo (legal e/ou pelo relator), com urgência antes da próxima partida.
- Acolhimento das preliminares; anulação da decisão.
- Reforma para absolver ou desclassificar.
- Subsidiariamente, redução da pena e compensação da suspensão cumprida.
- Intimação para sustentação oral na sessão.

## Checklist pré-protocolo
- [ ] Hora da proclamação conferida na ata e prazo de três dias contado
- [ ] Acórdão a ser redigido? Prazo recontado do art. 138, parágrafo único
- [ ] Emolumentos pagos e comprovante juntado no protocolo
- [ ] Órgão competente indicado
- [ ] Pedido de efeito suspensivo destacado na primeira página
- [ ] Nenhuma prova nova anexada (art. 150)
- [ ] Redação vigente do CBJD conferida

## Erros a evitar
- Recorrer sem o comprovante de emolumentos: deserção.
- Contar o prazo da publicação, e não da proclamação do resultado.
- Pedir efeito suspensivo integral quando a lei só suspende o que excede duas partidas ou quinze dias.
- Juntar documento novo no recurso.
- Recorrer de decisão do Pleno do STJD dentro da Justiça Desportiva.

## Integração com o núcleo
`prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

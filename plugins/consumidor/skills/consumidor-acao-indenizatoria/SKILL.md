---
name: consumidor-acao-indenizatoria
description: >
  Redige petição inicial de ação indenizatória em relação de consumo (fato do
  produto ou do serviço), com responsabilidade objetiva dos arts. 12 a 14 do CDC,
  inversão do ônus da prova (art. 6º, VIII), prescrição quinquenal (art. 27) e
  critérios de arbitramento do dano moral. Use quando o usuário pedir ação de
  danos morais e materiais contra fornecedor, indenização por falha na prestação
  de serviço, acidente de consumo, defeito do produto, "processar a empresa" ou
  inicial no Juizado Especial por dano ao consumidor.
metadata:
  area: consumidor
  tipo_peca: inicial
  verificado_em: 2026-11-01
---
# Ação indenizatória de consumo (fato do produto ou do serviço)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: dano à saúde, segurança, patrimônio ou personalidade causado por defeito do produto (art. 12) ou do serviço (art. 14), inclusive vítima equiparada (art. 17).
- Não usar como peça principal: produto/serviço que apenas não funciona, sem dano além do próprio bem (vício: `consumidor-vicio-do-produto-ou-servico`); inscrição em cadastro (`consumidor-negativacao-indevida`); voo (`consumidor-transporte-aereo`); negativa de plano (`consumidor-plano-de-saude`); cobrança paga a maior (`consumidor-repeticao-em-dobro`).
- Profissional liberal: responsabilidade subjetiva (art. 14, § 4º) — a tese muda; exigir prova de culpa.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Qualificação completa das partes (CPC 319, II) e CNPJ do fornecedor; há outros fornecedores da cadeia?
2. Data do fato e data em que o consumidor soube do dano e de quem o causou (termo inicial do art. 27).
3. Narrativa cronológica, protocolos de atendimento, reclamações (SAC, Procon, plataforma pública), respostas da empresa.
4. Provas disponíveis: notas, contratos, fotos, laudos, prints com data, testemunhas.
5. Danos materiais com valores comprovados (emergentes e lucros cessantes) e repercussões concretas do dano moral.
6. Valor pretendido; escolha entre Juizado (Lei 9.099/1995) e Justiça Comum; interesse em audiência de conciliação.

## Prazo e contagem
- Prescrição: 5 anos da ciência do dano e da autoria (CDC art. 27). Confirmar termo inicial com o usuário.
- Não confundir com decadência do art. 26 (vício). Se o pedido for só reexecução/troca/abatimento, a skill é outra.
- Prazos processuais posteriores: dias úteis (CPC 219) — usar `prazos-processuais`.

## Estrutura da peça
Endereçamento (foro do domicílio do autor, CDC art. 101, I) → qualificação → síntese → fatos → relação de consumo → responsabilidade objetiva e defeito → nexo e danos → inversão do ônus → tutela de urgência (se houver) → pedidos → provas → valor da causa → audiência. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Demonstrar que autor é consumidor (art. 2º, ou equiparado art. 17/29) e réu fornecedor (art. 3º).
- Legitimidade passiva: fabricante/produtor/importador (art. 12); comerciante só nas hipóteses do art. 13; no serviço, todos os da cadeia respondem solidariamente (arts. 7º p.ú., 25 § 1º, 34).
- Juizado: limite de valor e vedação de perícia complexa — avaliar antes de escolher o rito.
- Valor da causa: soma dos pedidos, incluído o dano moral pretendido (CPC 292, V e VI).

## Fundamentos verificados
- CDC arts. 6º, VI e VIII; 12; 14; 17; 25; 27; 101, I. CPC arts. 300, 373 § 1º.
- Dano moral: STJ aplica o método bifásico (valor básico pelo grupo de precedentes + ajuste pelas circunstâncias) — AgInt no REsp 1.798.479 e REsp 2.069.520.
- Súmula 37/STJ: dano material e moral cumuláveis.
- Fortuito interno de banco: Súmula 479/STJ.
Detalhe e modo de uso em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Inversão do ônus da prova (art. 6º, VIII), com indicação dos fatos sobre os quais deve recair.
- Condenação em danos materiais (valor certo, com documentos) e morais (valor sugerido e fundamentado).
- Correção monetária e juros: indicar índices e termos iniciais pelo núcleo `juros-e-correcao` — nunca escrever taxa fixa.
- Custas e honorários (CPC 85); gratuidade se cabível; produção de provas especificadas.

## Checklist pré-protocolo
- [ ] Termo inicial da prescrição (art. 27) conferido e inferior a 5 anos
- [ ] Defeito descrito (o que faltou de segurança) e distinguido de mero vício
- [ ] Todos os fornecedores da cadeia avaliados para o polo passivo
- [ ] Cada dano material ligado a um documento
- [ ] Dano moral com fatos concretos (não só "transtornos")
- [ ] Pedido de inversão fundamentado em verossimilhança ou hipossuficiência
- [ ] Valor da causa = soma dos pedidos
- [ ] Juros/correção remetidos ao núcleo
- [ ] Precedentes acrescentados passaram por `verificacao-de-citacoes`

## Erros a evitar
- Pedir dano moral "in re ipsa" sem verificar se a hipótese admite presunção (atraso de voo e fraude bancária sem peculiaridades, por exemplo, exigem prova).
- Usar o prazo de 90 dias do art. 26 para pretensão indenizatória (o prazo é o do art. 27).
- Pedir inversão do ônus de forma genérica e não pedir provas próprias.
- Incluir comerciante como réu principal por defeito de produto fora do art. 13.
- Escrever taxa de juros na peça sem o núcleo.

## Integração com o núcleo
`juros-e-correcao` (todo pedido condenatório), `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

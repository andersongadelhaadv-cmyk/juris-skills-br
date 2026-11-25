---
name: trabalhista-notificacao-extrajudicial
description: >
  Redige notificação extrajudicial em relação de emprego, de qualquer dos lados:
  convocação para retorno ao trabalho (abandono, Súmula 32 do TST), cobrança de
  verbas rescisórias e documentos (CLT art. 477, § 6º), comunicação de falta
  grave do empregador (art. 483) ou contranotificação. Alerta que a notificação
  não interrompe a prescrição (CLT art. 11, § 3º). Use quando o usuário pedir
  notificação trabalhista, carta de convocação de empregado faltoso, notificar
  a empresa por verbas não pagas ou responder notificação de empregado.
metadata:
  area: trabalhista
  tipo_peca: notificacao
  verificado_em: 2026-11-25
---
# Notificação extrajudicial trabalhista

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar (empregador): convocar empregado ausente a retornar ou justificar faltas, inclusive após alta previdenciária; formalizar advertência ou ciência de fato apurado; responder cobrança de ex-empregado.
- Usar (empregado): cobrar verbas rescisórias, guias e documentos; comunicar descumprimento contratual antes de decidir pela rescisão indireta; pedir cópia de documentos (ponto, contracheques).
- Não usar: ajuizar a rescisão indireta (`trabalhista-rescisao-indireta`); acordo para homologação judicial (`trabalhista-acordo-extrajudicial`); notificação em contrato civil ou PJ (`contratos-notificacao-de-descumprimento`); relação de consumo (`consumidor-notificacao-extrajudicial`).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Quem notifica e quem é notificado (qualificação, endereço atual, e-mail e telefone conhecidos).
2. Dados do contrato: admissão, função, situação atual (ativo, afastado, dispensado) e data da dispensa, se houver.
3. Fato que motiva a notificação, com datas (última presença, data da alta do INSS, data do desligamento, parcela não paga).
4. O que se exige, em que prazo, e a consequência anunciada.
5. Meio de envio disponível (cartório, AR com conteúdo declarado, e-mail com confirmação, aplicativo) e como se provará o recebimento.

## Prazo e contagem
- **A notificação não interrompe a prescrição**: na CLT, a interrupção só ocorre pelo ajuizamento de reclamação trabalhista (art. 11, § 3º). Conferir a prescrição bienal e quinquenal (art. 11, caput) antes de gastar tempo com notificação.
- Verbas rescisórias e documentos: até 10 dias contados do término do contrato (art. 477, § 6º).
- Abandono de emprego: presunção quando o trabalhador não retorna em 30 dias após a cessação do benefício previdenciário nem justifica (Súmula 32 do TST). Fora dessa hipótese, o prazo de ausência relevante não está fixado em lei [VERIFICAR: critério jurisprudencial para ausência injustificada sem benefício].
- Prazos processuais posteriores: `prazos-processuais`.

## Estrutura da peça
Identificação das partes → contrato → fatos com datas → fundamento legal → exigência objetiva com prazo → consequência → canal de resposta → assinatura. Modelos por hipótese em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Prova do recebimento**: o valor da notificação está em provar que chegou ao endereço correto. Preferir cartório ou meio com conteúdo e entrega comprovados; guardar o comprovante.
- **Tom**: informativo e sem ameaça desproporcional. Notificação agressiva ao empregado pode ser usada como prova de assédio ou pressão.
- **Abandono**: a convocação documenta o elemento de intenção de não voltar; a justa causa por abandono está no art. 482, "i". Não anunciar justa causa antes de esgotado o prazo concedido.
- **Rescisão indireta**: o art. 483 lista as faltas do empregador; nas hipóteses das alíneas "d" e "g", o empregado pode pleitear a rescisão permanecendo ou não no serviço (§ 3º). A notificação ajuda a provar a ciência da empresa, mas não substitui a ação.
- **Sem dado sensível desnecessário**: não expor diagnóstico, CID ou fatos íntimos além do indispensável.

## Fundamentos verificados
CLT arts. 11 (caput e § 3º), 477 (caput e § 6º), 482, "i", e 483 (caput, "d", "g" e § 3º); Súmula 32 do TST. Detalhe em [fundamentos](references/fundamentos.md).

## Cláusulas essenciais
- Identificação completa do notificante e do notificado e do contrato.
- Narrativa curta dos fatos, com datas.
- Exigência única e verificável (comparecer em data e local; pagar e entregar documentos; justificar ausência).
- Prazo claro, contado do recebimento.
- Consequência lícita e proporcional (medidas legais cabíveis; ajuizamento de ação).
- Canal de resposta e pessoa de contato.

## Checklist pré-protocolo
- [ ] Prescrição conferida — a notificação não a interrompe
- [ ] Endereço atualizado e meio de envio com prova de entrega
- [ ] Datas conferidas com documentos (alta do INSS, TRCT, último ponto)
- [ ] Exigência objetiva e prazo explícitos
- [ ] Sem ameaça, sem expressão ofensiva, sem dado sensível
- [ ] Nenhum valor com juros ou correção calculado aqui: `juros-e-correcao`
- [ ] Cópia e comprovante arquivados para instruir eventual ação

## Erros a evitar
- Confiar na notificação para "segurar" a prescrição (art. 11, § 3º).
- Aplicar justa causa por abandono sem convocação provada ou antes de 30 dias da cessação do benefício (Súmula 32).
- Enviar só por aplicativo de mensagens, sem prova de conteúdo e leitura.
- Anunciar consequência que a lei não autoriza (desconto, retenção de documentos).
- Empregado: notificar rescisão indireta e deixar de comparecer sem avaliar o § 3º do art. 483.

## Integração com o núcleo
`prazos-processuais`, `juros-e-correcao`, `fidelidade-factual`, `estilo-forense`, `verificacao-de-citacoes`.

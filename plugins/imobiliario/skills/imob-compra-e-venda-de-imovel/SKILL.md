---
name: imob-compra-e-venda-de-imovel
description: >
  Redige e revisa promessa (compromisso) de compra e venda e contrato de compra
  e venda de imóvel, com due diligence de certidões, forma exigida (escritura
  pública do art. 108 do CC), direito real do promitente comprador (arts. 1.417
  e 1.418 do CC) e cláusulas de preço, arras, posse e resolução. Use quando o
  usuário pedir minuta de promessa de compra e venda, contrato de venda de casa,
  apartamento ou terreno, revisão de compromisso enviado pela outra parte,
  cláusula de arras ou sinal, checklist de documentos para escritura ou
  orientação para levar a promessa a registro.
metadata:
  area: imobiliario
  tipo_peca: contrato
  verificado_em: 2026-11-25
---
# Compra e venda de imóvel (promessa e contrato definitivo)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: (a) promessa de compra e venda entre particulares ou com loteador/incorporador; (b) minuta-base para a escritura definitiva; (c) revisão de compromisso recebido; (d) cessão de direitos de promessa.
- Não usar: desfazimento de promessa já assinada (`imob-distrato-imobiliario`); financiamento bancário do saldo (`imob-revisao-de-financiamento-sfh`); análise isolada da matrícula (`imob-analise-de-matricula-e-due-diligence`); opinião sobre viabilidade do negócio (`imob-parecer-juridico-imobiliario`); venda de bens móveis ou de estabelecimento (`contratos-compra-e-venda-empresarial`); locação (`imob-locacao-residencial` ou `contratos-locacao-comercial`); estruturação da incorporação (`imob-incorporacao-imobiliaria`); bem de inventário (`sucessoes-inventario-judicial` / `sucessoes-inventario-extrajudicial`).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Matrícula atualizada (número, cartório) e descrição do imóvel exatamente como na matrícula.
2. Qualificação completa das partes, estado civil e regime de bens (outorga do cônjuge), pessoa jurídica com atos societários e poderes.
3. Preço, forma de pagamento (sinal, parcelas, financiamento, FGTS, permuta), índice de correção pretendido.
4. Situação de posse: imóvel ocupado? Por quem? Data de entrega.
5. Ônus e pendências conhecidos: hipoteca, alienação fiduciária, penhora, ação, débitos de IPTU e condomínio.
6. Se há loteador ou incorporador (regime da Lei 4.591/1964 ou da Lei 6.766/1979) e se a venda é a consumidor.
7. Quem paga ITBI, escritura e registro (o padrão legal pode ser alterado no contrato).

## Prazo e contagem
- Não há prazo processual nesta peça. Defina no contrato prazos para entrega de certidões, outorga da escritura e imissão na posse, em dias corridos ou úteis, sem ambiguidade.
- Prazos de eventual ação (adjudicação compulsória, resolução): `prazos-processuais`.

## Estrutura do documento
Quadro-resumo → partes → objeto (descrição da matrícula) → origem e situação do imóvel → preço e pagamento → arras → posse e riscos → obrigações de certidões e escritura → tributos e despesas → inadimplemento e resolução → irretratabilidade ou arrependimento → cessão → registro → foro. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e cuidados de forma
- Escritura pública: essencial à validade de negócio sobre direito real imobiliário acima de 30 salários mínimos, salvo lei em contrário (CC, art. 108). A promessa pode ser por instrumento particular; a venda definitiva, em regra, não.
- Direito real do promitente comprador: promessa sem cláusula de arrependimento, registrada no Registro de Imóveis (CC, art. 1.417). Com ele, pode exigir a escritura e, recusada, pedir a adjudicação (CC, art. 1.418).
- Adjudicação compulsória não depende do registro da promessa (Súmula 239/STJ); o registro dá oponibilidade a terceiros.
- Propriedade só se transfere com o registro do título (CC, art. 1.245); até lá o alienante continua dono perante terceiros (§ 1º).
- Documentos para a escritura: ITBI, certidões fiscais e certidões de propriedade e de ônus reais (Lei 7.433/1985, art. 1º, § 2º). Para a extensão da due diligence, ver `imob-analise-de-matricula-e-due-diligence`.

## Fundamentos verificados
- CC, arts. 108, 413, 417 a 420, 474, 475, 481, 490, 1.225 (VII), 1.227, 1.245, 1.417, 1.418.
- Lei 7.433/1985, art. 1º, § 2º; Lei 13.097/2015, art. 54.
- Lei 4.591/1964, art. 35-A (quadro-resumo em venda de unidade de incorporação).
- Súmula 239/STJ (adjudicação sem registro); Súmula 84/STJ (embargos de terceiro com promessa não registrada); Súmula 308/STJ (hipoteca da construtora ineficaz perante adquirentes), aplicada também fora do SFH (REsp 1.995.732, 3ª Turma, 2026).
- Dívidas condominiais na promessa: Tema 886/STJ em revisão no Tema 1.349 [VERIFICAR: situação do julgamento].
Detalhe em [fundamentos](references/fundamentos.md).

## Cláusulas essenciais
- Descrição do imóvel idêntica à matrícula; declaração de inexistência de ônus, com exceções listadas.
- Preço certo, cronograma, índice de correção e encargos de mora: taxa e índice pelo núcleo `juros-e-correcao`, nunca percentual inventado.
- Arras: dizer se são confirmatórias (CC, arts. 417 a 419) ou penitenciais, com direito de arrependimento (art. 420). Arras penitenciais impedem o direito real do art. 1.417.
- Cláusula penal proporcional; lembrar a redução equitativa do art. 413.
- Cláusula resolutiva expressa (art. 474), com notificação prévia e prazo para purgar a mora.
- Obrigação do vendedor de entregar certidões em data certa e de quitar débitos anteriores à posse.
- Repartição de despesas: na falta de cláusula, escritura e registro com o comprador e tradição com o vendedor (art. 490).
- Irretratabilidade e autorização para registro da promessa.
- Venda a consumidor por incorporador: quadro-resumo do art. 35-A da Lei 4.591/1964 e regras de desfazimento (`imob-distrato-imobiliario`).

## Checklist pré-assinatura
- [ ] Matrícula com no máximo 30 dias, conferida ato por ato
- [ ] Vendedor é o titular registral (ou cadeia de cessões documentada)
- [ ] Outorga conjugal ou prova de dispensa (regime de bens)
- [ ] Certidões da Lei 7.433/1985 e pesquisa complementar decidida com o cliente
- [ ] Ônus existentes com plano de baixa (quitação, liberação de hipoteca ou de alienação fiduciária)
- [ ] Débitos de IPTU e condomínio quitados ou assumidos expressamente
- [ ] Arras qualificadas (confirmatórias ou penitenciais)
- [ ] Data e condição da entrega da posse
- [ ] Encargos de mora remetidos ao núcleo `juros-e-correcao`
- [ ] Previsão de registro da promessa

## Erros a evitar
- Descrever o imóvel pela inscrição do IPTU e não pela matrícula.
- Prever arrependimento por descuido e perder o direito real à aquisição.
- Pagar todo o preço por instrumento particular sem prazo e sanção para a escritura.
- Ignorar alienação fiduciária ou hipoteca do vendedor sem cláusula de liberação simultânea.
- Supor que certidão negativa de ações protege tudo: a lei de concentração tem limites (ver `imob-analise-de-matricula-e-due-diligence`).
- Fixar multa ou juros sem passar pelo núcleo.

## Integração com o núcleo
`juros-e-correcao`, `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

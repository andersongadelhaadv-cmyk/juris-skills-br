---
name: desp-defesa-disciplinar
description: >
  Prepara a defesa de atleta, treinador, dirigente, árbitro ou clube denunciado
  pela Procuradoria perante a Comissão Disciplinar ou o Tribunal de Justiça
  Desportiva (TJD/STJD), com base no art. 217 da Constituição, nos arts. 49 a
  55 da Lei 9.615/1998 e no CBJD. Use quando o usuário pedir defesa em processo
  disciplinar desportivo, defesa contra denúncia por expulsão, agressão,
  ofensa, conduta antidesportiva, invasão de campo, suspensão preventiva ou
  sustentação oral em sessão de julgamento da Justiça Desportiva.
metadata:
  area: desportivo
  tipo_peca: contestacao
  verificado_em: 2026-11-25
---
# Defesa disciplinar na Justiça Desportiva

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: denúncia da Procuradoria (ou pedido de suspensão preventiva) em processo disciplinar regido pelo CBJD, em primeira instância (Comissão Disciplinar do TJD ou do STJD, conforme a competição).
- Não usar: recurso contra decisão já proferida (`desp-recurso-stjd`); violação de regra antidopagem, que corre na Justiça Desportiva Antidopagem (`desp-defesa-antidoping`); ação no Judiciário após esgotar a via desportiva (`desp-mandado-seguranca-suspensao-atleta`); vínculo trabalhista ou rescisão do contrato do atleta (`trabalhista-*`); arbitragem internacional (`desp-recurso-tas-cas`).

## Entradas mínimas (perguntar o que faltar; nunca supor fatos)
1. Denúncia completa: fatos narrados, qualificação do denunciado e dispositivos do CBJD imputados.
2. Súmula da partida, relatório do árbitro e do delegado, e eventuais aditamentos.
3. Vídeo da jogada (íntegra e ângulos disponíveis), fotos, áudio, notícias.
4. Competição, entidade organizadora e órgão competente (TJD estadual ou STJD).
5. Data da citação/intimação, data e hora da sessão, regimento interno do tribunal e tabela de emolumentos.
6. Antecedentes do denunciado (punições anteriores, reincidência) e suspensão automática já cumprida.
7. Houve suspensão preventiva? Desde quando?
8. Testemunhas disponíveis e se comparecem à sessão.

## Prazo e contagem
- Prazos do CBJD: correm da intimação ou citação, excluindo o dia do começo e incluindo o do vencimento; são contínuos (não param em sábado, domingo e feriado), prorrogando-se para o primeiro dia útil se o início ou o fim cair em dia sem expediente (CBJD, art. 43, texto consolidado de 2009).
- Sem prazo fixado, o prazo da parte é de três dias (CBJD, art. 42, § 2º).
- A Justiça Desportiva tem até sessenta dias, contados da instauração, para decisão final (CF, art. 217, § 2º).
- Suspensão preventiva limitada a trinta dias e compensada na punição (CBJD, art. 35, § 1º).
- Conferir no regimento do tribunal se há prazo próprio para defesa escrita; prazos judiciais posteriores: `prazos-processuais`.

## Estrutura da peça
Endereçamento ao órgão → qualificação e procuração → síntese da denúncia → preliminares (nulidades, competência, inépcia, prescrição) → mérito (fato, autoria, tipicidade, prova de vídeo) → subsidiário (desclassificação, atenuantes, pena mínima, compensação da suspensão cumprida) → requerimento de provas e sustentação oral → pedidos. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Denúncia deve conter descrição detalhada dos fatos, qualificação do infrator e dispositivo infringido (CBJD, art. 79); dispositivo errado não anula, mas permite pedir adiamento quando corrigido na sessão (art. 79, parágrafo único).
- Nulidade deve ser alegada na primeira oportunidade (CBJD, art. 53) — levantar já na defesa.
- Competência: conferir se o caso é da Comissão Disciplinar ou do Pleno e se o tribunal é o da competição.
- Penas disciplinares não se aplicam a menores de quatorze anos, e penas pecuniárias não se aplicam a atletas não profissionais (Lei 9.615/1998, art. 50, §§ 2º e 3º).
- Transação disciplinar: verificar se a infração admite proposta da Procuradoria (CBJD, art. 80-A) antes da sessão.

## Fundamentos verificados
- CF, art. 217, §§ 1º e 2º (esgotamento da via desportiva; sessenta dias).
- Lei 9.615/1998, arts. 49, 50, 52 e 53 (Justiça Desportiva autônoma; Comissões Disciplinares; ampla defesa e contraditório no procedimento sumário).
- CBJD (texto consolidado pela Resolução CNE nº 29/2009): arts. 35, 42, 43, 53, 79, 80-A, 123 a 125.
Detalhe em [fundamentos](references/fundamentos.md). Jurisprudência judicial sobre o tema não foi localizada no JuriBase [VERIFICAR: buscar precedente específico antes de citar].

## Pedidos e requerimentos
- Acolhimento das preliminares e arquivamento.
- Absolvição por inexistência do fato, ausência de autoria ou atipicidade.
- Subsidiariamente: desclassificação para infração mais branda, pena no mínimo, conversão em advertência quando cabível, e compensação da suspensão preventiva/automática.
- Produção de prova de vídeo na sessão, oitiva de testemunhas e depoimento pessoal (CBJD, art. 124).
- Sustentação oral (CBJD, art. 125) e intimação do advogado para a sessão.

## Checklist pré-protocolo
- [ ] Denúncia lida contra a súmula: cada fato imputado tem suporte no documento?
- [ ] Vídeo integral obtido e minutagem indicada na peça
- [ ] Redação vigente do CBJD e do regimento do tribunal conferida (o texto usado aqui é o consolidado de 2009)
- [ ] Preliminares de nulidade todas arguidas agora
- [ ] Suspensão cumprida (automática ou preventiva) documentada para compensação
- [ ] Emolumentos recolhidos, se exigidos
- [ ] Testemunhas avisadas da data e da hora

## Erros a evitar
- Deixar nulidade para o recurso: precluiu (CBJD, art. 53).
- Contestar só a narrativa da súmula sem enfrentar a presunção que o regimento lhe dá; a prova de vídeo é o caminho.
- Esquecer pedir compensação da suspensão preventiva.
- Ir ao Judiciário antes de esgotar a via desportiva em matéria de disciplina e competição (CF, art. 217, § 1º).
- Citar artigo do CBJD sem conferir a redação vigente.

## Integração com o núcleo
`prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

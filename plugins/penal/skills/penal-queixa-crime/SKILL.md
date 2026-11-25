---
name: penal-queixa-crime
description: >
  Redige queixa-crime em ação penal privada (CPP arts. 30, 41 e 44; CP art.
  100) — calúnia, difamação, injúria, dano simples e outros crimes de ação
  privada — com procuração de poderes especiais, controle da decadência de 6
  meses (CPP art. 38; CP art. 103) e do prazo de 12 meses na violência
  doméstica contra a mulher (Lei 15.438/2026). Use quando o usuário pedir
  queixa-crime, ação penal privada, processar criminalmente por ofensa, ou
  quiser saber se ainda dá tempo de oferecer queixa.
metadata:
  area: penal
  tipo_peca: inicial
  verificado_em: 2026-11-25
---
# Queixa-crime

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: crime de ação penal exclusivamente privada (a lei diz "somente se procede mediante queixa"), como calúnia, difamação e injúria simples (CP 145) e outros tipos com essa cláusula; queixa subsidiária quando o MP perde o prazo da denúncia em crime de ação pública [VERIFICAR: CPP art. 29 não conferido nesta skill]; crime contra a honra de servidor em razão da função (legitimidade concorrente: Súmula 714/STF).
- Não usar: crime de ação pública incondicionada ou condicionada à representação (o ofendido representa; quem denuncia é o MP); injúria do art. 140 §3º e ofensa a servidor optando pela representação (CP 145, parágrafo único); defesa do querelado (`penal-resposta-a-acusacao`); indenização civil pela ofensa (`digital-ofensas-em-redes-sociais` ou `consumidor-acao-indenizatoria`); medidas protetivas (`penal-maria-da-penha-medidas-protetivas`).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. O fato: o que foi dito ou feito, por quem, onde, quando, diante de quem ou em qual meio (com prova: print com URL e data, ata notarial, áudio, testemunhas).
2. **Data em que o ofendido soube quem é o autor** (marco da decadência) e como prova essa data.
3. Qualificação do autor ou dados para identificá-lo (CPP 41); havendo vários autores, todos (indivisibilidade, CPP 48).
4. Contexto doméstico e familiar contra mulher? (prazo de 12 meses; possível ação pública).
5. A vítima é servidor ofendido em razão da função? Houve representação ao MP?
6. Houve acordo, retratação, pedido de desculpas aceito, ou ato que possa ser renúncia tácita (CP 104)?
7. Rol de testemunhas e provas a requerer.

## Prazo e contagem
- Decadência: 6 meses do dia em que o ofendido souber quem é o autor (CPP 38, caput; CP 103). Na violência doméstica e familiar contra a mulher, 12 meses (CPP 38 §2º, incluído pela Lei 15.438/2026).
- A decadência extingue a punibilidade (CP 107, IV). Prazo do Código Penal conta o dia do começo e segue o calendário comum (CP 10). Não protocole na véspera: confira com `prazos-processuais`.
- A lei afasta a decadência pelo **exercício do direito de queixa** (CPP 38). Não trate boletim de ocorrência ou pedido de inquérito como exercício do direito [VERIFICAR: não foi conferido precedente específico; aja como se não suspendessem]. Custas recolhidas depois não tornam intempestiva a queixa oferecida no prazo (AgRg no RHC 200.064).
- Depois de oferecida: perempção por 30 dias de inércia, falta a ato ou não pedir condenação nas alegações finais (CPP 60).

## Estrutura da peça
Endereçamento (JECRIM se pena máxima não superior a 2 anos — Lei 9.099, art. 61) → querelante e querelado(s) → fato com todas as circunstâncias → classificação → tempestividade → pedido de recebimento, citação e condenação → rol de testemunhas. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Requisitos do art. 41 do CPP: exposição do fato com todas as circunstâncias, qualificação ou identificação do acusado, classificação do crime e, quando necessário, rol de testemunhas. Queixa vaga é rejeitada por inépcia (CPP 395, I).
- Procuração com poderes especiais, com o nome do querelante e a menção ao fato criminoso (CPP 44). O STJ aceita menção simples, sem descrição pormenorizada; a indicação do delito basta (AgRg no HC 825.712). Corrija vício da procuração **dentro** do prazo decadencial.
- Indivisibilidade: a queixa contra um obriga ao processo de todos; renúncia a um se estende aos demais (CPP 48 e 49).
- O MP pode aditar em 3 dias (CPP 45 e 46 §2º).
- Crimes contra a honra no rito comum: audiência de reconciliação antes do recebimento (CPP 520 a 522); exceção da verdade contestável em 2 dias (CPP 523).
- No JECRIM: composição civil homologada implica renúncia ao direito de queixa (Lei 9.099, art. 74, parágrafo único); queixa pode ser oral (art. 77 §3º).

## Fundamentos verificados
- CPP 19, 30, 31, 32, 38, 41, 44, 45, 46 §2º, 48 a 53, 57, 58, 60, 395, 520 a 523, 581, I.
- CP 10, 100, 103 a 107, 138 a 141 §3º, 145. Lei 9.099/1995, arts. 61, 74, 77 §3º. Lei 15.438/2026.
- Súmula 714/STF; STJ: AgRg no HC 825.712, AgRg no AREsp 2.348.450, AgRg no RHC 238.680, AgRg no RHC 200.064.
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
1. Designação de audiência de reconciliação (CPP 520), se rito comum dos crimes contra a honra; ou de audiência preliminar (Lei 9.099, art. 72), se JECRIM.
2. Recebimento da queixa e citação do querelado.
3. Intimação do MP (CPP 45).
4. Produção de prova: oitiva das testemunhas arroladas, juntada de ata notarial, requisição de dados a provedor quando necessário.
5. Condenação nas penas do tipo indicado, com causas de aumento (CP 141).
6. Valor mínimo de reparação, se pretendido [VERIFICAR: CPP art. 387, IV, não conferido nesta skill]; juros e correção pelo núcleo `juros-e-correcao`.

## Checklist pré-protocolo
- [ ] Data do conhecimento da autoria documentada; prazo de 6 (ou 12) meses calculado com folga
- [ ] Procuração com poderes especiais, nome do querelante e menção ao fato
- [ ] Todos os autores incluídos (indivisibilidade)
- [ ] Fato descrito com data, local, meio, palavras exatas e destinatários
- [ ] Classificação correta e causa de aumento, se houver
- [ ] Competência (JECRIM x vara criminal) conferida pela pena máxima
- [ ] Prova pré-constituída juntada (ata notarial, prints com URL)
- [ ] Custas recolhidas ou pedido de gratuidade

## Erros a evitar
- Contar a decadência da data do fato quando a autoria só foi conhecida depois, ou o contrário, sem prova da data.
- Contar com o boletim de ocorrência ou com o inquérito para segurar a decadência.
- Procuração genérica "para propor ação penal" sem menção ao fato.
- Processar só um dos ofensores conhecidos (renúncia tácita aos demais).
- Deixar de pedir a condenação nas alegações finais (perempção, CPP 60, III).

## Integração com o núcleo
`prazos-processuais`, `juros-e-correcao`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

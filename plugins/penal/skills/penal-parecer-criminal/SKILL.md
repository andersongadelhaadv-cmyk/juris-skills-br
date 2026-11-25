---
name: penal-parecer-criminal
description: >
  Elabora parecer jurídico criminal consultivo (atividade privativa da advocacia,
  EOAB art. 1º, II): enquadramento típico de conduta passada ou pretendida,
  risco penal de operação empresarial, viabilidade de tese defensiva, prescrição,
  cabimento de ANPP ou transação, e estratégia para cliente investigado ou
  denunciado. Use quando o usuário pedir parecer penal, opinião legal criminal,
  consulta sobre se uma conduta é crime, análise de risco penal, memorando de
  estratégia de defesa, segunda opinião sobre processo criminal ou avaliação de
  chances de recurso.
metadata:
  area: penal
  tipo_peca: parecer
  verificado_em: 2026-11-25
---
# Parecer criminal (consultivo)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo ou da entrega ao cliente.

## Quando usar / quando não usar
- Usar: consulta escrita de cliente (pessoa física ou empresa) ou de colega sobre (a) tipicidade de conduta já praticada ou planejada; (b) risco penal de operação, contrato, política interna ou comunicação; (c) diagnóstico de inquérito ou ação penal em curso (teses, provas, prescrição, saídas negociadas); (d) segunda opinião sobre estratégia recursal.
- Não usar:
  - peça processual concreta — `penal-resposta-a-acusacao`, `penal-alegacoes-finais`, `penal-apelacao-criminal`, `penal-habeas-corpus`, `penal-recurso-especial-criminal`;
  - atuação na investigação — `penal-defesa-no-inquerito-policial`, `penal-defesa-em-pic`, `penal-acesso-aos-autos-do-inquerito`;
  - negociação de acordo — `penal-anpp`;
  - crime ambiental, cibernético ou militar — `amb-defesa-crime-ambiental`, `digital-crime-cibernetico`, `mil-defesa-criminal-militar`;
  - programa de integridade empresarial — `reg-programa-integridade-compliance`; parecer de outra área — `consumidor-parecer`, `trib-parecer-tributario`, `soc-parecer-societario`, `contratos-parecer-sobre-contrato`.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Quem consulta e em que qualidade (investigado, vítima, empresa, gestor, colega). Conflito de interesses checado.
2. A **pergunta exata** a ser respondida (uma ou mais, numeradas).
3. Fatos com datas, valores, pessoas e documentos; o que é certo, o que é versão do cliente e o que é desconhecido.
4. Existe procedimento instaurado? Número, fase, decisões, peças obtidas (com acesso regular — EOAB art. 7º, XIV; Súmula Vinculante 14).
5. Antecedentes do interessado e eventual benefício anterior (relevante para ANPP, transação, sursis).
6. Finalidade do parecer: decisão interna, apresentação a terceiro, juntada em processo (muda tom e grau de reserva).

## Prazo e contagem
- Não há prazo legal para o parecer; há prazos **que o parecer deve apontar**: prescrição da pretensão punitiva (calcule por tipo e marcos interruptivos, ver `penal-dosimetria`), decadência da representação ou queixa, prazos processuais em curso (`prazos-processuais`).
- Registre a data-base do parecer: a conclusão vale para a lei e a jurisprudência daquela data.

## Estrutura do documento
Ementa → consulta (perguntas) → documentos examinados e premissas fáticas → análise por pergunta (tipo penal, elementos, prova, excludentes, prescrição, jurisprudência) → riscos graduados → alternativas e recomendações → respostas objetivas → ressalvas → data e assinatura. Detalhe em [estrutura](references/estrutura.md).

## Requisitos e cautelas
- **Premissas explícitas**: o parecer responde aos fatos informados. Liste-as e diga o que mudaria a conclusão.
- **Análise do tipo penal completa**: conduta, objeto, sujeitos, elemento subjetivo (dolo/culpa), elementares normativas, consumação/tentativa, concurso de pessoas, causas de aumento, crimes conexos (ex.: lavagem a partir de crime antecedente).
- **Gradação de risco honesta**: baixo / moderado / alto, com a razão de cada nota. Nunca prometer resultado.
- **Conduta futura**: o parecer orienta para a licitude; não ajuda a ocultar, fracionar ou disfarçar ilícito. Se a pergunta for "como fazer sem ser pego", recuse esse ponto e aponte a alternativa lícita.
- **Sigilo profissional**: marcar como confidencial e restrito ao cliente; cuidado ao circular por e-mail corporativo. Avaliar se o parecer deve ser escrito ou apenas verbal quando houver risco de apreensão de documentos.
- **Jurisprudência**: toda citação conferida em `verificacao-de-citacoes`; divergência entre turmas do STJ ou entre STJ e STF deve ser exposta, não escondida.

## Fundamentos verificados
- EOAB (Lei 8.906/1994) art. 1º, II (consultoria privativa) e art. 7º, XIV (exame de autos de investigação), § 11 (limitação a diligências em andamento).
- CF art. 5º, LV (ampla defesa).
- Súmula Vinculante 14 do STF (acesso da defesa a elementos já documentados).
Detalhe em [fundamentos](references/fundamentos.md).

## Conteúdo essencial das respostas
- Resposta direta a cada pergunta (sim / não / depende de X), antes da fundamentação longa.
- Risco por cenário e por pessoa (empresa x sócio x empregado).
- Medidas recomendadas: preservar documentos, não contatar testemunhas, avaliar colaboração ou acordo, regularização (ex.: pagamento em crimes tributários — conferir regra específica com `trib-parecer-tributario`), comunicação a autoridade quando cabível.
- O que fazer se houver busca, intimação ou prisão (contato do advogado; direito ao silêncio — CF 5º, LXIII).

## Checklist antes de entregar
- [ ] Perguntas numeradas e respondidas na mesma ordem
- [ ] Premissas fáticas listadas, com fonte de cada uma
- [ ] Tipo penal analisado elemento por elemento
- [ ] Prescrição e decadência verificadas
- [ ] Saídas negociadas avaliadas (ANPP, transação, suspensão condicional)
- [ ] Riscos graduados e justificados
- [ ] Citações conferidas; nenhuma de memória
- [ ] Marcação de confidencialidade e data-base
- [ ] Nenhum dado pessoal desnecessário de terceiros

## Erros a evitar
- Responder à pergunta que o cliente gostaria de ter feito, e não à que fez.
- Tratar a versão do cliente como fato provado.
- Concluir "não é crime" sem examinar tipos subsidiários e conexos.
- Esquecer a pessoa jurídica (crime ambiental) e os administradores.
- Citar acórdão isolado como "entendimento pacífico".
- Parecer longo sem conclusão objetiva na primeira página.

## Integração com o núcleo
`verificacao-de-citacoes`, `fidelidade-factual` (premissas x documentos), `prazos-processuais`, `estilo-forense`. Cálculo de pena e prescrição: `penal-dosimetria`.

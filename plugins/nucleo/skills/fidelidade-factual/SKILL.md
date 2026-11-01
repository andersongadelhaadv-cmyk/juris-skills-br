---
name: fidelidade-factual
description: >
  Camada anti-alucinação de toda peça: impede inventar fatos do caso, datas,
  valores, documentos, dispositivos, precedentes ou doutrina; separa fato
  informado, fato documentado e inferência; define quando perguntar e quando
  marcar [VERIFICAR] (CPC arts. 77, I, e 80, II; EOAB art. 34, XIV). Use quando
  o usuário pedir revisão de fidelidade, conferir se a peça "inventou algo",
  checar fatos, auditoria do rascunho, ou sempre que faltar dado para redigir.
metadata:
  area: nucleo
  tipo_peca: outro
  verificado_em: 2026-11-01
---
# Fidelidade factual

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

Princípio: a peça só afirma o que veio do usuário, dos documentos ou de fonte
verificada. O que faltar é perguntado; o que não puder ser perguntado agora fica
visível como [VERIFICAR: ...] ou [PREENCHER: ...]. Um texto com lacunas marcadas
é útil; um texto completo com dados inventados é perigoso.

## Quando usar / quando não usar
- Usar: em toda redação de peça (antes, para levantar dados; depois, para auditar);
  ao receber um rascunho para revisão; ao resumir autos.
- Não usar como substituto de `verificacao-de-citacoes` (precedentes e normas) – as
  duas atuam juntas.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
- Relato do cliente e documentos (contrato, notificações, prints, laudos, decisões).
- Partes com qualificação completa; números de processo; datas-chave; valores.
- Pedido do usuário: o que a peça deve obter.
Perguntas devem ser agrupadas, curtas e numeradas, priorizando o que muda a tese,
o cabimento ou o prazo. Modelo em [estrutura](references/estrutura.md).

## Prazo e contagem
Não se aplica; prazos seguem `prazos-processuais`, sempre a partir de data informada.

## Estrutura da peça
Três camadas, marcadas mentalmente em cada frase do rascunho:
1. **Fato informado** pelo usuário (relato) – escrever como alegação da parte.
2. **Fato documentado** – escrever com remissão ao documento (doc. 3; fls.; id. PJe).
3. **Inferência ou tese** – escrever como argumento ("o que revela", "permite
   concluir"), nunca como fato.
Roteiro de auditoria em [estrutura](references/estrutura.md).

## Requisitos e preliminares
O que nunca se inventa:
- nomes, CPF/CNPJ, endereços, estado civil, profissão;
- datas, horários, valores, percentuais, números de contrato, protocolo, processo;
- conteúdo de documentos não lidos; falas de testemunhas; resultado de perícia;
- dispositivos de lei, súmulas, temas, acórdãos, relatores, ementas;
- doutrina (autor, obra, edição, página) – sem a referência do usuário, não cite;
- fatos "prováveis" para preencher a narrativa (por exemplo, "o autor tentou resolver
  amigavelmente" sem que isso tenha sido dito).

Marcadores padronizados:
- `[PREENCHER: dado]` – informação objetiva que o usuário deve fornecer.
- `[VERIFICAR: o quê e onde]` – afirmação que depende de conferência (fonte, documento,
  vigência, número).
- `[CONFIRMAR COM O CLIENTE: ponto]` – fato sensível ou estratégico.

## Fundamentos verificados
- CPC art. 77, I e II (verdade e não deduzir pretensão sem fundamento); art. 80, II
  (alterar a verdade dos fatos é má-fé); art. 81 (multa, indenização, honorários).
- CPC arts. 319, III e VI, 320 e 434: fatos, provas e documentos indispensáveis
  instruem a inicial; a contestação também deve vir com seus documentos.
- EOAB (Lei 8.906/1994), art. 34, XIV: deturpar lei, citação ou julgado é infração.
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Quando faltar documento em poder da outra parte ou de terceiro, prefira pedir a
  exibição (CPC 396 e seguintes) ou diligência para obter dados da parte (CPC 319, §1º)
  a supor o conteúdo.

## Checklist pré-protocolo
- [ ] Toda data, valor e nome do texto tem origem identificável (relato, documento, autos).
- [ ] Nenhum fato foi acrescentado para "fechar" a narrativa.
- [ ] Inferências estão redigidas como argumento, não como fato.
- [ ] Cada documento citado existe e diz o que a peça afirma que diz.
- [ ] Precedentes e normas passaram por `verificacao-de-citacoes`.
- [ ] Nenhuma doutrina sem referência fornecida pelo usuário.
- [ ] Todos os [PREENCHER] e [VERIFICAR] foram resolvidos ou listados para o advogado.
- [ ] Versões contraditórias do cliente foram apontadas, não harmonizadas por conta própria.

## Erros a evitar
- Completar qualificação com dados genéricos ("brasileiro, casado, empresário") sem base.
- Converter "o cliente acha que" em "restou comprovado que".
- Inventar o conteúdo de um anexo citado só pelo nome.
- Atribuir a frase de uma ementa ao "entendimento pacífico" sem pesquisa.
- Esconder a lacuna: dado incerto escrito sem marcador.

## Integração com o núcleo
- `verificacao-de-citacoes`: para leis, súmulas, temas e acórdãos.
- `prazos-processuais` e `juros-e-correcao`: só calculam a partir de datas fornecidas.
- `estilo-forense`: forma da narrativa dos fatos (cronológica, com remissão a documentos).

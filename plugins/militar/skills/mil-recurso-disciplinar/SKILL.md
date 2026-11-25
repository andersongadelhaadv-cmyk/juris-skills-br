---
name: mil-recurso-disciplinar
description: >
  Redige defesa e recursos no processo disciplinar militar: pedido de
  reconsideração, recurso disciplinar hierárquico e cancelamento de registro de
  punição (Lei 6.880/1980, arts. 47 e 51; Regulamento Disciplinar do Exército,
  Decreto 4.346/2002, como modelo), com regra sobre guarda municipal (Lei
  13.022/2014). Use quando o usuário pedir recurso contra punição disciplinar
  de militar, reconsideração de ato, defesa em apuração de transgressão,
  cancelamento de punição na ficha, recurso contra prisão ou detenção
  disciplinar ou contra punição aplicada a guarda municipal.
metadata:
  area: militar
  tipo_peca: recurso
  verificado_em: 2026-11-25
---
# Recurso em processo disciplinar militar

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: punição disciplinar aplicada ou em apuração (repreensão, detenção, prisão, impedimento, licenciamento ou exclusão a bem da disciplina) a militar das Forças Armadas ou, com o regulamento estadual, a policial ou bombeiro militar.
- Não usar: esfera administrativa esgotada ou ilegalidade urgente — `mil-mandado-de-seguranca`; prisão disciplinar com vício formal grave — `mil-habeas-corpus`; exclusão já consumada com pedido de volta e reparação — `mil-reintegracao-e-reforma`; servidor civil — `adm-defesa-em-pad`.
- Guarda municipal não é militar: não pode ficar sujeita a regulamento disciplinar de natureza militar (Lei 13.022/2014, art. 14, parágrafo único). Defesa e recurso seguem o código de conduta e a lei municipal (art. 14) — use `adm-defesa-em-pad`; se o município aplicou regulamento militar, essa é a tese central de nulidade.

## Entradas mínimas (perguntar o que faltar; nunca supor fatos)
1. Força ou corporação e regulamento aplicável (RDE, regulamentos da Marinha e da Aeronáutica, regulamento estadual), na versão vigente na data do fato.
2. Documento de apuração (formulário, sindicância), defesa apresentada, decisão e boletim de publicação, com datas.
3. Transgressão imputada (item do regulamento) e punição aplicada; classificação do comportamento afetada.
4. Data da ciência oficial da decisão (marca o prazo).
5. Autoridade que puniu e cadeia de comando até o comandante da Força.
6. Fato também é crime militar? Há IPM ou ação penal?

## Prazo e contagem
- Estatuto: o direito de recorrer administrativamente prescreve em 45 dias, ou 15 dias para quota compulsória e quadro de acesso (Lei 6.880/1980, art. 51, § 1º, redação da Lei 13.954/2019).
- RDE (Exército): reconsideração em cinco dias úteis da ciência da publicação (art. 53, § 2º); recurso disciplinar em cinco dias úteis da ciência da decisão (art. 54, § 2º); decisões em dez dias úteis (arts. 53, § 3º, e 54, § 6º).
- Divergência entre o prazo do Estatuto (lei posterior) e o do regulamento: protocole dentro do prazo menor e, se perdido, sustente o prazo legal [VERIFICAR entendimento atual].
- Marinha, Aeronáutica e corporações estaduais: prazos do próprio regulamento [VERIFICAR o texto local]. Mandado de segurança: 120 dias, sem interrupção por reconsideração (Súmula 430/STF). Contagem: `prazos-processuais`.

## Estrutura da peça
Pedido de reconsideração à autoridade que puniu → recurso à autoridade imediatamente superior, sucessivamente até o comandante da Força (RDE, art. 54, § 1º). Roteiro em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Nenhuma punição sem contraditório, ampla defesa e fatos apurados (CF art. 5º, LV; RDE, art. 35, § 1º); o § 2º do art. 35 do RDE lista os direitos do militar (acompanhar a apuração, ser ouvido, produzir prova, obter cópias, decisão que enfrente as alegações).
- Penas de impedimento, detenção ou prisão não ultrapassam 30 dias (Estatuto, art. 47, § 1º).
- Recurso individual, sobre caso específico, restrito aos fatos e fundamentado (RDE, art. 54, § 3º); nenhuma autoridade pode deixar de encaminhá-lo por falta de formalidade (art. 54, § 4º). Pedido coletivo é vedado (Estatuto, art. 51, § 2º).
- Ausência de advogado não anula, por si, o processo disciplinar (Súmula Vinculante 5).
- Fato que também é crime militar: prescrição disciplinar pela lei penal militar (STJ, AgInt no RMS 59.583); instâncias independentes (Tema 565/STF).
- Prisão e detenção de PM e bombeiro militar: a Lei 13.967/2019 e a ADI 6.595 afetam o tema [VERIFICAR o resultado e o alcance no portal do STF antes de usar].

## Fundamentos verificados
- CF art. 5º, LV; Lei 6.880/1980, arts. 47, 49 e 51; Decreto 4.346/2002 (RDE), arts. 35, 52 a 59; Lei 13.022/2014, arts. 13 e 14.
- Súmulas 430 e Vinculante 5 do STF; Tema 565/STF; STJ, AgInt no RMS 59.583.
Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Anulação da punição e cancelamento de tudo que a ela se refira (RDE, art. 55) ou, em parte, atenuação ou relevação (art. 55, parágrafo único).
- Afastamento da subordinação direta da autoridade recorrida, se preciso para a disciplina (art. 56).
- Tramitação urgente (art. 57, parágrafo único) e encaminhamento obrigatório (art. 54, § 4º).
- Cancelamento de registro de punição antiga, se preenchidos os requisitos do art. 59 do RDE.

## Checklist pré-protocolo
- [ ] Regulamento certo (Força ou Estado) e versão da data do fato
- [ ] Ciência oficial datada e prazo menor controlado
- [ ] Vícios de contraditório apontados item a item do art. 35, § 2º, do RDE (ou equivalente)
- [ ] Recurso individual, fundamentado e com provas anexas
- [ ] Guarda municipal? Afastado o regulamento militar (Lei 13.022/2014, art. 14)
- [ ] Prazo de 120 dias do MS anotado desde a ciência

## Erros a evitar
- Recorrer coletivamente ou misturar casos de vários militares.
- Deixar o prazo do MS correr enquanto aguarda a reconsideração.
- Aplicar o RDE a marinheiro, aviador ou policial militar sem conferir o regulamento próprio.
- Tratar guarda municipal como militar.

## Integração com o núcleo
`prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

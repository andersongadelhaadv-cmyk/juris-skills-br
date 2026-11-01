---
name: civel-juizado-especial
description: >
  Redige peças do Juizado Especial Cível (Lei 9.099/1995): pedido inicial,
  contestação com pedido contraposto e recurso inominado (arts. 41 a 43), com
  limites de valor (40 salários mínimos; advogado obrigatório acima de 20),
  prazos em dias úteis (art. 12-A) e remissão aos juizados federal e da Fazenda
  (60 salários mínimos). Use quando o usuário pedir ação no juizado, "pequenas
  causas", JEC, contestação no juizado, recurso inominado ou recurso à turma recursal.
metadata:
  area: processo-civil
  tipo_peca: inicial
  verificado_em: 2026-11-01
---
# Juizado Especial Cível (inicial, contestação, recurso inominado)

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: causas de menor complexidade (Lei 9.099, art. 3º): até 40 salários mínimos; causas do art. 275, II, do CPC/1973 (mantidas pelo art. 1.063 do CPC, redação da Lei 14.976/2024); despejo para uso próprio; possessórias de imóvel até 40 SM.
- Juizado Federal (Lei 10.259, art. 3º) e da Fazenda Pública (Lei 12.153, art. 2º): até 60 SM, competência absoluta onde instalados; adaptar endereçamento e partes.
- Não usar: causas alimentares, falimentares, fiscais, de interesse da Fazenda (no JEC estadual), acidente de trabalho, resíduos, estado e capacidade (art. 3º, §2º); partes vedadas (art. 8º); causa complexa que exija perícia.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
- Valor da causa e do salário mínimo vigente na data do ajuizamento; se o cliente aceita renunciar ao excedente (art. 3º, §3º).
- Qualificação das partes e enquadramento do autor no art. 8º, §1º.
- Fatos, documentos, testemunhas (até três, levadas à audiência).
- Para recurso: sentença, data da ciência, valor do preparo.

## Prazo e contagem
- Todos os prazos em dias úteis (art. 12-A).
- Contestação: até a audiência de instrução, oral ou escrita (art. 30), conforme o rito local.
- Recurso inominado: 10 dias da ciência da sentença (art. 42); preparo em 48 horas seguintes à interposição, sem intimação, sob pena de deserção (§1º); contrarrazões em 10 dias (§2º).
- ED: 5 dias, interrompem o prazo (arts. 49 e 50). Use `prazos-processuais`.

## Estrutura da peça
Inicial simples (art. 14) → contestação concentrada com pedido contraposto (arts. 30 e 31) → recurso inominado com razões e pedido (art. 42). Detalhe em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Advogado: facultativo até 20 SM; obrigatório acima (art. 9º) e sempre no recurso (art. 41, §2º).
- Pedido pode ser genérico se a extensão não puder ser determinada (art. 14, §2º), mas a sentença deve ser líquida (art. 38, p.ú.).
- Sem intervenção de terceiros; litisconsórcio admitido (art. 10). Sem citação por edital (art. 18, §2º).
- Ausência do autor a qualquer audiência extingue o processo (art. 51, I).
- Reconvenção não cabe; pedido contraposto nos mesmos fatos e no limite do art. 3º (art. 31).
- Recurso inominado só tem efeito devolutivo, salvo concessão para evitar dano irreparável (art. 43).

## Fundamentos verificados
Lei 9.099/1995, arts. 3º, 4º, 8º, 9º, 10, 12-A, 14, 18, 20, 30, 31, 38, 41 a 43, 48 a 55; Lei 10.259/2001, art. 3º; Lei 12.153/2009, art. 2º; CPC art. 1.063; Súmula 203 do STJ; Súmula 640 do STF. Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Inicial: citação com advertência do art. 18, §1º; procedência; pedidos dentro do teto (soma dos cumulados — art. 15).
- Contestação: improcedência; pedido contraposto, se houver.
- Recurso: reforma ou anulação; efeito suspensivo excepcional (art. 43); honorários de 10% a 20% contra o recorrente vencido (art. 55).
- Juros e correção: indicar índice e termo pela skill `juros-e-correcao`.

## Checklist pré-protocolo
- [ ] Valor dentro do teto (40 SM no JEC; 60 SM no JEF/JEFP), com renúncia ao excedente consciente.
- [ ] Autor admitido (art. 8º) e matéria não excluída (art. 3º, §2º).
- [ ] Foro do art. 4º.
- [ ] Recurso: 10 dias úteis, preparo em 48 horas, advogado constituído.
- [ ] Contestação: toda a defesa concentrada; pedido contraposto com valor.
- [ ] Prova testemunhal: até três testemunhas, comparecimento combinado.

## Erros a evitar
- Contar o preparo do recurso em dias (são 48 horas da interposição) ou aguardar intimação para pagar.
- Interpor REsp contra acórdão de turma recursal (Súmula 203 do STJ); só RE, se houver questão constitucional (Súmula 640 do STF).
- Reconvir no juizado.
- Faltar à audiência (extinção) ou deixar o preposto sem carta de preposição (art. 9º, §4º).
- Pedir valor acima do teto sem renunciar ao excedente.

## Integração com o núcleo
- `prazos-processuais` (dias úteis, 48 horas do preparo, 10 dias do recurso).
- `juros-e-correcao` para o pedido condenatório (sentença deve ser líquida).
- `verificacao-de-citacoes` para enunciados e precedentes de turmas recursais.
- `fidelidade-factual` e `estilo-forense` na revisão.

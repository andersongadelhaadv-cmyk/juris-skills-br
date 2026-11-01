---
name: roteador-de-pecas
description: >
  Hub de entrada do repositório: a partir do pedido do usuário, identifica
  área, fase processual, polo e tipo de peça e indica a skill certa (e as do
  núcleo que a acompanham), com base no catálogo de todas as skills por área.
  Use quando o usuário não souber qual peça cabe, pedir "qual skill usar",
  "por onde começo", "que peça eu faço", "qual recurso cabe", listar as skills
  disponíveis, ou descrever um caso sem dizer a peça.
metadata:
  area: nucleo
  tipo_peca: outro
  verificado_em: 2026-11-01
---
# Roteador de peças

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

A escolha da peça é decisão do advogado. Esta skill organiza a triagem e aponta a
skill de redação; quando houver mais de um caminho possível, apresenta as opções
com o critério que as distingue, em vez de escolher sozinha.

## Quando usar / quando não usar
- Usar: no início do atendimento, quando a peça não está definida; quando o usuário
  pede a lista do que existe; quando o pedido mistura áreas.
- Não usar quando o usuário já indicou a peça e a skill correspondente existe: vá direto a ela.

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. **Área** (cível, consumo, família, sucessões, trabalho, penal, previdenciário,
   tributário, Fazenda, administrativo).
2. **Fase**: consultivo/extrajudicial; administrativo; conhecimento (1º grau); recurso
   (e contra qual decisão); execução ou cumprimento.
3. **Polo**: autor/réu, reclamante/reclamada, defesa/assistência, contribuinte/Fazenda.
4. **Última decisão ou ato** e data da intimação (para cabimento e prazo).
5. **Rito**: comum, juizado, sumaríssimo, especial.

## Prazo e contagem
Assim que a peça for definida, calcule o prazo com `prazos-processuais` antes de
redigir, e avise o usuário se estiver perto do vencimento.

## Estrutura da peça
Fluxo de triagem: área → fase → polo → decisão atacada → skill. Mapa por situação e
catálogo completo em [catálogo](references/catalogo.md); critérios de desempate em
[estrutura](references/estrutura.md).

## Requisitos e preliminares
Encaminhamentos frequentes (amostra; a lista completa está no catálogo):
| Situação descrita | Skill |
|---|---|
| Quero processar (cível comum) | `civel-peticao-inicial`; até 40 salários mínimos, avaliar `civel-juizado-especial` |
| Fui citado (cível) | `civel-contestacao` (+ `civel-reconvencao`, se houver pretensão própria) |
| Saiu sentença cível | `civel-embargos-de-declaracao` (vício) ou `civel-apelacao` |
| Decisão interlocutória cível | `civel-agravo-de-instrumento` (rol do art. 1.015 ou urgência) |
| Decisão de relator | `civel-agravo-interno` |
| Acórdão de TJ/TRF | `civel-recurso-especial` e/ou `civel-recurso-extraordinario` |
| Cobrar com título | `civel-execucao-titulo-extrajudicial` ou `civel-cumprimento-de-sentenca` |
| Defesa do executado | `civel-impugnacao-ao-cumprimento`, `civel-embargos-a-execucao`, `civel-excecao-de-pre-executividade` |
| Reclamação trabalhista / defesa | `trabalhista-reclamacao` / `trabalhista-contestacao` |
| Recurso trabalhista | `trabalhista-recurso-ordinario`, `trabalhista-recurso-de-revista`, `trabalhista-agravo-de-peticao` |
| Denúncia recebida | `penal-resposta-a-acusacao` |
| Prisão | `penal-habeas-corpus` ou `penal-liberdade-provisoria-e-relaxamento` |
| Sentença penal | `penal-apelacao-criminal`; decisão do art. 581: `penal-recurso-em-sentido-estrito` |
| Execução penal | `penal-progressao-de-regime`, `penal-livramento-condicional`, `penal-agravo-em-execucao` |
| Benefício do INSS | `prev-requerimento-administrativo` → `prev-recurso-crps` → ação específica |
| Alimentos | `familia-acao-de-alimentos`, `familia-revisional-e-exoneracao-de-alimentos`, `familia-execucao-de-alimentos` |
| Execução fiscal | `trib-embargos-a-execucao-fiscal` ou `trib-excecao-pre-executividade-fiscal` |
| Ato de autoridade ilegal | `adm-mandado-de-seguranca`, `trib-mandado-de-seguranca` ou `trabalhista-mandado-de-seguranca` |
| Licitação | `adm-impugnacao-ao-edital`, `adm-recurso-em-licitacao`, `adm-defesa-em-processo-sancionador-licitacao` |

Se a peça pedida não tiver skill própria, diga isso, use a skill mais próxima da
mesma área como base estrutural e aplique todas as skills do núcleo.

## Fundamentos verificados
O cabimento de cada peça é tratado e fundamentado na skill de destino. Os
critérios de desempate desta skill usam dispositivos conferidos: Lei 9.099, arts. 3º
e 8º (40 SM; quem pode ser parte); Lei 10.259, art. 3º, e Lei 12.153, art. 2º (60 SM); CPC arts. 1.015, 1.021 e
1.042; CPP arts. 581 e 593, §4º; Lei 12.016, art. 23. Ver
[estrutura](references/estrutura.md).

## Pedidos e requerimentos
Não se aplica. A saída é: skill indicada, motivo em uma frase, dados ainda
necessários e prazo estimado.

## Checklist pré-protocolo
- [ ] Área, fase, polo e decisão atacada confirmados com o usuário.
- [ ] Cabimento conferido na skill de destino (não presumido pelo nome).
- [ ] Prazo calculado com `prazos-processuais`.
- [ ] Skills do núcleo associadas: `fidelidade-factual`, `verificacao-de-citacoes`,
      `estilo-forense` e, se houver condenação em dinheiro, `juros-e-correcao`.
- [ ] Quando há duas vias possíveis, ambas apresentadas ao usuário com o critério de escolha.

## Erros a evitar
- Escolher recurso pelo nome da decisão, e não pelo seu conteúdo.
- Ignorar o juizado ou o rito sumaríssimo quando o valor permite.
- Encaminhar matéria penal para skill cível de recurso (prazos e regras diferem).
- Tratar "mandado de segurança" como uma peça só: há versões por área.
- Dizer que existe skill que não está no catálogo.

## Integração com o núcleo
Todas as peças passam por `fidelidade-factual`, `verificacao-de-citacoes` e
`estilo-forense`; prazos por `prazos-processuais`; pedidos em dinheiro por
`juros-e-correcao`.

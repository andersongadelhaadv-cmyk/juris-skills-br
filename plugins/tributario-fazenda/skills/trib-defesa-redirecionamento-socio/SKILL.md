---
name: trib-defesa-redirecionamento-socio
description: >
  Monta a defesa do sócio, administrador ou ex-sócio contra o redirecionamento
  da execução fiscal (CTN art. 135, III; Súmulas 430 e 435/STJ; Temas 981, 444,
  103 e 108/STJ): manifestação contra o pedido da Fazenda, exceção de
  pré-executividade com prova documental, agravo contra a decisão que inclui o
  sócio ou embargos se houver garantia. Use quando o usuário pedir defesa de
  sócio incluído na execução fiscal, redirecionamento por dissolução irregular,
  ex-sócio cobrado por dívida da empresa, nome do sócio na CDA, prescrição para
  redirecionar ou exclusão do sócio do polo passivo.
metadata:
  area: tributario-fazenda
  tipo_peca: outro
  verificado_em: 2026-11-25
---
# Defesa contra o redirecionamento da execução fiscal ao sócio

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: a Fazenda pede (ou o juiz já deferiu) a inclusão de sócio, administrador ou terceiro não sócio no polo passivo da execução fiscal da empresa; ou o nome do sócio consta da CDA e ele quer sair do processo.
- Escolha da peça (esta skill dá as teses; a forma vem da skill vizinha):
  - prova toda documental (contrato social, alterações registradas, distrato com liquidação, datas): exceção — `trib-excecao-pre-executividade-fiscal`;
  - tese que exige prova (testemunhas, perícia contábil) e há garantia: `trib-embargos-a-execucao-fiscal`;
  - decisão que deferiu o redirecionamento: agravo de instrumento — `civel-agravo-de-instrumento`;
  - prescrição para redirecionar como tese central: também `trib-prescricao-intercorrente`.
- Não usar: desconsideração da personalidade em execução cível comum (`consumidor-desconsideracao-personalidade-juridica`, `civel-*`); dissolução societária entre sócios (`soc-dissolucao-parcial-e-exclusao-de-socio`); terceiro não incluído no processo que só teve bem atingido (`trib-embargos-de-terceiro-execucao-fiscal`).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Cópia integral da execução: CDA (o nome do sócio consta?), petição de redirecionamento, certidão do oficial que "não encontrou" a empresa, decisão de inclusão.
2. Ficha cadastral completa na Junta Comercial e todas as alterações contratuais, com datas de **registro**.
3. Período de gerência/administração do cliente e data de sua saída (registrada).
4. Situação da empresa: ativa, mudou de endereço comunicando o fisco, distrato registrado, liquidação feita (balanço, pagamento de credores), falência ou recuperação.
5. Fatos geradores e vencimentos dos débitos cobrados.
6. Datas: citação da empresa, diligência negativa, pedido de redirecionamento, citação do sócio.
7. Houve processo administrativo de responsabilização antes da inscrição do sócio na CDA?

## Prazo e contagem
- Manifestação contra o pedido da Fazenda: prazo fixado pelo juiz.
- Agravo de instrumento contra a decisão de inclusão, embargos (30 dias da garantia, LEF art. 16) e exceção (sem prazo, mas não suspende os embargos): conte com `prazos-processuais`.
- Prescrição para redirecionar: ver Requisitos (Tema 444) e calcule com `prazos-processuais`.

## Estrutura da peça
Síntese do redirecionamento → legitimidade (posição do cliente na sociedade no tempo) → ausência de ato do art. 135 → inexistência de dissolução irregular ou não administração na data dela (Tema 981) → prescrição do redirecionamento (Tema 444) → nulidade da inclusão na CDA sem apuração → pedidos. Roteiro em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- Responsabilidade pessoal dos diretores, gerentes ou representantes só por atos com excesso de poderes ou infração de lei, contrato social ou estatutos (CTN art. 135, III). A LEF admite execução contra o responsável "nos termos da lei" (art. 4º, V, e § 2º).
- Inadimplemento da sociedade, por si só, não gera responsabilidade do sócio-gerente (Súmula 430/STJ).
- Empresa que deixa de funcionar no domicílio fiscal sem comunicar os órgãos competentes: presume-se dissolvida irregularmente e o redirecionamento ao sócio-gerente é legítimo (Súmula 435/STJ). A presunção é atacável: prove a comunicação, o funcionamento em outro endereço informado ou a liquidação regular.
- Dissolução irregular: o redirecionamento cabe contra sócio ou terceiro não sócio **com poderes de administração na data em que configurada ou presumida a dissolução**, ainda que não os tivesse no fato gerador (Tema 981/STJ, REsp 1.643.944, 1ª Seção, 2022). Defesa típica: o cliente não administrava na data da dissolução (saída registrada antes da diligência negativa).
- Sócio que exercia a gerência no fato gerador, mas se retirou regularmente e não deu causa à dissolução [VERIFICAR: tese do Tema 962/STJ, sem cobertura no JuriBase].
- Distrato registrado sem liquidação (levantamento do ativo, pagamento dos credores) não prova dissolução regular (STJ, AREsp 2.938.315, 2ª Turma, 2025; REsp 1.877.340, 2ª Turma, 2022).
- Nome na CDA: se a execução foi ajuizada contra a empresa e o nome do sócio consta da CDA, a ele cabe provar a ausência dos requisitos do art. 135; a exceção não serve se a prova exigir dilação (Temas 103 e 108/STJ, conforme AgInt nos EDcl no REsp 2.026.107, 1ª Turma, 2024). Mas, com prova pré-constituída, a ilegitimidade pode ser reconhecida na exceção (REsp 2.194.361, 2ª Turma, 2026, com distinção desses temas e aplicação da Súmula 430). Nome fora da CDA: ônus da Fazenda [VERIFICAR: trecho dos Temas 103/108].
- Incidente de desconsideração: dispensado quando o redirecionamento se funda nos arts. 134 e 135 do CTN (AgInt no AgInt no REsp 2.062.586, 1ª Turma, 2023). Não baseie a defesa só na falta do incidente.
- Prescrição do redirecionamento (Tema 444/STJ, REsp 1.201.993): prazo de 5 anos contado da citação da pessoa jurídica quando o ato inequívoco de dissolução é anterior; se a dissolução é posterior à citação, a contagem parte do ato (actio nata) (AgInt no REsp 2.080.885, 1ª Turma, 2025; AgInt no AREsp 1.849.369, 1ª Turma, 2022).

## Fundamentos verificados
CTN arts. 134 e 135; LEF art. 4º; Súmulas 393, 430 e 435/STJ; Temas 981, 444, 103 e 108/STJ (pelos acórdãos indicados); AREsp 2.938.315; REsp 1.877.340; REsp 2.194.361; AgInt no AgInt no REsp 2.062.586. Detalhe em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Indeferimento do redirecionamento ou exclusão do sócio do polo passivo.
- Levantamento de bloqueios e penhoras sobre bens do sócio.
- Subsidiariamente, limitação da responsabilidade ao período de gerência e aos débitos ligados ao ato imputado.
- Honorários contra a Fazenda na exclusão (regras e exceções em `trib-excecao-pre-executividade-fiscal`).
- Valores a liberar ou recalcular: `juros-e-correcao`.

## Checklist pré-protocolo
- [ ] Linha do tempo: gerência do cliente × fatos geradores × diligência negativa × citações
- [ ] Alterações contratuais com data de registro na Junta
- [ ] Prova de comunicação de endereço ou de liquidação regular (contra a Súmula 435)
- [ ] Nome na CDA verificado — define ônus e via
- [ ] Prescrição do redirecionamento calculada (Tema 444)
- [ ] Peça certa escolhida (exceção, agravo, embargos) e prazos controlados

## Erros a evitar
- Usar exceção com prova dependente de testemunha ou perícia quando o nome está na CDA.
- Alegar apenas que "não havia gerência no fato gerador" quando a imputação é a dissolução irregular (Tema 981).
- Juntar distrato sem prova de liquidação.
- Basear a defesa só na falta de incidente de desconsideração.
- Deixar passar o prazo do agravo esperando decisão sobre manifestação.

## Integração com o núcleo
`prazos-processuais`, `juros-e-correcao`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

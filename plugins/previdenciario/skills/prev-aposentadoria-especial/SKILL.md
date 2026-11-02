---
name: prev-aposentadoria-especial
description: >
  Estrutura a ação de aposentadoria especial ou de reconhecimento e conversão de
  tempo especial no RGPS (Lei 8.213/1991, arts. 57 e 58; EC 103/2019, arts. 19,
  21 e 25, §2º), com análise de PPP/LTCAT e dos limites de ruído. Use quando o
  usuário pedir aposentadoria especial, tempo especial, insalubridade para o INSS,
  conversão de tempo especial em comum, PPP, LTCAT, ruído, EPI eficaz ou agente nocivo.
metadata:
  area: previdenciario
  tipo_peca: inicial
  verificado_em: 2026-11-01
---
# Aposentadoria especial e conversão de tempo especial

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: concessão de aposentadoria especial (15, 20 ou 25 anos de exposição); averbação de tempo especial; conversão de tempo especial em comum para períodos até 13/11/2019; revisão para incluir tempo especial (observar a decadência, ver `prev-revisao-de-beneficio`).
- Servidor público: ver `prev-rpps-servidor` (STF Tema 942 e Súmula Vinculante 33).
- Não usar para adicional de insalubridade trabalhista (área trabalhista).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Períodos, empregadores, cargos e setores.
2. PPP de cada período (com responsável pelos registros ambientais e técnica de medição) e LTCAT quando houver.
3. Agente nocivo, intensidade/concentração, habitualidade e permanência.
4. Filiação antes ou depois de 13/11/2019 e idade na DER.
5. Requerimento administrativo com os PPPs juntados (Tema 350 STF).
6. Se o segurado continua trabalhando exposto (STF Tema 709).

## Prazo e contagem
- Concessão: sem decadência (STF Tema 313); prescrição quinquenal das parcelas.
- Revisão para incluir tempo especial: decadência de 10 anos (Lei 8.213, art. 103).
- Prazos processuais em dias úteis (CPC, art. 219).

## Estrutura da peça   (detalhe em [estrutura](references/estrutura.md))
1. Competência e interesse de agir.
2. Fatos: quadro de períodos com agente e prova.
3. Direito: lei vigente na época da prestação (tempus regit actum) por período.
4. Ruído: limites por época e metodologia.
5. EPI: limites da descaracterização.
6. Regra de concessão: direito adquirido, art. 21 (pontos) ou art. 19 (idade).
7. Conversão de tempo especial até 13/11/2019 (subsidiário).
8. Pedidos e provas (perícia técnica).

## Requisitos e preliminares
- Ruído: 80 dB até 05/03/1997; 90 dB de 06/03/1997 a 18/11/2003; 85 dB a partir de 19/11/2003 (STJ Tema 694, REsp 1.398.260, tese reproduzida em AgInt no REsp 1.950.196). A partir de 19/11/2003, medição pela NHO-01/NR-15 com indicação da técnica no PPP (TNU Tema 174); com NEN superior a 85 dB, ou, sem NEN, nível de pico com perícia que comprove habitualidade (STJ, EDcl no REsp 1.886.795).
- EPI: eficácia real afasta a especialidade, mas não para ruído (STF Tema 555); e não obsta o reconhecimento antes de 03/12/1998 (TNU Súmula 87).
- Regras de concessão pós-EC 103: art. 21 (filiados até 13/11/2019): 66, 76 ou 86 pontos com 15, 20 ou 25 anos de exposição, sem acréscimo anual; art. 19, §1º, I (filiados depois): 55, 58 ou 60 anos com 15, 20 ou 25 anos.
- Conversão em comum só para tempo até a entrada em vigor da EC 103 (art. 25, §2º).
- Categoria profissional: vedada após a EC 103 (CF, art. 201, §1º, II). Para períodos anteriores à vigência da Lei 9.032, de 28/04/1995, admite-se o enquadramento pela categoria dos Decretos 53.831/1964 e 83.080/1979, ou a prova da exposição por qualquer meio, salvo ruído e calor, que sempre exigiram laudo (STJ, AgInt no AREsp 2.091.072).

## Fundamentos verificados   (detalhe em [fundamentos](references/fundamentos.md))
- Lei 8.213, arts. 57 (15/20/25 anos; §8º vedação de continuar exposto) e 58 (PPP com base em LTCAT; §2º informação sobre EPI).
- EC 103, arts. 19, §1º, I; 21; 25, §2º; 26, §§2º e 5º.
- STJ Tema 694 (ruído 90 dB entre 1997 e 2003, sem retroação do Decreto 4.882/2003).
- STF Tema 555 (EPI e ruído); STF Tema 709 (vedação de continuar em atividade especial).
- TNU Tema 174 (metodologia), Súmulas 9, 68 e 87.

## Pedidos e requerimentos
- Reconhecimento dos períodos especiais indicados.
- Concessão da aposentadoria especial pela regra aplicável, desde a DER; subsidiariamente, conversão do tempo especial até 13/11/2019 e concessão de aposentadoria comum pela regra mais vantajosa; reafirmação da DER.
- Perícia técnica judicial (por similaridade, se a empresa estiver extinta).
- Atrasados com correção e juros conforme `juros-e-correcao`.

## Checklist pré-protocolo
- [ ] PPP de cada período, com técnica de medição e responsável técnico.
- [ ] LTCAT anexado quando o PPP for omisso na metodologia (TNU Tema 174, b).
- [ ] Limite de ruído correto para cada época.
- [ ] Verificado se o cliente continua exposto (Tema 709 STF) e orientado.
- [ ] Conversão pedida apenas para períodos até 13/11/2019.
- [ ] Juros e correção remetidos ao núcleo.

## Erros a evitar
- Aplicar 85 dB ao período de 06/03/1997 a 18/11/2003.
- Aceitar a declaração de EPI eficaz no PPP como obstáculo para ruído.
- Pedir conversão de tempo especial posterior a 13/11/2019.
- Usar pontuação do art. 21 com acréscimo anual (não há).
- Omitir o pedido subsidiário de aposentadoria comum com conversão.

## Integração com o núcleo
- `juros-e-correcao` para os atrasados.
- `prazos-processuais`; `verificacao-de-citacoes` para qualquer precedente novo (ex.: outros agentes nocivos).
- `fidelidade-factual` para conferir os dados do PPP; `estilo-forense`.

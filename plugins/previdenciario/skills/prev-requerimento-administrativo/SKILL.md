---
name: prev-requerimento-administrativo
description: >
  Prepara o requerimento administrativo de benefício ao INSS pelo Meu INSS,
  com conferência do CNIS, rol de documentos e cuidado com o interesse de agir
  (STF Tema 350; Lei 8.213/1991, arts. 29-A e 124-A). Use quando o usuário
  pedir requerimento no INSS, pedido administrativo, protocolo no Meu INSS,
  DER, acerto de CNIS, pedido de benefício antes da ação ou "dar entrada no INSS".
metadata:
  area: previdenciario
  tipo_peca: requerimento
  verificado_em: 2026-11-01
---
# Requerimento administrativo ao INSS

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: pedido inicial de qualquer benefício do RGPS ou do BPC; acerto ou inclusão de vínculos e remunerações no CNIS; pedido de revisão administrativa; juntada de documentos em exigência.
- Usar também quando o objetivo final é a ação judicial: o requerimento bem instruído é o que constitui o interesse de agir (STF Tema 350).
- Não usar para recorrer de indeferimento (ver `prev-recurso-crps`) nem para petição inicial judicial (ver as skills de benefício da área).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
1. Benefício pretendido e fato gerador (idade, tempo, incapacidade, óbito, deficiência).
2. CPF, NIT e acesso ao Meu INSS (ou procuração com poderes para representação administrativa).
3. Extrato CNIS atualizado e cópia das CTPS.
4. Períodos controvertidos: sem registro no CNIS, com indicador de pendência, especiais, rurais, militares, RPPS (CTC).
5. Data em que o segurado quer fixar a DER e se há requerimento anterior (número do benefício, data e motivo do indeferimento).

## Prazo e contagem
- Não há prazo para requerer benefício (STF Tema 313, item I: não há decadência para a concessão inicial). Mas a DER define o início dos efeitos financeiros em vários benefícios: pensão por morte (Lei 8.213, art. 74), aposentadoria por idade do empregado desligado (art. 49), benefícios por incapacidade requeridos após 30 dias do afastamento (art. 60, §1º).
- Decisão do INSS: Lei 9.784/1999, arts. 48 e 49 (dever de decidir; 30 dias após a instrução, prorrogáveis). A demora excessiva também caracteriza interesse de agir (Tema 350).
- Prazos de exigência: os fixados pelo INSS na carta; registrar a data de ciência.

## Estrutura da peça   (detalhe em [estrutura](references/estrutura.md))
1. Identificação do requerente e do procurador.
2. Benefício requerido e espécie.
3. Síntese dos fatos com períodos e documentos.
4. Pedido de acerto de CNIS (art. 29-A, §2º), se houver.
5. Pedido de reconhecimento de períodos especiais ou rurais, com indicação da prova.
6. Pedido de concessão do melhor benefício (Tema 334 STF) e de reafirmação da DER, se cabível.
7. Rol de documentos anexados.

## Requisitos e preliminares
- Requerimento pelo canal eletrônico do INSS (art. 124-A da Lei 8.213); anexar tudo em PDF legível, nomeado por período.
- Instruir com TODA a matéria de fato que se pretende discutir depois em juízo: o Tema 350 dispensa novo pedido em revisão ou restabelecimento, salvo se depender de fato ainda não levado ao INSS.
- CTPS sem defeito formal tem presunção relativa de veracidade mesmo fora do CNIS (TNU, Súmula 75): anexar a CTPS completa.

## Fundamentos verificados   (detalhe em [fundamentos](references/fundamentos.md))
- STF Tema 350 (RE 631.240): exigência de prévio requerimento; não confunde com exaurimento da via administrativa; exceções.
- Lei 8.213, art. 29-A: CNIS como base; direito de pedir inclusão, exclusão ou retificação com documentos.
- STF Tema 334: direito ao cálculo pelo quadro mais favorável.
- TNU, Súmula 75: CTPS sem defeito formal prova tempo de serviço.

## Pedidos e requerimentos
- Concessão do benefício X desde a DER.
- Acerto do CNIS nos períodos indicados.
- Reconhecimento de tempo especial/rural indicado, com justificação administrativa se houver prova testemunhal a produzir.
- Concessão do benefício mais vantajoso entre as regras aplicáveis e reafirmação da DER, se os requisitos se completarem no curso do processo.
- Emissão de carta de exigências específica, em vez de indeferimento, se faltar documento.

## Checklist pré-protocolo
- [ ] CNIS emitido há menos de 30 dias e comparado vínculo a vínculo com a CTPS.
- [ ] Indicadores de pendência (PEXT, IREM etc.) identificados e com documento para cada um.
- [ ] PPP/LTCAT anexados para todo período especial pretendido.
- [ ] Autodeclaração rural e documentos do art. 106 para período rural.
- [ ] Procuração e termo de representação assinados.
- [ ] Simulação das regras de aposentadoria anexada ou guardada no dossiê.
- [ ] Comprovante de protocolo salvo com número e DER.

## Erros a evitar
- Protocolar pedido genérico sem os documentos de fato: o juiz pode extinguir a ação futura por falta de interesse de agir quanto à matéria não submetida ao INSS.
- Deixar de pedir o acerto do CNIS, levando o INSS a calcular com remunerações ausentes.
- Perder a janela de 90/180 dias da pensão por morte (art. 74, I) por esperar documentos.
- Prometer prazo de análise ao cliente; o prazo legal é frequentemente descumprido.
- Citar o teto do RGPS de 2026 sem conferir a portaria interministerial vigente [VERIFICAR]. Salário mínimo de 2026: R$ 1.621,00 (Decreto 12.797/2025).

## Integração com o núcleo
- `prazos-processuais` para o controle das datas de exigência e de recurso.
- `verificacao-de-citacoes` para qualquer precedente acrescentado.
- `fidelidade-factual` para conferir períodos e datas contra o CNIS.
- `estilo-forense` para a redação final.
- `juros-e-correcao` não se aplica ao requerimento; usar na ação de cobrança de atrasados.

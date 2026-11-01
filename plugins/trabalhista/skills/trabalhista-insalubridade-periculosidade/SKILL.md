---
name: trabalhista-insalubridade-periculosidade
description: >
  Estrutura pedido ou defesa sobre adicional de insalubridade (CLT arts. 189-192)
  e de periculosidade (art. 193), com perícia obrigatória (art. 195), base de
  cálculo, não cumulação (art. 193 §2º), EPI e enquadramento em norma
  regulamentadora (Súmula 448 do TST). Use quando o usuário pedir adicional de
  insalubridade, adicional de periculosidade, perícia de insalubridade, NR-15,
  NR-16, agente químico, ruído, eletricidade, inflamáveis, motoboy, vigilante,
  limpeza de banheiro, quesitos periciais ou impugnação ao laudo.
metadata:
  area: trabalhista
  tipo_peca: inicial
  verificado_em: 2026-11-01
---
# Adicionais de insalubridade e periculosidade

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

## Quando usar / quando não usar
- Usar: pedido em reclamação (com `trabalhista-reclamacao`), defesa (com `trabalhista-contestacao`), quesitos periciais e impugnação ao laudo.
- Não usar para tempo especial no INSS (é matéria previdenciária, com regras próprias).

## Entradas mínimas (perguntar ao usuário o que faltar; nunca supor fatos)
- Função, setor, tarefas reais e tempo de exposição por jornada.
- Agentes: químicos, físicos (ruído, calor, frio), biológicos; inflamáveis, explosivos, energia elétrica, segurança patrimonial, motocicleta, trânsito.
- EPIs fornecidos (fichas de entrega com CA), treinamento, fiscalização do uso.
- PGR/PPRA, LTCAT, PCMSO, laudos anteriores, pagamento espontâneo do adicional.
- Norma coletiva sobre base de cálculo.

## Prazo e contagem
- Prescrição comum (CF art. 7º XXIX; CLT art. 11). Efeitos pecuniários a partir da inclusão da atividade nos quadros oficiais (art. 196).

## Estrutura da peça
Tópico próprio: atividade e agente; enquadramento na NR; ausência ou ineficácia de EPI; percentual e base; reflexos; pedido de perícia com quesitos. Roteiro em [estrutura](references/estrutura.md).

## Requisitos e preliminares
- **Insalubridade** (arts. 189-192): agente acima dos limites de tolerância fixados pelo Ministério do Trabalho; graus máximo, médio e mínimo — 40%, 20% e 10% (art. 192). Precisa estar na relação oficial; laudo sozinho não basta (Súmula 448 I). Limpeza de banheiros de uso público ou coletivo de grande circulação e coleta do respectivo lixo: grau máximo (Súmula 448 II).
- **Base de cálculo da insalubridade**: o art. 192 fala em salário mínimo; o salário mínimo não pode ser indexador nem ser substituído por decisão judicial (Súmula Vinculante 4 do STF). A Súmula 228 do TST (salário básico) teve sua aplicação questionada após a SV 4 [VERIFICAR situação da Súmula 228 no site do TST]. Verificar se há norma coletiva mais favorável.
- **Periculosidade** (art. 193): inflamáveis, explosivos, energia elétrica; segurança pessoal ou patrimonial; motocicleta (§4º); agentes de trânsito (III, Lei 14.684/2023); exceção dos tanques de combustível para consumo próprio de veículos (§5º, Lei 14.766/2023). Adicional de 30% sobre o salário-base, sem gratificações, prêmios ou PLR (§1º; Súmula 191 do TST para eletricitários). Exposição intermitente gera direito; eventual ou por tempo extremamente reduzido não (Súmula 364 I). Frentista: Súmula 39.
- **Não cumulação**: o empregado pode optar pelo adicional de insalubridade (art. 193 §2º).
- **EPI**: o simples fornecimento não exime; é preciso eliminar ou neutralizar e fiscalizar o uso (Súmula 289). Eliminação do risco faz cessar o adicional (art. 194).
- **Perícia obrigatória** (art. 195 §2º), por médico ou engenheiro do trabalho. Pagamento espontâneo do adicional de periculosidade torna o fato incontroverso e dispensa perícia (Súmula 453). Intermitência não afasta a insalubridade (Súmula 47).
- **Honorários periciais**: de quem sucumbe no objeto da perícia; para o beneficiário da gratuidade, observar a ADI 5766 (anotação no art. 790-B) e a vedação de adiantamento (§3º) [VERIFICAR alcance do acórdão].

## Fundamentos verificados
CLT arts. 189 a 196, 790-B; CF art. 7º XXIII; Súmulas 39, 47, 191, 289, 364, 448, 453 do TST; SV 4 do STF. Detalhes em [fundamentos](references/fundamentos.md).

## Pedidos e requerimentos
- Perícia técnica, com quesitos (ver estrutura).
- Adicional no grau/percentual apurado, desde a admissão (respeitada a prescrição), com reflexos em férias + 1/3, 13º, horas extras, aviso prévio e FGTS.
- Pedido de opção pelo mais vantajoso, se houver os dois.
- Correção e juros conforme `juros-e-correcao`.

## Checklist pré-protocolo
- [ ] Agente e anexo da NR identificados.
- [ ] Fichas de EPI pedidas em exibição (inicial) ou juntadas (defesa).
- [ ] Base de cálculo fundamentada (lei, norma coletiva, SV 4), sem citar a Súmula 228 sem conferir.
- [ ] Quesitos formulados.
- [ ] Pedido de opção entre adicionais quando ambos.
- [ ] Valor estimado (art. 840 §1º), ressalvando a dependência da perícia.

## Erros a evitar
- Pedir os dois adicionais cumulados.
- Usar o salário bruto com gratificações como base da periculosidade.
- Basear o pedido só em laudo sem enquadramento na relação oficial.
- Aceitar que EPI entregue, sem prova de eficácia e fiscalização, afasta o adicional.

## Integração com o núcleo
`juros-e-correcao`, `prazos-processuais`, `verificacao-de-citacoes`, `fidelidade-factual`, `estilo-forense`.

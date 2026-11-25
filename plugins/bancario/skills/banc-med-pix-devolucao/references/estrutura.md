# Roteiro — requerimento de MED e bloqueio (Pix)

1. **Destinatário.** Banco do pagador (SAC/aplicativo; se sem resposta, ouvidoria). Cópia ao banco recebedor, se identificado.
2. **Identificação.** Nome, CPF, agência e conta do cliente; procurador, se houver.
3. **Assunto.** "Solicitação de acionamento do Mecanismo Especial de Devolução (MED) e de bloqueio de recursos — Pix com fundada suspeita de fraude."
4. **Transações.** Tabela: data, hora, valor, ID/E2E, recebedor, instituição do recebedor, chave.
5. **Fatos.** Narrativa curta: como ocorreu, quando o cliente percebeu, primeiro aviso (canal, protocolo). Anexar BO.
6. **Fundamento.**
   - Regulamento anexo à Res. BCB 1/2020: MED para fundada suspeita de fraude ou falha operacional (art. 41-B); solicitação pelo banco do pagador, por meio do DICT, quando receber reclamação do usuário (art. 41-C, II, "a"); notificação de infração e bloqueio do valor ou do saldo disponível (art. 41-D); comunicação ao recebedor (art. 41-F).
   - Bloqueio cautelar pelo banco recebedor quando há suspeita de fraude (art. 39-B).
7. **Pedidos.**
   - Acionamento imediato do MED e abertura de notificação de infração para cada transação.
   - Informação, por escrito, do resultado e dos valores bloqueados e devolvidos.
   - Cópia dos registros e gravações do atendimento.
8. **Prazo e reserva.** Pedido de resposta no menor prazo; se a demanda for à ouvidoria, prazo de 10 dias úteis (Res. CMN 4.860/2020, art. 6º, § 2º). Ressalva de que o cliente adotará as medidas judiciais e administrativas cabíveis.
9. **Fecho.** Local, data, assinatura; lista de anexos.

## Depois do requerimento
- Sem resposta ou com recusa: reclamação no BC (`banc-reclamacao-bacen-e-ouvidoria`) e avaliação da ação (`banc-fraude-pix-e-transferencia-nao-autorizada`), na qual a demora ou a omissão no MED é fato relevante.

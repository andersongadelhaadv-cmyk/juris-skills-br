# Roteiro — requerimento de revisão e cancelamento de inscrição em dívida ativa

1. **Endereçamento.** Unidade da procuradoria responsável pela inscrição (PGFN, procuradoria do Estado ou do Município). Confira se o ente exige protocolo por portal eletrônico.
2. **Qualificação.** Requerente (devedor ou corresponsável), CPF/CNPJ, procurador com instrumento de mandato.
3. **Identificação da dívida.** Número da inscrição, da CDA, do processo administrativo de origem; se houver, número da execução fiscal, do protesto e das averbações.
4. **Síntese.** Uma frase: a inscrição X deve ser cancelada (ou retificada) porque...
5. **Fatos.** Linha do tempo: fato gerador, lançamento ou declaração, defesa administrativa, decisão definitiva, inscrição, notificação, protesto, ajuizamento. Tabela com datas.
6. **Fundamento do cancelamento** — escolha a hipótese:
   - **Crédito extinto antes da inscrição** (pagamento, compensação homologada, decisão administrativa ou judicial favorável): junte o comprovante e mostre que a inscrição não poderia existir.
   - **Exigibilidade suspensa na data da inscrição** (depósito, liminar, parcelamento, impugnação pendente): junte a prova da suspensão.
   - **Nulidade do termo de inscrição**: aponte o requisito do art. 2º, § 5º, da LEF ou do art. 202 do CTN que falta ou está errado e o prejuízo concreto à defesa. Fundamento legal ausente ou deficiente: Tema 1.350/STJ. Sujeito passivo errado: Súmula 392/STJ.
   - **Prescrição ou decadência**: indique as datas e remeta o cálculo a `trib-prescricao-intercorrente`.
7. **Do dever de controle de legalidade.** LEF art. 2º, § 3º: a própria procuradoria deve conferir certeza e liquidez; presunção relativa (CTN art. 204; LEF art. 3º).
8. **Pedidos.** Cancelamento total ou retificação; baixa de protesto, cadastros e averbações; manifestação nos autos da execução, se houver; certidão atualizada.
9. **Documentos.** CDA, extrato da dívida, comprovantes, decisões, procuração, atos societários (se o problema for de sujeito passivo).

## Mapa da via judicial (se o pedido for negado ou o prazo apertar)
| Situação | Via |
| --- | --- |
| Execução ajuizada, vício provado por documento, sem garantia | `trib-excecao-pre-executividade-fiscal` |
| Execução garantida ou tese com prova | `trib-embargos-a-execucao-fiscal` |
| Sem execução, discutir o crédito | `trib-acao-anulatoria` ou `trib-mandado-de-seguranca` |
| Precisa de certidão enquanto discute | `trib-garantia-antecipada-certidao` / `trib-certidao-negativa-cpen` |

# Fluxo de verificação e padrão de citação

## 1. Fluxo para precedentes
1. **Liste** todas as citações do texto (inclusive as que o usuário colou).
2. **Normalize**: tribunal + classe + número (ex.: "STJ REsp 2.199.164"; "Súmula 54 do STJ";
   "Tema 1191 do STF"). Para tema, sempre diga o tribunal.
3. **Verifique** uma a uma com `verificar_citacao`.
4. **Classifique** o estado e aplique a ação da tabela do SKILL.md.
5. **Leia a ementa** devolvida. Responda: o caso julgado tem os mesmos fatos relevantes?
   A tese decide a questão do usuário ou só tangencia? Há distinção a fazer?
6. **Vigência**: para súmula e tema, abra a `fonteUrl` e confira se há nota de
   cancelamento, revisão ou superação. A base avisa que não registra esse dado.
7. **Lacunas**: se faltar precedente para uma tese, use `buscar_jurisprudencia` com
   consulta descritiva (fatos + dispositivo) e filtro de tribunais. Prefira, nesta ordem:
   vinculantes (STF controle concentrado, súmula vinculante, repercussão geral, repetitivos,
   IRDR/IAC, relevância do REsp), súmulas, órgão especial ou seção, turmas, tribunal local.
8. **Registre**: em skill, no fontes.yaml (tipo, referência, status, url, data); em peça,
   numa lista de conferência ao final do rascunho, que o advogado apaga antes do protocolo.

## 2. Fluxo para normas
1. Identifique tipo, número e ano.
2. Consulte `https://legis.senado.leg.br/dadosabertos/legislacao/lista?tipo=<TIPO>&numero=<n>&ano=<aaaa>`
   (LEI, LCP, EMC, DEL, MPV). O campo `id` do documento é o código da norma.
3. Abra `https://legis.senado.leg.br/norma/<id>`: confira ementa, data, publicação,
   "normas posteriores" (o que alterou ou revogou) e a observação de vigência.
4. Para transcrever um dispositivo, abra o texto publicado ou a compilação vinculada
   na mesma página. Se houver alteração em 2024–2026, confira a redação nova e a data de
   produção de efeitos.
5. Fontes alternativas: portal da Câmara (legislação federal); texto compilado oficial.
   O portal do Planalto costuma bloquear acesso automatizado; não insista.
6. Se nada carregar: cite o dispositivo pelo número, sem transcrever, e marque
   [VERIFICAR: redação vigente].

## 3. Padrão de citação na peça
**Acórdão**: Tribunal, Órgão, Classe nº, Rel. Min./Des. Nome, julgado em dd/mm/aaaa
[, DJe dd/mm/aaaa, se a base informar]. Disponível em: <link>.
Ex.: STJ, Corte Especial, REsp 2.199.164, Rel. Min. Ricardo Villas Bôas Cueva, julgado em
15/10/2025 (Tema 1368). Disponível em: https://scon.stj.jus.br/SCON/GetInteiroTeorDoAcordao?num_registro=202500618396.

**Súmula**: Súmula nº do Tribunal: "texto literal". Link.

**Tema**: Tema nº do STF (repercussão geral) / do STJ (repetitivo), processo-paradigma,
tese literal entre aspas. Link.

**Lei**: art., §, inciso, alínea, da Lei nº/ano (nome usual na primeira menção). Ex.:
art. 406, §1º, do Código Civil (Lei 10.406/2002), com a redação da Lei 14.905/2024.

**Transcrição**: só o trecho que decide, entre aspas, com no máximo cinco linhas. Em
seguida, uma frase que liga o trecho ao caso.

## 4. Mensagens-padrão ao usuário
- NAO_ENCONTRADO: "Não localizei [citação] na base consultada. Isso não significa que
  não exista. Mantive a tese sem o número e marquei [VERIFICAR]. Se tiver o link ou o
  inteiro teor, envie para eu conferir."
- INDISPONIVEL: "A base não respondeu agora. Mantive [VERIFICAR] na citação; vou tentar de
  novo ou você pode conferir no site do tribunal."
- DIVERGENCIA: "A citação existe, mas [campo] é [valor real], não [valor informado].
  Corrigi no texto."
- Sem ferramentas: "Não tenho acesso à base de jurisprudência nesta sessão. Todas as
  citações estão marcadas [VERIFICAR] e precisam ser conferidas no site oficial."

## 5. Onde conferir manualmente
- STF: portal.stf.jus.br (jurisprudência, súmulas, repercussão geral).
- STJ: scon.stj.jus.br (acórdãos e súmulas); processo.stj.jus.br/repetitivos.
- TST: jurisprudencia.tst.jus.br (acórdãos, súmulas, OJs).
- TNU: cjf.jus.br (temas representativos).
- Tribunais locais: sistema de consulta de jurisprudência de cada TJ/TRF/TRT.

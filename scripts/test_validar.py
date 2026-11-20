#!/usr/bin/env python3
"""Testes do validador. Uso: python3 -m unittest scripts/test_validar.py"""
import contextlib
import datetime
import io
import pathlib
import sys
import tempfile
import textwrap
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import validar  # noqa: E402

HOJE = datetime.date(2026, 11, 20)

SKILL = """\
---
name: civel-teste
description: >
  Skill de teste usada pelo validador para conferir as travas. Use quando
  rodar os testes automatizados do repositório.
metadata:
  area: {area}
  verificado_em: {data}
---
# Teste

Ferramenta de apoio; o advogado responsável revisa toda peça antes do protocolo.

{corpo}
"""

FONTES_OK = """\
itens:
  - tipo: sumula
    referencia: "Súmula 302 do STJ"
    status: CONFIRMADO
    url: https://exemplo.gov.br/302
"""


class ValidadorTest(unittest.TestCase):
    def montar(self, corpo="Aplica a Súmula 302 do STJ.", fontes=FONTES_OK,
               area="processo-civil", data="2026-11-01", pendencias=None):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        raiz = pathlib.Path(tmp.name)
        pasta = raiz / "plugins/processo-civil/skills/civel-teste"
        (pasta / "references").mkdir(parents=True)
        (pasta / "SKILL.md").write_text(SKILL.format(area=area, data=data, corpo=corpo), encoding="utf-8")
        (pasta / "fontes.yaml").write_text(textwrap.dedent(fontes), encoding="utf-8")
        if pendencias is not None:
            (raiz / "scripts").mkdir()
            (raiz / validar.PENDENCIAS).write_text(pendencias, encoding="utf-8")
        return raiz

    def rodar(self, raiz, hoje=HOJE):
        saida = io.StringIO()
        with contextlib.redirect_stdout(saida):
            codigo = validar.validar(raiz, hoje)
        return codigo, saida.getvalue()

    def test_skill_correta_passa(self):
        codigo, saida = self.rodar(self.montar())
        self.assertEqual(codigo, 0, saida)

    def test_citacao_sem_registro_falha(self):
        codigo, saida = self.rodar(self.montar(corpo="Aplica o Tema 313 do STF."))
        self.assertEqual(codigo, 1)
        self.assertIn("Tema 313 citado no texto sem item", saida)

    def test_citacao_em_references_tambem_conta(self):
        raiz = self.montar()
        ref = raiz / "plugins/processo-civil/skills/civel-teste/references/fundamentos.md"
        ref.write_text("Ver REsp 2.001.973/RS, 3ª Seção.", encoding="utf-8")
        codigo, saida = self.rodar(raiz)
        self.assertEqual(codigo, 1)
        self.assertIn("REsp 2001973", saida)

    def test_lista_de_sumulas(self):
        codigo, saida = self.rodar(self.montar(corpo="Súmulas 302 e 608 do STJ."))
        self.assertEqual(codigo, 1)
        self.assertIn("Súmula 608", saida)
        self.assertNotIn("Súmula 302 citado", saida)

    def test_turma_nao_vira_numero(self):
        corpo = "Súmula 302 do STJ; REsp 2.034.650, 2ª Turma."
        fontes = FONTES_OK + '  - tipo: precedente\n    referencia: "REsp 2.034.650"\n    status: CONFIRMADO\n    url: https://x\n'
        codigo, saida = self.rodar(self.montar(corpo=corpo, fontes=fontes))
        self.assertEqual(codigo, 0, saida)

    def test_lista_de_adis_e_abreviacoes(self):
        corpo = "Súmula 302 do STJ; ADIs 7.156/7.236; SV 22; Súm. 162; Tema Repetitivo 905."
        codigo, saida = self.rodar(self.montar(corpo=corpo))
        self.assertEqual(codigo, 1)
        for esperado in ("ADI 7156", "ADI 7236", "SV 22", "Súmula 162", "Tema 905"):
            self.assertIn(esperado + " citado", saida)

    def test_codigo_civil_nao_e_citacao(self):
        codigo, saida = self.rodar(self.montar(corpo="Súmula 302 do STJ; CC 1.829."))
        self.assertEqual(codigo, 0, saida)

    def test_pendencia_conhecida_vira_aviso(self):
        raiz = self.montar(corpo="Súmula 302 do STJ e Tema 313 do STF.",
                           pendencias="# lacunas\ncivel-teste: Tema 313\n")
        codigo, saida = self.rodar(raiz)
        self.assertEqual(codigo, 0, saida)
        self.assertIn("1 citação(ões) pendente(s)", saida)

    def test_pendencia_resolvida_avisa_para_remover(self):
        raiz = self.montar(pendencias="civel-teste: Tema 313\n")
        codigo, saida = self.rodar(raiz)
        self.assertEqual(codigo, 0)
        self.assertIn("já resolvida", saida)

    def test_registro_verificar_sem_marcador_falha(self):
        fontes = FONTES_OK.replace("CONFIRMADO", "VERIFICAR")
        codigo, saida = self.rodar(self.montar(fontes=fontes))
        self.assertEqual(codigo, 1)
        self.assertIn("não traz nenhum marcador [VERIFICAR]", saida)

    def test_registro_verificar_com_marcador_passa(self):
        fontes = FONTES_OK.replace("CONFIRMADO", "VERIFICAR")
        corpo = "Aplica a Súmula 302 do STJ [VERIFICAR: vigência]."
        codigo, saida = self.rodar(self.montar(corpo=corpo, fontes=fontes))
        self.assertEqual(codigo, 0, saida)

    def test_validade_aviso_e_erro(self):
        raiz = self.montar(data="2026-11-01")
        codigo, saida = self.rodar(raiz, hoje=datetime.date(2027, 2, 15))
        self.assertEqual(codigo, 0)
        self.assertIn("AVISO", saida)
        codigo, saida = self.rodar(raiz, hoje=datetime.date(2027, 5, 15))
        self.assertEqual(codigo, 1)
        self.assertIn("vencido", saida)

    def test_area_volatil_vence_antes(self):
        raiz = self.montar(area="previdenciario", data="2026-11-01")
        codigo, saida = self.rodar(raiz, hoje=datetime.date(2027, 2, 15))
        self.assertEqual(codigo, 1)
        self.assertIn("limite 90", saida)

    def test_revisar_ate_vencido_falha(self):
        fontes = FONTES_OK + "    revisar_ate: 2026-11-10\n"
        codigo, saida = self.rodar(self.montar(fontes=fontes))
        self.assertEqual(codigo, 1)
        self.assertIn("revisar_ate 2026-11-10 vencido", saida)

    def test_revisar_ate_futuro_passa(self):
        fontes = FONTES_OK + "    revisar_ate: 2027-03-01\n"
        codigo, saida = self.rodar(self.montar(fontes=fontes))
        self.assertEqual(codigo, 0, saida)


if __name__ == "__main__":
    unittest.main()

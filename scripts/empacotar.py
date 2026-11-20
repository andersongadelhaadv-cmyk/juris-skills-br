#!/usr/bin/env python3
"""Gera os arquivos de venda em dist/ (fora do git).

Saídas:
  dist/juris-skills-br-completo-<versao>.zip
      LEIA-ME.md + skills/<area>/<skill>.zip para todas as skills,
      com o núcleo em skills/0-nucleo/ (instalar primeiro).
  dist/avulsas/<skill>-<versao>.zip
      LEIA-ME.md + a skill comprada + as skills do núcleo, das quais
      todas as skills de área dependem (juros, prazos, citações).

Cada <skill>.zip interno segue o formato de envio de skill no app do
Claude: a pasta da skill na raiz do zip, com SKILL.md, references/ e
fontes.yaml.

Uso: python3 scripts/empacotar.py [--saida PASTA] [--somente SKILL ...]
O validador roda antes; com erro, nada é gerado.
"""
import argparse
import io
import pathlib
import re
import shutil
import subprocess
import sys
import zipfile

RAIZ = pathlib.Path(__file__).resolve().parent.parent
NUCLEO = "nucleo"
# Data fixa nas entradas: o mesmo conteúdo gera o mesmo zip.
DATA_ZIP = (2026, 1, 1, 0, 0, 0)

LEIA_ME = """\
# {titulo}

Versão {versao}. Skills jurídicas brasileiras para o Claude.

Ferramenta de apoio: o advogado responsável revisa toda peça antes do protocolo.

## Conteúdo

{conteudo}

## Como instalar no app do Claude (web, desktop ou celular)

1. Em Configurações > Capacidades, ative "Execução de código e criação de arquivos".
2. Em Skills, use "Enviar skill" e envie **um zip por vez**, sem descompactar.
3. Envie primeiro as skills do núcleo ({n_nucleo} arquivos em `{pasta_nucleo}`).
   As skills de área usam o núcleo para juros, prazos e verificação de citações.
4. Depois envie as skills das áreas que você usa. Não precisa enviar todas.

## Como instalar no Claude Code

```
/plugin marketplace add andersongadelhaadv-cmyk/juris-skills-br
/plugin install nucleo@juris-skills-br
```

## Atualizações

Cada skill traz um `fontes.yaml` com a norma ou o precedente, o link oficial e a
data da consulta. O que não pôde ser confirmado aparece no texto como `[VERIFICAR]`.
Quando sair uma versão nova, envie de novo os zips das skills que mudaram: o app
substitui a skill de mesmo nome.
"""


def versao():
    for linha in (RAIZ / "CHANGELOG.md").read_text(encoding="utf-8").splitlines():
        m = re.match(r"^## (v\d+\.\d+\.\d+)", linha)
        if m:
            return m.group(1)
    sys.exit("ERRO versão não encontrada no CHANGELOG.md")


def skills_por_area():
    areas = {}
    for sk in sorted(RAIZ.glob("plugins/*/skills/*/SKILL.md")):
        area = sk.parts[-4]
        areas.setdefault(area, []).append(sk.parent)
    return areas


def _escrever(zf, nome, dados):
    info = zipfile.ZipInfo(nome, date_time=DATA_ZIP)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = 0o644 << 16
    zf.writestr(info, dados)


def zip_da_skill(pasta):
    """Bytes do zip de uma skill: pasta <nome>/ na raiz."""
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as zf:
        for arq in sorted(p for p in pasta.rglob("*") if p.is_file()):
            if "__pycache__" in arq.parts or arq.name.startswith("."):
                continue
            _escrever(zf, f"{pasta.name}/{arq.relative_to(pasta).as_posix()}", arq.read_bytes())
    return buf.getvalue()


def gravar_pacote(destino, titulo, ver, grupos):
    """grupos: lista de (pasta_no_zip, [pastas de skill])."""
    linhas = []
    for pasta_zip, skills in grupos:
        linhas.append(f"- `{pasta_zip}/`: " + ", ".join(f"`{s.name}`" for s in skills))
    nucleo = next((g for g in grupos if g[0].endswith(NUCLEO)), None)
    leia = LEIA_ME.format(titulo=titulo, versao=ver, conteudo="\n".join(linhas),
                          n_nucleo=len(nucleo[1]) if nucleo else 0,
                          pasta_nucleo=nucleo[0] if nucleo else "-")
    destino.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(destino, "w") as zf:
        _escrever(zf, "LEIA-ME.md", leia)
        for pasta_zip, skills in grupos:
            for s in skills:
                _escrever(zf, f"{pasta_zip}/{s.name}.zip", zip_da_skill(s))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--saida", default=str(RAIZ / "dist"))
    ap.add_argument("--somente", nargs="*", help="gerar avulsas só destas skills")
    args = ap.parse_args()

    r = subprocess.run([sys.executable, str(RAIZ / "scripts/validar.py")], capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stdout)
        sys.exit("ERRO o validador falhou; nada foi gerado")

    ver = versao()
    saida = pathlib.Path(args.saida)
    if saida.exists():
        shutil.rmtree(saida)
    areas = skills_por_area()
    if NUCLEO not in areas:
        sys.exit("ERRO plugin nucleo não encontrado")
    nucleo = areas[NUCLEO]
    pasta_nucleo = f"skills/0-{NUCLEO}"

    grupos = [(pasta_nucleo, nucleo)] + [(f"skills/{a}", s) for a, s in sorted(areas.items()) if a != NUCLEO]
    total = sum(len(s) for _, s in grupos)
    completo = saida / f"juris-skills-br-completo-{ver}.zip"
    gravar_pacote(completo, f"juris-skills-br — pacote completo ({total} skills)", ver, grupos)

    nomes_nucleo = {s.name for s in nucleo}
    avulsas = 0
    for area, skills in sorted(areas.items()):
        if area == NUCLEO:
            continue
        for s in skills:
            if args.somente and s.name not in args.somente:
                continue
            gravar_pacote(saida / "avulsas" / f"{s.name}-{ver}.zip",
                          f"juris-skills-br — {s.name} (com o núcleo)", ver,
                          [(pasta_nucleo, nucleo), (f"skills/{area}", [s])])
            avulsas += 1
    assert not (nomes_nucleo & {p.stem for p in (saida / "avulsas").glob("*")}), "núcleo vendido como avulsa"
    print(f"{completo.relative_to(saida.parent)}: {total} skills")
    print(f"{avulsas} avulsas em {(saida / 'avulsas').relative_to(saida.parent)}/ (cada uma com o núcleo)")


if __name__ == "__main__":
    main()

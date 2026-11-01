#!/usr/bin/env python3
"""Validador do repositório juris-skills-br.

Checa, em todas as skills:
  1. frontmatter: name em kebab-case (<= 64), único, igual ao nome da pasta;
     description presente (>= 60 caracteres, com gatilho "Use quando").
  2. metadata obrigatória: area, verificado_em (AAAA-MM-DD).
  3. fontes.yaml presente, com a lista "itens" e cada item com
     tipo, referencia, status e url.
  4. status permitido: CONFIRMADO, DIVERGENCIA_CORRIGIDA, VERIFICAR, LEI.
  5. links relativos (references/..., ../...) apontam para arquivos que existem.
  6. SKILL.md com no máximo 200 linhas.
  7. aviso de responsabilidade presente no corpo.

Uso: python3 scripts/validar.py [--nomes ARQUIVO]
  --nomes: arquivo opcional (local, fora do repositório) com termos que não
           podem aparecer em nenhum arquivo versionado.
Sai com código 1 se houver erro.
"""
import argparse
import pathlib
import re
import sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent
NOME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
DATA_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
STATUS_OK = {"CONFIRMADO", "DIVERGENCIA_CORRIGIDA", "VERIFICAR", "LEI"}
AVISO = "o advogado responsável revisa"
LINK_RE = re.compile(r"\]\(((?:\.\./|references/|\./)[^)#\s]+)")


def ler_frontmatter(texto):
    if not texto.startswith("---\n"):
        return None, texto
    fim = texto.find("\n---", 4)
    if fim < 0:
        return None, texto
    bruto = texto[4:fim]
    corpo = texto[fim + 4:]
    dados, chave_atual, bloco = {}, None, []
    meta = {}
    em_meta = False
    for linha in bruto.splitlines():
        if re.match(r"^[a-z_]+:", linha):
            if chave_atual and bloco:
                dados[chave_atual] = " ".join(b.strip() for b in bloco).strip()
            chave, _, valor = linha.partition(":")
            chave_atual, bloco = chave.strip(), []
            em_meta = chave_atual == "metadata"
            valor = valor.strip()
            if valor in (">", "|", ">-", "|-"):
                continue
            if valor:
                dados[chave_atual] = valor.strip('"').strip("'")
                chave_atual = None
        elif em_meta and re.match(r"^\s+[a-z_]+:", linha):
            k, _, v = linha.strip().partition(":")
            meta[k.strip()] = v.strip().strip('"').strip("'")
        elif chave_atual:
            bloco.append(linha)
    if chave_atual and bloco:
        dados[chave_atual] = " ".join(b.strip() for b in bloco).strip()
    dados["metadata"] = meta
    return dados, corpo


def ler_fontes(caminho):
    """Leitor mínimo de fontes.yaml (lista de dicionários em 'itens')."""
    itens, atual = [], None
    for linha in caminho.read_text(encoding="utf-8").splitlines():
        if not linha.strip() or linha.lstrip().startswith("#"):
            continue
        m = re.match(r"^\s*-\s+([a-z_]+):\s*(.*)$", linha)
        if m:
            atual = {m.group(1): m.group(2).strip().strip('"')}
            itens.append(atual)
            continue
        m = re.match(r"^\s+([a-z_]+):\s*(.*)$", linha)
        if m and atual is not None:
            atual[m.group(1)] = m.group(2).strip().strip('"')
    return itens


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--nomes", help="arquivo local com termos proibidos")
    args = ap.parse_args()

    erros, nomes_vistos = [], {}
    skills = sorted(RAIZ.glob("plugins/*/skills/*/SKILL.md"))
    if not skills:
        erros.append("nenhuma skill encontrada")

    for sk in skills:
        rel = sk.relative_to(RAIZ)
        texto = sk.read_text(encoding="utf-8")
        fm, corpo = ler_frontmatter(texto)
        if fm is None:
            erros.append(f"{rel}: sem frontmatter")
            continue
        nome = fm.get("name", "")
        if not NOME_RE.match(nome) or len(nome) > 64:
            erros.append(f"{rel}: name inválido '{nome}'")
        if nome != sk.parent.name:
            erros.append(f"{rel}: name '{nome}' difere da pasta '{sk.parent.name}'")
        if nome in nomes_vistos:
            erros.append(f"{rel}: name duplicado (também em {nomes_vistos[nome]})")
        nomes_vistos[nome] = rel
        desc = fm.get("description", "")
        if len(desc) < 60 or "use quando" not in desc.lower():
            erros.append(f"{rel}: description curta ou sem gatilho 'Use quando'")
        meta = fm.get("metadata", {})
        if not meta.get("area"):
            erros.append(f"{rel}: metadata.area ausente")
        if not DATA_RE.match(meta.get("verificado_em", "")):
            erros.append(f"{rel}: metadata.verificado_em ausente ou inválido")
        if AVISO not in corpo.lower():
            erros.append(f"{rel}: aviso de responsabilidade ausente")
        if texto.count("\n") + 1 > 200:
            erros.append(f"{rel}: mais de 200 linhas")
        for alvo in LINK_RE.findall(texto):
            if not (sk.parent / alvo).resolve().exists():
                erros.append(f"{rel}: link quebrado '{alvo}'")
        for ref in sk.parent.glob("references/*.md"):
            for alvo in LINK_RE.findall(ref.read_text(encoding="utf-8")):
                if not (ref.parent / alvo).resolve().exists():
                    erros.append(f"{ref.relative_to(RAIZ)}: link quebrado '{alvo}'")
        fontes = sk.parent / "fontes.yaml"
        if not fontes.exists():
            erros.append(f"{rel}: fontes.yaml ausente")
        else:
            itens = ler_fontes(fontes)
            if not itens:
                erros.append(f"{fontes.relative_to(RAIZ)}: sem itens")
            for i, it in enumerate(itens):
                for campo in ("tipo", "referencia", "status", "url"):
                    if not it.get(campo):
                        erros.append(f"{fontes.relative_to(RAIZ)}[{i}]: campo '{campo}' ausente")
                if it.get("status") and it["status"] not in STATUS_OK:
                    erros.append(f"{fontes.relative_to(RAIZ)}[{i}]: status inválido '{it['status']}'")

    if args.nomes:
        termos = [t.strip() for t in pathlib.Path(args.nomes).read_text(encoding="utf-8").splitlines() if t.strip()]
        padroes = [re.compile(r"(?<![\w-])" + re.escape(t) + r"(?![\w-])", re.I) for t in termos]
        for arq in RAIZ.rglob("*"):
            if arq.is_dir() or ".git" in arq.parts:
                continue
            try:
                conteudo = arq.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            for t, p in zip(termos, padroes):
                if p.search(conteudo) or p.search(str(arq.relative_to(RAIZ))):
                    erros.append(f"{arq.relative_to(RAIZ)}: termo proibido encontrado")
                    break

    for e in erros:
        print("ERRO", e)
    print(f"{len(skills)} skills verificadas, {len(erros)} erro(s)")
    sys.exit(1 if erros else 0)


if __name__ == "__main__":
    main()

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
  8. toda súmula, tema, ADI/ADC/ADPF e processo (REsp, RE, HC...) citado no
     SKILL.md ou em references/ tem item correspondente no fontes.yaml.
     Lacunas já conhecidas ficam em scripts/pendencias-citacoes.txt; só
     lacuna nova falha.
  9. item com status VERIFICAR no fontes.yaml exige marcador [VERIFICAR]
     no texto da skill (o registro não pode duvidar e o texto afirmar).
 10. validade: verificado_em com mais de 90 dias gera aviso e com mais de
     180 dias gera erro (metade disso em previdenciario e tributario-fazenda).
     Item do fontes.yaml com revisar_ate vencido gera erro.

Uso: python3 scripts/validar.py [--nomes ARQUIVO] [--raiz PASTA] [--hoje AAAA-MM-DD]
  --nomes: arquivo opcional (local, fora do repositório) com termos que não
           podem aparecer em nenhum arquivo versionado.
  --raiz:  raiz do repositório (padrão: a pasta acima de scripts/).
  --hoje:  data de referência para a validade (padrão: hoje).
Sai com código 1 se houver erro. Avisos não alteram o código de saída.
"""
import argparse
import datetime
import pathlib
import re
import sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent
NOME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
DATA_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
STATUS_OK = {"CONFIRMADO", "DIVERGENCIA_CORRIGIDA", "VERIFICAR", "LEI"}
AVISO = "o advogado responsável revisa"
LINK_RE = re.compile(r"\]\(((?:\.\./|references/|\./)[^)#\s]+)")
PENDENCIAS = "scripts/pendencias-citacoes.txt"

# Validade, em dias: (aviso, erro). Áreas que mudam rápido têm metade do prazo.
VALIDADE_PADRAO = (90, 180)
VALIDADE_AREA = {"previdenciario": (45, 90), "tributario-fazenda": (45, 90)}

# Citações conferidas pelo item 8. "CC" fica de fora de propósito: no texto
# quase sempre é o Código Civil, não conflito de competência.
_CLASSE = (r"([Ss][úu]m(?:ulas?|\.)(?:\s+[Vv]inculantes?)?|SV|[Tt]emas?(?:\s+[Rr]epetitivos?)?|"
           r"REsp|AREsp|EREsp|EAREsp|RE|ARE|HC|RHC|ADIs?|ADCs?|ADPFs?|RMS)")
_NUM = r"(\d{1,3}(?:\.\d{3})+|\d+)(?![\d\wªº°])"
CITACAO_RE = re.compile(r"(?<![\w/])" + _CLASSE + r"\s+(?:n\.?\s*[º°]\s*|n\.\s*)?" + _NUM
                        + r"((?:\s*(?:,|e|/)\s*" + _NUM + r")*)")
# Classes em que "1.234, 5.678 e 9.012" ou "7.156/7.236" é lista de números.
# Em processo (REsp, HC...) não: "/SP" e ", 2ª Turma" seguem o número.
_COM_LISTA = ("Súmula", "SV", "Tema", "ADI", "ADC", "ADPF")


def _classe(bruta):
    b = bruta.lower().replace("ú", "u").split()[0]
    if b.startswith("sum"):
        return "SV" if "vinc" in bruta.lower() else "Súmula"
    if b == "sv":
        return "SV"
    b = {"temas": "tema", "adis": "adi", "adcs": "adc", "adpfs": "adpf"}.get(b, b)
    nomes = {"tema": "Tema", "resp": "REsp", "aresp": "AREsp", "eresp": "EREsp", "earesp": "EAREsp"}
    return nomes.get(b, b.upper())


def citacoes(texto):
    """Conjunto de (classe, número) citados no texto."""
    achadas = set()
    for m in CITACAO_RE.finditer(texto):
        classe = _classe(m.group(1))
        numeros = [m.group(2)]
        if classe in _COM_LISTA:
            numeros += re.findall(r"\d{1,3}(?:\.\d{3})+|\d+", m.group(3) or "")
        for n in numeros:
            achadas.add((classe, n.replace(".", "")))
    return achadas


def ler_pendencias(raiz):
    """Lacunas conhecidas: linhas 'skill: Classe Número'. Comentários com #."""
    arq = raiz / PENDENCIAS
    pend = set()
    if not arq.exists():
        return pend
    for linha in arq.read_text(encoding="utf-8").splitlines():
        linha = linha.split("#", 1)[0].strip()
        if not linha:
            continue
        skill, _, cit = linha.partition(":")
        partes = cit.split()
        if len(partes) == 2:
            pend.add((skill.strip(), partes[0], partes[1]))
    return pend


def _data(valor):
    try:
        return datetime.date.fromisoformat(valor)
    except ValueError:
        return None


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
    ap.add_argument("--raiz", help="raiz do repositório")
    ap.add_argument("--hoje", help="data de referência AAAA-MM-DD")
    args = ap.parse_args()
    raiz = pathlib.Path(args.raiz).resolve() if args.raiz else RAIZ
    hoje = _data(args.hoje) if args.hoje else datetime.date.today()
    if hoje is None:
        print("ERRO --hoje inválido")
        sys.exit(2)
    sys.exit(validar(raiz, hoje, args.nomes))


def validar(raiz, hoje, nomes=None):
    RAIZ = raiz
    erros, avisos, nomes_vistos = [], [], {}
    pendencias = ler_pendencias(RAIZ)
    pendencias_usadas = set()
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
        verificado = _data(meta.get("verificado_em", "")) if DATA_RE.match(meta.get("verificado_em", "")) else None
        if verificado is None:
            erros.append(f"{rel}: metadata.verificado_em ausente ou inválido")
        else:
            aviso_dias, erro_dias = VALIDADE_AREA.get(meta.get("area", ""), VALIDADE_PADRAO)
            idade = (hoje - verificado).days
            if idade > erro_dias:
                erros.append(f"{rel}: verificado_em {verificado} vencido "
                             f"({idade} dias; limite {erro_dias}) — reconferir as fontes")
            elif idade > aviso_dias:
                avisos.append(f"{rel}: verificado_em {verificado} com {idade} dias "
                              f"(reconferir até {verificado + datetime.timedelta(days=erro_dias)})")
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
        textos = [corpo] + [r.read_text(encoding="utf-8")
                            for r in sorted(sk.parent.glob("references/*.md"))]
        texto_skill = "\n".join(textos)
        fontes = sk.parent / "fontes.yaml"
        if not fontes.exists():
            erros.append(f"{rel}: fontes.yaml ausente")
        else:
            bruto_fontes = fontes.read_text(encoding="utf-8")
            registradas = citacoes(bruto_fontes)
            for classe, numero in sorted(citacoes(texto_skill) - registradas):
                chave = (nome, classe, numero)
                if chave in pendencias:
                    pendencias_usadas.add(chave)
                else:
                    erros.append(f"{rel}: {classe} {numero} citado no texto sem item no fontes.yaml")
            itens = ler_fontes(fontes)
            if any(it.get("status") == "VERIFICAR" for it in itens) and "[VERIFICAR" not in texto_skill:
                erros.append(f"{fontes.relative_to(RAIZ)}: há item VERIFICAR, mas o texto da skill "
                             f"não traz nenhum marcador [VERIFICAR]")
            for i, it in enumerate(itens):
                if "revisar_ate" in it:
                    limite = _data(it["revisar_ate"])
                    if limite is None:
                        erros.append(f"{fontes.relative_to(RAIZ)}[{i}]: revisar_ate inválido '{it['revisar_ate']}'")
                    elif limite < hoje:
                        erros.append(f"{fontes.relative_to(RAIZ)}[{i}]: revisar_ate {limite} vencido "
                                     f"({it.get('referencia', '')[:60]})")
            if not itens:
                erros.append(f"{fontes.relative_to(RAIZ)}: sem itens")
            for i, it in enumerate(itens):
                for campo in ("tipo", "referencia", "status", "url"):
                    if not it.get(campo):
                        erros.append(f"{fontes.relative_to(RAIZ)}[{i}]: campo '{campo}' ausente")
                if it.get("status") and it["status"] not in STATUS_OK:
                    erros.append(f"{fontes.relative_to(RAIZ)}[{i}]: status inválido '{it['status']}'")

    for skill, classe, numero in sorted(pendencias - pendencias_usadas):
        avisos.append(f"{PENDENCIAS}: '{skill}: {classe} {numero}' já resolvida — remova a linha")
    if pendencias_usadas:
        avisos.append(f"{len(pendencias_usadas)} citação(ões) pendente(s) de registro em {PENDENCIAS}")

    if nomes:
        termos = [t.strip() for t in pathlib.Path(nomes).read_text(encoding="utf-8").splitlines() if t.strip()]
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

    for a in avisos:
        print("AVISO", a)
    for e in erros:
        print("ERRO", e)
    print(f"{len(skills)} skills verificadas, {len(erros)} erro(s), {len(avisos)} aviso(s)")
    return 1 if erros else 0


if __name__ == "__main__":
    main()

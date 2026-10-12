"""Inventário inicial dos dados brutos; não modifica arquivos de entrada."""
from pathlib import Path
import csv
import re

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
OUT = ROOT / "results" / "tables" / "data_inventory.csv"

def inspect_arff(path):
    attrs, relation, n = [], "", 0
    try:
        with path.open("r", encoding="utf-8-sig", errors="replace") as f:
            in_data = False
            for line in f:
                s = line.strip()
                if not s or s.startswith("%"):
                    continue
                if s.lower().startswith("@relation"):
                    relation = s[len("@relation"):].strip()
                elif s.lower().startswith("@attribute"):
                    attrs.append(s)
                elif s.lower() == "@data":
                    in_data = True
                elif in_data and not s.startswith("%"):
                    n += 1
        return relation, len(attrs), n, " | ".join(attrs)
    except OSError as e:
        return "", 0, 0, f"ERRO: {e}"

def inspect_csv(path):
    # Arquivos enviados incluem CSV separado por ponto e vírgula.
    for enc in ("utf-8-sig", "latin-1"):
        try:
            with path.open("r", encoding=enc, newline="") as f:
                sample = f.read(4096)
                f.seek(0)
                try:
                    dialect = csv.Sniffer().sniff(sample, delimiters=",;\t")
                except csv.Error:
                    dialect = csv.excel
                reader = csv.reader(f, dialect)
                header = next(reader, [])
                rows = sum(1 for row in reader if row)
            return len(header), rows, dialect.delimiter, " | ".join(header)
        except UnicodeDecodeError:
            continue
    return 0, 0, "", "Não foi possível ler cabeçalho"

def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    rows = []
    for p in sorted(RAW.rglob("*")):
        if not p.is_file():
            continue
        rec = {"arquivo": p.relative_to(ROOT).as_posix(), "bytes": p.stat().st_size,
               "formato": p.suffix.lower(), "relacao_arff": "", "atributos": "",
               "registros_estimados": "", "separador_csv": "", "cabecalho": ""}
        if p.suffix.lower() == ".arff":
            relation, count, n, attrs = inspect_arff(p)
            rec.update(relacao_arff=relation, atributos=count, registros_estimados=n, cabecalho=attrs)
        elif p.suffix.lower() == ".csv":
            count, n, delim, header = inspect_csv(p)
            rec.update(atributos=count, registros_estimados=n, separador_csv=repr(delim), cabecalho=header)
        elif p.suffix.lower() == ".txt":
            try:
                with p.open("r", encoding="utf-8-sig", errors="replace") as f:
                    lines = sum(1 for _ in f)
                rec["registros_estimados"] = f"{lines} linhas (não interpretadas)"
            except OSError:
                pass
        rows.append(rec)
    fields = ["arquivo", "bytes", "formato", "relacao_arff", "atributos", "registros_estimados", "separador_csv", "cabecalho"]
    with OUT.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader(); w.writerows(rows)
    print(f"Arquivos encontrados: {len(rows)}")
    print(f"Inventário salvo em: {OUT.relative_to(ROOT)}")
    for r in rows:
        print(f"- {r['arquivo']} ({r['bytes']} bytes; atributos={r['atributos']}; registros={r['registros_estimados']})")

if __name__ == "__main__":
    main()

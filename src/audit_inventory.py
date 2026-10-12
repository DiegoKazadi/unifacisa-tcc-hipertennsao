from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
DATA_RAW = ROOT / "data" / "raw"
OUT = ROOT / "results" / "tables" / "inventario_arquivos.csv"
OUT.parent.mkdir(parents=True, exist_ok=True)

rows = []
for path in sorted(DATA_RAW.rglob("*")):
    if path.is_file():
        rows.append({
            "arquivo": path.relative_to(ROOT).as_posix(),
            "extensao": path.suffix.lower() or "(sem extensão)",
            "tamanho_bytes": path.stat().st_size,
        })

with OUT.open("w", newline="", encoding="utf-8-sig") as f:
    writer = csv.DictWriter(f, fieldnames=["arquivo", "extensao", "tamanho_bytes"])
    writer.writeheader()
    writer.writerows(rows)

print(f"Arquivos inventariados: {len(rows)}")
print(f"Saída: {OUT.relative_to(ROOT).as_posix()}")

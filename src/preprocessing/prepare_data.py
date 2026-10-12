"""Inspeciona e prepara um CSV após a variável-alvo ser confirmada.

Este script não escolhe automaticamente a variável-alvo: isso evita treinar
um modelo para doença cardíaca quando o objetivo declarado é hipertensão.
"""
from pathlib import Path
import argparse
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, help="Caminho do CSV relativo à raiz ou absoluto")
    parser.add_argument("--target", required=True, help="Nome EXATO da coluna-alvo confirmada no TCC")
    parser.add_argument("--output", default="data/processed/dataset_preparado.csv")
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.is_absolute():
        input_path = ROOT / input_path
    output_path = Path(args.output)
    if not output_path.is_absolute():
        output_path = ROOT / output_path

    if not input_path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {input_path}")

    df = pd.read_csv(input_path)
    print(f"Arquivo: {input_path}")
    print(f"Dimensões: {df.shape[0]} linhas x {df.shape[1]} colunas")
    print("Colunas:", df.columns.tolist())

    if args.target not in df.columns:
        raise ValueError(
            f"A coluna-alvo '{args.target}' não existe. "
            f"Colunas disponíveis: {df.columns.tolist()}"
        )

    print("\nDistribuição da variável-alvo:")
    print(df[args.target].value_counts(dropna=False))
    print("\nValores ausentes por coluna:")
    print(df.isna().sum().sort_values(ascending=False))

    output_path.parent.mkdir(parents=True, exist_ok=True)
    # Salva uma cópia sem alterar os valores; limpeza será definida na metodologia.
    df.to_csv(output_path, index=False)
    print(f"\nCópia de trabalho salva em: {output_path.relative_to(ROOT) if output_path.is_relative_to(ROOT) else output_path}")

if __name__ == "__main__":
    main()

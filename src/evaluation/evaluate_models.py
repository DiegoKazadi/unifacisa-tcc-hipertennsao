"""Funções genéricas para avaliar classificadores após o treinamento."""
from pathlib import Path
import pandas as pd
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, classification_report
)

def evaluate_predictions(y_true, y_pred, model_name="modelo", positive_label=None):
    """Retorna métricas e matriz de confusão; não treina nenhum modelo."""
    labels = sorted(set(y_true) | set(y_pred), key=str)
    if positive_label is not None and positive_label in labels:
        precision = precision_score(y_true, y_pred, pos_label=positive_label, zero_division=0)
        recall = recall_score(y_true, y_pred, pos_label=positive_label, zero_division=0)
        f1 = f1_score(y_true, y_pred, pos_label=positive_label, zero_division=0)
    else:
        precision = precision_score(y_true, y_pred, average="weighted", zero_division=0)
        recall = recall_score(y_true, y_pred, average="weighted", zero_division=0)
        f1 = f1_score(y_true, y_pred, average="weighted", zero_division=0)

    result = {
        "modelo": model_name,
        "acuracia": accuracy_score(y_true, y_pred),
        "precisao": precision,
        "sensibilidade_ou_recall": recall,
        "f1": f1,
    }
    matrix = confusion_matrix(y_true, y_pred, labels=labels)
    matrix_df = pd.DataFrame(
        matrix,
        index=[f"real_{label}" for label in labels],
        columns=[f"predito_{label}" for label in labels],
    )
    return result, matrix_df

def save_results(metrics, confusion, output_dir="results/tables", prefix="experimento"):
    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)
    pd.DataFrame([metrics]).to_csv(output / f"{prefix}_metricas.csv", index=False)
    confusion.to_csv(output / f"{prefix}_matriz_confusao.csv", index=True)
    print(f"Resultados salvos em: {output}")

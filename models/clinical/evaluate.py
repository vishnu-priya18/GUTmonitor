import os
import sys
import json
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, precision_recall_fscore_support

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from models.clinical.config import RESULTS_DIR, RISK_LEVEL_NAMES

def evaluate_clinical_model(pipeline, X_test, y_test, feature_names, importances):
    print("Evaluating Clinical Model on Test Set...")
    y_pred = pipeline.predict(X_test)
    
    acc = accuracy_score(y_test, y_pred)
    precision, recall, f1, _ = precision_recall_fscore_support(y_test, y_pred, average='macro', zero_division=0)
    
    report = classification_report(y_test, y_pred, target_names=RISK_LEVEL_NAMES, output_dict=True, zero_division=0)
    cm = confusion_matrix(y_test, y_pred)
    
    metrics = {
        "dataset": "Gastrointestinal Symptoms & Lifestyle Dataset (1,000 patient records)",
        "num_test_samples": len(X_test),
        "accuracy": round(float(acc), 4),
        "precision_macro": round(float(precision), 4),
        "recall_macro": round(float(recall), 4),
        "f1_macro": round(float(f1), 4),
        "classes": RISK_LEVEL_NAMES,
        "confusion_matrix": cm.tolist(),
        "classification_report": report
    }
    
    metrics_path = os.path.join(RESULTS_DIR, "metrics.json")
    with open(metrics_path, "w") as f:
        json.dump(metrics, f, indent=2)
        
    plt.figure(figsize=(6, 5))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Purples', xticklabels=RISK_LEVEL_NAMES, yticklabels=RISK_LEVEL_NAMES)
    plt.title("Clinical Tabular Model Test Confusion Matrix")
    plt.ylabel("Actual Risk")
    plt.xlabel("Predicted Risk")
    plt.tight_layout()
    plt.savefig(os.path.join(RESULTS_DIR, "confusion_matrix.png"), dpi=150)
    plt.close()
    
    indices = np.argsort(importances)[::-1][:10]
    top_features = [feature_names[i] for i in indices]
    top_importances = [importances[i] for i in indices]
    
    plt.figure(figsize=(8, 5))
    sns.barplot(x=top_importances, y=top_features, palette="viridis")
    plt.title("Top 10 Clinical & Lifestyle Feature Importances")
    plt.xlabel("Gini Importance")
    plt.tight_layout()
    plt.savefig(os.path.join(RESULTS_DIR, "feature_importance.png"), dpi=150)
    plt.close()
    
    print(f"Clinical Model Metrics saved to {metrics_path}")
    print(f"Test Accuracy: {acc*100:.2f}% | Macro F1: {f1:.4f}")
    return metrics

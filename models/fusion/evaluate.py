import os
import sys
import json
import torch
import matplotlib.pyplot as plt
import seaborn as sns
from torch.utils.data import DataLoader
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, precision_recall_fscore_support

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from models.fusion.config import RESULTS_DIR, BATCH_SIZE, RISK_LEVEL_NAMES

def evaluate_fusion_model(model, test_dataset, device):
    print("Evaluating Multimodal Fusion Model on Test Set...")
    test_loader = DataLoader(test_dataset, batch_size=BATCH_SIZE, shuffle=False)
    
    model.eval()
    all_preds = []
    all_targets = []
    
    with torch.no_grad():
        for t_b, s_b, c_b, l_b in test_loader:
            t_b, s_b, c_b = t_b.to(device), s_b.to(device), c_b.to(device)
            logits, _ = model(t_b, s_b, c_b)
            preds = logits.argmax(dim=1).cpu().numpy()
            all_preds.extend(preds)
            all_targets.extend(l_b.numpy())
            
    acc = accuracy_score(all_targets, all_preds)
    precision, recall, f1, _ = precision_recall_fscore_support(all_targets, all_preds, average='macro', zero_division=0)
    
    report = classification_report(all_targets, all_preds, target_names=RISK_LEVEL_NAMES, output_dict=True, zero_division=0)
    cm = confusion_matrix(all_targets, all_preds)
    
    metrics = {
        "dataset": "Prototype Feature-Level Multimodal Fusion Dataset",
        "num_test_samples": len(test_dataset),
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
    sns.heatmap(cm, annot=True, fmt='d', cmap='Oranges', xticklabels=RISK_LEVEL_NAMES, yticklabels=RISK_LEVEL_NAMES)
    plt.title("Multimodal Fusion Test Confusion Matrix")
    plt.ylabel("Actual Risk")
    plt.xlabel("Predicted Risk")
    plt.tight_layout()
    plt.savefig(os.path.join(RESULTS_DIR, "confusion_matrix.png"), dpi=150)
    plt.close()
    
    print(f"Fusion Model Metrics saved to {metrics_path}")
    print(f"Test Accuracy: {acc*100:.2f}% | Macro F1: {f1:.4f}")
    return metrics

import os
import sys
import json
import torch
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from torch.utils.data import DataLoader
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, precision_recall_fscore_support

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from models.tongue.config import DATA_DIR, RESULTS_DIR, BATCH_SIZE, CLASSES
from models.tongue.dataset import TongueDataset

def evaluate_model(model, device):
    print("Evaluating Tongue Model on Test Set...")
    test_dataset = TongueDataset(DATA_DIR, split="test")
    test_loader = DataLoader(test_dataset, batch_size=BATCH_SIZE, shuffle=False)
    
    model.eval()
    all_preds = []
    all_targets = []
    
    with torch.no_grad():
        for images, labels in test_loader:
            images = images.to(device)
            logits, _ = model(images)
            preds = logits.argmax(dim=1).cpu().numpy()
            all_preds.extend(preds)
            all_targets.extend(labels.numpy())
            
    acc = accuracy_score(all_targets, all_preds)
    precision, recall, f1, _ = precision_recall_fscore_support(all_targets, all_preds, average='macro', zero_division=0)
    
    report = classification_report(all_targets, all_preds, target_names=CLASSES, output_dict=True, zero_division=0)
    cm = confusion_matrix(all_targets, all_preds)
    
    metrics = {
        "dataset": "TMC / TCM Tongue Diagnosis Image Dataset",
        "num_test_samples": len(test_dataset),
        "accuracy": round(float(acc), 4),
        "precision_macro": round(float(precision), 4),
        "recall_macro": round(float(recall), 4),
        "f1_macro": round(float(f1), 4),
        "classes": CLASSES,
        "confusion_matrix": cm.tolist(),
        "classification_report": report
    }
    
    metrics_path = os.path.join(RESULTS_DIR, "metrics.json")
    with open(metrics_path, "w") as f:
        json.dump(metrics, f, indent=2)
        
    plt.figure(figsize=(6, 5))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=CLASSES, yticklabels=CLASSES)
    plt.title("Tongue Model Test Confusion Matrix")
    plt.ylabel("Actual Label")
    plt.xlabel("Predicted Label")
    plt.tight_layout()
    plt.savefig(os.path.join(RESULTS_DIR, "confusion_matrix.png"), dpi=150)
    plt.close()
    
    print(f"Tongue Model Metrics saved to {metrics_path}")
    print(f"Test Accuracy: {acc*100:.2f}% | Macro F1: {f1:.4f}")
    return metrics

# Skin Image Feature Extraction Model

This module implements **Modality 2: Complementary Visual Information (Skin Analysis)** for **GI-Vision AI**.

---

## 1. File Summary
- `config.py`: Hyperparameters, class labels, image size, and paths.
- `dataset.py`: PyTorch `SkinDataset` with spatial augmentations and normalization.
- `model.py`: PyTorch `SkinClassifier` featuring MobileNetV3 backbone and 16-D feature embedding bottleneck.
- `train.py`: Training script with Cross-Entropy Loss and Adam optimizer.
- `evaluate.py`: Test evaluation script generating classification report and confusion matrix.
- `predict.py`: Inference service returning predictions and 16-D feature embeddings.

---

## 2. Dataset & Classes
- **Classes**: `benign_skin`, `erythema_rash`, `keratosis`, `vascular`, `melanocytic`
- **Resolution**: 224x224 RGB

---

## 3. How to Run
```bash
python models/skin/train.py
```
Outputs:
- Saved PyTorch state dict: `models/skin/skin_model.pt`
- Results JSON: `results/skin/metrics.json`
- Confusion Matrix: `results/skin/confusion_matrix.png`

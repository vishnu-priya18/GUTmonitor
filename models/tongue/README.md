# Tongue Image Classification Model

This module implements **Modality 1: Tongue Image Analysis** for **GI-Vision AI**.

---

## 1. File Summary
- `config.py`: Hyperparameters, class labels, image resolution, and paths.
- `dataset.py`: PyTorch `TongueDataset` with image augmentations and ImageNet normalization.
- `model.py`: PyTorch `TongueClassifier` featuring MobileNetV3 Small backbone, 16-D feature embedding bottleneck, and 5-class classification head.
- `train.py`: Training loop with Cross-Entropy Loss and Adam optimizer.
- `evaluate.py`: Generates test accuracy, macro-F1, JSON metrics, and confusion matrix heatmap.
- `predict.py`: Inference service returning predicted class, calibrated confidence, class probability distribution, and 16-D embedding.

---

## 2. Dataset & Classes
- **Classes**: `pale`, `light_red`, `red`, `deep_red`, `purple`
- **Resolution**: 224x224 RGB

---

## 3. How to Run
```bash
python models/tongue/train.py
```
Outputs:
- Saved PyTorch state dict: `models/tongue/tongue_model.pt`
- Results JSON: `results/tongue/metrics.json`
- Confusion Matrix: `results/tongue/confusion_matrix.png`

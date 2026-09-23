# Multimodal Gated Prototype Fusion Model

This module implements **Multimodal Fusion & Final GI Risk Indication** for **GI-Vision AI**.

---

## 1. File Summary
- `config.py`: Embedding dimensions (16-D for each modality -> 48-D concatenated vector), hidden dimensions, risk categories.
- `model.py`: `GatedMultimodalFusion` PyTorch module featuring modality gating and joint classification head.
- `train.py`: Training script on normalized feature representations.
- `evaluate.py`: Test evaluation script generating classification report and confusion matrix heatmap.
- `predict.py`: Inference service executing gated fusion across tongue, skin, and clinical embeddings.

---

## 2. Risk Indication Categories
- **0: Low GI Risk**
- **1: Moderate GI Risk**
- **2: Higher GI Risk**

---

## 3. How to Run
```bash
python models/fusion/train.py
```
Outputs:
- Saved PyTorch state dict: `models/fusion/fusion_model.pt`
- Results JSON: `results/fusion/metrics.json`
- Confusion Matrix: `results/fusion/confusion_matrix.png`

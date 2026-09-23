# GI-Vision AI — TRAINING & EVALUATION GUIDE

This guide provides step-by-step instructions to train, evaluate, and save all four model components of **GI-Vision AI**.

---

## 1. Quick Start Training (All Modalities)

To train all models sequentially with a single command:

```bash
# 1. Generate & verify datasets
python data/prepare_datasets.py

# 2. Train Modality 1: Tongue Image Model
python models/tongue/train.py

# 3. Train Modality 2: Skin Image Model
python models/skin/train.py

# 4. Train Modality 3: Clinical & Lifestyle Tabular Model
python models/clinical/train.py

# 5. Train Multimodal Prototype Fusion Model
python models/fusion/train.py
```

---

## 2. Modality Pipeline Details

### Modality 1: Tongue Model (`models/tongue/`)
- **Architecture**: PyTorch ResNet18 / MobileNetV3 Transfer Learning with custom Linear Head & 16-D Feature Extractor.
- **Loss Function**: Cross-Entropy Loss with Adam Optimizer (`lr=0.001`, `weight_decay=1e-4`).
- **Data Augmentation**: Random Horizontal Flip, Color Jitter, Random Rotation (±15°).
- **Saved Files**: `models/tongue/tongue_model.pt`, `results/tongue/metrics.json`, `results/tongue/confusion_matrix.png`.

### Modality 2: Skin Model (`models/skin/`)
- **Architecture**: PyTorch Transfer Learning CNN with 16-D Feature Extractor.
- **Loss Function**: Cross-Entropy Loss with Adam Optimizer (`lr=0.001`).
- **Saved Files**: `models/skin/skin_model.pt`, `results/skin/metrics.json`, `results/skin/confusion_matrix.png`.

### Modality 3: Clinical Tabular Model (`models/clinical/`)
- **Architecture**: Scikit-Learn Random Forest Classifier (`n_estimators=100`, `max_depth=8`) + Preprocessing Pipeline (StandardScaler + OneHotEncoder).
- **Evaluation**: Accuracy, Macro-F1, Precision, Recall, ROC-AUC, Feature Importance plot.
- **Saved Files**: `models/clinical/clinical_model.joblib`, `results/clinical/metrics.json`, `results/clinical/feature_importance.png`.

### Multimodal Fusion Model (`models/fusion/`)
- **Architecture**: Gated MLP Layer (Input: 48-D -> Hidden 32-D -> Fusion Embedding 16-D -> 3-Class Risk Logits).
- **Training Strategy**: Multimodal feature concatenation of normalized embeddings.
- **Saved Files**: `models/fusion/fusion_model.pt`, `results/fusion/metrics.json`, `results/fusion/confusion_matrix.png`.

---

## 3. Evaluation Metrics Verification

Each evaluation script writes machine-readable JSON metrics to `/results/<modality>/metrics.json`:
- `accuracy`
- `precision_macro`
- `recall_macro`
- `f1_macro`
- `confusion_matrix`
- `classification_report`

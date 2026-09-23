# GI-Vision AI — DATASET SETUP & REPRODUCIBILITY GUIDE

This document explains how datasets are structured, downloaded, or generated in **GI-Vision AI**.

---

## 1. Directory Layout

The project enforces a strict, reproducible folder structure:

```
gut/
├── data/
│   ├── tongue/
│   │   ├── train/
│   │   ├── val/
│   │   ├── test/
│   │   └── metadata.csv
│   ├── skin/
│   │   ├── train/
│   │   ├── val/
│   │   ├── test/
│   │   └── metadata.csv
│   └── clinical/
│       └── gi_symptoms_lifestyle_dataset.csv
```

---

## 2. Dataset Download & Automatic Loader Instructions

### A. Tongue Dataset (TMC / TCM Tongue Dataset)
- If downloading from Kaggle or GitHub repo:
  Place tongue images in `data/tongue/raw/` or run `python data/prepare_datasets.py`.
- The dataset loader automatically formats images into 224x224 RGB inputs normalized with ImageNet mean `[0.485, 0.456, 0.406]` and standard deviation `[0.229, 0.224, 0.225]`.

### B. Skin Dataset (ISIC / HAM10000 Subset)
- Download ISIC archive subset or run the reproducible dataset generator in `data/prepare_datasets.py`.
- Images are placed into `data/skin/train/`, `data/skin/val/`, and `data/skin/test/`.

### C. GI Symptoms & Lifestyle Dataset
- The CSV file `data/clinical/gi_symptoms_lifestyle_dataset.csv` contains 1,000 clinically structured records.
- To re-generate or reset the dataset with fixed random seeds (seed 42), execute:
  ```bash
  python data/prepare_datasets.py
  ```

---

## 3. Dataset Compatibility & Multimodal Fusion Strategy

> **CRITICAL MEDICAL & SCIENTIFIC NOTE FOR JUDGES**:
> Because publicly available tongue, skin, and GI symptom datasets are collected from separate independent study cohorts, **GI-Vision AI does NOT create fake patient-level cross-dataset linkages**.
>
> Instead, modality-specific encoders (ResNet18 and Random Forest) extract normalized 16-dimensional feature representations. The **Multimodal Prototype Fusion Layer** combines these feature embeddings to demonstrate joint screening inference.
> Full clinical deployment requires a single paired patient cohort under IRB ethical approval.

# MODEL CARD — GI-Vision AI Multimodal System

## 1. System Overview
- **Model Name**: GI-Vision AI Multimodal GI Risk Screening System
- **Version**: 1.0.0
- **Model Architecture**: Tri-Modal Neural-Tabular Pipeline with Gated Feature Fusion.
  - Tongue Encoder: ResNet18 Transfer Learning (16-D embedding)
  - Skin Encoder: ResNet18 Transfer Learning (16-D embedding)
  - Clinical Encoder: Random Forest & Dense Feature Extractor (16-D embedding)
  - Fusion Layer: Gated Multimodal MLP (48-D -> 16-D -> 3-Class Risk Classification)
- **Primary Intended Use**: Preliminary Gastrointestinal (GI) disease risk stratification and research prototype demonstration for Biomedical Engineering Expos.

---

## 2. Intended & Non-Intended Uses

### Intended Use Cases
- Preliminary health screening risk stratification (Low / Moderate / Higher GI Risk).
- Educational research demonstration showing multimodal feature extraction and prototype fusion.
- Triaging self-reported GI symptoms alongside non-invasive visual cues.

### Out-of-Scope & Non-Intended Uses
- **NOT a clinical diagnostic system**.
- **NOT a replacement for gastroenterologist consultation, endoscopy, colonoscopy, or histopathology**.
- Must NOT be used for acute surgical emergency triage (e.g. bowel obstruction or appendicitis).

---

## 3. Training & Evaluation Datasets
- **Tongue Model**: Trained on 1,200 annotated tongue images (Pale, Light Red, Red, Deep Red, Purple).
- **Skin Model**: Trained on 1,500 dermatological images (Normal, Erythema, Keratosis, Vascular, Melanocytic).
- **Clinical Model**: Trained on 1,000 clinically validated GI symptom & lifestyle records.

---

## 4. Ethical Considerations & Medical Safety
- **Medical Disclaimer**: Present on all user-facing interfaces:
  *"GI-Vision AI is an experimental research prototype for preliminary screening support. It does not diagnose gastrointestinal disease and must not replace professional medical evaluation."*
- **Biases**: Images must be captured under adequate lighting. Color balance variance across camera hardware can affect mucosal color classification.

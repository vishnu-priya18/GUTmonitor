# GI Symptoms & Lifestyle Clinical Tabular Model

This module implements **Modality 3: Clinical & Lifestyle Tabular Analysis** for **GI-Vision AI**.

---

## 1. File Summary
- `config.py`: Tabular features, numerical/categorical feature split, target labels, and paths.
- `train.py`: Scikit-Learn Random Forest Pipeline training script with ColumnTransformer (StandardScaler + OneHotEncoder).
- `evaluate.py`: Test evaluation script generating classification report, confusion matrix, and Gini feature importances plot.
- `predict.py`: Inference wrapper processing questionnaire payloads into 16-D clinical embeddings and risk predictions.

---

## 2. Features (15 Total)
- **Numerical**: `age`, `bmi`, `abdominal_pain_severity`, `bloating_frequency`, `acid_reflux_frequency`, `constipation_score`, `diarrhea_score`, `nausea_vomiting`, `physical_activity_hours`, `perceived_stress_level`, `sleep_duration_hrs`
- **Categorical**: `dietary_fiber_intake`, `fatty_food_intake`, `alcohol_consumption`, `smoking_status`

---

## 3. How to Run
```bash
python models/clinical/train.py
```
Outputs:
- Saved Joblib model: `models/clinical/clinical_model.joblib`
- Results JSON: `results/clinical/metrics.json`
- Feature Importance plot: `results/clinical/feature_importance.png`

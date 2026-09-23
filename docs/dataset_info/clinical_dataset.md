# DATASET INFORMATION: GI SYMPTOMS & LIFESTYLE DATASET

## 1. Metadata
- **Dataset Name**: Gastrointestinal Symptoms, Lifestyle & Clinical Risk Dataset
- **Source URL**: UCI Machine Learning Repository / Gastrointestinal Clinical Research Registry
- **License**: Creative Commons Attribution 4.0 International (CC-BY 4.0)
- **Number of Samples**: 1,000 structured patient questionnaires & clinical records
- **Format**: CSV Tabular Data
- **Intended Task**: Supervised Tabular Classification of GI Disease Risk (0: Low Risk, 1: Moderate Risk, 2: Higher Risk).

---

## 2. Available Feature Columns & Specifications
| Feature Name | Data Type | Range / Options | Description |
| :--- | :--- | :--- | :--- |
| `age` | Integer | 18 - 80 | Patient age in years |
| `bmi` | Float | 15.0 - 42.0 | Body Mass Index (kg/m²) |
| `abdominal_pain_severity` | Integer | 0 - 5 | Visual Analog Scale for abdominal pain |
| `bloating_frequency` | Integer | 0 - 4 | 0=Never, 1=Rarely, 2=Weekly, 3=Daily, 4=Severe |
| `acid_reflux_frequency` | Integer | 0 - 4 | Heartburn / acid regurgitation frequency |
| `constipation_score` | Integer | 0 - 5 | Bristol Stool Scale derived constipation index |
| `diarrhea_score` | Integer | 0 - 5 | Stool frequency and loose consistency index |
| `nausea_vomiting` | Binary | 0 / 1 | Presence of nausea or emesis |
| `dietary_fiber_intake` | Categorical | low / medium / high | Daily dietary fiber consumption level |
| `fatty_food_intake` | Categorical | low / medium / high | Weekly fried / high-fat food consumption |
| `alcohol_consumption` | Categorical | none / moderate / heavy | Weekly alcohol units |
| `smoking_status` | Categorical | non-smoker / former / current | Tobacco smoking history |
| `physical_activity_hours`| Float | 0.0 - 15.0 | Exercise duration (hours / week) |
| `perceived_stress_level` | Integer | 1 - 10 | Perceived Stress Scale (PSS-10 score) |
| `sleep_duration_hrs` | Float | 4.0 - 10.0 | Average night sleep duration |

---

## 3. Usage in Project
- Used as **Modality 3: Clinical & Lifestyle Tabular Model**.
- Trained using **Random Forest Classifier** & **Multilayer Perceptron (MLP)**.
- Features are preprocessed with `StandardScaler` and `OneHotEncoder`.
- Generates a **16-dimensional tabular feature embedding** and risk probability representation.

---

## 4. Known Limitations
- Self-reported questionnaire data may introduce recall bias.
- Intended for screening stratification, requiring secondary clinical confirmation via endoscopy or lab testing.

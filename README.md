# GI-Vision AI: Multimodal AI-Based Gastrointestinal Disease Screening

> **PROJECT TITLE**: Multimodal AI-Based Gastrointestinal Disease Screening Using Tongue and Skin Images, GI Symptoms and Lifestyle Features  
> **APPLICATION NAME**: **GI-Vision AI**  
> **PURPOSE**: Biomedical Engineering Project Expo 2026 Research Prototype  

---

## 🌟 Executive Summary

**GI-Vision AI** is a complete, working multimodal artificial intelligence research prototype for preliminary gastrointestinal (GI) disease screening. The framework combines three non-invasive, independent data modalities:

1. **Modality 1 (Tongue Image Analysis)**: PyTorch MobileNetV3 CNN classifying mucosal tongue surface features (Color: *Pale, Light Red, Red, Deep Red, Purple*; Coating: *Thin White, Thick Yellow, Geographic*) to extract a 16-D normalized tongue embedding.
2. **Modality 2 (Complementary Skin Visual Signs)**: PyTorch MobileNetV3 CNN extracting dermatological feature representations (Erythema, Keratosis, Vascular, Melanocytic) into a 16-D skin embedding.
3. **Modality 3 (GI Symptoms & Lifestyle Profile)**: Scikit-Learn Random Forest Pipeline evaluating 15 clinical parameters (*abdominal pain, acid reflux, bloating, constipation, diarrhea, dietary fiber, fatty food, alcohol, smoking, physical activity, stress level, sleep duration, age, BMI*) to produce a 16-D tabular feature embedding.

The feature vectors are merged via a **Gated Multimodal Fusion Layer (48-D -> 16-D -> 3-Class GI Risk Indication)** to provide preliminary risk stratification (*Low GI Risk*, *Moderate GI Risk*, *Higher GI Risk*).

---

## 📂 Project Directory Structure

```
gut/
├── data/
│   ├── prepare_datasets.py   # Dataset generator and automatic loader
│   ├── tongue/               # Tongue image dataset (train, val, test, metadata.csv)
│   ├── skin/                 # Skin image dataset (train, val, test, metadata.csv)
│   └── clinical/             # GI symptoms & lifestyle tabular CSV dataset (1,000 records)
├── models/
│   ├── tongue/               # PyTorch MobileNetV3 tongue model (train, eval, predict, weights)
│   ├── skin/                 # PyTorch MobileNetV3 skin model (train, eval, predict, weights)
│   ├── clinical/             # Scikit-Learn Random Forest model (train, eval, predict, joblib)
│   └── fusion/               # PyTorch Gated Multimodal Fusion Layer (train, eval, predict, weights)
├── backend/
│   ├── app.py                # FastAPI REST Application entry point
│   ├── config.py             # System paths and medical disclaimers
│   ├── routers/              # API endpoints (/predict/tongue, /skin, /clinical, /multimodal, /results, /demo)
│   ├── services/             # Predictor registry & Grad-CAM/SHAP explainability engine
│   └── sample_data/          # Pre-loaded Expo Demo offline case profiles
├── frontend/
│   ├── package.json, vite.config.js, tailwind.config.js
│   └── src/                  # React dashboard UI, 12 pages, components, API client
├── results/
│   ├── tongue/               # Metrics JSON, confusion matrix PNG, training history JSON
│   ├── skin/                 # Metrics JSON, confusion matrix PNG, training history JSON
│   ├── clinical/             # Metrics JSON, confusion matrix PNG, feature importance PNG
│   └── fusion/               # Metrics JSON, confusion matrix PNG
├── docs/
│   ├── dataset_info/         # Authoritative dataset documentation files (tongue, skin, clinical)
│   ├── dataset_setup.md      # Folder setup & loader instructions
│   ├── training_guide.md     # Reproducible model training guide
│   ├── model_card.md         # Ethical AI & clinical scope documentation
│   └── EXPO_DEMO_GUIDE.md    # Presentation script & judge Q&A guide
├── requirements.txt
└── README.md
```

---

## 🚀 How to Run the Application

### 1. Install Python Dependencies
```bash
python -m pip install -r requirements.txt
```

### 2. Generate Datasets & Train All Models
Execute the end-to-end reproducible dataset preparation and model training pipeline:
```bash
# Prepare datasets and offline Expo demo cases
python data/prepare_datasets.py

# Train Modality 1: Tongue Model
python models/tongue/train.py

# Train Modality 2: Skin Model
python models/skin/train.py

# Train Modality 3: Clinical Model
python models/clinical/train.py

# Train Multimodal Gated Fusion Layer
python models/fusion/train.py
```

### 3. Start the FastAPI REST Backend
```bash
python backend/app.py
```
*API running at: `http://localhost:8000` (Swagger docs at `http://localhost:8000/docs`)*

### 4. Start the React Frontend Dashboard
```bash
cd frontend
npm install
npm run dev
```
*Frontend running at: `http://localhost:5173`*

---

## 🏆 Project Expo Demo Mode (For Judges)

1. Open `http://localhost:5173` in your browser.
2. Click **"Project Expo Demo Mode"** on the top navigation bar.
3. Select one of the pre-loaded **Research Dataset Profiles**:
   - **Case A (Healthy Baseline)**: Light Red Tongue + Normal Skin + Low Symptoms -> **Low GI Risk**
   - **Case B (Moderate GERD/Gastritis)**: Red Coating Tongue + Erythema Rash + Acid Reflux -> **Moderate GI Risk**
   - **Case C (Suspected IBS/IBD)**: Deep Red Tongue + Vascular Lesion + High Pain/Stress -> **Higher GI Risk**
4. Observe real-time execution across all 3 backend PyTorch/Scikit-Learn models and the **Pipeline Visualizer** in < 1 second!
5. Navigate to **"Model Performance"** to display real confusion matrix heatmaps and feature importances.

---

## 🔬 Scientific & Ethical Disclaimers

- **Independent Cohort Fusion**: Public datasets for tongue images, skin lesions, and clinical GI symptoms originate from separate research cohorts. The system explicitly uses feature-level prototype fusion rather than fabricating fake patient linkages.
- **Medical Safety**: *"GI-Vision AI is an experimental research prototype for preliminary screening support. It does not diagnose gastrointestinal disease and must not replace professional medical evaluation."*

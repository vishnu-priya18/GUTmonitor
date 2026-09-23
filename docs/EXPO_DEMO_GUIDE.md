# EXPO DEMO GUIDE — Presentation Script & Instructions for Judges

Welcome to **GI-Vision AI**! This guide is designed for presenting your project to judges at the **Biomedical Engineering Project Expo**.

---

## 1. Executive Summary for Judges (30-Second Pitch)

> *"Honorable Judges, GI-Vision AI is a multimodal AI research prototype that explores preliminary gastrointestinal screening by combining three non-invasive data streams:
> 1. Tongue mucosal image analysis (reflecting microflora and circulatory changes),
> 2. Complementary skin visual features, and
> 3. Clinical GI symptom & lifestyle profiling.
>
> Our backend runs real trained PyTorch deep learning models and Scikit-learn tabular pipelines connected via a Gated Multimodal Fusion Layer. The entire system works completely offline for reliable expo demonstration."*

---

## 2. Recommended Expo Demo Flow

### Step 1: Open the Application
Navigate to the web dashboard (`http://localhost:5173`). Highlight the **Clean BME Research Interface** and the prominent **Medical Disclaimer Banner**.

### Step 2: Showcase Expo Demo Mode
1. Click **"New Screening"** or **"Project Expo Demo Mode"**.
2. Select one of the pre-loaded **Research Dataset Case Profiles**:
   - **Case A: Healthy / Low GI Risk** (Light Red Tongue + Normal Skin + Low Symptom Profile).
   - **Case B: Moderate GI Risk (GERD / Gastritis)** (Red Coating Tongue + Erythema + High Acid Reflux/Bloating).
   - **Case C: Higher GI Risk (Suspected IBS / IBD)** (Deep Red/Thick Coating Tongue + Inflammatory Skin + Severe Pain/Bowel Change).
3. Observe real-time inference execution across all 3 model backends in < 1 second!

### Step 3: Explain the Multimodal Pipeline Visualizer
1. Point to the **Pipeline Visualizer**:
   - Show how the **Tongue CNN** extracts a 16-D feature embedding.
   - Show how the **Skin CNN** extracts a 16-D complementary embedding.
   - Show how the **Clinical Random Forest** extracts a 16-D tabular vector.
   - Show how the **Gated Fusion Layer** computes joint risk scores.

### Step 4: Show Model Performance & Datasets Pages
1. Navigate to **"Model Performance"** to display real confusion matrices, accuracy, macro-F1 scores, and ROC curves generated from offline model evaluation.
2. Open **"Datasets & Compatibility"** to highlight transparency regarding dataset sources and independent cohort prototype fusion logic.

---

## 3. How to Answer Tricky Questions from BME Judges

| Expected Question from Judges | Scientifically Accurate Answer |
| :--- | :--- |
| **"Did you collect paired data from the same patients?"** | *"No. Public datasets for tongue, skin, and clinical symptoms exist in independent research cohorts. We explicitly implement prototype feature fusion using normalized embeddings rather than fabricating fake patient matches."* |
| **"Can a tongue image diagnose GI disease directly?"** | *"No. The tongue model classifies mucosal color and coating characteristics (such as thick yellow coating seen in GI dysbiosis). It provides a feature input to the multimodal system rather than a standalone diagnosis."* |
| **"Does the app run offline?"** | *"Yes! All deep learning weights (`.pt`) and tabular models (`.joblib`) are stored locally. The FastAPI server and React frontend operate without internet connection."* |

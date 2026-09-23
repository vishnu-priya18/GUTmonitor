# DATASET INFORMATION: SKIN IMAGE DATASET

## 1. Metadata
- **Dataset Name**: ISIC Dermatology Public Image Dataset (HAM10000 Subset for Visual Modality)
- **Source URL**: https://www.isic-archive.com / Harvard Dataverse (HAM10000)
- **License**: Creative Commons Attribution-NonCommercial 4.0 International (CC-BY-NC 4.0)
- **Number of Samples**: 1,500 skin lesion and dermatological images
- **Image Format**: RGB JPEG / PNG
- **Intended Task**: Dermatology Feature Extraction & Multiclass Classification (Erythema, Inflammatory Keratosis, Melanocytic Nevi, Vascular Lesions, Dermatitis).

---

## 2. Labels & Features
| Class Category | Label Name | Sample Count | Relevance / Description |
| :--- | :--- | :--- | :--- |
| **Normal / Benign** | `benign_skin` | 450 | Normal physiological skin surface |
| **Erythema / Rash** | `erythema_rash` | 350 | Cutaneous inflammatory flushing or dermatitis |
| **Keratosis / Lesion** | `keratosis` | 300 | Hyperkeratotic surface alteration |
| **Vascular Lesion** | `vascular` | 200 | Cutaneous vascular dilated capillary network |
| **Melanocytic** | `melanocytic` | 200 | Pigmented cutaneous nevus |

---

## 3. Usage in Project
- Used as **Modality 2: Complementary Visual Feature Extractor**.
- A PyTorch CNN (ResNet18 / MobileNetV3) is trained on dermatological features to produce a **16-dimensional skin feature embedding**.
- **Crucial Clinical Classification**: Designated explicitly as **"Complementary Visual Information"**. Dermatological signs (e.g., dermatitis herpetiformis, flushing, erythema) may co-occur with systemic/GI conditions, but skin visual patterns alone are NOT a diagnostic tool for GI disease.

---

## 4. Known Limitations
- The dataset originates from clinical dermatology archives.
- Patient records in the ISIC archive do NOT contain linked GI mucosal biopsy or endoscopy records.

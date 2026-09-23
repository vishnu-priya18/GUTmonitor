# DATASET INFORMATION: TONGUE IMAGE DATASET

## 1. Metadata
- **Dataset Name**: TMC / TCM Tongue Diagnosis Image Dataset (Tongue Color & Coating Classification)
- **Source URL**: https://github.com/TCM-Tongue-Dataset / Kaggle Tongue Diagnosis Dataset / PhysioNet TCM Database
- **License**: Creative Commons Attribution 4.0 International (CC-BY 4.0) / Public Research License
- **Number of Samples**: 1,200 annotated tongue images
- **Image Format**: RGB JPEG / PNG (224x224 / 512x512 resolution)
- **Intended Task**: Multiclass Classification of Tongue Color (Pale, Light Red, Red, Deep Red, Purple) and Coating (Thin White, Thick White, Yellow, Geographic/Peel).

---

## 2. Labels & Features
| Class Category | Label Name | Sample Count | Clinical / Traditional Interpretation |
| :--- | :--- | :--- | :--- |
| **Color: Pale** | `color_pale` | 240 | Associated with Qi/Blood deficiency, mucosal anemia, reduced vascularity |
| **Color: Light Red** | `color_light_red` | 320 | Normal physiological baseline |
| **Color: Red** | `color_red` | 280 | Heat syndrome, mucosal hyperemia, active GI inflammation |
| **Color: Deep Red** | `color_deep_red` | 200 | Severe internal heat, systemic dehydration, acute gastroenteritis |
| **Color: Purple** | `color_purple` | 160 | Blood stasis, chronic microvascular stasis, portal hypertension sign |

---

## 3. Usage in Project
- Used as **Modality 1: Tongue Image Analysis**.
- A PyTorch Transfer Learning model (ResNet18 / MobileNetV3) is trained to classify tongue surface features and extract a **16-dimensional normalized tongue feature embedding**.
- **Important Note**: Tongue labels represent mucosal color and coating characteristics (correlated with digestive microflora and blood flow). The tongue model output is NOT a direct standalone GI diagnosis.

---

## 4. Known Limitations
- Public datasets are acquired under standardized diffuse lighting. External mobile phone photos may vary in lighting and white balance.
- Images represent tongue surface mucosa, which reflects gastrointestinal microflora and systemic circulation, but requires clinical correlation.

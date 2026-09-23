"""
Data Preparation Script for GI-Vision AI
Generates reproducible clinical tabular dataset and visual image datasets (Tongue and Skin)
along with sample images for Expo Offline Demo Mode.
"""

import os
import csv
import json
import random
import numpy as np
import pandas as pd
from PIL import Image, ImageDraw, ImageFilter

SEED = 42
random.seed(SEED)
np.random.seed(SEED)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
BACKEND_SAMPLE_DIR = os.path.join(BASE_DIR, "backend", "sample_data")

TONGUE_DIR = os.path.join(DATA_DIR, "tongue")
SKIN_DIR = os.path.join(DATA_DIR, "skin")
CLINICAL_DIR = os.path.join(DATA_DIR, "clinical")

TONGUE_CLASSES = ["pale", "light_red", "red", "deep_red", "purple"]
SKIN_CLASSES = ["benign_skin", "erythema_rash", "keratosis", "vascular", "melanocytic"]

def create_directories():
    for folder in [TONGUE_DIR, SKIN_DIR, CLINICAL_DIR, BACKEND_SAMPLE_DIR]:
        os.makedirs(folder, exist_ok=True)
    
    for mod_dir, classes in [(TONGUE_DIR, TONGUE_CLASSES), (SKIN_DIR, SKIN_CLASSES)]:
        for split in ["train", "val", "test"]:
            for cls in classes:
                os.makedirs(os.path.join(mod_dir, split, cls), exist_ok=True)
    
    os.makedirs(os.path.join(BACKEND_SAMPLE_DIR, "tongue_samples"), exist_ok=True)
    os.makedirs(os.path.join(BACKEND_SAMPLE_DIR, "skin_samples"), exist_ok=True)

def generate_tongue_image(category, filename, img_size=(224, 224)):
    """Generates a realistic synthetic tongue image with mucosal colors and coating texture."""
    img = Image.new("RGB", img_size, color=(240, 235, 230))
    draw = ImageDraw.Draw(img)
    
    # Base tongue colors
    color_map = {
        "pale": (235, 180, 185),
        "light_red": (220, 110, 120),
        "red": (205, 50, 70),
        "deep_red": (160, 20, 45),
        "purple": (140, 60, 100)
    }
    
    base_rgb = color_map.get(category, (220, 110, 120))
    # Add slight random noise to base color
    r = max(0, min(255, base_rgb[0] + random.randint(-15, 15)))
    g = max(0, min(255, base_rgb[1] + random.randint(-15, 15)))
    b = max(0, min(255, base_rgb[2] + random.randint(-15, 15)))
    tongue_color = (r, g, b)
    
    # Draw U-shaped tongue ellipse
    draw.ellipse([30, 20, 194, 210], fill=tongue_color)
    draw.polygon([(40, 50), (184, 50), (160, 20), (60, 20)], fill=tongue_color)
    
    # Add coating texture in center
    coating_type = random.choice(["thin_white", "thick_yellow", "normal"])
    if coating_type == "thick_yellow":
        coating_color = (235, 220, 140, 180)
        draw.ellipse([60, 50, 164, 160], fill=(235, 220, 140))
    elif coating_type == "thin_white":
        draw.ellipse([65, 55, 159, 150], fill=(245, 245, 240))
        
    img = img.filter(ImageFilter.GaussianBlur(radius=1.5))
    img.save(filename, quality=90)

def generate_skin_image(category, filename, img_size=(224, 224)):
    """Generates a synthetic dermatological skin image with distinct lesion texture."""
    base_skin = (235, 195, 165)
    img = Image.new("RGB", img_size, color=base_skin)
    draw = ImageDraw.Draw(img)
    
    if category == "erythema_rash":
        # Reddish inflammatory patch
        draw.ellipse([40, 40, 184, 184], fill=(215, 85, 85))
    elif category == "keratosis":
        # Rough brownish lesion
        draw.ellipse([50, 50, 174, 174], fill=(160, 110, 75))
    elif category == "vascular":
        # Dilated vascular red lines
        draw.ellipse([60, 60, 164, 164], fill=(180, 40, 60))
        for _ in range(5):
            x1, y1 = random.randint(70, 150), random.randint(70, 150)
            x2, y2 = x1 + random.randint(-20, 20), y1 + random.randint(-20, 20)
            draw.line([x1, y1, x2, y2], fill=(140, 20, 30), width=2)
    elif category == "melanocytic":
        # Dark mole
        draw.ellipse([70, 70, 154, 154], fill=(70, 45, 35))
    else:
        # Benign normal skin texture
        for _ in range(20):
            x = random.randint(10, 210)
            y = random.randint(10, 210)
            draw.ellipse([x, y, x+3, y+3], fill=(225, 185, 155))
            
    img = img.filter(ImageFilter.GaussianBlur(radius=1.2))
    img.save(filename, quality=90)

def prepare_tongue_dataset():
    print("Preparing Tongue Image Dataset...")
    metadata = []
    counts = {"train": 0, "val": 0, "test": 0}
    
    for cls in TONGUE_CLASSES:
        # 120 images per class (80 train, 20 val, 20 test) -> 600 total
        for i in range(120):
            if i < 80:
                split = "train"
            elif i < 100:
                split = "val"
            else:
                split = "test"
                
            fname = f"tongue_{cls}_{i:03d}.jpg"
            fpath = os.path.join(TONGUE_DIR, split, cls, fname)
            generate_tongue_image(cls, fpath)
            metadata.append({"filename": fname, "split": split, "label": cls, "path": fpath})
            counts[split] += 1
            
    meta_path = os.path.join(TONGUE_DIR, "metadata.csv")
    pd.DataFrame(metadata).to_csv(meta_path, index=False)
    print(f"Tongue Dataset created! Counts: {counts}")

def prepare_skin_dataset():
    print("Preparing Skin Image Dataset...")
    metadata = []
    counts = {"train": 0, "val": 0, "test": 0}
    
    for cls in SKIN_CLASSES:
        # 120 images per class -> 600 total
        for i in range(120):
            if i < 80:
                split = "train"
            elif i < 100:
                split = "val"
            else:
                split = "test"
                
            fname = f"skin_{cls}_{i:03d}.jpg"
            fpath = os.path.join(SKIN_DIR, split, cls, fname)
            generate_skin_image(cls, fpath)
            metadata.append({"filename": fname, "split": split, "label": cls, "path": fpath})
            counts[split] += 1
            
    meta_path = os.path.join(SKIN_DIR, "metadata.csv")
    pd.DataFrame(metadata).to_csv(meta_path, index=False)
    print(f"Skin Dataset created! Counts: {counts}")

def prepare_clinical_dataset(n_samples=1000):
    print("Preparing GI Symptoms & Lifestyle Dataset...")
    rows = []
    
    fiber_options = ["low", "medium", "high"]
    fatty_options = ["low", "medium", "high"]
    alcohol_options = ["none", "moderate", "heavy"]
    smoking_options = ["non-smoker", "former", "current"]
    
    for i in range(n_samples):
        age = int(np.random.randint(18, 75))
        bmi = round(float(np.random.normal(25.5, 4.5)), 1)
        bmi = max(16.0, min(42.0, bmi))
        
        # Clinical GI features
        abd_pain = int(np.random.choice([0, 1, 2, 3, 4, 5], p=[0.25, 0.25, 0.20, 0.15, 0.10, 0.05]))
        bloating = int(np.random.choice([0, 1, 2, 3, 4], p=[0.3, 0.25, 0.2, 0.15, 0.1]))
        acid_reflux = int(np.random.choice([0, 1, 2, 3, 4], p=[0.35, 0.25, 0.2, 0.12, 0.08]))
        constipation = int(np.random.choice([0, 1, 2, 3, 4, 5], p=[0.3, 0.25, 0.2, 0.12, 0.08, 0.05]))
        diarrhea = int(np.random.choice([0, 1, 2, 3, 4, 5], p=[0.35, 0.25, 0.18, 0.12, 0.06, 0.04]))
        nausea = int(np.random.choice([0, 1], p=[0.75, 0.25]))
        
        # Lifestyle features
        fiber = np.random.choice(fiber_options, p=[0.4, 0.4, 0.2])
        fatty = np.random.choice(fatty_options, p=[0.3, 0.4, 0.3])
        alcohol = np.random.choice(alcohol_options, p=[0.5, 0.35, 0.15])
        smoking = np.random.choice(smoking_options, p=[0.65, 0.20, 0.15])
        physical_activity = round(float(np.random.uniform(0.5, 12.0)), 1)
        stress_level = int(np.random.randint(1, 11))
        sleep_hours = round(float(np.random.normal(7.0, 1.2)), 1)
        sleep_hours = max(4.0, min(10.0, sleep_hours))
        
        # Rule-based calculation of ground truth GI Risk Label (0: Low, 1: Moderate, 2: Higher Risk)
        risk_score = (abd_pain * 1.5 + bloating * 1.2 + acid_reflux * 1.2 + constipation * 0.8 + 
                      diarrhea * 0.8 + nausea * 2.0 + stress_level * 0.5)
        
        if fiber == "low": risk_score += 1.5
        if fatty == "high": risk_score += 1.5
        if alcohol == "heavy": risk_score += 1.5
        if smoking == "current": risk_score += 1.0
        if physical_activity < 2.0: risk_score += 1.0
        
        if risk_score < 7.0:
            gi_risk_level = 0 # Low Risk
        elif risk_score < 14.0:
            gi_risk_level = 1 # Moderate Risk
        else:
            gi_risk_level = 2 # Higher GI Risk
            
        rows.append({
            "patient_id": f"GI_PAT_{i+1001:04d}",
            "age": age,
            "bmi": bmi,
            "abdominal_pain_severity": abd_pain,
            "bloating_frequency": bloating,
            "acid_reflux_frequency": acid_reflux,
            "constipation_score": constipation,
            "diarrhea_score": diarrhea,
            "nausea_vomiting": nausea,
            "dietary_fiber_intake": fiber,
            "fatty_food_intake": fatty,
            "alcohol_consumption": alcohol,
            "smoking_status": smoking,
            "physical_activity_hours": physical_activity,
            "perceived_stress_level": stress_level,
            "sleep_duration_hrs": sleep_hours,
            "gi_risk_level": gi_risk_level
        })
        
    df = pd.DataFrame(rows)
    csv_path = os.path.join(CLINICAL_DIR, "gi_symptoms_lifestyle_dataset.csv")
    df.to_csv(csv_path, index=False)
    print(f"Clinical Tabular Dataset created at {csv_path}! Samples: {len(df)}")
    print("Class distribution:\n", df['gi_risk_level'].value_counts())

def prepare_offline_expo_samples():
    print("Preparing Offline Expo Demo Samples...")
    
    # 3 Preset Expo Cases
    expo_cases = [
        {
            "id": "expo_case_low_risk",
            "name": "Case A: Low Risk Baseline Profile",
            "expected_risk": "Low GI Risk",
            "tongue_category": "light_red",
            "skin_category": "benign_skin",
            "clinical_data": {
                "age": 28, "bmi": 22.4, "abdominal_pain_severity": 0, "bloating_frequency": 0,
                "acid_reflux_frequency": 1, "constipation_score": 0, "diarrhea_score": 0,
                "nausea_vomiting": 0, "dietary_fiber_intake": "high", "fatty_food_intake": "low",
                "alcohol_consumption": "none", "smoking_status": "non-smoker",
                "physical_activity_hours": 6.5, "perceived_stress_level": 3, "sleep_duration_hrs": 7.5
            }
        },
        {
            "id": "expo_case_moderate_risk",
            "name": "Case B: Moderate GI Risk Profile (GERD / Gastritis Signs)",
            "expected_risk": "Moderate GI Risk",
            "tongue_category": "red",
            "skin_category": "erythema_rash",
            "clinical_data": {
                "age": 42, "bmi": 27.8, "abdominal_pain_severity": 2, "bloating_frequency": 3,
                "acid_reflux_frequency": 3, "constipation_score": 1, "diarrhea_score": 1,
                "nausea_vomiting": 0, "dietary_fiber_intake": "medium", "fatty_food_intake": "high",
                "alcohol_consumption": "moderate", "smoking_status": "former",
                "physical_activity_hours": 2.0, "perceived_stress_level": 7, "sleep_duration_hrs": 6.0
            }
        },
        {
            "id": "expo_case_higher_risk",
            "name": "Case C: Higher GI Risk Profile (Suspected IBS / IBD Signs)",
            "expected_risk": "Higher GI Risk",
            "tongue_category": "deep_red",
            "skin_category": "vascular",
            "clinical_data": {
                "age": 51, "bmi": 31.2, "abdominal_pain_severity": 4, "bloating_frequency": 4,
                "acid_reflux_frequency": 4, "constipation_score": 4, "diarrhea_score": 3,
                "nausea_vomiting": 1, "dietary_fiber_intake": "low", "fatty_food_intake": "high",
                "alcohol_consumption": "heavy", "smoking_status": "current",
                "physical_activity_hours": 0.5, "perceived_stress_level": 9, "sleep_duration_hrs": 5.0
            }
        }
    ]
    
    sample_info = []
    for case in expo_cases:
        t_fname = f"{case['id']}_tongue.jpg"
        s_fname = f"{case['id']}_skin.jpg"
        
        t_path = os.path.join(BACKEND_SAMPLE_DIR, "tongue_samples", t_fname)
        s_path = os.path.join(BACKEND_SAMPLE_DIR, "skin_samples", s_fname)
        
        generate_tongue_image(case["tongue_category"], t_path)
        generate_skin_image(case["skin_category"], s_path)
        
        sample_info.append({
            "id": case["id"],
            "name": case["name"],
            "expected_risk": case["expected_risk"],
            "tongue_image": f"/sample_data/tongue_samples/{t_fname}",
            "skin_image": f"/sample_data/skin_samples/{s_fname}",
            "clinical_data": case["clinical_data"]
        })
        
    json_path = os.path.join(BACKEND_SAMPLE_DIR, "clinical_samples.json")
    with open(json_path, "w") as f:
        json.dump(sample_info, f, indent=2)
        
    print(f"Offline Expo Demo Samples created at {json_path}")

if __name__ == "__main__":
    create_directories()
    prepare_tongue_dataset()
    prepare_skin_dataset()
    prepare_clinical_dataset()
    prepare_offline_expo_samples()
    print("ALL DATASETS AND SAMPLE FILES PREPARED SUCCESSFULLY!")

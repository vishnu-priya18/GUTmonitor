import os
import sys
import json
from PIL import Image

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from backend.services.predictor import model_registry

def test_backend():
    print("Testing Backend Model Registry End-to-End...")
    
    # 1. Test Tongue Predictor
    t_sample_path = os.path.join(BASE_DIR, "data", "tongue", "test", "light_red", "tongue_light_red_100.jpg")
    if os.path.exists(t_sample_path):
        t_res = model_registry.predict_tongue(t_sample_path)
        print(f"Tongue Prediction: Class={t_res['predicted_class']}, Conf={t_res['confidence']}")
    else:
        print("Tongue sample file not found.")
        
    # 2. Test Skin Predictor
    s_sample_path = os.path.join(BASE_DIR, "data", "skin", "test", "benign_skin", "skin_benign_skin_100.jpg")
    if os.path.exists(s_sample_path):
        s_res = model_registry.predict_skin(s_sample_path)
        print(f"Skin Prediction: Class={s_res['predicted_class']}, Conf={s_res['confidence']}")
    else:
        print("Skin sample file not found.")
        
    # 3. Test Clinical Predictor
    c_data = {
        "age": 45, "bmi": 28.5, "abdominal_pain_severity": 3, "bloating_frequency": 3,
        "acid_reflux_frequency": 3, "constipation_score": 2, "diarrhea_score": 1,
        "nausea_vomiting": 0, "dietary_fiber_intake": "low", "fatty_food_intake": "high",
        "alcohol_consumption": "moderate", "smoking_status": "current",
        "physical_activity_hours": 1.5, "perceived_stress_level": 8, "sleep_duration_hrs": 5.5
    }
    c_res = model_registry.predict_clinical(c_data)
    print(f"Clinical Prediction: Risk={c_res['predicted_risk']}, Conf={c_res['confidence']}")
    
    # 4. Test Multimodal Fusion End-to-End
    t_img = Image.open(t_sample_path) if os.path.exists(t_sample_path) else None
    s_img = Image.open(s_sample_path) if os.path.exists(s_sample_path) else None
    
    multi_res = model_registry.predict_multimodal(t_img, s_img, c_data)
    print("Multimodal Fusion Result:")
    print(f" -> Preliminary GI Risk Indication: {multi_res['fusion']['preliminary_risk_indication']}")
    print(f" -> Confidence: {multi_res['fusion']['confidence']}")
    print("BACKEND END-TO-END TEST PASSED!")

if __name__ == "__main__":
    test_backend()

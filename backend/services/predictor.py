import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from models.tongue.predict import TonguePredictor
from models.skin.predict import SkinPredictor
from models.clinical.predict import ClinicalPredictor
from models.fusion.predict import FusionPredictor

class ModelRegistry:
    def __init__(self):
        print("Initializing GI-Vision AI Model Registry...")
        self.tongue_predictor = TonguePredictor()
        self.skin_predictor = SkinPredictor()
        self.clinical_predictor = ClinicalPredictor()
        self.fusion_predictor = FusionPredictor()
        
    def predict_tongue(self, image_input):
        return self.tongue_predictor.predict(image_input)
        
    def predict_skin(self, image_input):
        return self.skin_predictor.predict(image_input)
        
    def predict_clinical(self, clinical_data):
        return self.clinical_predictor.predict(clinical_data)
        
    def predict_multimodal(self, tongue_img=None, skin_img=None, clinical_data=None):
        tongue_res = self.predict_tongue(tongue_img) if tongue_img else {
            "predicted_class": "light_red", "confidence": 0.8,
            "embedding": [0.05]*16, "class_probabilities": {"light_red": 0.8}
        }
        
        skin_res = self.predict_skin(skin_img) if skin_img else {
            "predicted_class": "benign_skin", "confidence": 0.85,
            "embedding": [0.05]*16, "class_probabilities": {"benign_skin": 0.85}
        }
        
        clinical_res = self.predict_clinical(clinical_data or {})
        
        fusion_res = self.fusion_predictor.predict(
            tongue_emb=tongue_res["embedding"],
            skin_emb=skin_res["embedding"],
            clinical_emb=clinical_res["embedding"]
        )
        
        return {
            "tongue": tongue_res,
            "skin": skin_res,
            "clinical": clinical_res,
            "fusion": fusion_res,
            "status": "success"
        }

model_registry = ModelRegistry()

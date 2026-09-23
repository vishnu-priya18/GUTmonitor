import os
import sys
import torch
import torch.nn.functional as F

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from models.fusion.config import MODEL_SAVE_PATH, RISK_LEVEL_NAMES
from models.fusion.model import GatedMultimodalFusion

class FusionPredictor:
    def __init__(self, model_path=MODEL_SAVE_PATH):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model = GatedMultimodalFusion().to(self.device)
        
        if os.path.exists(model_path):
            self.model.load_state_dict(torch.load(model_path, map_location=self.device, weights_only=True))
            print(f"Loaded Fusion Model from {model_path}")
        else:
            print(f"Warning: Fusion Model file not found at {model_path}. Using uninitialized weights.")
            
        self.model.eval()
        
    def predict(self, tongue_emb, skin_emb, clinical_emb):
        t_tensor = torch.tensor([tongue_emb], dtype=torch.float32).to(self.device)
        s_tensor = torch.tensor([skin_emb], dtype=torch.float32).to(self.device)
        c_tensor = torch.tensor([clinical_emb], dtype=torch.float32).to(self.device)
        
        with torch.no_grad():
            logits, fused_h = self.model(t_tensor, s_tensor, c_tensor)
            probs = F.softmax(logits, dim=1).squeeze(0).cpu().numpy()
            
        pred_idx = int(probs.argmax())
        predicted_risk = RISK_LEVEL_NAMES[pred_idx]
        confidence = float(probs[pred_idx])
        
        prob_dict = {RISK_LEVEL_NAMES[i]: round(float(probs[i]), 4) for i in range(len(RISK_LEVEL_NAMES))}
        
        return {
            "preliminary_risk_indication": predicted_risk,
            "confidence": round(confidence, 4),
            "risk_probabilities": prob_dict,
            "fused_features": fused_h.squeeze(0).cpu().numpy().tolist(),
            "fusion_type": "Gated Feature-Level Prototype Fusion",
            "disclaimer": "Prototype Multimodal Fusion Demonstration — Modality models are trained on validated independent research datasets. Full clinical validation requires a paired multimodal dataset collected from the same participants under appropriate ethical approval."
        }

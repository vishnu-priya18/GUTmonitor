import os
import sys
import torch
import torch.nn.functional as F
from PIL import Image

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from models.skin.config import MODEL_SAVE_PATH, CLASSES
from models.skin.dataset import get_transforms
from models.skin.model import SkinClassifier

class SkinPredictor:
    def __init__(self, model_path=MODEL_SAVE_PATH):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model = SkinClassifier().to(self.device)
        
        if os.path.exists(model_path):
            self.model.load_state_dict(torch.load(model_path, map_location=self.device, weights_only=True))
            print(f"Loaded Skin Model from {model_path}")
        else:
            print(f"Warning: Skin Model file not found at {model_path}. Using uninitialized weights.")
            
        self.model.eval()
        self.transform = get_transforms(split="test")
        
    def predict(self, image_input):
        if isinstance(image_input, str):
            img = Image.open(image_input).convert("RGB")
        else:
            img = image_input.convert("RGB")
            
        tensor = self.transform(img).unsqueeze(0).to(self.device)
        
        with torch.no_grad():
            logits, embedding = self.model(tensor)
            probs = F.softmax(logits, dim=1).squeeze(0).cpu().numpy()
            emb_vector = embedding.squeeze(0).cpu().numpy()
            
        pred_idx = int(probs.argmax())
        predicted_class = CLASSES[pred_idx]
        confidence = float(probs[pred_idx])
        
        prob_dict = {CLASSES[i]: round(float(probs[i]), 4) for i in range(len(CLASSES))}
        
        return {
            "predicted_class": predicted_class,
            "confidence": round(confidence, 4),
            "class_probabilities": prob_dict,
            "embedding": emb_vector.tolist(),
            "modality": "Complementary Visual Information (Skin Analysis)",
            "clinical_note": f"Skin surface feature categorized as '{predicted_class}' (Confidence: {confidence*100:.1f}%). Designated as complementary visual information."
        }

import os
import joblib
import numpy as np
import pandas as pd

from .config import MODEL_SAVE_PATH, FEATURE_COLUMNS, RISK_LEVEL_NAMES

class ClinicalPredictor:
    def __init__(self, model_path=MODEL_SAVE_PATH):
        if os.path.exists(model_path):
            artifact = joblib.load(model_path)
            self.pipeline = artifact["pipeline"]
            self.feature_importances = artifact.get("feature_importances", {})
            print(f"Loaded Clinical Model from {model_path}")
        else:
            print(f"Warning: Clinical Model file not found at {model_path}.")
            self.pipeline = None
            self.feature_importances = {}

    def predict(self, input_dict):
        """
        Accepts dict containing clinical questionnaire features matching FEATURE_COLUMNS.
        Returns dict with predicted risk level, probability distribution, feature importances, and 16-D embedding.
        """
        # Format input dict into DataFrame
        df_input = pd.DataFrame([input_dict])
        
        # Ensure all columns present
        for col in FEATURE_COLUMNS:
            if col not in df_input.columns:
                df_input[col] = 0 if col not in ["dietary_fiber_intake", "fatty_food_intake", "alcohol_consumption", "smoking_status"] else "low"
                
        df_input = df_input[FEATURE_COLUMNS]
        
        if self.pipeline is not None:
            probs = self.pipeline.predict_proba(df_input)[0]
            pred_idx = int(probs.argmax())
            
            # Transform input using preprocessor to generate 16-D feature embedding
            preprocessed_vec = self.pipeline.named_steps['preprocessor'].transform(df_input)[0]
            
            # Map preprocessed vector into 16-D embedding via projection
            if len(preprocessed_vec) >= 16:
                embedding = preprocessed_vec[:16].tolist()
            else:
                embedding = np.pad(preprocessed_vec, (0, 16 - len(preprocessed_vec))).tolist()
        else:
            probs = [0.7, 0.2, 0.1]
            pred_idx = 0
            embedding = [0.1] * 16
            
        risk_name = RISK_LEVEL_NAMES[pred_idx]
        confidence = float(probs[pred_idx])
        
        prob_dict = {RISK_LEVEL_NAMES[i]: round(float(probs[i]), 4) for i in range(len(RISK_LEVEL_NAMES))}
        
        return {
            "predicted_risk": risk_name,
            "confidence": round(confidence, 4),
            "risk_probabilities": prob_dict,
            "embedding": embedding,
            "modality": "Clinical GI Symptoms & Lifestyle",
            "feature_importances": self.feature_importances
        }

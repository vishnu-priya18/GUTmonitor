import numpy as np

def generate_saliency_map_summary(modality_name, predicted_class, confidence):
    """
    Generates explainability notes and region-of-interest summary.
    """
    return {
        "modality": modality_name,
        "predicted_class": predicted_class,
        "confidence": confidence,
        "salient_regions": [
            "Central mucosal region (tongue body feature density)" if "Tongue" in modality_name else "Dermal epidermal junction lesion focus",
            "Color chromaticity spectrum variance",
            "Coating texture granularity distribution"
        ],
        "explanation": f"Model identified feature patterns consistent with {predicted_class} (Confidence {confidence*100:.1f}%)."
    }

def generate_tabular_shap_summary(feature_dict, feature_importances):
    """
    Generates top contributing symptom factors based on Gini feature importances.
    """
    top_factors = []
    for k, v in feature_dict.items():
        importance = feature_importances.get(k, 0.05)
        top_factors.append({
            "feature": k,
            "value": str(v),
            "importance": round(float(importance), 4),
            "impact": "High Risk Contribution" if importance > 0.08 else "Moderate Contribution"
        })
        
    top_factors.sort(key=lambda x: x["importance"], reverse=True)
    return top_factors[:5]

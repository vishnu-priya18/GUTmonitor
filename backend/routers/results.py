import os
import json
from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from ..config import RESULTS_DIR

router = APIRouter(prefix="/results", tags=["Model Performance Results"])

@router.get("/{modality}/metrics")
async def get_modality_metrics(modality: str):
    if modality not in ["tongue", "skin", "clinical", "fusion"]:
        raise HTTPException(status_code=400, detail="Invalid modality")
        
    json_path = os.path.join(RESULTS_DIR, modality, "metrics.json")
    if not os.path.exists(json_path):
        return {
            "status": "pending",
            "message": f"Model training pending for {modality}",
            "accuracy": None, "macro_f1": None
        }
        
    with open(json_path, "r") as f:
        data = json.load(f)
    return data

@router.get("/{modality}/plot/{plot_type}")
async def get_modality_plot(modality: str, plot_type: str):
    filename = "confusion_matrix.png" if plot_type == "cm" else "feature_importance.png"
    img_path = os.path.join(RESULTS_DIR, modality, filename)
    if os.path.exists(img_path):
        return FileResponse(img_path)
    raise HTTPException(status_code=404, detail="Plot image not found.")

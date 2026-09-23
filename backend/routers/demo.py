import os
import json
from fastapi import APIRouter, HTTPException
from PIL import Image
from ..config import SAMPLE_DATA_DIR, BASE_DIR
from ..services.predictor import model_registry

router = APIRouter(prefix="/demo", tags=["Offline Expo Demo"])

@router.get("/samples")
async def get_demo_samples():
    json_path = os.path.join(SAMPLE_DATA_DIR, "clinical_samples.json")
    if not os.path.exists(json_path):
        raise HTTPException(status_code=404, detail="Demo samples file not found. Run python data/prepare_datasets.py")
        
    with open(json_path, "r") as f:
        samples = json.load(f)
    return samples

@router.post("/evaluate_case/{case_id}")
async def evaluate_demo_case(case_id: str):
    json_path = os.path.join(SAMPLE_DATA_DIR, "clinical_samples.json")
    if not os.path.exists(json_path):
        raise HTTPException(status_code=404, detail="Demo samples file not found.")
        
    with open(json_path, "r") as f:
        samples = json.load(f)
        
    case = next((c for c in samples if c["id"] == case_id), None)
    if not case:
        raise HTTPException(status_code=404, detail=f"Case ID {case_id} not found.")
        
    # Load sample images from disk
    t_img_rel = case["tongue_image"].lstrip("/")
    s_img_rel = case["skin_image"].lstrip("/")
    
    t_img_path = os.path.join(BASE_DIR, "backend", t_img_rel)
    s_img_path = os.path.join(BASE_DIR, "backend", s_img_rel)
    
    tongue_img = Image.open(t_img_path).convert("RGB") if os.path.exists(t_img_path) else None
    skin_img = Image.open(s_img_path).convert("RGB") if os.path.exists(s_img_path) else None
    
    result = model_registry.predict_multimodal(tongue_img, skin_img, case["clinical_data"])
    result["case_id"] = case_id
    result["case_name"] = case["name"]
    result["expected_risk"] = case["expected_risk"]
    return result

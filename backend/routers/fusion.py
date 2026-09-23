from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from PIL import Image
import io
import json
from typing import Optional
from ..services.predictor import model_registry

router = APIRouter(prefix="/predict", tags=["Multimodal Fusion"])

@router.post("/multimodal")
async def predict_multimodal(
    tongue_file: Optional[UploadFile] = File(None),
    skin_file: Optional[UploadFile] = File(None),
    clinical_payload: Optional[str] = Form(None)
):
    tongue_img = None
    if tongue_file and tongue_file.content_type.startswith("image/"):
        contents = await tongue_file.read()
        tongue_img = Image.open(io.BytesIO(contents)).convert("RGB")
        
    skin_img = None
    if skin_file and skin_file.content_type.startswith("image/"):
        contents = await skin_file.read()
        skin_img = Image.open(io.BytesIO(contents)).convert("RGB")
        
    clinical_data = {}
    if clinical_payload:
        try:
            clinical_data = json.loads(clinical_payload)
        except Exception:
            pass
            
    result = model_registry.predict_multimodal(tongue_img, skin_img, clinical_data)
    return result

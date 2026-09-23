from fastapi import APIRouter, UploadFile, File, HTTPException
from PIL import Image
import io
from ..services.predictor import model_registry
from ..services.explainability import generate_saliency_map_summary

router = APIRouter(prefix="/predict", tags=["Tongue Model"])

@router.post("/tongue")
async def predict_tongue_image(file: UploadFile = File(...)):
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Uploaded file must be an image.")
        
    contents = await file.read()
    try:
        img = Image.open(io.BytesIO(contents)).convert("RGB")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid image file: {str(e)}")
        
    result = model_registry.predict_tongue(img)
    explainability = generate_saliency_map_summary("Tongue Image Analysis", result["predicted_class"], result["confidence"])
    result["explainability"] = explainability
    return result

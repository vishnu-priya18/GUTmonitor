import os
import sys
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from backend.config import SAMPLE_DATA_DIR, DISCLAIMER_TEXT
from backend.routers import tongue, skin, clinical, fusion, results, demo

app = FastAPI(
    title="GI-Vision AI REST API",
    description="Multimodal Gastrointestinal Screening Backend Service",
    version="1.0.0"
)

# Enable CORS for React Frontend (vite port 5173 / 3000 / localhost)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount sample_data static files for Expo Demo offline images
os.makedirs(SAMPLE_DATA_DIR, exist_ok=True)
app.mount("/sample_data", StaticFiles(directory=SAMPLE_DATA_DIR), name="sample_data")

# Include Routers
app.include_router(tongue.router, prefix="/api")
app.include_router(skin.router, prefix="/api")
app.include_router(clinical.router, prefix="/api")
app.include_router(fusion.router, prefix="/api")
app.include_router(results.router, prefix="/api")
app.include_router(demo.router, prefix="/api")

@app.get("/")
async def root_status():
    return {
        "status": "online",
        "app_name": "GI-Vision AI Backend",
        "version": "1.0.0",
        "disclaimer": DISCLAIMER_TEXT,
        "endpoints": [
            "POST /api/predict/tongue",
            "POST /api/predict/skin",
            "POST /api/predict/clinical",
            "POST /api/predict/multimodal",
            "GET /api/results/{modality}/metrics",
            "GET /api/demo/samples"
        ]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.app:app", host="0.0.0.0", port=8000, reload=True)

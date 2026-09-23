import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODELS_DIR = os.path.join(BASE_DIR, "models")
RESULTS_DIR = os.path.join(BASE_DIR, "results")
SAMPLE_DATA_DIR = os.path.join(BASE_DIR, "backend", "sample_data")

TONGUE_MODEL_PATH = os.path.join(MODELS_DIR, "tongue", "tongue_model.pt")
SKIN_MODEL_PATH = os.path.join(MODELS_DIR, "skin", "skin_model.pt")
CLINICAL_MODEL_PATH = os.path.join(MODELS_DIR, "clinical", "clinical_model.joblib")
FUSION_MODEL_PATH = os.path.join(MODELS_DIR, "fusion", "fusion_model.pt")

DISCLAIMER_TEXT = (
    "GI-Vision AI is an experimental research prototype for preliminary screening support. "
    "It does not diagnose gastrointestinal disease and must not replace professional medical evaluation."
)

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RESULTS_DIR = os.path.join(BASE_DIR, "results", "fusion")
MODEL_SAVE_PATH = os.path.join(BASE_DIR, "models", "fusion", "fusion_model.pt")

TONGUE_EMBED_DIM = 16
SKIN_EMBED_DIM = 16
CLINICAL_EMBED_DIM = 16
CONCAT_DIM = TONGUE_EMBED_DIM + SKIN_EMBED_DIM + CLINICAL_EMBED_DIM # 48-D

HIDDEN_DIM = 32
NUM_CLASSES = 3
RISK_LEVEL_NAMES = ["Low GI Risk", "Moderate GI Risk", "Higher GI Risk"]

BATCH_SIZE = 16
EPOCHS = 15
LEARNING_RATE = 0.001
SEED = 42

os.makedirs(RESULTS_DIR, exist_ok=True)
os.makedirs(os.path.dirname(MODEL_SAVE_PATH), exist_ok=True)

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_DIR = os.path.join(BASE_DIR, "data", "skin")
RESULTS_DIR = os.path.join(BASE_DIR, "results", "skin")
MODEL_SAVE_PATH = os.path.join(BASE_DIR, "models", "skin", "skin_model.pt")

CLASSES = ["benign_skin", "erythema_rash", "keratosis", "vascular", "melanocytic"]
NUM_CLASSES = len(CLASSES)
IMAGE_SIZE = (224, 224)
BATCH_SIZE = 16
EPOCHS = 10
LEARNING_RATE = 0.001
EMBEDDING_DIM = 16
SEED = 42

os.makedirs(RESULTS_DIR, exist_ok=True)
os.makedirs(os.path.dirname(MODEL_SAVE_PATH), exist_ok=True)

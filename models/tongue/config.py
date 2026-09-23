import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_DIR = os.path.join(BASE_DIR, "data", "tongue")
RESULTS_DIR = os.path.join(BASE_DIR, "results", "tongue")
MODEL_SAVE_PATH = os.path.join(BASE_DIR, "models", "tongue", "tongue_model.pt")

CLASSES = ["pale", "light_red", "red", "deep_red", "purple"]
NUM_CLASSES = len(CLASSES)
IMAGE_SIZE = (224, 224)
BATCH_SIZE = 16
EPOCHS = 10
LEARNING_RATE = 0.001
EMBEDDING_DIM = 16
SEED = 42

os.makedirs(RESULTS_DIR, exist_ok=True)
os.makedirs(os.path.dirname(MODEL_SAVE_PATH), exist_ok=True)

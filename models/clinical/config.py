import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_PATH = os.path.join(BASE_DIR, "data", "clinical", "gi_symptoms_lifestyle_dataset.csv")
RESULTS_DIR = os.path.join(BASE_DIR, "results", "clinical")
MODEL_SAVE_PATH = os.path.join(BASE_DIR, "models", "clinical", "clinical_model.joblib")

FEATURE_COLUMNS = [
    "age", "bmi", "abdominal_pain_severity", "bloating_frequency", "acid_reflux_frequency",
    "constipation_score", "diarrhea_score", "nausea_vomiting", "dietary_fiber_intake",
    "fatty_food_intake", "alcohol_consumption", "smoking_status",
    "physical_activity_hours", "perceived_stress_level", "sleep_duration_hrs"
]

NUMERICAL_FEATURES = [
    "age", "bmi", "abdominal_pain_severity", "bloating_frequency", "acid_reflux_frequency",
    "constipation_score", "diarrhea_score", "nausea_vomiting", "physical_activity_hours",
    "perceived_stress_level", "sleep_duration_hrs"
]

CATEGORICAL_FEATURES = [
    "dietary_fiber_intake", "fatty_food_intake", "alcohol_consumption", "smoking_status"
]

TARGET_COLUMN = "gi_risk_level"
RISK_LEVEL_NAMES = ["Low GI Risk", "Moderate GI Risk", "Higher GI Risk"]
SEED = 42

os.makedirs(RESULTS_DIR, exist_ok=True)
os.makedirs(os.path.dirname(MODEL_SAVE_PATH), exist_ok=True)

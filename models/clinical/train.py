import os
import sys
import json
import joblib
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
import torch

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from models.clinical.config import (
    DATA_PATH, RESULTS_DIR, MODEL_SAVE_PATH, FEATURE_COLUMNS,
    NUMERICAL_FEATURES, CATEGORICAL_FEATURES, TARGET_COLUMN, RISK_LEVEL_NAMES, SEED
)
from models.clinical.evaluate import evaluate_clinical_model

def train():
    np.random.seed(SEED)
    torch.manual_seed(SEED)
    
    if not os.path.exists(DATA_PATH):
        print("Error: Clinical dataset file not found. Run python data/prepare_datasets.py first.")
        return
        
    df = pd.read_csv(DATA_PATH)
    X = df[FEATURE_COLUMNS]
    y = df[TARGET_COLUMN]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=SEED, stratify=y)
    
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), NUMERICAL_FEATURES),
            ('cat', OneHotEncoder(handle_unknown='ignore', sparse_output=False), CATEGORICAL_FEATURES)
        ]
    )
    
    rf = RandomForestClassifier(n_estimators=100, max_depth=8, random_state=SEED)
    pipeline = Pipeline(steps=[('preprocessor', preprocessor), ('classifier', rf)])
    
    pipeline.fit(X_train, y_train)
    
    preprocessed_feature_names = NUMERICAL_FEATURES + list(
        pipeline.named_steps['preprocessor'].named_transformers_['cat'].get_feature_names_out(CATEGORICAL_FEATURES)
    )
    importances = pipeline.named_steps['classifier'].feature_importances_
    feature_imp = dict(zip(preprocessed_feature_names, [round(float(imp), 4) for imp in importances]))
    
    model_artifact = {
        "pipeline": pipeline,
        "preprocessed_feature_names": preprocessed_feature_names,
        "feature_importances": feature_imp
    }
    joblib.dump(model_artifact, MODEL_SAVE_PATH)
    print(f"Saved Clinical Model artifact to {MODEL_SAVE_PATH}")
    
    evaluate_clinical_model(pipeline, X_test, y_test, preprocessed_feature_names, importances)

if __name__ == "__main__":
    train()

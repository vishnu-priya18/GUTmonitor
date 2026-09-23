from fastapi import APIRouter
from pydantic import BaseModel, Field
from typing import Optional
from ..services.predictor import model_registry
from ..services.explainability import generate_tabular_shap_summary

router = APIRouter(prefix="/predict", tags=["Clinical Model"])

class ClinicalQuestionnaireSchema(BaseModel):
    age: int = Field(35, ge=18, le=100)
    bmi: float = Field(24.5, ge=12.0, le=50.0)
    abdominal_pain_severity: int = Field(0, ge=0, le=5)
    bloating_frequency: int = Field(0, ge=0, le=4)
    acid_reflux_frequency: int = Field(0, ge=0, le=4)
    constipation_score: int = Field(0, ge=0, le=5)
    diarrhea_score: int = Field(0, ge=0, le=5)
    nausea_vomiting: int = Field(0, ge=0, le=1)
    dietary_fiber_intake: str = Field("medium", description="low / medium / high")
    fatty_food_intake: str = Field("medium", description="low / medium / high")
    alcohol_consumption: str = Field("none", description="none / moderate / heavy")
    smoking_status: str = Field("non-smoker", description="non-smoker / former / current")
    physical_activity_hours: float = Field(3.0, ge=0.0, le=30.0)
    perceived_stress_level: int = Field(5, ge=1, le=10)
    sleep_duration_hrs: float = Field(7.0, ge=3.0, le=12.0)

@router.post("/clinical")
async def predict_clinical_symptoms(data: ClinicalQuestionnaireSchema):
    input_dict = data.model_dump()
    result = model_registry.predict_clinical(input_dict)
    
    top_factors = generate_tabular_shap_summary(input_dict, result.get("feature_importances", {}))
    result["top_contributing_factors"] = top_factors
    return result

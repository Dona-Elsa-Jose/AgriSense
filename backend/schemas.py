from pydantic import BaseModel, Field
from typing import Optional, List

# ===========================================================================
# Module 1: Irrigation & Telemetry Schemas
# ===========================================================================

class TelemetryInput(BaseModel):
    soil_moisture: float = Field(..., ge=0, le=100, description="Soil moisture percentage (0-100%)")
    temperature: float = Field(..., description="Ambient or soil temperature in Celsius")
    humidity: Optional[float] = Field(None, ge=0, le=100, description="Air humidity percentage")
    crop_type: Optional[str] = Field("default", description="Target crop for customized water thresholds")

class IrrigationRecommendation(BaseModel):
    status: str  # e.g., "CRITICAL_DRY", "OPTIMAL", "OVERWATERED_WARNING"
    action_required: str  # e.g., "IRRIGATE_IMMEDIATELY", "PAUSE_IRRIGATION", "MAINTAIN"
    recommended_water_liters_per_sqm: float
    alert_message: str
    moisture_percentage: float


# ===========================================================================
# Module 2: Crop & Fertilizer Recommendation Engine Schemas
# ===========================================================================

class SoilInput(BaseModel):
    N: float = Field(..., description="Nitrogen level in soil")
    P: float = Field(..., description="Phosphorus level in soil")
    K: float = Field(..., description="Potassium level in soil")
    ph: float = Field(..., ge=0, le=14, description="Soil pH level")
    temperature: float = Field(..., description="Temperature in Celsius")
    humidity: float = Field(..., ge=0, le=100, description="Relative humidity percentage")
    rainfall: float = Field(..., ge=0, description="Rainfall in mm")

class CropCandidate(BaseModel):
    crop: str
    confidence: float
    profitability_score: float

class CropOutput(BaseModel):
    top_crops: List[CropCandidate]
    recommended_crop: str

class FertilizerPlanItem(BaseModel):
    nutrient: str
    amendment: str
    quantity_kg_per_acre: float

class FertilizerOutput(BaseModel):
    fertilizer_plan: List[FertilizerPlanItem]
    explanation: str

class Module2Response(BaseModel):
    crop: CropOutput
    fertilizer: FertilizerOutput


# ===========================================================================
# Module 3: AI Leaf Pathology Scanner Schemas
# ===========================================================================

class TreatmentPlan(BaseModel):
    step_1_immediate_action: str = Field(..., description="Immediate cultural sanitation or isolation action")
    step_2_organic_control: str = Field(..., description="Organic or bio-control treatment")
    step_3_chemical_treatment: str = Field(..., description="Targeted chemical fungicide intervention")
    step_4_preventive_strategy: str = Field(..., description="Long-term agronomic prevention strategy")

class PathologyDiagnosis(BaseModel):
    is_plant_leaf: bool = Field(True, description="True if image contains plant foliage")
    crop: str = Field(..., description="Detected crop type")
    disease_name: str = Field(..., description="Specific identified disease or Healthy Foliage")
    confidence_score: float = Field(..., description="Confidence percentage (0-100%)")
    severity: str = Field(..., description="Optimal, Low, Moderate, High, or Critical")
    pathogen_type: str = Field(..., description="Fungal, Bacterial, Viral, Pest, or None")
    symptoms: str = Field(..., description="Visual symptoms observed on the leaf")
    irrigation_telemetry_advice: str = Field(..., description="Actionable cross-module link to Module 1 Smart Irrigation")
    treatment_plan: TreatmentPlan
    engine_mode: str = Field("AI Vision Scanner", description="Active AI engine (Cloud Vision AI or Local Edge CV)")
    computer_vision_telemetry: Optional[dict] = Field(None, description="Pixel-level metrics (ExG, Necrosis, Chlorosis)")

class DiseaseCatalogItem(BaseModel):
    key: str
    crop: str
    disease_name: str
    severity: str
    pathogen_type: str

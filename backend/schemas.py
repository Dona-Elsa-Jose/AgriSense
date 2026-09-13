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

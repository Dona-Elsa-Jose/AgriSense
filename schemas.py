"""
Module 2 — Crop & Fertilizer Recommendation Engine
Shared contract between crop_engine/ (Person A) and fertilizer_engine/ (Person B).

RULE: Only edit this file together. If your function's input/output needs
to change shape, that's a conversation, not a solo edit.
"""

from pydantic import BaseModel
from typing import List


# ---------------------------------------------------------------------------
# Shared input — both engines receive this same soil/environmental reading
# ---------------------------------------------------------------------------
class SoilInput(BaseModel):
    N: float
    P: float
    K: float
    ph: float
    temperature: float
    humidity: float
    rainfall: float


# ---------------------------------------------------------------------------
# Person A owns: crop_engine/predict.py implements predict_crop()
# Signature: predict_crop(soil: SoilInput) -> CropOutput
# ---------------------------------------------------------------------------
class CropCandidate(BaseModel):
    crop: str
    confidence: float
    profitability_score: float


class CropOutput(BaseModel):
    top_crops: List[CropCandidate]
    recommended_crop: str


# ---------------------------------------------------------------------------
# Person B owns: fertilizer_engine/recommend.py implements recommend_fertilizer()
# Signature: recommend_fertilizer(crop: str, soil: SoilInput) -> FertilizerOutput
# Note: takes crop as a plain str (crop_output.recommended_crop), not the
# whole CropOutput — keeps this function testable without Person A's model.
# ---------------------------------------------------------------------------
class FertilizerPlanItem(BaseModel):
    nutrient: str
    amendment: str
    quantity_kg_per_acre: float


class FertilizerOutput(BaseModel):
    fertilizer_plan: List[FertilizerPlanItem]
    explanation: str


# ---------------------------------------------------------------------------
# api.py owns: the merged response returned by POST /api/module2/recommend
# Built last, together, once both engines work standalone.
# ---------------------------------------------------------------------------
class Module2Response(BaseModel):
    crop: CropOutput
    fertilizer: FertilizerOutput

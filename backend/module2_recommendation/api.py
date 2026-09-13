from fastapi import APIRouter, HTTPException

# 1. Shared schemas from the unified single source of truth
from backend.schemas import SoilInput, Module2Response

# 2. Person A's Crop Prediction Engine (relocated inside module2_recommendation)
from backend.module2_recommendation.crop.predict import predict_crop 

# 3. Person B's Fertilizer Recommendation Engine (moved inside module2_recommendation/fertilizer)
from backend.module2_recommendation.fertilizer.recommend import recommend_fertilizer 

module2_router = APIRouter(
    prefix="/api/module2",
    tags=["Crop & Fertilizer Recommendation Engine"]
)

@module2_router.post("/recommend", response_model=Module2Response)
def get_recommendation(soil: SoilInput):
    try:
        crop_result = predict_crop(soil)
        fertilizer_result = recommend_fertilizer(crop=crop_result.recommended_crop, soil=soil)
        
        return Module2Response(
            crop=crop_result,
            fertilizer=fertilizer_result
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
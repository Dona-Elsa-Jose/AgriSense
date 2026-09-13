from fastapi import APIRouter, HTTPException
from schemas import SoilInput, Module2Response

# Import Person A's work
from crop_engine.predict import predict_crop 

# Import Your work
from fertilizer_engine.recommend import recommend_fertilizer 

# Use APIRouter so this can be attached to the main project later
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
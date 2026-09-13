from fastapi import APIRouter, HTTPException
from backend.schemas import SoilInput, CropOutput
from backend.module2_recommendation.crop.predict import predict_crop

router = APIRouter(prefix="/api/v1/recommend", tags=["Crop Recommendation"])

@router.post("/crop", response_model=CropOutput)
def recommend_crop(soil: SoilInput):
    """
    Ingests soil NPK values and climate metrics, then returns top crop recommendations
    with confidence and profitability scores.
    """
    try:
        return predict_crop(soil)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
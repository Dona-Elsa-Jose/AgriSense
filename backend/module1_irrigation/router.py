from fastapi import APIRouter, HTTPException
from backend.schemas import TelemetryInput, IrrigationRecommendation
from backend.module1_irrigation.engine import calculate_irrigation

router = APIRouter(prefix="/api/v1/irrigation", tags=["Smart Irrigation"])

@router.post("/evaluate", response_model=IrrigationRecommendation)
def evaluate_telemetry(telemetry: TelemetryInput):
    """
    Ingests live or slider-simulated telemetry data and returns
    real-time field status, alerts, and water volume advice.
    """
    try:
        return calculate_irrigation(telemetry)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
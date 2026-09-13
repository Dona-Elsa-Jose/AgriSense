from backend.schemas import TelemetryInput, IrrigationRecommendation

def calculate_irrigation(telemetry: TelemetryInput) -> IrrigationRecommendation:
    moisture = telemetry.soil_moisture
    temp = telemetry.temperature
    
    # Base thresholds
    dry_threshold = 30.0
    optimal_high = 70.0
    overwater_threshold = 85.0

    # Evapotranspiration multiplier based on temperature
    temp_factor = 1.2 if temp > 30 else (0.9 if temp < 18 else 1.0)

    if moisture < dry_threshold:
        status = "CRITICAL_DRY"
        action = "IRRIGATE_IMMEDIATELY"
        # Calculate water deficit volume (liters per square meter)
        deficit = (55.0 - moisture) * 0.15 * temp_factor
        water_volume = round(max(deficit, 1.5), 2)
        alert = f"Alert: Soil moisture is dangerously low ({moisture}%). Initiate watering to prevent crop wilting."
        
    elif dry_threshold <= moisture <= optimal_high:
        status = "OPTIMAL"
        action = "MAINTAIN"
        water_volume = 0.0
        alert = f"Status Normal: Soil moisture is optimal ({moisture}%). No irrigation needed at this time."
        
    else:  # moisture > optimal_high
        status = "OVERWATERED_WARNING"
        action = "PAUSE_IRRIGATION"
        water_volume = 0.0
        if moisture >= overwater_threshold:
            alert = f"CRITICAL WARNING: Soil moisture at {moisture}%. Pause all irrigation immediately to prevent root rot and anaerobic soil conditions!"
        else:
            alert = f"Warning: Soil moisture elevated ({moisture}%). Hold off on scheduled watering."

    return IrrigationRecommendation(
        status=status,
        action_required=action,
        recommended_water_liters_per_sqm=water_volume,
        alert_message=alert,
        moisture_percentage=moisture
    )
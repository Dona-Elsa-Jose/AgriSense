"""
fertilizer.py
Contains agronomic baseline targets (ICAR standards in kg/acre) 
and optimal pH ranges for 22 crops.
"""

from typing import Dict, Any

CROP_AGRONOMIC_TARGETS: Dict[str, Dict[str, float]] = {
    # Cereals & Pulses (Pulses fix their own nitrogen, so N requirements are low)
    "rice": {"N": 48.0, "P": 24.0, "K": 24.0, "ph_min": 5.5, "ph_max": 6.8},
    "maize": {"N": 60.0, "P": 24.0, "K": 24.0, "ph_min": 5.8, "ph_max": 7.2},
    "chickpea": {"N": 10.0, "P": 20.0, "K": 10.0, "ph_min": 6.0, "ph_max": 7.5},
    "kidneybeans": {"N": 12.0, "P": 24.0, "K": 12.0, "ph_min": 5.8, "ph_max": 6.8},
    "pigeonpeas": {"N": 10.0, "P": 20.0, "K": 10.0, "ph_min": 6.0, "ph_max": 7.5},
    "mothbeans": {"N": 10.0, "P": 15.0, "K": 10.0, "ph_min": 6.0, "ph_max": 7.5},
    "mungbean": {"N": 10.0, "P": 16.0, "K": 10.0, "ph_min": 6.0, "ph_max": 7.5},
    "blackgram": {"N": 10.0, "P": 16.0, "K": 10.0, "ph_min": 6.0, "ph_max": 7.5},
    "lentil": {"N": 10.0, "P": 16.0, "K": 10.0, "ph_min": 6.0, "ph_max": 7.5},

    # Fruits (Heavy potassium feeders for fruit development)
    "apple": {"N": 70.0, "P": 35.0, "K": 70.0, "ph_min": 6.0, "ph_max": 7.0},
    "banana": {"N": 100.0, "P": 40.0, "K": 120.0, "ph_min": 6.5, "ph_max": 7.5},
    "grapes": {"N": 80.0, "P": 40.0, "K": 80.0, "ph_min": 6.5, "ph_max": 7.5},
    "mango": {"N": 60.0, "P": 30.0, "K": 60.0, "ph_min": 6.0, "ph_max": 7.5},
    "muskmelon": {"N": 40.0, "P": 24.0, "K": 24.0, "ph_min": 6.0, "ph_max": 7.0},
    "orange": {"N": 60.0, "P": 20.0, "K": 40.0, "ph_min": 6.0, "ph_max": 7.5},
    "papaya": {"N": 80.0, "P": 40.0, "K": 80.0, "ph_min": 6.0, "ph_max": 7.0},
    "pomegranate": {"N": 60.0, "P": 30.0, "K": 40.0, "ph_min": 6.5, "ph_max": 7.5},
    "watermelon": {"N": 40.0, "P": 24.0, "K": 24.0, "ph_min": 6.0, "ph_max": 7.0},

    # Commercial / Cash Crops
    "coconut": {"N": 100.0, "P": 40.0, "K": 150.0, "ph_min": 5.5, "ph_max": 8.0},
    "coffee": {"N": 60.0, "P": 40.0, "K": 60.0, "ph_min": 5.5, "ph_max": 6.5},
    "cotton": {"N": 48.0, "P": 24.0, "K": 24.0, "ph_min": 6.0, "ph_max": 8.0},
    "jute": {"N": 32.0, "P": 16.0, "K": 16.0, "ph_min": 6.0, "ph_max": 7.5},
}

DEFAULT_TARGET: Dict[str, float] = {
    "N": 40.0, 
    "P": 20.0, 
    "K": 20.0, 
    "ph_min": 6.0, 
    "ph_max": 7.0
}

def get_crop_target(crop_name: str) -> Dict[str, float]:
    """Safely fetch target crop data with fallback."""
    key = crop_name.strip().lower()
    return CROP_AGRONOMIC_TARGETS.get(key, DEFAULT_TARGET)
"""
Unified System Integration Test
Verifies that Module 1, Module 2, and Module 3 all load, function, and work together
without breaking each other.
"""

import os
import sys

# Ensure backend package is on python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

print("\n" + "="*75)
print("AGRISENSE UNIFIED API & MULTI-MODULE VERIFICATION TEST")
print("="*75)

# 1. Test Unified FastAPI App Route Registration
from backend.main import app

routes = [f"{r.methods} {r.path}" for r in app.routes if hasattr(r, "methods")]
print("\n[1] Registered Unified API Routes:")
for route in routes:
    if "/api" in route or route == "{'GET'} /":
        print(f"    -> {route}")

# 2. Test Module 1 (Smart Irrigation)
from backend.schemas import TelemetryInput
from backend.module1_irrigation.engine import calculate_irrigation

m1_input = TelemetryInput(soil_moisture=25.0, temperature=32.0, crop_type="tomato")
m1_output = calculate_irrigation(m1_input)
print(f"\n[2] Module 1 (Smart Irrigation):")
print(f"    Input Moisture:  {m1_input.soil_moisture}%")
print(f"    Status:          {m1_output.status}")
print(f"    Action Required: {m1_output.action_required}")
print(f"    Water Volume:    {m1_output.recommended_water_liters_per_sqm} L/m²")

# 3. Test Module 2 (Crop & Fertilizer Recommendation)
from backend.schemas import SoilInput
from backend.module2_recommendation.crop.predict import predict_crop
from backend.module2_recommendation.fertilizer.recommend import recommend_fertilizer

m2_soil = SoilInput(N=80.0, P=40.0, K=40.0, ph=6.5, temperature=28.0, humidity=70.0, rainfall=120.0)
m2_crop = predict_crop(m2_soil)
m2_fert = recommend_fertilizer(crop=m2_crop.recommended_crop, soil=m2_soil)
print(f"\n[3] Module 2 (Crop & Fertilizer Engine):")
print(f"    Recommended Crop: {m2_crop.recommended_crop}")
print(f"    Top Candidates:   {[c.crop for c in m2_crop.top_crops]}")
print(f"    Fertilizer Plan:  {len(m2_fert.fertilizer_plan)} amendments recommended")

# 4. Test Module 3 (AI Leaf Pathology Scanner)
from backend.module3_pathology.vision_engine import run_pipeline
from backend.module3_pathology.database import list_all_diseases

sample_img_path = os.path.join(os.path.dirname(__file__), "sample_images", "tomato_early_blight_sample.jpg")
with open(sample_img_path, "rb") as f:
    m3_diagnosis = run_pipeline(f.read())

print(f"\n[4] Module 3 (AI Leaf Pathology Scanner):")
print(f"    Detected Crop:    {m3_diagnosis['crop']}")
print(f"    Detected Disease: {m3_diagnosis['disease_name']}")
print(f"    Confidence:       {m3_diagnosis['confidence_score']}%")
print(f"    Severity:         {m3_diagnosis['severity']}")
print(f"    AI Engine Mode:   {m3_diagnosis['engine_mode']}")
print(f"    Telemetry Sync:   {m3_diagnosis['irrigation_telemetry_advice'][:75]}...")

print("\n" + "="*75)
print("ALL 3 MODULES VERIFIED & OPERATING COHESIVELY TOGETHER!")
print("="*75 + "\n")

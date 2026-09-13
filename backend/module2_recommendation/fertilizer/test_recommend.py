# Standalone test script to verify your engine logic works locally.
import sys
from pathlib import Path

# Add root project path to allow schemas import
sys.path.append(str(Path(__file__).resolve().parent.parent))

from schemas import SoilInput
from fertilizer_engine.recommend import recommend_fertilizer

def run_tests():
    # Test 1: A heavy-feeding fruit (Banana) on depleted, acidic soil
    print("--- TEST 1: Banana on poor soil ---")
    soil_1 = SoilInput(N=20.0, P=10.0, K=15.0, ph=5.2, temperature=28.0, humidity=80.0, rainfall=200.0)
    result_1 = recommend_fertilizer("banana", soil_1)
    
    for item in result_1.fertilizer_plan:
        print(f"{item.amendment}: {item.quantity_kg_per_acre} kg/acre")
    print(f"Explanation: {result_1.explanation}\n")

    # Test 2: A pulse (Chickpea) which requires very low Nitrogen
    print("--- TEST 2: Chickpea (Pulse) on decent soil ---")
    soil_2 = SoilInput(N=8.0, P=5.0, K=5.0, ph=6.5, temperature=22.0, humidity=50.0, rainfall=60.0)
    result_2 = recommend_fertilizer("chickpea", soil_2)
    
    for item in result_2.fertilizer_plan:
        print(f"{item.amendment}: {item.quantity_kg_per_acre} kg/acre")
    print(f"Explanation: {result_2.explanation}\n")

if __name__ == "__main__":
    run_tests()
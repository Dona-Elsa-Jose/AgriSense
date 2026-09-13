"""
recommend.py
Owned by: Person B (fertilizer engine)
Core logic orchestrator. Imports from the other files and returns the contract schema.
"""

import sys
from pathlib import Path

# Ensures it can find schemas.py in the root directory above
sys.path.append(str(Path(__file__).resolve().parent.parent))

from schemas import SoilInput, FertilizerOutput, FertilizerPlanItem
from fertilizer_engine.fertilizer import CROP_AGRONOMIC_TARGETS, DEFAULT_TARGET
import fertilizer_engine.explain as explain


def recommend_fertilizer(crop: str, soil: SoilInput) -> FertilizerOutput:
    # Normalize crop name to match dictionary keys (e.g., "Kidney Beans" -> "kidneybeans")
    crop_normalized = crop.strip().lower().replace(" ", "")
    target = CROP_AGRONOMIC_TARGETS.get(crop_normalized, DEFAULT_TARGET)

    n_deficit = max(0.0, target["N"] - soil.N)
    p_deficit = max(0.0, target["P"] - soil.P)
    k_deficit = max(0.0, target["K"] - soil.K)

    plan = []
    explanations = []

    # 1. Phosphorus & DAP Stoichiometry (46% P, 18% N)
    dap_supplied_n = 0.0
    if p_deficit > 0:
        dap_kg = p_deficit / 0.46
        dap_supplied_n = dap_kg * 0.18
        plan.append(
            FertilizerPlanItem(
                nutrient="Phosphorus (P)",
                amendment="DAP (Diammonium Phosphate)",
                quantity_kg_per_acre=round(dap_kg, 1),
            )
        )
        explanations.append(
            explain.generate_phosphorus_explanation(
                crop.title(), p_deficit, target["P"], dap_kg, dap_supplied_n
            )
        )

    # 2. Nitrogen & Urea Stoichiometry (46% N)
    remaining_n_deficit = max(0.0, n_deficit - dap_supplied_n)
    if remaining_n_deficit > 0:
        urea_kg = remaining_n_deficit / 0.46
        plan.append(
            FertilizerPlanItem(
                nutrient="Nitrogen (N)",
                amendment="Urea",
                quantity_kg_per_acre=round(urea_kg, 1),
            )
        )
        explanations.append(
            explain.generate_nitrogen_explanation(
                target["N"], n_deficit, urea_kg, dap_supplied_n
            )
        )
    elif n_deficit > 0 and dap_supplied_n >= n_deficit:
        explanations.append(
            explain.generate_nitrogen_fulfilled_by_dap_explanation(n_deficit)
        )

    # 3. Potassium & MOP Stoichiometry (60% K)
    if k_deficit > 0:
        mop_kg = k_deficit / 0.60
        plan.append(
            FertilizerPlanItem(
                nutrient="Potassium (K)",
                amendment="MOP (Muriate of Potash)",
                quantity_kg_per_acre=round(mop_kg, 1),
            )
        )
        explanations.append(
            explain.generate_potassium_explanation(
                target["K"], k_deficit, mop_kg
            )
        )

    # 4. pH Diagnostics
    if soil.ph < target["ph_min"]:
        lime_kg = round((target["ph_min"] - soil.ph) * 400, 1)
        plan.append(
            FertilizerPlanItem(
                nutrient="pH Correction (Acidic)",
                amendment="Agricultural Lime",
                quantity_kg_per_acre=lime_kg,
            )
        )
        explanations.append(
            explain.generate_ph_explanation(
                soil.ph, target["ph_min"], target["ph_max"], lime_kg=lime_kg
            )
        )
    elif soil.ph > target["ph_max"]:
        gypsum_kg = round((soil.ph - target["ph_max"]) * 300, 1)
        plan.append(
            FertilizerPlanItem(
                nutrient="pH Correction (Alkaline)",
                amendment="Agricultural Gypsum",
                quantity_kg_per_acre=gypsum_kg,
            )
        )
        explanations.append(
            explain.generate_ph_explanation(
                soil.ph, target["ph_min"], target["ph_max"], gypsum_kg=gypsum_kg
            )
        )

    # 5. Organic Fallback for healthy soil
    if not plan:
        plan.append(
            FertilizerPlanItem(
                nutrient="Soil Maintenance",
                amendment="Organic Farmyard Manure",
                quantity_kg_per_acre=2000.0,
            )
        )
        explanations.append(
            "Soil parameters are perfectly balanced for this crop. No chemical fertilizer required. Add organic manure to maintain soil health."
        )

    return FertilizerOutput(
        fertilizer_plan=plan, explanation=" | ".join(explanations)
    )
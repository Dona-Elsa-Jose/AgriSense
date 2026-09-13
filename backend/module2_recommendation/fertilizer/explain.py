"""
explain.py
Handles the generation of agronomic reasoning for the UI.
"""

def generate_phosphorus_explanation(crop: str, p_deficit: float, target_p: float, dap_kg: float, dap_supplied_n: float) -> str:
    p_pct = round((p_deficit / target_p) * 100) if target_p > 0 else 0
    return (f"Phosphorus is {p_pct}% below the {round(target_p, 1)} kg/acre baseline for {crop}. "
            f"Applying {round(dap_kg, 1)} kg/acre of DAP resolves this deficit and supplies a basal credit of "
            f"{round(dap_supplied_n, 1)} kg/acre Nitrogen.")

def generate_nitrogen_explanation(target_n: float, n_deficit: float, urea_kg: float, dap_supplied_n: float) -> str:
    n_pct = round((n_deficit / target_n) * 100) if target_n > 0 else 0
    msg = f"Nitrogen deficit detected ({n_pct}% below target). "
    if dap_supplied_n > 0:
        msg += f"After deducting the N supplied by DAP, {round(urea_kg, 1)} kg/acre of Urea is required."
    else:
        msg += f"{round(urea_kg, 1)} kg/acre of Urea is required for optimal vegetative growth."
    return msg

def generate_nitrogen_fulfilled_by_dap_explanation(n_deficit: float) -> str:
    return f"The calculated Nitrogen deficit ({round(n_deficit, 1)} kg/acre) is fully satisfied by the DAP prescription. No Urea needed."

def generate_potassium_explanation(target_k: float, k_deficit: float, mop_kg: float) -> str:
    k_pct = round((k_deficit / target_k) * 100) if target_k > 0 else 0
    return (f"Potassium is {k_pct}% below requirement. {round(mop_kg, 1)} kg/acre of MOP is recommended "
            "to ensure crop resilience and quality.")

def generate_ph_explanation(soil_ph: float, ph_min: float, ph_max: float, lime_kg: float = 0, gypsum_kg: float = 0) -> str:
    if soil_ph < ph_min:
        return f"Warning: Soil pH ({soil_ph}) is too acidic (optimal >={ph_min}). Add {round(lime_kg, 1)} kg/acre Agricultural Lime prior to sowing."
    elif soil_ph > ph_max:
        return f"Warning: Soil pH ({soil_ph}) is too alkaline (optimal <={ph_max}). Consider {round(gypsum_kg, 1)} kg/acre Agricultural Gypsum."
    return ""
"""
Comprehensive Plant Pathology Knowledge Base
Contains diagnostic data, severity levels, and multi-stage treatment plans
for major agricultural crops and diseases across fungal, bacterial, and healthy states.
"""

PATHOLOGY_DATABASE = {
    "bacterial_leaf_spot": {
        "crop": "Tomato / Pepper",
        "disease_name": "Bacterial Leaf Spot (Xanthomonas campestris)",
        "pathogen_type": "Bacterial",
        "severity": "High",
        "symptoms": "Small, water-soaked angular dark brown lesions that don't cross leaf veins, often with translucent greasy borders and yellow halos.",
        "irrigation_telemetry_advice": "Bacteria spread via water droplets and splash. Cease overhead irrigation immediately; reduce greenhouse relative humidity below 75%.",
        "treatment_plan": {
            "step_1_immediate_action": "Do NOT work in fields while foliage is wet. Prune and bag infected plants. Disinfect pruners with 10% bleach between cuts.",
            "step_2_organic_control": "Apply copper bactericides (copper sulfate or copper hydroxide) tank-mixed with mancozeb for synergistic protection.",
            "step_3_chemical_treatment": "In regions where copper-resistant strains occur, apply Agri-Mycin (Streptomycin sulfate) or Kasugamycin under strict local agricultural guidelines.",
            "step_4_preventive_strategy": "Use certified hot-water-treated seeds. Implement a 2-to-3 year rotation away from solanaceous crops."
        }
    },
    "tomato_early_blight": {
        "crop": "Tomato",
        "disease_name": "Early Blight (Alternaria solani)",
        "pathogen_type": "Fungal",
        "severity": "Moderate to High",
        "symptoms": "Concentric dark brown rings ('target board' pattern) on older lower leaves, yellowing halos, stem cankers.",
        "irrigation_telemetry_advice": "Reduce canopy moisture. Avoid overhead irrigation (Module 1 alert: switch to drip irrigation to keep soil moisture between 60-70% without wetting foliage).",
        "treatment_plan": {
            "step_1_immediate_action": "Prune and dispose of all infected lower leaves immediately. Do NOT compost diseased foliage. Disinfect shears with 70% alcohol.",
            "step_2_organic_control": "Spray copper octanoate (copper soap fungicide) or bio-fungicide containing Bacillus subtilis every 7-10 days.",
            "step_3_chemical_treatment": "For severe infestation, apply chlorothalonil or mancozeb-based fungicides at first symptom onset.",
            "step_4_preventive_strategy": "Mulch soil surface with straw to prevent soil-borne spores from splashing onto lower leaves during rainfall."
        }
    },
    "tomato_late_blight": {
        "crop": "Tomato",
        "disease_name": "Late Blight (Phytophthora infestans)",
        "pathogen_type": "Oomycete / Water Mold",
        "severity": "Critical",
        "symptoms": "Water-soaked dark lesions on leaves and stems, white fuzzy fungal growth on leaf undersides in high humidity, rapid plant collapse.",
        "irrigation_telemetry_advice": "High relative humidity (>90%) accelerates spread. Halt overhead misting and lower greenhouse humidity.",
        "treatment_plan": {
            "step_1_immediate_action": "Isolate the area immediately. Remove and bag severely infected plants in sealed plastic bags to prevent airborne spore dissemination.",
            "step_2_organic_control": "Apply preventative copper hydroxide spray to adjacent healthy foliage.",
            "step_3_chemical_treatment": "Apply systemic fungicides containing Dimethomorph, Cymoxanil, or Metalaxyl according to label intervals.",
            "step_4_preventive_strategy": "Ensure wide plant spacing for high airflow and implement strict 3-year solanaceous crop rotation."
        }
    },
    "potato_late_blight": {
        "crop": "Potato",
        "disease_name": "Late Blight (Phytophthora infestans)",
        "pathogen_type": "Oomycete",
        "severity": "Critical",
        "symptoms": "Dark brown, irregular water-soaked spots on leaf edges, rapid leaf death, brown rot on tubers.",
        "irrigation_telemetry_advice": "Ensure soil drainage is optimal. Soil moisture over 85% during cool temperatures dramatically spikes infection risk.",
        "treatment_plan": {
            "step_1_immediate_action": "Cut off infected vines below ground level before tuber harvest to prevent spores washing into tubers.",
            "step_2_organic_control": "Fixed copper fungicides applied proactively before anticipated wet weather fronts.",
            "step_3_chemical_treatment": "Systemic treatment with Fluopicolide or Propamocarb hydrochloride.",
            "step_4_preventive_strategy": "Plant certified disease-free seed potatoes with resistant cultivars (e.g., Sarpo Mira)."
        }
    },
    "corn_common_rust": {
        "crop": "Corn / Maize",
        "disease_name": "Common Rust (Puccinia sorghi)",
        "pathogen_type": "Fungal",
        "severity": "Moderate",
        "symptoms": "Golden-brown to cinnamon-brown powdery pustules on both upper and lower leaf surfaces.",
        "irrigation_telemetry_advice": "Infection thrives in 16-25°C with free moisture on leaves for over 6 hours. Schedule irrigation during early morning so sun dries leaves.",
        "treatment_plan": {
            "step_1_immediate_action": "Scout field weekly. Determine infection severity index across canopy before silking stage.",
            "step_2_organic_control": "Sulfur dusting or neem seed extract sprays for smallholder plots.",
            "step_3_chemical_treatment": "Triazole or Strobilurin fungicides (e.g., Azoxystrobin + Difenoconazole) if pustules appear on ear leaves before tasseling.",
            "step_4_preventive_strategy": "Select rust-resistant hybrid seed varieties with Rp genes."
        }
    },
    "apple_scab": {
        "crop": "Apple",
        "disease_name": "Apple Scab (Venturia inaequalis)",
        "pathogen_type": "Fungal",
        "severity": "Moderate to High",
        "symptoms": "Olive-green to velvety dark brown lesions on leaves and fruit, leaf distortion and premature defoliation.",
        "irrigation_telemetry_advice": "Spore release is triggered by spring rains. Avoid sprinkler systems that wet the tree canopy.",
        "treatment_plan": {
            "step_1_immediate_action": "Rake and destroy fallen leaves in autumn to reduce primary overwintering inoculum.",
            "step_2_organic_control": "Lime sulfur or liquid sulfur sprays during green-tip and tight-cluster stages.",
            "step_3_chemical_treatment": "Apply Captan or Myclobutanil beginning at bud break and repeated through petal fall.",
            "step_4_preventive_strategy": "Prune open-center canopy architecture to maximize sunlight and wind penetration."
        }
    },
    "powdery_mildew": {
        "crop": "General / Cucurbit / Berry",
        "disease_name": "Powdery Mildew (Podosphaera / Erysiphe spp.)",
        "pathogen_type": "Fungal",
        "severity": "Moderate",
        "symptoms": "White powdery talcum-powder-like patches on leaf surfaces, curling foliage, reduced photosynthesis.",
        "irrigation_telemetry_advice": "Develops in high humidity but dry leaf surfaces. Maintain consistent root zone irrigation to reduce plant water stress.",
        "treatment_plan": {
            "step_1_immediate_action": "Pinch off severely affected leaves. Increase airflow between plants.",
            "step_2_organic_control": "Spray potassium bicarbonate solution or diluted milk spray (1:9 ratio) under bright sunlight.",
            "step_3_chemical_treatment": "Myclobutanil or sulfur-based protective fungicides.",
            "step_4_preventive_strategy": "Plant in full sun locations; avoid planting in shaded stagnant air pockets."
        }
    },
    "early_stage_foliar_lesions": {
        "crop": "General Crop / Solanaceous",
        "disease_name": "Incipient Foliar Lesions (Early Disease Stage)",
        "pathogen_type": "Fungal / Bacterial Onset",
        "severity": "Low (Early Detection)",
        "symptoms": "Localized micro-lesions, pinprick necrotic spots, or early chlorotic flecks beginning to form on the leaf lamina.",
        "irrigation_telemetry_advice": "Critical window: disease is in inception stage. Adjust Module 1 irrigation to prevent free moisture on leaves for >4 hours.",
        "treatment_plan": {
            "step_1_immediate_action": "Inspect surrounding canopy for further micro-spots. Remove affected leaves if isolated to lower foliage.",
            "step_2_organic_control": "Prophylactic spray of neem seed extract or Bacillus subtilis bio-fungicide to halt germination of spores.",
            "step_3_chemical_treatment": "Broad-spectrum protectant spray (e.g., copper hydroxide or Mancozeb) at light dosage to protect adjacent foliage.",
            "step_4_preventive_strategy": "Increase airflow and reduce humidity to arrest early disease establishment before full systemic spread."
        }
    },
    "healthy_leaf": {
        "crop": "General Crop",
        "disease_name": "Healthy Foliage (No Pathology Detected)",
        "pathogen_type": "None",
        "severity": "Optimal",
        "symptoms": "Vibrant green coloration, uniform leaf lamina, unblemished venation, no necrotic spots or chlorosis.",
        "irrigation_telemetry_advice": "Maintain current irrigation schedule based on Module 1 telemetry sensors.",
        "treatment_plan": {
            "step_1_immediate_action": "No chemical or remediation intervention required.",
            "step_2_organic_control": "Continue standard preventive biostimulant or seaweed extract foliar nutrition.",
            "step_3_chemical_treatment": "No fungicide application needed; preserve beneficial microflora.",
            "step_4_preventive_strategy": "Maintain regular weekly visual scouting and monitor telemetry logs for sudden moisture or temperature spikes."
        }
    }
}

def get_disease_info(key: str):
    return PATHOLOGY_DATABASE.get(key, PATHOLOGY_DATABASE["healthy_leaf"])

def list_all_diseases():
    return [
        {
            "key": k,
            "crop": v["crop"],
            "disease_name": v["disease_name"],
            "severity": v["severity"],
            "pathogen_type": v["pathogen_type"]
        }
        for k, v in PATHOLOGY_DATABASE.items()
    ]

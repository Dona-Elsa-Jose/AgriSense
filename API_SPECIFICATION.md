# Module 3: AI Leaf Pathology Scanner — API Specification

This document provides the integration contract for **Module 4 (Central Dashboard & UI Command Center)** to consume the leaf pathology computer vision services.

---

## Base URL
```
http://localhost:8000
```
*(CORS is enabled for all origins `*`)*

---

## 1. Diagnose Leaf Image
Analyzes an uploaded leaf photograph and returns the detected crop, specific disease, confidence percentage, symptoms, irrigation correlation (Module 1 link), and step-by-step treatment plan.

- **Method**: `POST`
- **Endpoint**: `/api/diagnose`
- **Content-Type**: `multipart/form-data`

### Request Parameters
| Field | Type | Description |
| :--- | :--- | :--- |
| `file` | `File` (binary) | Image file of affected leaf (`image/jpeg`, `image/png`, `image/webp`) |

### Example Response (JSON)
```json
{
  "is_plant_leaf": true,
  "crop": "Tomato",
  "disease_name": "Early Blight (Alternaria solani)",
  "confidence_score": 96.8,
  "severity": "Moderate to High",
  "pathogen_type": "Fungal",
  "symptoms": "Concentric dark brown rings ('target board' pattern) on older lower leaves, yellowing halos, stem cankers.",
  "irrigation_telemetry_advice": "Reduce canopy moisture. Avoid overhead irrigation (Module 1 alert: switch to drip irrigation to keep soil moisture between 60-70% without wetting foliage).",
  "treatment_plan": {
    "step_1_immediate_action": "Prune and dispose of all infected lower leaves immediately. Do NOT compost diseased foliage. Disinfect shears with 70% alcohol.",
    "step_2_organic_control": "Spray copper octanoate (copper soap fungicide) or bio-fungicide containing Bacillus subtilis every 7-10 days.",
    "step_3_chemical_treatment": "For severe infestation, apply chlorothalonil or mancozeb-based fungicides at first symptom onset.",
    "step_4_preventive_strategy": "Mulch soil surface with straw to prevent soil-borne spores from splashing onto lower leaves during rainfall."
  },
  "engine_mode": "Gemini Vision AI (Live Cloud Engine)"
}
```

---

## 2. Get Disease Catalog
Returns catalog of known plant diseases and reference data.

- **Method**: `GET`
- **Endpoint**: `/api/diseases`

---

## 3. Healthcheck
- **Method**: `GET`
- **Endpoint**: `/api/health`

---

## Module 4 Frontend Integration Code Snippets

### JavaScript `fetch` Example:
```javascript
async function scanLeaf(imageFile) {
  const formData = new FormData();
  formData.append('file', imageFile);

  const response = await fetch('http://localhost:8000/api/diagnose', {
    method: 'POST',
    body: formData
  });

  if (!response.ok) {
    throw new Error('Diagnosis failed');
  }

  const result = await response.json();
  console.log('Detected Disease:', result.disease_name);
  console.log('Confidence:', result.confidence_score + '%');
  console.log('Treatment Plan:', result.treatment_plan);
  return result;
}
```

### React Hook Example:
```jsx
import React, { useState } from 'react';

export function LeafScannerModule() {
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleUpload = async (e) => {
    const file = e.target.files[0];
    if (!file) return;

    setLoading(true);
    const formData = new FormData();
    formData.append('file', file);

    try {
      const res = await fetch('http://localhost:8000/api/diagnose', {
        method: 'POST',
        body: formData
      });
      const data = await res.json();
      setResult(data);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="module-card">
      <h3>AI Leaf Pathology Scanner</h3>
      <input type="file" accept="image/*" onChange={handleUpload} />
      {loading && <p>Scanning leaf...</p>}
      {result && (
        <div>
          <h4>{result.crop} - {result.disease_name} ({result.confidence_score}%)</h4>
          <p><strong>Immediate Action:</strong> {result.treatment_plan.step_1_immediate_action}</p>
        </div>
      )}
    </div>
  );
}
```

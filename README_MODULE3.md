# 🌱 Module 3: AI Leaf Pathology Scanner (Computer Vision)
> **Part of the SmartAgri Hackathon Suite**

A visual diagnostic pipeline designed to detect crop plant diseases early. Users upload or snap a photo of an affected crop leaf to instantly identify plant health issues, receive exact disease classifications with high-precision confidence scores, and get an actionable, step-by-step clinical treatment plan to prevent yield loss.

---

## 🚀 Key Features

1. **Computer Vision Diagnostic Engine**:
   - **Dual-Engine Architecture**:
     - **Cloud AI Vision Engine**: Powered by Google Gemini 2.5 / 1.5 Flash Vision for zero-shot diagnosis across any crop with detailed visual reasoning.
     - **Edge/Offline Fallback Engine**: Color histogram, necrotic lesion index & chlorosis analyzer backed by a clinical plant pathology database — guarantees **zero failure** during live judge evaluations even if internet drops!
2. **Actionable Step-by-Step Treatment Prescriptions**:
   - **Step 1**: Immediate Cultural Sanitation (pruning, isolation, sterilizing tools)
   - **Step 2**: Organic & Bio-Control Remedies (Bacillus subtilis, copper soap, neem formulations)
   - **Step 3**: Chemical & Targeted Fungicides (Chlorothalonil, Mancozeb, Azoxystrobin with dosage)
   - **Step 4**: Long-Term Preventive Agronomy (crop rotation, canopy airflow, resistant varieties)
3. **Cross-Module Telemetry Link (Module 1 Integration)**:
   - Evaluates whether disease is fungal/humidity-triggered and provides real-time irrigation adjustments (e.g. *"Stop overhead misting; maintain soil moisture at 65% via drip lines"*).
4. **Standalone Demo Dashboard + REST API for Module 4**:
   - Drag-and-drop leaf upload, live camera frame capture, animated laser scanning beam, confidence meter, and instant test sample chips.
   - Clean REST API (`/api/diagnose`) with CORS enabled for seamless integration into the Central Dashboard.

---

## 📁 Project Structure

```
leaf_pathology_scanner/
├── backend/
│   ├── app.py                  # FastAPI server & static file host
│   ├── vision_engine.py        # Vision diagnostic pipeline (Cloud AI + Offline Fallback)
│   ├── pathology_db.py         # Clinical pathology database & treatment protocols
│   └── requirements.txt        # Backend dependencies
├── frontend/
│   ├── index.html              # Standalone interactive demonstration UI
│   ├── style.css               # Modern agri-tech emerald/dark theme
│   └── app.js                  # Drag-and-drop, camera snap, and API client logic
├── API_SPECIFICATION.md        # API documentation & React/fetch code for Module 4
└── README.md                   # Project documentation & presentation guide
```

---

## ⚡ Quickstart Guide

### 1. Install Dependencies
In your terminal, navigate to the `backend` folder and install dependencies:
```powershell
cd C:\Users\bobby\leaf_pathology_scanner\backend
py -m pip install -r requirements.txt
```

### 2. (Optional) Set Cloud Vision API Key
If you have a Google Gemini API key:
```powershell
$env:GEMINI_API_KEY="your-gemini-api-key-here"
```
*(Note: If you don't set an API key, the system automatically uses the intelligent offline edge engine without error).*

### 3. Launch the Server & UI
```powershell
py app.py
```
Open your browser at:
👉 **[http://localhost:8000](http://localhost:8000)**

---

## 🏆 Hackathon Presentation & Live Demo Script

When presenting to judges:

1. **The Problem**: *"Crop diseases like Early Blight and Rust spread rapidly through fungal spores, causing up to 40% yield loss before physical symptoms are formally identified by traditional lab testing."*
2. **The Solution (Module 3)**: *"Our AI Leaf Pathology Scanner puts an expert agronomist in the farmer's pocket. In under 2 seconds, it analyzes leaf lamina discoloration, identifies the exact pathogen, computes a confidence score, and provides a 4-step treatment plan."*
3. **Show, Don't Tell**:
   - Click one of the **Quick Test Samples** (e.g., `Tomato Blight` or `Corn Rust`).
   - Watch the animated laser scan trigger.
   - Point out the **Confidence Meter (e.g. 96.8%)** and the **Severity tag**.
   - Show the **Telemetry Link**: Explain how Module 3 alerts Module 1 to adjust soil moisture probes and halt overhead sprinklers!
   - Highlight the **Step-by-Step Treatment Plan** showing both organic remedies and commercial fungicides.
4. **Integration with Module 4**: Show the *"Copy JSON"* button and explain that the Central Dashboard team can consume the `/api/diagnose` endpoint with just 5 lines of code!

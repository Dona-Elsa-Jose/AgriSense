from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.module1_irrigation.router import router as irrigation_router
from backend.module2_recommendation.router import router as crop_router

app = FastAPI(
    title="AgriSense API Hub",
    description="Unified Backend Engine for Smart Irrigation, Crop/Fertilizer Recommendations, and Leaf Pathology",
    version="1.0.0"
)

# Enable CORS for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Module Routers
app.include_router(irrigation_router)
app.include_router(crop_router)

@app.get("/")
def root():
    return {
        "project": "AgriSense API Hub",
        "status": "Online",
        "active_modules": ["Module 1: Smart Irrigation", "Module 2: Crop Recommendation Engine"]
    }
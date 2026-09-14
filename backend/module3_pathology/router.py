"""
Module 3: AI Leaf Pathology Scanner Router
Exposes REST API endpoints for plant disease image diagnosis,
clinical treatment plans, and pathology catalogs.
"""

from fastapi import APIRouter, File, UploadFile, HTTPException
from typing import List

from backend.schemas import PathologyDiagnosis, DiseaseCatalogItem
from backend.module3_pathology.vision_engine import run_pipeline
from backend.module3_pathology.database import list_all_diseases

router = APIRouter(prefix="/api/v1/pathology", tags=["Module 3: Leaf Pathology"])

@router.get("/health")
def pathology_health():
    """Health check for Module 3 vision pipeline."""
    return {
        "status": "online",
        "module": "Module 3: AI Leaf Pathology Scanner",
        "engine": "Dual-Engine Vision Pipeline (Gemini 3.6 Flash + Local Edge CV)"
    }

@router.get("/diseases", response_model=List[DiseaseCatalogItem])
def get_pathology_catalog():
    """Retrieve database catalog of recognizable plant diseases and pathogens."""
    return list_all_diseases()

@router.post("/diagnose", response_model=PathologyDiagnosis)
async def diagnose_leaf_image(file: UploadFile = File(...)):
    """
    Primary Diagnostic Endpoint:
    Accepts an uploaded image file (JPEG, PNG, WebP) of a crop leaf.
    Performs Computer Vision pathology analysis and returns the disease name,
    confidence percentage, severity, visual symptoms, and a 4-step treatment plan.
    """
    content_type = file.content_type or ""
    filename = (file.filename or "").lower()
    valid_exts = (".jpg", ".jpeg", ".png", ".webp", ".bmp")

    if not content_type.startswith("image/") and not any(filename.endswith(ext) for ext in valid_exts):
        raise HTTPException(
            status_code=400,
            detail="Invalid file format. Uploaded file must be an image (JPEG, PNG, WebP)."
        )
        
    contents = await file.read()
    if len(contents) == 0:
        raise HTTPException(status_code=400, detail="Empty image payload received.")
        
    try:
        diagnosis = run_pipeline(contents)
        return diagnosis
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Diagnostic error: {str(e)}")

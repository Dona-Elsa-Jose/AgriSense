from fastapi import APIRouter, File, UploadFile, HTTPException
from typing import List
from backend.schemas import PathologyDiagnosis, DiseaseCatalogItem
from backend.module3_pathology.vision_engine import run_pipeline
from backend.module3_pathology.database import list_all_diseases

router = APIRouter(prefix="/api/v1/pathology", tags=["Module 3: Leaf Pathology"])

@router.get("/health")
def pathology_health():
    return {"status": "online", "module": "Module 3: AI Leaf Pathology Scanner"}

@router.get("/diseases", response_model=List[DiseaseCatalogItem])
def get_pathology_catalog():
    return list_all_diseases()

@router.post("/diagnose", response_model=PathologyDiagnosis)
async def diagnose_leaf_image(file: UploadFile = File(...)):
    contents = await file.read()
    return run_pipeline(contents)

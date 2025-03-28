from fastapi import APIRouter, HTTPException
from models.treino import Treino
from schemas.treino_schema import TreinoCreate, TreinoUpdate

router = APIRouter()

@router.get("/")
async def listar_treinos():
    return {"treinos": []}

@router.post("/")
async def criar_treino(treino: TreinoCreate):
    return {"message": "Treino criado com sucesso"}
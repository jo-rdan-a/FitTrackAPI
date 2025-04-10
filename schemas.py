# app/schemas.py
from pydantic import BaseModel
from typing import Optional
from datetime import date

# ----------- ALUNO -----------
class AlunoCreate(BaseModel):
    nome: str
    email: str
    senha: str
    telefone: Optional[str] = None
    data_nascimento: Optional[date] = None

class AlunoOut(BaseModel):
    id: int
    nome: str
    email: str

    class Config:
        orm_mode = True

# ----------- INSTRUTOR -----------
class InstrutorCreate(BaseModel):
    nome: str
    email: str
    senha: str
    telefone: Optional[str] = None
    especializacao: Optional[str] = None

class InstrutorOut(BaseModel):
    id: int
    nome: str
    email: str

    class Config:
        orm_mode = True

# ----------- MEDIDAS -----------
class MedidaCreate(BaseModel):
    data: date
    peso: float
    altura: float
    cintura: float
    quadril: float
    torax: float

class MedidaOut(MedidaCreate):
    id: int

    class Config:
        orm_mode = True

# ----------- FICHA DE TREINO -----------
class FichaTreinoCreate(BaseModel):
    descricao: str
    series: str
    repeticoes: str
    descanso: str

class FichaTreinoOut(FichaTreinoCreate):
    id: int

    class Config:
        orm_mode = True

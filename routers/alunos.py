# app/routers/alunos.py
from fastapi import APIRouter, Depends, Request, Form
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from models.models import Aluno, Medida, FichaTreino, DiaTreino, ExercicioTreino
from fastapi.templating import Jinja2Templates
from datetime import date
from sqlalchemy.orm import joinedload
from fastapi.encoders import jsonable_encoder

from dao import database

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/aluno/{aluno_id}/dashboard")
def dashboard_aluno(aluno_id: int, request: Request, db: Session = Depends(database.get_db)):
    aluno = db.query(Aluno).filter(Aluno.id == aluno_id).first()
    
    medidas_raw = db.query(Medida).filter(Medida.aluno_id == aluno_id).order_by(Medida.data.desc()).all()
    medidas = jsonable_encoder(medidas_raw)  # 🔥 converte para dicionário JSON serializável

    ficha = db.query(FichaTreino).options(
        joinedload(FichaTreino.dias).joinedload(DiaTreino.exercicios_treino).joinedload(ExercicioTreino.exercicio)
    ).filter(FichaTreino.aluno_id == aluno_id)\
     .order_by(FichaTreino.data_inicio.desc())\
     .first()

    return templates.TemplateResponse("dashboard_aluno.html", {
        "request": request,
        "aluno": aluno,
        "medidas": medidas,  # agora já serializado
        "ficha": ficha
    })

@router.get("/aluno/{aluno_id}/medidas")
def formulario_medidas(aluno_id: int, request: Request):
    return templates.TemplateResponse("cadastro_medidas.html", {
        "request": request,
        "aluno_id": aluno_id
    })

@router.post("/aluno/{aluno_id}/medidas")
def registrar_medidas(
    aluno_id: int,
    request: Request,
    db: Session = Depends(database.get_db),
    peso: float = Form(...),
    altura: float = Form(...),
    cintura: float = Form(...),
    quadril: float = Form(...),
    torax: float = Form(...)
):
    nova_medida = Medida(
        aluno_id=aluno_id,
        data=date.today(),
        peso=peso,
        altura=altura,
        cintura=cintura,
        quadril=quadril,
        torax=torax
    )
    db.add(nova_medida)
    db.commit()
    return RedirectResponse(f"/aluno/{aluno_id}/dashboard", status_code=303)

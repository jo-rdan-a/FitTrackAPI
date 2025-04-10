from fastapi import APIRouter, Depends, Request, Form
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from dao import database
from models.models import Aluno, Medida
from datetime import date
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/medidas/aluno/{aluno_id}")
def visualizar_medidas(aluno_id: int, request: Request, db: Session = Depends(database.get_db)):
    medidas = db.query(Medida).filter(Medida.aluno_id == aluno_id).order_by(Medida.data.desc()).all()
    aluno = db.query(Aluno).filter(Aluno.id == aluno_id).first()
    return templates.TemplateResponse("dashboard_aluno.html", {
        "request": request,
        "aluno": aluno,
        "medidas": medidas
    })

@router.get("/medidas/aluno/{aluno_id}/nova")
def form_medida(aluno_id: int, request: Request):
    return templates.TemplateResponse("cadastro_medidas.html", {
        "request": request,
        "aluno_id": aluno_id
    })

@router.post("/medidas/aluno/{aluno_id}")
def registrar_medida(
    aluno_id: int,
    request: Request,
    db: Session = Depends(database.get_db),
    peso: float = Form(...),
    altura: float = Form(...),
    cintura: float = Form(...),
    quadril: float = Form(...),
    torax: float = Form(...)
):
    nova = Medida(
        aluno_id=aluno_id,
        data=date.today(),
        peso=peso,
        altura=altura,
        cintura=cintura,
        quadril=quadril,
        torax=torax
    )
    db.add(nova)
    db.commit()
    return RedirectResponse(f"/medidas/aluno/{aluno_id}", status_code=303)

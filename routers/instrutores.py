from fastapi import APIRouter, Depends, Request, Form, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from models.models import Aluno, Instrutor, FichaTreino, Exercicio
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from dao.database import get_db

from dao import database

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/instrutor/{instrutor_id}/dashboard")
def dashboard_instrutor(instrutor_id: int, request: Request, db: Session = Depends(database.get_db)):
    instrutor = db.query(Instrutor).filter(Instrutor.id == instrutor_id).first()
    fichas = db.query(FichaTreino).filter(FichaTreino.instrutor_id == instrutor_id).all()
    return templates.TemplateResponse("dashboard_instrutor.html", {
        "request": request,
        "instrutor": instrutor,
        "fichas": fichas
    })

@router.get("/instrutor/{instrutor_id}/ficha/criar")
def formulario_ficha(instrutor_id: int, request: Request, db: Session = Depends(database.get_db)):
    alunos = db.query(Aluno).all()
    return templates.TemplateResponse("criar_ficha.html", {
        "request": request,
        "instrutor_id": instrutor_id,
        "alunos": alunos
    })

@router.get("/instrutor/{instrutor_id}/exercicio/novo")
def form_novo_exercicio(instrutor_id: int, request: Request):
    return templates.TemplateResponse("cadastro_exercicio.html", {
        "request": request,
        "instrutor_id": instrutor_id
    })

@router.post("/instrutor/{instrutor_id}/exercicio/novo")
def criar_exercicio(
    instrutor_id: int,
    request: Request,
    nome: str = Form(...),
    grupo_muscular: str = Form(...),
    db: Session = Depends(database.get_db)
):
    novo = Exercicio(nome=nome, grupo_muscular=grupo_muscular)
    db.add(novo)
    db.commit()
    return RedirectResponse(f"/instrutor/{instrutor_id}/exercicio/novo", status_code=303)

@router.post("/fichas/{ficha_id}/excluir")
def excluir_ficha(ficha_id: int, db: Session = Depends(database.get_db)):
    ficha = db.query(FichaTreino).filter(FichaTreino.id == ficha_id).first()
    if not ficha:
        raise HTTPException(status_code=404, detail="Ficha não encontrada")

    instrutor_id = ficha.instrutor_id
    db.delete(ficha)
    db.commit()
    return RedirectResponse(f"/instrutor/{instrutor_id}/dashboard", status_code=303)

@router.get("/instrutor/{instrutor_id}/alunos", response_class=HTMLResponse)
def listar_alunos(instrutor_id: int, request: Request, db: Session = Depends(get_db)):
    alunos = db.query(Aluno).all()
    return templates.TemplateResponse("alunos.html", {
        "request": request,
        "alunos": alunos,
        "instrutor_id": instrutor_id
    })

@router.get("/instrutor/{instrutor_id}/alunos/{aluno_id}/editar", response_class=HTMLResponse)
def editar_aluno_form(
    instrutor_id: int,
    aluno_id: int,
    request: Request,
    db: Session = Depends(get_db)
):
    aluno = db.query(Aluno).filter(Aluno.id == aluno_id).first()
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")

    return templates.TemplateResponse("editar_aluno.html", {
        "request": request,
        "aluno": aluno,
        "instrutor_id": instrutor_id
    })

@router.post("/instrutor/{instrutor_id}/alunos/{aluno_id}/editar")
def editar_aluno(
    instrutor_id: int,
    aluno_id: int,
    nome: str = Form(...),
    email: str = Form(...),
    db: Session = Depends(get_db)
):
    aluno = db.query(Aluno).filter(Aluno.id == aluno_id).first()
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    
    aluno.nome = nome
    aluno.email = email
    db.commit()

    return RedirectResponse(
        url=f"/instrutor/{instrutor_id}/alunos",  # Redireciona para a lista do instrutor
        status_code=303
    )

@router.post("/instrutor/{instrutor_id}/alunos/{aluno_id}/excluir")
def excluir_aluno(instrutor_id: int, aluno_id: int, db: Session = Depends(get_db)):
    aluno = db.query(Aluno).filter(Aluno.id == aluno_id).first()
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    
    db.delete(aluno)
    db.commit()

    return RedirectResponse(f"/instrutor/{instrutor_id}/alunos", status_code=303)
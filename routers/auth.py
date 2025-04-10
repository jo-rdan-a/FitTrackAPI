from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from models.models import Aluno, Instrutor
from fastapi.templating import Jinja2Templates
from passlib.hash import bcrypt

from dao import database

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/login")
def login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.post("/login")
def login(
    request: Request,
    db: Session = Depends(database.get_db),
    email: str = Form(...),
    senha: str = Form(...),
):
    user = (
        db.query(Aluno).filter(Aluno.email == email).first()
        or db.query(Instrutor).filter(Instrutor.email == email).first()
    )

    if user and bcrypt.verify(senha, user.senha):
        if isinstance(user, Aluno):
            response = RedirectResponse(f"/aluno/{user.id}/dashboard", status_code=303)
            response.set_cookie("usuario_id", str(user.id))
            response.set_cookie("tipo_usuario", "aluno")
            return response
        elif isinstance(user, Instrutor):
            response = RedirectResponse(f"/instrutor/{user.id}/dashboard", status_code=303)
            response.set_cookie("usuario_id", str(user.id))
            response.set_cookie("tipo_usuario", "instrutor")
            return response

    return templates.TemplateResponse("login.html", {
        "request": request,
        "erro": "Email ou senha inválidos"
    })

@router.get("/logout")
def logout():
    response = RedirectResponse(url="/login", status_code=302)
    response.delete_cookie("usuario_id")  # ou o nome do seu cookie de sessão
    response.delete_cookie("tipo_usuario")  # se estiver usando também
    return response

@router.get("/criar_admin")
def criar_admin(db: Session = Depends(database.get_db)):
    from passlib.hash import bcrypt

    # Verifica se já existe um admin com este email
    existente = db.query(Instrutor).filter(Instrutor.email == "admin@treino.com").first()
    if existente:
        return {"msg": "Admin já existe!"}

    senha_cripto = bcrypt.hash("@treino2025")
    admin = Instrutor(
        nome="Admin",
        email="admin@treino.com",
        senha=senha_cripto,
        telefone="88999999999",
        especializacao="Musculação"
    )
    db.add(admin)
    db.commit()
    return {"msg": "Admin criado com sucesso! Email: admin@treino.com | Senha: 123456"}

@router.get("/cadastro", response_class=HTMLResponse)
def exibir_formulario_cadastro(request: Request):
    return templates.TemplateResponse("cadastro_aluno.html", {"request": request})

@router.post("/cadastro")
def processar_cadastro(
    request: Request,
    nome: str = Form(...),
    email: str = Form(...),
    senha: str = Form(...),
    idade: int = Form(...),
    objetivo: str = Form(...),
    outro_objetivo: str = Form(None),
    db: Session = Depends(database.get_db)
):
    from passlib.hash import bcrypt

    objetivo_final = outro_objetivo if objetivo == "Outro" and outro_objetivo else objetivo

    existente = db.query(Aluno).filter(Aluno.email == email).first()
    if existente:
        return templates.TemplateResponse("cadastro_aluno.html", {
            "request": request,
            "erro": "Email já cadastrado."
        })

    aluno = Aluno(
        nome=nome,
        email=email,
        senha=bcrypt.hash(senha),
        idade=idade,
        objetivo=objetivo_final
    )
    db.add(aluno)
    db.commit()

    return RedirectResponse("/login", status_code=303)
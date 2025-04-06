from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database import get_db
from controllers import (
    aluno_controller,
    instrutor_controller,
    administrador_controller,
    ficha_controller,
    medidas_controller,
)

app = FastAPI()

# Configuração do Jinja2
templates = Jinja2Templates(directory="app/templates")


# Rotas para Alunos



@app.post("/aluno/criar")
async def create_aluno(request: Request, db: Session = Depends(get_db)):
    form = await request.form()
    aluno = aluno_controller.AlunoController.create(db, form)
    return templates.TemplateResponse(
        "alunos/sucesso.html", {"request": request, "aluno": aluno}
    )


# Rotas para Instrutores
@app.get("/instrutores")
async def list_instrutores(request: Request, db: Session = Depends(get_db)):
    instrutores = instrutor_controller.InstrutorController.get_all(db)
    return templates.TemplateResponse(
        "instrutores/lista.html", {"request": request, "instrutores": instrutores}
    )


@app.get("/instrutor/{instrutor_id}")
async def instrutor_detail(
    request: Request, instrutor_id: int, db: Session = Depends(get_db)
):
    instrutor = instrutor_controller.InstrutorController.get_by_id(db, instrutor_id)
    if not instrutor:
        raise HTTPException(status_code=404, detail="Instrutor não encontrado")
    return templates.TemplateResponse(
        "instrutores/detalhe.html", {"request": request, "instrutor": instrutor}
    )


@app.post("/instrutor/criar")
async def create_instrutor(request: Request, db: Session = Depends(get_db)):
    form = await request.form()
    instrutor = instrutor_controller.InstrutorController.create(db, form)
    return templates.TemplateResponse(
        "instrutores/sucesso.html", {"request": request, "instrutor": instrutor}
    )


# Rotas para Administradores
@app.get("/administradores")
async def list_administradores(request: Request, db: Session = Depends(get_db)):
    administradores = administrador_controller.AdministradorController.get_all(db)
    return templates.TemplateResponse(
        "administradores/lista.html",
        {"request": request, "administradores": administradores},
    )


@app.get("/administrador/{administrador_id}")
async def administrador_detail(
    request: Request, administrador_id: int, db: Session = Depends(get_db)
):
    administrador = administrador_controller.AdministradorController.get_by_id(
        db, administrador_id
    )
    if not administrador:
        raise HTTPException(status_code=404, detail="Administrador não encontrado")
    return templates.TemplateResponse(
        "administradores/detalhe.html",
        {"request": request, "administrador": administrador},
    )


@app.post("/administrador/criar")
async def create_administrador(request: Request, db: Session = Depends(get_db)):
    form = await request.form()
    administrador = administrador_controller.AdministradorController.create(db, form)
    return templates.TemplateResponse(
        "administradores/sucesso.html",
        {"request": request, "administrador": administrador},
    )


# Rotas para Fichas de Treino
@app.get("/fichas")
async def list_fichas(request: Request, db: Session = Depends(get_db)):
    fichas = ficha_controller.FichaTreinoController.get_all(db)
    return templates.TemplateResponse(
        "fichas/lista.html", {"request": request, "fichas": fichas}
    )


@app.get("/ficha/{ficha_id}")
async def ficha_detail(request: Request, ficha_id: int, db: Session = Depends(get_db)):
    ficha = ficha_controller.FichaTreinoController.get_by_id(db, ficha_id)
    if not ficha:
        raise HTTPException(status_code=404, detail="Ficha não encontrada")
    return templates.TemplateResponse(
        "fichas/detalhe.html", {"request": request, "ficha": ficha}
    )


@app.post("/ficha/criar")
async def create_ficha(request: Request, db: Session = Depends(get_db)):
    form = await request.form()
    ficha = ficha_controller.FichaTreinoController.create(db, form)
    return templates.TemplateResponse(
        "fichas/sucesso.html", {"request": request, "ficha": ficha}
    )


# Rotas para Medidas Corporais
@app.get("/medidas")
async def list_medidas(request: Request, db: Session = Depends(get_db)):
    medidas = medidas_controller.MedidaCorporalController.get_all(db)
    return templates.TemplateResponse(
        "medidas/lista.html", {"request": request, "medidas": medidas}
    )


@app.get("/medida/{medida_id}")
async def medida_detail(
    request: Request, medida_id: int, db: Session = Depends(get_db)
):
    medida = medidas_controller.MedidaCorporalController.get_by_id(db, medida_id)
    if not medida:
        raise HTTPException(status_code=404, detail="Medida não encontrada")
    return templates.TemplateResponse(
        "medidas/detalhe.html", {"request": request, "medida": medida}
    )


@app.post("/medida/criar")
async def create_medida(request: Request, db: Session = Depends(get_db)):
    form = await request.form()
    medida = medidas_controller.MedidaCorporalController.create(db, form)
    return templates.TemplateResponse(
        "medidas/sucesso.html", {"request": request, "medida": medida}
    )
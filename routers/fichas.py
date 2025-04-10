from fastapi import APIRouter, Request, Form, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from datetime import date

from dao import database
from models.models import FichaTreino, DiaTreino, ExercicioTreino, Exercicio, Aluno
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/fichas/criar")
def form_criar_ficha(request: Request, db: Session = Depends(database.get_db), instrutor_id: int = 1):
    exercicios_raw = db.query(Exercicio).all()
    alunos = db.query(Aluno).all()

    exercicios = [
        {
            "id": ex.id,
            "nome": ex.nome,
            "grupo_muscular": ex.grupo_muscular or ""
        }
        for ex in exercicios_raw
    ]

    return templates.TemplateResponse("criar_ficha.html", {
        "request": request,
        "instrutor_id": instrutor_id,
        "exercicios": exercicios,
        "alunos": alunos  # adiciona todos os alunos no contexto
    })


@router.post("/fichas/criar")
async def criar_ficha(
    request: Request,
    db: Session = Depends(database.get_db),
    aluno_id: int = Form(...),
    instrutor_id: int = Form(...),
    # vai tratar os dias dinamicamente
):
    form = await request.form()
    dias_semana = ["Segunda", "Terca", "Quarta", "Quinta", "Sexta"]
    dia_para_numero = {dia: i + 1 for i, dia in enumerate(dias_semana)}

    # Cria ficha principal
    ficha = FichaTreino(
        aluno_id=aluno_id,
        instrutor_id=instrutor_id,
        data_inicio=date.today()
    )
    db.add(ficha)
    db.commit()
    db.refresh(ficha)

    for dia in dias_semana:
        exercicios_ids = form.getlist(f"exercicio_id_{dia}[]")
        series_list = form.getlist(f"series_{dia}[]")
        repeticoes_list = form.getlist(f"repeticoes_{dia}[]")

        if not exercicios_ids:
            continue

        dia_treino = DiaTreino(
            ficha_id=ficha.id,
            dia_semana=dia_para_numero[dia],
            nome_treino=f"Treino de {dia}",
            descricao=f"{len(exercicios_ids)} exercícios"
        )
        db.add(dia_treino)
        db.commit()
        db.refresh(dia_treino)

        for i in range(len(exercicios_ids)):
            exercicio_treino = ExercicioTreino(
                dia_treino_id=dia_treino.id,
                exercicio_id=int(exercicios_ids[i]),
                series=int(series_list[i]),
                repeticoes=repeticoes_list[i]
            )
            db.add(exercicio_treino)

    db.commit()

    return RedirectResponse(f"/instrutor/{instrutor_id}/dashboard", status_code=303)

@router.get("/fichas/{ficha_id}/editar")
def editar_ficha(ficha_id: int, request: Request, db: Session = Depends(database.get_db)):
    ficha = db.query(FichaTreino).filter(FichaTreino.id == ficha_id).first()
    if not ficha:
        raise HTTPException(status_code=404, detail="Ficha não encontrada")

    exercicios = db.query(Exercicio).all()  # Para o select de exercícios

    return templates.TemplateResponse("editar_ficha.html", {
        "request": request,
        "ficha": ficha,
        "exercicios": exercicios
    })

@router.post("/fichas/{ficha_id}/editar")
async def salvar_edicao_ficha(ficha_id: int, request: Request, db: Session = Depends(database.get_db)):
    form = await request.form()
    ficha = db.query(FichaTreino).filter(FichaTreino.id == ficha_id).first()

    if not ficha:
        raise HTTPException(status_code=404, detail="Ficha não encontrada")

    for dia in ficha.dias:
        # Apaga todos os exercícios antigos daquele dia
        db.query(ExercicioTreino).filter(ExercicioTreino.dia_treino_id == dia.id).delete()

        # Adiciona os novos
        exercicios_ids = form.getlist(f"exercicio_id_{dia.id}[]")
        series_list = form.getlist(f"series_{dia.id}[]")
        repeticoes_list = form.getlist(f"repeticoes_{dia.id}[]")

        for i in range(len(exercicios_ids)):
            novo = ExercicioTreino(
                dia_treino_id=dia.id,
                exercicio_id=int(exercicios_ids[i]),
                series=int(series_list[i]),
                repeticoes=repeticoes_list[i]
            )
            db.add(novo)

    db.commit()

    return RedirectResponse(f"/instrutor/{ficha.instrutor_id}/dashboard", status_code=303)


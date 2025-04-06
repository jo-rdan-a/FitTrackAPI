from fastapi import APIRouter, Depends, Request, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.aluno import Aluno
from dao.aluno_dao import AlunoDAO
from fastapi.templating import Jinja2Templates

router = APIRouter()

# Configuração do Jinja2 para templates
templates = Jinja2Templates(directory="app/templates")

# Rota para criar um aluno
@router.post("/alunos/")
def create_aluno(aluno: Aluno, db: Session = Depends(get_db)):
    return AlunoDAO.create(db, aluno)

# Rota para obter um aluno específico pelo ID
@router.get("/alunos/{aluno_id}")
def get_aluno(aluno_id: int, db: Session = Depends(get_db)):
    return AlunoDAO.get_by_id(db, aluno_id)

# Rota para obter todos os alunos
@router.get("/alunos")
def get_all_alunos(db: Session = Depends(get_db)):
    return AlunoDAO.get_all(db)

# Rota para excluir um aluno pelo ID
@router.delete("/alunos/{aluno_id}")
def delete_aluno(aluno_id: int, db: Session = Depends(get_db)):
    return AlunoDAO.delete(db, aluno_id)

# Rota para listar todos os alunos no formato HTML
@router.get("/alunos/view")
async def list_alunos(request: Request, db: Session = Depends(get_db)):
    alunos = get_all_alunos(db)
    return templates.TemplateResponse(
        "alunos/lista.html", {"request": request, "alunos": alunos}
    )

# Rota para ver o detalhe de um aluno específico
@router.get("/aluno/{aluno_id}/view")
async def aluno_detail(request: Request, aluno_id: int, db: Session = Depends(get_db)):
    aluno = get_aluno(aluno_id, db)
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return templates.TemplateResponse(
        "alunos/detalhe.html", {"request": request, "aluno": aluno}
    )

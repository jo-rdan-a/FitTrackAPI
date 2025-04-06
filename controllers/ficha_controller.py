from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models.ficha import FichaTreino
from dao.ficha_dao import FichaTreinoDAO

router = APIRouter()

@router.post("/fichas/")
def create_ficha(ficha: FichaTreino, db: Session = Depends(get_db)):
    return FichaTreinoDAO.create(db, ficha)


@router.get("/fichas/{ficha_id}")
def get_ficha(ficha_id: int, db: Session = Depends(get_db)):
    return FichaTreinoDAO.get_by_id(db, ficha_id)


@router.get("/fichas/")
def get_all_fichas(db: Session = Depends(get_db)):
    return FichaTreinoDAO.get_all(db)


@router.delete("/fichas/{ficha_id}")
def delete_ficha(ficha_id: int, db: Session = Depends(get_db)):
    return FichaTreinoDAO.delete(db, ficha_id)
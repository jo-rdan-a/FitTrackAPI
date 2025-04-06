from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models.instrutor import Instrutor
from dao.instrutor_dao import InstrutorDAO

router = APIRouter()

@router.post("/instrutores/")
def create_instrutor(instrutor: Instrutor, db: Session = Depends(get_db)):
    return InstrutorDAO.create(db, instrutor)


@router.get("/instrutores/{instrutor_id}")
def get_instrutor(instrutor_id: int, db: Session = Depends(get_db)):
    return InstrutorDAO.get_by_id(db, instrutor_id)


@router.get("/instrutores/")
def get_all_instrutores(db: Session = Depends(get_db)):
    return InstrutorDAO.get_all(db)


@router.delete("/instrutores/{instrutor_id}")
def delete_instrutor(instrutor_id: int, db: Session = Depends(get_db)):
    return InstrutorDAO.delete(db, instrutor_id)
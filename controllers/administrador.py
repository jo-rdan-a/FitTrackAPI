from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models.administrador import Administrador
from dao.administrador_dao import AdministradorDAO

router = APIRouter()

@router.post("/administradores/")
def create_administrador(administrador: Administrador, db: Session = Depends(get_db)):
    return AdministradorDAO.create(db, administrador)


@router.get("/administradores/{administrador_id}")
def get_administrador(administrador_id: int, db: Session = Depends(get_db)):
    return AdministradorDAO.get_by_id(db, administrador_id)


@router.get("/administradores/")
def get_all_administradores(db: Session = Depends(get_db)):
    return AdministradorDAO.get_all(db)


@router.delete("/administradores/{administrador_id}")
def delete_administrador(administrador_id: int, db: Session = Depends(get_db)):
    return AdministradorDAO.delete(db, administrador_id)
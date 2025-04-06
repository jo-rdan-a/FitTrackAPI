from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models.medidas import MedidaCorporal
from dao.medidas_dao import MedidaCorporalDAO

router = APIRouter()

@router.post("/medidas/")
def create_medida(medida: MedidaCorporal, db: Session = Depends(get_db)):
    return MedidaCorporalDAO.create(db, medida)


@router.get("/medidas/{medida_id}")
def get_medida(medida_id: int, db: Session = Depends(get_db)):
    return MedidaCorporalDAO.get_by_id(db, medida_id)


@router.get("/medidas/")
def get_all_medidas(db: Session = Depends(get_db)):
    return MedidaCorporalDAO.get_all(db)


@router.delete("/medidas/{medida_id}")
def delete_medida(medida_id: int, db: Session = Depends(get_db)):
    return MedidaCorporalDAO.delete(db, medida_id)

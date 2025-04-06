from sqlalchemy.orm import Session
from models.ficha import FichaTreino

class FichaTreinoDAO:
    @staticmethod
    def create(db: Session, ficha: FichaTreino):
        db.add(ficha)
        db.commit()
        db.refresh(ficha)
        return ficha

    @staticmethod
    def get_by_id(db: Session, ficha_id: int):
        return db.query(FichaTreino).filter(FichaTreino.id == ficha_id).first()

    @staticmethod
    def get_all(db: Session):
        return db.query(FichaTreino).all()

    @staticmethod
    def delete(db: Session, ficha_id: int):
        ficha = db.query(FichaTreino).filter(FichaTreino.id == ficha_id).first()
        if ficha:
            db.delete(ficha)
            db.commit()
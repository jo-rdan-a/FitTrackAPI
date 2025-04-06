from sqlalchemy.orm import Session
from models.medidas import MedidaCorporal

class MedidaCorporalDAO:
    @staticmethod
    def create(db: Session, medida: MedidaCorporal):
        db.add(medida)
        db.commit()
        db.refresh(medida)
        return medida

    @staticmethod
    def get_by_id(db: Session, medida_id: int):
        return db.query(MedidaCorporal).filter(MedidaCorporal.id == medida_id).first()

    @staticmethod
    def get_all(db: Session):
        return db.query(MedidaCorporal).all()

    @staticmethod
    def delete(db: Session, medida_id: int):
        medida = db.query(MedidaCorporal).filter(MedidaCorporal.id == medida_id).first()
        if medida:
            db.delete(medida)
            db.commit()
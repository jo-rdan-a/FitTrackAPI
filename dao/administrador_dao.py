from sqlalchemy.orm import Session
from models.administrador import Administrador

class AdministradorDAO:
    @staticmethod
    def create(db: Session, administrador: Administrador):
        db.add(administrador)
        db.commit()
        db.refresh(administrador)
        return administrador

    @staticmethod
    def get_by_id(db: Session, administrador_id: int):
        return (
            db.query(Administrador).filter(Administrador.id == administrador_id).first()
        )

    @staticmethod
    def get_all(db: Session):
        return db.query(Administrador).all()

    @staticmethod
    def delete(db: Session, administrador_id: int):
        administrador = (
            db.query(Administrador).filter(Administrador.id == administrador_id).first()
        )
        if administrador:
            db.delete(administrador)
            db.commit()
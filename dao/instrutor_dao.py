from sqlalchemy.orm import Session
from models.instrutor import Instrutor

class InstrutorDAO:
    @staticmethod
    def create(db: Session, instrutor: Instrutor):
        db.add(instrutor)
        db.commit()
        db.refresh(instrutor)
        return instrutor

    @staticmethod
    def get_by_id(db: Session, instrutor_id: int):
        return db.query(Instrutor).filter(Instrutor.id == instrutor_id).first()

    @staticmethod
    def get_all(db: Session):
        return db.query(Instrutor).all()

    @staticmethod
    def delete(db: Session, instrutor_id: int):
        instrutor = db.query(Instrutor).filter(Instrutor.id == instrutor_id).first()
        if instrutor:
            db.delete(instrutor)
            db.commit()
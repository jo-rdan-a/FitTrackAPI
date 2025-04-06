from sqlalchemy.orm import Session
from models.aluno import Aluno

class AlunoDAO:
    @staticmethod
    def create(db: Session, aluno: Aluno):
        db.add(aluno)
        db.commit()
        db.refresh(aluno)
        return aluno

    @staticmethod
    def get_by_id(db: Session, aluno_id: int):
        return db.query(Aluno).filter(Aluno.id == aluno_id).first()

    @staticmethod
    def get_all(db: Session):
        return db.query(Aluno).all()

    @staticmethod
    def delete(db: Session, aluno_id: int):
        aluno = db.query(Aluno).filter(Aluno.id == aluno_id).first()
        if aluno:
            db.delete(aluno)
            db.commit()
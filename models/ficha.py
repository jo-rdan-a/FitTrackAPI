from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class FichaTreino(Base):
    __tablename__ = "fichas_treino"

    id = Column(Integer, primary_key=True, index=True)
    aluno_id = Column(Integer, ForeignKey("alunos.id"), nullable=False)
    instrutor_id = Column(Integer, ForeignKey("instrutores.id"), nullable=False)
    aluno = relationship("Aluno", back_populates="fichas")
    instrutor = relationship("Instrutor", back_populates="fichas")
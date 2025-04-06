from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from database import Base


# Model de Aluno
class Aluno(Base):
    __tablename__ = "alunos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    telefone = Column(String, nullable=True)
    data_nascimento = Column(Date, nullable=False)
    medidas = relationship("MedidaCorporal", back_populates="aluno")
    fichas = relationship("FichaTreino", back_populates="aluno")

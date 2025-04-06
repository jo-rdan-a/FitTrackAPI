from sqlalchemy import Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from database import Base

class MedidaCorporal(Base):
    __tablename__ = "medidas_corporais"

    id = Column(Integer, primary_key=True, index=True)
    aluno_id = Column(Integer, ForeignKey("alunos.id"), nullable=False)
    peso = Column(Float, nullable=False)
    altura = Column(Float, nullable=False)
    circunferencia_torax = Column(Float, nullable=True)
    circunferencia_abdomen = Column(Float, nullable=True)
    circunferencia_quadril = Column(Float, nullable=True)
    aluno = relationship("Aluno", back_populates="medidas")

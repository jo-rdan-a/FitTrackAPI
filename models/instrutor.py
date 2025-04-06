from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

# Model de Instrutor
class Instrutor(Base):
    __tablename__ = "instrutores"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    telefone = Column(String, nullable=True)
    especializacao = Column(String, nullable=True)
    fichas = relationship("FichaTreino", back_populates="instrutor")

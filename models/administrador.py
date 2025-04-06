from sqlalchemy import Column, Integer, String
from database import Base

# Model de Administrador
class Administrador(Base):
    __tablename__ = "administradores"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)


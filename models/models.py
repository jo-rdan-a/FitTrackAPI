from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Text
from sqlalchemy.orm import relationship
from dao.database import Base

class Aluno(Base):
    __tablename__ = "alunos"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)
    senha = Column(String, nullable=False)
    idade = Column(String, nullable=False)
    objetivo = Column(String, nullable=False)
    telefone = Column(String)
    data_nascimento = Column(Date)

    medidas = relationship("Medida", back_populates="aluno")
    fichas = relationship("FichaTreino", back_populates="aluno")

class Instrutor(Base):
    __tablename__ = "instrutores"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)
    senha = Column(String, nullable=False)
    telefone = Column(String)
    especializacao = Column(String)

    fichas_montadas = relationship("FichaTreino", back_populates="instrutor")

class Medida(Base):
    __tablename__ = "medidas"
    id = Column(Integer, primary_key=True, index=True)
    aluno_id = Column(Integer, ForeignKey("alunos.id"))
    data = Column(Date)
    peso = Column(Float)
    altura = Column(Float)
    cintura = Column(Float)
    quadril = Column(Float)
    torax = Column(Float)

    aluno = relationship("Aluno", back_populates="medidas")

class FichaTreino(Base):
    __tablename__ = "ficha_treino"
    id = Column(Integer, primary_key=True, index=True)
    aluno_id = Column(Integer, ForeignKey("alunos.id"))
    instrutor_id = Column(Integer, ForeignKey("instrutores.id"))
    data_inicio = Column(Date)

    aluno = relationship("Aluno", back_populates="fichas")
    instrutor = relationship("Instrutor", back_populates="fichas_montadas")
    dias = relationship("DiaTreino", back_populates="ficha", cascade="all, delete")


class DiaTreino(Base):
    __tablename__ = "dias_treino"
    id = Column(Integer, primary_key=True, index=True)
    ficha_id = Column(Integer, ForeignKey("ficha_treino.id"))
    dia_semana = Column(Integer)  # 1=Segunda, 2=Terça...
    nome_treino = Column(String)
    descricao = Column(String)

    ficha = relationship("FichaTreino", back_populates="dias")
    exercicios_treino = relationship("ExercicioTreino", back_populates="dia", cascade="all, delete")


class Exercicio(Base):
    __tablename__ = "exercicios"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    grupo_muscular = Column(String)

    exercicios_treino = relationship("ExercicioTreino", back_populates="exercicio")


class ExercicioTreino(Base):
    __tablename__ = "exercicios_treino"
    id = Column(Integer, primary_key=True, index=True)
    dia_treino_id = Column(Integer, ForeignKey("dias_treino.id"))
    exercicio_id = Column(Integer, ForeignKey("exercicios.id"))
    series = Column(Integer)
    repeticoes = Column(String)

    dia = relationship("DiaTreino", back_populates="exercicios_treino")
    exercicio = relationship("Exercicio", back_populates="exercicios_treino")
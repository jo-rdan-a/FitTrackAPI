from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session

# URL de conexão com o banco de dados (substitua com os dados do seu banco)
SQLALCHEMY_DATABASE_URL = (
    "mysql+pymysql://usuario:senha@localhost:3306/monitoramento_treino"
)

# Criação do objeto engine para conexão
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True, pool_size=20, max_overflow=0)

# Base de dados para criação de modelos
Base: DeclarativeMeta = declarative_base()

# SessionLocal é uma classe que cria uma instância de sessão
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Função para obter a sessão de banco de dados
def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

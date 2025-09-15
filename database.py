import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# --- Configuração do banco ---

# String de conexão usando variáveis de ambiente
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# String de conexão do SQLAlchemy
DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Engine
engine = create_engine(DATABASE_URL)

# Sessão
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os models
Base = declarative_base()

def get_db():
    """
    Função utilitária para obter uma sessão de banco de dados.
    Ideal para uso com geradores em frameworks como o FastAPI.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
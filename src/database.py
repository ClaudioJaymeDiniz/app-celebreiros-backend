from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL de conexão com o SQLite
DATABASE_URL = "sqlite:///./celebreiros.db"

# Criar a engine de conexão
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False}, echo=True)

# Configurar a sessão
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os modelos
Base = declarative_base()

# Função para criar as tabelas
def create_tables():
    Base.metadata.create_all(bind=engine)

# Função para gerenciar a sessão do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
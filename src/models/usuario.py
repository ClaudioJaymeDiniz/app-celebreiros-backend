from sqlalchemy import Column, Integer, String, DateTime
from src.database import Base
from datetime import datetime

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False, index=True)
    senha = Column(String, nullable=False)
    nivel_acesso = Column(String, nullable=False)
    data_criacao = Column(DateTime, default=datetime.utcnow)
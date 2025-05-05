from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from src.database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False, index=True)
    senha = Column(String, nullable=False)
    nivel_acesso = Column(String, nullable=False)
    data_criacao = Column(DateTime, default=datetime.now)

    # Relacionamento com os resultados dos quizzes
    resultados = relationship("QuizResultado", back_populates="usuario")
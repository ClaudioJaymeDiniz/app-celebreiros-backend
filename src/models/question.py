from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from src.database import Base

class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    aula = Column(String, nullable=False)
    pergunta = Column(String, nullable=False)
    alternativa_a = Column(String, nullable=False)
    alternativa_b = Column(String, nullable=False)
    alternativa_c = Column(String, nullable=False)
    alternativa_d = Column(String, nullable=False)
    resposta_correta = Column(String, nullable=False)
    data_criacao = Column(DateTime, default=datetime.now)
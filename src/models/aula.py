from sqlalchemy import Column, Integer, String, DateTime
from src.database import Base
from datetime import datetime

class Aula(Base):
    __tablename__ = "aulas"
    
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    video_url = Column(String, nullable=False)
    data_criacao = Column(DateTime, default=datetime.utcnow)
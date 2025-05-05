from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from src.database import Base

class QuizResultado(Base):
    __tablename__ = "quiz_resultados"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    aula = Column(String, nullable=False)
    acertos = Column(Integer, nullable=False)
    total_questoes = Column(Integer, nullable=False)
    data_realizacao = Column(DateTime, default=datetime.utcnow)

    # Relacionamento com o usuário
    usuario = relationship("Usuario", back_populates="resultados")
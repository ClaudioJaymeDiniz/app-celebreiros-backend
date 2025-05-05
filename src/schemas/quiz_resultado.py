from pydantic import BaseModel
from datetime import datetime

class QuizResultadoCreate(BaseModel):
    aula: str
    acertos: int
    total_questoes: int

class QuizResultadoResponse(QuizResultadoCreate):
    id: int
    usuario_id: int
    data_realizacao: datetime

    class Config:
        from_attributes = True
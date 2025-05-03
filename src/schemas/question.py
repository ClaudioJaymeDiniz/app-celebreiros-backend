from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class QuestionCreateInput(BaseModel):
    aula: str
    pergunta: str
    alternativa_a: str
    alternativa_b: str
    alternativa_c: str
    alternativa_d: str
    resposta_correta: str  # Pode ser 'A', 'B', 'C' ou 'D'

class QuestionCreate(BaseModel):
    aula: str
    pergunta: str
    alternativa_a: str
    alternativa_b: str
    alternativa_c: str
    alternativa_d: str
    resposta_correta: str
    data_criacao: datetime = datetime.now()

class QuestionResponse(BaseModel):
    id: int
    aula: str
    pergunta: str
    alternativa_a: str
    alternativa_b: str
    alternativa_c: str
    alternativa_d: str
    data_criacao: datetime

    class Config:
        orm_mode = True

class QuestionUpdate(BaseModel):
    aula: Optional[str] = None
    pergunta: Optional[str] = None
    alternativa_a: Optional[str] = None
    alternativa_b: Optional[str] = None
    alternativa_c: Optional[str] = None
    alternativa_d: Optional[str] = None
    resposta_correta: Optional[str] = None
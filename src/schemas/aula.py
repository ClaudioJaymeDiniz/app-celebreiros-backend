from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List
from src.schemas.question import QuestionResponse

class AulaBase(BaseModel):
    titulo: str
    video_url: str

class AulaCreate(AulaBase):
    pass

class AulaResponse(AulaBase):
    id: int
    data_criacao: datetime
    questoes: List[QuestionResponse] = []

    class Config:
        orm_mode = True
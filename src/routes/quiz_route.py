from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.database import get_db
from src.models.quiz_resultado import QuizResultado
from src.schemas.quiz_resultado import QuizResultadoCreate, QuizResultadoResponse
from src.auth.auth import get_current_user
from typing import List

router = APIRouter()

@router.post("/quiz/resultado", response_model=QuizResultadoResponse)
async def registrar_resultado_quiz(
    resultado: QuizResultadoCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """Registra o resultado de um quiz realizado pelo usuário"""
    novo_resultado = QuizResultado(
        usuario_id=current_user.id,
        aula=resultado.aula,
        acertos=resultado.acertos,
        total_questoes=resultado.total_questoes
    )
    db.add(novo_resultado)
    db.commit()
    db.refresh(novo_resultado)
    return novo_resultado

@router.get("/quiz/resultados/usuario", response_model=List[QuizResultadoResponse])
async def listar_resultados_usuario(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """Lista todos os resultados dos quizzes do usuário logado"""
    return db.query(QuizResultado).filter(QuizResultado.usuario_id == current_user.id).all()
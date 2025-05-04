from fastapi import APIRouter, Depends, HTTPException
from src.auth.dependencies import verificar_admin
from sqlalchemy.orm import Session
from src.database import get_db
from src.models.question import Question
from src.schemas.question import QuestionCreateInput, QuestionResponse, QuestionUpdate  
from datetime import datetime, timezone
from typing import List

router = APIRouter()

@router.post("/questoes", response_model=QuestionResponse)
async def criar_questao(
    questao: QuestionCreateInput,
    db: Session = Depends(get_db),
    admin = Depends(verificar_admin)
):
    nova_questao = Question(
        aula=questao.aula,
        pergunta=questao.pergunta,
        alternativa_a=questao.alternativa_a,
        alternativa_b=questao.alternativa_b,
        alternativa_c=questao.alternativa_c,
        alternativa_d=questao.alternativa_d,
        resposta_correta=questao.resposta_correta,
        data_criacao=datetime.now(timezone.utc)  # Fixed timezone usage
    )
    
    db.add(nova_questao)
    db.commit()
    db.refresh(nova_questao)
    return nova_questao

@router.get("/questoes", response_model=List[QuestionResponse])
async def listar_questoes(db: Session = Depends(get_db)):
    """Lista todas as questões cadastradas"""
    return db.query(Question).all()

@router.get("/questoes/aula/{aula}", response_model=List[QuestionResponse])
async def listar_questoes_por_aula(aula: str, db: Session = Depends(get_db)):
    """Lista todas as questões de uma aula específica"""
    questoes = db.query(Question).filter(Question.aula == aula).all()
    if not questoes:
        raise HTTPException(status_code=404, detail=f"Nenhuma questão encontrada para a aula {aula}")
    return questoes

@router.put("/questoes/{questao_id}", response_model=QuestionResponse)
async def atualizar_questao(
    questao_id: int,
    questao: QuestionUpdate,  # Alterado para QuestionUpdate
    db: Session = Depends(get_db),
    admin = Depends(verificar_admin)
):
    """Atualiza uma questão existente"""
    db_questao = db.query(Question).filter(Question.id == questao_id).first()
    if not db_questao:
        raise HTTPException(status_code=404, detail="Questão não encontrada")
    
    # Atualiza apenas os campos que foram fornecidos
    questao_data = questao.dict(exclude_unset=True)
    for key, value in questao_data.items():
        setattr(db_questao, key, value)
    
    db.commit()
    db.refresh(db_questao)
    return db_questao

@router.delete("/questoes/{questao_id}")
async def deletar_questao(
    questao_id: int,
    db: Session = Depends(get_db),
    admin = Depends(verificar_admin)
):
    """Deleta uma questão"""
    questao = db.query(Question).filter(Question.id == questao_id).first()
    if not questao:
        raise HTTPException(status_code=404, detail="Questão não encontrada")
    
    db.delete(questao)
    db.commit()
    return {"message": f"Questão {questao_id} deletada com sucesso"}
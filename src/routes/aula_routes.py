from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.database import get_db
from src.models.aula import Aula
from src.schemas.aula import AulaCreate, AulaResponse
from src.auth.dependencies import verificar_admin
from typing import List
from datetime import datetime, timezone

router = APIRouter()

@router.post("/aulas", response_model=AulaResponse)
async def criar_aula(
    aula: AulaCreate,
    db: Session = Depends(get_db),
    admin = Depends(verificar_admin)
):
    """Cria uma nova aula"""
    nova_aula = Aula(
        titulo=aula.titulo,
        video_url=aula.video_url,
        data_criacao=datetime.now(timezone.utc)
    )
    
    db.add(nova_aula)
    db.commit()
    db.refresh(nova_aula)
    return nova_aula

@router.get("/aulas", response_model=List[AulaResponse])
async def listar_aulas(db: Session = Depends(get_db)):
    """Lista todas as aulas cadastradas"""
    return db.query(Aula).all()

@router.get("/aulas/{aula_id}", response_model=AulaResponse)
async def obter_aula(aula_id: int, db: Session = Depends(get_db)):
    """Obtém uma aula específica pelo ID"""
    aula = db.query(Aula).filter(Aula.id == aula_id).first()
    if not aula:
        raise HTTPException(status_code=404, detail="Aula não encontrada")
    return aula

@router.put("/aulas/{aula_id}", response_model=AulaResponse)
async def atualizar_aula(
    aula_id: int,
    aula: AulaCreate,
    db: Session = Depends(get_db),
    admin = Depends(verificar_admin)
):
    """Atualiza uma aula existente"""
    db_aula = db.query(Aula).filter(Aula.id == aula_id).first()
    if not db_aula:
        raise HTTPException(status_code=404, detail="Aula não encontrada")
    
    db_aula.titulo = aula.titulo
    db_aula.video_url = aula.video_url
    
    db.commit()
    db.refresh(db_aula)
    return db_aula

@router.delete("/aulas/{aula_id}")
async def deletar_aula(
    aula_id: int,
    db: Session = Depends(get_db),
    admin = Depends(verificar_admin)
):
    """Deleta uma aula"""
    aula = db.query(Aula).filter(Aula.id == aula_id).first()
    if not aula:
        raise HTTPException(status_code=404, detail="Aula não encontrada")
    
    db.delete(aula)
    db.commit()
    return {"message": f"Aula {aula_id} deletada com sucesso"}
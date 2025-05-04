from fastapi import Depends, HTTPException, status
from src.auth.auth import get_current_user
from src.schemas.usuario import NivelAcesso

async def verificar_admin(current_user = Depends(get_current_user)):
    if current_user.nivel_acesso != NivelAcesso.ADMIN:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Acesso negado. Apenas administradores podem acessar este recurso."
        )
    return current_user
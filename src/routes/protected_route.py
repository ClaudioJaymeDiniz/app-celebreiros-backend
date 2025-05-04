from fastapi import APIRouter, Depends
from src.auth.auth import get_current_user
from src.schemas.usuario import UsuarioResponse
from src.models.usuario import Usuario

router = APIRouter()

@router.get("/me", response_model=UsuarioResponse)
async def read_users_me(current_user: Usuario = Depends(get_current_user)):
    return current_user
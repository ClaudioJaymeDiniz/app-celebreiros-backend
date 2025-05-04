from fastapi import FastAPI
from pydantic import EmailStr
from src.database import get_db, create_tables
from src.auth.admin import criar_admin_se_nao_existe
from src.routes import auth, question_routes, protected_route

app = FastAPI()

# Create database tables on startup
create_tables()

# Criar tabelas e admin na inicialização
@app.on_event("startup")
async def startup_event():
    db = next(get_db())
    criar_admin_se_nao_existe(db)

# Incluir as rotas
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(question_routes.router, prefix="/api", tags=["questions"])
app.include_router(protected_route.router, prefix="/api", tags=["user"])

@app.get("/")
async def root():
    return {"Acesse localhost:8000/docs"}
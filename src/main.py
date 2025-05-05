from fastapi import FastAPI
from pydantic import EmailStr
from src.database import get_db, create_tables
from src.auth.admin import criar_admin_se_nao_existe
from src.routes import auth, question_routes, protected_route, quiz_route, aula_routes
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configuração do CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, substitua por uma lista de origens permitidas
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
app.include_router(quiz_route.router, prefix="/api", tags=["quiz"])
app.include_router(aula_routes.router, prefix="/api", tags=["aulas"])

@app.get("/")
async def root():
    return {"Acesse localhost:8000/docs"}